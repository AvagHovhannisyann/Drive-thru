#!/usr/bin/env python3
"""Find and fetch free sound effects and music from Mixkit for use in a film's sound track.

    python3 tools/film/sounds.py search sfx whoosh           # tags: whoosh click keyboard impact rain footsteps door ...
    python3 tools/film/sounds.py search music ambient         # tags: ambient cinematic corporate piano-ish moods and genres
    python3 tools/film/sounds.py get sfx 1492 --title "Cinematic whoosh fast transition"
    python3 tools/film/sounds.py get music 127 --title "Valley Sunset"

Standard library only. Files go to /opt/film-studio/assets/{sfx,music}/mixkit_<id>.mp3 and each
download is added to manifest.jsonl there (id, title, URL, licence, date), so a film can list its
sources. Use them in a cue sheet with {"type": "file", "file": "/opt/film-studio/assets/sfx/mixkit_1492.mp3", ...}.

Licence: Mixkit Sound Effects Free License / Mixkit Stock Music Free License. Free to use in
videos, including commercial ones; NOT to be redistributed as stand-alone files. Never commit
these files to a repository. https://mixkit.co/license/
Needs mixkit.co and assets.mixkit.co in the environment's allowed hosts.
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

AGENT = {"User-Agent": "Mozilla/5.0 (film-toolkit)"}
PAGES = {"sfx": "https://mixkit.co/free-sound-effects/{tag}/", "music": "https://mixkit.co/free-stock-music/{tag}/"}
FILES = {"sfx": "https://assets.mixkit.co/active_storage/sfx/{id}/{id}-preview.mp3", "music": "https://assets.mixkit.co/music/{id}/{id}.mp3"}
LICENCE = {"sfx": "Mixkit Sound Effects Free License", "music": "Mixkit Stock Music Free License"}


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=AGENT), timeout=120) as response:
        return response.read()


def search(kind: str, tag: str, limit: int) -> int:
    html = fetch(PAGES[kind].format(tag=tag)).decode("utf8", "ignore")
    ids = [(m.start(), m.group(1)) for m in re.finditer(r'data-audio-player-item-id-value="(\d+)"', html)]
    titles = [(m.start(), m.group(1).strip()) for m in re.finditer(r'item-grid-card__title">\s*(?:<[^>]+>\s*)*([^<]+?)\s*<', html)]
    for index, (position, sound_id) in enumerate(ids[:limit]):
        following = ids[index + 1][0] if index + 1 < len(ids) else len(html)
        title = next((t for pos, t in titles if position < pos < following), "")
        print(f"{sound_id:>6}  {title}")
    print(f"{len(ids)} {kind} results for '{tag}'" + ("" if ids else " (try another tag; the page for this one may not exist)"))
    return 0 if ids else 1


def get(kind: str, sound_id: str, title: str, dest: Path) -> int:
    folder = dest / kind
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / f"mixkit_{sound_id}.mp3"
    url = FILES[kind].format(id=sound_id)
    if not target.exists():
        data = fetch(url)
        if not (data[:3] == b"ID3" or data[:1] == b"\xff"):
            print(f"FAIL  {url} did not return an MP3 file")
            return 1
        target.write_bytes(data)
        with open(folder / "manifest.jsonl", "a") as manifest:
            manifest.write(json.dumps({"id": sound_id, "kind": kind, "title": title, "url": url, "licence": LICENCE[kind],
                                       "fetched": datetime.date.today().isoformat(), "file": str(target)}) + "\n")
    print(f"{target} ({target.stat().st_size / 1e3:.0f} kB) - {LICENCE[kind]}: use in the film, do not redistribute the file")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("search")
    s.add_argument("kind", choices=("sfx", "music"))
    s.add_argument("tag")
    s.add_argument("--limit", type=int, default=20)
    g = sub.add_parser("get")
    g.add_argument("kind", choices=("sfx", "music"))
    g.add_argument("id")
    g.add_argument("--title", default="")
    g.add_argument("--dest", default=os.environ.get("FILM_HOME", "/opt/film-studio") + "/assets")
    args = parser.parse_args()
    if args.command == "search":
        return search(args.kind, args.tag, args.limit)
    return get(args.kind, args.id, args.title, Path(args.dest))


if __name__ == "__main__":
    sys.exit(main())
