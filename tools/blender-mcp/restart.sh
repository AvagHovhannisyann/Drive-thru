#!/usr/bin/env bash
# Restart the Blender MCP service (stop, then start). The live Blender scene is not
# saved automatically - save it through MCP first if you need it.
#
# Usage: ./restart.sh [--keep-xvfb]   (--keep-xvfb restarts Blender only)
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
"$DIR/stop.sh" "$@" || echo "stop.sh reported warnings; continuing with start" >&2
exec "$DIR/start.sh"
