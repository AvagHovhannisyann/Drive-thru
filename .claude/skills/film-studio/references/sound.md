# Sound: `tools/film/audio.py`

Everything is offline. A cue sheet (JSON) on the film clock goes in, a 48 kHz 24-bit stereo WAV comes
out at the target loudness (default -14 LUFS integrated, peaks at or under -1 dBFS).

## Track types

| type | What it is | Main settings |
|---|---|---|
| `pad` | Warm sustained chord (detuned saws, moving low-pass) | `notes`, `t`, `dur`, `attack`, `release`, `bright` (Hz) |
| `keys` | Any General MIDI instrument through FluidSynth (FluidR3_GM) | `program` (0 piano, 4 e-piano, 11 vibraphone, 24 nylon guitar, 32 bass, 46 harp, 48 strings, 52 choir, 89 warm pad), `notes` `[[time, pitch, length, velocity], ...]` |
| `tick` | Soft keyboard key | `times` (one per typed character) |
| `thud` | Small landing | `t`, `pitch` |
| `whoosh` | Air for cuts and fast moves; place it so it PEAKS on the cut (start about half its length early) | `t`, `dur` |
| `chime` | Bell tone | `t`, `note`, `dur` |
| `riser`, `sub` | Build-up, low hit | `t`, `dur`, `note` |
| `sfx` | Bundled CC0 interface sounds: `uisfx:<pack>/<cue>` | packs: arcade cinematic dreamy glass mechanical minimal organic rubber scifi soft studio zen; cues include press release toggle-on toggle-off success complete notification typing open close send error |
| `file` | Any audio file | `file`, `t` or `times` |

Every track: `gain` (peak level of that track in dBFS before the mix), `pan` (-1..1), `reverb` (send),
`fade` `[in, out]`.

## Rules that keep it from sounding cheap

- Take every time from the picture's own numbers (the script that animates a hop also writes the
  landing time). Never place sounds by ear against a guessed time.
- Music sits under the picture: pad around -15, melody -11, effects -12 to -20, key ticks -22 to -27.
- One sound per visible event, and silence is allowed. Do not fill every frame.
- A cut wants a reason in the sound: a whoosh peaking on it, a note landing on it, or a hard stop.
- Check with numbers, since nobody here can listen: the tool prints loudness and peak; verify event
  times with onset detection (librosa) against the cue sheet (they should agree within one frame).

## What is not available offline

Voice-over and generated music or sound effects need an online service (for example ElevenLabs)
and a key from the user; neither is set up. A recorded voice file from the user works with `file`.
