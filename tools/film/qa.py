#!/usr/bin/env python3
"""Delivery check for a finished film. Measures; does not judge taste.

    /opt/film-studio/venv/bin/python tools/film/qa.py FILM.mp4 [--expect-size 3840x2160] [--expect-fps 24]
        [--expect-frames 192] [--lufs -14] [--sheet sheet.jpg] [--columns 6] [--json report.json]

Checks: container facts from ffprobe, exact frame count, picture and sound length agree,
no black or frozen stretches that were not planned (--allow-black S, --allow-freeze S),
integrated loudness within 1 LU of the target and true peak under -1 dBTP, brightness flicker
(frame-to-frame change in mean luma that stands out from its neighbours), and it writes a
contact sheet of evenly spaced frames to LOOK at. Exit code 0 = every check passed.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys

import cv2
import numpy as np


def run(command: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(command, capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("film")
    parser.add_argument("--expect-size")
    parser.add_argument("--expect-fps", type=float)
    parser.add_argument("--expect-frames", type=int)
    parser.add_argument("--lufs", type=float, default=-14.0)
    parser.add_argument("--allow-black", type=float, default=0.0, help="seconds of black allowed (fades)")
    parser.add_argument("--allow-freeze", type=float, default=0.0, help="seconds of frozen picture allowed (holds)")
    parser.add_argument("--sheet")
    parser.add_argument("--columns", type=int, default=6)
    parser.add_argument("--rows", type=int, default=4)
    parser.add_argument("--json")
    args = parser.parse_args()

    probe = json.loads(run(["ffprobe", "-v", "error", "-count_frames", "-show_streams", "-show_format", "-of", "json", args.film]).stdout)
    video = next(s for s in probe["streams"] if s["codec_type"] == "video")
    audio = next((s for s in probe["streams"] if s["codec_type"] == "audio"), None)
    num, den = (int(v) for v in video["avg_frame_rate"].split("/"))
    fps = num / den
    frames = int(video.get("nb_read_frames") or video.get("nb_frames"))
    report = {"file": args.film, "video": {"codec": video["codec_name"], "size": f"{video['width']}x{video['height']}", "fps": round(fps, 3),
              "frames": frames, "seconds": round(frames / fps, 3), "pix_fmt": video.get("pix_fmt"),
              "colour": [video.get("color_primaries"), video.get("color_transfer"), video.get("color_space")]},
              "megabytes": round(int(probe["format"]["size"]) / 1e6, 1), "checks": []}
    checks = report["checks"]

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "ok": bool(ok), "detail": detail})

    if args.expect_size:
        check("size", report["video"]["size"] == args.expect_size, f"{report['video']['size']} (expected {args.expect_size})")
    if args.expect_fps:
        check("frame rate", abs(fps - args.expect_fps) < 0.01, f"{fps:.3f} fps (expected {args.expect_fps})")
    if args.expect_frames:
        check("frame count", frames == args.expect_frames, f"{frames} (expected {args.expect_frames})")
    check("colour tags", report["video"]["colour"] == ["bt709"] * 3, str(report["video"]["colour"]))

    if audio:
        seconds = float(audio.get("duration") or probe["format"]["duration"])
        report["audio"] = {"codec": audio["codec_name"], "rate": int(audio["sample_rate"]), "channels": audio["channels"], "seconds": round(seconds, 3)}
        check("sound and picture length", abs(seconds - frames / fps) <= 2.5 / fps, f"sound {seconds:.3f} s, picture {frames / fps:.3f} s")
        loud = run(["ffmpeg", "-nostats", "-i", args.film, "-map", "0:a:0", "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
        integrated = re.findall(r"I:\s+(-?[\d.]+) LUFS", loud)
        peak = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", loud)
        if integrated:
            report["audio"].update(lufs=float(integrated[-1]), true_peak=float(peak[-1]) if peak else None)
            check("loudness", abs(float(integrated[-1]) - args.lufs) <= 1.0, f"{integrated[-1]} LUFS (target {args.lufs})")
            if peak:
                check("true peak", float(peak[-1]) <= -0.9, f"{peak[-1]} dBTP (limit -1)")
    else:
        check("sound", False, "no audio stream")

    detect = run(["ffmpeg", "-nostats", "-i", args.film, "-map", "0:v:0", "-vf", "blackdetect=d=0.2:pix_th=0.05,freezedetect=n=0.0008:d=0.5",
                  "-f", "null", "-"]).stderr
    black = sum(float(v) for v in re.findall(r"black_duration:([\d.]+)", detect))
    freeze = sum(float(v) for v in re.findall(r"freeze_duration: ([\d.]+)", detect))
    check("black", black <= args.allow_black + 1e-6, f"{black:.2f} s black (allowed {args.allow_black})")
    check("frozen picture", freeze <= args.allow_freeze + 1e-6, f"{freeze:.2f} s frozen (allowed {args.allow_freeze})")

    # Brightness per frame from a small greyscale copy: fast, and enough to see flicker.
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", args.film, "-map", "0:v:0", "-vf", "scale=160:90,format=gray", "-f", "rawvideo", "-"],
                         capture_output=True).stdout
    luma = np.frombuffer(raw, np.uint8).reshape(-1, 90, 160).astype(np.float32).mean(axis=(1, 2)) / 255.0
    change = np.abs(np.diff(luma))
    # A flicker frame differs from BOTH neighbours while they agree with each other.
    spikes = [int(i) for i in range(1, len(luma) - 1)
              if abs(luma[i] - luma[i - 1]) > 0.012 and abs(luma[i] - luma[i + 1]) > 0.012 and abs(luma[i + 1] - luma[i - 1]) < 0.006]
    report["luma"] = {"min": round(float(luma.min()), 3), "max": round(float(luma.max()), 3), "largest_step": round(float(change.max()), 3)}
    check("flicker", not spikes, f"{len(spikes)} single-frame brightness spikes" + (f" at frames {spikes[:8]}" if spikes else ""))

    if args.sheet:
        count = args.columns * args.rows
        picks = np.linspace(0, frames - 1, count).round().astype(int)
        capture = cv2.VideoCapture(args.film)
        tiles = []
        for index in picks:
            capture.set(cv2.CAP_PROP_POS_FRAMES, int(index))
            ok, image = capture.read()
            if not ok:
                continue
            tile = cv2.resize(image, (480, round(480 * image.shape[0] / image.shape[1])), interpolation=cv2.INTER_AREA)
            cv2.putText(tile, f"{index / fps:5.2f}s  f{index + 1}", (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
            tiles.append(tile)
        rows = [np.hstack(tiles[r * args.columns:(r + 1) * args.columns]) for r in range(len(tiles) // args.columns)]
        cv2.imwrite(args.sheet, np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 88])
        report["sheet"] = args.sheet

    passed = all(c["ok"] for c in checks)
    report["result"] = "PASS" if passed else "FAIL"
    print(f"{report['video']['size']} {report['video']['codec']} {report['video']['fps']} fps, {frames} frames, {report['megabytes']} MB")
    for c in checks:
        print(f"{'ok  ' if c['ok'] else 'FAIL'}  {c['name']}: {c['detail']}")
    print("RESULT:", report["result"])
    if args.json:
        with open(args.json, "w") as handle:
            json.dump(report, handle, indent=1)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
