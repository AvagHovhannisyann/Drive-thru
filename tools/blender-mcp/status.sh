#!/usr/bin/env bash
# Report the state of the Blender MCP service. Read-only: it changes nothing.
#
# Usage: ./status.sh [--mcp] [--quiet]
#   --mcp    also show the Claude Code registration (spawns the stdio server once)
#   --quiet  print nothing, just set the exit code
# Exit code: 0 = healthy (Blender answered a command over the socket), 1 = not healthy.
set -u
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

show_mcp=0
quiet=0
while [ $# -gt 0 ]; do
  case "$1" in
    --mcp) show_mcp=1; shift ;;
    --quiet) quiet=1; shift ;;
    -h|--help) sed -n '2,7p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) bmcp_die "unknown argument: $1" ;;
  esac
done

healthy=1
row()  { [ "$quiet" -eq 1 ] || printf '%-5s %-14s %s\n' "$1" "$2" "$3"; }
ok()   { row "OK" "$1" "$2"; }
warn() { row "WARN" "$1" "$2"; }
fail() { row "FAIL" "$1" "$2"; healthy=0; }
note() { row "" "$1" "$2"; }

# Elapsed time and resident memory of a process, e.g. "up 01:02:03, 512 MB".
proc_usage() {
  local etime rss
  etime="$(ps -o etime= -p "$1" 2>/dev/null | tr -d ' ')"
  rss="$(ps -o rss= -p "$1" 2>/dev/null | tr -d ' ')"
  printf 'up %s, %s MB RSS' "${etime:-?}" "$(( ${rss:-0} / 1024 ))"
}

[ "$quiet" -eq 1 ] || echo "Blender MCP service - $(bmcp_ts)"

# ---- installation ------------------------------------------------------------
if [ -x "$BMCP_BLENDER_BIN" ]; then
  ok "blender" "$("$BMCP_BLENDER_BIN" --version 2>/dev/null | head -n1) at $BMCP_BLENDER_DIR"
else
  fail "blender" "not installed at $BMCP_BLENDER_BIN (run install.sh)"
fi
if [ -f "$BMCP_ADDON_FILE" ]; then
  addon_sha="$(sha256sum "$BMCP_ADDON_FILE" | cut -d' ' -f1)"
  addon_proto="$(grep -m1 -E '^ADDON_PROTOCOL_VERSION\s*=' "$BMCP_ADDON_FILE" | tr -cd '0-9')"
  if [ -z "$BMCP_ADDON_SHA256" ] || [ "$addon_sha" = "$BMCP_ADDON_SHA256" ]; then
    ok "add-on file" "$BMCP_ADDON_FILE (protocol $addon_proto, sha256 ${addon_sha:0:12}..., matches $BMCP_MCP_SPEC)"
  else
    warn "add-on file" "$BMCP_ADDON_FILE sha256 ${addon_sha:0:12}... differs from the pin for $BMCP_MCP_SPEC (re-run install.sh)"
  fi
else
  fail "add-on file" "missing: $BMCP_ADDON_FILE (run install.sh)"
fi

# ---- processes ---------------------------------------------------------------
if pid="$(bmcp_xvfb_pid)"; then
  if bmcp_display_answers; then
    ok "xvfb" "pid $pid on display $BMCP_DISPLAY ($(proc_usage "$pid"))"
  else
    fail "xvfb" "pid $pid is alive but display $BMCP_DISPLAY does not answer"
  fi
else
  lock_pid="$(bmcp_display_lock_pid || true)"
  fail "xvfb" "not running${lock_pid:+ (lock file $BMCP_X_LOCK names pid $lock_pid)}"
fi

if pid="$(bmcp_supervisor_pid)"; then
  ok "supervisor" "pid $pid ($(proc_usage "$pid"))"
else
  fail "supervisor" "not running (Blender will not be restarted if it exits)"
fi

blender_pid="$(bmcp_blender_pid || true)"
if [ -n "$blender_pid" ]; then
  ok "blender proc" "pid $blender_pid ($(proc_usage "$blender_pid")), GUI on $BMCP_DISPLAY"
else
  fail "blender proc" "not running"
fi

# ---- socket ------------------------------------------------------------------
listener="$(bmcp_port_listener || true)"
if [ -n "$listener" ]; then
  addr="${listener%% *}"
  lpid="${listener##* }"
  case "$addr" in
    127.*:"$BMCP_PORT") bound="loopback only" ;;
    *) bound="NOT loopback-only"; ;;
  esac
  if [ "$bound" != "loopback only" ]; then
    fail "socket" "listening on $addr - exposed beyond localhost, stop the service"
  elif [ -n "$blender_pid" ] && [ "$lpid" = "$blender_pid" ]; then
    ok "socket" "$addr ($bound), owned by Blender pid $lpid"
  else
    fail "socket" "$addr is held by pid ${lpid:-?}, which is not the service's Blender"
  fi
else
  fail "socket" "nothing listening on $BMCP_HOST:$BMCP_PORT"
fi

# ---- does Blender actually execute commands? ---------------------------------
if info="$(bmcp_addon_ping 8 2>&1)"; then
  ok "add-on reply" "$(printf '%s' "$info" | "$(bmcp_python)" -c '
import json, sys
d = json.load(sys.stdin)
print("%s v%s, protocol %s, %d commands" % (
    d.get("name"), ".".join(map(str, d.get("addon_version", []))),
    d.get("protocol_version"), len(d.get("capabilities", []))))' 2>/dev/null || echo "$info")"
elif [ -n "$blender_pid" ] && [ -n "$listener" ]; then
  fail "add-on reply" "no answer within 8 s - Blender is busy (a render or long script blocks its main thread) or hung"
else
  fail "add-on reply" "$info"
fi

# ---- what Blender itself reports (heartbeat written by blender_startup.py) ----
if [ -f "$BMCP_STATUS_FILE" ]; then
  "$(bmcp_python)" - "$BMCP_STATUS_FILE" "$quiet" <<'PY'
import json, sys, time
try:
    d = json.load(open(sys.argv[1]))
except (OSError, ValueError) as exc:
    print(f"WARN  heartbeat      unreadable status file: {exc}")
    sys.exit(0)
if sys.argv[2] == "1":
    sys.exit(0)
age = time.time() - d.get("timestamp", 0)
limit = 3 * d.get("watchdog_interval", 5) + 5
tag = "OK" if age <= limit and d.get("ok") else "WARN"
state = "fresh" if age <= limit else "STALE - main thread busy or hung"
print(f"{tag:<5} {'heartbeat':<14} {age:.0f}s old ({state}), watchdog repairs: {d.get('watchdog_repairs')}"
      + (f", last error: {d.get('error')}" if d.get("error") else ""))
gpu = d.get("gpu") or {}
print(f"{'':<5} {'graphics':<14} {gpu.get('backend')} / {gpu.get('renderer')} / {gpu.get('version')}")
print(f"{'':<5} {'rendering':<14} scene '{d.get('scene')}' engine {d.get('render_engine')}, "
      f"Cycles device {d.get('cycles_device')}, GPU present: {d.get('has_gpu')}")
print(f"{'':<5} {'blend file':<14} {d.get('blend_file') or '(unsaved)'}")
print(f"{'':<5} {'privacy':<14} bind {d.get('bind_address')}, remote connections "
      f"{'ON' if d.get('allow_remote_connections') else 'off'}, telemetry consent "
      f"{'ON' if d.get('telemetry_consent') else 'off'}, Blender online access "
      f"{'ON' if d.get('online_access') else 'off'}")
PY
else
  warn "heartbeat" "no status file yet ($BMCP_STATUS_FILE)"
fi

# ---- Claude Code registration (optional, slower) ------------------------------
if [ "$show_mcp" -eq 1 ]; then
  if command -v claude >/dev/null 2>&1; then
    if reg="$(cd "$BMCP_DIR/../.." && timeout 90 claude mcp get "$BMCP_MCP_NAME" 2>&1)"; then
      ok "claude mcp" "server '$BMCP_MCP_NAME' is registered:"
      [ "$quiet" -eq 1 ] || printf '%s\n' "$reg" | sed 's/^/                     /'
      # "Pending approval" is the interactive CLI's trust prompt for .mcp.json servers.
      # Cloud and other non-interactive sessions load project servers without it.
      case "$reg" in *"Pending approval"*)
        note "" "(approval applies to the interactive CLI only; cloud sessions load .mcp.json servers at start)" ;;
      esac
    else
      warn "claude mcp" "server '$BMCP_MCP_NAME' is not registered (run install.sh): $(printf '%s' "$reg" | head -n1)"
    fi
  else
    warn "claude mcp" "claude CLI not found on PATH"
  fi
fi

if [ "$quiet" -ne 1 ]; then
  note "logs" "$BMCP_LOG_DIR/{blender,supervisor,xvfb}.log"
  if [ "$healthy" -eq 1 ]; then echo "RESULT: healthy"; else echo "RESULT: NOT healthy"; fi
fi
[ "$healthy" -eq 1 ]
