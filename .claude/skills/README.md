# Blender Skills pack (vendored)

The 94 skill folders and the shared `references/` folder in this directory are a copy of
[arjun988/blender-skills](https://github.com/arjun988/blender-skills), MIT licensed
(`LICENSE-blender-skills`). Claude Code loads every `<name>/SKILL.md` here at session start;
this file and the licence are ignored by the loader.

| | |
|---|---|
| Version | 1.3.0 |
| Upstream commit | `904f095d8f36a6e72adaebb08d07f884a074743d` (2026-11-06) |
| Copied | 2026-11-10, the upstream `.claude/skills/` folder |
| Contents | 94 `SKILL.md` + 175 reference files, markdown only (no scripts, hooks or settings) |

## Local change

`blender-director/SKILL.md`: removed the first of two `role:` keys in its metadata
(`role: specialist`; `role: orchestrator` stays). A repeated key is invalid YAML for strict
parsers and this is the pack's entry-point skill. Everything else is byte-identical to upstream.

## Not copied

Upstream `.mcp.json` and `.cursor/mcp.json` (Windows-only `cmd /c uvx blender-mcp`, unpinned).
This repository's own `.mcp.json` registers the pinned server documented in
`tools/blender-mcp/README.md`.

## Using the pack in this repository

- Start with `blender-director`; it plans the work and routes to the other skills.
- The skills execute through the `blender` MCP server (`mcp__blender__*` tools). The Blender
  service must be running: `tools/blender-mcp/start.sh`.
- Tool names differ slightly from what some skills print: the pack's `get_viewport_screenshot`
  is `look` in this server version (`mcp-for-blender` 2.2.7). `execute_blender_code` and
  `get_scene_info` are unchanged. The pack itself says the server's tool list is authoritative.
- Paths in the pack's examples are Windows paths (`C:/export/...`). Here, write to
  `/opt/blender-mcp/work/` or into the repository.
- Poly Haven / Sketchfab / generation tools need hosts that this cloud environment does not allow.

## Check and update

```bash
python3 tools/blender-mcp/check_skills.py        # 94 skills, valid metadata, no broken reference links
```

To move to a newer upstream version: clone it somewhere outside this repository, review
`diff -r <clone>/.claude/skills .claude/skills`, copy with
`cp -r <clone>/.claude/skills/. .claude/skills/`, run the check above (re-apply the fix if it
reports a repeated key), then update the table in this file.
