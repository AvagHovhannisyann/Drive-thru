#!/usr/bin/env python3
"""Integrity check for the Blender Skills pack installed in .claude/skills/.

Standard library only:  python3 tools/blender-mcp/check_skills.py [--expect 94] [--dir PATH]

Checks, for every <skill>/SKILL.md:
  * YAML front matter exists, with `name` equal to the folder name and a `description`
    of 1-1024 characters (what Claude Code needs to list and trigger a skill)
  * no key is repeated in the front matter (invalid for strict YAML parsers)
  * every `*.md` file it points to (`../references/x.md`, `references/x.md`) exists
and that the pack contains only markdown files (no scripts, executables or symlinks).

Exit code 0 = all checks pass.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

FRONT_MATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
KEY = re.compile(r"^(\s*)([A-Za-z0-9_-]+):\s*(.*)$")
NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
# Paths to reference files as the skills write them (prose, backticks, tables, links):
# `references/x.md` is relative to the skill folder, `../references/x.md` is the shared folder.
MD_PATH = re.compile(r"(?<![A-Za-z0-9_./-])((?:\.\./|\./)?references/[A-Za-z0-9_.-]+\.md)")
# Files in the skills folder that are not part of any skill.
EXTRA_FILES = {"README.md", "LICENSE-blender-skills"}


def parse_front_matter(text: str) -> tuple[dict[str, str], list[str]]:
    """Top-level keys with their values, and the names of keys that occur twice."""
    match = FRONT_MATTER.match(text)
    if not match:
        raise ValueError("no YAML front matter")
    values: dict[str, str] = {}
    seen: collections.Counter[str] = collections.Counter()
    parent = ""
    for line in match.group(1).splitlines():
        key = KEY.match(line)
        if not key:
            continue
        indent, name, value = key.groups()
        if indent:
            seen[f"{parent}.{name}"] += 1
        else:
            parent = name
            seen[name] += 1
            values[name] = value.strip().strip("'\"")
    return values, sorted(k for k, count in seen.items() if count > 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--dir", default=str(Path(__file__).resolve().parents[2] / ".claude" / "skills"))
    parser.add_argument("--expect", type=int, default=94, help="number of skills the pack should contain")
    args = parser.parse_args()

    root = Path(args.dir)
    if not root.is_dir():
        print(f"FAIL  skills directory not found: {root}")
        return 1

    problems: list[str] = []
    skills = sorted(p.parent for p in root.glob("*/SKILL.md"))
    references = 0

    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if path.is_symlink():
            problems.append(f"{relative}: symlink")
        elif path.is_file():
            if path.suffix != ".md" and str(relative) not in EXTRA_FILES:
                problems.append(f"{relative}: not a markdown file")
            if path.stat().st_mode & 0o111:
                problems.append(f"{relative}: executable bit set")
            if path.suffix == ".md" and path.name != "SKILL.md" and str(relative) not in EXTRA_FILES:
                references += 1

    for skill in skills:
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        try:
            meta, duplicates = parse_front_matter(text)
        except ValueError as exc:
            problems.append(f"{skill.name}: {exc}")
            continue
        if duplicates:
            problems.append(f"{skill.name}: repeated front-matter key(s) {', '.join(duplicates)}")
        name = meta.get("name", "")
        if name != skill.name or not NAME.fullmatch(name) or len(name) > 64:
            problems.append(f"{skill.name}: name field is {name!r}")
        description = meta.get("description", "")
        if not 1 <= len(description) <= 1024:
            problems.append(f"{skill.name}: description has {len(description)} characters")
        for target in sorted(set(MD_PATH.findall(text))):
            if not (skill / target).resolve().is_file():
                problems.append(f"{skill.name}: points to missing file {target}")

    if len(skills) != args.expect:
        problems.append(f"found {len(skills)} skills, expected {args.expect}")

    print(f"skills: {len(skills)} (expected {args.expect}), reference files: {references}, directory: {root}")
    for problem in problems:
        print(f"FAIL  {problem}")
    print("RESULT: " + ("PASS" if not problems else f"FAIL ({len(problems)} problem(s))"))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
