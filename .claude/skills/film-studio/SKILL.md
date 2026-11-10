---
name: film-studio
description: Make a finished short film (ad, explainer, concept or product film, title piece) with Blender on this CPU-only cloud machine - plan on one clock, build the set from code, render plates with light groups, animate light, screens and titles in the compositor, score and mix offline, encode and check. Use for any request to make, plan, continue, re-cut, fix or estimate a video, film, animation, trailer or ad here. Start with this skill; it routes to the other Blender and video skills.
---

# Film studio

How films get made in this repository. The tools are in `tools/film/` (commands: `tools/film/README.md`).
A complete worked example that exercises every stage is `tools/film/examples/proof/` (`run.sh`).

## Ground rules

1. **One clock.** Every shot, light change, screen picture, hop, note and title is placed in film
   seconds. Frame = round(seconds x fps) + 1 (`fk.frame`). Sound times are computed from the same
   numbers that animate the picture, never typed in twice.
2. **Budget before building.** On this machine a path-traced frame costs minutes
   (`references/render-budget.md`). Decide per shot whether it is a plate (one render, then free) or
   frame-by-frame (expensive), and add up the hours before writing any scene code.
3. **Look at what you make.** Open every still and contact sheet with the Read tool before describing
   it. Use `look_check.py` for exposure and colour and `qa.py` for the finished file. Report only
   what was seen or measured.
4. **Deterministic.** Nothing is captured in real time. Pictures are functions of t; renders,
   screen pages and sound can each be re-run alone and give the same result.
5. **Original.** Study references for method; do not recreate an existing film, character or brand.
6. **Resumable.** Plates and frames are files and every tool skips what exists. A suspended container
   costs nothing but a restart of the same command.

## Before the first Blender call

```bash
tools/blender-mcp/status.sh --quiet || tools/blender-mcp/start.sh     # live Blender 5.2 for look development
[ -x /opt/film-studio/venv/bin/python ] || tools/film/install.sh       # film toolchain (about 2 min when missing)
```

Use the live session (`mcp__blender__execute_blender_code`, `look`) to explore a look quickly; put
everything that must be reproducible in scripts run with `blender -b`.

## Order of work

| Step | Output | Gate before moving on |
|---|---|---|
| 1. Brief | Purpose, audience, length, aspect ratio, delivery size, any required words | If length, format or the words on screen are unknown, ask once; otherwise decide and say so |
| 2. Treatment | `references/treatment-template.md` filled in: one-line idea, beats, timeline rows SHOTS / LIGHT / SCREEN / CHARACTER / SCORE / SOUND / TITLES | Each beat has one job; nothing on screen without a reason |
| 3. Shot list and budget | Per shot: seconds, type (plate / frames), lens, light state, what moves; total render hours | Total fits the time available, with half again as reserve |
| 4. Set | `scene.py` builds the set from code with `filmkit`; top-view plan in metres first | Quarter-size stills from every camera, looked at, three rounds |
| 5. Screens and titles | Web pages with `window.seek(t)`, rendered by `html_frames.cjs` | Readable at delivery size; text spelled and timed |
| 6. Plates and frames | `fk.render_plate` per plate shot; region frames for small motion; `render_farm.py` for moving shots | For every moving shot, five quarter-size frames on a `sheet.py` contact sheet BEFORE the full render; first plate checked at full size |
| 7. Picture | One shot JSON per shot -> `comp.py shot` | `look_check.py` on a still from each light state; contact sheet per shot |
| 8. Sound | Cue sheet -> `audio.py` | Loudness and event times printed and inside tolerance |
| 9. Delivery | `encode.py`, then `qa.py` with expected size, rate and frame count | QA passes; contact sheet looked at; send the file with SendUserFile |

## Choosing the shot type

| The shot needs | Type | Cost |
|---|---|---|
| Locked camera; light, screens, titles or a slow push-in change | **plate** | one render, then about a second per frame |
| The same plus something small that moves (a character hop, a hand, a cursor on a desk) | **plate + regions** | the plate plus a fraction of a frame per moving frame |
| Moving shadows over time (sun crossing the room) | **plate + sequences** | one extra plate per sun position, cross-faded |
| A real camera move, parallax, large motion | **frames** | full price per frame; keep these short, smaller and at fewer samples |

Spend the frame-by-frame budget on the two or three shots that need to feel like a camera in a room
(a reveal, a macro arc). Everything else is plates. Format details: `references/shot-format.md`.

## Building blocks (all in `tools/film/blender/filmkit.py`)

`fk.reset`, `fk.cycles`, `fk.color` · `fk.box / cylinder / sphere / lathe / plane / rod / torus_arc / text`
with bevels · `fk.material`, `fk.wood`, `fk.add_surface_noise`, `fk.screen_material`, `fk.glass`,
`fk.emission` · `fk.area / spot / point / sun`, `fk.world_sky / world_hdri / world_color`, all with
`group=` · `fk.camera`, `fk.cut_to` · `fk.key`, `fk.bake`, `fk.hop`, easing functions ·
`fk.render_plate`, `fk.plate_meta`, `fk.render_still` · downloaded assets: `fk.pbr_material`,
`fk.import_model`, `fk.world_hdri("<asset id>")` after `tools/film/assets.py get <id>`.

## Which other skill to load

| Need | Skill |
|---|---|
| Blender 5.2 API facts, running bpy, what changed since 4.x | `blender-core` (read its `references/api-changes-5x.md` on any AttributeError) |
| Keyframes, actions, NLA | `blender-animation` |
| Render settings, colour management, passes | `blender-rendering` |
| Day/night, sky, fog, mood numbers | `blender-time-of-day`, `blender-lighting-lookdev`, `blender-lighting` |
| Lens, focus, composition | `blender-cameras`, `camera-cinematography` |
| Materials, wear, decals | `blender-pbr-materials`, `blender-texturing`, `blender-materials`, `materials` |
| Geometry nodes, scatter, procedural effects | `procedural-blender-nodes`, `blender-geometry-nodes` |
| Rain, snow, dust | `blender-weather-fx` |
| Modelling a specific prop or matching a reference | `blender-asset-studio`, `blender-hardsurface-modeling`, `reference-to-3d` |
| Asset review before it goes in a shot | `blender-asset-qa` |
| Art direction and style vocabulary | `blender-director` and the style skills beside it |
| Whole-film examples to learn from | `blender-film`, `blender-car-film`, `blender-forest`, `video-3d-production` |
| Screen content and title motion in HTML | `motion-design`, `business-motion-film` |
| Storyboard, critique rounds, sound placement with real sounds | `video-director` (and its `real-sfx`) |
| Cuts, captions, loudness, platform exports | `ffmpeg-skill` |
| Real surfaces, props and skies | `tools/film/assets.py` (Poly Haven, CC0): scanned texture sets, models, HDRIs |
| Recorded sound effects and music | `tools/film/sounds.py` (Mixkit; use in films, never commit the files) |
| Renting GPUs (needs the user's key and network access) | `runpod`, `runpodctl`, `runpod-pod-deploy` |

Tool names differ from some skills: their `get_viewport_screenshot` is `look` here. Their Windows
paths (`C:/...`) become `/opt/film-studio/work/...`. Where a vendored skill and this one disagree
about rendering on this machine, this one is right: it was measured here.

## Reviews

After stills and again after the first assembly, ask a fresh agent (Agent tool, no context from you
beyond the brief and the pictures) to list what looks wrong or cheap, most serious first. Fix,
re-render only the affected shot, re-check. Two rounds are normal.

## Limits to state plainly when planning

- 4 CPU threads, no GPU. EEVEE cannot be used. Real-camera shots at 3840x2160 or at 60 fps are not
  affordable; plate shots at 3840x2160 are.
- Assets: Poly Haven (CC0) through `assets.py` while its hosts are allowed in the environment; otherwise
  procedural materials and Blender's bundled HDRIs. Prefer scanned texture sets and models for hero
  surfaces and props: they look far better than procedural ones for the same render cost.
- Sound: Mixkit effects and music through `sounds.py` while its hosts are allowed, plus synthesis,
  General MIDI instruments and the bundled interface sounds. No voice-over and no generated music
  without an online service and a key from the user.
- A rented GPU farm removes the render limit; it needs the user's account key and network access,
  and costs money. Offer it with numbers; do not assume it.

## References

- `references/treatment-template.md` - the one-page brief, beats, timeline rows, shot list and risks, filled in for the proof film
- `references/render-budget.md` - measured speeds, formulas, what 4K and 60 fps cost here
- `references/craft.md` - lens plan, light, surfaces, character, titles, finish, review loop
- `references/shot-format.md` - the shot JSON for `comp.py`
- `references/sound.md` - cue sheets and mixing rules
- `references/blender-notes.md` - Blender 5.2 facts verified on this machine
