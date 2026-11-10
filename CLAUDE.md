# Notes for Claude

## Blender (live MCP service + skills)

- Blender work runs against a live Blender 4.5 LTS driven through the `blender` MCP server
  (`mcp__blender__*` tools, registered in `.mcp.json`). The server only bridges to Blender; the
  Blender service itself has to be running. Before the first Blender call in a session:
  `tools/blender-mcp/status.sh --quiet || tools/blender-mcp/start.sh`
  If Blender is not installed in this container, run `tools/blender-mcp/install.sh` first
  (needs the "Drive-thru" cloud environment, which allows `download.blender.org`).
  Operations guide: `tools/blender-mcp/README.md`.
- If the `mcp__blender__*` tools are not loaded in the session, call the same server from the
  terminal: `uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_call.py --list`
- Skills: `.claude/skills/` holds the Blender Skills pack; start with `blender-director`.
  Its `get_viewport_screenshot` is the `look` tool in this server version.
- Headless Linux without a GPU: render with Cycles on CPU. One MCP call may run at most 180 s,
  so long renders go to a separate `blender -b` process (see the README, "Rendering").
- Write Blender outputs to `/opt/blender-mcp/work/` or into the repository, never to `C:/` paths.
- The batch scripts in `design/3d/` expect `BLENDER=/opt/blender-dl/current/blender`.
