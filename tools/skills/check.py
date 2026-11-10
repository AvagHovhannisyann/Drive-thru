#!/usr/bin/env python3
"""Integrity check for every skill in .claude/skills/.

Standard library only:  python3 tools/skills/check.py [--dir PATH] [--quiet]

For every <skill>/SKILL.md:
  * YAML front matter exists, `name` equals the folder name, `description` has 1-1024 characters
  * no front-matter key is repeated, and none of the keys the vendoring step removes
    (`strip_frontmatter_keys` in packs.json) has come back
  * the skill belongs to exactly one pack in PACKS.lock.json
For skills copied by tools/skills/vendor.py: the folder still has the recorded content hash.
For the hand-copied markdown pack (arjun988/blender-skills): markdown files only, no
executable bits, and every `references/*.md` path a skill points to exists.
No symlinks anywhere.

Exit code 0 = all checks pass.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FRONT_MATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
KEY = re.compile(r"^(\s*)([A-Za-z0-9_-]+):\s*(.*)$")
NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
MD_PATH = re.compile(r"(?<![A-Za-z0-9_./-])((?:\.\./|\./)?references/[A-Za-z0-9_.-]+\.md)")
TOP_LEVEL_FILES = {"README.md", "LICENSE-blender-skills", "PACKS.lock.json"}


def parse_front_matter(text: str) -> tuple[dict[str, str], list[str]]:
    """Top-level keys with their values, and the names of keys that occur twice."""
    match = FRONT_MATTER.match(text)
    if not match:
        raise ValueError("no YAML front matter")
    values: dict[str, str] = {}
    seen: collections.Counter[str] = collections.Counter()
    parent = ""
    lines = match.group(1).splitlines()
    for index, line in enumerate(lines):
        key = KEY.match(line)
        if not key:
            continue
        indent, name, value = key.groups()
        if indent:
            seen[f"{parent}.{name}"] += 1
            continue
        parent = name
        seen[name] += 1
        value = value.strip()
        if value in {">", "|", ">-", "|-", ">+", "|+"}:  # block scalar: join the indented lines
            block = []
            for following in lines[index + 1:]:
                if following.strip() and not following.startswith((" ", "\t")):
                    break
                block.append(following.strip())
            value = " ".join(part for part in block if part)
        values[name] = value.strip("'\"")
    return values, sorted(k for k, count in seen.items() if count > 1)


def tree_digest(folder: Path) -> tuple[str, int]:
    digest = hashlib.sha256()
    count = 0
    # Python writes __pycache__ next to a script the first time it runs: not part of the content.
    for path in sorted(p for p in folder.rglob("*") if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts):
        digest.update(str(path.relative_to(folder)).encode() + b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
        count += 1
    return digest.hexdigest(), count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dir", default=str(ROOT / ".claude" / "skills"))
    parser.add_argument("--quiet", action="store_true", help="print only failures and the result line")
    args = parser.parse_args()

    root = Path(args.dir)
    lock_file = root / "PACKS.lock.json"
    if not lock_file.is_file():
        print(f"FAIL  {lock_file} not found (run tools/skills/vendor.py)")
        return 1
    lock = json.loads(lock_file.read_text())
    strip = json.loads(Path(__file__).with_name("packs.json").read_text())["strip_frontmatter_keys"]
    vendored: dict[str, dict] = lock["skills"]
    markdown_pack = {name: pid for pid, pack in lock["packs"].items() for name in pack.get("skill_names", [])}
    shared_dirs = {d for pack in lock["packs"].values() for d in pack.get("shared_dirs", [])}
    problems: list[str] = []
    skills = sorted(p.parent for p in root.glob("*/SKILL.md"))

    for path in root.rglob("*"):
        if path.is_symlink():
            problems.append(f"{path.relative_to(root)}: symlink")
    for entry in sorted(root.iterdir()):
        if entry.is_file() and entry.name not in TOP_LEVEL_FILES:
            problems.append(f"{entry.name}: unexpected file at the top level")
        if entry.is_dir() and entry.name not in shared_dirs | {"LICENSES"} and not (entry / "SKILL.md").is_file():
            problems.append(f"{entry.name}/: folder without SKILL.md")

    per_pack: collections.Counter[str] = collections.Counter()
    for skill in skills:
        name = skill.name
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        try:
            meta, duplicates = parse_front_matter(text)
        except ValueError as exc:
            problems.append(f"{name}: {exc}")
            continue
        if duplicates:
            problems.append(f"{name}: repeated front-matter key(s) {', '.join(duplicates)}")
        declared = meta.get("name", "")
        if declared != name or not NAME.fullmatch(declared) or len(declared) > 64:
            problems.append(f"{name}: name field is {declared!r}")
        if not 1 <= len(meta.get("description", "")) <= 1024:
            problems.append(f"{name}: description has {len(meta.get('description', ''))} characters")

        if name in vendored and name in markdown_pack:
            problems.append(f"{name}: listed in two packs")
        elif name in vendored:
            per_pack[vendored[name]["pack"]] += 1
            digest, files = tree_digest(skill)
            if digest != vendored[name]["sha256"]:
                problems.append(f"{name}: content differs from PACKS.lock.json ({files} files now, {vendored[name]['files']} recorded)")
            for key in strip:
                if key in meta:
                    problems.append(f"{name}: front matter contains {key!r}")
        elif name in markdown_pack:
            per_pack[markdown_pack[name]] += 1
            for path in sorted(skill.rglob("*")):
                if path.is_file() and path.suffix != ".md":
                    problems.append(f"{path.relative_to(root)}: not a markdown file")
                if path.is_file() and path.stat().st_mode & 0o111:
                    problems.append(f"{path.relative_to(root)}: executable bit set")
            for target in sorted(set(MD_PATH.findall(text))):
                if not (skill / target).resolve().is_file():
                    problems.append(f"{name}: points to missing file {target}")
        else:
            problems.append(f"{name}: not listed in PACKS.lock.json")

    for name in sorted(set(vendored) | set(markdown_pack)):
        if not (root / name / "SKILL.md").is_file():
            problems.append(f"{name}: recorded in PACKS.lock.json but missing")
    for pid, pack in lock["packs"].items():
        if not args.quiet:
            print(f"  {per_pack[pid]:>3} / {pack['skills']:<3} {pid}  ({pack['repo']} @ {pack['commit'][:7]}, {pack['license']})")
        if per_pack[pid] != pack["skills"]:
            problems.append(f"{pid}: {per_pack[pid]} skills present, {pack['skills']} recorded")
        licence = root / ("LICENSE-blender-skills" if pack.get("skill_names") else f"LICENSES/{pid}.txt")
        if not pack.get("local") and not licence.is_file():
            problems.append(f"{pid}: licence file missing ({licence.relative_to(root)})")

    print(f"skills: {len(skills)} in {len(lock['packs'])} packs, directory: {root}")
    for problem in problems:
        print(f"FAIL  {problem}")
    print("RESULT: " + ("PASS" if not problems else f"FAIL ({len(problems)} problem(s))"))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
