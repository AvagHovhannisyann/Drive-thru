#!/usr/bin/env bash
# Install everything the Blender MCP service needs. Idempotent: a re-run only does
# what is missing or out of date. Does not start anything (see start.sh).
#
#   1. apt: Xvfb, Mesa software OpenGL and the X11 libraries Blender links against
#   2. Blender (official build, version + SHA-256 pinned in config.env)
#   3. uvx present; the pinned mcp-for-blender package fetched into uv's cache
#   4. the add-on bundled in that package, installed with the upstream installer
#   5. the stdio MCP server registered with Claude Code (existing entries are kept)
#   6. a record of what was installed -> $BMCP_HOME/versions.json
#
# Needs: Ubuntu/Debian, root (or sudo), HTTPS access to download.blender.org and PyPI.
# Usage: ./install.sh [--no-register] [--force-addon]
set -euo pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

register=1
force_addon=0
while [ $# -gt 0 ]; do
  case "$1" in
    --no-register) register=0; shift ;;
    --force-addon) force_addon=1; shift ;;
    -h|--help) sed -n '2,14p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) bmcp_die "unknown argument: $1" ;;
  esac
done

REPO_ROOT="$(cd "$BMCP_DIR/../.." && pwd)"
SUDO=""
[ "$(id -u)" -eq 0 ] || SUDO="sudo"

bmcp_require_loopback
$SUDO mkdir -p "$BMCP_HOME" "$BMCP_BLENDER_ROOT"
[ -w "$BMCP_HOME" ] || $SUDO chown "$(id -u):$(id -g)" "$BMCP_HOME" "$BMCP_BLENDER_ROOT"
bmcp_mkdirs

# ---- 1. system packages ------------------------------------------------------
# Blender's own README lists libX11, libXi, libXxf86vm, libXfixes, libXrender, libGL,
# libxkbcommon, libSM, libICE; Xvfb needs Mesa's llvmpipe driver (libgl1-mesa-dri)
# to offer OpenGL 4.5 through GLX. x11-utils/mesa-utils are for diagnostics only.
APT_PACKAGES=(
  xvfb xauth x11-utils mesa-utils
  libgl1 libgl1-mesa-dri libglx-mesa0 libegl1 libvulkan1
  libx11-6 libxext6 libxi6 libxxf86vm1 libxfixes3 libxrender1
  libxkbcommon0 libxkbcommon-x11-0 libsm6 libice6
  xz-utils ca-certificates curl procps iproute2 coreutils
)
missing=()
for pkg in "${APT_PACKAGES[@]}"; do
  dpkg-query -W -f='${Status}' "$pkg" 2>/dev/null | grep -q "install ok installed" || missing+=("$pkg")
done
if [ "${#missing[@]}" -gt 0 ]; then
  bmcp_log "apt: installing ${missing[*]}"
  $SUDO env DEBIAN_FRONTEND=noninteractive apt-get update -qq
  $SUDO env DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends "${missing[@]}"
else
  bmcp_log "apt: all ${#APT_PACKAGES[@]} packages already installed"
fi

# ---- 2. Blender --------------------------------------------------------------
blender_installed() {
  [ -x "$BMCP_BLENDER_BIN" ] &&
    "$BMCP_BLENDER_BIN" --version 2>/dev/null | head -n1 | grep -q "^Blender $BMCP_BLENDER_VERSION\b"
}
if blender_installed; then
  bmcp_log "blender: $BMCP_BLENDER_VERSION already installed at $BMCP_BLENDER_DIR"
else
  base="https://download.blender.org/release/Blender$BMCP_BLENDER_SERIES"
  tarball="blender-$BMCP_BLENDER_VERSION-linux-x64.tar.xz"
  work="$(mktemp -d "$BMCP_BLENDER_ROOT/.download.XXXXXX")"
  trap 'rm -rf "$work"' EXIT

  expected="$BMCP_BLENDER_SHA256"
  if [ "$expected" = "official" ]; then
    curl -fsSL --retry 4 --retry-delay 3 -o "$work/sums" "$base/blender-$BMCP_BLENDER_VERSION.sha256"
    expected="$(awk -v f="$tarball" '$2 == f { print $1 }' "$work/sums")"
    [ -n "$expected" ] || bmcp_die "no checksum for $tarball in the official sha256 file"
    bmcp_log "blender: using the official checksum $expected"
  fi

  bmcp_log "blender: downloading $base/$tarball"
  curl -fL -sS --retry 5 --retry-delay 3 -o "$work/$tarball" "$base/$tarball"
  actual="$(sha256sum "$work/$tarball" | cut -d' ' -f1)"
  [ "$actual" = "$expected" ] ||
    bmcp_die "checksum mismatch for $tarball: expected $expected, got $actual - nothing was installed"
  bmcp_log "blender: sha256 verified, extracting"
  tar -xJf "$work/$tarball" -C "$work"
  [ -x "$work/blender-$BMCP_BLENDER_VERSION-linux-x64/blender" ] || bmcp_die "unexpected archive layout"
  rm -rf "$BMCP_BLENDER_DIR"
  mv "$work/blender-$BMCP_BLENDER_VERSION-linux-x64" "$BMCP_BLENDER_DIR"
  rm -rf "$work"
  trap - EXIT
  blender_installed || bmcp_die "Blender does not run after install: $BMCP_BLENDER_BIN"
  bmcp_log "blender: installed $("$BMCP_BLENDER_BIN" --version | head -n1)"
fi
# Stable paths: /opt/blender-dl/current and `blender` on PATH (never replaces a
# foreign blender binary; only a link this script owns).
ln -sfn "$BMCP_BLENDER_DIR" "$BMCP_BLENDER_ROOT/current"
path_blender="$(command -v blender 2>/dev/null || true)"
if [ -z "$path_blender" ] || { [ -L /usr/local/bin/blender ] && [[ "$(readlink /usr/local/bin/blender)" == "$BMCP_BLENDER_ROOT"/* ]]; }; then
  $SUDO ln -sfn "$BMCP_BLENDER_ROOT/current/blender" /usr/local/bin/blender
fi
missing_libs="$(ldd "$BMCP_BLENDER_BIN" 2>/dev/null | grep "not found" || true)"
[ -z "$missing_libs" ] || bmcp_die "Blender is missing shared libraries: $missing_libs"

# ---- 3. uvx + the pinned MCP package -----------------------------------------
if [ ! -x "$BMCP_UVX" ]; then
  found="$(command -v uvx 2>/dev/null || true)"
  [ -n "$found" ] || bmcp_die "uvx not found at $BMCP_UVX or on PATH. Install uv (https://docs.astral.sh/uv/getting-started/installation/) and set BMCP_UVX in config.env."
  bmcp_die "uvx is at $found, not $BMCP_UVX - set BMCP_UVX=$found in config.env so the registered command is correct"
fi
bmcp_log "uv: $("$BMCP_UVX" --version 2>/dev/null)"
# First run downloads the package and its dependencies from PyPI into uv's cache.
"$BMCP_UVX" "$BMCP_MCP_SPEC" --help >/dev/null 2>&1 ||
  bmcp_die "could not fetch/run $BMCP_MCP_SPEC with uvx (PyPI reachable?)"
mcp_versions="$("$BMCP_UVX" --from "${BMCP_MCP_PACKAGE}==${BMCP_MCP_VERSION}" python - <<'PY' 2>/dev/null
import hashlib, importlib.metadata as md, json, pathlib, blender_mcp
from blender_mcp import addon_manager
bundled = pathlib.Path(addon_manager.get_bundled_addon_path())
print(json.dumps({
    "mcp-for-blender": md.version("mcp-for-blender"),
    "expected_addon_protocol": addon_manager.EXPECTED_ADDON_PROTOCOL_VERSION,
    "bundled_addon_sha256": hashlib.sha256(bundled.read_bytes()).hexdigest(),
    "dependencies": {d: md.version(d) for d in ("mcp", "httpx", "pydantic", "anyio")},
}))
PY
)"
[ -n "$mcp_versions" ] || bmcp_die "could not inspect the installed $BMCP_MCP_SPEC package"
bmcp_log "mcp package: $mcp_versions"

# ---- 4. the add-on -----------------------------------------------------------
# Installed with the package's own installer, into the service's private user
# scripts directory (not ~/.config/blender), as blender_mcp.py.
addon_sha() { [ -f "$BMCP_ADDON_FILE" ] && sha256sum "$BMCP_ADDON_FILE" | cut -d' ' -f1; }
bundled_sha="$(printf '%s' "$mcp_versions" | sed -n 's/.*"bundled_addon_sha256": "\([0-9a-f]*\)".*/\1/p')"
if [ -n "$BMCP_ADDON_SHA256" ] && [ "$bundled_sha" != "$BMCP_ADDON_SHA256" ]; then
  bmcp_die "add-on bundled in $BMCP_MCP_SPEC has sha256 $bundled_sha, config.env pins $BMCP_ADDON_SHA256 - update BMCP_ADDON_SHA256 after reviewing the new add-on"
fi
if [ "$force_addon" -eq 0 ] && [ "$(addon_sha || true)" = "$bundled_sha" ]; then
  bmcp_log "add-on: already installed and identical to the one bundled in $BMCP_MCP_SPEC"
else
  bmcp_log "add-on: installing into $BMCP_ADDONS_DIR"
  "$BMCP_UVX" "$BMCP_MCP_SPEC" install-addon --addons-dir "$BMCP_ADDONS_DIR" 2>&1 | sed 's/^/    /'
  [ "$(addon_sha || true)" = "$bundled_sha" ] || bmcp_die "add-on at $BMCP_ADDON_FILE does not match the bundled one after install"
  if bmcp_blender_pid >/dev/null 2>&1; then
    bmcp_log "add-on: the service is running the previous add-on - run restart.sh to load the new one"
  fi
fi

# ---- 5. register the stdio MCP server with Claude Code ------------------------
# Equivalent of upstream's `claude mcp add blender uvx mcp-for-blender`, with an
# absolute uvx path, the pinned version, and explicit loopback/privacy settings:
#   DISABLE_TELEMETRY=true   no usage records leave this machine
#   BLENDER_HOST/PORT        the add-on socket (loopback)
#   BLENDERMCP_ADDONS_DIR    lets the server's start-up check find the add-on
# Default scope is "project": the entry lives in the repository's .mcp.json, the file
# Claude Code cloud sessions load on their own. If the committed entry already matches
# config.env nothing is written.
claude_entry() {   # prints the stored entry for our name in the configured scope, if any
  "$(bmcp_python)" - "$REPO_ROOT" "$BMCP_MCP_NAME" "$BMCP_CLAUDE_SCOPE" <<'PY'
import json, os, sys
root, name, scope = sys.argv[1:4]
def load(path):
    try:
        return json.load(open(path))
    except (OSError, ValueError):
        return {}
if scope == "project":
    servers = load(os.path.join(root, ".mcp.json")).get("mcpServers", {})
else:
    cfg = load(os.path.expanduser("~/.claude.json"))
    servers = cfg.get("mcpServers", {}) if scope == "user" else \
        cfg.get("projects", {}).get(root, {}).get("mcpServers", {})
entry = servers.get(name)
if entry is not None:
    print(json.dumps({"command": entry.get("command"), "args": entry.get("args", []),
                      "env": entry.get("env", {})}, sort_keys=True))
PY
}
expected_entry="$("$(bmcp_python)" - "$BMCP_UVX" "$BMCP_MCP_SPEC" "$BMCP_HOST" "$BMCP_PORT" "$BMCP_ADDONS_DIR" <<'PY'
import json, sys
uvx, spec, host, port, addons = sys.argv[1:6]
print(json.dumps({"command": uvx, "args": [spec], "env": {
    "DISABLE_TELEMETRY": "true", "BLENDER_HOST": host, "BLENDER_PORT": port,
    "BLENDERMCP_ADDONS_DIR": addons}}, sort_keys=True))
PY
)"
if [ "$register" -eq 0 ]; then
  bmcp_log "claude: registration skipped (--no-register)"
elif ! command -v claude >/dev/null 2>&1; then
  bmcp_log "claude: CLI not on PATH - registration skipped. Command to register later:"
  bmcp_log "  claude mcp add --scope $BMCP_CLAUDE_SCOPE $BMCP_MCP_NAME -e DISABLE_TELEMETRY=true -e BLENDER_HOST=$BMCP_HOST -e BLENDER_PORT=$BMCP_PORT -e BLENDERMCP_ADDONS_DIR=$BMCP_ADDONS_DIR -- $BMCP_UVX $BMCP_MCP_SPEC"
else
  cd "$REPO_ROOT"   # local/project scope is keyed by the project directory
  current="$(claude_entry || true)"
  if [ "$current" = "$expected_entry" ]; then
    bmcp_log "claude: server '$BMCP_MCP_NAME' already registered ($BMCP_CLAUDE_SCOPE scope) with the expected command"
  else
    # local/user scope edits ~/.claude.json: keep a private copy first (it holds account
    # details). project scope edits the repository's .mcp.json, which git already tracks.
    if [ "$BMCP_CLAUDE_SCOPE" != "project" ] && [ -f "$HOME/.claude.json" ]; then
      mkdir -p "$BMCP_HOME/backups" && chmod 700 "$BMCP_HOME/backups"
      cp -p "$HOME/.claude.json" "$BMCP_HOME/backups/claude.json.$(date -u +%Y%m%dT%H%M%SZ)"
    fi
    if [ -n "$current" ]; then
      bmcp_log "claude: replacing the existing '$BMCP_MCP_NAME' entry (was: $current)"
      claude mcp remove "$BMCP_MCP_NAME" --scope "$BMCP_CLAUDE_SCOPE" >/dev/null
    fi
    claude mcp add --scope "$BMCP_CLAUDE_SCOPE" "$BMCP_MCP_NAME" \
      -e DISABLE_TELEMETRY=true \
      -e "BLENDER_HOST=$BMCP_HOST" \
      -e "BLENDER_PORT=$BMCP_PORT" \
      -e "BLENDERMCP_ADDONS_DIR=$BMCP_ADDONS_DIR" \
      -- "$BMCP_UVX" "$BMCP_MCP_SPEC"
    [ "$(claude_entry || true)" = "$expected_entry" ] ||
      bmcp_die "claude mcp add ran but the stored entry is not the expected one: $(claude_entry || true)"
    bmcp_log "claude: registered '$BMCP_MCP_NAME' ($BMCP_CLAUDE_SCOPE scope): $expected_entry"
    if [ "$BMCP_CLAUDE_SCOPE" = "project" ]; then
      bmcp_log "claude: $REPO_ROOT/.mcp.json changed - commit it so new sessions use the same command"
    fi
  fi
fi

# ---- 6. record what is installed ---------------------------------------------
pkg_version() { dpkg-query -W -f='${Version}' "$1" 2>/dev/null || echo "n/a"; }
blender_version_text="$("$BMCP_BLENDER_BIN" --version 2>/dev/null)"
REC_TIME="$(bmcp_ts)" \
REC_OS="$(. /etc/os-release && echo "$PRETTY_NAME")" \
REC_KERNEL="$(uname -r)" \
REC_ARCH="$(uname -m)" \
REC_BLENDER_VERSION="$(printf '%s\n' "$blender_version_text" | head -n1)" \
REC_BLENDER_HASH="$(printf '%s\n' "$blender_version_text" | sed -n 's/^\s*build hash: //p')" \
REC_BLENDER_DIR="$BMCP_BLENDER_DIR" \
REC_BLENDER_URL="https://download.blender.org/release/Blender$BMCP_BLENDER_SERIES/blender-$BMCP_BLENDER_VERSION-linux-x64.tar.xz" \
REC_BLENDER_SHA="$BMCP_BLENDER_SHA256" \
REC_MCP_PACKAGE="$mcp_versions" \
REC_MCP_COMMAND="$expected_entry" \
REC_ADDON_FILE="$BMCP_ADDON_FILE" \
REC_ADDON_SHA="$(addon_sha)" \
REC_ADDON_PROTOCOL="$(grep -m1 -E '^ADDON_PROTOCOL_VERSION\s*=' "$BMCP_ADDON_FILE" | tr -cd '0-9')" \
REC_ADDON_BLINFO="$(sed -n 's/^\s*"version": (\([0-9, ]*\)),.*/\1/p' "$BMCP_ADDON_FILE" | head -n1)" \
REC_UV="$("$BMCP_UVX" --version 2>/dev/null)" \
REC_CLAUDE="$(claude --version 2>/dev/null || echo n/a)" \
REC_APT="xvfb=$(pkg_version xvfb) libgl1-mesa-dri=$(pkg_version libgl1-mesa-dri) libglx-mesa0=$(pkg_version libglx-mesa0) mesa-utils=$(pkg_version mesa-utils) x11-utils=$(pkg_version x11-utils)" \
REC_GPU="$(bmcp_has_gpu && echo 1 || echo 0)" \
"$(bmcp_python)" - "$BMCP_HOME/versions.json" <<'PY'
import json, os, sys
env = os.environ
record = {
    "recorded_utc": env["REC_TIME"],
    "os": env["REC_OS"],
    "kernel": env["REC_KERNEL"],
    "arch": env["REC_ARCH"],
    "blender": {
        "version": env["REC_BLENDER_VERSION"],
        "build_hash": env["REC_BLENDER_HASH"],
        "path": env["REC_BLENDER_DIR"],
        "source": env["REC_BLENDER_URL"],
        "tarball_sha256": env["REC_BLENDER_SHA"],
    },
    "mcp_package": json.loads(env["REC_MCP_PACKAGE"]),
    "mcp_command": json.loads(env["REC_MCP_COMMAND"]),
    "addon": {
        "file": env["REC_ADDON_FILE"],
        "sha256": env["REC_ADDON_SHA"],
        "protocol": env["REC_ADDON_PROTOCOL"],
        "bl_info_version": env["REC_ADDON_BLINFO"],
    },
    "uv": env["REC_UV"],
    "claude_cli": env["REC_CLAUDE"],
    "apt": dict(item.split("=", 1) for item in env["REC_APT"].split()),
    "gpu_present": env["REC_GPU"] == "1",
}
with open(sys.argv[1], "w", encoding="utf-8") as handle:
    json.dump(record, handle, indent=2, sort_keys=True)
    handle.write("\n")
print(json.dumps(record, indent=2, sort_keys=True))
PY
bmcp_log "install complete - versions recorded in $BMCP_HOME/versions.json; next: $BMCP_DIR/start.sh"
