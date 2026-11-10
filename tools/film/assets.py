#!/usr/bin/env python3
"""Fetch free CC0 assets from Poly Haven: HDRIs, PBR texture sets and models.

    python3 tools/film/assets.py search hdris sunset            # also: textures, models
    python3 tools/film/assets.py get kloofendal_48d_partly_cloudy_puresky --res 2k
    python3 tools/film/assets.py get wood_table_001 --res 2k     # texture set: colour, roughness, normal, displacement
    python3 tools/film/assets.py get potted_plant_04 --res 1k    # model as glTF with its textures

Standard library only. Files go to /opt/film-studio/assets/{hdris,textures,models}/ (or --dest) and
every download is checked against the MD5 the API publishes. Existing files are kept. Each asset
folder gets an `asset.json` with the file paths, which `filmkit.pbr_material` and
`filmkit.world_hdri` accept. Needs api.polyhaven.com and dl.polyhaven.org in the environment's
allowed hosts. All Poly Haven assets are CC0 (public domain): https://polyhaven.com/license
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.polyhaven.com"
AGENT = {"User-Agent": "film-toolkit/1.0"}
TEXTURE_MAPS = {"Diffuse": "color", "Rough": "roughness", "nor_gl": "normal", "Displacement": "displacement",
                "AO": "ao", "Metal": "metallic", "Translucent": "translucency", "arm": "arm"}


def api(path: str):
    with urllib.request.urlopen(urllib.request.Request(f"{API}/{path}", headers=AGENT), timeout=60) as response:
        return json.load(response)


def download(entry: dict, target: Path) -> Path:
    if target.exists() and target.stat().st_size == entry.get("size", -1):
        return target
    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_suffix(target.suffix + ".part")
    digest = hashlib.md5(usedforsecurity=False)
    with urllib.request.urlopen(urllib.request.Request(entry["url"], headers=AGENT), timeout=300) as response, open(partial, "wb") as out:
        for block in iter(lambda: response.read(1 << 20), b""):
            digest.update(block)
            out.write(block)
    if entry.get("md5") and digest.hexdigest() != entry["md5"]:
        partial.unlink()
        raise SystemExit(f"checksum mismatch for {entry['url']}")
    partial.replace(target)
    return target


def search(kind: str, words: list[str], limit: int) -> int:
    assets = api(f"assets?t={urllib.parse.quote(kind)}")
    wanted = [w.lower() for w in words]
    rows = []
    for name, info in assets.items():
        text = " ".join([name, info.get("name", "")] + info.get("tags", []) + info.get("categories", [])).lower()
        if all(w in text for w in wanted):
            rows.append((info.get("download_count", 0), name, info.get("name", ""), ", ".join(info.get("categories", [])[:4])))
    for count, name, title, categories in sorted(rows, reverse=True)[:limit]:
        print(f"{name:44s} {count:>9d} downloads  {title}  [{categories}]")
    print(f"{len(rows)} of {len(assets)} {kind} match")
    return 0


def get(name: str, res: str, dest: Path, hdr_format: str) -> int:
    info = api(f"info/{urllib.parse.quote(name)}")
    files = api(f"files/{urllib.parse.quote(name)}")
    kind = {0: "hdris", 1: "textures", 2: "models"}[info["type"]]
    folder = dest / kind / name
    record = {"id": name, "name": info.get("name"), "type": kind, "resolution": res, "license": "CC0-1.0",
              "source": f"https://polyhaven.com/a/{name}", "files": {}}

    def pick(options: dict) -> dict:
        if res in options:
            return options[res]
        fallback = sorted(options, key=lambda k: int(k.rstrip("k")))[0]
        print(f"note: {res} not offered, using {fallback}")
        return options[fallback]

    if kind == "hdris":
        entry = pick(files["hdri"])[hdr_format]
        record["files"]["hdri"] = str(download(entry, folder / f"{name}_{res}.{hdr_format}"))
    elif kind == "textures":
        for key, label in TEXTURE_MAPS.items():
            if key not in files:
                continue
            formats = pick(files[key])
            ext = "exr" if key == "Displacement" and "exr" in formats and "png" not in formats else ("jpg" if "jpg" in formats else next(iter(formats)))
            record["files"][label] = str(download(formats[ext], folder / f"{name}_{label}_{res}.{ext}"))
        record["dimensions_mm"] = info.get("dimensions")
    else:
        entry = pick(files["gltf"])["gltf"]
        record["files"]["gltf"] = str(download(entry, folder / f"{name}_{res}.gltf"))
        for relative, extra in entry.get("include", {}).items():
            download(extra, folder / relative)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "asset.json").write_text(json.dumps(record, indent=1) + "\n")
    size = sum(p.stat().st_size for p in folder.rglob("*") if p.is_file()) / 1e6
    print(f"{kind[:-1]} {name} ({res}): {len(record['files'])} file(s), {size:.1f} MB -> {folder}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    s = sub.add_parser("search")
    s.add_argument("kind", choices=("hdris", "textures", "models"))
    s.add_argument("words", nargs="*")
    s.add_argument("--limit", type=int, default=12)
    g = sub.add_parser("get")
    g.add_argument("name")
    g.add_argument("--res", default="2k")
    g.add_argument("--format", default="hdr", choices=("hdr", "exr"), help="HDRI file format")
    g.add_argument("--dest", default=os.environ.get("FILM_HOME", "/opt/film-studio") + "/assets")
    args = parser.parse_args()
    if args.command == "search":
        return search(args.kind, args.words, args.limit)
    return get(args.name, args.res, Path(args.dest), args.format)


if __name__ == "__main__":
    sys.exit(main())
