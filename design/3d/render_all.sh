#!/bin/bash
# Final render batch (1920x1080). Run from repo root: bash design/3d/render_all.sh
OUT=design/renders/final
mkdir -p $OUT
BL=${BLENDER:-/opt/blender-dl/blender-4.5.9-linux-x64/blender}
R() { $BL -b -P design/3d/render_views.py -- --mode $1 --views $2 --samples $3 --pct 100 --out $OUT 2>&1 | grep -E "RENDERED|Error|Traceback" ; }
R day hero,hero_wide,aerial,ararat,plaza,terrace,aerial_nw,ararat_ground 128
R dusk hero,drivethru,interior,plaza,approach 192
R night hero,aerial 192
R day cutaway 96
$BL -b -P design/3d/product_scene.py -- --out design/renders/final/packaging.png --samples 160 --pct 100 2>&1 | grep -E "RENDERED|Error|Traceback"
echo ALLDONE
