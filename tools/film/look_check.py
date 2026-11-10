#!/usr/bin/env python3
"""Measure the exposure and colour of stills, so "too bright", "milky" and "dull" are numbers.

    /opt/film-studio/venv/bin/python tools/film/look_check.py still1.png [still2.png ...] [--night] [--json out.json]

For each picture (display-referred, as delivered):
  clipped   share of pixels at or above 98 % in any channel   want < 0.5 %  (blown highlights)
  crushed   share of pixels at or below 1.5 % luma            want < 12 %   (25 % for --night)
  black     5th percentile of luma                             want < 0.08 for interiors (no milky fog)
  key       median luma                                        day 0.25-0.55, night 0.06-0.25
  contrast  95th minus 5th percentile                          want > 0.45 (0.3 for --night)
  colour    Hasler-Suesstrunk colourfulness                    want > 18 (dull below, garish above 110)
A warning is a prompt to look again, not a verdict: a fade to black fails every line and is fine.
Exit code 0 = no warnings.
"""

from __future__ import annotations

import argparse
import json
import sys

import cv2
import numpy as np


def measure(path: str) -> dict:
    image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise FileNotFoundError(path)
    scale = 65535.0 if image.dtype == np.uint16 else 255.0
    rgb = cv2.cvtColor(image[..., :3], cv2.COLOR_BGR2RGB).astype(np.float32) / scale
    luma = rgb @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    rg, yb = rgb[..., 0] - rgb[..., 1], 0.5 * (rgb[..., 0] + rgb[..., 1]) - rgb[..., 2]
    colour = (np.hypot(rg.std(), yb.std()) + 0.3 * np.hypot(rg.mean(), yb.mean())) * 255
    p5, p50, p95 = (float(v) for v in np.percentile(luma, (5, 50, 95)))
    return {"file": path, "clipped": float((rgb.max(axis=-1) >= 0.98).mean() * 100), "crushed": float((luma <= 0.015).mean() * 100),
            "black": p5, "key": p50, "contrast": p95 - p5, "colour": float(colour)}


def warnings(m: dict, night: bool) -> list[str]:
    out = []
    if m["clipped"] > 0.5:
        out.append(f"blown highlights {m['clipped']:.1f} %")
    if m["crushed"] > (25 if night else 12):
        out.append(f"crushed shadows {m['crushed']:.0f} %")
    if m["black"] > 0.08:
        out.append(f"milky blacks (5th percentile {m['black']:.2f})")
    low, high = (0.06, 0.25) if night else (0.25, 0.55)
    if not low <= m["key"] <= high:
        out.append(f"median luma {m['key']:.2f} outside {low}-{high}")
    if m["contrast"] < (0.3 if night else 0.45):
        out.append(f"flat (contrast {m['contrast']:.2f})")
    if not 18 <= m["colour"] <= 110:
        out.append(f"colourfulness {m['colour']:.0f}")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("stills", nargs="+")
    parser.add_argument("--night", action="store_true")
    parser.add_argument("--json")
    args = parser.parse_args()
    results, failed = [], False
    for path in args.stills:
        m = measure(path)
        m["warnings"] = warnings(m, args.night)
        failed |= bool(m["warnings"])
        results.append(m)
        print(f"{path}\n   clipped {m['clipped']:.2f} %  crushed {m['crushed']:.1f} %  black {m['black']:.3f}  key {m['key']:.3f}  "
              f"contrast {m['contrast']:.2f}  colour {m['colour']:.0f}   {'; '.join(m['warnings']) or 'ok'}")
    if args.json:
        with open(args.json, "w") as handle:
            json.dump(results, handle, indent=1)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
