"""Pipeline-proof set: a small desk by a window, built only from code (no downloaded assets).

    blender -b --python tools/film/examples/proof/scene.py -- --out /opt/film-studio/work/proof [--still]

Writes <out>/proof.blend. Units are metres; the room corner behind the desk is at x=-2, y=2.
"""

import math
import os
import random
import sys

import bmesh
import bpy
from mathutils import Vector

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "blender"))
import filmkit as fk  # noqa: E402

DESK_Z = 0.76          # top surface of the desk
DESK_Y = 1.55          # desk centre (it stands against the back wall at y = 2)


def per_object_variation(mat, amount=0.12):
    """Shift the wood pattern and its brightness per object, so planks and books differ."""
    tree = mat.node_tree
    info = tree.nodes.new("ShaderNodeObjectInfo")
    mapping = next(n for n in tree.nodes if n.type == "MAPPING")
    scale = tree.nodes.new("ShaderNodeVectorMath")
    scale.operation = "SCALE"
    scale.inputs["Scale"].default_value = 37.0
    combine = tree.nodes.new("ShaderNodeCombineXYZ")
    for axis in "XYZ":
        tree.links.new(info.outputs["Random"], combine.inputs[axis])
    tree.links.new(combine.outputs["Vector"], scale.inputs[0])
    tree.links.new(scale.outputs["Vector"], mapping.inputs["Location"])
    bsdf = fk.principled(mat)
    link = next(l for l in tree.links if l.to_socket == bsdf.inputs["Base Color"])
    source = link.from_socket
    hsv = tree.nodes.new("ShaderNodeHueSaturation")
    value = tree.nodes.new("ShaderNodeMapRange")
    value.inputs["To Min"].default_value, value.inputs["To Max"].default_value = 1 - amount, 1 + amount
    tree.links.new(info.outputs["Random"], value.inputs["Value"])
    tree.links.new(value.outputs["Result"], hsv.inputs["Value"])
    tree.links.new(source, hsv.inputs["Color"])
    tree.links.new(hsv.outputs["Color"], bsdf.inputs["Base Color"])
    return mat


def build_room(coll):
    wall = fk.add_surface_noise(fk.material("M_Wall", (0.78, 0.70, 0.60), rough=0.85), scale=18, bump=0.35,
                                rough_var=0.05, color_var=0.04)
    floor_mat = per_object_variation(fk.wood("M_Floor", dark=(0.16, 0.085, 0.04), light=(0.36, 0.21, 0.11),
                                             grain_scale=3.0, stretch=10, rough=0.38, axis="Y", coat=0.35), 0.16)
    trim = fk.material("M_Trim", (0.86, 0.84, 0.80), rough=0.45)

    # Floor: real planks, so the gaps and the per-plank variation are geometry, not a texture.
    plank_w, x = 0.14, -2.0
    rng = random.Random(7)
    index = 0
    while x < 2.2:
        y = -2.4 + rng.uniform(-0.6, 0.0)
        while y < 2.0:
            length = rng.uniform(0.9, 1.6)
            fk.box(f"Plank_{index:03d}", (plank_w - 0.002, length - 0.002, 0.02), (x + plank_w / 2, y + length / 2, -0.01),
                   bevel_width=0.0012, segments=2, mat=floor_mat, coll=coll)
            y += length
            index += 1
        x += plank_w

    fk.box("Wall_Back", (4.4, 0.12, 2.8), (0.1, 2.06, 1.4), mat=wall, coll=coll)
    fk.box("Wall_Right", (0.12, 4.6, 2.8), (2.26, -0.2, 1.4), mat=wall, coll=coll)
    # Left wall with a window opening (sill 0.95 m, 1.25 m wide, 1.35 m tall), built from four pieces.
    wx, w0, w1, z0, z1 = -2.06, 0.15, 1.40, 0.95, 2.30
    fk.box("Wall_Left_Low", (0.12, 4.6, z0), (wx, -0.2, z0 / 2), mat=wall, coll=coll)
    fk.box("Wall_Left_High", (0.12, 4.6, 2.8 - z1), (wx, -0.2, (2.8 + z1) / 2), mat=wall, coll=coll)
    fk.box("Wall_Left_Near", (0.12, w0 + 2.5, z1 - z0), (wx, (w0 - 2.5) / 2, (z0 + z1) / 2), mat=wall, coll=coll)
    fk.box("Wall_Left_Far", (0.12, 2.1 - w1, z1 - z0), (wx, (w1 + 2.1) / 2, (z0 + z1) / 2), mat=wall, coll=coll)
    fk.box("Ceiling", (4.6, 4.8, 0.1), (0.1, -0.2, 2.85), mat=wall, coll=coll)
    fk.box("Window_Sill", (0.26, w1 - w0 + 0.12, 0.035), (wx + 0.08, (w0 + w1) / 2, z0 + 0.012), bevel_width=0.006,
           mat=trim, coll=coll)
    for name, size, loc in (
        ("Frame_Top", (0.07, w1 - w0, 0.05), (wx, (w0 + w1) / 2, z1 - 0.025)),
        ("Frame_Bottom", (0.07, w1 - w0, 0.05), (wx, (w0 + w1) / 2, z0 + 0.055)),
        ("Frame_L", (0.07, 0.05, z1 - z0), (wx, w0 + 0.025, (z0 + z1) / 2)),
        ("Frame_R", (0.07, 0.05, z1 - z0), (wx, w1 - 0.025, (z0 + z1) / 2)),
        ("Mullion_V", (0.045, 0.035, z1 - z0), (wx, (w0 + w1) / 2, (z0 + z1) / 2)),
        ("Mullion_H", (0.045, w1 - w0, 0.035), (wx, (w0 + w1) / 2, z0 + (z1 - z0) * 0.58)),
    ):
        fk.box(name, size, loc, bevel_width=0.004, mat=trim, coll=coll)
    fk.box("Window_Glass", (0.004, w1 - w0, z1 - z0), (wx, (w0 + w1) / 2, (z0 + z1) / 2),
           mat=fk.glass("M_WindowGlass", thin=True), coll=coll)
    fk.box("Skirting_Back", (4.3, 0.018, 0.09), (0.1, 1.99, 0.045), bevel_width=0.004, mat=trim, coll=coll)
    fk.box("Skirting_Left", (0.018, 4.3, 0.09), (-1.99, -0.2, 0.045), bevel_width=0.004, mat=trim, coll=coll)


def build_desk(coll):
    top = fk.wood("M_DeskTop", dark=(0.09, 0.04, 0.018), light=(0.23, 0.11, 0.048), grain_scale=4.0, stretch=14,
                  rough=0.34, axis="X", coat=0.45, banding=0.5)
    steel = fk.add_surface_noise(fk.material("M_Steel", (0.05, 0.05, 0.055), rough=0.45, metallic=1.0), scale=120,
                                 bump=0.05, rough_var=0.1, color_var=0.0)
    fk.box("Desk_Top", (1.60, 0.72, 0.036), (0.0, DESK_Y, DESK_Z - 0.018), bevel_width=0.006, mat=top, coll=coll)
    for sx in (-1, 1):
        for sy in (-1, 1):
            fk.box(f"Desk_Leg_{sx}_{sy}", (0.035, 0.035, DESK_Z - 0.036),
                   (sx * 0.74, DESK_Y + sy * 0.30, (DESK_Z - 0.036) / 2), bevel_width=0.003, mat=steel, coll=coll)
    fk.box("Desk_Rail", (1.44, 0.02, 0.05), (0.0, DESK_Y + 0.30, DESK_Z - 0.075), bevel_width=0.002, mat=steel, coll=coll)

    shelf = fk.wood("M_Shelf", dark=(0.13, 0.065, 0.03), light=(0.33, 0.18, 0.09), grain_scale=6, stretch=14, axis="X")
    fk.box("Shelf", (1.10, 0.20, 0.028), (0.25, 1.89, 1.52), bevel_width=0.004, mat=shelf, coll=coll)
    for sx in (-0.22, 0.72):
        fk.box(f"Shelf_Bracket_{sx}", (0.02, 0.16, 0.02), (sx, 1.91, 1.497), bevel_width=0.002, mat=steel, coll=coll)


def build_laptop(coll, screen_image):
    alu = fk.add_surface_noise(fk.material("M_Aluminium", (0.62, 0.63, 0.65), rough=0.32, metallic=1.0), scale=300,
                               bump=0.03, rough_var=0.05, color_var=0.0)
    key_mat = fk.material("M_Keys", (0.018, 0.018, 0.02), rough=0.55)
    root = fk.empty("Laptop", (0.0, DESK_Y - 0.06, DESK_Z), coll)
    w, d = 0.325, 0.225
    fk.parent(fk.box("Laptop_Base", (w, d, 0.012), (0, 0, 0.006), bevel_width=0.004, segments=4, mat=alu, coll=coll), root)
    fk.parent(fk.box("Laptop_KeyWell", (w - 0.04, 0.115, 0.001), (0, 0.035, 0.0122), mat=key_mat, coll=coll), root)
    fk.parent(fk.box("Laptop_Trackpad", (0.11, 0.07, 0.0006), (0, -0.065, 0.0123), bevel_width=0.0002,
                     mat=fk.material("M_Trackpad", (0.55, 0.56, 0.58), rough=0.22, metallic=1.0), coll=coll), root)
    cols, rows, pitch = 14, 5, 0.0192
    for r in range(rows):
        for c in range(cols):
            if r == rows - 1 and 4 <= c <= 8:
                if c != 4:
                    continue
                size, cx = (pitch * 5 - 0.003, pitch - 0.003, 0.0022), (6 - (cols - 1) / 2) * pitch
            else:
                size, cx = (pitch - 0.003, pitch - 0.003, 0.0022), (c - (cols - 1) / 2) * pitch
            key = fk.box(f"Key_{r}_{c:02d}", size, (cx, 0.035 + (rows / 2 - r - 0.5) * pitch, 0.0136),
                         bevel_width=0.0006, segments=2, mat=key_mat, coll=coll)
            fk.parent(key, root)
    hinge = fk.empty("Laptop_Hinge", (0, d / 2 - 0.004, 0.011), coll)
    fk.parent(hinge, root)
    hinge.rotation_euler = (math.radians(-18), 0, 0)             # lid leans 18 degrees past vertical
    lid_h = 0.215
    fk.parent(fk.box("Laptop_Lid", (w, 0.006, lid_h), (0, 0.003, lid_h / 2), bevel_width=0.0025, segments=4,
                     mat=alu, coll=coll), hinge)
    fk.parent(fk.box("Laptop_Bezel", (w - 0.006, 0.001, lid_h - 0.006), (0, -0.0004, lid_h / 2),
                     mat=fk.material("M_Bezel", (0.008, 0.008, 0.009), rough=0.3), coll=coll), hinge)
    screen = fk.plane("Laptop_Screen", (w - 0.022, (w - 0.022) * 10 / 16), (0, -0.0011, lid_h / 2 + 0.003),
                      rot=(math.radians(90), 0, 0), mat=fk.screen_material("M_Screen", screen_image, strength=2.4),
                      coll=coll)
    fk.parent(screen, hinge)
    fk.lightgroup("screen")
    screen.lightgroup = "screen"
    return root, screen


def build_lamp(coll):
    brass = fk.add_surface_noise(fk.material("M_Brass", (0.72, 0.50, 0.20), rough=0.28, metallic=1.0), scale=200,
                                 bump=0.04, rough_var=0.1, color_var=0.03)
    shade_mat = fk.material("M_Shade", (0.62, 0.20, 0.07), rough=0.38, coat_weight=0.7, coat_roughness=0.12)
    x, y = 0.60, DESK_Y + 0.16
    fk.lathe("Lamp_Base", [(0.0, 0.0), (0.075, 0.0), (0.078, 0.006), (0.07, 0.016), (0.02, 0.024), (0.012, 0.03), (0.0, 0.03)],
             loc=(x, y, DESK_Z), mat=brass, coll=coll)
    elbow = (x, y, DESK_Z + 0.31)
    tip = (x - 0.25, y - 0.07, DESK_Z + 0.42)
    fk.rod("Lamp_Stem", (x, y, DESK_Z + 0.025), elbow, 0.0065, mat=brass, coll=coll)
    fk.rod("Lamp_Arm", elbow, tip, 0.0055, mat=brass, coll=coll)
    fk.sphere("Lamp_Elbow", 0.011, elbow, segments=24, mat=brass, coll=coll)
    head = fk.empty("Lamp_Head", tip, coll)
    aim = Vector((0.12, DESK_Y - 0.02, DESK_Z)) - Vector(tip)        # tilt the shade toward the middle of the desk
    head.rotation_euler = aim.to_track_quat("-Z", "Y").to_euler()
    # The shade hangs from the arm: narrow neck at the top (z = 0), opening 8 cm below.
    shade = fk.lathe("Lamp_Shade", [(0.012, 0.012), (0.02, 0.0), (0.032, -0.012), (0.058, -0.045), (0.086, -0.082)],
                     mat=shade_mat, coll=coll, thickness=0.0024)
    fk.parent(shade, head)
    bulb = fk.sphere("Lamp_Bulb", 0.021, (0, 0, -0.045), segments=24, coll=coll,
                     mat=fk.emission("M_Bulb", (1.0, 0.70, 0.40), 14.0))
    fk.parent(bulb, head)
    fk.lightgroup("lamp")
    bulb.lightgroup = "lamp"
    light = fk.spot("Lamp_Light", (0, 0, -0.05), None, power=34.0, angle=120, blend=0.6, radius=0.02,
                    temperature=2700, group="lamp", coll=coll)
    fk.parent(light, head)                                         # a spot shines along its own -Z: out of the shade
    return head


def build_props(coll):
    rng = random.Random(3)
    ceramic = fk.material("M_Mug", (0.86, 0.84, 0.78), rough=0.22, coat_weight=0.5, coat_roughness=0.08)
    fk.lathe("Mug", [(0.0, 0.004), (0.034, 0.004), (0.038, 0.012), (0.04, 0.085), (0.0385, 0.088)],
             loc=(-0.36, DESK_Y - 0.10, DESK_Z), mat=ceramic, coll=coll, thickness=0.004)
    fk.torus_arc("Mug_Handle", 0.024, 0.0052, start=-90, end=90, segments=24, mat=ceramic, coll=coll,
                 loc=(-0.36 + 0.036 * math.cos(math.radians(-125)), DESK_Y - 0.10 + 0.036 * math.sin(math.radians(-125)), DESK_Z + 0.047),
                 rot=(0, 0, math.radians(-125)))
    fk.cylinder("Mug_Coffee", 0.036, 0.002, (-0.36, DESK_Y - 0.10, DESK_Z + 0.07), verts=32, coll=coll,
                mat=fk.material("M_Coffee", (0.05, 0.022, 0.008), rough=0.08))

    terracotta = fk.add_surface_noise(fk.material("M_Terracotta", (0.55, 0.24, 0.13), rough=0.8), scale=60, bump=0.4)
    px, py = -0.58, DESK_Y + 0.17
    fk.lathe("Pot", [(0.0, 0.0), (0.05, 0.0), (0.066, 0.10), (0.072, 0.10), (0.072, 0.118), (0.062, 0.118), (0.058, 0.02), (0.0, 0.02)],
             loc=(px, py, DESK_Z), mat=terracotta, coll=coll)
    fk.cylinder("Pot_Soil", 0.06, 0.004, (px, py, DESK_Z + 0.10), verts=32, coll=coll,
                mat=fk.add_surface_noise(fk.material("M_Soil", (0.035, 0.022, 0.014), rough=0.95), scale=200, bump=1.0))
    leaf_mat = fk.add_surface_noise(fk.material("M_Leaf", (0.07, 0.24, 0.06), rough=0.38, subsurface_weight=0.25,
                                                coat_weight=0.3, coat_roughness=0.3), scale=30, bump=0.1, color_var=0.25)
    for i in range(13):
        ang = i * 2.399963 + rng.uniform(-0.2, 0.2)             # golden-angle spiral
        tilt = math.radians(rng.uniform(18, 62))
        length = rng.uniform(0.13, 0.24)
        bm = bmesh.new()
        segments = 10
        rows = []
        for s in range(segments + 1):
            u = s / segments
            half = 0.5 * length * 0.42 * math.sin(math.pi * u ** 0.75) * (1 - 0.15 * u)
            droop = -0.35 * length * u * u
            rows.append([bm.verts.new((-half, u * length, droop + abs(half) * 0.25)), bm.verts.new((0, u * length, droop)),
                         bm.verts.new((half, u * length, droop + abs(half) * 0.25))])
        for a, b in zip(rows, rows[1:]):
            bm.faces.new((a[0], a[1], b[1], b[0]))
            bm.faces.new((a[1], a[2], b[2], b[1]))
        mesh = bpy.data.meshes.new(f"Leaf_{i:02d}")
        bm.to_mesh(mesh)
        bm.free()
        mesh.materials.append(leaf_mat)
        leaf = fk.link(bpy.data.objects.new(f"Leaf_{i:02d}", mesh), coll)
        fk.smooth(leaf, 180)
        solid = leaf.modifiers.new("Solidify", "SOLIDIFY")
        solid.thickness = 0.0012
        sub = leaf.modifiers.new("Subdivision", "SUBSURF")
        sub.levels = sub.render_levels = 2
        leaf.location = (px, py, DESK_Z + 0.10 + 0.012 * i)
        leaf.rotation_euler = (tilt, 0, ang)

    covers = [(0.50, 0.10, 0.07), (0.10, 0.22, 0.34), (0.80, 0.62, 0.22), (0.14, 0.30, 0.20), (0.62, 0.30, 0.16),
              (0.28, 0.10, 0.22), (0.75, 0.72, 0.65)]
    paper = fk.material("M_Paper", (0.82, 0.79, 0.70), rough=0.9)
    z = DESK_Z
    for i, (wd, dp, th) in enumerate(((0.23, 0.16, 0.028), (0.21, 0.15, 0.022), (0.19, 0.135, 0.034))):
        cover = fk.add_surface_noise(fk.material(f"M_Book_{i}", covers[i], rough=0.62, sheen_weight=0.3), scale=400,
                                     bump=0.2, color_var=0.05)
        rot = (0, 0, math.radians(rng.uniform(-9, 9)))
        fk.box(f"Book_{i}", (wd, dp, th), (0.50, DESK_Y - 0.13, z + th / 2), bevel_width=0.0018, mat=cover, coll=coll, rot=rot)
        fk.box(f"Book_{i}_Pages", (wd - 0.004, dp - 0.006, th - 0.006), (0.503, DESK_Y - 0.133, z + th / 2), mat=paper,
               coll=coll, rot=rot)
        z += th
    x = -0.15
    for i in range(9):
        th, ht, dp = rng.uniform(0.018, 0.04), rng.uniform(0.17, 0.235), rng.uniform(0.12, 0.15)
        cover = fk.add_surface_noise(fk.material(f"M_ShelfBook_{i}", covers[i % len(covers)], rough=0.6, sheen_weight=0.3),
                                     scale=400, bump=0.2, color_var=0.05)
        lean = math.radians(-11) if i == 8 else 0.0
        fk.box(f"ShelfBook_{i}", (th, dp, ht), (x + th / 2 + (0.02 if i == 8 else 0), 1.90, 1.534 + ht / 2),
               bevel_width=0.0015, mat=cover, coll=coll, rot=(0, lean, 0))
        x += th + 0.002
    fk.lathe("Vase", [(0.0, 0.0), (0.03, 0.0), (0.045, 0.05), (0.04, 0.11), (0.018, 0.15), (0.022, 0.17)],
             loc=(0.62, 1.90, 1.534), coll=coll, thickness=0.003, subsurf=1,
             mat=fk.material("M_Vase", (0.10, 0.20, 0.26), rough=0.18, coat_weight=1.0, coat_roughness=0.05))

    frame_wood = fk.wood("M_Frame", dark=(0.05, 0.03, 0.02), light=(0.14, 0.08, 0.045), grain_scale=14, stretch=10, axis="Z")
    fx, fz, fw, fh = -0.62, 1.42, 0.36, 0.46
    fk.box("Frame", (fw, 0.022, fh), (fx, 1.985, fz), bevel_width=0.004, mat=frame_wood, coll=coll)
    fk.box("Frame_Mat", (fw - 0.04, 0.004, fh - 0.04), (fx, 1.973, fz), coll=coll,
           mat=fk.material("M_Passepartout", (0.88, 0.86, 0.80), rough=0.9))
    art = fk.material("M_Art", (0.9, 0.9, 0.9), rough=0.75)
    tree = art.node_tree
    grad = tree.nodes.new("ShaderNodeTexGradient")
    grad.gradient_type = "SPHERICAL"
    coords = tree.nodes.new("ShaderNodeTexCoord")
    mapping = tree.nodes.new("ShaderNodeMapping")
    mapping.inputs["Location"].default_value = (0.0, 0.0, -0.12)
    mapping.inputs["Scale"].default_value = (5.2, 5.2, 5.2)
    ramp = tree.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.interpolation = "CONSTANT"
    ramp.color_ramp.elements[0].color = (0.83, 0.78, 0.66, 1)
    ramp.color_ramp.elements[1].position, ramp.color_ramp.elements[1].color = 0.42, (0.10, 0.22, 0.30, 1)
    tree.links.new(coords.outputs["Object"], mapping.inputs["Vector"])
    tree.links.new(mapping.outputs["Vector"], grad.inputs["Vector"])
    tree.links.new(grad.outputs["Fac"], ramp.inputs["Fac"])
    tree.links.new(ramp.outputs["Color"], fk.principled(art).inputs["Base Color"])
    fk.box("Frame_Art", (fw - 0.12, 0.002, fh - 0.12), (fx, 1.9705, fz), mat=art, coll=coll)


def build_pip(coll):
    """Pip: the original test character (a small lantern-shaped robot)."""
    body_mat = fk.add_surface_noise(fk.material("M_PipBody", (0.03, 0.36, 0.40), rough=0.34, coat_weight=0.7,
                                                coat_roughness=0.12), scale=80, bump=0.06, color_var=0.05)
    dark = fk.material("M_PipDark", (0.012, 0.012, 0.014), rough=0.12, coat_weight=1.0)
    root = fk.empty("Pip", (0.27, DESK_Y - 0.20, DESK_Z), coll)
    root.scale = (1.35, 1.35, 1.35)
    squash = fk.empty("Pip_Squash", (0, 0, 0), coll)
    fk.parent(squash, root)
    body = fk.lathe("Pip_Body", [(0.0, 0.006), (0.026, 0.006), (0.036, 0.016), (0.038, 0.045), (0.032, 0.068), (0.018, 0.08), (0.0, 0.083)],
                    loc=(0, 0, 0), mat=body_mat, coll=coll, subsurf=2)
    fk.parent(body, squash)
    for sx in (-1, 1):
        fk.parent(fk.sphere(f"Pip_Eye_{sx}", 0.0075, (sx * 0.013, -0.0325, 0.05), segments=24, mat=dark, coll=coll,
                            scale=(1, 0.55, 1.25)), squash)
        fk.parent(fk.sphere(f"Pip_Foot_{sx}", 0.011, (sx * 0.017, -0.004, 0.006), segments=24, mat=dark, coll=coll,
                            scale=(1, 1.35, 0.6)), root)
    fk.parent(fk.cylinder("Pip_Antenna", 0.0016, 0.03, (0, 0, 0.096), verts=12, mat=dark, coll=coll), squash)
    tip = fk.sphere("Pip_Tip", 0.0055, (0, 0, 0.114), segments=20, coll=coll,
                    mat=fk.emission("M_PipTip", (1.0, 0.72, 0.25), 9.0))
    fk.parent(tip, squash)
    return root, squash


def build_lights(coll, mood="golden"):
    """Light groups: sun, sky, lamp, screen, fill. Levels are set for the golden-hour look;
    night and blue-hour looks come from the same groups (see shots.py and relight)."""
    fk.world_sky(elevation=9.0, azimuth=258.0, strength=0.26, group="sky")
    fk.sun("Sun", elevation=14.0, azimuth=250.0, strength=7.0, angle=1.4, temperature=3400, group="sun", coll=coll)
    # A large, dim card behind the camera stands in for light bounced off the unseen half of the room.
    fk.area("Fill", (1.2, -1.9, 1.9), (0, 1.4, 0.9), size=(2.4, 1.6), power=12.0, temperature=5600, group="fill", coll=coll)


def build(screen_image):
    sc = fk.reset(fps=24, res=(1920, 1080), name="Proof")
    set_coll, props, hero = fk.collection("Set"), fk.collection("Props"), fk.collection("Hero")
    build_room(set_coll)
    build_desk(set_coll)
    build_laptop(props, screen_image)
    build_lamp(props)
    build_props(props)
    build_pip(hero)
    build_lights(fk.collection("Lights"))
    fk.cycles(samples=128, threshold=0.03)
    fk.color("AgX", "AgX - Medium High Contrast", exposure=0.35)
    return sc


if __name__ == "__main__":
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = args[args.index("--out") + 1] if "--out" in args else "/opt/film-studio/work/proof"
    os.makedirs(out, exist_ok=True)
    placeholder = os.path.join(out, "screen_placeholder.png")
    if not os.path.exists(placeholder):
        image = bpy.data.images.new("placeholder", 1920, 1200)
        image.generated_color = (0.07, 0.09, 0.14, 1.0)
        image.filepath_raw, image.file_format = placeholder, "PNG"
        image.save()
    screen = args[args.index("--screen") + 1] if "--screen" in args else placeholder
    sc = build(screen)
    cam = fk.camera("Cam_Wide", (0.62, -0.30, 1.10), (0.02, DESK_Y, DESK_Z + 0.13), lens=40, fstop=2.8,
                    focus=bpy.data.objects["Laptop_Screen"])
    sc.camera = cam
    fk.save(os.path.join(out, "proof.blend"))
    if "--still" in args:
        sc.render.resolution_percentage = 50
        seconds = fk.render_still(os.path.join(out, "look_still"))
        print(f"STILL seconds={seconds:.1f}")
