#!/usr/bin/env bash
# Pipeline proof: an 8-second 3840x2160 film made on CPU only. Every stage can be run again;
# finished work is kept (plates, region frames and macro frames are skipped when they exist).
#
#   tools/film/examples/proof/run.sh [WORK_DIR]        default /opt/film-studio/work/proof
#
# Stages: set -> screen and title frames -> plate -> region frames -> macro frames -> picture -> sound -> encode -> check
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILM="$(cd "$HERE/../.." && pwd)"
WORK="${1:-/opt/film-studio/work/proof}"
PY="${FILM_PY:-/opt/film-studio/venv/bin/python}"
BLENDER="${BLENDER:-/opt/blender-dl/current/blender}"
mkdir -p "$WORK"/{frames,ui,title}
step() { printf '\n== %s (%s)\n' "$1" "$(date -u +%H:%M:%S)"; }

step "set"
[ -f "$WORK/proof.blend" ] || "$BLENDER" -b --factory-startup --python "$HERE/scene.py" -- --out "$WORK" | grep -E "Saved|Error" || true

step "screen and title frames"
[ -f "$WORK/ui/ui_0192.png" ] || node "$FILM/html_frames.cjs" "$HERE/screen/index.html" "$WORK/ui" --duration 8 --fps 24 --size 1920x1200
[ -f "$WORK/title/title_0144.png" ] || node "$FILM/html_frames.cjs" "$HERE/title/index.html" "$WORK/title" --duration 6 --fps 24 \
  --size 1920x1080 --scale 2 --name title --transparent

step "S1 plate (one 4K render with five light groups)"
[ -f "$WORK/s1_plate.exr" ] || "$BLENDER" -b "$WORK/proof.blend" --python "$HERE/shots.py" -- plate --out "$WORK" --samples 64 | grep -E "PLATE|Error"

step "S1 region frames (only the area where the character moves)"
"$BLENDER" -b "$WORK/proof.blend" --python "$HERE/shots.py" -- region --out "$WORK" --frames 101-120 --samples 32 | grep -E "REGION|Error" || true

step "S2 macro frames (real camera move, 1600x900)"
"$BLENDER" -b "$WORK/proof.blend" --python "$HERE/shots.py" -- macro --out "$WORK" --frames 1-48 --samples 24 \
  --screen "$WORK/ui/ui_0001.png" --screen-frames 192 | grep -E "MACRO|Error" || true

step "picture: relight, screens, titles, grade"
cp "$HERE/s1.json" "$HERE/s2.json" "$WORK/"
"$PY" "$FILM/comp.py" shot "$WORK/s1.json"
"$PY" "$FILM/comp.py" shot "$WORK/s2.json"

step "sound"
"$PY" "$HERE/make_cues.py" "$WORK/cues.json"
"$PY" "$FILM/audio.py" "$WORK/cues.json" "$WORK/proof_mix.wav"

step "encode"
python3 "$FILM/encode.py" "$WORK/pipeline_proof_4k.mp4" --fps 24 --frames "$WORK/frames/s1_*.png" "$WORK/frames/s2_*.png" \
  --audio "$WORK/proof_mix.wav" --preset h264 --crf 17

step "check"
"$PY" "$FILM/qa.py" "$WORK/pipeline_proof_4k.mp4" --expect-size 3840x2160 --expect-fps 24 --expect-frames 192 --lufs -14 \
  --allow-black 0.5 --sheet "$WORK/proof_sheet.jpg" --json "$WORK/proof_qa.json"
