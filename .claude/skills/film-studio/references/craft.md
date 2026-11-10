# Craft: what makes a code-built Blender film look directed

Distilled from a shot-by-shot study of a 59-second, 13-shot Blender film made by an AI agent
(one cosy room, a toy character, a laptop that "works through the night"; rendered on rented GPUs),
and from the film pipelines in the vendored skills. Study the method. Do not copy that film.

## 1. One place, one clock, few ideas

- One location dressed well beats five thin ones. Every prop is modelled once and seen from many lenses.
- Everything is driven by film seconds: shots, light, screen content, character, score, sound, titles.
  Write the timeline first as rows (SHOTS / LIGHT / SCREEN / CHARACTER / SCORE / SOUND / TITLES);
  the frame number is seconds x fps. A change to the edit is a change to numbers, not to scenes.
- Plan the room in millimetres on a top view with a camera arrow and lens per shot before modelling.

## 2. Lens plan

| Use | Lens | Aperture | Note |
|---|---|---|---|
| Establishing, the whole set | 28-35 mm | f/2.8-4 | camera low, slight push-in |
| Normal view, two objects in relation | 40-50 mm | f/2.8 | default |
| Insert on a prop or a face | 85-100 mm | f/1.8-2.8 | shallow focus, background becomes colour |
| Macro (keys, fingers, texture) | 90-105 mm close | f/2-4 | focus on the nearest edge of the subject |

Alternate wide and tight. Two wides in a row feel static, two macros in a row lose the room.
Cut on an action or a sound. Typical lengths: 2.5-5 s per shot, the opener and the last shot longer.

## 3. Light is the story

- Give each light a job and a GROUP: sun (hard, warm, low), sky (soft, cool), practicals (lamp, screen),
  fill (a large dim card standing in for the bounce of the unseen room). Groups let the compositor move
  the time of day with no new render.
- Time passing = sun gain down and redder, sky down and bluer, practicals up. Night is NOT dark:
  expose for the practicals, keep a blue floor of 3-6 % sky so shadows have colour.
- Warm practical against cool ambient is the look; keep both in frame.
- A lamp switching on wants two frames of flicker before it settles.

## 4. Surfaces

- Bevel every man-made edge (0.5-6 mm); an unbevelled edge is the first thing that reads as CG.
- No uniform surface: small roughness and colour variation plus fine bump (`fk.add_surface_noise`).
- Real geometry for repeated things seen close (planks, keys, books) with per-object variation.
- Roughness does more than colour. Glossy coat over a rough base for ceramics, lacquered wood, plastic.
- For hero surfaces and props use scanned assets (`tools/film/assets.py`): a Poly Haven wood set or a
  photoscanned pot beats any procedural version. Keep procedural materials for walls, plastics and metals.
- Screens are emissive images with a glossy coat; what they show is a real web page rendered to frames.

## 5. Character with almost no rig

A simple shape with eyes carries a film if it moves well: anticipation (crouch), stretch in flight,
squash on landing, one overshoot, then stillness. `fk.hop()` gives height and scale for one hop.
Turn the whole body to look at things. Keep hops low (30-80 % of body height) and landings on a sound.

## 6. Titles

Serif for statements, small spaced sans for labels. Words arrive one after another (60-80 ms apart),
rise 20-30 px while fading and un-blurring, hold at least 1.2 s plus 0.25 s per word, leave together.
Keep them inside the lower-left or centre safe area, never over the subject's face or the screen text.
Titles are HTML pages rendered to transparent PNG frames and laid over the graded picture.

## 7. Finish

Bloom only from real highlights (threshold near 1.0), a light vignette, a trace of chromatic aberration,
fine grain last. AgX with a contrast look; move exposure, not light power, for global brightness.
The same finish goes on every shot, so plates and frame-by-frame shots match.

## 8. Review loop (do not skip)

1. Stills at quarter size for composition and light, looked at with your own eyes, three rounds minimum.
2. A contact sheet of the animation (12-24 frames) before any long render: poses, framing, continuity.
3. After the encode: `tools/film/qa.py` numbers plus its contact sheet; fix and re-run only what changed.
A separate reviewer agent that has not seen your intent catches more than you will.
