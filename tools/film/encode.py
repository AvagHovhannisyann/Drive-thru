#!/usr/bin/env python3
"""Frames + sound -> delivery file.

    python3 tools/film/encode.py OUT.mp4 --fps 24 --frames "frames/s1_*.png" "frames/s2_*.png"
            [--audio mix.wav] [--preset h264|hevc10|prores] [--size 3840x2160] [--crf 16]

Frame patterns are taken in the order given and, within a pattern, in name order, so each shot can
write its own numbered files. Standard library + ffmpeg. Presets:
  h264    8-bit H.264 High, yuv420p, BT.709 tags, faststart: plays everywhere (default)
  hevc10  10-bit H.265, smaller files for 4K; needs a recent player
  prores  ProRes 422 HQ master (.mov) for further editing
"""

import argparse
import glob
import os
import subprocess
import sys
import tempfile

PRESETS = {
    "h264": ["-c:v", "libx264", "-preset", "slow", "-pix_fmt", "yuv420p", "-profile:v", "high"],
    "hevc10": ["-c:v", "libx265", "-preset", "medium", "-pix_fmt", "yuv420p10le", "-tag:v", "hvc1"],
    "prores": ["-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le", "-vendor", "apl0"],
}
BT709 = ["-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-color_range", "tv"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("out")
    parser.add_argument("--frames", nargs="+", required=True)
    parser.add_argument("--fps", type=float, default=24)
    parser.add_argument("--audio")
    parser.add_argument("--preset", choices=PRESETS, default="h264")
    parser.add_argument("--crf", type=int)
    parser.add_argument("--size", help="WxH: scale with Lanczos (for delivery sizes other than the frames)")
    args = parser.parse_args()

    files = [name for pattern in args.frames for name in sorted(glob.glob(pattern))]
    if not files:
        print("no frames match", args.frames)
        return 1
    with tempfile.TemporaryDirectory(dir=os.path.dirname(os.path.abspath(args.out))) as tmp:
        for index, name in enumerate(files, 1):
            target = os.path.join(tmp, f"f_{index:06d}{os.path.splitext(name)[1]}")
            try:
                os.link(name, target)
            except OSError:
                os.symlink(os.path.abspath(name), target)
        ext = os.path.splitext(files[0])[1]
        command = ["ffmpeg", "-v", "error", "-stats", "-y", "-framerate", str(args.fps), "-i", os.path.join(tmp, f"f_%06d{ext}")]
        if args.audio:
            command += ["-i", args.audio]
        filters = ["scale=in_range=pc:out_range=tv:out_color_matrix=bt709:flags=lanczos+accurate_rnd+full_chroma_int"
                   + (f":w={args.size.split('x')[0]}:h={args.size.split('x')[1]}" if args.size else "")]
        command += ["-vf", ",".join(filters)] + PRESETS[args.preset] + BT709
        if args.preset != "prores":
            command += ["-crf", str(args.crf if args.crf is not None else (16 if args.preset == "h264" else 18)), "-movflags", "+faststart"]
        if args.audio:
            command += (["-c:a", "pcm_s24le"] if args.preset == "prores" else ["-c:a", "aac", "-b:a", "256k"]) + ["-shortest"]
        command += ["-r", str(args.fps), args.out]
        result = subprocess.run(command)
    if result.returncode == 0:
        print(f"wrote {args.out}: {len(files)} frames at {args.fps} fps = {len(files) / args.fps:.2f} s, {os.path.getsize(args.out) / 1e6:.1f} MB")
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
