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
| `uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_e2e_test.py` | Full-chain test through MCP. Outputs in `/opt/blender-mcp/test-output/`. `--keep-scene` leaves the test scene open. |
| `uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_call.py …` | Call any tool of the MCP server from the terminal (see below). |

`supervise.sh`, `blender_startup.py` and `lib.sh` are internal; do not run them directly.

## Restart procedure

| Situation | Do this |
|---|---|
| New session / fresh container (nothing installed) | `tools/blender-mcp/install.sh && tools/blender-mcp/start.sh` |
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

Registered (local scope, project `/home/user/Drive-thru`) by `install.sh` with:

```bash
claude mcp add --scope local blender \
  -e DISABLE_TELEMETRY=true -e BLENDER_HOST=127.0.0.1 -e BLENDER_PORT=9876 \
  -e BLENDERMCP_ADDONS_DIR=/opt/blender-mcp/userdata/scripts/addons \
  -- /root/.local/bin/uvx mcp-for-blender@2.2.7
```

This is upstream's `claude mcp add blender uvx mcp-for-blender` with an absolute `uvx` path, a
pinned version (so server and add-on always match) and explicit settings. Check it with
`claude mcp get blender` (expect `Status: ✓ Connected`); remove it with
`claude mcp remove blender -s local`. Other MCP servers are not touched.

Tools offered by the server: `get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`,
`search_assets`, `import_asset`, `generate_3d`, `disable_telemetry`, `record_trajectory_feedback`.
In a Claude Code session they appear as `mcp__blender__<tool>`.

**Limitation.** Claude Code connects MCP servers when a session starts. A session that was already
running when the server was registered does not gain the `mcp__blender__*` tools (observed in the
session that built this). Such a session can still drive Blender *through MCP* from the terminal:

```bash
PY="uvx --from mcp-for-blender==2.2.7 python tools/blender-mcp/mcp_call.py"
$PY --list
$PY get_scene_info '{"fields": ["location", "size", "settings"]}'
$PY execute_blender_code --code 'import bpy; print(bpy.app.version_string, [o.name for o in bpy.data.objects])'
$PY execute_blender_code --code-file path/to/script.py
$PY look '{"mode": "camera", "max_size": 800}' --save-images /opt/blender-mcp/tmp
```

`mcp_call.py` reads the registered command from Claude Code's config and starts the server the
same way Claude Code does, so it exercises the identical path.

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
| `BMCP_CLAUDE_SCOPE` / `BMCP_MCP_NAME` | `local` / `blender` | Claude Code registration |

Changing host or port: also re-run `install.sh` so the registered command matches.

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
  container. A reclaimed container loses `/opt/blender-dl`, `/opt/blender-mcp` and the Claude Code
  registration; the scripts in this directory restore all of it (see "Restart procedure").
- **Native tools.** See the limitation under "Using it from Claude Code".

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
