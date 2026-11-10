#!/usr/bin/env python3
"""Copy third-party skill packs into .claude/skills/ as described by packs.json.

Standard library only.

    python3 tools/skills/vendor.py --src /path/to/clones [--only PACK_ID ...] [--dry-run]

`--src` holds one clone per pack, named `<owner>__<repo>` (for example
`EL4CTEO__blender-skills`). Each clone must be checked out at the commit recorded in
packs.json; the script refuses a clone at any other commit.

What it does for every skill of every pack that is not `preinstalled`:
  * copies the skill folder to .claude/skills/<name>/ (replacing a previous copy of it)
  * leaves out the names in `exclude_names` and anything that is a symlink
  * removes the front-matter keys in `strip_frontmatter_keys` from SKILL.md, so a
    third-party skill cannot pre-approve tools or register hooks
  * copies the pack's licence to .claude/skills/LICENSES/<pack id>.txt
and then writes .claude/skills/PACKS.lock.json: per skill, the pack it belongs to, the
number of files and a SHA-256 over its content. tools/skills/check.py verifies that lock.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / ".claude" / "skills"
MANIFEST = Path(__file__).with_name("packs.json")
LOCK = SKILLS / "PACKS.lock.json"
FRONT_MATTER = re.compile(r"\A---\r?\n(.*?\r?\n)---\r?\n", re.S)
NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")


def tree_digest(folder: Path) -> tuple[str, int]:
    """SHA-256 over the sorted relative paths and contents of every file in a folder."""
    digest = hashlib.sha256()
    count = 0
    # Python writes __pycache__ next to a script the first time it runs: not part of the content.
    for path in sorted(p for p in folder.rglob("*") if p.is_file() and not p.is_symlink() and "__pycache__" not in p.parts):
        digest.update(str(path.relative_to(folder)).encode() + b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
        count += 1
    return digest.hexdigest(), count


def strip_keys(text: str, keys: list[str]) -> tuple[str, list[str]]:
    """Remove top-level front-matter keys (with their indented or list continuation lines)."""
    match = FRONT_MATTER.match(text)
    if not match:
        return text, []
    kept: list[str] = []
    removed: list[str] = []
    dropping = False
    for line in match.group(1).splitlines(keepends=True):
        top = re.match(r"^([A-Za-z0-9_-]+):", line)
        if top:
            dropping = top.group(1) in keys
            if dropping:
                removed.append(top.group(1))
        if not dropping:
            kept.append(line)
    return "---\n" + "".join(kept) + "---\n" + text[match.end():], removed


def declared_name(skill_md: Path) -> str:
    match = FRONT_MATTER.match(skill_md.read_text(encoding="utf-8", errors="replace"))
    if match:
        for line in match.group(1).splitlines():
            if line.startswith("name:"):
                return line.split(":", 1)[1].strip().strip("'\"")
    return ""


def copy_tree(src: Path, dst: Path, exclude: set[str], include: list[str] | None) -> None:
    def keep(path: Path) -> bool:
        relative = path.relative_to(src)
        if path.is_symlink() or any(part in exclude for part in relative.parts):
            return False
        return not any(str(relative).endswith(tail) for tail in exclude if "/" in tail)

    tops = [src / name for name in include] if include else list(src.iterdir())
    for top in tops:
        if not top.exists():
            raise SystemExit(f"missing in source: {top}")
        for path in [top] if top.is_file() else sorted(top.rglob("*")):
            if path.is_file() and keep(path):
                target = dst / path.relative_to(src)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--src", required=True, help="folder with one clone per pack (<owner>__<repo>)")
    parser.add_argument("--only", nargs="*", help="pack ids to (re)copy; default: all")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text())
    exclude = set(manifest["exclude_names"])
    strip = manifest["strip_frontmatter_keys"]
    lock = json.loads(LOCK.read_text()) if LOCK.exists() else {"skills": {}, "packs": {}}
    owners = {name: info["pack"] for name, info in lock["skills"].items()}
    problems: list[str] = []

    for pack in manifest["packs"]:
        pid = pack["id"]
        if pack.get("preinstalled"):
            # Recorded only: every top-level skill folder not claimed by another pack belongs to it.
            continue
        if pack.get("local"):
            # Written in this repository: nothing to copy, only the content hash is recorded.
            for name in pack["local"]:
                digest, files = tree_digest(SKILLS / name)
                lock["skills"][name] = {"pack": pid, "files": files, "sha256": digest}
                owners[name] = pid
            lock["packs"][pid] = {key: pack[key] for key in ("repo", "commit", "license", "purpose")}
            lock["packs"][pid].update(skills=len(pack["local"]), local=True)
            print(f"{pid}: {len(pack['local'])} local skill(s) recorded")
            continue
        if args.only and pid not in args.only:
            continue
        clone = Path(args.src) / pack["repo"].replace("/", "__")
        head = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        if head != pack["commit"]:
            problems.append(f"{pid}: clone is at {head or 'no commit'}, manifest says {pack['commit']}")
            continue

        if "skills_dir" in pack:
            mapping = {str(p.parent.relative_to(clone)): p.parent.name
                       for p in sorted((clone / pack["skills_dir"]).glob("*/SKILL.md"))}
        else:
            mapping = dict(pack["skills"])
        copied: list[str] = []
        for source, name in mapping.items():
            if name in pack.get("skip", {}):
                continue
            src = clone / source
            if not NAME.fullmatch(name) or declared_name(src / "SKILL.md") != name:
                problems.append(f"{pid}: {source} declares name {declared_name(src / 'SKILL.md')!r}, expected {name!r}")
                continue
            if owners.get(name, pid) != pid or ((SKILLS / name).exists() and name not in owners):
                problems.append(f"{pid}: skill name {name!r} is already used by {owners.get(name, 'an existing skill')}")
                continue
            if args.dry_run:
                copied.append(name)
                continue
            dst = SKILLS / name
            if dst.exists():
                shutil.rmtree(dst)
            copy_tree(src, dst, exclude, pack.get("include"))
            skill_md = dst / "SKILL.md"
            text, removed = strip_keys(skill_md.read_text(encoding="utf-8"), strip)
            if removed:
                skill_md.write_text(text, encoding="utf-8")
            digest, files = tree_digest(dst)
            lock["skills"][name] = {"pack": pid, "files": files, "sha256": digest,
                                    **({"removed_frontmatter": removed} if removed else {})}
            owners[name] = pid
            copied.append(name)

        if not args.dry_run:
            # Drop skills this pack no longer provides.
            for name in [n for n, info in lock["skills"].items() if info["pack"] == pid and n not in copied]:
                shutil.rmtree(SKILLS / name, ignore_errors=True)
                del lock["skills"][name]
            licence = SKILLS / "LICENSES" / f"{pid}.txt"
            licence.parent.mkdir(exist_ok=True)
            shutil.copy2(clone / pack["license_src"], licence)
            lock["packs"][pid] = {key: pack[key] for key in ("repo", "commit", "license", "purpose")}
            lock["packs"][pid]["skills"] = len(copied)
            if pack.get("skip"):
                lock["packs"][pid]["skipped"] = pack["skip"]
        print(f"{pid}: {len(copied)} skill(s){' (dry run)' if args.dry_run else ''}")

    if not args.dry_run:
        claimed = set(lock["skills"])
        for pack in manifest["packs"]:
            if pack.get("preinstalled"):
                own = sorted(p.parent.name for p in SKILLS.glob("*/SKILL.md") if p.parent.name not in claimed)
                lock["packs"][pack["id"]] = {key: pack[key] for key in ("repo", "commit", "license", "purpose")}
                lock["packs"][pack["id"]].update(skills=len(own), skill_names=own, shared_dirs=pack.get("shared_dirs", []))
        lock["skills"] = dict(sorted(lock["skills"].items()))
        LOCK.write_text(json.dumps(lock, indent=1) + "\n")

    for problem in problems:
        print(f"FAIL  {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
