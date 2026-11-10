# Blender MCP service (headless Linux / Claude Code cloud sessions)

Runs a live Blender that Claude drives through the Model Context Protocol, with no local PC,
no display and no clicks in Blender's UI.

```
Claude Code ──stdio──▶ mcp-for-blender (MCP server, started by Claude Code via uvx)
                              │ TCP 127.0.0.1:9876  (JSON commands, loopback only)
                              ▼
                 "MCP for Blender" add-on  ─ inside ─▶  Blender 4.5 LTS GUI process
                                                              │ X11
                                                              ▼
                                                   Xvfb virtual display :99
```

The Blender GUI process is persistent and supervised (restarted if it dies). It is *not* a
one-shot `blender -b` process: the add-on cannot serve commands in background mode.
Separate `blender -b` processes remain the right tool for long renders (see "Rendering").

## Quick start

All commands are run from the repository root.

```bash
tools/blender-mcp/install.sh     # once per container: ~1 min on a fresh one, seconds afterwards
tools/blender-mcp/start.sh       # Xvfb + Blender + add-on socket; waits until Blender answers
tools/blender-mcp/status.sh      # health report, exit code 0 = healthy
```

End-to-end check through the MCP protocol (builds a test scene, saves a `.blend`, renders a PNG):

```bash
uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_e2e_test.py
```

## What is installed (verified 2026-11-10)

| Component | Version | Where | Integrity |
|---|---|---|---|
| Blender (official build) | 4.5.16 LTS, build `3f6797307da5` | `/opt/blender-dl/blender-4.5.16-linux-x64` (`/opt/blender-dl/current`, `blender` on PATH) | tarball SHA-256 `23432b06…84b10c11`, checked against the official `blender-4.5.16.sha256` |
| MCP server | `mcp-for-blender` 2.2.7 (PyPI; upstream `ahujasid/blender-mcp`, formerly `blender-mcp`) | uv cache, run as `/root/.local/bin/uvx mcp-for-blender@2.2.7` | wheel SHA-256 `2fd2ad6f…1640472c` (PyPI) |
| Add-on | "MCP for Blender" `bl_info` 1.8, protocol 15 | `/opt/blender-mcp/userdata/scripts/addons/blender_mcp.py` | SHA-256 `a7b3873a…a121828b` = file bundled in the 2.2.7 wheel = upstream `main/addon.py` on that date |
| MCP SDK | `mcp` 1.30.0 (resolved by uvx) | uv cache | — |
| uv / uvx | 0.11.32 | `/root/.local/bin` | preinstalled in the image |
| Xvfb | 21.1.12 | apt | — |
| OpenGL | Mesa 25.2.8 llvmpipe, OpenGL 4.5 core (software) | apt | — |
| Claude Code CLI | 2.1.322 | `/opt/node22/bin/claude` | — |

Host at verification time: Ubuntu 24.04.5, x86_64, 4 vCPU, 15 GB RAM, no GPU.
Pins live in [`config.env`](config.env); the full machine-readable record of an install is
written to `/opt/blender-mcp/versions.json` (snapshot of the verified run:
[`versions.lock.json`](versions.lock.json)).

## Commands

| Command | What it does |
|---|---|
| `tools/blender-mcp/install.sh` | apt packages, Blender (download + SHA-256 check), add-on, Claude Code registration, version record. Idempotent. `--no-register` skips Claude Code; `--force-addon` reinstalls the add-on. |
| `tools/blender-mcp/start.sh` | Starts Xvfb `:99`, the supervisor and Blender; waits (default 120 s, `--wait N`) until the add-on answers a command; prints status. Safe to repeat. |
| `tools/blender-mcp/stop.sh` | Stops supervisor, Blender, Xvfb. `--keep-xvfb` leaves the display up. |
| `tools/blender-mcp/restart.sh` | `stop.sh` then `start.sh`. `--keep-xvfb` restarts Blender only. |
| `tools/blender-mcp/status.sh` | Read-only health report. `--mcp` also shows the Claude Code registration; `--quiet` only sets the exit code. |
| `python3 tools/blender-mcp/check_skills.py` | Integrity check of the Blender Skills pack in `.claude/skills/`. |
| `uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_e2e_test.py` | Full-chain test through MCP. Outputs in `/opt/blender-mcp/test-output/`. `--keep-scene` leaves the test scene open. |
| `uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_call.py …` | Call any tool of the MCP server from the terminal (see below). |

`supervise.sh`, `blender_startup.py` and `lib.sh` are internal; do not run them directly.

## Restart procedure

| Situation | Do this |
|---|---|
| New session / fresh container (nothing installed) | `tools/blender-mcp/install.sh && tools/blender-mcp/start.sh` |
| Session resumed after being idle (container was suspended) | `tools/blender-mcp/start.sh`. Files are back, processes are not; the stale X lock and pid files left behind are detected and cleared. |
| Service stopped, or `status.sh` says NOT healthy | `tools/blender-mcp/restart.sh` |
| Blender crashed or was killed | Nothing: the supervisor restarts it after 5 s (then 10/20/40/60 s). It gives up after 5 exits in 5 minutes; then read `blender.log` and run `restart.sh`. |
| A script reset Blender (`wm.read_factory_settings`) | Nothing: the watchdog re-enables the add-on and reopens the socket within ~5 s. The MCP call that did the reset itself returns "connection closed"; the next call works. |
| Xvfb died | Nothing: within ~20 s the supervisor stops the now window-less Blender and starts both again. |
| Blender is unresponsive but alive | `status.sh` reports "busy or hung". If it is a long render, wait. Otherwise `tools/blender-mcp/restart.sh` (the unsaved scene is lost). |
| Clean slate | `tools/blender-mcp/stop.sh && rm -rf /opt/blender-mcp/userdata/config && tools/blender-mcp/start.sh` (resets the service's private Blender preferences). |

Restarting Blender discards the live scene. Save first if it matters, through MCP:
`bpy.ops.wm.save_as_mainfile(filepath="/opt/blender-mcp/work/scene.blend")`.

Stale X locks: `/tmp/.X99-lock` and `/tmp/.X11-unix/X99` are removed only after the scripts
have verified that the PID in the lock is not a live X server, that no X server process is
running for that display, and that nothing accepts connections on its socket. If a live process
owns the display the scripts stop with an error and change nothing.

## Logs and files

Everything the service writes is under `/opt/blender-mcp` (outside the repository):

| Path | Content |
|---|---|
| `logs/blender.log` | Blender stdout/stderr, add-on messages, `[bmcp-startup]` lines |
| `logs/supervisor.log` | starts, exits, restarts, display recovery |
| `logs/xvfb.log` | X server output (keysym warnings at start are harmless) |
| `run/*.pid`, `run/blender-status.json` | PIDs and the heartbeat Blender writes every 5 s |
| `userdata/` | the service's private Blender config + scripts (`BLENDER_USER_RESOURCES`); holds the add-on |
| `tmp/` | Blender temp files (`quit.blend`, viewport captures) |
| `work/` | scratch space for scenes, frames and exports (not kept when the container is reclaimed) |
| `test-output/` | `mcp_test_scene.blend`, `mcp_test_render.png`, `mcp_test_look.png`, `mcp_e2e_report.json` |
| `versions.json`, `backups/` | install record; copies of `~/.claude.json` taken before each registration change |

Logs are appended across restarts and survive for the life of the container.
Follow them with `tail -f /opt/blender-mcp/logs/blender.log`.

## How the add-on is started without the sidebar button

[`blender_startup.py`](blender_startup.py) is passed to Blender with `--python`. The names
below were read from the installed add-on (2.2.7), not assumed:

- enables the add-on: `addon_utils.enable("blender_mcp", default_set=True, persistent=True)`
- pins the listener: add-on preference `bind_address = "127.0.0.1"`, `allow_remote_connections = False`,
  `Scene.blendermcp_port = 9876`
- starts the socket with the add-on's own operator: `bpy.ops.blendermcp.start_server()`
- verifies `bpy.types.blendermcp_server.running`, host and port
- repeats the check every 5 s (`bpy.app.timers`, persistent) and after every file load

The add-on also has its own auto-start (`Scene.blendermcp_auto_start_server`, default on); the
startup script does not rely on it.

Service defaults chosen for this environment:

- **Loopback only.** The add-on executes arbitrary Python for whoever connects. Scripts refuse a
  non-`127.x` `BMCP_HOST`, and `status.sh` fails if the listener is bound anywhere else.
  Xvfb runs with `-nolisten tcp`.
- **No telemetry, no self-update.** `DISABLE_TELEMETRY=true` for the MCP server,
  `BLENDERMCP_NO_UPDATE_CHECK=1` for the add-on (it would otherwise offer to replace itself from
  GitHub `main`); telemetry consent stays off; Blender's own online access is off.
- **Private Blender profile.** `BLENDER_USER_RESOURCES=/opt/blender-mcp/userdata`, so plain
  `blender -b …` batch renders (e.g. `design/3d/render_all.sh`) run without the add-on.
- **CPU rendering.** No GPU here: the UI draws with llvmpipe and the unsaved default scene is
  switched from EEVEE to Cycles on CPU (`BMCP_DEFAULT_ENGINE`, set `KEEP` to disable). Saved
  `.blend` files are never modified.

## Using it from Claude Code

The server is registered in the repository's project-scoped [`.mcp.json`](../../.mcp.json).
`install.sh` keeps that entry in step with `config.env`; it was created with:

```bash
claude mcp add --scope project blender \
  -e DISABLE_TELEMETRY=true -e BLENDER_HOST=127.0.0.1 -e BLENDER_PORT=9876 \
  -e BLENDERMCP_ADDONS_DIR=/opt/blender-mcp/userdata/scripts/addons \
  -- /root/.local/bin/uvx mcp-for-blender@2.2.7
```

This is upstream's `claude mcp add blender uvx mcp-for-blender` with an absolute `uvx` path, a
pinned version (so server and add-on always match) and explicit settings. Other MCP servers are
not touched. Remove it with `claude mcp remove blender -s project`.

Tools offered by the server: `get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`,
`search_assets`, `import_asset`, `generate_3d`, `disable_telemetry`, `record_trajectory_feedback`.
In a Claude Code session they appear as `mcp__blender__<tool>`.

**When the tools are available.** Claude Code reads `.mcp.json` (and `.claude/skills/`) when a
session starts.

- A Claude Code process started in this repository after the files existed loaded the server
  (`blender: connected, source: project`), all nine `mcp__blender__*` tools and all 94 skills
  (checked 2026-11-10 with the non-interactive loader of Claude Code 2.1.322). The Claude Code
  documentation says cloud sessions load a repository's `.mcp.json` servers and `.claude/skills/`
  the same way, without an approval step.
- `claude mcp get blender` reports `Pending approval` for a project-scoped server. That is the
  interactive CLI's trust prompt; it does not apply to cloud or other non-interactive sessions.
- Observed in a cloud session on 2026-11-10: after the session was resumed, the nine
  `mcp__blender__*` tools and the 94 skills were available natively, and `get_scene_info`,
  `execute_blender_code` and `look` returned results from the live Blender.
- A session that was already running when the files were added does not gain the tools or the
  skills (observed). It can still drive Blender *through MCP* from the terminal:

```bash
PY="uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_call.py"
$PY --list
$PY get_scene_info '{"fields": ["location", "size", "settings"]}'
$PY execute_blender_code --code 'import bpy; print(bpy.app.version_string, [o.name for o in bpy.data.objects])'
$PY execute_blender_code --code-file path/to/script.py
$PY look '{"mode": "camera", "max_size": 800}' --save-images /opt/blender-mcp/tmp
```

`mcp_call.py` reads the registered command from Claude Code's config (`.mcp.json` included) and
starts the server the same way Claude Code does, so it exercises the identical path.

The MCP server is only a bridge: its tools answer "could not connect to Blender" until the
service is running (`tools/blender-mcp/start.sh`). [`CLAUDE.md`](../../CLAUDE.md) tells every
session in this repository to start it before the first Blender call.

## Blender Skills pack

[`.claude/skills/`](../../.claude/skills/README.md) holds the 94 skills of
[arjun988/blender-skills](https://github.com/arjun988/blender-skills) 1.3.0 (MIT), copied from
commit `904f095` after review: markdown only, no scripts, hooks or settings. Start a Blender task
with `blender-director`. The skills run through the tools above; their `get_viewport_screenshot`
is `look` in this server version. Integrity check:

```bash
python3 tools/blender-mcp/check_skills.py     # 94 skills, valid metadata, no broken reference links
```

## Rendering

- One MCP command may run for at most **180 s** (fixed in the server and add-on). A render started
  with `bpy.ops.render.render()` inside `execute_blender_code` blocks Blender until it finishes;
  past 180 s the call returns a timeout although Blender keeps rendering.
- Measured here (4 vCPU, default cube scene, 640×360): Cycles 16 samples 1.2 s, Workbench 0.1 s,
  EEVEE 24.6 s (software OpenGL). Prefer Cycles on CPU.
- For anything long (animation, high resolution) save the scene through MCP and render in a
  separate background Blender, detached from the service:

```bash
# through MCP:  bpy.ops.wm.save_as_mainfile(filepath="/opt/blender-mcp/work/shot.blend", copy=True)
mkdir -p /opt/blender-mcp/work/frames
nohup blender -b /opt/blender-mcp/work/shot.blend -o /opt/blender-mcp/work/frames/frame_#### \
  -F PNG -s 1 -e 240 -a > /opt/blender-mcp/logs/render-shot.log 2>&1 &
tail -f /opt/blender-mcp/logs/render-shot.log      # "Saved: ..." per frame
```

  Argument order matters to Blender: `-S <scene>`, `-o`, `-F` must come before `-f`/`-a`.
- Scripting gotcha found while testing: if a script creates objects with the data API in a
  brand-new scene and only then switches the window to it (`window.scene = scene`), their
  `matrix_world` stays stale, `get_scene_info` reports them at the origin and `look` through the
  camera is blank. Switch the window to the new scene first, then add objects.

## Configuration

Edit [`config.env`](config.env) or override per command (`BMCP_PORT=9877 tools/blender-mcp/start.sh`).

| Variable | Default | Meaning |
|---|---|---|
| `BMCP_BLENDER_VERSION` / `BMCP_BLENDER_SHA256` | `4.5.16` / pinned | Blender build and its tarball hash (`official` = fetch the hash from download.blender.org) |
| `BMCP_MCP_VERSION` / `BMCP_ADDON_SHA256` | `2.2.7` / pinned | MCP package and the hash of its bundled add-on |
| `BMCP_HOME` | `/opt/blender-mcp` | logs, run state, private Blender profile, test output |
| `BMCP_DISPLAY` / `BMCP_SCREEN` | `:99` / `1920x1080x24` | virtual display |
| `BMCP_HOST` / `BMCP_PORT` | `127.0.0.1` / `9876` | add-on socket (loopback enforced) |
| `BMCP_DEFAULT_ENGINE` | `CYCLES` | engine for the unsaved default scene when there is no GPU |
| `BMCP_WATCHDOG_INTERVAL` | `5` | seconds between in-Blender socket checks |
| `BMCP_DISPLAY_CHECK_INTERVAL` | `10` | seconds between the supervisor's display checks |
| `BMCP_MAX_RESTARTS` / `BMCP_RESTART_WINDOW` | `5` / `300` | crash-loop guard |
| `BMCP_CLAUDE_SCOPE` / `BMCP_MCP_NAME` | `project` / `blender` | Claude Code registration (`project` = the committed `.mcp.json`) |

Changing host, port or the MCP version: re-run `install.sh` so `.mcp.json` matches, then commit it.

## Upgrading

```bash
# Blender: pick a release from https://download.blender.org/release/Blender4.5/ and copy its
# linux-x64 hash from blender-<version>.sha256 into config.env, then:
tools/blender-mcp/install.sh && tools/blender-mcp/restart.sh

# MCP server + add-on: set BMCP_MCP_VERSION and clear BMCP_ADDON_SHA256 in config.env, run
# install.sh, review the new add-on, record its hash (printed as bundled_addon_sha256), then:
tools/blender-mcp/install.sh && tools/blender-mcp/restart.sh
uvx --from mcp-for-blender==<new version> python tools/blender-mcp/mcp_e2e_test.py
```

The earlier render scripts default to `/opt/blender-dl/blender-4.5.9-linux-x64/blender`; run them
against this install with `BLENDER=/opt/blender-dl/current/blender bash design/3d/render_all.sh`.

## Environment limits (Claude Code cloud sessions)

- **Network.** The default environment only allows package registries; `download.blender.org`
  is refused by the egress proxy (HTTP 403). The personal environment "Drive-thru" adds exactly
  that host. Asset hosts used by optional add-on features (Poly Haven, Sketchfab, …) are not
  allowed; those tools will fail until their hosts are added to the environment.
- **Persistence.** There is no systemd (PID 1 is the sandbox init). The service is kept alive by
  its own supervisor and survives between turns and commands, but only for the life of the
  container. A new container gets Blender back from the "Drive-thru" environment's setup script
  (it runs `install.sh`), and the MCP registration and skills from the repository itself.
  Running processes are never carried over: start the service in each new session with
  `tools/blender-mcp/start.sh` (the Claude Code documentation's advice for background services is
  exactly that, or a `SessionStart` hook). Observed on 2026-11-10: after about 50 idle minutes
  the container was suspended; on resume the disk (including `/opt/blender-dl` and
  `/opt/blender-mcp`) was back, every process was gone, and `start.sh` had the service healthy
  again in 8 s. A brand-new session starts from the environment's snapshot instead and may not
  have those directories.
- **Session start only.** MCP servers and skills are picked up when a session starts, not by a
  session that is already running (see "Using it from Claude Code").

## Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `install.sh`: curl error 56 / HTTP 403 for download.blender.org | Session is not on an environment that allows the host. Switch to "Drive-thru" or add the host. |
| `start.sh`: "display :99 is owned by another live process" | Another X server uses `:99`. Stop it or run with `BMCP_DISPLAY=:98`. |
| `start.sh`: "port 9876 is already in use by another process" | Something else listens there. Free it or change `BMCP_PORT` (and re-run `install.sh`). |
| MCP tool: "Could not connect to Blender" | Service not running: `tools/blender-mcp/start.sh`. |
| MCP tool: "Timeout waiting for Blender response" | The command ran longer than 180 s (usually a render). Use a background render. |
| `status.sh`: add-on reply FAIL, heartbeat STALE, process alive | Blender's main thread is busy or hung; wait for a render, else `restart.sh`. |
| `get_addon_status` shows `up_to_date: false` | Server and add-on versions differ: `tools/blender-mcp/install.sh --force-addon && tools/blender-mcp/restart.sh`. |
| `GHOST/Wayland: error …` in `blender.log` | Harmless; Blender falls back to X11. |
| First Blender tool call of a session waits, then fails with "the server asked the user a question" after 60 s | The upstream server shows a one-time telemetry opt-in dialog to clients that support dialogs (Claude Code does), even though `DISABLE_TELEMETRY=true` already stops all collection here. Answer it in the app, or ignore it: only that one call fails, later calls work, and it is asked once per session until an explicit yes/no is stored in `~/.config/blender-mcp/consent_prompt.json`. |
