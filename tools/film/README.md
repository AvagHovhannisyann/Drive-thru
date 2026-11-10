# Film toolkit

Tools for making a finished short film with Blender on this CPU-only cloud machine. The method and
the craft rules are in the `film-studio` skill (`.claude/skills/film-studio/`); this page is the
reference for the commands.

| Stage | Tool | What it does |
|---|---|---|
| Set-up | `install.sh` | apt packages, Python environment in `/opt/film-studio/venv`, fonts. Safe to re-run. |
| Fonts | `fonts.py`, `fonts.txt` | 19 open-licence families from Google Fonts as static TTF, registered with fontconfig. |
| Build | `blender/filmkit.py` | Helpers for Blender 5.2: geometry with bevels, materials, lights in groups, cameras, animation on a clock in seconds, plates. |
| Screens, titles | `html_frames.cjs` | A web page -> numbered PNG frames, one per film frame, no real-time playback. |
| Render | `blender/filmkit.py: render_plate` | One multilayer EXR with a pass per light group (+ a region variant for small moving things). |
| Render | `render_farm.py` | A frame range in the background, resumable, with seconds per frame and a time estimate. |
| Picture | `comp.py` | Denoise per light group, relight over time, insert screens, push-in, titles, bloom, grain, AgX. |
| Sound | `audio.py` | Score and effects from a cue sheet: synthesis, General MIDI instruments, bundled CC0 interface sounds; mixed to a loudness target. |
| Delivery | `encode.py` | Frames + sound -> H.264 / 10-bit H.265 / ProRes with BT.709 tags. |
| Checks | `sheet.py`, `look_check.py`, `qa.py` | Contact sheets from frames or linear EXR renders (with crops); exposure and colour of stills as numbers; delivery checks for the finished file. |
| Self-test | `blender/selftest.py` | Calls every `filmkit` helper once on the installed Blender (`blender -b --factory-startup --python tools/film/blender/selftest.py`). |
| Example | `examples/proof/` | An 8-second 3840x2160 film that uses every stage: `examples/proof/run.sh`. |

Python tools that need numpy, OpenCV, OpenColorIO or OpenImageDenoise run with
`/opt/film-studio/venv/bin/python`; the rest run with any Python 3 or Node 22.

## The idea that makes 4K possible without a GPU

Path tracing on these four CPU cores runs at roughly 0.7 million samples per second. A 3840x2160
frame at 64 samples is about 530 million samples: a quarter of an hour. A film cannot be rendered
frame by frame at that price, so most shots are **plates**:

1. Lock the camera off and render ONE frame with every light in a light group
   (`fk.render_plate`). Cycles writes a separate pass per group at no extra cost.
2. `comp.py` denoises each pass and adds them back together with any gain and tint per group, per
   frame. Light is additive, so this is exact: dusk to night, a lamp switching on, a screen that
   lights the room are all arithmetic.
3. What a screen shows is a web page rendered to frames and placed on the tracked screen corners.
4. A slow push-in is a resample of the plate. Things that really move (a small character) are
   rendered again only in the region around them and blended in.

Shots that need a real camera move are rendered frame by frame at a lower size and sample count and
go through the same finishing, so they match.

## Commands

```bash
tools/film/install.sh                                         # once per container
tools/blender-mcp/status.sh --quiet || tools/blender-mcp/start.sh   # live Blender for look development

# set and plate (inside Blender; see examples/proof/scene.py and shots.py)
blender -b --factory-startup --python tools/film/examples/proof/scene.py -- --out WORK
blender -b WORK/proof.blend --python tools/film/examples/proof/shots.py -- plate --out WORK --samples 64

# screen and title pictures
node tools/film/html_frames.cjs page/index.html WORK/ui --duration 8 --fps 24 --size 1920x1200
node tools/film/html_frames.cjs title/index.html WORK/title --duration 6 --size 1920x1080 --scale 2 --name title --transparent

# look development from a plate: seconds per try instead of minutes
PY=/opt/film-studio/venv/bin/python
$PY tools/film/comp.py still WORK/s1_plate.exr look.png --gains '{"sun": 0, "lamp": 3, "sky": [0.1, [0.4, 0.55, 1]]}' \
    --look '{"exposure": 0.6, "bloom": 0.2}' --screen WORK/ui/ui_0100.png
$PY tools/film/look_check.py look.png --night
$PY tools/film/sheet.py sheet.jpg WORK/preview/s2_00*.exr --look '{"exposure": 0.65}' --labels      # look before a long render

# every frame of a shot, then sound, encode, check
$PY tools/film/comp.py shot WORK/s1.json                       # skips frames that exist; --overwrite, --frames 0-23
$PY tools/film/audio.py WORK/cues.json WORK/mix.wav
python3 tools/film/encode.py WORK/film.mp4 --fps 24 --frames "WORK/frames/s1_*.png" "WORK/frames/s2_*.png" --audio WORK/mix.wav
$PY tools/film/qa.py WORK/film.mp4 --expect-size 3840x2160 --expect-fps 24 --sheet WORK/sheet.jpg

# a frame-by-frame shot in the background, resumable
python3 tools/film/render_farm.py WORK/shot.blend --frames 1-120 --out WORK/s3/s3_#### --format EXR --samples 24
```

Shot description format: `.claude/skills/film-studio/references/shot-format.md`.
Cue sheet format: `.claude/skills/film-studio/references/sound.md`.

## Delivery sizes

Film grain is expensive to compress. The 8-second proof at 3840x2160 came to 125 MB as H.264 at
CRF 17 and to 32 MB as 10-bit H.265 at CRF 18 with the same measured fidelity (PSNR 39.7 dB against
the frames). Use `--preset hevc10` for 4K files that will be shared, `h264` for 1080p and for
anything that must play everywhere, `prores` for a master that will be edited further.

## Long renders and the container

The container is suspended when the session is idle and every process stops. Rendering survives this
because nothing is lost: plates and frames are files, `render_farm.py`, the proof's `shots.py` and
`comp.py` all skip what exists. After a resume, start the Blender service again and re-run the same
command.

## Limits

- No GPU: EEVEE is not usable (software OpenGL), Cycles runs on 4 CPU threads.
- No online asset or sound libraries unless the hosts are allowed in the cloud environment
  (Poly Haven for HDRIs, textures and models; Mixkit for music and effects). Without them: procedural
  materials, Blender's eight bundled HDRIs, synthesised and General MIDI sound.
- No voice-over or generated music without an online service and a key.
- 60 fps and true 4K for moving-camera shots are out of reach on CPU; see the render budget in the skill.
