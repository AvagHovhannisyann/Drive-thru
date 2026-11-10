#!/usr/bin/env bash
# Stop the Blender MCP service: supervisor, Blender, then Xvfb.
# Only processes verified to be the ones this service started are signalled.
#
# Usage: ./stop.sh [--keep-xvfb]     (--keep-xvfb leaves the virtual display running)
set -u
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

keep_xvfb=0
while [ $# -gt 0 ]; do
  case "$1" in
    --keep-xvfb) keep_xvfb=1; shift ;;
    -h|--help) sed -n '2,5p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) bmcp_die "unknown argument: $1" ;;
  esac
done
bmcp_mkdirs
rc=0

# 1. Supervisor first, so it does not restart Blender. It forwards TERM to Blender
#    and waits for it, so allow for Blender's own shutdown time.
if pid="$(bmcp_supervisor_pid)"; then
  bmcp_log "stopping supervisor (pid $pid)"
  bmcp_terminate "$pid" 25 || { bmcp_log "supervisor pid $pid did not exit"; rc=1; }
else
  bmcp_log "supervisor not running"
fi
rm -f "$BMCP_SUPERVISOR_PIDFILE"

# 2. Blender, if it outlived the supervisor (or the supervisor was already gone).
blender_pids=()
pid="$(bmcp_blender_pid || true)"
[ -n "$pid" ] && blender_pids+=("$pid")
# Also catch a service Blender whose pid file was lost.
while read -r pid; do
  [ -n "$pid" ] && blender_pids+=("$pid")
done < <(pgrep -f -- "--python $BMCP_STARTUP_SCRIPT" 2>/dev/null)
for pid in "${blender_pids[@]:-}"; do
  bmcp_is_our_blender "$pid" || continue   # verified again; also skips duplicates already stopped
  bmcp_log "stopping Blender (pid $pid)"
  bmcp_terminate "$pid" 15 || { bmcp_log "Blender pid $pid did not exit"; rc=1; }
done
rm -f "$BMCP_BLENDER_PIDFILE" "$BMCP_STATUS_FILE"

# 3. Xvfb.
if [ "$keep_xvfb" -eq 1 ]; then
  bmcp_log "leaving Xvfb running (--keep-xvfb)"
else
  if pid="$(bmcp_xvfb_pid)"; then
    bmcp_log "stopping Xvfb on $BMCP_DISPLAY (pid $pid)"
    bmcp_terminate "$pid" 10 || { bmcp_log "Xvfb pid $pid did not exit"; rc=1; }
  else
    bmcp_log "Xvfb (ours) not running"
  fi
  rm -f "$BMCP_XVFB_PIDFILE"
  # Xvfb removes its own lock on a clean exit. If one is left behind it is deleted
  # only when no live process owns the display (verified inside the helper).
  bmcp_clear_stale_display || true
fi

listener="$(bmcp_port_listener || true)"
if [ -n "$listener" ]; then
  bmcp_log "note: port $BMCP_PORT still has a listener that is not this service: $listener"
fi
if [ "$rc" -eq 0 ]; then bmcp_log "stopped"; else bmcp_log "stopped with warnings"; fi
exit "$rc"
