#!/usr/bin/env python3
"""Contact sheet from frames, to LOOK at before a long render or an encode.

    /opt/film-studio/venv/bin/python tools/film/sheet.py OUT.jpg FRAME [FRAME ...] [--columns 4] [--width 640]
        [--crop X0,Y0,X1,Y1] [--look '{"exposure": 0.6}'] [--labels]

Frames are PNG/JPG pictures or linear EXR renders (single-layer; graded with --look through the
same finishing as the film, without grain). `--crop` cuts the same rectangle (fractions of the
frame, origin top-left) from every frame at full resolution before scaling: use it to inspect a
character or a seam. Give frames in the order you want them, e.g. with a shell glob.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import comp  # noqa: E402


def load(path: str, look: dict) -> np.ndarray:
    if path.lower().endswith(".exr"):
        picture = comp.finish(comp.read_frame(path), {**look, "grain": 0.0}, with_grain=False)
        return cv2.cvtColor(picture, cv2.COLOR_RGB2BGR)
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(path)
    return image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("out")
    parser.add_argument("frames", nargs="+")
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--width", type=int, default=640, help="width of one tile in pixels")
    parser.add_argument("--crop", help="X0,Y0,X1,Y1 as fractions of the frame")
    parser.add_argument("--look", default="{}")
    parser.add_argument("--labels", action="store_true", help="write the file name on each tile")
    args = parser.parse_args()
    look = json.loads(args.look)
    tiles = []
    for path in args.frames:
        image = load(path, look)
        if args.crop:
            x0, y0, x1, y1 = (float(v) for v in args.crop.split(","))
            h, w = image.shape[:2]
            image = image[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)]
        height = round(args.width * image.shape[0] / image.shape[1])
        tile = cv2.resize(image, (args.width, height), interpolation=cv2.INTER_AREA if image.shape[1] > args.width else cv2.INTER_CUBIC)
        if args.labels:
            name = os.path.splitext(os.path.basename(path))[0]
            cv2.putText(tile, name, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(tile, name, (8, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)
        tiles.append(tile)
    while len(tiles) % args.columns:
        tiles.append(np.zeros_like(tiles[0]))
    rows = [np.hstack(tiles[i:i + args.columns]) for i in range(0, len(tiles), args.columns)]
    cv2.imwrite(args.out, np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 90])
    print(f"wrote {args.out}: {len(args.frames)} frames, {rows[0].shape[1]} x {sum(r.shape[0] for r in rows)} px")
    return 0


if __name__ == "__main__":
    sys.exit(main())
