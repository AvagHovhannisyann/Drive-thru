# Notes for Claude

## Blender (live MCP service + skills)

- Blender work runs against a live Blender 5.2 LTS driven through the `blender` MCP server
  (`mcp__blender__*` tools, registered in `.mcp.json`). The server only bridges to Blender; the
  Blender service itself has to be running. Before the first Blender call in a session:
  `tools/blender-mcp/status.sh --quiet || tools/blender-mcp/start.sh`
  If Blender is not installed in this container, run `tools/blender-mcp/install.sh` first
  (needs the "Drive-thru" cloud environment, which allows `download.blender.org`).
  Operations guide: `tools/blender-mcp/README.md`.
- If the `mcp__blender__*` tools are not loaded in the session, call the same server from the
  terminal: `uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_call.py --list`
- The first `mcp__blender__*` call of a session can show the user a telemetry opt-in dialog from
  the upstream server and fail after 60 s if nobody answers. Do not answer it for the user and do
  not retry that call in the same turn; say what happened and carry on with the other tools
  (collection is disabled here by `DISABLE_TELEMETRY=true` whatever the answer).
- Skills: `.claude/skills/` holds 178 skills in 13 packs (`tools/skills/check.py` lists them). For any
  video or film request start with `film-studio`; for a single asset or a style question start with
  `blender-director`. The packs' `get_viewport_screenshot` is the `look` tool in this server version.
- Headless Linux without a GPU: render with Cycles on CPU. One MCP call may run at most 180 s,
  so long renders go to a separate `blender -b` process (see the README, "Rendering").
- Write Blender outputs to `/opt/blender-mcp/work/` or into the repository, never to `C:/` paths.
- The batch scripts in `design/3d/` expect `BLENDER=/opt/blender-dl/current/blender`.

## Films (tools/film)

- Read the `film-studio` skill first. Toolchain: `tools/film/install.sh` (Python environment in
  `/opt/film-studio/venv`, fonts, sound tools). Commands and limits: `tools/film/README.md`.
- This machine has 4 CPU threads and no GPU: about 0.7 million path-tracing samples per second. Plan
  films as plate shots (one render with light groups, then `tools/film/comp.py`) and keep real camera
  moves short. Give the user render-time numbers before starting a long render.
- Long renders run in the background and are resumable; the container stops all processes when the
  session goes idle, so re-run the same command after a resume.
- Outside libraries (allowed in the "Drive-thru" environment): `tools/film/assets.py` for Poly Haven
  HDRIs, textures and models (CC0), `tools/film/sounds.py` for Mixkit effects and music (never commit
  those files). They land in `/opt/film-studio/assets/`.
- Work files go to `/opt/film-studio/work/<project>/`; only scripts, pages, shot and cue files belong
  in the repository. Never commit rendered frames, plates or videos (a small contact sheet as a record is fine).
