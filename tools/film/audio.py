#!/usr/bin/env python3
"""Score and sound for a film from a cue sheet, with no online service.

    /opt/film-studio/venv/bin/python tools/film/audio.py CUES.json OUT.wav [--stems DIR]

The cue sheet is on the same clock as the picture (seconds from the start of the film):

    {"duration": 8.0, "lufs": -14, "reverb": 0.22,
     "tracks": [
       {"type": "pad",   "t": 0, "dur": 8, "notes": ["F2", "C3", "A3", "E4"], "gain": -16},
       {"type": "keys",  "program": 0, "gain": -12, "notes": [[0.5, "A4", 1.2, 70], [1.0, "C5", 1.0, 64]]},
       {"type": "tick",  "times": [0.3, 0.41, 0.55], "gain": -24},
       {"type": "thud",  "t": 1.34, "gain": -12},
       {"type": "whoosh", "t": 5.75, "dur": 0.5, "gain": -14},
       {"type": "chime", "t": 6.4, "note": "C6", "gain": -14},
       {"type": "sfx",   "t": 2.6, "file": "uisfx:mechanical/toggle-on", "gain": -6},
       {"type": "file",  "t": 0, "file": "music.wav", "gain": -8}
     ]}

Sources: numpy synthesis (pad, tick, thud, whoosh, chime, riser, sub), FluidSynth with the
General MIDI soundfont for real instruments ("keys": any GM program, 0 = grand piano, 48 = strings),
the CC0 uisfx interface sounds bundled with the video-director skill, and your own files.
Every track may set "pan" (-1..1), "reverb" (send 0..1) and "fade" [in, out] seconds.
The mix is limited and normalised to the target loudness (default -14 LUFS, peaks under -1 dBFS).
"""

from __future__ import annotations

import argparse
import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal

SR = 48000
SOUNDFONT = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
UISFX = Path(__file__).resolve().parents[2] / ".claude/skills/video-director/real-sfx/vendor/node_modules/uisfx/sounds"
NOTES = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}


def midi(note: str | int) -> int:
    if isinstance(note, int):
        return note
    name, octave = note.rstrip("0123456789-"), int(note[len(note.rstrip("0123456789-")):])
    return 12 * (octave + 1) + NOTES[name[0].upper()] + name.count("#") - name.count("b")


def hz(note: str | int) -> float:
    return 440.0 * 2 ** ((midi(note) - 69) / 12)


def db(gain: float) -> float:
    return 10 ** (gain / 20)


def envelope(n: int, attack: float, release: float) -> np.ndarray:
    env = np.ones(n, np.float32)
    a, r = min(n, int(attack * SR)), min(n, int(release * SR))
    if a:
        env[:a] = np.sin(np.linspace(0, np.pi / 2, a)) ** 2
    if r:
        env[-r:] *= np.cos(np.linspace(0, np.pi / 2, r)) ** 2
    return env


def lowpass(x: np.ndarray, cutoff: float, order: int = 2) -> np.ndarray:
    sos = signal.butter(order, min(cutoff, SR * 0.45), "low", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=0).astype(np.float32)


def bandpass(x: np.ndarray, low: float, high: float) -> np.ndarray:
    sos = signal.butter(2, [max(20, low), min(high, SR * 0.45)], "band", fs=SR, output="sos")
    return signal.sosfilt(sos, x, axis=0).astype(np.float32)


def stereo(mono: np.ndarray, pan: float = 0.0) -> np.ndarray:
    angle = (pan + 1) * math.pi / 4
    return np.stack([mono * math.cos(angle), mono * math.sin(angle)], axis=1).astype(np.float32)


# --------------------------------------------------------------------------- synthesis


def pad(notes: list, dur: float, attack: float = 1.5, release: float = 2.0, bright: float = 900.0, seed: int = 1) -> np.ndarray:
    """Warm sustained chord: detuned saw pairs per note, slowly moving low-pass, wide stereo."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    left, right = np.zeros(n, np.float32), np.zeros(n, np.float32)
    for index, note in enumerate(notes):
        f = hz(note)
        for detune, side in ((-0.06, 0), (0.07, 1), (0.0, index % 2)):
            phase = rng.random() * math.tau
            freq = f * 2 ** (detune / 12)
            wave = sum(np.sin(math.tau * freq * k * t + phase * k) / k for k in range(1, 9)).astype(np.float32)
            wave *= 1 + 0.08 * np.sin(math.tau * (0.11 + 0.05 * index) * t + phase)
            (left if side == 0 else right)[:] += wave / (len(notes) * 3)
    out = np.stack([left, right], axis=1)
    sweep = bright * (1 + 0.5 * np.sin(math.tau * t / max(dur, 1e-3) * 0.5))
    lo, hi = lowpass(out, bright * 0.6, 2), lowpass(out, bright * 1.6, 2)
    mix = ((sweep - bright * 0.5) / bright)[:, None].clip(0, 1).astype(np.float32)
    return (lo * (1 - mix) + hi * mix) * envelope(n, attack, release)[:, None]


def tick(seed: int = 0, bright: float = 1.0) -> np.ndarray:
    """One soft keyboard key: a damped click plus a short low body."""
    rng = np.random.default_rng(seed)
    n = int(0.06 * SR)
    t = np.arange(n) / SR
    click = bandpass(rng.standard_normal(n).astype(np.float32), 1800 * bright, 6500 * bright) * np.exp(-t * 190)
    body = np.sin(math.tau * (150 + 40 * rng.random()) * t) * np.exp(-t * 85) * 0.5
    return ((click * 0.9 + body) * (0.8 + 0.4 * rng.random())).astype(np.float32)


def thud(pitch: float = 95.0, dur: float = 0.32) -> np.ndarray:
    """Small soft landing: pitch-dropping sine with a dull tap on top."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    freq = pitch * (0.55 + 0.45 * np.exp(-t * 26))
    tone = np.sin(math.tau * np.cumsum(freq) / SR) * np.exp(-t * 15)
    tap = lowpass(np.random.default_rng(3).standard_normal(n).astype(np.float32), 1400) * np.exp(-t * 120) * 0.5
    return (tone + tap).astype(np.float32)


def whoosh(dur: float = 0.6, low: float = 250.0, high: float = 5000.0, seed: int = 5) -> np.ndarray:
    """Air movement for cuts and fast moves: noise through a band that sweeps up, swelling then fading."""
    n = int(dur * SR)
    noise = np.random.default_rng(seed).standard_normal(n).astype(np.float32)
    out = np.zeros(n, np.float32)
    blocks = 24
    for b in range(blocks):
        a, e = b * n // blocks, (b + 1) * n // blocks
        centre = low * (high / low) ** ((b + 0.5) / blocks)
        out[a:e] = bandpass(noise, centre * 0.6, centre * 1.6)[a:e]
    u = np.linspace(0, 1, n)
    return (out * np.sin(np.pi * u ** 0.8) ** 2).astype(np.float32)


def chime(note: str | int = "C6", dur: float = 2.2) -> np.ndarray:
    """Bell-like tone: inharmonic partials that decay at different rates."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = hz(note)
    out = np.zeros(n, np.float32)
    for ratio, level, decay in ((1.0, 1.0, 2.2), (2.76, 0.42, 3.6), (5.4, 0.2, 5.5), (8.93, 0.1, 8.0), (0.5, 0.25, 1.6)):
        out += (level * np.sin(math.tau * f * ratio * t) * np.exp(-t * decay)).astype(np.float32)
    out[: int(0.004 * SR)] *= np.linspace(0, 1, int(0.004 * SR))
    return out


def riser(dur: float = 2.0, start: str | int = "C3", octaves: float = 1.0) -> np.ndarray:
    n = int(dur * SR)
    u = np.linspace(0, 1, n)
    freq = hz(start) * 2 ** (octaves * u ** 2)
    phase = math.tau * np.cumsum(freq) / SR
    tone = sum(np.sin(phase * k) / k for k in (1, 2, 3)) * 0.4
    air = bandpass(np.random.default_rng(9).standard_normal(n).astype(np.float32), 800, 7000) * 0.4 * u
    return ((tone + air) * u ** 2).astype(np.float32)


def sub(note: str | int = "F1", dur: float = 1.5) -> np.ndarray:
    n = int(dur * SR)
    t = np.arange(n) / SR
    return (np.sin(math.tau * hz(note) * t) * np.exp(-t * 2.2) * np.minimum(1, t * 200)).astype(np.float32)


def fluidsynth(notes: list, program: int = 0, tail: float = 3.0) -> np.ndarray:
    """Notes [[time, pitch, duration, velocity], ...] played by a General MIDI instrument."""
    import mido
    mid = mido.MidiFile(ticks_per_beat=480)
    track = mido.MidiTrack()
    mid.tracks.append(track)
    track.append(mido.MetaMessage("set_tempo", tempo=500000))          # 120 bpm: 960 ticks per second
    track.append(mido.Message("program_change", program=program, time=0))
    events = []
    for start, pitch, length, velocity in notes:
        events.append((start, "note_on", midi(pitch), int(velocity)))
        events.append((start + length, "note_off", midi(pitch), 0))
    last = 0.0
    for when, kind, pitch, velocity in sorted(events):
        track.append(mido.Message(kind, note=pitch, velocity=velocity, time=int(round((when - last) * 960))))
        last = when
    track.append(mido.MetaMessage("end_of_track", time=int(tail * 960)))
    with tempfile.TemporaryDirectory() as tmp:
        mid.save(f"{tmp}/part.mid")
        subprocess.run(["fluidsynth", "-ni", "-g", "0.8", "-r", str(SR), "-F", f"{tmp}/part.wav", SOUNDFONT, f"{tmp}/part.mid"],
                       check=True, capture_output=True)
        data, rate = sf.read(f"{tmp}/part.wav", dtype="float32", always_2d=True)
    assert rate == SR
    return data


def load(path: str, base: Path) -> np.ndarray:
    """A sound file as float32 stereo at 48 kHz. 'uisfx:<pack>/<cue>' reads the bundled library."""
    source = UISFX / (path[len("uisfx:"):] + ".mp3") if path.startswith("uisfx:") else (base / path)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(source), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


# --------------------------------------------------------------------------- mix


def limit(x: np.ndarray, ceiling_db: float = -1.0, lookahead: float = 0.004) -> np.ndarray:
    """Look-ahead peak limiter with no make-up gain: peaks end up at or under the ceiling."""
    from scipy.ndimage import maximum_filter1d, minimum_filter1d, uniform_filter1d
    window = max(1, int(lookahead * SR))
    peak = maximum_filter1d(np.abs(x).max(axis=1), size=2 * window + 1)
    gain = np.minimum(1.0, db(ceiling_db) / np.maximum(peak, 1e-9))
    gain = uniform_filter1d(minimum_filter1d(gain, size=2 * window + 1), size=window)
    return (x * gain[:, None]).astype(np.float32)


def render(cues: dict, base: Path, stems_dir: Path | None = None) -> np.ndarray:
    import pedalboard
    import pyloudnorm
    total = int(cues["duration"] * SR)
    dry = np.zeros((total, 2), np.float32)
    wet = np.zeros((total, 2), np.float32)
    for index, track in enumerate(cues["tracks"]):
        kind = track["type"]
        events: list[tuple[float, np.ndarray]] = []
        if kind == "pad":
            events.append((track.get("t", 0.0), pad(track["notes"], track["dur"], track.get("attack", 1.5), track.get("release", 2.0),
                                                    track.get("bright", 900.0), seed=index)))
        elif kind == "keys":
            events.append((0.0, fluidsynth(track["notes"], track.get("program", 0))))
        elif kind == "tick":
            events += [(when, stereo(tick(seed=i + 11 * index, bright=track.get("bright", 1.0)), track.get("pan", 0.0)))
                       for i, when in enumerate(track["times"])]
        elif kind == "thud":
            events.append((track["t"], stereo(thud(track.get("pitch", 95.0)), track.get("pan", 0.0))))
        elif kind == "whoosh":
            events.append((track["t"], stereo(whoosh(track.get("dur", 0.6)), track.get("pan", 0.0))))
        elif kind == "chime":
            events.append((track["t"], stereo(chime(track.get("note", "C6"), track.get("dur", 2.2)), track.get("pan", 0.0))))
        elif kind == "riser":
            events.append((track["t"], stereo(riser(track.get("dur", 2.0), track.get("note", "C3")), track.get("pan", 0.0))))
        elif kind == "sub":
            events.append((track["t"], stereo(sub(track.get("note", "F1"), track.get("dur", 1.5)))))
        elif kind in ("sfx", "file"):
            sound = load(track["file"], base)
            events += [(when, sound) for when in track.get("times", [track.get("t", 0.0)])]
        else:
            raise SystemExit(f"unknown track type {kind!r}")
        stem = np.zeros((total, 2), np.float32)
        for when, sound in events:
            sound = sound if sound.ndim == 2 else stereo(sound)
            start = int(when * SR)
            if start >= total:
                continue
            sound = sound[: total - start]
            stem[start:start + len(sound)] += sound
        peak = float(np.abs(stem).max()) or 1.0
        stem *= db(track.get("gain", -12.0)) / peak             # gain = peak level of the track in dBFS
        if track.get("fade"):
            stem *= envelope(total, track["fade"][0], track["fade"][1])[:, None]
        dry += stem
        wet += stem * track.get("reverb", 0.25 if kind in ("pad", "keys", "chime", "riser") else 0.08)
        if stems_dir:
            stems_dir.mkdir(parents=True, exist_ok=True)
            sf.write(stems_dir / f"{index:02d}_{kind}.wav", stem, SR, subtype="PCM_24")
    room = pedalboard.Pedalboard([pedalboard.Reverb(room_size=0.78, damping=0.45, wet_level=1.0, dry_level=0.0, width=1.0)])
    mix = dry + room(wet, SR) * cues.get("reverb", 0.22) * 4
    mix = pedalboard.Pedalboard([pedalboard.HighpassFilter(28), pedalboard.Compressor(threshold_db=-16, ratio=2.2, attack_ms=12, release_ms=180)])(mix, SR)
    meter = pyloudnorm.Meter(SR)
    target = cues.get("lufs", -14.0)
    for _ in range(3):                                   # normalise, limit, and correct what the limiter took away
        loudness = meter.integrated_loudness(mix)
        if not math.isfinite(loudness) or abs(target - loudness) < 0.1:
            break
        mix = limit(mix * db(target - loudness), cues.get("ceiling", -1.0))
    fade = min(total, int(cues.get("fade_out", 0.4) * SR))
    if fade:
        mix[-fade:] *= np.linspace(1, 0, fade)[:, None] ** 2
    return np.clip(mix, -1.0, 1.0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("cues")
    parser.add_argument("out")
    parser.add_argument("--stems", help="also write one file per track into this folder")
    args = parser.parse_args()
    cues = json.loads(Path(args.cues).read_text())
    mix = render(cues, Path(args.cues).resolve().parent, Path(args.stems) if args.stems else None)
    sf.write(args.out, mix, SR, subtype="PCM_24")
    import pyloudnorm
    print(f"wrote {args.out}: {len(mix) / SR:.2f} s, {pyloudnorm.Meter(SR).integrated_loudness(mix):.1f} LUFS, "
          f"peak {20 * math.log10(float(np.abs(mix).max()) + 1e-9):.1f} dBFS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
