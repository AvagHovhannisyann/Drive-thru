"""
Blender scene builder for the drive-thru prototype.

Reads design/layout.json (geometry, single source of truth) and brand/out/brand.json
(colours, wordmarks, signage textures) and constructs a full Cycles scene: terrain,
highway with auxiliary lanes, site paving and kerbs, landscaping, the building (tuff
volumes, glazed café lantern, sloped oak-soffit roof, brand tower), drive-thru canopy and
menu boards, furniture, lighting, procedural vehicles and cameras.

Usage (headless):
  blender -b -P design/3d/build_scene.py -- --mode day --save design/3d/drive_thru.blend
  (render_views.py imports this module and renders named cameras)
"""
import bpy
import bmesh
import json
import math
import os
import glob
import random
import sys
from mathutils import Vector, Euler, noise

ROOT = "/home/user/Drive-thru"
A = f"{ROOT}/design/3d/assets"
L = json.load(open(f"{ROOT}/design/layout.json"))
BRAND_JSON = f"{ROOT}/brand/out/brand.json"
BRAND = json.load(open(BRAND_JSON)) if os.path.exists(BRAND_JSON) else {}

random.seed(7)


def hexrgb(h, default=(0.5, 0.5, 0.5)):
    if not h:
        return default
    h = h.lstrip("#")
    srgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in srgb]
    return tuple(lin)


COL = {k: hexrgb(v) for k, v in BRAND.get("colors", {}).items()}
C_PRIMARY = COL.get("primary", hexrgb("#1F3B2D"))
C_ACCENT = COL.get("accent", hexrgb("#E8873A"))
C_LIGHT = COL.get("light", hexrgb("#F4EDE2"))


# ======================================================================================
# helpers
# ======================================================================================
def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)
    return sc


COLLS = {}


def coll(name):
    if name not in COLLS:
        c = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(c)
        COLLS[name] = c
    return COLLS[name]


def link(ob, cname):
    coll(cname).objects.link(ob)
    return ob


def mesh_obj(name, verts, faces, mats, cname, smooth_angle=None, mat_idx=None):
    me = bpy.data.meshes.new(name)
    me.from_pydata([tuple(v) for v in verts], [], [tuple(f) for f in faces])
    me.update()
    for m in (mats if isinstance(mats, (list, tuple)) else [mats]):
        me.materials.append(m)
    if mat_idx:
        for i, p in enumerate(me.polygons):
            p.material_index = mat_idx[i]
    if smooth_angle is not None:
        for p in me.polygons:
            p.use_smooth = True
        try:
            me.set_sharp_from_angle(angle=math.radians(smooth_angle))
        except Exception:
            pass
    ob = bpy.data.objects.new(name, me)
    return link(ob, cname)


def box(name, x0, y0, z0, x1, y1, z1, mat, cname="building", bevel=0.0, mats_by_face=None):
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    z0, z1 = min(z0, z1), max(z0, z1)
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
         (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    f = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    mats = [mat] if mats_by_face is None else mats_by_face[0]
    idx = None if mats_by_face is None else mats_by_face[1]
    ob = mesh_obj(name, v, f, mats, cname, mat_idx=idx)
    if bevel > 0:
        m = ob.modifiers.new("bev", "BEVEL")
        m.width = bevel
        m.segments = 2
        m.limit_method = "ANGLE"
    return ob


def poly_area_sign(poly):
    s = 0.0
    for i in range(len(poly)):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % len(poly)]
        s += x0 * y1 - x1 * y0
    return s


def prism(name, poly, z0, z1, mat_side, mat_top=None, cname="site"):
    """Extrude a 2D polygon between z0 and z1 (top face material separate)."""
    poly = list(poly)
    if poly_area_sign(poly) < 0:
        poly = poly[::-1]
    n = len(poly)
    verts = [(x, y, z0) for x, y in poly] + [(x, y, z1) for x, y in poly]
    faces = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))]
    idx = [0, 1]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, n + j, n + i))
        idx.append(0)
    mats = [mat_side, mat_top or mat_side]
    return mesh_obj(name, verts, faces, mats, cname, mat_idx=idx)


def offset_poly(poly, d):
    """Naive inward offset for convex-ish polygons (miter)."""
    poly = list(poly)
    if poly_area_sign(poly) < 0:
        poly = poly[::-1]
    n = len(poly)
    out = []
    for i in range(n):
        p0 = Vector(poly[i - 1]); p1 = Vector(poly[i]); p2 = Vector(poly[(i + 1) % n])
        e0 = (p1 - p0).normalized(); e1 = (p2 - p1).normalized()
        n0 = Vector((-e0.y, e0.x)); n1 = Vector((-e1.y, e1.x))
        bis = (n0 + n1)
        if bis.length < 1e-6:
            bis = n0
        bis.normalize()
        cosang = max(0.3, bis.dot(n1))
        q = p1 + bis * (d / cosang)
        out.append((q.x, q.y))
    return out


def strip(name, pts, width, z, mat, cname="markings", dash=None):
    """Flat ribbon along a polyline. dash=(on, off) creates dashed markings."""
    segs = []
    if dash:
        on, off = dash
        total = sum((Vector(pts[i + 1]) - Vector(pts[i])).length for i in range(len(pts) - 1))
        s = 0.0
        while s < total:
            segs.append((s, min(s + on, total)))
            s += on + off
    else:
        total = sum((Vector(pts[i + 1]) - Vector(pts[i])).length for i in range(len(pts) - 1))
        segs.append((0, total))

    def at(s):
        acc = 0
        for i in range(len(pts) - 1):
            a, b = Vector(pts[i]), Vector(pts[i + 1])
            l = (b - a).length
            if acc + l >= s or i == len(pts) - 2:
                t = 0 if l == 0 else (s - acc) / l
                return a + (b - a) * min(max(t, 0), 1), (b - a).normalized()
            acc += l

    verts, faces = [], []
    for s0, s1 in segs:
        n = max(2, int((s1 - s0) / 0.5) + 1)
        base = len(verts)
        for k in range(n):
            s = s0 + (s1 - s0) * k / (n - 1)
            p, d = at(s)
            nrm = Vector((-d.y, d.x)) * width / 2
            verts += [(p.x + nrm.x, p.y + nrm.y, z), (p.x - nrm.x, p.y - nrm.y, z)]
        for k in range(n - 1):
            a = base + 2 * k
            faces.append((a, a + 1, a + 3, a + 2))
    return mesh_obj(name, verts, faces, [mat], cname)


def look_at(ob, target):
    d = Vector(target) - ob.location
    ob.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()


# ======================================================================================
# materials
# ======================================================================================
MATS = {}


def principled(name, color, rough=0.5, metal=0.0, coat=0.0, coat_rough=0.05, emission=None, estr=0.0,
               transmission=0.0, ior=1.45, alpha=1.0, spec=0.5):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    b.inputs["Coat Weight"].default_value = coat
    b.inputs["Coat Roughness"].default_value = coat_rough
    b.inputs["Transmission Weight"].default_value = transmission
    b.inputs["IOR"].default_value = ior
    b.inputs["Specular IOR Level"].default_value = spec
    b.inputs["Alpha"].default_value = alpha
    if emission is not None:
        b.inputs["Emission Color"].default_value = (*emission, 1)
        b.inputs["Emission Strength"].default_value = estr
    MATS[name] = m
    return m


def tex_node(nt, path, colorspace, proj="BOX", blend=0.25):
    it = nt.nodes.new("ShaderNodeTexImage")
    it.image = bpy.data.images.load(path, check_existing=True)
    it.image.colorspace_settings.name = colorspace
    it.projection = proj
    it.projection_blend = blend
    return it


def pbr(name, tex, size=2.0, tint=None, tint_fac=0.0, bright=1.0, bump=1.0, rough_add=0.0, rot_z=0.0, hue=0.5, sat=1.0):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    b = N["Principled BSDF"]
    tc = N.new("ShaderNodeTexCoord")
    mp = N.new("ShaderNodeMapping")
    mp.inputs["Scale"].default_value = (1 / size, 1 / size, 1 / size)
    mp.inputs["Rotation"].default_value = (0, 0, math.radians(rot_z))
    Lk.new(tc.outputs["Object"], mp.inputs["Vector"])

    def find(kind):
        fs = glob.glob(f"{A}/tex/{tex}/{tex}_{kind}.*")
        return fs[0] if fs else None

    d = find("Diffuse")
    if d:
        it = tex_node(nt, d, "sRGB")
        Lk.new(mp.outputs[0], it.inputs[0])
        hsv = N.new("ShaderNodeHueSaturation")
        hsv.inputs["Hue"].default_value = hue
        hsv.inputs["Saturation"].default_value = sat
        hsv.inputs["Value"].default_value = bright
        Lk.new(it.outputs[0], hsv.inputs["Color"])
        out = hsv.outputs[0]
        if tint is not None and tint_fac > 0:
            mix = N.new("ShaderNodeMix")
            mix.data_type = "RGBA"
            mix.blend_type = "MULTIPLY"
            mix.inputs[0].default_value = tint_fac
            Lk.new(out, mix.inputs[6])
            mix.inputs[7].default_value = (*tint, 1)
            out = mix.outputs[2]
        Lk.new(out, b.inputs["Base Color"])
    r = find("Rough")
    if r:
        it = tex_node(nt, r, "Non-Color")
        Lk.new(mp.outputs[0], it.inputs[0])
        if rough_add:
            ma = N.new("ShaderNodeMath"); ma.operation = "ADD"; ma.use_clamp = True
            ma.inputs[1].default_value = rough_add
            Lk.new(it.outputs[0], ma.inputs[0]); Lk.new(ma.outputs[0], b.inputs["Roughness"])
        else:
            Lk.new(it.outputs[0], b.inputs["Roughness"])
    n = find("nor_gl")
    if n and bump > 0:
        it = tex_node(nt, n, "Non-Color")
        Lk.new(mp.outputs[0], it.inputs[0])
        nm = N.new("ShaderNodeNormalMap")
        nm.inputs["Strength"].default_value = bump
        Lk.new(it.outputs[0], nm.inputs["Color"])
        Lk.new(nm.outputs[0], b.inputs["Normal"])
    MATS[name] = m
    return m


def wall_uv(nt):
    """Returns a vector socket with (u,v) for vertical walls: u along the wall, v = z."""
    N, Lk = nt.nodes, nt.links
    tc = N.new("ShaderNodeTexCoord")
    sep = N.new("ShaderNodeSeparateXYZ"); Lk.new(tc.outputs["Object"], sep.inputs[0])
    geo = N.new("ShaderNodeNewGeometry")
    sn = N.new("ShaderNodeSeparateXYZ"); Lk.new(geo.outputs["Normal"], sn.inputs[0])
    ax = N.new("ShaderNodeMath"); ax.operation = "ABSOLUTE"; Lk.new(sn.outputs[0], ax.inputs[0])
    ay = N.new("ShaderNodeMath"); ay.operation = "ABSOLUTE"; Lk.new(sn.outputs[1], ay.inputs[0])
    gt = N.new("ShaderNodeMath"); gt.operation = "GREATER_THAN"; Lk.new(ax.outputs[0], gt.inputs[0]); Lk.new(ay.outputs[0], gt.inputs[1])
    mx = N.new("ShaderNodeMix"); mx.data_type = "FLOAT"
    Lk.new(gt.outputs[0], mx.inputs[0]); Lk.new(sep.outputs[0], mx.inputs[2]); Lk.new(sep.outputs[1], mx.inputs[3])
    cmb = N.new("ShaderNodeCombineXYZ"); Lk.new(mx.outputs[0], cmb.inputs[0]); Lk.new(sep.outputs[2], cmb.inputs[1])
    return cmb.outputs[0]


def mat_tuff(name="tuff", c1=(0.62, 0.36, 0.27), c2=(0.70, 0.45, 0.32), brick_w=0.9, row_h=0.3):
    """Procedural Armenian tuff cladding: sawn slabs, warm apricot/rose variation, porous surface."""
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    b = N["Principled BSDF"]
    uv = wall_uv(nt)
    br = N.new("ShaderNodeTexBrick")
    br.offset = 0.5
    br.offset_frequency = 2
    br.inputs["Color1"].default_value = (*c1, 1)
    br.inputs["Color2"].default_value = (*c2, 1)
    br.inputs["Mortar"].default_value = (0.08, 0.05, 0.04, 1)
    br.inputs["Scale"].default_value = 1.0
    br.inputs["Mortar Size"].default_value = 0.006
    br.inputs["Mortar Smooth"].default_value = 0.1
    br.inputs["Bias"].default_value = 0.0
    br.inputs["Brick Width"].default_value = brick_w
    br.inputs["Row Height"].default_value = row_h
    Lk.new(uv, br.inputs["Vector"])
    # mottling
    tc = N.new("ShaderNodeTexCoord")
    nz = N.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 6.0; nz.inputs["Detail"].default_value = 8
    Lk.new(tc.outputs["Object"], nz.inputs["Vector"])
    ramp = N.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].position = 0.35; ramp.color_ramp.elements[0].color = (0.82, 0.78, 0.76, 1)
    ramp.color_ramp.elements[1].position = 0.75; ramp.color_ramp.elements[1].color = (1.08, 1.04, 1.0, 1)
    Lk.new(nz.outputs["Fac"], ramp.inputs[0])
    mul = N.new("ShaderNodeMix"); mul.data_type = "RGBA"; mul.blend_type = "MULTIPLY"; mul.inputs[0].default_value = 1.0
    Lk.new(br.outputs["Color"], mul.inputs[6]); Lk.new(ramp.outputs[0], mul.inputs[7])
    # pores
    vo = N.new("ShaderNodeTexVoronoi"); vo.inputs["Scale"].default_value = 160.0
    Lk.new(tc.outputs["Object"], vo.inputs["Vector"])
    pr = N.new("ShaderNodeMath"); pr.operation = "LESS_THAN"; pr.inputs[1].default_value = 0.12
    Lk.new(vo.outputs["Distance"], pr.inputs[0])
    pm = N.new("ShaderNodeMix"); pm.data_type = "RGBA"; pm.blend_type = "MULTIPLY"
    pf = N.new("ShaderNodeMath"); pf.operation = "MULTIPLY"; pf.inputs[1].default_value = 0.45
    Lk.new(pr.outputs[0], pf.inputs[0]); Lk.new(pf.outputs[0], pm.inputs[0])
    Lk.new(mul.outputs[2], pm.inputs[6]); pm.inputs[7].default_value = (0.35, 0.25, 0.2, 1)
    Lk.new(pm.outputs[2], b.inputs["Base Color"])
    b.inputs["Roughness"].default_value = 0.88
    # bump: recessed joints + pores + fine grain
    bump = N.new("ShaderNodeBump"); bump.inputs["Strength"].default_value = 0.35; bump.inputs["Distance"].default_value = 0.01
    hsum = N.new("ShaderNodeMath"); hsum.operation = "SUBTRACT"
    inv = N.new("ShaderNodeMath"); inv.operation = "SUBTRACT"; inv.inputs[0].default_value = 1.0
    Lk.new(br.outputs["Fac"], inv.inputs[1])
    Lk.new(inv.outputs[0], hsum.inputs[0]); Lk.new(pf.outputs[0], hsum.inputs[1])
    Lk.new(hsum.outputs[0], bump.inputs["Height"])
    Lk.new(bump.outputs[0], b.inputs["Normal"])
    MATS[name] = m
    return m


def mat_pavers(name="basalt_pavers", c=(0.055, 0.055, 0.058), w=0.6, h=0.3):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    b = N["Principled BSDF"]
    tc = N.new("ShaderNodeTexCoord")
    br = N.new("ShaderNodeTexBrick")
    br.offset = 0.5
    br.inputs["Color1"].default_value = (*c, 1)
    br.inputs["Color2"].default_value = (c[0] * 1.35, c[1] * 1.35, c[2] * 1.35, 1)
    br.inputs["Mortar"].default_value = (0.03, 0.03, 0.03, 1)
    br.inputs["Mortar Size"].default_value = 0.004
    br.inputs["Brick Width"].default_value = w
    br.inputs["Row Height"].default_value = h
    br.inputs["Scale"].default_value = 1.0
    Lk.new(tc.outputs["Object"], br.inputs["Vector"])
    nz = N.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 30
    Lk.new(tc.outputs["Object"], nz.inputs["Vector"])
    mx = N.new("ShaderNodeMix"); mx.data_type = "RGBA"; mx.blend_type = "OVERLAY"; mx.inputs[0].default_value = 0.25
    Lk.new(br.outputs["Color"], mx.inputs[6]); Lk.new(nz.outputs["Color"], mx.inputs[7])
    Lk.new(mx.outputs[2], b.inputs["Base Color"])
    rr = N.new("ShaderNodeMapRange"); rr.inputs[3].default_value = 0.55; rr.inputs[4].default_value = 0.8
    Lk.new(nz.outputs["Fac"], rr.inputs[0]); Lk.new(rr.outputs[0], b.inputs["Roughness"])
    bump = N.new("ShaderNodeBump"); bump.inputs["Strength"].default_value = 0.4
    inv = N.new("ShaderNodeMath"); inv.operation = "SUBTRACT"; inv.inputs[0].default_value = 1.0
    Lk.new(br.outputs["Fac"], inv.inputs[1]); Lk.new(inv.outputs[0], bump.inputs["Height"])
    Lk.new(bump.outputs[0], b.inputs["Normal"])
    MATS[name] = m
    return m


def mat_image(name, path, emit=0.0, rough=0.4, fallback=(0.1, 0.1, 0.1)):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = rough
    if path and os.path.exists(path):
        it = nt.nodes.new("ShaderNodeTexImage")
        it.image = bpy.data.images.load(path, check_existing=True)
        it.extension = "CLIP"
        nt.links.new(it.outputs["Color"], b.inputs["Base Color"])
        if emit > 0:
            nt.links.new(it.outputs["Color"], b.inputs["Emission Color"])
            b.inputs["Emission Strength"].default_value = emit
        if it.image.alpha_mode != "NONE" and path.endswith(".png"):
            nt.links.new(it.outputs["Alpha"], b.inputs["Alpha"])
    else:
        b.inputs["Base Color"].default_value = (*fallback, 1)
        if emit > 0:
            b.inputs["Emission Color"].default_value = (*fallback, 1)
            b.inputs["Emission Strength"].default_value = emit
    MATS[name] = m
    return m


def image_plane(name, path, cx, cy, cz, w, h, facing, emit=0.0, cname="signage", rough=0.4, offset=0.0):
    """Vertical image plane centred at (cx,cy,cz), facing 'N','S','E','W'."""
    m = mat_image(name + "_m", path, emit=emit, rough=rough)
    hw, hh = w / 2, h / 2
    if facing == "S":
        v = [(cx - hw, cy - offset, cz - hh), (cx + hw, cy - offset, cz - hh), (cx + hw, cy - offset, cz + hh), (cx - hw, cy - offset, cz + hh)]
    elif facing == "N":
        v = [(cx + hw, cy + offset, cz - hh), (cx - hw, cy + offset, cz - hh), (cx - hw, cy + offset, cz + hh), (cx + hw, cy + offset, cz + hh)]
    elif facing == "E":
        v = [(cx + offset, cy - hw, cz - hh), (cx + offset, cy + hw, cz - hh), (cx + offset, cy + hw, cz + hh), (cx + offset, cy - hw, cz + hh)]
    else:
        v = [(cx - offset, cy + hw, cz - hh), (cx - offset, cy - hw, cz - hh), (cx - offset, cy - hw, cz + hh), (cx - offset, cy + hw, cz + hh)]
    ob = mesh_obj(name, v, [(0, 1, 2, 3)], [m], cname)
    me = ob.data
    uvl = me.uv_layers.new(name="UVMap")
    for i, uvc in enumerate([(0, 0), (1, 0), (1, 1), (0, 1)]):
        uvl.data[i].uv = uvc
    # make image node use UV
    nt = m.node_tree
    for n in nt.nodes:
        if n.type == "TEX_IMAGE":
            uvn = nt.nodes.new("ShaderNodeUVMap")
            nt.links.new(uvn.outputs[0], n.inputs[0])
    return ob


def mat_steppe(name="steppe_proc"):
    """Kotayk/Gegharkunik highland steppe: olive meadow / dry golden grass / rock on slopes, with aerial haze."""
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    b = N["Principled BSDF"]
    tc = N.new("ShaderNodeTexCoord")
    tex = glob.glob(f"{A}/tex/aerial_grass_rock/aerial_grass_rock_Diffuse.*")[0]
    def img(scale):
        mp = N.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value = (1 / scale,) * 3
        Lk.new(tc.outputs["Object"], mp.inputs[0])
        it = tex_node(nt, tex, "sRGB", proj="FLAT"); Lk.new(mp.outputs[0], it.inputs[0])
        return it
    i1, i2 = img(13.0), img(97.0)
    nz = N.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 0.004; nz.inputs["Detail"].default_value = 6
    Lk.new(tc.outputs["Object"], nz.inputs[0])
    mx = N.new("ShaderNodeMix"); mx.data_type = "RGBA"; Lk.new(nz.outputs["Fac"], mx.inputs[0])
    Lk.new(i1.outputs[0], mx.inputs[6]); Lk.new(i2.outputs[0], mx.inputs[7])
    bw = N.new("ShaderNodeRGBToBW"); Lk.new(mx.outputs[2], bw.inputs[0])
    # large-scale vegetation zones
    nz2 = N.new("ShaderNodeTexNoise"); nz2.inputs["Scale"].default_value = 0.0025; nz2.inputs["Detail"].default_value = 4
    Lk.new(tc.outputs["Object"], nz2.inputs[0])
    ramp = N.new("ShaderNodeValToRGB")
    els = ramp.color_ramp.elements
    els[0].position = 0.38; els[0].color = (0.115, 0.135, 0.05, 1)     # olive meadow
    els[1].position = 0.62; els[1].color = (0.30, 0.235, 0.105, 1)     # dry golden grass
    e = els.new(0.5); e.color = (0.19, 0.18, 0.075, 1)
    Lk.new(nz2.outputs["Fac"], ramp.inputs[0])
    # slope -> rock
    geo = N.new("ShaderNodeNewGeometry"); sep = N.new("ShaderNodeSeparateXYZ"); Lk.new(geo.outputs["Normal"], sep.inputs[0])
    sl = N.new("ShaderNodeMapRange"); sl.inputs[1].default_value = 0.93; sl.inputs[2].default_value = 0.78
    Lk.new(sep.outputs[2], sl.inputs[0])
    rock = N.new("ShaderNodeMix"); rock.data_type = "RGBA"; Lk.new(sl.outputs[0], rock.inputs[0])
    Lk.new(ramp.outputs[0], rock.inputs[6]); rock.inputs[7].default_value = (0.22, 0.2, 0.18, 1)
    # modulate by texture luminance for detail
    det = N.new("ShaderNodeMapRange"); det.inputs[3].default_value = 0.55; det.inputs[4].default_value = 1.6
    Lk.new(bw.outputs[0], det.inputs[0])
    mul = N.new("ShaderNodeMix"); mul.data_type = "RGBA"; mul.blend_type = "MULTIPLY"; mul.inputs[0].default_value = 1.0
    Lk.new(rock.outputs[2], mul.inputs[6])
    cval = N.new("ShaderNodeCombineColor"); Lk.new(det.outputs[0], cval.inputs[0]); Lk.new(det.outputs[0], cval.inputs[1]); Lk.new(det.outputs[0], cval.inputs[2])
    Lk.new(cval.outputs[0], mul.inputs[7])
    # aerial perspective
    cam = N.new("ShaderNodeCameraData")
    hz = N.new("ShaderNodeMapRange"); hz.inputs[1].default_value = 250; hz.inputs[2].default_value = 4200
    hz.inputs[3].default_value = 0.0; hz.inputs[4].default_value = 0.78
    Lk.new(cam.outputs["View Distance"], hz.inputs[0])
    hm = N.new("ShaderNodeMix"); hm.data_type = "RGBA"; Lk.new(hz.outputs[0], hm.inputs[0])
    Lk.new(mul.outputs[2], hm.inputs[6]); hm.inputs[7].default_value = (0.45, 0.55, 0.68, 1)
    Lk.new(hm.outputs[2], b.inputs["Base Color"])
    em = N.new("ShaderNodeMath"); em.operation = "MULTIPLY"; em.inputs[1].default_value = HAZE_EMIT[0]
    Lk.new(hz.outputs[0], em.inputs[0])
    b.inputs["Emission Color"].default_value = (0.55, 0.66, 0.82, 1)
    Lk.new(em.outputs[0], b.inputs["Emission Strength"])
    b.inputs["Roughness"].default_value = 0.95
    MATS[name] = m
    return m


HAZE_EMIT = [0.35]


def set_haze(night):
    HAZE_EMIT[0] = 0.02 if night else 0.35


def init_materials():
    M = {}
    M["asphalt"] = pbr("asphalt_site", "asphalt_02", size=5.0, bright=0.82, bump=0.6)
    M["asphalt_hwy"] = pbr("asphalt_hwy", "worn_asphalt", size=6.0, bright=0.7, bump=0.5)
    M["kerb"] = pbr("kerb_concrete", "brushed_concrete", size=1.5, bright=1.15, bump=0.4)
    M["concrete"] = pbr("concrete", "concrete_floor_02", size=3.0, bright=1.05, bump=0.3)
    M["grass"] = pbr("grass_irrigated", "aerial_grass_rock", size=6.0, bright=0.75, hue=0.52, sat=1.15, bump=0.3)
    M["steppe"] = mat_steppe()
    M["gravel"] = pbr("gravel_mulch", "gravel", size=1.5, bright=0.6, bump=0.6)
    M["oak"] = pbr("oak_soffit", "oak_wood_planks", size=2.2, bright=1.05, rot_z=90, bump=0.3)
    M["tuff"] = mat_tuff()
    M["tuff_dark"] = mat_tuff("tuff_dark", c1=(0.42, 0.22, 0.17), c2=(0.48, 0.27, 0.2))
    M["pavers"] = mat_pavers()
    M["bronze"] = principled("bronze", (0.105, 0.072, 0.048), rough=0.32, metal=1.0)
    M["bronze_matte"] = principled("bronze_matte", (0.09, 0.065, 0.045), rough=0.55, metal=0.8)
    M["steel_dark"] = principled("steel_dark", (0.03, 0.03, 0.032), rough=0.45, metal=0.6)
    M["glass"] = principled("glass", (0.92, 0.96, 0.96), rough=0.0, transmission=1.0, ior=1.5)
    M["glass_dark"] = principled("glass_dark", (0.02, 0.025, 0.03), rough=0.05, metal=0.0, coat=1.0, spec=1.0)
    M["membrane"] = principled("roof_membrane", (0.12, 0.12, 0.12), rough=0.7)
    M["plaster"] = principled("plaster_white", (0.80, 0.78, 0.74), rough=0.8)
    M["floor_int"] = principled("polished_concrete", (0.35, 0.34, 0.33), rough=0.25)
    M["counter"] = principled("quartz_counter", (0.85, 0.84, 0.82), rough=0.2)
    M["paint_white"] = principled("marking_white", (0.82, 0.82, 0.8), rough=0.6)
    M["paint_yellow"] = principled("marking_yellow", (0.85, 0.6, 0.05), rough=0.6)
    M["paint_blue"] = principled("marking_blue", (0.05, 0.2, 0.6), rough=0.6)
    M["paint_green"] = principled("marking_green", (0.05, 0.35, 0.15), rough=0.6)
    M["barrier"] = pbr("barrier_concrete", "brushed_concrete", size=2.0, bright=1.25)
    M["led_warm"] = principled("led_warm", (1, 0.85, 0.65), rough=0.4, emission=(1.0, 0.78, 0.52), estr=0.0)
    M["interior_glow"] = principled("interior_glow", (0.9, 0.85, 0.78), rough=0.6, emission=(1.0, 0.82, 0.6), estr=0.0)
    M["primary"] = principled("brand_primary", C_PRIMARY, rough=0.4)
    M["accent"] = principled("brand_accent", C_ACCENT, rough=0.35)
    M["rubber"] = principled("rubber", (0.015, 0.015, 0.015), rough=0.8)
    M["rim"] = principled("rim", (0.6, 0.6, 0.62), rough=0.25, metal=1.0)
    M["chrome"] = principled("chrome", (0.8, 0.8, 0.8), rough=0.1, metal=1.0)
    M["tail"] = principled("taillight", (0.3, 0.0, 0.0), rough=0.2, emission=(1.0, 0.02, 0.01), estr=0.0)
    M["head"] = principled("headlight", (0.9, 0.9, 0.9), rough=0.1, emission=(1.0, 0.95, 0.85), estr=0.0)
    M["ev_charger"] = principled("ev_charger", (0.85, 0.85, 0.83), rough=0.3)
    M["soil"] = principled("soil", (0.12, 0.08, 0.05), rough=0.9)
    M["mountain"] = pbr("mountain_rock", "aerial_grass_rock", size=60.0, bright=0.85, hue=0.47, sat=0.6, bump=0.0)
    return M


# ======================================================================================
# terrain and highway
# ======================================================================================
def terrain_height(x, y):
    hw_y = -18.0
    # flat zone around site and highway corridor
    d_site = max(0.0, max(abs(x - 37) - 60, 0) ** 2 + max(abs(y - 22) - 45, 0) ** 2) ** 0.5
    d_hwy = max(0.0, abs(y - hw_y) - 30)
    d = min(d_site, d_hwy) if y < 60 else d_site
    if y < hw_y:
        d = d_hwy
    t = min(1.0, d / 260.0)
    t = t * t * (3 - 2 * t)
    v = Vector((x / 420.0, y / 420.0, 0.0))
    hills = noise.fractal(v, 0.6, 2.0, 5) * 26.0 + 12.0
    # distant mountain range to the north/north-east (Gegham / Tsaghkunyats analogue)
    ridge = 0.0
    if y > 700:
        r = min(1.0, (y - 700) / 1300.0)
        ridge = (r ** 1.6) * (360 + 160 * noise.fractal(Vector((x / 900, y / 900, 3.1)), 0.55, 2.1, 6))
    south = 0.0
    if y < -400:
        r = min(1.0, (-400 - y) / 1600.0)
        south = (r ** 1.8) * (180 + 90 * noise.fractal(Vector((x / 700, y / 700, 7.7)), 0.55, 2.1, 5))
    return t * max(0.0, hills) + ridge + south


def build_terrain(M):
    size, n = 5200.0, 260
    verts, faces = [], []
    # non-uniform grid: denser near the site
    def axis(i):
        u = (i / n) * 2 - 1
        return math.copysign(abs(u) ** 1.8, u) * size / 2 + 37
    xs = [axis(i) for i in range(n + 1)]
    ys = [axis(i) - 15 for i in range(n + 1)]
    for j, y in enumerate(ys):
        for i, x in enumerate(xs):
            z = terrain_height(x, y) - 0.06
            verts.append((x, y, z))
    for j in range(n):
        for i in range(n):
            a = j * (n + 1) + i
            faces.append((a, a + 1, a + n + 2, a + n + 1))
    ob = mesh_obj("terrain", verts, faces, [M["steppe"]], "terrain", smooth_angle=60)
    return ob


def build_highway(M):
    hw = L["highway"]
    x0, x1 = hw["x0"], hw["x1"]
    yn = hw["y_edge"]
    yfar = hw["y_far"]
    # asphalt full width (both carriageways incl. shoulders), median raised separately
    box("hwy_asphalt", x0, yfar, -0.05, x1, yn, 0.0, M["asphalt_hwy"], "highway")
    med = hw["median"]
    # median: grass strip with concrete New Jersey barrier
    box("median_grass", x0, med[0] + 0.2, -0.05, x1, med[1] - 0.2, 0.08, M["grass"], "highway")
    prof = [(-0.30, 0.0), (0.30, 0.0), (0.30, 0.08), (0.10, 0.33), (0.08, 0.81), (-0.08, 0.81), (-0.10, 0.33), (-0.30, 0.08)]
    yc = (med[0] + med[1]) / 2
    verts = []
    for x in (x0, x1):
        for py, pz in prof:
            verts.append((x, yc + py, pz))
    n = len(prof)
    faces = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, n + j, n + i))
    mesh_obj("median_barrier", verts, faces, [M["barrier"]], "highway")
    # markings
    W = M["paint_white"]
    nc, sc = hw["north"], hw["south"]
    for carr, tag in ((nc, "n"), (sc, "s")):
        yo = carr["shoulder"][1] if tag == "n" else carr["shoulder"][1]
        # outer edge line (between shoulder and lane1)
        ye = carr["lane1"][1] if tag == "n" else carr["lane1"][0]
        # careful with orientation: lane tuple is (low, high)
        y_edge_line = carr["lane1"][1] if tag == "n" else carr["lane1"][0]
        y_inner_line = carr["lane2"][0] if tag == "n" else carr["lane2"][1]
        y_mid = carr["lane1"][0] if tag == "n" else carr["lane1"][1]
        if tag == "n":
            # gap in edge line where aux lanes join
            strip(f"edge_{tag}_a", [(x0, y_edge_line), (-110, y_edge_line)], 0.2, 0.004, W)
            strip(f"edge_{tag}_b", [(11, y_edge_line), (64, y_edge_line)], 0.2, 0.004, W)
            strip(f"edge_{tag}_c", [(150, y_edge_line), (x1, y_edge_line)], 0.2, 0.004, W)
            strip(f"aux_dash_{tag}_a", [(-110, y_edge_line), (11, y_edge_line)], 0.3, 0.004, W, dash=(1.0, 1.0))
            strip(f"aux_dash_{tag}_b", [(64, y_edge_line), (150, y_edge_line)], 0.3, 0.004, W, dash=(1.0, 1.0))
        else:
            strip(f"edge_{tag}", [(x0, y_edge_line), (x1, y_edge_line)], 0.2, 0.004, W)
        strip(f"inner_{tag}", [(x0, y_inner_line), (x1, y_inner_line)], 0.15, 0.004, W)
        strip(f"lanes_{tag}", [(x0, y_mid), (x1, y_mid)], 0.15, 0.004, W, dash=(4.0, 8.0))
    # verge between highway and site: grass with shallow swale
    box("verge", x0, yn, -0.08, x1, 0.0, 0.02, M["grass"], "highway")
    # auxiliary lanes (asphalt over verge where needed)
    aux = L["aux"]
    ya, yb = aux["y_inner"], aux["y_outer"]
    prism("decel_lane", [(64, ya), (110, ya), (150, ya), (110, yb), (64, yb)], -0.04, 0.025, M["asphalt_hwy"], cname="highway")
    prism("accel_lane", [(11, ya), (11, yb), (-60, yb), (-110, ya)], -0.04, 0.025, M["asphalt_hwy"], cname="highway")
    strip("aux_edge_e", [(64, yb), (110, yb), (150, ya + 0.1)], 0.2, 0.03, W)
    strip("aux_edge_w", [(11, yb), (-60, yb), (-110, ya + 0.1)], 0.2, 0.03, W)
    # driveways across verge
    prism("entry_drive", [(63.0, yb), (71.5, yb), (72.5, 0.0), (62.5, 0.0)], -0.04, 0.03, M["asphalt"], cname="site")
    prism("exit_drive", [(2.5, yb), (11.5, yb), (11.0, 0.0), (3.0, 0.0)], -0.04, 0.03, M["asphalt"], cname="site")
    # highway lighting poles along median (sparse)
    return


# ======================================================================================
# site
# ======================================================================================
def build_site(M):
    S = L["site"]
    box("site_asphalt", 0, 0, -0.04, S["w"], S["d"], 0.03, M["asphalt"], "site")
    kh = 0.15
    for el in L["landscape"]:
        poly = el["poly"]
        k = el["kind"]
        if k == "pad":
            continue
        if k == "plaza":
            prism(f"plaza", poly, 0.0, kh, M["kerb"], M["pavers"], cname="site")
        elif k == "island":
            prism(f"isl_{el['id']}", poly, 0.0, kh, M["kerb"], M["kerb"], cname="site")
        else:
            prism(f"kerb_{el['id']}", poly, 0.0, kh, M["kerb"], M["kerb"], cname="site")
            inner = offset_poly(poly, -0.16)
            prism(f"plant_{el['id']}", inner, 0.0, kh + 0.02, M["soil"], M["grass"], cname="site")


def build_markings(M):
    W, Y = M["paint_white"], M["paint_yellow"]
    c = L["circulation"]
    z = 0.034
    # lane edges for stacking lanes
    for xx in (58.0, 66.0):
        strip(f"stack_edge_{xx}", [(xx, 12.0), (xx, 27.0)], 0.12, z, W)
    strip("stack_div", [(62.0, 10.0), (62.0, 19.0)], 0.12, z, W, dash=(1.5, 1.5))
    # window lane edge
    strip("winlane_edge", [(54.0, 37.1), (18.25, 37.1)], 0.12, z, W)
    # stop bars at windows
    for w in c["windows"]:
        strip(f"stop_{w['id']}", [(w["x"] - 1.2, 33.7), (w["x"] - 1.2, 37.0)], 0.3, z, W)
    # parking stall lines
    for s in L["parking"]["stalls"]:
        x, y, w, l = s["x"], s["y"], s["w"], s["l"]
        mat = W
        for xx in (x - w / 2, x + w / 2):
            strip(f"stall_{s['id']}_{xx:.1f}", [(xx, y - l / 2), (xx, y + l / 2)], 0.12, z, mat)
        if s["type"] == "acc":
            box(f"acc_{s['id']}", x - w / 2 + 0.1, y - l / 2 + 0.1, 0.03, x + w / 2 - 0.1, y + l / 2 - 0.1, z - 0.001, M["paint_blue"], "markings")
        if s["type"] == "ev":
            box(f"ev_{s['id']}", x - w / 2 + 0.1, y - l / 2 + 0.1, 0.03, x + w / 2 - 0.1, y + l / 2 - 0.1, z - 0.001, M["paint_green"], "markings")
    lb = L["parking"]["long_bay"]["poly"]
    strip("long_bay", [lb[3], lb[0], lb[1], lb[2]], 0.12, z, W)
    # arrows (simple chevrons) along drive-thru path
    def arrow(name, x, y, heading):
        h = math.radians(heading)
        d = Vector((math.cos(h), math.sin(h)))
        n = Vector((-d.y, d.x))
        p = Vector((x, y))
        shaft = [p - d * 1.6, p + d * 0.6]
        strip(name + "_s", [tuple(shaft[0]), tuple(shaft[1])], 0.18, z, W)
        tip = p + d * 1.4
        l1 = p + d * 0.4 + n * 0.6
        l2 = p + d * 0.4 - n * 0.6
        mesh_obj(name + "_h", [(tip.x, tip.y, z), (l1.x, l1.y, z), (l2.x, l2.y, z)], [(0, 1, 2)], [W], "markings")
    arrow("arr1", 59.75, 14.0, 90); arrow("arr2", 64.25, 14.0, 90)
    arrow("arr3", 50.0, 35.35, 180); arrow("arr4", 22.0, 35.35, 180)
    arrow("arr5", 12.25, 22.0, -90); arrow("arr6", 40.0, 12.0, 180); arrow("arr7", 25.0, 12.0, 180)
    arrow("arr8", 67.0, 3.0, 90); arrow("arr9", 7.0, 3.5, -90)


# ======================================================================================
# building
# ======================================================================================
def roof_z(x, y):
    """Underside of the hypar roof (bilinear surface through the four corner heights)."""
    r = L["building"]["roof"]
    u = (x - r["x0"]) / (r["x1"] - r["x0"])
    v = (y - r["y0"]) / (r["y1"] - r["y0"])
    south = r["z_sw"] + u * (r["z_se"] - r["z_sw"])
    north = r["z_nw"] + u * (r["z_ne"] - r["z_nw"])
    return south + v * (north - south)


def facade_line(b, facade, t=0.35):
    x0, x1, y0, y1 = b["x0"], b["x1"], b["y0"], b["y1"]
    if facade == "N":
        return lambda s, off=0.0: (s, y1 - t / 2 + off)
    if facade == "S":
        return lambda s, off=0.0: (s, y0 + t / 2 - off)
    if facade == "E":
        return lambda s, off=0.0: (x1 - t / 2 + off, s)
    return lambda s, off=0.0: (x0 + t / 2 - off, s)


def slab_quad(name, facade, b, a, c, zbot, ztop_fn, thick, mat, cname="building", off=0.0):
    """Vertical slab along a facade from s=a..c, bottom zbot, top following ztop_fn(x,y)."""
    P = facade_line(b, facade)
    pa0, pc0 = P(a, off - thick / 2), P(c, off - thick / 2)
    pa1, pc1 = P(a, off + thick / 2), P(c, off + thick / 2)
    za, zc = ztop_fn(*P(a)), ztop_fn(*P(c))
    v = [(pa0[0], pa0[1], zbot), (pc0[0], pc0[1], zbot), (pc0[0], pc0[1], zc), (pa0[0], pa0[1], za),
         (pa1[0], pa1[1], zbot), (pc1[0], pc1[1], zbot), (pc1[0], pc1[1], zc), (pa1[0], pa1[1], za)]
    f = [(0, 1, 2, 3), (5, 4, 7, 6), (4, 0, 3, 7), (1, 5, 6, 2), (3, 2, 6, 7), (4, 5, 1, 0)]
    return mesh_obj(name, v, f, [mat], cname)


def mullions(name, facade, b, a, c, zbot, ztop_fn, M, spacing=1.5, w=0.06, d=0.14, ends=True):
    P = facade_line(b, facade)
    n = max(1, round((c - a) / spacing))
    ss = [a + (c - a) * i / n for i in range(0 if ends else 1, n + 1 if ends else n)]
    for i, s in enumerate(ss):
        x, y = P(s)
        zt = ztop_fn(x, y)
        if facade in ("N", "S"):
            box(f"{name}_mu{i}", s - w / 2, y - d / 2, zbot, s + w / 2, y + d / 2, zt, M["bronze"])
        else:
            box(f"{name}_mu{i}", x - d / 2, s - w / 2, zbot, x + d / 2, s + w / 2, zt, M["bronze"])


def hband(name, facade, b, a, c, z, M, h=0.07, d=0.14):
    P = facade_line(b, facade)
    (xa, ya), (xc, yc) = P(a), P(c)
    if facade in ("N", "S"):
        box(name, a, ya - d / 2, z - h / 2, c, ya + d / 2, z + h / 2, M["bronze"])
    else:
        box(name, xa - d / 2, a, z - h / 2, xa + d / 2, c, z + h / 2, M["bronze"])


def build_building(M, night=False):
    b = L["building"]
    x0, x1, y0, y1, f0 = b["x0"], b["x1"], b["y0"], b["y1"], b["ffl"]
    r = b["roof"]
    WT = f0 + r["wall_top"]          # top of tuff walls; frameless clerestory above up to roof soffit
    box("plinth", x0 - 0.05, y0 - 0.05, 0.0, x1 + 0.05, y1 + 0.05, f0, M["concrete"])
    box("floor", x0 + 0.3, y0 + 0.3, f0, x1 - 0.3, y1 - 0.3, f0 + 0.01, M["floor_int"], "interior")
    flat = lambda z: (lambda x, y: z)
    rz = lambda x, y: roof_z(x, y) - 0.002
    for fac in ("N", "S", "E", "W"):
        ops = sorted([o for o in b["openings"] if o["facade"] == fac], key=lambda o: o["a"])
        a0, a1 = (x0, x1) if fac in ("N", "S") else (y0, y1)
        # curtain-wall ranges (full height to roof)
        cws = [o for o in ops if o["kind"] == "curtain_wall"]
        others = [o for o in ops if o["kind"] != "curtain_wall" and not any(cw["a"] <= o["a"] and o["b"] <= cw["b"] for cw in cws)]
        cur = a0
        k = 0
        events = sorted(cws + others, key=lambda o: o["a"])
        for o in events:
            if o["a"] > cur:
                slab_quad(f"tuff_{fac}{k}", fac, b, cur, o["a"], f0, flat(WT), 0.35, M["tuff"]); k += 1
            if o["kind"] == "curtain_wall":
                slab_quad(f"cwglass_{fac}{k}", fac, b, o["a"], o["b"], f0, rz, 0.024, M["glass"]); k += 1
                mullions(f"cw_{fac}{k}", fac, b, o["a"], o["b"], f0, rz, M, spacing=1.6)
                hband(f"cw_tr_{fac}{k}", fac, b, o["a"], o["b"], WT, M)
                hband(f"cw_sill_{fac}{k}", fac, b, o["a"], o["b"], f0 + 0.04, M, h=0.08)
            else:
                if o["sill"] > 0:
                    slab_quad(f"tuff_sill_{fac}{k}", fac, b, o["a"], o["b"], f0, flat(f0 + o["sill"]), 0.35, M["tuff"]); k += 1
                head = f0 + o["head"]
                if head < WT:
                    P = facade_line(b, fac)
                    # head slab between head and wall top
                    va = []
                    slab_quad(f"tuff_head_{fac}{k}", fac, b, o["a"], o["b"], head, flat(WT), 0.35, M["tuff"]); k += 1
                if o["kind"] in ("glazing", "service_window"):
                    slab_quad(f"glass_{fac}{k}", fac, b, o["a"], o["b"], f0 + o["sill"], flat(head), 0.024, M["glass"]); k += 1
                    mullions(f"gl_{fac}{k}", fac, b, o["a"], o["b"], f0 + o["sill"], flat(head), M,
                             spacing=1.0 if o["kind"] == "glazing" else 2.0)
                    hband(f"gl_b_{fac}{k}", fac, b, o["a"], o["b"], f0 + o["sill"], M)
                    hband(f"gl_t_{fac}{k}", fac, b, o["a"], o["b"], head, M)
                elif o["kind"] in ("door_solid", "door"):
                    slab_quad(f"door_{fac}{k}", fac, b, o["a"], o["b"], f0, flat(head), 0.06, M["bronze_matte"], off=0.12); k += 1
            cur = o["b"]
        if cur < a1:
            slab_quad(f"tuff_{fac}{k}", fac, b, cur, a1, f0, flat(WT), 0.35, M["tuff"]); k += 1
        # clerestory band above tuff walls, except where a curtain wall already reaches the roof
        cur = a0
        for cw in cws + [dict(a=a1, b=a1)]:
            if cw["a"] > cur + 0.01:
                slab_quad(f"clere_{fac}{k}", fac, b, cur, cw["a"], WT, rz, 0.024, M["glass"]); k += 1
                mullions(f"clm_{fac}{k}", fac, b, cur, cw["a"], WT, rz, M, spacing=1.5, w=0.04, d=0.1)
            cur = max(cur, cw["b"])
        # bronze coping on top of tuff walls (thin)
    for (xa, ya, xb, yb) in ((x0, y1 - 0.38, x1, y1 + 0.02), (x0, y0 - 0.02, x1, y0 + 0.38), (x1 - 0.38, y0, x1 + 0.02, y1), (x0 - 0.02, y0, x0 + 0.38, y1)):
        box(f"coping_{xa:.0f}_{ya:.0f}", xa, ya, WT - 0.02, xb, yb, WT + 0.03, M["bronze"])
    # projecting service-window surrounds on the north (drive-thru) facade
    for w in L["circulation"]["windows"]:
        wx = w["x"]
        box(f"svc_shelf_{w['id']}", wx - 1.2, y1, f0 + 0.9, wx + 1.2, y1 + 0.42, f0 + 0.98, M["bronze"])
        box(f"svc_hood_{w['id']}", wx - 1.2, y1, f0 + 2.48, wx + 1.2, y1 + 0.55, f0 + 2.62, M["bronze"])
        box(f"svc_jl_{w['id']}", wx - 1.2, y1, f0 + 0.9, wx - 1.06, y1 + 0.42, f0 + 2.62, M["bronze"])
        box(f"svc_jr_{w['id']}", wx + 1.06, y1, f0 + 0.9, wx + 1.2, y1 + 0.42, f0 + 2.62, M["bronze"])
        sign = BRAND.get("textures", {}).get(f"window_{w['id']}")
        image_plane(f"svc_sign_{w['id']}", sign, wx, y1 + 0.56, f0 + 2.55, 2.2, 0.12, "N", emit=3.0 if night else 0.6, offset=0.0)
    build_interior(M, b, night)
    build_roof(M, b, night)
    build_tower(M, b, night)
    build_pergola(M, b)
    build_canopy(M, b, night)


def build_interior(M, b, night):
    x0, x1, y0, y1, f0 = b["x0"], b["x1"], b["y0"], b["y1"], b["ffl"]
    mid = 28.0
    WT = f0 + b["roof"]["wall_top"]
    # partitions (to wall-top; café is open to the sloping oak soffit)
    box("int_wall_mid_w", x0 + 0.35, mid - 0.06, f0, 35.0, mid + 0.06, WT, M["plaster"], "interior")
    box("int_wall_r4", 29.45, y0 + 0.35, f0, 29.55, mid, WT, M["plaster"], "interior")
    box("int_wall_r3", 34.95, y0 + 0.35, f0, 35.05, mid, WT, M["plaster"], "interior")
    box("int_wall_bo", 28.95, mid, f0, 29.05, y1 - 0.35, WT, M["plaster"], "interior")
    # ceilings for BOH rooms (café and bar line open to roof soffit)
    box("ceiling_boh", x0 + 0.35, y0 + 0.35, f0 + 2.9, 35.0, mid, f0 + 2.95, M["plaster"], "interior")
    box("ceiling_store", x0 + 0.35, mid, f0 + 2.9, 29.0, y1 - 0.35, f0 + 2.95, M["plaster"], "interior")
    # café counter, back wall in brand primary with menu screens
    box("cafe_counter", 38.6, mid + 0.05, f0, x1 - 0.4, mid + 1.0, f0 + 1.0, M["tuff_dark"], "interior")
    box("cafe_counter_top", 38.5, mid, f0 + 1.0, x1 - 0.38, mid + 1.05, f0 + 1.06, M["counter"], "interior")
    box("cafe_backwall", 35.05, mid - 0.04, f0 + 1.06, x1 - 0.36, mid + 0.02, WT, M["primary"], "interior")
    box("window_bar", 35.4, y0 + 0.4, f0 + 1.0, x1 - 0.6, y0 + 0.85, f0 + 1.05, M["oak"], "interior")
    for i in range(6):
        sx = 35.9 + i * 1.1
        box(f"stool_{i}", sx - 0.18, y0 + 1.05, f0, sx + 0.18, y0 + 1.4, f0 + 0.75, M["bronze_matte"], "interior")
    for i, (tx, ty) in enumerate([(37.0, 26.6), (40.2, 26.6)]):
        box(f"table_{i}", tx - 0.45, ty - 0.45, f0 + 0.72, tx + 0.45, ty + 0.45, f0 + 0.76, M["oak"], "interior")
        box(f"table_leg_{i}", tx - 0.05, ty - 0.05, f0, tx + 0.05, ty + 0.05, f0 + 0.72, M["bronze_matte"], "interior")
    for e in b["equipment"]:
        bx = e["box"]
        mat = M["chrome"] if ("Espresso" in e["name"] or "Grinder" in e["name"] or "brewer" in e["name"]) else M["counter"]
        box(f"eq_{e['tag']}", bx[0], bx[1], f0, bx[2], bx[3], f0 + min(e["h"], 2.2), mat, "interior")
    box("bar_counter", 29.1, y1 - 1.05, f0, x1 - 0.4, y1 - 0.4, f0 + 0.9, M["counter"], "interior")
    box("bar_backsplash", 29.1, mid + 0.06, f0 + 0.9, 35.0, mid + 0.12, f0 + 2.2, M["tuff_dark"], "interior")
    mb = BRAND.get("textures", {}).get("menu_interior")
    image_plane("int_menu_1", mb, 36.9, mid + 0.03, f0 + 2.35, 1.5, 0.85, "S", emit=2.5 if night else 1.0, cname="interior", offset=0.01)
    image_plane("int_menu_2", mb, 38.6, mid + 0.03, f0 + 2.35, 1.5, 0.85, "S", emit=2.5 if night else 1.0, cname="interior", offset=0.01)
    lg = BRAND.get("textures", {}).get("logo_badge")
    image_plane("int_logo", lg, 41.2, mid + 0.03, f0 + 2.45, 1.2, 1.2, "S", emit=2.0 if night else 0.3, cname="interior", offset=0.01)
    # pendant lights over window bar (hang from sloping soffit)
    for i in range(5):
        px = 35.9 + i * 1.5
        zt = roof_z(px, y0 + 0.62)
        box(f"pendant_cord_{i}", px - 0.006, y0 + 0.616, f0 + 2.3, px + 0.006, y0 + 0.628, zt, M["steel_dark"], "interior")
        box(f"pendant_{i}", px - 0.13, y0 + 0.49, f0 + 2.05, px + 0.13, y0 + 0.75, f0 + 2.3, M["led_warm"], "interior")
    lights = [(39.0, 26.0), (36.5, 26.0), (41.5, 26.0), (33.0, 30.5), (38.0, 30.5), (42.0, 30.5), (26.5, 30.5)]
    for i, (lx, ly) in enumerate(lights):
        ld = bpy.data.lights.new(f"int_light_{i}", "AREA")
        ld.energy = 650 if night else 140
        ld.color = (1.0, 0.84, 0.66)
        ld.size = 1.2
        lo = bpy.data.objects.new(f"int_light_{i}", ld)
        lo.location = (lx, ly, min(roof_z(lx, ly) - 0.3, f0 + 3.4))
        link(lo, "lights_interior")


def build_roof(M, b, night):
    r = b["roof"]
    x0, x1, y0, y1, t = r["x0"], r["x1"], r["y0"], r["y1"], r["thickness"]
    nx, ny = 30, 20
    verts, faces, idx = [], [], []
    grid = lambda i, j: (x0 + (x1 - x0) * i / nx, y0 + (y1 - y0) * j / ny)
    for top in (0, 1):
        for j in range(ny + 1):
            for i in range(nx + 1):
                x, y = grid(i, j)
                verts.append((x, y, roof_z(x, y) + (t if top else 0.0)))
    off = (nx + 1) * (ny + 1)
    V = lambda i, j, top=0: (off if top else 0) + j * (nx + 1) + i
    for j in range(ny):
        for i in range(nx):
            faces.append((V(i, j), V(i, j + 1), V(i + 1, j + 1), V(i + 1, j))); idx.append(0)
            faces.append((V(i, j, 1), V(i + 1, j, 1), V(i + 1, j + 1, 1), V(i, j + 1, 1))); idx.append(1)
    for i in range(nx):
        faces.append((V(i, 0), V(i + 1, 0), V(i + 1, 0, 1), V(i, 0, 1))); idx.append(2)
        faces.append((V(i + 1, ny), V(i, ny), V(i, ny, 1), V(i + 1, ny, 1))); idx.append(2)
    for j in range(ny):
        faces.append((V(0, j + 1), V(0, j), V(0, j, 1), V(0, j + 1, 1))); idx.append(2)
        faces.append((V(nx, j), V(nx, j + 1), V(nx, j + 1, 1), V(nx, j, 1))); idx.append(2)
    mesh_obj("roof", verts, faces, [M["oak"], M["membrane"], M["bronze"]], "building", mat_idx=idx)
    # LED reveal just inside the fascia
    e = 0.07
    segs = [((x0 + e, y0 + e), (x1 - e, y0 + e)), ((x1 - e, y0 + e), (x1 - e, y1 - e)),
            ((x1 - e, y1 - e), (x0 + e, y1 - e)), ((x0 + e, y1 - e), (x0 + e, y0 + e))]
    for k, (p, q) in enumerate(segs):
        n = 24
        vv, ff = [], []
        d = Vector((q[0] - p[0], q[1] - p[1])).normalized(); nn = Vector((-d.y, d.x)) * 0.025
        for s in range(n + 1):
            px = p[0] + (q[0] - p[0]) * s / n; py = p[1] + (q[1] - p[1]) * s / n
            z = roof_z(px, py) - 0.01
            vv += [(px + nn.x, py + nn.y, z), (px - nn.x, py - nn.y, z)]
        for s in range(n):
            a = 2 * s; ff.append((a, a + 1, a + 3, a + 2))
        mesh_obj(f"roof_led_{k}", vv, ff, [M["led_warm"]], "building")
    if night:
        pts = []
        for xx in range(int(x0) + 2, int(x1) - 1, 3):
            pts += [(xx + 0.5, y1 - 1.7), (xx + 0.5, y0 + 1.7)]
        for k, (px, py) in enumerate(pts):
            ld = bpy.data.lights.new(f"downlight_{k}", "SPOT")
            ld.energy = 110; ld.color = (1.0, 0.8, 0.58)
            ld.spot_size = math.radians(75); ld.spot_blend = 0.6; ld.shadow_soft_size = 0.05
            lo = bpy.data.objects.new(f"downlight_{k}", ld)
            lo.location = (px, py, roof_z(px, py) - 0.03)
            link(lo, "lights_exterior")
    # slim bronze columns at the far cantilever corners (NW, NE); SE corner carried by the tower
    for (px, py) in ((x0 + 0.5, y1 - 0.5), (x1 - 0.5, y1 - 0.5), (x0 + 0.5, y0 + 0.5)):
        box(f"col_{px:.0f}_{py:.0f}", px - 0.1, py - 0.1, 0.0, px + 0.1, py + 0.1, roof_z(px, py), M["bronze"])


def build_tower(M, b, night):
    t = b["tower"]
    cx, cy, w, d, h = t["x"], t["y"], t["w"], t["d"], t["h"]
    box("tower", cx - w / 2, cy - d / 2, 0.0, cx + w / 2, cy + d / 2, h, M["tuff"], "building")
    box("tower_cap", cx - w / 2 - 0.03, cy - d / 2 - 0.03, h, cx + w / 2 + 0.03, cy + d / 2 + 0.03, h + 0.1, M["bronze"], "building")
    # recessed vertical reveal (bronze) on south and east faces
    box("tower_reveal_s", cx - 0.04, cy - d / 2 - 0.01, 0.4, cx + 0.04, cy - d / 2 + 0.02, h - 2.4, M["bronze"], "building")
    logo = BRAND.get("textures", {}).get("logo_tower")
    for fac in ("S", "E", "W", "N"):
        if fac in ("S", "N"):
            yy = cy - d / 2 if fac == "S" else cy + d / 2
            image_plane(f"tower_logo_{fac}", logo, cx, yy, h - 1.15, 1.45, 1.45, fac, emit=7.0 if night else 0.0, offset=0.012, rough=0.3)
        else:
            xx = cx + w / 2 if fac == "E" else cx - w / 2
            image_plane(f"tower_logo_{fac}", logo, xx, cy, h - 1.15, 1.45, 1.45, fac, emit=7.0 if night else 0.0, offset=0.012, rough=0.3)
    p = b["pylon"]
    box("pylon", p["x"] - p["w"] / 2, p["y"] - p["d"] / 2, 0.0, p["x"] + p["w"] / 2, p["y"] + p["d"] / 2, p["h"], M["tuff"], "signage")
    box("pylon_base", p["x"] - p["w"] / 2 - 0.2, p["y"] - p["d"] / 2 - 0.2, 0.0, p["x"] + p["w"] / 2 + 0.2, p["y"] + p["d"] / 2 + 0.2, 0.4, M["concrete"], "signage")
    box("pylon_cap", p["x"] - p["w"] / 2 - 0.03, p["y"] - p["d"] / 2 - 0.03, p["h"], p["x"] + p["w"] / 2 + 0.03, p["y"] + p["d"] / 2 + 0.03, p["h"] + 0.08, M["bronze"], "signage")
    pl = BRAND.get("textures", {}).get("pylon_face")
    for fac in ("S", "N"):
        yy = p["y"] - p["d"] / 2 if fac == "S" else p["y"] + p["d"] / 2
        image_plane(f"pylon_face_{fac}", pl, p["x"], yy, p["h"] - 2.6, 1.9, 4.8, fac, emit=5.0 if night else 0.0, offset=0.012)
    fw = BRAND.get("textures", {}).get("wordmark_fascia")
    zN = roof_z(35.5, b["roof"]["y1"]) + b["roof"]["thickness"] / 2
    image_plane("fascia_word_N", fw, 35.5, b["roof"]["y1"], zN, 5.2, 0.3, "N", emit=5.0 if night else 0.0, offset=0.012)
    zS = roof_z(30.5, b["roof"]["y0"]) + b["roof"]["thickness"] / 2
    image_plane("fascia_word_S", fw, 30.5, b["roof"]["y0"], zS, 5.2, 0.3, "S", emit=5.0 if night else 0.0, offset=0.012)


def build_pergola(M, b):
    p = b["pergola"]
    x0, y0, x1, y1, z = p["x0"], p["y0"], p["x1"], p["y1"], p["z"]
    for (px, py) in ((x0, y0), (x1 - 0.12, y0), (x0, y1 - 0.12), ((x0 + x1) / 2, y0), (x0, (y0 + y1) / 2)):
        box(f"perg_post_{px:.1f}_{py:.1f}", px, py, 0.15, px + 0.12, py + 0.12, z, M["bronze"], "building")
    box("perg_beam_s", x0, y0, z - 0.25, x1, y0 + 0.12, z, M["bronze"], "building")
    box("perg_beam_n", x0, y1 - 0.12, z - 0.25, x1, y1, z, M["bronze"], "building")
    box("perg_beam_w", x0, y0, z - 0.25, x0 + 0.12, y1, z, M["bronze"], "building")
    s = x0 + 0.1
    while s < x1 - 0.1:
        box(f"perg_slat_{s:.2f}", s, y0, z, s + p["slat"], y1, z + 0.16, M["oak"], "building")
        s += p["spacing"]


def build_canopy(M, b, night):
    c = b["order_canopy"]
    x0, y0, x1, y1, t = c["x0"], c["y0"], c["x1"], c["y1"], c["thickness"]
    zf = lambda x, y: c["z_s"] + (y - y0) / (y1 - y0) * (c["z_n"] - c["z_s"])
    v = [(x0, y0, zf(x0, y0)), (x1, y0, zf(x1, y0)), (x1, y1, zf(x1, y1)), (x0, y1, zf(x0, y1))]
    vt = [(x, y, z + t) for (x, y, z) in v]
    faces = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    mesh_obj("can_roof", v + vt, faces, [M["oak"], M["membrane"], M["bronze"]], "building", mat_idx=[0, 1, 2, 2, 2, 2])
    for (px, py) in ((57.3, y0 + 0.5), (57.3, y1 - 0.5), (61.95, y0 + 0.5), (61.95, y1 - 0.5)):
        box(f"can_post_{px:.1f}_{py:.1f}", px - 0.09, py - 0.09, 0.15, px + 0.09, py + 0.09, zf(px, py), M["bronze"], "building")
    mb = BRAND.get("textures", {}).get("menu_board")
    for op in L["circulation"]["order_points"]:
        x, y = op["x"], op["y"]
        box(f"mb_post_{op['id']}", x - 0.14, y - 1.15, 0.15, x + 0.14, y + 1.15, 2.55, M["bronze_matte"], "signage")
        image_plane(f"mb_screen_{op['id']}", mb, x + 0.15, y, 1.78, 2.05, 1.18, "E", emit=3.0 if night else 1.4, cname="signage")
        box(f"speaker_{op['id']}", x - 0.1, y - 2.3, 0.15, x + 0.22, y - 1.85, 1.3, M["bronze_matte"], "signage")
    pb = BRAND.get("textures", {}).get("preview_board")
    for i, p in enumerate(L["circulation"]["preview_boards"]):
        box(f"pv_post_{i}", p["x"] - 0.1, p["y"] - 0.62, 0.15, p["x"] + 0.1, p["y"] + 0.62, 2.25, M["bronze_matte"], "signage")
        image_plane(f"pv_screen_{i}", pb, p["x"] + 0.11, p["y"], 1.62, 1.15, 1.05, "E", emit=2.5 if night else 1.1, cname="signage")
    if night:
        for k, (px, py) in enumerate([(59.75, 20.5), (64.25, 20.5), (59.75, 25), (64.25, 25)]):
            ld = bpy.data.lights.new(f"can_light_{k}", "SPOT"); ld.energy = 170; ld.spot_size = math.radians(80)
            ld.color = (1.0, 0.82, 0.6)
            lo = bpy.data.objects.new(f"can_light_{k}", ld); lo.location = (px, py, zf(px, py) - 0.05); link(lo, "lights_exterior")


# ======================================================================================
# vegetation, furniture, lights
# ======================================================================================
TEMPLATES = {}
MM = {}


def fix_images():
    for img in bpy.data.images:
        fp = bpy.path.abspath(img.filepath)
        if img.filepath and not os.path.exists(fp):
            hits = glob.glob(f"{A}/models/**/{os.path.basename(img.filepath)}", recursive=True)
            if hits:
                img.filepath = hits[0]


def template(model, cname):
    key = (model, cname)
    if key in TEMPLATES:
        return TEMPLATES[key]
    p = f"{A}/models/{model}/{model}_1k.blend"
    if not os.path.exists(p):
        return None
    with bpy.data.libraries.load(p, link=False) as (df, dt):
        dt.collections = [c for c in df.collections if c == cname]
    if not dt.collections:
        return None
    c = dt.collections[0]
    fix_images()
    TEMPLATES[key] = c
    return c


def instance(c, name, x, y, z=0.0, rot=0.0, s=1.0, cname="vegetation"):
    if c is None:
        return None
    e = bpy.data.objects.new(name, None)
    e.instance_type = "COLLECTION"
    e.instance_collection = c
    e.location = (x, y, z)
    e.rotation_euler = (0, 0, math.radians(rot))
    e.scale = (s, s, s)
    return link(e, cname)


def point_in_poly(x, y, poly):
    inside = False
    n = len(poly)
    for i in range(n):
        x0, y0 = poly[i]; x1, y1 = poly[(i + 1) % n]
        if ((y0 > y) != (y1 > y)) and (x < (x1 - x0) * (y - y0) / (y1 - y0 + 1e-12) + x0):
            inside = not inside
    return inside


def build_vegetation(M, quality="final"):
    tA = template("island_tree_01", "island_tree_01_LOD1")
    tB = template("tree_small_02", "tree_small_02_LOD1")
    tS = template("jacaranda_tree", "jacaranda_tree_LOD1")
    kinds = {"tree_a": (tA, 0.9), "tree_b": (tB, 1.15), "tree_small": (tB, 0.8)}
    for i, t in enumerate(L["trees"]):
        c, sc = kinds.get(t["kind"], (tA, 1.0))
        instance(c, f"tree_{i}", t["x"], t["y"], 0.17, t["rot"], sc * t["s"])
    shrubs = [template(f"shrub_0{k}", f"shrub_0{k}_LOD1") for k in (1, 2, 3, 4)]
    shrubs = [s for s in shrubs if s]
    grass = template("grass_medium_01", "grass_medium_01_LOD1")
    rnd = random.Random(11)
    n_sh = 0
    for el in L["landscape"]:
        if el["kind"] != "planting":
            continue
        poly = el["poly"]
        xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
        area = abs(poly_area_sign(poly)) / 2
        dens_sh = 0.10 if quality == "final" else 0.04
        dens_gr = 0.55 if quality == "final" else 0.15
        for k in range(int(area * dens_sh)):
            x = rnd.uniform(min(xs) + 0.5, max(xs) - 0.5); y = rnd.uniform(min(ys) + 0.5, max(ys) - 0.5)
            if point_in_poly(x, y, poly) and shrubs:
                instance(rnd.choice(shrubs), f"shrub_{n_sh}", x, y, 0.17, rnd.uniform(0, 360), rnd.uniform(0.6, 1.0)); n_sh += 1
        if grass:
            for k in range(int(area * dens_gr)):
                x = rnd.uniform(min(xs) + 0.3, max(xs) - 0.3); y = rnd.uniform(min(ys) + 0.3, max(ys) - 0.3)
                if point_in_poly(x, y, poly):
                    instance(grass, f"grass_{n_sh}_{k}", x, y, 0.17, rnd.uniform(0, 360), rnd.uniform(0.7, 1.2)); n_sh += 1
    # roadside steppe vegetation scatter along verge/outside site
    if grass:
        for k in range(900 if quality == "final" else 200):
            x = rnd.uniform(-160, 230); y = rnd.uniform(46, 140)
            instance(grass, f"steppe_grass_{k}", x, y, terrain_height(x, y) - 0.05, rnd.uniform(0, 360), rnd.uniform(0.8, 1.5))
    # distant tree clusters (village / windbreak rows typical of Kotayk)
    for k in range(70):
        x = rnd.uniform(-450, 550); y = rnd.uniform(150, 600)
        instance(rnd.choice([tA, tB]), f"far_tree_{k}", x, y, terrain_height(x, y) - 0.2, rnd.uniform(0, 360), rnd.uniform(1.0, 1.6))
    for k in range(40):  # windbreak row along highway far side
        x = -300 + k * 16 + rnd.uniform(-3, 3)
        y = L["highway"]["y_far"] - 14
        instance(rnd.choice([tA, tB]), f"wind_{k}", x, y, terrain_height(x, y) - 0.1, rnd.uniform(0, 360), rnd.uniform(1.0, 1.4))


def build_furniture(M):
    tset = template("outdoor_table_chair_set_01", "outdoor_table_chair_set_01")
    plant = template("planter_box_01", "planter_box_01")
    lamp = template("street_lamp_01", "street_lamp_01")
    bin_ = template("metal_trash_can", "metal_trash_can")
    p = L["building"]["pergola"]
    k = 0
    for xx in (17.2, 19.9, 22.6):
        for yy in (22.4, 25.2, 27.6):
            instance(tset, f"tset_{k}", xx, yy, 0.15, (k * 47) % 360, 1.0, "furniture"); k += 1
    for xx in (26.0, 29.0, 45.0):
        instance(tset, f"tset_{k}", xx, 21.6, 0.15, k * 30, 1.0, "furniture"); k += 1
    for i, (xx, yy) in enumerate([(24.8, 20.6), (35.0, 20.6), (47.3, 23.0), (47.3, 30.5), (16.0, 30.0)]):
        instance(plant, f"planter_{i}", xx, yy, 0.15, 0, 1.0, "furniture")
    for i, (xx, yy) in enumerate([(44.0, 20.6), (20.0, 20.4)]):
        instance(bin_, f"bin_{i}", xx, yy, 0.15, 0, 1.0, "furniture")
    # bollards along plaza edge
    for i in range(14):
        bx = 16.5 + i * 2.3
        box(f"bollard_{i}", bx - 0.08, 20.05, 0.15, bx + 0.08, 20.21, 1.05, M["bronze"], "furniture")
    # EV chargers
    for s in L["parking"]["stalls"]:
        if s["type"] == "ev":
            box(f"evc_{s['id']}", s["x"] - 0.25, 3.5, 0.15, s["x"] + 0.25, 3.85, 1.7, M["ev_charger"], "furniture")
            box(f"evc_scr_{s['id']}", s["x"] - 0.18, 3.83, 1.15, s["x"] + 0.18, 3.86, 1.5, M["glass_dark"], "furniture")
    # site lighting poles (procedural slim poles)
    for i, lp in enumerate(L["lights"]):
        x, y, h = lp["x"], lp["y"], lp["h"]
        box(f"pole_{i}", x - 0.07, y - 0.07, 0.0, x + 0.07, y + 0.07, h, M["steel_dark"], "furniture")
        box(f"pole_head_{i}", x - 0.35, y - 0.12, h - 0.1, x + 0.35, y + 0.12, h, M["steel_dark"], "furniture")


def build_site_lights(night):
    if not night:
        return
    for i, lp in enumerate(L["lights"]):
        ld = bpy.data.lights.new(f"pole_light_{i}", "SPOT")
        ld.energy = 5200
        ld.spot_size = math.radians(115)
        ld.spot_blend = 0.5
        ld.color = (1.0, 0.86, 0.68)
        ld.shadow_soft_size = 0.2
        lo = bpy.data.objects.new(f"pole_light_{i}", ld)
        lo.location = (lp["x"], lp["y"], lp["h"] - 0.15)
        link(lo, "lights_exterior")
    # pylon and tower wash
    for (x, y, z, e) in ((71.2, -1.0, 0.6, 600), (45.6, 19.5, 0.3, 500), (48.5, 22.5, 0.3, 300)):
        ld = bpy.data.lights.new("wash", "SPOT"); ld.energy = e; ld.spot_size = math.radians(30); ld.color = (1, 0.8, 0.6)
        lo = bpy.data.objects.new("wash", ld); lo.location = (x, y, z)
        look_at(lo, (x, y + 1.5, 6.0)); link(lo, "lights_exterior")


# ======================================================================================
# vehicles
# ======================================================================================
CAR_COLORS = [(0.8, 0.8, 0.8), (0.02, 0.02, 0.022), (0.35, 0.36, 0.38), (0.55, 0.56, 0.58), (0.05, 0.08, 0.2),
              (0.4, 0.03, 0.03), (0.75, 0.75, 0.72), (0.12, 0.12, 0.13), (0.45, 0.38, 0.28)]


def side_profile(kind):
    if kind == "suv":
        L_, W_ = 4.75, 1.92
        body = [(-2.37, 0.38), (-2.37, 1.02), (-2.2, 1.12), (-1.9, 1.16), (1.15, 1.12), (2.15, 0.98), (2.37, 0.8), (2.37, 0.38)]
        cabin = [(-2.05, 1.14), (-1.9, 1.74), (0.75, 1.76), (1.3, 1.12)]
    elif kind == "hatch":
        L_, W_ = 4.15, 1.8
        body = [(-2.07, 0.33), (-2.07, 0.95), (-1.95, 1.0), (1.0, 0.98), (1.9, 0.85), (2.07, 0.65), (2.07, 0.33)]
        cabin = [(-1.95, 0.99), (-1.75, 1.47), (0.45, 1.5), (1.05, 0.97)]
    else:  # sedan / ev
        L_, W_ = 4.85, 1.84
        body = [(-2.42, 0.33), (-2.42, 0.86), (-2.15, 0.98), (-1.45, 1.0), (0.9, 0.98), (2.15, 0.82), (2.42, 0.62), (2.42, 0.33)]
        cabin = [(-1.5, 0.99), (-0.85, 1.43), (0.35, 1.45), (0.95, 0.97)]
    return L_, W_, body, cabin


def extrude_profile(name, prof, half_w, mat, cname, taper_top=1.0, zcut=None):
    n = len(prof)
    verts = []
    for side in (-1, 1):
        for (x, z) in prof:
            w = half_w
            if taper_top != 1.0:
                zmin = min(p[1] for p in prof); zmax = max(p[1] for p in prof)
                t = (z - zmin) / (zmax - zmin + 1e-9)
                w = half_w * (1 - (1 - taper_top) * t)
            verts.append((x, side * w, z))
    faces = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, n + j, n + i))
    return mesh_obj(name, verts, faces, [mat], cname)


def make_car(name, kind, color, x, y, heading, night=False, lights_on=False):
    L_, W_, body, cabin = side_profile(kind)
    paint = principled(f"paint_{name}", color, rough=0.28, metal=0.55 if sum(color) > 0.3 else 0.2, coat=1.0, coat_rough=0.03)
    parts = []
    b = extrude_profile(name + "_body", body, W_ / 2, paint, "vehicles")
    m = b.modifiers.new("bev", "BEVEL"); m.width = 0.12; m.segments = 4; m.limit_method = "ANGLE"
    for p in b.data.polygons:
        p.use_smooth = True
    parts.append(b)
    c = extrude_profile(name + "_cabin", cabin, W_ / 2 - 0.06, MM["glass_dark"], "vehicles", taper_top=0.82)
    m = c.modifiers.new("bev", "BEVEL"); m.width = 0.08; m.segments = 3; m.limit_method = "ANGLE"
    for p in c.data.polygons:
        p.use_smooth = True
    parts.append(c)
    # roof panel in paint colour over glass
    rx0, rz0 = cabin[1]; rx1, rz1 = cabin[2]
    r = box(name + "_roof", rx0 + 0.08, -(W_ / 2 - 0.2), rz0 - 0.02, rx1 - 0.05, (W_ / 2 - 0.2), rz1 + 0.025, paint, "vehicles", bevel=0.04)
    parts.append(r)
    wr = 0.34 if kind != "suv" else 0.38
    ax = L_ / 2 - 0.85
    for sx in (-ax, ax):
        for sy in (-W_ / 2 + 0.12, W_ / 2 - 0.12):
            bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=wr, depth=0.24, location=(sx, sy, wr), rotation=(math.pi / 2, 0, 0))
            t = bpy.context.active_object; t.name = name + "_tire"; t.data.materials.append(MM["rubber"])
            for cc in t.users_collection:
                cc.objects.unlink(t)
            link(t, "vehicles"); parts.append(t)
            bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=wr * 0.62, depth=0.245, location=(sx, sy, wr), rotation=(math.pi / 2, 0, 0))
            rr = bpy.context.active_object; rr.name = name + "_rim"; rr.data.materials.append(MM["rim"])
            for cc in rr.users_collection:
                cc.objects.unlink(rr)
            link(rr, "vehicles"); parts.append(rr)
    # lights
    hx = L_ / 2 + 0.005
    zl = body[-2][1] - 0.08 if kind != "hatch" else 0.72
    for sy in (-W_ / 2 + 0.3, W_ / 2 - 0.3):
        h = box(name + "_hl", hx - 0.05, sy - 0.22, zl - 0.06, hx, sy + 0.22, zl + 0.04, MM["head"], "vehicles"); parts.append(h)
        t = box(name + "_tl", -hx, sy - 0.25, 0.82, -hx + 0.05, sy + 0.25, 0.92, MM["tail"], "vehicles"); parts.append(t)
    # parent all to an empty
    e = bpy.data.objects.new(name, None)
    link(e, "vehicles")
    for p in parts:
        p.parent = e
    e.location = (x, y, 0.03)
    e.rotation_euler = (0, 0, math.radians(heading))
    return e


def build_vehicles(night=False):
    rnd = random.Random(3)
    for i, q in enumerate(L["cars"]["queue"]):
        make_car(f"q{i}", q["kind"], CAR_COLORS[i % len(CAR_COLORS)], q["x"], q["y"], q["heading"], night, lights_on=night)
    stalls = {s["id"]: s for s in L["parking"]["stalls"]}
    for i, (sid, kind) in enumerate(L["cars"]["parked"]):
        s = stalls[sid]
        make_car(f"p{i}", "sedan" if kind == "ev" else kind, CAR_COLORS[(i * 3 + 2) % len(CAR_COLORS)], s["x"], s["y"],
                 s["heading"] + rnd.choice([0, 180]) * 0, night)
    hw = L["highway"]
    # highway traffic: westbound (north carriageway) heading 180, eastbound heading 0
    nl1 = sum(hw["north"]["lane1"]) / 2; nl2 = sum(hw["north"]["lane2"]) / 2
    sl1 = sum(hw["south"]["lane1"]) / 2; sl2 = sum(hw["south"]["lane2"]) / 2
    traffic = [(120, nl1, 180, "sedan"), (-35, nl1, 180, "suv"), (78, nl2, 180, "sedan"), (-120, nl2, 180, "hatch"),
               (10, sl1, 0, "suv"), (95, sl1, 0, "sedan"), (-70, sl2, 0, "sedan"), (160, sl2, 0, "hatch"),
               (95.0, (L["aux"]["y_inner"] + L["aux"]["y_outer"]) / 2, 180, "sedan")]
    for i, (x, y, h, k) in enumerate(traffic):
        make_car(f"h{i}", k, CAR_COLORS[(i * 5 + 1) % len(CAR_COLORS)], x, y, h, night, lights_on=night)


# ======================================================================================
# world, cameras, render settings
# ======================================================================================
def setup_world(mode):
    sc = bpy.context.scene
    w = bpy.data.worlds.new("world"); sc.world = w; w.use_nodes = True
    nt = w.node_tree
    bg = nt.nodes["Background"]
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    tc = nt.nodes.new("ShaderNodeTexCoord"); mp = nt.nodes.new("ShaderNodeMapping")
    nt.links.new(tc.outputs["Generated"], mp.inputs[0]); nt.links.new(mp.outputs[0], env.inputs[0])
    nt.links.new(env.outputs[0], bg.inputs[0])
    hd = {"day": "kloofendal_48d_partly_cloudy_puresky", "golden": "qwantani_late_afternoon_puresky",
          "dusk": "qwantani_dusk_2_puresky", "night": "qwantani_dusk_2_puresky", "clear": "kloofendal_43d_clear_puresky"}[mode]
    env.image = bpy.data.images.load(f"{A}/hdri/{hd}_4k.hdr", check_existing=True)
    strength = {"day": 1.0, "golden": 1.1, "dusk": 0.22, "night": 0.05, "clear": 1.0}[mode]
    bg.inputs["Strength"].default_value = strength
    mp.inputs["Rotation"].default_value = (0, 0, math.radians({"day": 210, "golden": 120, "dusk": 300, "night": 300, "clear": 200}[mode]))
    if mode in ("day", "golden", "clear"):
        sd = bpy.data.lights.new("sun", "SUN")
        sd.energy = {"day": 4.2, "golden": 3.0, "clear": 4.6}[mode]
        sd.angle = math.radians(0.6)
        sd.color = (1.0, 0.96, 0.9) if mode != "golden" else (1.0, 0.78, 0.55)
        so = bpy.data.objects.new("sun", sd)
        az, el = {"day": (150, 46), "golden": (255, 13), "clear": (140, 52)}[mode]
        # azimuth measured clockwise from north (+y); light points opposite to sun position
        azr, elr = math.radians(az), math.radians(el)
        sun_dir = Vector((math.sin(azr) * math.cos(elr), math.cos(azr) * math.cos(elr), math.sin(elr)))
        so.rotation_euler = (-sun_dir).to_track_quat("-Z", "Y").to_euler()
        link(so, "lights_exterior")


def add_camera(name, loc, target, lens=35, ortho=None, shift_y=0.0):
    cd = bpy.data.cameras.new(name)
    cd.lens = lens
    cd.sensor_width = 36
    cd.clip_end = 8000
    cd.shift_y = shift_y
    if ortho:
        cd.type = "ORTHO"; cd.ortho_scale = ortho
    co = bpy.data.objects.new(name, cd)
    co.location = loc
    look_at(co, target)
    link(co, "cameras")
    return co


def build_cameras():
    cams = {}
    cams["hero"] = add_camera("cam_hero", (66.5, 3.2, 1.7), (36.0, 25.5, 4.4), lens=22, shift_y=0.08)
    cams["hero_wide"] = add_camera("cam_hero_wide", (84.0, -8.6, 1.7), (38.0, 24.0, 4.6), lens=24, shift_y=0.1)
    cams["aerial"] = add_camera("cam_aerial", (104.0, -58.0, 54.0), (36.0, 19.0, 0.0), lens=30)
    cams["aerial_nw"] = add_camera("cam_aerial_nw", (-20.0, 78.0, 38.0), (38.0, 22.0, 0.0), lens=30)
    cams["top"] = add_camera("cam_top", (37.0, 10.0, 300.0), (37.0, 10.0, 0.0), ortho=112)
    cams["drivethru"] = add_camera("cam_drivethru", (52.0, 36.9, 1.45), (32.0, 33.6, 2.4), lens=22)
    cams["terrace"] = add_camera("cam_terrace", (13.4, 16.6, 1.65), (34.0, 27.0, 3.4), lens=22)
    cams["approach"] = add_camera("cam_approach", (230.0, -10.4, 1.25), (55.0, 8.0, 5.0), lens=50)
    cams["plaza"] = add_camera("cam_plaza", (48.8, 10.6, 1.65), (37.5, 25.0, 3.6), lens=22)
    cams["cutaway"] = add_camera("cam_cutaway", (52.0, 8.0, 26.0), (33.5, 28.5, 0.5), lens=38)
    cams["interior"] = add_camera("cam_interior", (42.3, 24.6, 1.6), (33.0, 30.5, 1.6), lens=20)
    return cams


def render_settings(samples=128, res=(1920, 1080), pct=100):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = samples
    sc.cycles.use_adaptive_sampling = True
    sc.cycles.adaptive_threshold = 0.02
    sc.cycles.use_denoising = True
    try:
        sc.cycles.denoiser = "OPENIMAGEDENOISE"
    except Exception:
        pass
    sc.cycles.max_bounces = 8
    sc.cycles.glossy_bounces = 4
    sc.cycles.transmission_bounces = 8
    sc.cycles.transparent_max_bounces = 16
    sc.cycles.caustics_reflective = False
    sc.cycles.caustics_refractive = False
    sc.cycles.sample_clamp_indirect = 8.0
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = pct
    sc.render.film_transparent = False
    sc.render.use_persistent_data = True
    sc.render.threads_mode = "FIXED"
    sc.render.threads = os.cpu_count() or 4
    sc.view_settings.view_transform = "AgX"
    for look in ("AgX - Medium High Contrast", "AgX - Base Contrast", "None"):
        try:
            sc.view_settings.look = look
            break
        except Exception:
            continue
    sc.render.image_settings.file_format = "PNG"
    sc.render.image_settings.color_depth = "8"


def set_light_mode(night):
    """Toggle emission strengths of LED/interior/vehicle light materials."""
    MM["led_warm"].node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 18.0 if night else 0.0
    MM["interior_glow"].node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 3.0 if night else 0.0
    # warm self-illumination of interior plaster at night (bounce light from fittings)
    pl = MM["plaster"].node_tree.nodes["Principled BSDF"]
    pl.inputs["Emission Color"].default_value = (1.0, 0.8, 0.6, 1)
    pl.inputs["Emission Strength"].default_value = 0.35 if night else 0.0
    MM["tail"].node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 6.0 if night else 0.0
    MM["head"].node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 25.0 if night else 0.0


def build(mode="day", quality="final"):
    reset()
    MATS.clear(); TEMPLATES.clear(); COLLS.clear()
    night = mode in ("dusk", "night")
    set_haze(night)
    M = init_materials()
    MM.clear(); MM.update(M)
    build_terrain(M)
    build_highway(M)
    build_site(M)
    build_markings(M)
    build_building(M, night)
    build_vegetation(M, quality)
    build_furniture(M)
    build_site_lights(night)
    build_vehicles(night)
    setup_world(mode)
    set_light_mode(night)
    cams = build_cameras()
    return cams


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    mode = argv[argv.index("--mode") + 1] if "--mode" in argv else "day"
    cams = build(mode, "preview")
    if "--save" in argv:
        bpy.ops.wm.save_as_mainfile(filepath=argv[argv.index("--save") + 1])
