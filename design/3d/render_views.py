"""
Render named camera views of the drive-thru prototype.

  blender -b -P design/3d/render_views.py -- --mode day --views hero,aerial --samples 128 --pct 100 --out renders/
"""
import bpy
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_scene as B  # noqa: E402

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []


def arg(k, d):
    return argv[argv.index(k) + 1] if k in argv else d


mode = arg("--mode", "day")
views = arg("--views", "hero").split(",")
samples = int(arg("--samples", "64"))
pct = int(arg("--pct", "50"))
out = arg("--out", f"{B.ROOT}/design/renders")
quality = arg("--quality", "final" if pct >= 100 else "preview")
w, h = (int(v) for v in arg("--res", "1920x1080").split("x"))
os.makedirs(out, exist_ok=True)

cams = B.build(mode, quality)
B.render_settings(samples=samples, res=(w, h), pct=pct)
if "--cutaway" in argv or "cutaway" in views:
    pass
sc = bpy.context.scene
import json as _json
from bpy_extras.object_utils import world_to_camera_view


def clay_cutaway():
    """White clay model + colour-coded functional zones; returns label anchors."""
    clay = B.principled("clay", (0.78, 0.77, 0.74), rough=0.9)
    clay_dark = B.principled("clay_dark", (0.42, 0.42, 0.41), rough=0.9)
    keep = {"glass", "glass_dark"}
    for ob in bpy.data.objects:
        if ob.name.startswith(("roof", "ceiling", "tower", "can_roof", "can_soffit", "perg_slat", "pv_", "pendant", "fascia_word", "roof_led")):
            ob.hide_render = True
        if ob.type == "MESH" and not ob.name.startswith(("terrain",)):
            for slot in ob.material_slots:
                if slot.material and slot.material.name not in keep:
                    slot.material = clay_dark if ob.name.startswith(("site_asphalt", "hwy_", "decel", "accel", "entry_drive", "exit_drive")) else clay
    cut = B.L["building"]["ffl"] + 1.4
    for ob in bpy.data.objects:
        if ob.type == "MESH" and ob.name.startswith(("tuff_", "int_wall", "cwglass", "glass_", "coping", "svc_", "clere", "cw_", "gl_", "clm_",
                                                     "door_", "cafe_backwall", "bar_backsplash", "col_", "int_menu", "int_logo")):
            for vtx in ob.data.vertices:
                vtx.co.z = min(vtx.co.z, cut)
            if ob.name.startswith(("clere", "coping", "int_menu", "int_logo", "svc_sign")):
                ob.hide_render = True
    bpy.context.scene.world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.6
    zone_cols = {"R1": (0.03, 0.2, 0.22), "R2": (0.25, 0.25, 0.27), "R3": (0.85, 0.38, 0.1), "R4": (0.25, 0.45, 0.7),
                 "R5": (0.45, 0.45, 0.47), "R6": (0.45, 0.45, 0.47)}
    b = B.L["building"]
    anchors = []
    for r in b["rooms"]:
        m = B.principled(f"zone_{r['id']}", zone_cols.get(r["id"], (0.6, 0.6, 0.6)), rough=0.7)
        B.box(f"zone_{r['id']}", r["x0"] + 0.06, r["y0"] + 0.06, b["ffl"] + 0.011, r["x1"] - 0.06, r["y1"] - 0.06, b["ffl"] + 0.02, m, "interior")
        anchors.append((r["id"], r["name"].split(" (")[0], ((r["x0"] + r["x1"]) / 2, (r["y0"] + r["y1"]) / 2, b["ffl"] + 0.05)))
    eqm = B.principled("eq_clay", (0.95, 0.95, 0.93), rough=0.5)
    for ob in bpy.data.objects:
        if ob.name.startswith(("eq_", "bar_counter", "cafe_counter")):
            for slot in ob.material_slots:
                slot.material = eqm
    anchors += [("W1", "Window 1 · pay", (39.6, 34.0, 1.2)), ("W2", "Window 2 · hand-off", (31.4, 34.0, 1.2)),
                ("T", "Terrace", (19.7, 24.6, 0.3)), ("OP", "Order points", (60.0, 24.0, 0.3)), ("P", "Parking", (30.0, 12.0, 0.1))]
    return anchors


for v in views:
    anchors = None
    if v == "cutaway":
        anchors = clay_cutaway()
    sc.camera = cams[v]
    sc.render.filepath = f"{out}/{v}_{mode}.png"
    t = time.time()
    bpy.ops.render.render(write_still=True)
    print(f"RENDERED {v} {mode} in {time.time() - t:.1f}s -> {sc.render.filepath}")
    if anchors:
        pts = []
        for aid, name, p in anchors:
            co = world_to_camera_view(sc, sc.camera, __import__("mathutils").Vector(p))
            pts.append({"id": aid, "name": name, "x": co.x, "y": 1 - co.y})
        _json.dump(pts, open(sc.render.filepath.replace(".png", "_labels.json"), "w"), indent=1)
    if v == "cutaway":
        for ob in bpy.data.objects:
            ob.hide_render = False
if "--save" in argv:
    bpy.ops.wm.save_as_mainfile(filepath=arg("--save", f"{B.ROOT}/design/3d/drive_thru.blend"))
