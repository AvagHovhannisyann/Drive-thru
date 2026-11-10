#!/usr/bin/env python3
"""Download the font families in fonts.txt from Google Fonts as static TTF files.

    python3 tools/film/fonts.py [--dest /opt/film-studio/fonts] [--list fonts.txt]

Standard library only. Files land in <dest>/<Family>/<Family>-<weight>[-Italic].ttf and the
folder is linked into fontconfig (/usr/local/share/fonts/film-studio) so the headless browser,
ffmpeg and ImageMagick find the families by name. Blender needs the file path: see
<dest>/index.json. Existing files are kept, so the script is safe to run again.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

CSS_API = "https://fonts.googleapis.com/css2"
FACE = re.compile(r"font-style:\s*(\w+);\s*font-weight:\s*(\d+);.*?src:\s*url\((https://fonts\.gstatic\.com/[^)]+\.ttf)\)", re.S)


def fetch(url: str) -> bytes:
    # A plain client User-Agent makes the API answer with static TrueType files.
    request = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dest", default=os.environ.get("FILM_HOME", "/opt/film-studio") + "/fonts")
    parser.add_argument("--list", default=str(Path(__file__).with_name("fonts.txt")))
    args = parser.parse_args()
    dest = Path(args.dest)
    index: dict[str, dict[str, str]] = {}
    failures = 0

    for raw in Path(args.list).read_text().splitlines():
        line = raw.split("#")[0].strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split("|")]
        family, weights = parts[0], parts[1].split(",")
        italics = parts[2].split(",") if len(parts) > 2 and parts[2] else []
        tuples = sorted([f"0,{w}" for w in weights] + [f"1,{w}" for w in italics])
        query = f"{family.replace(' ', '+')}:ital,wght@{';'.join(tuples)}" if italics else \
            f"{family.replace(' ', '+')}:wght@{';'.join(sorted(weights, key=int))}"
        folder = dest / family.replace(" ", "")
        folder.mkdir(parents=True, exist_ok=True)
        try:
            css = fetch(f"{CSS_API}?family={urllib.parse.quote(query, safe='+:,;@')}").decode()
        except OSError as exc:
            print(f"FAIL  {family}: {exc}")
            failures += 1
            continue
        faces = FACE.findall(css)
        for style, weight, url in faces:
            name = f"{family.replace(' ', '')}-{weight}{'-Italic' if style == 'italic' else ''}.ttf"
            target = folder / name
            if not target.exists():
                target.write_bytes(fetch(url))
            index.setdefault(family, {})[f"{weight}{'i' if style == 'italic' else ''}"] = str(target)
        print(f"{'ok  ' if faces else 'FAIL'}  {family}: {len(faces)} file(s)")
        failures += not faces

    (dest / "index.json").write_text(json.dumps(index, indent=1) + "\n")
    link = Path("/usr/local/share/fonts/film-studio")
    try:
        link.parent.mkdir(parents=True, exist_ok=True)
        if link.is_symlink() or not link.exists():
            link.unlink(missing_ok=True)
            link.symlink_to(dest)
        subprocess.run(["fc-cache", "-f", str(link)], check=False)
    except OSError as exc:
        print(f"note: could not register with fontconfig: {exc}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
