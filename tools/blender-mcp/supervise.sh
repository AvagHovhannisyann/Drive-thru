#!/usr/bin/env bash
# Supervisor for the live Blender GUI process. Started by start.sh (detached); do not
# run it by hand. It launches Blender on the virtual display with the startup script,
# and if Blender exits unexpectedly (crash, OOM kill, a script calling quit) it starts
# it again with a growing delay. It stops when it receives TERM (stop.sh) or when
# Blender keeps dying (crash-loop guard), so a broken install cannot spin forever.
set -u
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

bmcp_require_loopback
bmcp_mkdirs
echo $$ > "$BMCP_SUPERVISOR_PIDFILE"

child=""
stopping=0
on_term() {
  stopping=1
  if [ -n "$child" ] && bmcp_pid_alive "$child"; then
    kill -TERM "$child" 2>/dev/null
  fi
}
trap on_term TERM INT

has_gpu=0
gl_env=()
if bmcp_has_gpu; then
  has_gpu=1
else
  # No GPU: draw the UI with Mesa's software rasteriser (llvmpipe, OpenGL 4.5).
  gl_env=(LIBGL_ALWAYS_SOFTWARE=1)
fi

# Line-buffer Blender's C-level output so the log is live, when stdbuf is available.
buffer_cmd=()
command -v stdbuf >/dev/null 2>&1 && buffer_cmd=(stdbuf -oL -eL)

IFS=x read -r screen_w screen_h _depth <<< "$BMCP_SCREEN"

restart_times=()
delay=5
bmcp_log "supervisor pid $$ starting (display $BMCP_DISPLAY, socket $BMCP_HOST:$BMCP_PORT, gpu=$has_gpu)"

# Runs in a background subshell that `exec` turns into Blender itself, so $! below is
# Blender's own PID. Environment of the service's Blender:
#   BLENDER_USER_RESOURCES     private config/scripts dir (holds the add-on)
#   BLENDERMCP_NO_UPDATE_CHECK the add-on must not replace itself from GitHub main
#   DISABLE_TELEMETRY          belt and braces; the MCP server reads the same switch
#   TMPDIR                     keeps quit.blend and add-on temp files in BMCP_HOME
launch_blender() {
  exec env -u WAYLAND_DISPLAY \
    DISPLAY="$BMCP_DISPLAY" \
    XDG_RUNTIME_DIR="$BMCP_RUN_DIR/xdg" \
    TMPDIR="$BMCP_TMP_DIR" \
    BLENDER_USER_RESOURCES="$BMCP_USERDATA" \
    BLENDERMCP_NO_UPDATE_CHECK=1 \
    DISABLE_TELEMETRY=true \
    BMCP_ADDON_MODULE="$BMCP_ADDON_MODULE" \
    BMCP_HOST="$BMCP_HOST" \
    BMCP_PORT="$BMCP_PORT" \
    BMCP_STATUS_FILE="$BMCP_STATUS_FILE" \
    BMCP_WATCHDOG_INTERVAL="$BMCP_WATCHDOG_INTERVAL" \
    BMCP_DEFAULT_ENGINE="$BMCP_DEFAULT_ENGINE" \
    BMCP_HAS_GPU="$has_gpu" \
    "${gl_env[@]}" \
    "${buffer_cmd[@]}" "$BMCP_BLENDER_BIN" \
      --window-geometry 0 0 "$screen_w" "$screen_h" \
      --no-window-focus \
      --python "$BMCP_STARTUP_SCRIPT" \
      >> "$BMCP_LOG_DIR/blender.log" 2>&1
}

while [ "$stopping" -eq 0 ]; do
  started=$(date +%s)
  if bmcp_ensure_xvfb; then          # also brings Xvfb back if it died
    bmcp_log "launching $BMCP_BLENDER_BIN"
    launch_blender &
    child=$!
    echo "$child" > "$BMCP_BLENDER_PIDFILE"
    bmcp_log "blender pid $child"

    # Watch Blender until it is gone. Two things are handled besides a plain exit:
    #  * stop requested: TERM was forwarded by on_term; escalate to KILL after 10 s.
    #  * display lost: if Xvfb dies, Blender does not exit - it hangs with its socket
    #    still open. It can never get its window back, so it is stopped and both are
    #    started again. This check looks at the DISPLAY only; a Blender that is merely
    #    busy (a long render blocks its main thread) is never touched.
    ticks=0
    stop_ticks=0
    display_misses=0
    while bmcp_pid_alive "$child"; do
      sleep 1
      ticks=$(( ticks + 1 ))
      if [ "$stopping" -ne 0 ]; then
        stop_ticks=$(( stop_ticks + 1 ))
        [ "$stop_ticks" -eq 10 ] && { bmcp_log "blender pid $child ignored TERM for 10s - sending KILL"; kill -KILL "$child" 2>/dev/null; }
        continue
      fi
      [ $(( ticks % BMCP_DISPLAY_CHECK_INTERVAL )) -eq 0 ] || continue
      if bmcp_xvfb_pid >/dev/null && bmcp_display_answers; then
        display_misses=0
      else
        display_misses=$(( display_misses + 1 ))
        if [ "$display_misses" -ge 2 ]; then
          bmcp_log "display $BMCP_DISPLAY is gone but blender pid $child is still alive - stopping it so display and Blender can be restarted"
          bmcp_terminate "$child" 5
        fi
      fi
    done
    wait "$child"
    code=$?
    rm -f "$BMCP_BLENDER_PIDFILE" "$BMCP_STATUS_FILE"
    ran=$(( $(date +%s) - started ))
    if [ "$stopping" -ne 0 ]; then
      bmcp_log "blender pid $child stopped on request (exit $code)"
      break
    fi
    bmcp_log "blender pid $child exited unexpectedly (exit $code) after ${ran}s"
  else
    ran=0
    [ "$stopping" -ne 0 ] && break
    bmcp_log "display $BMCP_DISPLAY is not available - Blender not launched"
  fi

  # Crash-loop guard: count restarts inside the sliding window.
  now=$(date +%s)
  kept=()
  for t in "${restart_times[@]:-}"; do
    [ -n "$t" ] && [ $(( now - t )) -lt "$BMCP_RESTART_WINDOW" ] && kept+=("$t")
  done
  restart_times=("${kept[@]:-}" "$now")
  count=0
  for t in "${restart_times[@]}"; do [ -n "$t" ] && count=$(( count + 1 )); done
  if [ "$count" -gt "$BMCP_MAX_RESTARTS" ]; then
    bmcp_log "giving up: $count exits within ${BMCP_RESTART_WINDOW}s - see $BMCP_LOG_DIR/blender.log, then run restart.sh"
    break
  fi

  # A long healthy run resets the backoff; quick deaths back off 5s, 10s, 20s, 40s, 60s.
  [ "$ran" -ge 120 ] && delay=5
  bmcp_log "restarting blender in ${delay}s (restart $count of max $BMCP_MAX_RESTARTS per ${BMCP_RESTART_WINDOW}s)"
  slept=0
  while [ "$slept" -lt "$delay" ] && [ "$stopping" -eq 0 ]; do
    sleep 1
    slept=$(( slept + 1 ))
  done
  delay=$(( delay * 2 ))
  [ "$delay" -gt 60 ] && delay=60
done

rm -f "$BMCP_SUPERVISOR_PIDFILE"
bmcp_log "supervisor pid $$ exiting"
