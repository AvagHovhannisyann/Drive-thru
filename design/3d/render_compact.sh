#!/bin/bash
# Final renders of the CHAMPA Compact variant. Run from repo root: bash design/3d/render_compact.sh
OUT=design/renders/final
BL=${BLENDER:-/opt/blender-dl/blender-4.5.9-linux-x64/blender}
C() { $BL -b -P design/3d/compact_scene.py -- --mode $1 --views $2 --samples $3 --pct 100 --out $OUT 2>&1 | grep -E "RENDERED|Error|Traceback" ; }
C day c_aerial,c_hero,c_walkup,c_window 128
C dusk c_hero,c_aerial 192
echo COMPACTDONE
