# Treatment and timeline template

Fill this in before any scene code. One page. The example is the 8-second proof film
(`tools/film/examples/proof/`), so the numbers below match files that exist.

## Brief

| | |
|---|---|
| Purpose | Prove every stage of the pipeline on this machine |
| Audience and where it plays | The person commissioning films; phone or tablet first, then a large screen |
| Length, rate, size | 8.0 s, 24 fps, 3840 x 2160 |
| Words on screen | "One render. Every hour of the day." + one caption line |
| Sound | Soft pad and piano, interface sounds, no voice |

## Idea in one line

A desk passes from golden hour to lamp-lit night in one locked shot, then we go close to the small
character watching the screen.

## Beats

| # | Seconds | What the viewer should feel or learn | How |
|---|---|---|---|
| 1 | 0.0-2.6 | Warm, calm, someone is working | Sun bands on the wall, a brief being typed on the laptop |
| 2 | 2.6-4.2 | Time passes | Sun fades and reddens, sky goes blue, lamp flickers on |
| 3 | 4.2-6.0 | The claim | Character hop-turns to the screen; title arrives |
| 4 | 6.0-8.0 | Intimacy, a living thing | Macro, screen-lit face, two small hops, fade out |

## Timeline (seconds on one clock)

| Row | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| SHOTS | S1 wide plate, 40 mm, push-in 1.00 -> 1.075 ||||||| S2 macro 32 mm, real move ||
| LIGHT | sun 1.0 | sun 0.85 warm | lamp on at 2.6 | sun 0 at 3.2 | night levels from 4.0 || night (same numbers on the real lights) ||
| SCREEN | brief types 0.25-2.85 ||| queue bars fill, log lines 1.0-5.4 ||| continues ||
| CHARACTER | still |||| hop-turn 4.2-4.9 || hop 6.35, hop 7.05, lean 7.45 ||
| SCORE | pad Fmaj9, piano A4 C5 E5 G5 |||| pad Dm9, piano F5 E5 C5 || D5 | A4 | fade |
| SOUND | 51 key ticks ||| switch 2.6 | landing 4.68 | chime 5.4, whoosh peaks 6.0 | landing 6.79 | landing 7.45 | |
| TITLES | ||| in 3.3 || out 5.45 | | fade to black 7.35-8.0 | |

## Shot list and budget

| Shot | Seconds | Type | Camera | What moves | Render cost |
|---|---|---|---|---|---|
| S1 | 0.0-6.0 | plate + regions | 40 mm f/2.8, locked, focus on the screen | light, screen, character in a region for 20 frames, title | 1 plate (16 min) + 20 region frames (13 min) |
| S2 | 6.0-8.0 | frames | 32 mm f/2.8 low over the keyboard, slow push | camera, character | 48 frames at 1600 x 900, 16 samples |

Total machine time planned: about 1 hour. Reserve: 30 minutes.

## Risks and how each is checked

| Risk | Check |
|---|---|
| Region patch shows a border | Hop placed after the sun is gone (short shadows); strip of crops looked at before the full run |
| Macro framing or focus wrong | Five quarter-size frames rendered and looked at before the 48-frame render |
| Night too dark or lamp clipped | `look_check.py --night` on a still from the plate, three balances compared |
| Sound late against picture | Landing times computed from the hop formula; onset detection within one frame |
