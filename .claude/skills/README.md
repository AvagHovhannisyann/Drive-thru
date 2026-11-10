# Skills in this repository

Claude Code loads every `<name>/SKILL.md` in this folder at session start. `PACKS.lock.json` records
which pack each skill belongs to and a content hash; `LICENSES/` holds each pack's licence.

```bash
python3 tools/skills/check.py        # every skill: valid metadata, pack membership, unchanged content
```

## Packs

| Pack | Skills | Source (commit) | Licence | Use |
|---|---|---|---|---|
| film-studio | 1 | this repository | repository | Entry point for films: plate-based CPU pipeline, `tools/film` |
| arjun988-blender-skills | 94 | arjun988/blender-skills (904f095) v1.3.0 | MIT | Art direction, modelling, styles, export; entry `blender-director` |
| el4cteo-blender-skills | 28 | EL4CTEO/blender-skills (389f28a) | MIT | Blender 5.2 Python API by topic (`blender-core` first) |
| roble3-cc-blender-skill | 28 | RobLe3/cc-blender-skill (a2634b5) | MIT | Reference-to-3D, cameras, lighting, materials, quality gates |
| mromidev-claude-blender-skills | 3 | mromidev/claude-blender-skills (567116b) | MIT | Whole-film walk-throughs |
| blender-asset-studio | 1 | new-experement/blender-asset-studio (e68a7f3) | MIT | Asset build loop with visual review |
| gokayfem-video-to-blender | 1 | gokayfem/video-to-blender (bfeca3f) | MIT | Procedural node recipes |
| rwspatin-video-3d-skill | 1 | rwspatin/video-3d-skill (6bacc36) | MIT | Choosing between Three.js, Cycles and AI video |
| echris6-motion-video-kit | 1 | echris6/motion-video-kit (e4b1c00) | MIT | Motion film with critic loop, sound mix scripts |
| howseen-claude-motion-design | 1 | howseen-ai/claude-motion-design (3d90d34) | MIT | HTML motion design |
| sallyrs-video-director | 1 | SallyRS/video-director (5e869cf) | MIT (+ real-sfx MIT, uisfx MIT / audio CC0) | Direction, render checks, sound design |
| kajisho5-ffmpeg-skill | 1 | kajisho5/ffmpeg-skill (6e42a79) | MIT | Editing and delivery with FFmpeg |
| runpod-plugins-official | 17 | runpod/runpod-plugins-official (5a83c49) | Apache-2.0 | GPU rental; needs the user's key and network access |

## How third-party packs were brought in

`tools/skills/packs.json` lists every pack with its repository and the exact commit that was
reviewed. `tools/skills/vendor.py --src <folder of clones>` copies the skill folders and:

- removes the front-matter keys `allowed-tools` and `hooks` (32 skills had `allowed-tools`), so a
  third-party skill cannot pre-approve tools or register hooks here;
- leaves out `tests/`, `evals/`, caches and anything that is a symlink;
- skips two RobLe3 skills (`blender-animation`, `blender-rendering`) whose names the EL4CTEO pack also uses;
- copies only `SKILL.md`, `scripts/`, `references/`, `templates/`, `examples/` of ffmpeg-skill (not its demos, site or tests).

Every repository was scanned before copying (network calls, process execution, dynamic evaluation,
deletes, secrets, install-at-runtime, instruction overrides, hidden characters) and the hits were read.
Nothing malicious was found. Scripts that call online services (ElevenLabs, Poly Haven, Mixkit,
Gemini, RunPod) are inert here until a host is allowed and a key is provided.

The earlier hand-copied pack (arjun988) has one local change: a repeated `role:` key was removed from
`blender-director/SKILL.md`.

Reviewed and not installed (reasons in `tools/skills/packs.json`): remotion-dev/skills,
edemaistre/blender-expert-skills, aminellkadaoui/3d-scenes (no licence), Tejashmakwana/motionmaxxing
(bundles non-open-source GSAP), nocodehack/make-short (39 MB, Windows-specific),
sunxiayi/make-blender-education-video-skill (older than requested), viettranx/3dviz-pro-max,
iart-ai/motion-skills.

## Updating a pack

Clone the repository outside this one, review `git diff <old commit>..<new commit>`, put the new commit
in `tools/skills/packs.json`, run `python3 tools/skills/vendor.py --src <clones> --only <pack id>`,
then `python3 tools/skills/check.py`.

## Environment notes for the packs

- Tool names: the packs' `get_viewport_screenshot` is `look` in this server (`mcp-for-blender` 2.2.7).
- Paths in examples are often Windows paths; write to `/opt/film-studio/work/` or `/opt/blender-mcp/work/`.
- Online asset and sound libraries are blocked unless their hosts are added to the cloud environment.
