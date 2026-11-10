"""Pipeline-proof shots. Run inside Blender on the set built by scene.py:

    blender -b proof.blend --python shots.py -- plate  --out DIR [--scale 100] [--samples 64]
    blender -b proof.blend --python shots.py -- region --out DIR --frames 20-34 [--samples 32]
    blender -b proof.blend --python shots.py -- macro  --out DIR --frames 1-48 --screen UI_0001.png --screen-frames 144

Shot S1 (0.0-6.0 s): locked-off wide plate; light, screen and push-in happen in tools/film/comp.py.
                     Pip hops once (4.2-4.9 s, after the sun has gone): only the region around it is rendered for those frames.
Shot S2 (6.0-8.0 s): real camera move at night, rendered frame by frame at reduced size.
"""

import math
import os
import sys

import bpy

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "blender"))
import filmkit as fk  # noqa: E402

S1_HOP, S2_START, S2_LENGTH = 4.2, 6.0, 2.0
# Night levels per light group: [gain, tint]. S1 ends on these in the compositor (s1.json) and S2 sets
# the same numbers on the real lights, so the cut between the two shots matches.
NIGHT = {"sun": [0.0, (1, 1, 1)], "sky": [0.10, (0.40, 0.55, 1.0)], "fill": [0.08, (0.45, 0.60, 1.0)],
         "lamp": [10.0, (1, 1, 1)], "screen": [2.4, (1, 1, 1)]}
TURN = -129.0        # degrees about Z: from facing the wide camera to facing the laptop screen
args = sys.argv[sys.argv.index("--") + 1:]
mode = args[0]


def opt(name, default=None, cast=str):
    return cast(args[args.index(name) + 1]) if name in args else default


def animate_pip():
    pip, squash = bpy.data.objects["Pip"], bpy.data.objects["Pip_Squash"]
    base = pip.location.copy()

    def height(t):
        z1, _ = fk.hop(t, S1_HOP, 0.55, 0.075)
        z2, _ = fk.hop(t, S2_START + 0.35, 0.5, 0.06)
        z3, _ = fk.hop(t, S2_START + 1.05, 0.45, 0.035)
        return base.z + z1 + z2 + z3

    def stretch(t):
        s = 1.0
        for start, length, top in ((S1_HOP, 0.55, 0.075), (S2_START + 0.35, 0.5, 0.06), (S2_START + 1.05, 0.45, 0.035)):
            s *= fk.hop(t, start, length, top)[1]
        return s

    end = S2_START + S2_LENGTH
    fk.bake(pip, "location", height, 0.0, end, index=2)
    fk.bake(squash, "scale", stretch, 0.0, end, index=2)
    for axis in (0, 1):
        fk.bake(squash, "scale", lambda t: 1 / math.sqrt(stretch(t)), 0.0, end, index=axis)

    # The S1 hop is a half-turn in the air: Pip lands facing the laptop screen and stays that way.
    # In S2 it leans a little toward the camera after the second hop.
    def facing(t):
        turn = fk.ease_in_out_cubic((t - S1_HOP - 0.08) / 0.42)
        notice = fk.ease_in_out_cubic((t - S2_START - 1.45) / 0.4)
        return math.radians(TURN) * turn + math.radians(24) * notice

    fk.bake(pip, "rotation_euler", facing, 0.0, end, index=2)
    focus = fk.empty("Pip_Focus", (0, -0.034, 0.05))                 # between the eyes
    fk.parent(focus, squash)


def plain_white_screen():
    """Plate mode: the screen emits white; the compositor inserts the picture afterwards."""
    mat = bpy.data.materials["M_Screen"]
    bsdf = fk.principled(mat)
    for link in list(mat.node_tree.links):
        if link.to_socket == bsdf.inputs["Emission Color"]:
            mat.node_tree.links.remove(link)
    bsdf.inputs["Emission Color"].default_value = (1, 1, 1, 1)


def pip_region(sc, frames, margin=0.035):
    """Smallest frame-space rectangle that contains Pip, its shadow and reflection over `frames`."""
    from bpy_extras.object_utils import world_to_camera_view
    from mathutils import Vector
    xs, ys = [], []
    for f in frames:
        sc.frame_set(f)
        root = bpy.data.objects["Pip"].matrix_world.translation
        for dx in (-0.09, 0.09):
            for dy in (-0.12, 0.07):
                for z in (fk_desk, root.z + 0.17):
                    v = world_to_camera_view(sc, sc.camera, Vector((root.x + dx, root.y + dy, z)))
                    xs.append(v.x)
                    ys.append(v.y)
    return (max(0.0, min(xs) - margin), max(0.0, min(ys) - margin), min(1.0, max(xs) + margin), min(1.0, max(ys) + margin))


sc = bpy.context.scene
out = opt("--out", "/opt/film-studio/work/proof")
os.makedirs(out, exist_ok=True)
fk_desk = 0.76
animate_pip()

if mode in ("plate", "region"):
    plain_white_screen()
    sc.camera = bpy.data.objects["Cam_Wide"]
    sc.render.resolution_x, sc.render.resolution_y = 3840, 2160
    sc.render.resolution_percentage = opt("--scale", 100, int)
    if mode == "plate":
        sc.frame_set(1)
        seconds = fk.render_plate(os.path.join(out, "s1_plate"), samples=opt("--samples", 64, int), threshold=0.02,
                                  track=["Laptop_Screen"])
        print(f"PLATE seconds={seconds:.0f}")
    else:
        first, last = (int(v) for v in opt("--frames").split("-"))
        region = pip_region(sc, range(first, last + 1))
        print("REGION", [round(v, 4) for v in region])
        for f in range(first, last + 1):
            target = os.path.join(out, f"s1_region_{f:04d}")
            if os.path.exists(target + ".exr"):
                continue
            sc.frame_set(f)
            seconds = fk.render_plate(target, samples=opt("--samples", 32, int), threshold=0.03, region=region)
            print(f"REGION frame={f} seconds={seconds:.0f}", flush=True)

elif mode == "macro":
    # Night levels, set on the lights themselves: the same numbers S1 ends on in the compositor.
    bpy.data.objects["Sun"].hide_render = True
    world = sc.world.node_tree
    background = next(n for n in world.nodes if n.type == "BACKGROUND")
    sky_link = next(l for l in world.links if l.to_socket == background.inputs["Color"])
    tint = world.nodes.new("ShaderNodeMix")
    tint.data_type, tint.blend_type = "RGBA", "MULTIPLY"
    tint.inputs["Factor"].default_value = 1.0
    tint.inputs["B"].default_value = (*NIGHT["sky"][1], 1.0)
    world.links.new(sky_link.from_socket, tint.inputs["A"])
    world.links.new(tint.outputs["Result"], background.inputs["Color"])
    background.inputs["Strength"].default_value *= NIGHT["sky"][0]
    fill = bpy.data.objects["Fill"].data
    fill.energy, fill.color = fill.energy * NIGHT["fill"][0], NIGHT["fill"][1]
    bpy.data.objects["Lamp_Light"].data.energy *= NIGHT["lamp"][0]
    fk.principled(bpy.data.materials["M_Bulb"]).inputs["Emission Strength"].default_value *= NIGHT["lamp"][0]
    screen = opt("--screen")
    if screen:
        mat = bpy.data.materials["M_Screen"]
        tex = next(n for n in mat.node_tree.nodes if n.type == "TEX_IMAGE")
        tex.image = bpy.data.images.load(screen)
        tex.image.source = "SEQUENCE"
        frames = opt("--screen-frames", 1, int)
        tex.image_user.frame_duration, tex.image_user.frame_start = frames, 1
        tex.image_user.frame_offset = 0          # file number = film frame number
        tex.image_user.use_auto_refresh = True
        fk.principled(mat).inputs["Emission Strength"].default_value = 2.4 * NIGHT["screen"][0]
    pip = bpy.data.objects["Pip"]
    target = (pip.location.x - 0.015, pip.location.y, fk_desk + 0.105)
    # Low over the keyboard, looking back at Pip: the screen behind the camera lights its face.
    cam = fk.camera("Cam_Macro", (-0.13, 1.475, 0.815), target, lens=32, fstop=2.8, focus=bpy.data.objects["Pip_Focus"])
    sc.camera = cam
    # A slow push toward Pip, eased at both ends.
    fk.bake(cam, "location", lambda t: -0.13 + 0.055 * fk.ease_in_out_cubic((t - S2_START) / S2_LENGTH), S2_START,
            S2_START + S2_LENGTH, index=0)
    fk.bake(cam, "location", lambda t: 0.815 + 0.012 * fk.ease_in_out_cubic((t - S2_START) / S2_LENGTH), S2_START,
            S2_START + S2_LENGTH, index=2)
    track = cam.constraints.new("TRACK_TO")
    aim = fk.empty("Cam_Macro_Aim", target)
    track.target, track.track_axis, track.up_axis = aim, "TRACK_NEGATIVE_Z", "UP_Y"
    sc.render.resolution_x, sc.render.resolution_y = 1600, 900
    sc.render.resolution_percentage = opt("--scale", 100, int)
    fk.cycles(samples=opt("--samples", 24, int), threshold=0.05, denoise=True, motion_blur=True, shutter=0.4)
    sc.cycles.use_animated_seed = True
    first, last = (int(v) for v in opt("--frames", "1-48").split("-"))
    offset = fk.frame(S2_START) - 1
    s = sc.render.image_settings
    s.media_type, s.file_format, s.color_depth, s.exr_codec = "IMAGE", "OPEN_EXR", "16", "ZIP"
    import time
    for f in range(first, last + 1):
        target_path = os.path.join(out, f"s2_{f:04d}")
        if os.path.exists(target_path + ".exr"):
            continue
        sc.frame_set(f + offset)
        sc.render.filepath = target_path
        started = time.time()
        bpy.ops.render.render(write_still=True)
        print(f"MACRO frame={f} seconds={time.time() - started:.0f}", flush=True)
