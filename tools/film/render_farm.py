#!/usr/bin/env python3
"""Render an animation range with Blender in the background, resumable after any interruption.

    python3 tools/film/render_farm.py SCENE.blend --frames 1-240 --out /path/frames/shot_####
            [--jobs 1] [--format PNG|EXR] [--samples N] [--scale 50] [--blender PATH]

Run it again after a crash, a stop or a suspended container: finished frames are kept, frames
that were in progress are rendered again. Cycles on a CPU already uses every core, so the default
is one Blender process; `--jobs 2` (each with half the threads) helps only when frames are so light
that scene loading and saving dominate. Prints progress with the measured seconds per frame and a
time estimate, and at the end checks that every frame exists and is not empty.
"""

import argparse
import glob
import json
import os
import subprocess
import sys
import time


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("blend")
    parser.add_argument("--frames", required=True, help="first-last, e.g. 1-240")
    parser.add_argument("--out", required=True, help="output path with #### for the frame number")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--format", choices=("PNG", "EXR"), default="PNG")
    parser.add_argument("--samples", type=int)
    parser.add_argument("--scale", type=int)
    parser.add_argument("--blender", default=os.environ.get("BLENDER", "/opt/blender-dl/current/blender"))
    parser.add_argument("--poll", type=float, default=20.0)
    args = parser.parse_args()

    first, last = (int(v) for v in args.frames.split("-"))
    ext = ".exr" if args.format == "EXR" else ".png"
    name = lambda f: args.out.replace("####", f"{f:04d}") + ext  # noqa: E731
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    for path in glob.glob(args.out.replace("####", "*") + ext):          # placeholders of interrupted frames
        if os.path.getsize(path) == 0:
            os.remove(path)
    todo = [f for f in range(first, last + 1) if not os.path.exists(name(f))]
    print(f"{last - first + 1} frames in range, {len(todo)} to render")
    if not todo:
        return 0
    log = os.path.abspath(args.out.replace("####", "timing") + ".jsonl")
    worker = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blender", "farm_worker.py")
    threads = max(1, (os.cpu_count() or 4) // args.jobs)
    procs = []
    for index in range(args.jobs):
        command = [args.blender, "-b", args.blend, "--python", worker, "--", "--start", str(first), "--end", str(last),
                   "--out", args.out, "--format", args.format, "--log", log, "--worker", str(index)]
        command += ["--threads", str(threads)] if args.jobs > 1 else []
        command += ["--samples", str(args.samples)] if args.samples else []
        command += ["--scale", str(args.scale)] if args.scale else []
        procs.append(subprocess.Popen(command, stdout=open(log + f".worker{index}.log", "w"), stderr=subprocess.STDOUT))
    began = time.time()
    try:
        while any(p.poll() is None for p in procs):
            time.sleep(args.poll)
            done = sum(1 for f in todo if os.path.exists(name(f)) and os.path.getsize(name(f)) > 0)
            times = [json.loads(line)["seconds"] for line in open(log)] if os.path.exists(log) else []
            recent = times[-12:]
            per_frame = sum(recent) / len(recent) if recent else 0.0
            left = (len(todo) - done) * per_frame / args.jobs
            print(f"  {done}/{len(todo)} frames, {per_frame:.1f} s/frame, about {left / 60:.1f} min left "
                  f"({(time.time() - began) / 60:.1f} min so far)", flush=True)
    except KeyboardInterrupt:
        for p in procs:
            p.terminate()
        return 130
    missing = [f for f in range(first, last + 1) if not os.path.exists(name(f)) or os.path.getsize(name(f)) == 0]
    if missing:
        print(f"FAIL  {len(missing)} frame(s) missing, first {missing[:10]}; see {log}.worker*.log and run again")
        return 1
    print(f"done: frames {first}-{last} in {(time.time() - began) / 60:.1f} min -> {args.out}{ext}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
