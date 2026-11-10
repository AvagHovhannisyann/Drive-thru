#!/usr/bin/env bash
# Film toolchain for this repository: sound, fonts, image and colour tools, and the Python
# environment used by tools/film/*.py. Safe to run again; installs only what is missing.
#
#   tools/film/install.sh            # everything
#   FILM_HOME=/somewhere tools/film/install.sh
#
# Needs: Ubuntu with apt, network access to the package registries and to fonts.googleapis.com /
# fonts.gstatic.com (fonts are skipped with a note when those hosts are not reachable).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILM_HOME="${FILM_HOME:-/opt/film-studio}"
UV="${UV:-$(command -v uv || echo /root/.local/bin/uv)}"
SUDO=""; [ "$(id -u)" -eq 0 ] || SUDO="sudo"
log() { printf '[film-install] %s\n' "$*"; }

APT_PACKAGES=(ffmpeg sox libsox-fmt-all fluidsynth fluid-soundfont-gm timgm6mb-soundfont fonts-noto-core
  fonts-inter fonts-jetbrains-mono fonts-ebgaramond fonts-ibm-plex openimageio-tools openexr librsvg2-bin
  rubberband-cli mediainfo imagemagick)
missing=()
for package in "${APT_PACKAGES[@]}"; do
  dpkg -s "$package" >/dev/null 2>&1 || missing+=("$package")
done
if [ "${#missing[@]}" -gt 0 ]; then
  log "apt: installing ${missing[*]}"
  $SUDO env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends "${missing[@]}" >/dev/null \
    || { $SUDO apt-get update >/dev/null && $SUDO env DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends "${missing[@]}" >/dev/null; }
else
  log "apt: all ${#APT_PACKAGES[@]} packages present"
fi

$SUDO mkdir -p "$FILM_HOME"/{work,logs,fonts}
[ -w "$FILM_HOME" ] || $SUDO chown -R "$(id -u):$(id -g)" "$FILM_HOME"
if [ -x "$UV" ]; then
  [ -x "$FILM_HOME/venv/bin/python" ] || { log "python: creating $FILM_HOME/venv (uv)"; "$UV" venv "$FILM_HOME/venv" >/dev/null; }
  log "python: installing the pinned packages"
  VIRTUAL_ENV="$FILM_HOME/venv" "$UV" pip install -q -r "$HERE/requirements.txt"
else                                  # no uv on this machine: the standard library does the same, more slowly
  [ -x "$FILM_HOME/venv/bin/python" ] || { log "python: creating $FILM_HOME/venv (venv)"; python3 -m venv "$FILM_HOME/venv"; }
  log "python: installing the pinned packages with pip"
  "$FILM_HOME/venv/bin/python" -m pip install -q -r "$HERE/requirements.txt"
fi

if FILM_HOME="$FILM_HOME" python3 "$HERE/fonts.py" >"$FILM_HOME/logs/fonts.log" 2>&1; then
  log "fonts: $(find "$FILM_HOME/fonts" -name '*.ttf' | wc -l) files in $FILM_HOME/fonts"
else
  log "fonts: some families were not fetched (see $FILM_HOME/logs/fonts.log); the apt fonts still work"
fi

"$FILM_HOME/venv/bin/python" - "$FILM_HOME/versions.json" <<'PY'
import importlib.metadata as md, json, shutil, subprocess, sys
tools = {}
for name, args in (("ffmpeg", ["-version"]), ("sox", ["--version"]), ("fluidsynth", ["--version"]), ("oiiotool", ["--version"])):
    if shutil.which(name):
        tools[name] = subprocess.run([name, *args], capture_output=True, text=True).stdout.splitlines()[0][:80]
packages = {name: md.version(name) for name in ("numpy", "scipy", "opencv-python-headless", "librosa", "pedalboard",
                                                "pyloudnorm", "opencolorio", "OpenEXR", "oidn")}
json.dump({"tools": tools, "python": sys.version.split()[0], "packages": packages}, open(sys.argv[1], "w"), indent=1)
print("[film-install] versions recorded in", sys.argv[1])
PY
log "done. Python for the film tools: $FILM_HOME/venv/bin/python"
