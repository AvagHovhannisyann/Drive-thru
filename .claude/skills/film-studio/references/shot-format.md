# Shot descriptions for `tools/film/comp.py shot`

One JSON file per shot. Paths are relative to the JSON file. Times inside a shot are seconds from the
start of THAT shot; `first_frame` places its frames on the film's frame numbering.

```json
{
 "id": "s1", "fps": 24, "duration": 6.0, "first_frame": 1,
 "plate": "s1_plate.exr",
 "out": "frames/s1_####.png",
 "size": [3840, 2160],
 "lights": {
  "sun":  {"gain": [[0, 1.0], [3.2, 0.0]], "tint": [[0, [1, 1, 1]], [3.2, [1.0, 0.4, 0.22]]]},
  "lamp": [[0, 0, "hold"], [2.6, 0, "hold"], [2.6, 2.2, "hold"], [2.66, 0.5, "hold"], [2.72, 3.0], [3.6, 4.0]],
  "sky":  {"gain": [[0, 1], [4.6, 0.05]], "kelvin": [[0, 6500], [4.6, 12000]]},
  "screen": 1.2
 },
 "screens": {"Laptop_Screen": {"frames": "ui/ui_####.png", "first": 1, "last": 192}},
 "regions": [{"frames": "s1_region_####.exr", "first": 20, "last": 38, "feather": 16}],
 "sequences": {"sun": {"plates": ["sun_a.exr", "sun_b.exr", "sun_c.exr"], "position": [[0, 0], [6, 2]]}},
 "camera": {"scale": [[0, 1.0], [6, 1.075]], "center": [0.47, 0.52], "shift": [0, 0], "angle": 0},
 "overlays": [{"frames": "title/title_####.png", "first": 1, "last": 144}],
 "fade": [[0, 1], [5.4, 1], [6, 0]],
 "look": {"exposure": [[0, 0.35], [3.2, 0.75]], "bloom": 0.16, "bloom_threshold": 0.9,
          "vignette": 0.28, "chromatic": 0.0006, "grain": 0.012, "view": "AgX", "look": "AgX - Medium High Contrast"}
}
```

## Keys

| Key | Meaning |
|---|---|
| `plate` | Multilayer EXR from `filmkit.render_plate` (one pass per light group). Its `.json` holds the tracked screen corners. |
| `frames` | Use INSTEAD of `plate` for a shot rendered frame by frame: single-layer linear EXR files, already denoised. `source_first`, `source_fps` map shot time to file numbers. |
| `lights` | Per light group: a number, keys `[[time, value], ...]`, or `{"gain": keys, "tint": keys}` / `{"gain": keys, "kelvin": keys}`. Groups not listed stay at 1. |
| keys | `[time, value]` or `[time, value, mode]`; `mode` is how to travel to the NEXT key: `smooth` (default), `linear`, `hold`. Two keys at the same time make a jump. |
| `screens` | Object name (a plane tracked in the plate) -> image sequence. The room is lit by the average colour of the current picture; the picture itself replaces the white screen. `strength`, `offset` (s), `fps`, `blur_scale`, `group` (default `screen`). |
| `regions` | Frames where a small area was rendered again (something moved). The patch is blended in with a feathered edge. Frame numbers are film frame numbers. |
| `sequences` | A light group that changes shape over time (sun angle): several plates, `position` moves through them and neighbours are cross-faded. |
| `camera` | Move on the finished plate: `scale` (push-in), `center` (the point that stays put, fractions of the frame), `shift` (fractions of the width), `angle` (degrees). All can be keyed. |
| `size` | Output size. Render the plate at least `scale_max` times larger than this if the push-in must stay pin-sharp. |
| `overlays` | PNG sequences with transparency (titles) placed over the graded picture, under the grain. |
| `fade` | Picture level keys, 0 = black. |
| `look` | `exposure` (stops, can be keyed), `bloom`, `bloom_threshold`, `bloom_radius`, `vignette`, `chromatic`, `grain`, `grain_size`, `tint`, `view`, `look`. |

## What a plate shot can and cannot do

Can: any light level and colour per group, lights switching and flickering, screens showing anything,
slow push-in / pull-out / drift, titles, grade changes, small moving things via `regions`.

Cannot: parallax (a push-in is a zoom, not a dolly: keep it under about 10 % and slow), moving shadows
from ONE plate (render several sun plates and use `sequences`), reflections of a screen picture's
detail (the room gets the average colour only), large moving objects (render the shot frame by frame).

## Screens in plates

Render the screen as plain white emission (see `plain_white_screen()` in the proof example) and track
the plane: `fk.render_plate(path, track=["Laptop_Screen"])`. The plane must come from `fk.plane()`
(its UVs tell the compositor which corner is which). If the screen is out of focus the recorded
blur circle softens the inserted picture to match.
