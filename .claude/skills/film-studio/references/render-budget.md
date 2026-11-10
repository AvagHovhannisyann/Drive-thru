# Render budget on this machine

Measured 2026-11-10 with Blender 5.2.4 on the cloud container: 4 vCPU, 15 GB RAM, no GPU,
furnished interior (window sun, sky, lamp, emissive screen, about 480 objects with procedural
materials). Re-measure with the proof example after any change of machine: `tools/film/examples/proof/run.sh`.

## The one number

Cycles traces about **0.6 million samples per second** here (0.84 million with plain grey materials).

    seconds per frame  ~  width x height x samples / 600,000  + 2
    (+20 % with motion blur and depth of field; adaptive sampling saves little indoors)

| Frame | Samples | Time per frame | Source |
|---|---|---|---|
| 480 x 270 | 128 | 26 s | measured |
| 960 x 540 | 96, five light groups | 81 s | measured |
| 960 x 540 | 128 + denoise | 102 s | measured |
| 1600 x 900 | 16 + denoise, motion blur, depth of field | 52 s | measured (48 frames) |
| 1920 x 1080 | 32 | about 115 s | formula |
| 1920 x 1080 | 64 | about 225 s | formula |
| 3840 x 2160 | 64, five light groups | 948 s (15.8 min) | measured |
| 3840 x 2160 | 16 | about 4 min | formula |

Light groups are free: the five-group plate costs the same as a plain render.

## What each kind of shot costs

| Shot type | Render cost | Then per finished frame |
|---|---|---|
| Plate at 3840 x 2160, 64 samples | 16 min once | compositing only |
| Region frames (something small moves; region = 9 % of a 4K frame, 32 samples) | 38 s per moving frame | compositing only |
| Extra sun position for moving shadows | one more plate each (sun pass only is used) | compositing only |
| Frame-by-frame at 1600 x 900, 16 samples | 52 s per frame | compositing only (upscaled to 4K there) |
| Frame-by-frame at 3840 x 2160, 64 samples | 16 min per frame: not affordable | - |

Other stages are small (all measured): denoising the six passes of a 4K plate about 1.5 min, once;
compositing a 4K plate frame (relight, screen, push-in, bloom, grade, title, grain, PNG) 4 s per
worker, 1.3 s per frame with three workers; an upscaled frame-by-frame shot 3 s per worker;
192 screen frames at 1920 x 1200 in 18 s; 144 transparent 4K title frames in 35 s; the sound mix
in seconds; encoding 8 s of 4K film 109 s as H.264 (slow) or 82 s as 10-bit H.265, 16 s at 1080p.

## The proof film, as measured

8 s, 24 fps, 3840 x 2160: a 6 s plate shot (dusk to night, screen, title, a character hop in a
region) and a 2 s real camera move. `tools/film/examples/proof/proof_sheet.jpg` shows it.

| Stage | Machine time |
|---|---|
| Plate, 3840 x 2160, 64 samples, five light groups | 15.8 min |
| 20 region frames (9 % of the frame, 32 samples) | 13 min |
| 48 macro frames, 1600 x 900, 16 samples, motion blur | 41.6 min (52 s each) |
| Denoise, compositing 192 frames, sound, encode, checks | about 8 min |
| **Total** | **about 1 h 20 for 8 seconds** |

Three quarters of the film (the plate shot) cost 29 minutes; the 2-second camera move cost 42.
That ratio is the planning rule: every second of real camera movement costs about as much as
ten seconds of plate film.

## Worked examples

**30 s film, 24 fps, 3840 x 2160, 8 plate shots, 2 real camera moves of 2 s each**

| Item | Time |
|---|---|
| 8 plates x 16 min | 2 h 08 |
| 60 region frames (two short character moves) | 38 min |
| 96 moving-camera frames at 1600 x 900, 16 samples | 1 h 20 |
| Denoise, compositing 720 frames, encode, sound | about 30 min |
| **Total machine time** | **about 4 h 40**, plus look development |

The same 30 s rendered frame by frame at 4K and 64 samples: 720 x 16 min = **192 hours**.
That factor of 40 is why the plate method is the default here.

**60 s film:** double it: about 9 hours of machine time. Plan it across sessions; everything resumes.

## 60 fps and 4K

- Plate shots: any frame rate and any size up to the plate. 60 fps costs only 2.5x the compositing.
- Moving-camera shots: 60 fps is 2.5x the frames. Not affordable at useful quality; if 60 fps is
  required, keep the film to plate shots or accept a rented GPU.
- 24 fps is the cinema convention and what the studied reference film used at 4K. Offer 24 or 30 fps
  first and explain that 60 fps mainly buys smoothness in fast motion, which these films rarely have.
- Upscaled moving shots (1600 x 900 to 3840 x 2160) are visibly softer than plates. Use shallow depth
  of field and motion so the softness reads as lens, and never cut from a moving shot to a plate of
  the same framing.

## Levers, measured on the interior (480 x 270, 128 samples)

| Change | Effect on time |
|---|---|
| 64 samples and threshold 0.05 instead of 128 / 0.03 | -50 % |
| Fast GI approximation (`use_fast_gi`, method REPLACE) | -26 %, flatter contact shadows |
| Plain grey materials (upper bound for material simplification) | -25 % |
| Two diffuse bounces instead of four | -7 %, darker corners |
| Light tree off | -8 % |
| Path guiding | +12 % (slower) |
| Window glass removed or made invisible to shadow rays | no change |

Samples and pixels are the only strong levers. Halving bounces or simplifying shaders is not worth
the look it costs.

## Low samples and flicker

Frame-by-frame shots at 16 samples with OpenImageDenoise and an animated seed were measured on ten
consecutive frames of the proof's macro shot: static dark areas change by 0.3 of 255 levels from
frame to frame, lit textured areas by about 1.2 after blurring away fine detail. That is below the
film grain added in finishing (about 3 levels), so 16 samples is usable for short, shallow-focus
moving shots. Check it again on any shot with large flat mid-grey areas, where blotches show first.

## Moving shadows from plates

`sequences` cross-fades plates rendered at different sun angles. Measured: with 14 degree steps the
in-between frames show two shadow patterns at once. Keep steps small enough that a shadow edge moves
less than its own softness between neighbouring plates (about 2-3 degrees for a 1.5 degree sun), or
let the sun fade and redden without moving, which needs no extra plate.

## Staying alive during long renders

The container is suspended when the session is idle; processes stop, files stay. Start long renders
with `run_in_background`, keep working or schedule a check-in, and after a resume run the same
command again (finished plates and frames are skipped). Never run two Blender renders at once: they
share the same four cores and both take twice as long.

## Renting GPUs (not set up; needs the user's decision)

The studied reference film rendered about 1,400 4K frames on 10 rented GPUs in 52 minutes for $5.75.
A rented GPU removes the frame-by-frame limit above: every shot can move, and 4K at 60 fps becomes a
matter of money rather than days. It needs a RunPod API key from the user (ask with the credential
tool, never in chat), the RunPod hosts allowed in the cloud environment, and a check that the proxy
permits the file transfer. The `runpod*` skills in this repository cover the provider side.
Nothing here has been tested against a real GPU; say so when offering it.
