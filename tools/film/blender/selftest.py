"""Smoke test for filmkit on the installed Blender: every helper is called once at a tiny size.

    blender -b --factory-startup --python tools/film/blender/selftest.py

Prints one line per check and "FILMKIT SELFTEST: PASS" or "FAIL". Takes a few seconds.
"""
import math
import os
import sys
import tempfile
import traceback

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import filmkit as fk  # noqa: E402

results = []


def check(name, fn):
    try:
        detail = fn()
        results.append(True)
        print(f"ok    {name}" + (f": {detail}" if detail else ""))
    except Exception:
        results.append(False)
        print(f"FAIL  {name}\n{traceback.format_exc()}")


tmp = tempfile.mkdtemp(prefix="filmkit_")
sc = fk.reset(fps=24, res=(64, 36))
check("frame numbers", lambda: (fk.frame(0), fk.frame(1.0), fk.frame(2.5)) == (1, 25, 61) or 1 / 0)
check("cycles + colour", lambda: (fk.cycles(samples=2, threshold=0.5), fk.color("AgX", "AgX - Medium High Contrast", 0.2)) and None)
coll = fk.collection("Test")
wood = fk.wood("M_Wood")
check("geometry", lambda: [fk.box("Box", (1, 1, 0.1), (0, 0, -0.05), bevel_width=0.01, mat=wood, coll=coll),
                           fk.cylinder("Cyl", 0.1, 0.3, (0.3, 0, 0.15), bevel_width=0.005, coll=coll),
                           fk.sphere("Sph", 0.1, (-0.3, 0, 0.1), coll=coll),
                           fk.lathe("Lathe", [(0, 0), (0.08, 0), (0.1, 0.15), (0.09, 0.16)], loc=(0, 0.3, 0), thickness=0.004, subsurf=1, coll=coll),
                           fk.rod("Rod", (0, 0, 0), (0.2, 0.2, 0.4), 0.01, coll=coll),
                           fk.torus_arc("Arc", 0.05, 0.01, -90, 90, loc=(0.1, 0.3, 0.08), coll=coll)] and f"{len(bpy.data.objects)} objects")
check("materials", lambda: [fk.add_surface_noise(fk.material("M_A", (0.5, 0.2, 0.1), rough=0.4, coat_weight=0.5)),
                            fk.emission("M_E", (1, 0.8, 0.6), 5), fk.glass("M_G", thin=True)] and None)
font = os.path.join(fk.FONTS, "Fraunces", "Fraunces-400.ttf")
check("text with a font file", lambda: fk.text("Title", "Hello", font if os.path.exists(font) else None, size=0.1, loc=(0, 0, 0.3),
                                               rot=(math.radians(90), 0, 0), mat=bpy.data.materials["M_E"], coll=coll).data.font.name)
check("lights in groups", lambda: [fk.area("Key", (1, -1, 1.5), (0, 0, 0), size=(1, 0.5), power=60, temperature=4500, group="key"),
                                   fk.spot("Spot", (0, -1, 1), (0, 0, 0), group="key"), fk.point("Point", (0.5, 0, 0.5), group="prac"),
                                   fk.sun("Sun", 20, 240, group="sun")] and [g.name for g in bpy.context.view_layer.lightgroups])
check("sky world", lambda: fk.world_sky(15, 240, 0.3, group="sky").lightgroup)
hdri = "/opt/blender-dl/current/5.2/datafiles/studiolights/world/sunset.exr"
check("hdri world", lambda: fk.world_hdri(hdri, 0.5, 30, group="sky").name if os.path.exists(hdri) else "skipped (no bundled HDRI)")
check("flat world", lambda: fk.world_color((0.02, 0.03, 0.05), 1.0, group="sky").name)
screen = fk.plane("Screen", (0.32, 0.2), (0, 0.2, 0.25), rot=(math.radians(90), 0, 0), coll=coll)
image = bpy.data.images.new("ui", 16, 10)
image.filepath_raw, image.file_format = os.path.join(tmp, "ui_0001.png"), "PNG"
image.save()
check("screen material", lambda: screen.data.materials.append(fk.screen_material("M_Screen", image.filepath_raw, strength=2.0)))
cam_a = fk.camera("CamA", (0, -2, 0.6), (0, 0, 0.1), lens=35, fstop=2.8, focus=screen)
cam_b = fk.camera("CamB", (1, -1.5, 0.5), (0, 0, 0.1), lens=85, fstop=2.0)
check("camera cuts", lambda: (fk.cut_to(cam_a, 0.0), fk.cut_to(cam_b, 1.0)) and [m.frame for m in sc.timeline_markers])


def keys():
    fk.key(cam_a, "location", 0.0, (0, -2, 0.6), interp="BEZIER")
    fk.key(cam_a, "location", 1.0, (0, -1.6, 0.6), interp="CUBIC", easing="EASE_OUT")
    fk.key(cam_a.data, "lens", 0.0, 35.0)
    fk.key(cam_a.data, "lens", 1.0, 40.0)
    fk.bake(bpy.data.objects["Sph"], "location", lambda t: 0.1 + fk.hop(t, 0.2, 0.5, 0.1)[0], 0.0, 1.0, index=2)
    curves = fk.fcurves(cam_a)
    assert len(curves) == 3 and curves[0].keyframe_points[1].interpolation == "CUBIC", curves
    assert len(fk.fcurves(cam_a.data)) == 1 and len(fk.fcurves(bpy.data.objects["Sph"])) == 1
    return f"{len(curves)} location curves, {len(fk.fcurves(bpy.data.objects['Sph'])[0].keyframe_points)} baked keys"


check("keyframes, easing, bake", keys)
# Downloaded assets are optional: tested only when tools/film/assets.py has fetched something.
import glob  # noqa: E402
for kind, call in (("textures", lambda ref: fk.pbr_material("M_Asset", ref).name),
                   ("models", lambda ref: fk.import_model(ref, loc=(0.4, 0.4, 0), coll=coll).name),
                   ("hdris", lambda ref: fk.world_hdri(ref, 0.5, group="sky").name)):
    found = sorted(glob.glob(f"/opt/film-studio/assets/{kind}/*/asset.json"))
    if found:
        check(f"downloaded asset ({kind})", lambda call=call, ref=os.path.dirname(found[0]): call(ref))
    else:
        print(f"skip  downloaded asset ({kind}): none fetched")
fk.set_range(2.0)
check("still (PNG) with camera cut", lambda: f"{fk.render_still(os.path.join(tmp, 'still'), frame_number=30):.1f} s, camera {sc.camera.name}")
check("still file exists", lambda: os.path.getsize(os.path.join(tmp, "still.png")))
check("plate (EXR, light groups, tracked quad)", lambda: f"{fk.render_plate(os.path.join(tmp, 'plate'), samples=2, threshold=0.5, track=['Screen']):.1f} s")
check("plate metadata", lambda: sorted(__import__("json").load(open(os.path.join(tmp, "plate.json")))["quads"]["Screen"]))
check("region plate", lambda: f"{fk.render_plate(os.path.join(tmp, 'region'), samples=2, threshold=0.5, region=(0.3, 0.3, 0.7, 0.7)):.1f} s")
check("save", lambda: fk.save(os.path.join(tmp, "test.blend")) or os.path.getsize(os.path.join(tmp, "test.blend")))
print(f"work folder: {tmp}")
print("FILMKIT SELFTEST: " + ("PASS" if all(results) else f"FAIL ({results.count(False)} of {len(results)})"))
sys.exit(0 if all(results) else 1)
