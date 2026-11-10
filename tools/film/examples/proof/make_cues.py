#!/usr/bin/env python3
"""Cue sheet for the pipeline-proof film. Times come from the same numbers the picture uses."""
import json
import sys

TEXT = "Light the room from dusk to night, then let the lamp take over."
S1_HOP, S2 = 4.2, 6.0
typing = [round(0.25 + (i + 0.5) / len(TEXT) * 2.6 + 0.012 * ((i * 7919) % 5 - 2), 3)
          for i, ch in enumerate(TEXT) if ch != " "]
landings = [S1_HOP + 0.55 * 0.88, S2 + 0.35 + 0.5 * 0.88, S2 + 1.05 + 0.45 * 0.88]
cues = {
    "duration": 8.0, "lufs": -14, "reverb": 0.24, "fade_out": 0.9,
    "tracks": [
        {"type": "pad", "t": 0.0, "dur": 4.8, "notes": ["F2", "C3", "A3", "E4", "G4"], "gain": -15, "attack": 1.2, "release": 2.2, "bright": 1300},
        {"type": "pad", "t": 3.9, "dur": 4.1, "notes": ["D2", "A2", "F3", "C4", "E4"], "gain": -15, "attack": 1.4, "release": 1.6, "bright": 1000},
        {"type": "keys", "program": 0, "gain": -11, "reverb": 0.35,
         "notes": [[0.5, "A4", 1.6, 62], [1.25, "C5", 1.6, 58], [2.0, "E5", 1.6, 60], [2.75, "G5", 2.2, 66],
                   [4.0, "F5", 1.4, 58], [4.75, "E5", 1.4, 54], [5.5, "C5", 1.2, 56], [6.0, "D5", 1.8, 64], [7.0, "A4", 2.5, 52],
                   [0.5, "F3", 3.0, 44], [4.0, "D3", 3.5, 44]]},
        {"type": "tick", "times": typing, "gain": -22, "pan": -0.1},
        {"type": "thud", "t": landings[0], "gain": -14, "pan": 0.15},
        {"type": "sfx", "t": 2.6, "file": "uisfx:mechanical/toggle-on", "gain": -12, "pan": 0.3},
        {"type": "sfx", "t": 5.4, "file": "uisfx:studio/complete", "gain": -15, "reverb": 0.3},
        {"type": "whoosh", "t": 5.72, "dur": 0.56, "gain": -17},
        {"type": "thud", "t": landings[1], "gain": -13, "pan": 0.05},
        {"type": "thud", "t": landings[2], "gain": -17, "pan": 0.05, "pitch": 110},
        {"type": "chime", "t": 6.0, "note": "A5", "gain": -17, "dur": 2.0},
    ],
}
json.dump(cues, open(sys.argv[1], "w"), indent=1)
print(f"{len(typing)} key ticks, landings at {[round(v, 3) for v in landings]}")
