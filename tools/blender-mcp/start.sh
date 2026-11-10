#!/usr/bin/env bash
# Start the persistent Blender MCP service:
#   Xvfb (virtual display)  ->  supervisor  ->  Blender GUI + add-on socket on loopback
# Safe to run repeatedly: anything already running and healthy is left alone.
#
# Usage: ./start.sh [--wait SECONDS]      (default: wait up to 120 s for the socket)
set -u
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

wait_seconds=120
while [ $# -gt 0 ]; do
  case "$1" in
    --wait) wait_seconds="${2:?--wait needs a number}"; shift 2 ;;
    -h|--help) sed -n '2,7p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) bmcp_die "unknown argument: $1" ;;
  esac
done

bmcp_require_loopback
[ -x "$BMCP_BLENDER_BIN" ]  || bmcp_die "Blender not found at $BMCP_BLENDER_BIN - run $BMCP_DIR/install.sh"
[ -f "$BMCP_ADDON_FILE" ]   || bmcp_die "add-on not found at $BMCP_ADDON_FILE - run $BMCP_DIR/install.sh"
command -v Xvfb >/dev/null  || bmcp_die "Xvfb is not installed - run $BMCP_DIR/install.sh"
bmcp_mkdirs

# ---- 1. virtual display ------------------------------------------------------
# Reuses our running Xvfb, adopts one whose pid file was lost, clears a stale lock only
# when no live process owns the display, and refuses to touch a display owned by
# anything else (see bmcp_ensure_xvfb / bmcp_clear_stale_display in lib.sh).
bmcp_ensure_xvfb || bmcp_die "no usable X display $BMCP_DISPLAY (reason logged above)"
bmcp_log "Xvfb serving $BMCP_DISPLAY (pid $(bmcp_xvfb_pid))"

# ---- 2. Blender under its supervisor -----------------------------------------
if sup="$(bmcp_supervisor_pid)"; then
  bmcp_log "supervisor already running (pid $sup)"
else
  # Without a supervisor a leftover service Blender must not keep the port.
  if old="$(bmcp_blender_pid)"; then
    bmcp_log "stopping unsupervised Blender left from an earlier run (pid $old)"
    bmcp_terminate "$old" 10
  fi
  listener="$(bmcp_port_listener || true)"
  if [ -n "$listener" ]; then
    bmcp_die "port $BMCP_PORT is already in use by another process ($listener). Not touching it - free the port or set BMCP_PORT."
  fi
  rm -f "$BMCP_STATUS_FILE"
  bmcp_log "starting supervisor + Blender GUI on $BMCP_DISPLAY"
  setsid nohup "$BMCP_DIR/supervise.sh" >> "$BMCP_LOG_DIR/supervisor.log" 2>&1 < /dev/null &
fi

# ---- 3. wait until the add-on answers a real command -------------------------
bmcp_log "waiting up to ${wait_seconds}s for the add-on on $BMCP_HOST:$BMCP_PORT"
deadline=$(( $(date +%s) + wait_seconds ))
while :; do
  if info="$(bmcp_addon_ping 5 2>/dev/null)"; then
    bmcp_log "add-on answered: $info"
    break
  fi
  if ! bmcp_supervisor_pid >/dev/null; then
    tail -n 25 "$BMCP_LOG_DIR/supervisor.log" "$BMCP_LOG_DIR/blender.log" 2>/dev/null
    bmcp_die "supervisor is not running - Blender failed to start (log tail above)"
  fi
  if [ "$(date +%s)" -ge "$deadline" ]; then
    tail -n 25 "$BMCP_LOG_DIR/blender.log" 2>/dev/null
    bmcp_die "add-on did not answer within ${wait_seconds}s (log tail above; run status.sh for details)"
  fi
  sleep 1
done

exec "$BMCP_DIR/status.sh"
