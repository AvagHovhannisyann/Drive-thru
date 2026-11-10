#!/usr/bin/env bash
# Shared helpers for the Blender MCP service scripts. Source this file; do not run it.
#
#   . "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
#
# Design rule used throughout: never signal or delete anything on the strength of a
# PID file alone. A PID is only acted on after /proc confirms it is alive AND that
# its command line is the process we started (PIDs get reused).
#
# shellcheck disable=SC2034  # variables defined here are used by the sourcing scripts

BMCP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=config.env
. "$BMCP_DIR/config.env"

# --- derived paths ------------------------------------------------------------
BMCP_BLENDER_DIR="$BMCP_BLENDER_ROOT/blender-$BMCP_BLENDER_VERSION-linux-x64"
BMCP_BLENDER_BIN="$BMCP_BLENDER_DIR/blender"
BMCP_BLENDER_SERIES="${BMCP_BLENDER_VERSION%.*}"            # 4.5.16 -> 4.5
BMCP_LOG_DIR="$BMCP_HOME/logs"
BMCP_RUN_DIR="$BMCP_HOME/run"
BMCP_TMP_DIR="$BMCP_HOME/tmp"
BMCP_TEST_DIR="$BMCP_HOME/test-output"
# Blender user resources for the service only (BLENDER_USER_RESOURCES). Keeps the
# add-on and its preferences out of ~/.config/blender, so plain `blender -b` batch
# renders stay add-on free.
BMCP_USERDATA="$BMCP_HOME/userdata"
BMCP_ADDONS_DIR="$BMCP_USERDATA/scripts/addons"
BMCP_ADDON_FILE="$BMCP_ADDONS_DIR/$BMCP_ADDON_MODULE.py"
BMCP_STATUS_FILE="$BMCP_RUN_DIR/blender-status.json"
BMCP_XVFB_PIDFILE="$BMCP_RUN_DIR/xvfb.pid"
BMCP_BLENDER_PIDFILE="$BMCP_RUN_DIR/blender.pid"
BMCP_SUPERVISOR_PIDFILE="$BMCP_RUN_DIR/supervisor.pid"
BMCP_STARTUP_SCRIPT="$BMCP_DIR/blender_startup.py"
BMCP_DISPLAY_NUM="${BMCP_DISPLAY#:}"
BMCP_X_LOCK="/tmp/.X${BMCP_DISPLAY_NUM}-lock"
BMCP_X_SOCKET="/tmp/.X11-unix/X${BMCP_DISPLAY_NUM}"
# uvx "package@version" spec: one pin drives both the server and the bundled add-on.
BMCP_MCP_SPEC="${BMCP_MCP_PACKAGE}@${BMCP_MCP_VERSION}"

# --- logging ------------------------------------------------------------------
bmcp_ts()  { date -u +%Y-%m-%dT%H:%M:%SZ; }
bmcp_log() { printf '[%s] %s\n' "$(bmcp_ts)" "$*"; }
bmcp_die() { printf '[%s] ERROR: %s\n' "$(bmcp_ts)" "$*" >&2; exit 1; }

# --- configuration guards -----------------------------------------------------
# The add-on runs arbitrary Python for whoever connects, so only loopback is allowed.
bmcp_require_loopback() {
  [[ "$BMCP_HOST" =~ ^127\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]] ||
    bmcp_die "BMCP_HOST must be a 127.x.x.x loopback address (got '$BMCP_HOST')"
  if ! { [[ "$BMCP_PORT" =~ ^[0-9]+$ ]] && [ "$BMCP_PORT" -ge 1024 ] && [ "$BMCP_PORT" -le 65535 ]; }; then
    bmcp_die "BMCP_PORT must be a port number 1024-65535 (got '$BMCP_PORT')"
  fi
  [[ "$BMCP_DISPLAY_NUM" =~ ^[0-9]+$ ]] ||
    bmcp_die "BMCP_DISPLAY must look like ':99' (got '$BMCP_DISPLAY')"
}

bmcp_mkdirs() {
  mkdir -p "$BMCP_LOG_DIR" "$BMCP_RUN_DIR" "$BMCP_TMP_DIR" "$BMCP_TEST_DIR" \
           "$BMCP_ADDONS_DIR" "$BMCP_USERDATA/config" "$BMCP_RUN_DIR/xdg"
  chmod 700 "$BMCP_RUN_DIR/xdg"
}

# A Python for small helper snippets: system python3, else the one bundled with Blender.
bmcp_python() {
  if command -v python3 >/dev/null 2>&1; then command -v python3; return 0; fi
  local bundled
  for bundled in "$BMCP_BLENDER_DIR/$BMCP_BLENDER_SERIES"/python/bin/python3*; do
    [ -x "$bundled" ] && { echo "$bundled"; return 0; }
  done
  return 1
}

# True when a GPU that Blender could use is visible (NVIDIA driver or a DRM render node).
bmcp_has_gpu() {
  if command -v nvidia-smi >/dev/null 2>&1 && nvidia-smi -L >/dev/null 2>&1; then return 0; fi
  compgen -G "/dev/dri/renderD*" >/dev/null 2>&1
}

# --- process helpers ----------------------------------------------------------
# Alive = exists in /proc and is not a zombie.
bmcp_pid_alive() {
  local pid="${1:-}" state
  [[ "$pid" =~ ^[0-9]+$ ]] || return 1
  [ -r "/proc/$pid/stat" ] || return 1
  state="$(sed -e 's/^.*) //' "/proc/$pid/stat" 2>/dev/null | cut -d' ' -f1)"
  [ -n "$state" ] && [ "$state" != "Z" ] && [ "$state" != "X" ]
}

bmcp_pid_cmdline() { tr '\0' ' ' < "/proc/$1/cmdline" 2>/dev/null; }

bmcp_read_pidfile() { [ -f "$1" ] && tr -cd '0-9' < "$1"; }

# Is this PID an Xvfb serving OUR display?
bmcp_is_our_xvfb() {
  bmcp_pid_alive "$1" || return 1
  [[ "$(bmcp_pid_cmdline "$1")" =~ (^|/)Xvfb\ ${BMCP_DISPLAY}\  ]]
}

# Is this PID any kind of X server (ours or not)?
bmcp_is_x_server() {
  bmcp_pid_alive "$1" || return 1
  [[ "$(bmcp_pid_cmdline "$1")" =~ (^|/)(Xvfb|Xorg|X|Xvnc|Xtigervnc|Xephyr|Xwayland|Xnest)\  ]]
}

# Is this PID the service's Blender (our binary, our startup script)?
bmcp_is_our_blender() {
  bmcp_pid_alive "$1" || return 1
  local cmd; cmd="$(bmcp_pid_cmdline "$1")"
  [[ "$cmd" == *"$BMCP_BLENDER_BIN"* && "$cmd" == *"$BMCP_STARTUP_SCRIPT"* ]]
}

bmcp_is_our_supervisor() {
  bmcp_pid_alive "$1" || return 1
  [[ "$(bmcp_pid_cmdline "$1")" == *"$BMCP_DIR/supervise.sh"* ]]
}

# PID from a pid file, but only if it still is the expected process. Prints the PID.
bmcp_xvfb_pid()       { local p; p="$(bmcp_read_pidfile "$BMCP_XVFB_PIDFILE")";       bmcp_is_our_xvfb "$p"       && echo "$p"; }
bmcp_blender_pid()    { local p; p="$(bmcp_read_pidfile "$BMCP_BLENDER_PIDFILE")";    bmcp_is_our_blender "$p"    && echo "$p"; }
bmcp_supervisor_pid() { local p; p="$(bmcp_read_pidfile "$BMCP_SUPERVISOR_PIDFILE")"; bmcp_is_our_supervisor "$p" && echo "$p"; }

# Send TERM, wait up to $2 seconds, then KILL. Caller must have verified the PID.
bmcp_terminate() {
  local pid="$1" grace="${2:-10}" i
  bmcp_pid_alive "$pid" || return 0
  kill -TERM "$pid" 2>/dev/null
  for ((i = 0; i < grace * 5; i++)); do
    bmcp_pid_alive "$pid" || return 0
    sleep 0.2
  done
  bmcp_log "pid $pid ignored TERM for ${grace}s - sending KILL"
  kill -KILL "$pid" 2>/dev/null
  for ((i = 0; i < 25; i++)); do
    bmcp_pid_alive "$pid" || return 0
    sleep 0.2
  done
  return 1
}

# --- X display helpers --------------------------------------------------------
# PID recorded in the X lock file (may be stale).
bmcp_display_lock_pid() { [ -f "$BMCP_X_LOCK" ] && tr -cd '0-9' < "$BMCP_X_LOCK"; }

# True when something is accepting connections on the display's socket
# (filesystem socket or the Linux abstract socket of the same name).
bmcp_display_socket_live() {
  local py; py="$(bmcp_python)" || return 1
  "$py" - "$BMCP_X_SOCKET" <<'PY'
import socket, sys
path = sys.argv[1]
for address in (path, "\0" + path):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        s.connect(address)
    except OSError:
        continue
    else:
        sys.exit(0)
    finally:
        s.close()
sys.exit(1)
PY
}

# True when an X server answers the X11 protocol on the display.
bmcp_display_answers() {
  if command -v xdpyinfo >/dev/null 2>&1; then
    xdpyinfo -display "$BMCP_DISPLAY" >/dev/null 2>&1
  else
    bmcp_display_socket_live
  fi
}

# PID of the live process that owns the display, if any. "Owns" means: it holds the
# lock file and is an X server, or it is an X server started for this display.
bmcp_display_owner_pid() {
  local pid
  pid="$(bmcp_display_lock_pid)"
  if bmcp_is_x_server "$pid"; then echo "$pid"; return 0; fi
  pid="$(pgrep -f "(^|/)(Xvfb|Xorg|Xvnc|Xtigervnc|Xephyr|Xwayland|Xnest) ${BMCP_DISPLAY}( |\$)" 2>/dev/null | head -n1)"
  if bmcp_pid_alive "$pid"; then echo "$pid"; return 0; fi
  return 1
}

# Remove a stale lock/socket for our display - only when provably nobody owns it:
# no live X server process for the display AND nothing listening on its socket.
bmcp_clear_stale_display() {
  [ -e "$BMCP_X_LOCK" ] || [ -e "$BMCP_X_SOCKET" ] || return 0
  local owner
  if owner="$(bmcp_display_owner_pid)"; then
    bmcp_log "display $BMCP_DISPLAY is owned by live pid $owner - lock left untouched"
    return 1
  fi
  if bmcp_display_socket_live; then
    bmcp_log "display $BMCP_DISPLAY socket is accepting connections - lock left untouched"
    return 1
  fi
  bmcp_log "removing stale X lock for $BMCP_DISPLAY (lock pid '$(bmcp_display_lock_pid)' is not a live X server, socket is dead)"
  rm -f "$BMCP_X_LOCK" "$BMCP_X_SOCKET"
  return 0
}

# Make sure an Xvfb owned by this service is serving BMCP_DISPLAY. Logs the reason and
# returns non-zero instead of exiting, so start.sh and the supervisor can both use it.
bmcp_ensure_xvfb() {
  local pid owner i
  if pid="$(bmcp_xvfb_pid)"; then
    bmcp_display_answers && return 0
    bmcp_log "Xvfb pid $pid no longer answers on $BMCP_DISPLAY - replacing it"
    bmcp_terminate "$pid" 5
  fi

  if owner="$(bmcp_display_owner_pid)"; then
    if bmcp_is_our_xvfb "$owner" && bmcp_display_answers; then
      # A live Xvfb for our display whose pid file was lost: adopt it.
      echo "$owner" > "$BMCP_XVFB_PIDFILE"
      bmcp_log "adopted running Xvfb on $BMCP_DISPLAY (pid $owner)"
      return 0
    fi
    bmcp_log "display $BMCP_DISPLAY is owned by another live process (pid $owner: $(bmcp_pid_cmdline "$owner")) - not touching it; stop that process or set BMCP_DISPLAY to a free display"
    return 1
  fi

  # Nobody alive owns the display. A leftover lock/socket (e.g. after kill -9) is
  # removed only after that has been verified - see bmcp_clear_stale_display.
  bmcp_clear_stale_display || { bmcp_log "display $BMCP_DISPLAY looks in use; refusing to remove its lock"; return 1; }

  bmcp_log "starting Xvfb on $BMCP_DISPLAY ($BMCP_SCREEN)"
  # -nolisten tcp : the display is reachable through its local unix socket only
  # -noreset      : keep the server alive when the last client disconnects
  setsid nohup Xvfb "$BMCP_DISPLAY" -screen 0 "$BMCP_SCREEN" -nolisten tcp -noreset \
    +extension GLX +render >> "$BMCP_LOG_DIR/xvfb.log" 2>&1 < /dev/null &
  pid=$!
  echo "$pid" > "$BMCP_XVFB_PIDFILE"
  for ((i = 0; i < 50; i++)); do
    bmcp_pid_alive "$pid" || { bmcp_log "Xvfb exited during start - see $BMCP_LOG_DIR/xvfb.log"; return 1; }
    bmcp_display_answers && { bmcp_log "Xvfb is up on $BMCP_DISPLAY (pid $pid)"; return 0; }
    sleep 0.2
  done
  bmcp_log "Xvfb did not answer on $BMCP_DISPLAY within 10 s - see $BMCP_LOG_DIR/xvfb.log"
  return 1
}

# --- add-on socket helpers ----------------------------------------------------
# "ADDR PID" of whatever listens on the add-on port (empty if nothing does).
bmcp_port_listener() {
  command -v ss >/dev/null 2>&1 || return 1
  ss -H -ltnp "sport = :$BMCP_PORT" 2>/dev/null |
    awk '{ pid=""; if (match($0, /pid=[0-9]+/)) pid=substr($0, RSTART+4, RLENGTH-4); print $4, pid }' | head -n1
}

# Ask the add-on for its handshake over the raw socket protocol the MCP server uses
# ({"type": ..., "params": ...} -> {"status": ..., "result": ...}). Prints the result
# JSON. Succeeds only if Blender's main thread actually executed the command, which
# is a stronger check than "the port is open".
bmcp_addon_ping() {
  local py; py="$(bmcp_python)" || return 1
  "$py" - "$BMCP_HOST" "$BMCP_PORT" "${1:-5}" <<'PY'
import json, socket, sys
host, port, timeout = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
try:
    with socket.create_connection((host, port), timeout=timeout) as s:
        s.settimeout(timeout)
        s.sendall(json.dumps({"type": "get_addon_info", "params": {}}).encode("utf-8"))
        buf, reply = b"", None
        while reply is None:
            chunk = s.recv(65536)
            if not chunk:
                break
            buf += chunk
            try:
                reply = json.loads(buf.decode("utf-8"))
            except ValueError:
                continue
except OSError as exc:
    print(f"no answer from the add-on at {host}:{port}: {exc}", file=sys.stderr)
    sys.exit(1)
if not isinstance(reply, dict) or reply.get("status") == "error":
    print(f"unexpected reply from {host}:{port}: {reply!r}", file=sys.stderr)
    sys.exit(1)
print(json.dumps(reply.get("result", reply), sort_keys=True))
PY
}

# Read one key from the JSON status file Blender's startup script maintains.
bmcp_status_field() {
  local py; py="$(bmcp_python)" || return 1
  [ -f "$BMCP_STATUS_FILE" ] || return 1
  "$py" - "$BMCP_STATUS_FILE" "$1" <<'PY'
import json, sys
try:
    value = json.load(open(sys.argv[1])).get(sys.argv[2])
except (OSError, ValueError):
    sys.exit(1)
if value is None:
    sys.exit(1)
print(value)
PY
}
