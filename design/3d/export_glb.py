"""
Exports a web-friendly GLB of the prototype (site + building + signage + cars) for the interactive viewer.

Procedural Cycles shaders don't survive glTF export, so materials are replaced by flat PBR equivalents;
vegetation becomes low-poly proxies; terrain, lights and highway far-side scenery are dropped.

  blender -b -P design/3d/export_glb.py -- --out report/site/assets/drive_thru.glb
"""
import bpy
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_scene as B  # noqa: E402

argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
out = argv[argv.index("--out") + 1] if "--out" in argv else f"{B.ROOT}/report/site/assets/drive_thru.glb"
os.makedirs(os.path.dirname(out), exist_ok=True)

B.build("day", "preview")

# drop heavy / non-exportable content
drop = [ob.name for ob in bpy.data.objects if ob.type in ("LIGHT", "CAMERA") or ob.name == "terrain" or
        ob.name.startswith(("far_tree", "wind_", "steppe_grass", "grass_", "shrub_", "tree_"))]
for n in drop:
    bpy.data.objects.remove(bpy.data.objects[n], do_unlink=True)
# drop furniture instances and any template objects not linked to the scene, then purge orphans
for n in [ob.name for ob in bpy.data.objects if ob.type == "EMPTY" and ob.instance_collection is not None]:
    bpy.data.objects.remove(bpy.data.objects[n], do_unlink=True)
scene_objs = set(o.name for o in bpy.context.scene.objects)
for n in [ob.name for ob in bpy.data.objects if ob.name not in scene_objs]:
    bpy.data.objects.remove(bpy.data.objects[n], do_unlink=True)
for c in list(bpy.data.collections):
    if c.name not in [x.name for x in bpy.context.scene.collection.children_recursive]:
        bpy.data.collections.remove(c)
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
# drop everything far from the site (landscape module: fields, villages, poplars; distant mountains)
from mathutils import Vector as _V
far_objs = []
for ob in bpy.data.objects:
    if ob.type not in ("MESH", "EMPTY", "CURVE"):
        continue
    if ob.name.startswith(("hwy_", "median", "verge", "edge_", "inner_", "lanes_", "aux_")):
        continue
    if ob.parent is not None:
        continue
    if ob.type == "MESH" and len(ob.data.vertices):
        c = sum((ob.matrix_world @ _V(b) for b in ob.bound_box), _V()) / 8.0
        ext = max((ob.matrix_world @ _V(b) - c).length for b in ob.bound_box)
    else:
        c, ext = ob.matrix_world.translation, 0.0
    if (abs(c.x - 37) > 150 or abs(c.y - 22) > 110) or ext > 400:
        far_objs.append(ob)
kill_far = set()
for ob in far_objs:
    kill_far.add(ob.name); kill_far.update(ch.name for ch in ob.children_recursive)
for n in kill_far:
    if n in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[n], do_unlink=True)
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
# trim highway to +-140 m
for ob in bpy.data.objects:
    if ob.type == "MESH" and ob.name.startswith(("hwy_", "median", "verge", "edge_", "inner_", "lanes_", "aux_")):
        for v in ob.data.vertices:
            v.co.x = max(-140.0, min(220.0, v.co.x))
# remove highway cars far away
far = [ob for ob in bpy.data.objects if ob.type == "EMPTY" and ob.name[:1] == "h" and ob.name[1:].isdigit() and abs(ob.location.x - 37) > 140]
kill = set()
for ob in far:
    kill.add(ob.name)
    kill.update(c.name for c in ob.children_recursive)
for n in kill:
    if n in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects[n], do_unlink=True)


def flat(name, rgb, rough=0.6, metal=0.0, alpha=1.0, emit=None):
    m = bpy.data.materials.new("glb_" + name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if alpha < 1:
        b.inputs["Alpha"].default_value = alpha
        m.blend_method = "BLEND"
    if emit:
        b.inputs["Emission Color"].default_value = (*emit, 1)
        b.inputs["Emission Strength"].default_value = 1.0
    return m


MAP = {
    "tuff": flat("tuff", (0.63, 0.38, 0.27), 0.9), "tuff_dark": flat("tuff_dark", (0.42, 0.22, 0.17), 0.9),
    "asphalt_site": flat("asphalt", (0.09, 0.09, 0.09), 0.9), "asphalt_hwy": flat("asphalt_hwy", (0.07, 0.07, 0.075), 0.9),
    "kerb_concrete": flat("kerb", (0.55, 0.54, 0.52), 0.8), "concrete": flat("concrete", (0.5, 0.49, 0.47), 0.8),
    "grass_irrigated": flat("grass", (0.13, 0.2, 0.06), 0.95), "steppe_proc": flat("steppe", (0.2, 0.18, 0.08), 0.95),
    "oak_soffit": flat("oak", (0.42, 0.24, 0.12), 0.6), "basalt_pavers": flat("pavers", (0.07, 0.07, 0.075), 0.8),
    "bronze": flat("bronze", (0.105, 0.072, 0.048), 0.35, 1.0), "bronze_matte": flat("bronze_m", (0.09, 0.065, 0.045), 0.55, 0.8),
    "glass": flat("glass", (0.6, 0.75, 0.8), 0.05, 0.0, alpha=0.35), "roof_membrane": flat("membrane", (0.12, 0.12, 0.12), 0.7),
    "barrier_concrete": flat("barrier", (0.6, 0.6, 0.58), 0.8), "soil": flat("soil", (0.12, 0.08, 0.05), 0.9),
    "marking_white": flat("white", (0.8, 0.8, 0.78), 0.6), "marking_blue": flat("blue", (0.05, 0.2, 0.6), 0.6),
    "marking_green": flat("green", (0.05, 0.35, 0.15), 0.6), "plaster_white": flat("plaster", (0.8, 0.78, 0.74), 0.8),
    "led_warm": flat("led", (1.0, 0.8, 0.55), 0.4, emit=(1.0, 0.8, 0.55)),
}
for ob in bpy.data.objects:
    if ob.type != "MESH":
        continue
    for slot in ob.material_slots:
        m = slot.material
        if m and m.name in MAP:
            slot.material = MAP[m.name]

# low-poly tree proxies at layout tree positions
leaf = flat("leaf", (0.16, 0.26, 0.08), 0.9)
trunk = flat("trunk", (0.18, 0.12, 0.08), 0.9)
for i, t in enumerate(B.L["trees"]):
    s = t["s"] * (0.8 if t["kind"] == "tree_small" else 1.0)
    bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.12 * s, depth=2.4 * s, location=(t["x"], t["y"], 1.2 * s))
    bpy.context.active_object.data.materials.append(trunk)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=2.0 * s, location=(t["x"], t["y"], 3.6 * s))
    o = bpy.context.active_object
    o.scale = (1, 1, 0.8)
    o.data.materials.append(leaf)

# lighten car meshes for the web
heavy = [ob for ob in bpy.data.objects if ob.type == "MESH" and len(ob.data.vertices) > 2500 and not ob.name.startswith(("inner", "edge", "lanes", "aux", "hwy"))]
for ob in heavy:
    ob.data = ob.data.copy()
    m = ob.modifiers.new("dec", "DECIMATE"); m.ratio = 0.2
dg = bpy.context.evaluated_depsgraph_get()
for ob in heavy:
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg))
    ob.modifiers.clear()
    ob.data = me
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
# Blender Z-up -> glTF Y-up handled by exporter; centre the scene near the building
bpy.ops.export_scene.gltf(filepath=out, export_format="GLB", export_apply=True, export_yup=True,
                          export_texcoords=True, export_normals=True, export_materials="EXPORT", export_cameras=False,
                          export_lights=False, use_selection=False, export_image_format="AUTO")
print("GLB", out, os.path.getsize(out) / 1e6, "MB")
import collections as _c
tot = _c.Counter()
for o in bpy.data.objects:
    if o.type == "MESH":
        tot[o.name.split("_")[0]] += len(o.data.vertices)
print("BYPREFIX", tot.most_common(15))
