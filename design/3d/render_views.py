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
for v in views:
    if v == "cutaway":
        # hide roof, ceiling and tower for the axonometric cutaway
        for ob in bpy.data.objects:
            if ob.name.startswith(("roof", "ceiling", "tower", "can_roof", "can_soffit", "perg_slat")):
                ob.hide_render = True
    sc.camera = cams[v]
    sc.render.filepath = f"{out}/{v}_{mode}.png"
    t = time.time()
    bpy.ops.render.render(write_still=True)
    print(f"RENDERED {v} {mode} in {time.time() - t:.1f}s -> {sc.render.filepath}")
    if v == "cutaway":
        for ob in bpy.data.objects:
            ob.hide_render = False
if "--save" in argv:
    bpy.ops.wm.save_as_mainfile(filepath=arg("--save", f"{B.ROOT}/design/3d/drive_thru.blend"))
