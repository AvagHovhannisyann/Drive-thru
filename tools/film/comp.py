#!/usr/bin/env python3
"""Compositor for plate-based shots: denoise, relight, insert screens, finish and grade.

Run with the studio Python:  /opt/film-studio/venv/bin/python tools/film/comp.py <command> ...

    prepare PLATE.exr                 denoise every light-group pass once -> PLATE.plate.npz
    still   PLATE.exr OUT.png [...]   one graded picture from a plate (look development)
    shot    SHOT.json                 every frame of a shot -> PNG sequence (see docs in the skill)

Why: on a CPU-only machine a path-traced frame costs minutes. A locked-off shot needs ONE
render with a pass per light group; everything that changes afterwards (light levels and
colour, what a screen shows, a slow push-in, bloom, grain) is arithmetic on those passes.
Light is additive, so  picture = sum(gain_g * tint_g * pass_g)  is exact, not a trick.

All arithmetic is in scene-linear Rec.709. The display transform is Blender's own OCIO
configuration (AgX by default), so a graded frame matches what Blender would have saved.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import cv2
import numpy as np

BLENDER_OCIO = os.environ.get(
    "FILM_OCIO", "/opt/blender-dl/current/5.2/datafiles/colormanagement/config.ocio")
GUIDES = ("Denoising Albedo", "Denoising Normal")

# --------------------------------------------------------------------------- reading plates


def read_exr(path: str) -> dict[str, np.ndarray]:
    """All passes of a Blender multilayer EXR as float32 arrays, keyed by pass name."""
    import OpenEXR
    passes: dict[str, np.ndarray] = {}
    with OpenEXR.File(str(path)) as exr:
        for part in exr.parts:
            channels = part.channels
            first = next(iter(channels))
            name = first.split(".", 1)[1] if "." in first else first
            if len(channels) == 1:
                data = channels[first].pixels
                if name.endswith((".Z", ".X")):
                    name = name.rsplit(".", 1)[0]
            else:                                   # split vectors: X, Y, Z planes
                name = name.rsplit(".", 1)[0]
                data = np.stack([channels[key].pixels for key in sorted(channels)], axis=-1)
            passes[name] = np.asarray(data, dtype=np.float32)
    return passes


_oidn_device = None


def denoise(color: np.ndarray, albedo: np.ndarray | None = None, normal: np.ndarray | None = None) -> np.ndarray:
    """OpenImageDenoise 'RT' filter on a linear HDR image, guided by albedo and normal."""
    import oidn
    global _oidn_device
    if _oidn_device is None:
        _oidn_device = oidn.NewDevice()
        oidn.CommitDevice(_oidn_device)
    height, width = color.shape[:2]
    color = np.ascontiguousarray(color[..., :3], dtype=np.float32)
    output = np.zeros_like(color)
    filt = oidn.NewFilter(_oidn_device, "RT")
    oidn.SetSharedFilterImage(filt, "color", color, oidn.FORMAT_FLOAT3, width, height)
    keep = [color, output]
    if albedo is not None and normal is not None:
        albedo = np.ascontiguousarray(albedo[..., :3], dtype=np.float32)
        normal = np.ascontiguousarray(normal[..., :3], dtype=np.float32)
        oidn.SetSharedFilterImage(filt, "albedo", albedo, oidn.FORMAT_FLOAT3, width, height)
        oidn.SetSharedFilterImage(filt, "normal", normal, oidn.FORMAT_FLOAT3, width, height)
        keep += [albedo, normal]
    oidn.SetSharedFilterImage(filt, "output", output, oidn.FORMAT_FLOAT3, width, height)
    oidn.SetFilterBool(filt, "hdr", True) if hasattr(oidn, "SetFilterBool") else None
    oidn.CommitFilter(filt)
    oidn.ExecuteFilter(filt)
    oidn.ReleaseFilter(filt)
    return output


_plates: dict[str, dict[str, np.ndarray]] = {}


def prepare(plate: str, force: bool = False) -> dict[str, np.ndarray]:
    """Denoised light-group passes of a plate, cached next to it as <plate>.plate.npz and in memory.
    Keys: one per light group, 'other' (light in no group, when there is any) and 'depth'.
    A plate rendered with a region (see filmkit.render_plate) is cropped to that region before
    denoising; its position is returned as 'rect' = [top, bottom, left, right] in pixels."""
    plate = str(plate)
    if plate in _plates and not force:
        return _plates[plate]
    cache = Path(plate.removesuffix(".exr") + ".plate.npz")
    if cache.exists() and not force and cache.stat().st_mtime >= Path(plate).stat().st_mtime:
        with np.load(cache) as data:                       # float16 on disk, float32 in memory (faster arithmetic)
            _plates[plate] = {key: data[key].astype(np.float32) if data[key].dtype == np.float16 else data[key]
                              for key in data.files}
        return _plates[plate]
    passes = read_exr(plate)
    beauty = passes.get("Noisy Image", passes.get("Combined"))
    out: dict[str, np.ndarray] = {}
    if beauty is not None and beauty.shape[-1] == 4 and float(beauty[..., 3].min()) == 0.0:
        rows, cols = np.where(beauty[..., 3] > 0)
        top, bottom, left, right = int(rows.min()), int(rows.max()) + 1, int(cols.min()), int(cols.max()) + 1
        passes = {name: image[top:bottom, left:right] for name, image in passes.items()}
        beauty = passes.get("Noisy Image", passes.get("Combined"))
        out["rect"] = np.array([top, bottom, left, right], np.int32)
    albedo, normal = passes.get(GUIDES[0]), passes.get(GUIDES[1])
    groups = {name[len("Combined_"):]: image for name, image in passes.items() if name.startswith("Combined_")}
    if groups:
        total = np.zeros_like(next(iter(groups.values()))[..., :3])
        for name, image in groups.items():
            out[name] = denoise(image, albedo, normal).astype(np.float16)
            total += image[..., :3]
        rest = np.clip(beauty[..., :3] - total, 0, None)
        if float(rest.mean()) > 1e-4:
            out["other"] = denoise(rest, albedo, normal).astype(np.float16)
    elif beauty is not None:
        out["beauty"] = denoise(beauty, albedo, normal).astype(np.float16)
    if "Depth" in passes:
        out["depth"] = passes["Depth"].astype(np.float32)
    np.savez(cache, **out)
    _plates[plate] = {key: value.astype(np.float32) if value.dtype == np.float16 else value for key, value in out.items()}
    return _plates[plate]


def read_frame(path: str) -> np.ndarray:
    """A single-layer linear EXR frame (already denoised by the renderer) as float32 RGB."""
    passes = read_exr(path)
    image = passes.get("Combined", next(iter(passes.values())))
    return np.ascontiguousarray(image[..., :3], dtype=np.float32)


# --------------------------------------------------------------------------- colour


_processors: dict[tuple, object] = {}


def display(linear: np.ndarray, view: str = "AgX", look: str = "AgX - Medium High Contrast", exposure: float = 0.0,
            bits: int = 8) -> np.ndarray:
    """Scene-linear Rec.709 -> display-referred sRGB picture using Blender's OCIO configuration."""
    import PyOpenColorIO as ocio
    key = (view, look)
    if key not in _processors:
        config = ocio.Config.CreateFromFile(BLENDER_OCIO)
        transform = ocio.DisplayViewTransform(src=ocio.ROLE_SCENE_LINEAR, display="sRGB", view=view)
        if look and look != "None":
            group = ocio.GroupTransform()
            group.appendTransform(ocio.LookTransform(src=ocio.ROLE_SCENE_LINEAR, dst=ocio.ROLE_SCENE_LINEAR, looks=look))
            group.appendTransform(transform)
            transform = group
        _processors[key] = config.getProcessor(transform).getDefaultCPUProcessor()
    image = np.ascontiguousarray(linear[..., :3] * (2.0 ** exposure), dtype=np.float32)
    _processors[key].applyRGB(image)
    image = np.clip(image, 0.0, 1.0)
    if bits == 16:
        return (image * 65535.0 + 0.5).astype(np.uint16)
    noise = (np.random.default_rng(7).random(image.shape[:2], dtype=np.float32)[..., None] - 0.5) / 255.0
    return (np.clip(image + noise, 0, 1) * 255.0 + 0.5).astype(np.uint8)      # dithered: no banding in gradients


def srgb_to_linear(image: np.ndarray) -> np.ndarray:
    image = image.astype(np.float32) / (65535.0 if image.dtype == np.uint16 else 255.0)
    return np.where(image <= 0.04045, image / 12.92, ((image + 0.055) / 1.055) ** 2.4).astype(np.float32)


def kelvin(temperature: float) -> np.ndarray:
    """Approximate linear RGB tint of a black body, normalised to green = 1 (1000-12000 K)."""
    t = temperature / 100.0
    r = 255.0 if t <= 66 else 329.698727446 * (t - 60) ** -0.1332047592
    g = 99.4708025861 * math.log(t) - 161.1195681661 if t <= 66 else 288.1221695283 * (t - 60) ** -0.0755148492
    b = 255.0 if t >= 66 else (0.0 if t <= 19 else 138.5177312231 * math.log(t - 10) - 305.0447927307)
    srgb = np.clip(np.array([r, g, b]) / 255.0, 0.0, 1.0)
    linear = np.where(srgb <= 0.04045, srgb / 12.92, ((srgb + 0.055) / 1.055) ** 2.4)
    return (linear / max(linear[1], 1e-6)).astype(np.float32)


# --------------------------------------------------------------------------- picture operations (linear)


def relight(groups: dict[str, np.ndarray], gains: dict[str, float | list], skip: tuple[str, ...] = ("depth", "rect"),
            only: tuple[str, ...] | None = None) -> np.ndarray:
    """sum(gain * pass). A gain is a number, or [number, [r, g, b]] to tint that light as well.
    `only` restricts the sum to some groups (the rest count as zero)."""
    out = None
    for name, image in groups.items():
        if name in skip or (only is not None and name not in only):
            continue
        gain = gains.get(name, 1.0)
        factor = np.float32(gain) if not isinstance(gain, (list, tuple)) else \
            np.asarray(gain[1], np.float32) * np.float32(gain[0])
        if not np.any(factor):
            continue
        if out is None:
            out = np.multiply(image, factor, dtype=np.float32)
        else:
            out += np.multiply(image, factor, dtype=np.float32)
    if out is None:
        out = np.zeros(next(iter(groups.values())).shape[:2] + (3,), np.float32)
    return out


_masks: dict[tuple, np.ndarray] = {}


def quad_mask(shape: tuple[int, int], corners: list[list[float]], blur_px: float = 0.0, supersample: int = 4) -> np.ndarray:
    """Anti-aliased coverage (0-1) of a four-cornered polygon."""
    height, width = shape
    key = ("quad", height, width, tuple(round(float(v), 3) for c in corners for v in c), round(blur_px, 2))
    if key in _masks:
        return _masks[key]
    big = np.zeros((height * supersample, width * supersample), np.uint8)
    cv2.fillConvexPoly(big, np.round(np.asarray(corners, np.float32) * supersample).astype(np.int32), 255)
    mask = cv2.resize(big, (width, height), interpolation=cv2.INTER_AREA).astype(np.float32) / 255.0
    if blur_px > 0.6:
        mask = cv2.GaussianBlur(mask, (0, 0), blur_px / 2.5)
    _masks[key] = mask
    return mask


def insert_screen(picture: np.ndarray, without_screen: np.ndarray, screen_pass: np.ndarray, ui_linear: np.ndarray,
                  corners: list[list[float]], strength: float = 1.0, blur_px: float = 0.0) -> np.ndarray:
    """Put a picture on an emissive screen that was rendered plain white.
    `picture` already contains the room lit by the screen (screen pass scaled by the picture's
    mean colour); inside the screen outline the white pass is replaced by the picture itself."""
    height, width = picture.shape[:2]
    corners_np = np.asarray(corners, np.float32)
    target_w = max(np.linalg.norm(corners_np[1] - corners_np[0]), np.linalg.norm(corners_np[2] - corners_np[3]))
    scale = min(1.0, 2.0 * target_w / ui_linear.shape[1])
    source = cv2.resize(ui_linear, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA) if scale < 1 else ui_linear
    sh, sw = source.shape[:2]
    matrix = cv2.getPerspectiveTransform(np.float32([[0, 0], [sw, 0], [sw, sh], [0, sh]]), corners_np)
    warped = cv2.warpPerspective(source, matrix, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    if blur_px > 0.6:
        warped = cv2.GaussianBlur(warped, (0, 0), blur_px / 2.5)
    mask = quad_mask((height, width), corners, blur_px)[..., None]
    # What the white screen itself looked like in the plate, to keep its glossy falloff and vignetting.
    white = np.clip(screen_pass.astype(np.float32), 0, None)
    level = float(np.percentile(white[mask[..., 0] > 0.99].mean(axis=-1), 60)) if (mask > 0.99).any() else 1.0
    shading = np.clip(white.mean(axis=-1, keepdims=True) / max(level, 1e-4), 0.0, 1.5)
    lit = without_screen + warped * shading * level * strength
    return picture * (1 - mask) + lit * mask


def bloom(image: np.ndarray, threshold: float = 1.0, intensity: float = 0.12, radius: float = 0.02) -> np.ndarray:
    """Soft glow around highlights: bright parts are blurred at several sizes and added back."""
    if intensity <= 0:
        return image
    height, width = image.shape[:2]
    luminance = image @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    bright = image * np.clip((luminance - threshold) / np.maximum(luminance, 1e-4), 0, 1)[..., None]
    small = cv2.resize(bright, (max(8, width // 4), max(8, height // 4)), interpolation=cv2.INTER_AREA)
    glow = np.zeros_like(small)
    for scale, weight in ((0.35, 0.5), (1.0, 0.3), (2.6, 0.2)):
        glow += weight * cv2.GaussianBlur(small, (0, 0), max(0.5, radius * scale * width / 4))
    return image + intensity * cv2.resize(glow, (width, height), interpolation=cv2.INTER_LINEAR)


def vignette(image: np.ndarray, amount: float = 0.25, power: float = 2.2) -> np.ndarray:
    if amount <= 0:
        return image
    height, width = image.shape[:2]
    key = ("vignette", height, width, amount, power)
    if key not in _masks:
        y = ((np.arange(height, dtype=np.float32) - height / 2) / (height / 2))[:, None]
        x = ((np.arange(width, dtype=np.float32) - width / 2) / (width / 2))[None, :]
        _masks[key] = (1 - amount * (np.hypot(x, y) / math.sqrt(2)) ** power).astype(np.float32)[..., None]
    return image * _masks[key]


def chromatic(image: np.ndarray, amount: float = 0.0008) -> np.ndarray:
    """Lateral chromatic aberration: red slightly larger, blue slightly smaller, growing to the edges."""
    if amount <= 0:
        return image
    height, width = image.shape[:2]
    out = image.copy()
    for channel, scale in ((0, 1 + amount), (2, 1 - amount)):
        matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 0, scale)
        out[..., channel] = cv2.warpAffine(image[..., channel], matrix, (width, height), flags=cv2.INTER_LINEAR,
                                           borderMode=cv2.BORDER_REPLICATE)
    return out


def move(image: np.ndarray, scale: float = 1.0, center: tuple[float, float] = (0.5, 0.5), shift=(0.0, 0.0),
         angle: float = 0.0, out_size: tuple[int, int] | None = None) -> np.ndarray:
    """Push-in / drift on a finished plate. `center` (fractions of the frame) stays in place while
    the picture is enlarged by `scale`; `shift` is in fractions of the frame width, `angle` in degrees.
    Render the plate larger than the delivery size and pass `out_size` (w, h) to keep it sharp."""
    height, width = image.shape[:2]
    ow, oh = out_size or (width, height)
    fit = ow / width                                    # plate -> output at scale 1.0
    cx, cy = center[0] * width, center[1] * height
    matrix = cv2.getRotationMatrix2D((cx, cy), angle, scale * fit)
    matrix[0, 2] += center[0] * ow - cx + shift[0] * ow
    matrix[1, 2] += center[1] * oh - cy + shift[1] * ow
    shrink = scale * fit < 0.75
    return cv2.warpAffine(image, matrix, (ow, oh), flags=cv2.INTER_AREA if shrink else cv2.INTER_LANCZOS4,
                          borderMode=cv2.BORDER_REFLECT)


def grain(picture: np.ndarray, amount: float = 0.025, seed: int = 0, size: float = 1.0) -> np.ndarray:
    """Film grain on the display-referred picture (uint8 or uint16), strongest in the mid-tones."""
    if amount <= 0:
        return picture
    top = 65535.0 if picture.dtype == np.uint16 else 255.0
    image = picture.astype(np.float32) / top
    height, width = image.shape[:2]
    rng = np.random.default_rng(seed)
    noise = rng.standard_normal((int(height / size), int(width / size)), dtype=np.float32)
    if size != 1.0:
        noise = cv2.resize(noise, (width, height), interpolation=cv2.INTER_CUBIC)
    luminance = image.mean(axis=-1)
    weight = 4 * luminance * (1 - luminance) * 0.8 + 0.2
    image = np.clip(image + (noise * weight * amount)[..., None], 0, 1)
    return (image * top + 0.5).astype(picture.dtype)


def finish(linear: np.ndarray, look: dict, seed: int = 0, bits: int = 8, with_grain: bool = True) -> np.ndarray:
    """Lens effects in linear light, then the display transform, then grain."""
    image = bloom(linear, look.get("bloom_threshold", 1.0), look.get("bloom", 0.1), look.get("bloom_radius", 0.02))
    image = chromatic(image, look.get("chromatic", 0.0))
    image = vignette(image, look.get("vignette", 0.2))
    if look.get("tint"):
        image = image * np.asarray(look["tint"], np.float32)
    picture = display(image, look.get("view", "AgX"), look.get("look", "AgX - Medium High Contrast"),
                      look.get("exposure", 0.0), bits)
    return grain(picture, look.get("grain", 0.012), seed, look.get("grain_size", 1.0)) if with_grain else picture


def overlay(picture: np.ndarray, rgba_path: str, opacity: float = 1.0) -> np.ndarray:
    """Alpha-over a PNG with transparency (titles, captions, logos) on a finished picture."""
    top = cv2.imread(str(rgba_path), cv2.IMREAD_UNCHANGED)
    if top is None:
        raise FileNotFoundError(rgba_path)
    height, width = picture.shape[:2]
    if top.shape[:2] != (height, width):
        top = cv2.resize(top, (width, height), interpolation=cv2.INTER_AREA if top.shape[1] > width else cv2.INTER_CUBIC)
    scale = 65535.0 if picture.dtype == np.uint16 else 255.0
    alpha = top[..., 3:4].astype(np.float32) / 255.0 * opacity
    colour = cv2.cvtColor(top[..., :3], cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0 * scale
    return (picture.astype(np.float32) * (1 - alpha) + colour * alpha + 0.5).astype(picture.dtype)


def save_png(path: str, picture: np.ndarray) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), cv2.cvtColor(picture, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_PNG_COMPRESSION, 2])


def load_image_linear(path: str) -> np.ndarray:
    image = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if image is None:
        raise FileNotFoundError(path)
    return srgb_to_linear(cv2.cvtColor(image[..., :3], cv2.COLOR_BGR2RGB))


# --------------------------------------------------------------------------- shots


def interpolate(keys, t: float):
    """Value at time t from [[time, value], ...] keys (values: numbers or lists), smooth between keys.
    A third item per key chooses the ease into the NEXT key: 'linear', 'smooth' (default), 'hold'."""
    if not isinstance(keys, list) or not keys or not isinstance(keys[0], (list, tuple)):
        return keys
    if t <= keys[0][0]:
        return keys[0][1]
    for a, b in zip(keys, keys[1:]):
        if a[0] <= t <= b[0]:
            u = (t - a[0]) / max(b[0] - a[0], 1e-9)
            mode = a[2] if len(a) > 2 else "smooth"
            if mode == "hold":
                return a[1]
            if mode == "smooth":
                u = u * u * (3 - 2 * u)
            va, vb = np.asarray(a[1], np.float32), np.asarray(b[1], np.float32)
            value = va + (vb - va) * u
            return float(value) if value.ndim == 0 else value.tolist()
    return keys[-1][1]


def _frame_gains(spec: dict, t: float) -> dict:
    gains = {}
    for name, value in spec.items():
        if isinstance(value, dict):                      # {"gain": keys, "kelvin": keys} or {"gain":..., "tint":...}
            gain = interpolate(value.get("gain", 1.0), t)
            tint = kelvin(interpolate(value["kelvin"], t)) if "kelvin" in value else interpolate(value.get("tint"), t)
            gains[name] = [gain, tint] if tint is not None else gain
        else:
            gains[name] = interpolate(value, t)
    return gains


def _feather(height: int, width: int, edge: int) -> np.ndarray:
    ramp_y = np.minimum(np.arange(height), np.arange(height)[::-1]).astype(np.float32)
    ramp_x = np.minimum(np.arange(width), np.arange(width)[::-1]).astype(np.float32)
    weight = np.clip(np.minimum.outer(ramp_y, ramp_x) / max(edge, 1), 0, 1)
    return (weight * weight * (3 - 2 * weight))[..., None]


def render_frame(job: tuple) -> str:
    shot, index, base = job
    fps = shot["fps"]
    t = index / fps                                       # seconds since the start of the shot
    number = index + shot.get("first_frame", 1)
    out = Path(shot["out"].replace("####", f"{number:04d}"))
    if out.exists() and not shot.get("overwrite"):
        return str(out)
    look = dict(shot.get("look", {}))
    if "exposure" in look:
        look["exposure"] = interpolate(look["exposure"], t)

    if "frames" in shot:                                  # a shot rendered frame by frame (real camera move)
        source = int(round(t * shot.get("source_fps", fps))) + shot.get("source_first", 1)
        picture = read_frame(os.path.join(base, shot["frames"].replace("####", f"{source:04d}")))
    else:
        groups = dict(prepare(os.path.join(base, shot["plate"])))
        meta = json.loads(Path(os.path.join(base, shot["plate"]).removesuffix(".exr") + ".json").read_text()) \
            if shot.get("screens") else {}
        gains = _frame_gains(shot.get("lights", {}), t)

        # Region frames: the part of the picture where something moved was rendered again for this frame.
        for spec in shot.get("regions", []):
            if spec["first"] <= number <= spec["last"]:
                patch = prepare(os.path.join(base, spec["frames"].replace("####", f"{number:04d}")))
                top, bottom, left, right = (int(v) for v in patch["rect"])
                weight = _feather(bottom - top, right - left, spec.get("feather", 12))
                for name in [n for n in groups if n in patch and n not in ("depth", "rect")]:
                    merged = groups[name].copy()
                    merged[top:bottom, left:right] = merged[top:bottom, left:right] * (1 - weight) + patch[name] * weight
                    groups[name] = merged

        # Plates that replace each other over time (for example the sun at several angles): cross-fade.
        for name, spec in shot.get("sequences", {}).items():
            position = interpolate(spec["position"], t)        # 0 .. len(plates)-1
            lower = int(min(max(math.floor(position), 0), len(spec["plates"]) - 1))
            upper = min(lower + 1, len(spec["plates"]) - 1)
            mix = position - lower
            a = prepare(os.path.join(base, spec["plates"][lower]))[spec.get("pass", name)]
            groups[name] = a if upper == lower or mix <= 0 else \
                a * (1 - mix) + prepare(os.path.join(base, spec["plates"][upper]))[spec.get("pass", name)] * mix

        screens = shot.get("screens", {})
        screen_groups = {spec.get("group", "screen") for spec in screens.values()}
        ui_images = {}
        for name, spec in screens.items():
            ui_number = int(round((t + spec.get("offset", 0.0)) * spec.get("fps", fps))) + spec.get("first", 1)
            ui_number = min(max(ui_number, spec.get("first", 1)), spec.get("last", ui_number))
            ui = load_image_linear(os.path.join(base, spec["frames"].replace("####", f"{ui_number:04d}")))
            ui_images[name] = ui
            mean = ui.reshape(-1, 3).mean(axis=0) / max(spec.get("white_level", 1.0), 1e-6)
            group = spec.get("group", "screen")
            level = gains.get(group, 1.0)
            level = level[0] if isinstance(level, list) else level
            gains[group] = [level, mean.tolist()]              # the room is lit by the average colour of the picture
        if not screens:
            picture = relight(groups, gains)
        else:
            without = relight(groups, {**gains, **{g: 0.0 for g in screen_groups}})
            picture = without + relight(groups, gains, only=tuple(screen_groups))
            for name, spec in screens.items():
                group = spec.get("group", "screen")
                quad = meta["quads"][name]
                picture = insert_screen(picture, without, groups[group], ui_images[name], quad["corners"],
                                        strength=gains[group][0] * spec.get("strength", 1.0),
                                        blur_px=quad.get("blur_px", 0.0) * spec.get("blur_scale", 1.0))

    camera = shot.get("camera", {})
    size = tuple(shot["size"]) if shot.get("size") else None
    if camera or size:
        picture = move(picture, interpolate(camera.get("scale", 1.0), t), tuple(interpolate(camera.get("center", [0.5, 0.5]), t)),
                       tuple(interpolate(camera.get("shift", [0.0, 0.0]), t)), interpolate(camera.get("angle", 0.0), t), size)
    if "fade" in shot:                                    # [[time, level], ...]: 0 = black, 1 = full picture
        picture = picture * float(interpolate(shot["fade"], t))
    result = finish(picture, look, bits=shot.get("bits", 8), with_grain=False)
    for spec in shot.get("overlays", []):
        over = int(round((t + spec.get("offset", 0.0)) * spec.get("fps", fps))) + spec.get("first", 1)
        if spec.get("first", 1) <= over <= spec.get("last", over):
            result = overlay(result, os.path.join(base, spec["frames"].replace("####", f"{over:04d}")), spec.get("opacity", 1.0))
    result = grain(result, look.get("grain", 0.012), index + 1000 * shot.get("seed", 1), look.get("grain_size", 1.0))
    save_png(str(out), result)
    return str(out)


def run_shot(path: str, jobs: int = 0, only: str | None = None, overwrite: bool = False) -> None:
    shot = json.loads(Path(path).read_text())
    shot["overwrite"] = overwrite or shot.get("overwrite", False)
    base = str(Path(path).resolve().parent)
    shot["out"] = shot["out"] if os.path.isabs(shot["out"]) else os.path.join(base, shot["out"])
    count = int(round(shot["duration"] * shot["fps"]))
    frames = list(range(count))
    if only:
        first, _, last = only.partition("-")
        frames = list(range(int(first), int(last or first) + 1))
    if "plate" in shot:
        prepare(os.path.join(base, shot["plate"]))         # build caches once, before the workers start
    wanted = {index + shot.get("first_frame", 1) for index in frames}
    for spec in shot.get("regions", []):                   # only the region frames this run will use
        for name in sorted({spec["frames"].replace("####", f"{number:04d}") for number in wanted
                            if spec["first"] <= number <= spec["last"]}):
            prepare(os.path.join(base, name))
    for spec in shot.get("sequences", {}).values():
        for plate in spec["plates"]:
            prepare(os.path.join(base, plate))
    jobs = jobs or max(1, (os.cpu_count() or 2) - 1)
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        for done, _ in enumerate(pool.map(render_frame, [(shot, i, base) for i in frames], chunksize=2), 1):
            if done % 24 == 0 or done == len(frames):
                print(f"  {shot.get('id', Path(path).stem)}: {done}/{len(frames)} frames", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare", help="denoise the light groups of a plate")
    p.add_argument("plate")
    p.add_argument("--force", action="store_true")
    p = sub.add_parser("still", help="one graded picture from a plate")
    p.add_argument("plate")
    p.add_argument("out")
    p.add_argument("--gains", default="{}", help='JSON, e.g. \'{"sun": 1.2, "lamp": [0.5, [1, 0.8, 0.6]]}\'')
    p.add_argument("--look", default="{}", help='JSON, e.g. \'{"exposure": 0.3, "bloom": 0.15, "vignette": 0.25}\'')
    p.add_argument("--screen", help="picture to put on the tracked screen")
    p.add_argument("--screen-name", default="Laptop_Screen")
    p.add_argument("--screen-strength", type=float, default=1.0)
    p = sub.add_parser("shot", help="render every frame of a shot description")
    p.add_argument("shot")
    p.add_argument("--jobs", type=int, default=0)
    p.add_argument("--frames", help="only these frame indexes (0-based), e.g. 0-23")
    p.add_argument("--overwrite", action="store_true", help="render frames again even when the PNG exists")
    args = parser.parse_args()

    if args.command == "prepare":
        groups = prepare(args.plate, args.force)
        for name, image in groups.items():
            print(f"{name:>10}: shape {image.shape}, mean {float(np.asarray(image, np.float32).mean()):.4f}")
    elif args.command == "still":
        groups = prepare(args.plate)
        gains = json.loads(args.gains)
        picture = relight(groups, gains)
        if args.screen:
            meta = json.loads(Path(args.plate.removesuffix(".exr") + ".json").read_text())
            ui = load_image_linear(args.screen)
            level = gains.get("screen", 1.0)
            level = level[0] if isinstance(level, list) else level
            gains["screen"] = [level, ui.reshape(-1, 3).mean(axis=0).tolist()]
            picture = relight(groups, gains)
            quad = meta["quads"][args.screen_name]
            picture = insert_screen(picture, relight(groups, {**gains, "screen": 0.0}), groups["screen"], ui,
                                    quad["corners"], level * args.screen_strength, quad.get("blur_px", 0.0))
        save_png(args.out, finish(picture, json.loads(args.look)))
        print(f"wrote {args.out}")
    else:
        run_shot(args.shot, args.jobs, args.frames, args.overwrite)
    return 0


if __name__ == "__main__":
    sys.exit(main())
