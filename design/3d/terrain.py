"""
terrain.py -- Kotayk-plateau farmland around the highway-side drive-thru site
=============================================================================

Interface
---------
    import terrain
    info = terrain.build_landscape(link_fn, terrain_height_fn, site_center=(37, 22), exclude_fn=None,
                                   seed=11, quality="final", r_in=150.0, r_out=1500.0,
                                   terrain_obj=None, haze_emit=0.35)

* ``link_fn(ob, collection_name)``  links every created object (pass build_scene.link); everything goes to
  the "landscape" collection.  ``terrain_height_fn(x, y) -> z`` is build_scene.terrain_height.
* ``exclude_fn(x, y) -> bool``  True where nothing may be placed.  Default:
  ``abs(y + 18) < 45 or (-10 < x < 85 and -10 < y < 55)`` (highway corridor + site).
* ``quality`` "final" or "preview" (preview halves trees / rocks); ``seed`` changes the layout.
* ``terrain_obj`` the terrain mesh to drape on (default: the object named "terrain");
  ``haze_emit`` must match build_scene.HAZE_EMIT[0] (0.35).
* returns {"objects": {fields, tracks, trees, rocks, buildings, poles, wires},
           "faces": {... per layer ..., "total"}, "exact_drape": bool, "villages", "farm", "fields", "stats"}.
  Call it after build_terrain(); it takes ~2.5 s and adds ~210k faces with the default seed.

What it builds (rolling highland steppe at ~1,700 m, mountains to the north)
---------------------------------------------------------------------------
* Agricultural patchwork in the r_in..r_out ring: post-Soviet farm blocks on jittered grids whose
  orientation and block size change per angular sector, subdivided into long private strips or large
  collective fields (ripe wheat & barley with tramlines, stubble with harvest swaths, ploughed and
  harrowed soil, potato rows, alfalfa, dry fallow), 6 m gaps between blocks, ~0.8 m between strips.
  Parcels are clipped convexly to their sector, to the inner ring and away from excluded ground,
  skipped on slopes above ~17 deg (block median) and where terrain_height is discontinuous.
* Draping: fields and tracks are cut out of the *rendered* terrain mesh -- its rectilinear grid is read
  from the terrain object and every grid quad is split along the same v0-v2 diagonal Blender uses --
  then lifted so they sit +0.05 m above terrain_height (+0.09 m for tracks).  No z-fighting and no
  floating, whatever the terrain resolution.  If no grid terrain is found it falls back to sampling
  terrain_height_fn on its own 10 m lattice and lifts parcels 0.25 m (exact_drape = False).
* One shared field material driven by per-face attributes (colour with per-parcel hue/value jitter,
  furrow direction, row/swath/tramline spacing and contrast, random); multi-scale mottling plus the
  aerial_grass_rock texture for soil variation; furrows fade out with camera distance (70..260 m,
  swaths 0.9..2.4 km) to avoid moire; identical aerial-perspective haze to build_scene.mat_steppe
  (Camera View Distance 250..4200 m -> 0..0.78 mix to (0.45, 0.55, 0.68) + haze emission).
* Dirt tracks along block edges, main tracks from the highway frontage to every settlement, poplar /
  elm windbreak rows, basalt outcrops with lichen and loose boulders on the remaining steppe and
  slopes, 3-4 villages at 450-1150 m (tuff / plaster / stone houses, gable or hip roofs in rusty, green
  or galvanised metal, terracotta or slate, sheds, streets, gardens, apricot/apple orchards), a kolkhoz
  barn complex at 420-850 m (some roofless ruins) and a 10 kV line of concrete poles with sagging
  conductors along one main track.
"""
import bpy
import bmesh
import math
import os
import random
import bisect
from mathutils import Vector, noise

HAZE_COL = (0.45, 0.55, 0.68)
HAZE_EMIT_COL = (0.55, 0.66, 0.82)
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

CROPS = {
    #            colour (linear albedo)   row_sp row_c  swath_sp swath_c tram  weight
    "wheat":    ((0.215, 0.148, 0.048),   0.25, 0.00,  0.0,     0.00,   1.0,  20),
    "barley":   ((0.225, 0.178, 0.080),   0.25, 0.00,  0.0,     0.00,   1.0,  10),
    "stubble":  ((0.230, 0.186, 0.112),   0.25, 0.04,  5.5,     0.07,   0.0,  18),
    "ploughed": ((0.066, 0.055, 0.042),   0.75, 0.14,  0.0,     0.00,   0.0,  14),
    "harrowed": ((0.115, 0.092, 0.068),   0.45, 0.12,  12.0,    0.05,   0.0,  8),
    "potato":   ((0.050, 0.070, 0.030),   0.75, 0.18,  0.0,     0.00,   0.0,  8),
    "alfalfa":  ((0.074, 0.094, 0.040),   0.25, 0.00,  6.0,     0.07,   0.0,  9),
    "fallow":   ((0.140, 0.128, 0.078),   0.25, 0.00,  0.0,     0.00,   0.0,  13),
}


# ======================================================================================
# geometry helpers
# ======================================================================================
def _cross(ax, ay, bx, by):
    return ax * by - ay * bx


def _area(poly):
    s = 0.0
    for i in range(len(poly)):
        x0, y0 = poly[i][0], poly[i][1]
        x1, y1 = poly[(i + 1) % len(poly)][0], poly[(i + 1) % len(poly)][1]
        s += x0 * y1 - x1 * y0
    return 0.5 * s


def _ccw(poly):
    return poly if _area(poly) > 0 else poly[::-1]


def _inside_convex(poly, x, y):
    n = len(poly)
    for i in range(n):
        ax, ay = poly[i][0], poly[i][1]
        bx, by = poly[(i + 1) % n][0], poly[(i + 1) % n][1]
        if _cross(bx - ax, by - ay, x - ax, y - ay) < -1e-9:
            return False
    return True


def _clip(subject, clip):
    """Sutherland-Hodgman: subject = [(x, y, z)], clip = convex CCW [(x, y)]."""
    out = subject
    n = len(clip)
    for i in range(n):
        if not out:
            break
        ax, ay = clip[i]
        bx, by = clip[(i + 1) % n]
        ex, ey = bx - ax, by - ay
        inp = out
        out = []
        m = len(inp)
        for k in range(m):
            p = inp[k]
            q = inp[(k + 1) % m]
            dp = _cross(ex, ey, p[0] - ax, p[1] - ay)
            dq = _cross(ex, ey, q[0] - ax, q[1] - ay)
            if dp >= 0:
                out.append(p)
            if (dp >= 0) != (dq >= 0):
                t = dp / (dp - dq)
                out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]), p[2] + t * (q[2] - p[2])))
    return out


def _inset(poly, d):
    """Inset a convex CCW polygon by d (returns None if it collapses)."""
    n = len(poly)
    lines = []
    for i in range(n):
        ax, ay = poly[i]
        bx, by = poly[(i + 1) % n]
        ex, ey = bx - ax, by - ay
        ln = math.hypot(ex, ey)
        if ln < 1e-6:
            return None
        nx, ny = -ey / ln, ex / ln
        lines.append((ax + nx * d, ay + ny * d, ex, ey))
    out = []
    for i in range(n):
        x0, y0, e0x, e0y = lines[i - 1]
        x1, y1, e1x, e1y = lines[i]
        den = _cross(e0x, e0y, e1x, e1y)
        if abs(den) < 1e-9:
            out.append((x1, y1))
            continue
        t = _cross(x1 - x0, y1 - y0, e1x, e1y) / den
        out.append((x0 + e0x * t, y0 + e0y * t))
    if _area(out) < 0.05 * _area(poly):
        return None
    return out


def _lerp2(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


# ======================================================================================
# ground: exact height of the rendered terrain mesh
# ======================================================================================
class Ground:
    def __init__(self, fn, obj=None, fallback_extent=1800.0, center=(37.0, 22.0)):
        self.fn = fn
        self.exact = False
        ob = obj if obj is not None else bpy.data.objects.get("terrain")
        if ob is not None and ob.type == "MESH" and self._detect(ob):
            self.exact = True
        else:
            # own lattice sampling the analytic function (fields then float slightly more)
            sp = 10.0
            n = int(2 * fallback_extent / sp)
            self.xs = [center[0] - fallback_extent + i * sp for i in range(n + 1)]
            self.ys = [center[1] - fallback_extent + j * sp for j in range(n + 1)]
            self.nx = len(self.xs)
            self.Z = [fn(x, y) for y in self.ys for x in self.xs]
            self.dz = 0.0
        # offset between the analytic height and the mesh (build_scene puts the mesh 6 cm below)
        if self.exact:
            r = random.Random(3)
            ds = []
            for _ in range(60):
                i = r.randrange(self.nx); j = r.randrange(len(self.ys))
                ds.append(fn(self.xs[i], self.ys[j]) - self.Z[j * self.nx + i])
            ds.sort()
            self.dz = ds[len(ds) // 2]

    def _detect(self, ob):
        me = ob.data
        n = len(me.vertices)
        if n < 16:
            return False
        if any(abs(ob.matrix_world[i][j] - (1.0 if i == j else 0.0)) > 1e-6 for i in range(4) for j in range(4)):
            return False
        co = [0.0] * (3 * n)
        me.vertices.foreach_get("co", co)
        y0 = co[1]
        nx = 1
        while nx < n and abs(co[3 * nx + 1] - y0) < 1e-6:
            nx += 1
        if n % nx:
            return False
        ny = n // nx
        xs = co[0:3 * nx:3]
        ys = [co[3 * j * nx + 1] for j in range(ny)]
        if any(xs[i + 1] <= xs[i] for i in range(nx - 1)) or any(ys[j + 1] <= ys[j] for j in range(ny - 1)):
            return False
        r = random.Random(1)
        for _ in range(200):
            i, j = r.randrange(nx), r.randrange(ny)
            k = 3 * (j * nx + i)
            if abs(co[k] - xs[i]) > 1e-4 or abs(co[k + 1] - ys[j]) > 1e-4:
                return False
        if len(me.polygons) != (nx - 1) * (ny - 1):
            return False
        p = me.polygons[0]
        if tuple(p.vertices) != (0, 1, nx + 1, nx):
            return False
        self.xs, self.ys, self.nx = xs, ys, nx
        self.Z = co[2::3]
        return True

    def cell(self, x, y):
        i = min(max(bisect.bisect_right(self.xs, x) - 1, 0), len(self.xs) - 2)
        j = min(max(bisect.bisect_right(self.ys, y) - 1, 0), len(self.ys) - 2)
        return i, j

    def node(self, i, j):
        return self.Z[j * self.nx + i]

    def z(self, x, y):
        """Height of the terrain *mesh* surface (quads split along the v0-v2 diagonal)."""
        i, j = self.cell(x, y)
        x0, x1 = self.xs[i], self.xs[i + 1]
        y0, y1 = self.ys[j], self.ys[j + 1]
        u = min(max((x - x0) / (x1 - x0), 0.0), 1.0)
        v = min(max((y - y0) / (y1 - y0), 0.0), 1.0)
        z00, z10, z11, z01 = self.node(i, j), self.node(i + 1, j), self.node(i + 1, j + 1), self.node(i, j + 1)
        if u >= v:
            return z00 + u * (z10 - z00) + v * (z11 - z10)
        return z00 + v * (z01 - z00) + u * (z11 - z01)

    def steep(self, poly, limit=0.4, jump=0.45):
        """True if the terrain under the polygon contains a *discontinuity* of terrain_height (a mesh
        edge steeper than `limit` whose analytic height also jumps by > `jump` m across 0.6 m), e.g.
        build_scene's step at y = 60 east/west of the site.  Ordinary steep slopes pass."""
        xs_, ys_ = [p[0] for p in poly], [p[1] for p in poly]
        i0, j0 = self.cell(min(xs_), min(ys_))
        i1, j1 = self.cell(max(xs_), max(ys_))
        f = self.fn
        for j in range(j0, j1 + 1):
            for i in range(i0, i1 + 1):
                z = self.node(i, j)
                x0, y0 = self.xs[i], self.ys[j]
                if abs(self.node(i + 1, j) - z) > limit * (self.xs[i + 1] - x0):
                    for t in (0.25, 0.5, 0.75):
                        xm = x0 + t * (self.xs[i + 1] - x0)
                        if abs(f(xm + 0.3, y0) - f(xm - 0.3, y0)) > jump:
                            return True
                if abs(self.node(i, j + 1) - z) > limit * (self.ys[j + 1] - y0):
                    for t in (0.25, 0.5, 0.75):
                        ym = y0 + t * (self.ys[j + 1] - y0)
                        if abs(f(x0, ym + 0.3) - f(x0, ym - 0.3)) > jump:
                            return True
        return False

    def slope(self, x, y, d=15.0):
        f = self.fn
        gx = (f(x + d, y) - f(x - d, y)) / (2 * d)
        gy = (f(x, y + d) - f(x, y - d)) / (2 * d)
        return math.hypot(gx, gy)


class Draper:
    """Accumulates polygons cut out of the terrain lattice into one mesh with per-face data."""

    def __init__(self, ground, lift):
        self.g = ground
        self.lift = lift
        self.verts = []
        self.vidx = {}
        self.faces = []
        self.fdata = []

    def _v(self, key, x, y, z):
        k = self.vidx.get(key)
        if k is None:
            k = len(self.verts)
            self.vidx[key] = k
            self.verts.append((x, y, z))
        return k

    def add(self, poly, data, lift=None, share=True):
        """poly: convex polygon [(x, y)] (any winding)."""
        g = self.g
        lift = self.lift if lift is None else lift
        poly = _ccw([(p[0], p[1]) for p in poly])
        xs_, ys_ = [p[0] for p in poly], [p[1] for p in poly]
        i0, j0 = g.cell(min(xs_), min(ys_))
        i1, j1 = g.cell(max(xs_), max(ys_))
        tag = len(self.faces) if not share else 0
        ins = {}

        def inside(i, j):
            k = (i, j)
            r = ins.get(k)
            if r is None:
                r = _inside_convex(poly, g.xs[i], g.ys[j])
                ins[k] = r
            return r

        nf = 0
        for j in range(j0, j1 + 1):
            for i in range(i0, i1 + 1):
                c = [(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]
                fl = [inside(a, b) for a, b in c]
                P = [(g.xs[a], g.ys[b], g.node(a, b) + lift) for a, b in c]
                if all(fl):
                    f = tuple(self._v(("n", a, b, tag, lift), *p) for (a, b), p in zip(c, P))
                    self.faces.append(f); self.fdata.append(data); nf += 1
                    continue
                for tri in ((P[0], P[1], P[2]), (P[0], P[2], P[3])):
                    cp = _clip(list(tri), poly)
                    if len(cp) < 3 or abs(_area(cp)) < 1e-4:
                        continue
                    f = tuple(self._v(("p", round(p[0] * 500), round(p[1] * 500), tag, lift), *p) for p in cp)
                    if len(set(f)) < 3:
                        continue
                    # drop consecutive duplicates
                    ff = [f[0]]
                    for q in f[1:]:
                        if q != ff[-1]:
                            ff.append(q)
                    if ff[-1] == ff[0]:
                        ff.pop()
                    if len(ff) >= 3:
                        self.faces.append(tuple(ff)); self.fdata.append(data); nf += 1
        return nf

    def build(self, name, mat, attrs, link_fn, cname):
        me = bpy.data.meshes.new(name)
        me.from_pydata(self.verts, [], self.faces)
        me.update()
        me.materials.append(mat)
        n = len(me.polygons)
        for aname, (atype, getter, width) in attrs.items():
            a = me.attributes.new(aname, atype, "FACE")
            flat = []
            for d in self.fdata[:n]:
                v = getter(d)
                flat.extend(v)
            key = "color" if atype == "FLOAT_COLOR" else ("vector" if atype == "FLOAT_VECTOR" else "value")
            a.data.foreach_set(key, flat)
        for p in me.polygons:
            p.use_smooth = True
        ob = bpy.data.objects.new(name, me)
        link_fn(ob, cname)
        return ob


# ======================================================================================
# materials
# ======================================================================================
def _haze(nt, col_out, bsdf, haze_emit):
    N, Lk = nt.nodes, nt.links
    cam = N.new("ShaderNodeCameraData")
    hz = N.new("ShaderNodeMapRange")
    hz.inputs[1].default_value = 250.0; hz.inputs[2].default_value = 4200.0
    hz.inputs[3].default_value = 0.0; hz.inputs[4].default_value = 0.78
    Lk.new(cam.outputs["View Distance"], hz.inputs[0])
    hm = N.new("ShaderNodeMix"); hm.data_type = "RGBA"
    Lk.new(hz.outputs[0], hm.inputs[0]); Lk.new(col_out, hm.inputs[6]); hm.inputs[7].default_value = (*HAZE_COL, 1)
    Lk.new(hm.outputs[2], bsdf.inputs["Base Color"])
    em = N.new("ShaderNodeMath"); em.operation = "MULTIPLY"; em.inputs[1].default_value = haze_emit
    Lk.new(hz.outputs[0], em.inputs[0])
    bsdf.inputs["Emission Color"].default_value = (*HAZE_EMIT_COL, 1)
    Lk.new(em.outputs[0], bsdf.inputs["Emission Strength"])
    return cam


def _new_mat(name):
    m = bpy.data.materials.new(name)          # Blender suffixes the name if it already exists
    m.use_nodes = True
    return m


def _attr(N, name):
    a = N.new("ShaderNodeAttribute"); a.attribute_type = "GEOMETRY"; a.attribute_name = name
    return a


def _math(N, Lk, op, a, b=None, clamp=False):
    m = N.new("ShaderNodeMath"); m.operation = op; m.use_clamp = clamp
    if isinstance(a, (int, float)):
        m.inputs[0].default_value = a
    else:
        Lk.new(a, m.inputs[0])
    if b is not None:
        if isinstance(b, (int, float)):
            m.inputs[1].default_value = b
        else:
            Lk.new(b, m.inputs[1])
    return m.outputs[0]


def _maprange(N, Lk, v, a, b, c, d):
    m = N.new("ShaderNodeMapRange")
    m.inputs[1].default_value = a; m.inputs[2].default_value = b
    m.inputs[3].default_value = c; m.inputs[4].default_value = d
    Lk.new(v, m.inputs[0])
    return m.outputs[0]


def _img(N, Lk, vec_out, scale):
    tex = os.path.join(ASSETS, "tex", "aerial_grass_rock", "aerial_grass_rock_Diffuse.jpg")
    if not os.path.exists(tex):
        return None
    mp = N.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value = (1 / scale,) * 3
    Lk.new(vec_out, mp.inputs[0])
    it = N.new("ShaderNodeTexImage")
    it.image = bpy.data.images.load(tex, check_existing=True)
    it.image.colorspace_settings.name = "sRGB"
    it.projection = "FLAT"
    Lk.new(mp.outputs[0], it.inputs[0])
    bw = N.new("ShaderNodeRGBToBW"); Lk.new(it.outputs[0], bw.inputs[0])
    return bw.outputs[0]


def mat_fields(haze_emit=0.35):
    m = _new_mat("land_fields")
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    b = N["Principled BSDF"]
    geo = N.new("ShaderNodeNewGeometry")
    cam = N.new("ShaderNodeCameraData")
    dist = cam.outputs["View Distance"]
    fcol = _attr(N, "fcol")
    fdir = _attr(N, "fdir")         # (cos, sin, row spacing)
    fpar = _attr(N, "fpar")         # (row contrast, swath spacing, swath contrast)
    fpr2 = _attr(N, "fpr2")         # (tramline flag, random, unused)
    dot = N.new("ShaderNodeVectorMath"); dot.operation = "DOT_PRODUCT"
    sxy = N.new("ShaderNodeSeparateXYZ"); Lk.new(fdir.outputs["Vector"], sxy.inputs[0])
    cmb = N.new("ShaderNodeCombineXYZ"); Lk.new(sxy.outputs[0], cmb.inputs[0]); Lk.new(sxy.outputs[1], cmb.inputs[1])
    Lk.new(geo.outputs["Position"], dot.inputs[0]); Lk.new(cmb.outputs[0], dot.inputs[1])
    u = dot.outputs["Value"]
    sp = N.new("ShaderNodeSeparateXYZ"); Lk.new(fpar.outputs["Vector"], sp.inputs[0])
    s2 = N.new("ShaderNodeSeparateXYZ"); Lk.new(fpr2.outputs["Vector"], s2.inputs[0])
    # crop rows / furrows (fade 120 -> 380 m)
    rows = _math(N, Lk, "SINE", _math(N, Lk, "MULTIPLY", _math(N, Lk, "DIVIDE", u, sxy.outputs[2]), 2 * math.pi))
    rows = _math(N, Lk, "MULTIPLY", rows, sp.outputs[0])
    rows = _math(N, Lk, "MULTIPLY", rows, _maprange(N, Lk, dist, 70.0, 260.0, 1.0, 0.0))
    # harvest swaths (fade 900 -> 2400 m)
    sw_sp = _math(N, Lk, "MAXIMUM", sp.outputs[1], 0.5)
    sw = _math(N, Lk, "SINE", _math(N, Lk, "MULTIPLY", _math(N, Lk, "DIVIDE", u, sw_sp), 2 * math.pi))
    sw = _math(N, Lk, "MULTIPLY", sw, sp.outputs[2])
    sw = _math(N, Lk, "MULTIPLY", sw, _maprange(N, Lk, dist, 900.0, 2400.0, 1.0, 0.0))
    # tramlines every 18 m (dark 0.5 m pair), fade 700 -> 1600 m
    fr = _math(N, Lk, "FRACT", _math(N, Lk, "DIVIDE", u, 18.0))
    tl = _math(N, Lk, "LESS_THAN", fr, 0.035)
    tl = _math(N, Lk, "MULTIPLY", tl, s2.outputs[0])
    tl = _math(N, Lk, "MULTIPLY", tl, _maprange(N, Lk, dist, 700.0, 1600.0, -0.22, 0.0))
    # mottling
    tc = N.new("ShaderNodeTexCoord")
    nz1 = N.new("ShaderNodeTexNoise"); nz1.inputs["Scale"].default_value = 0.02; nz1.inputs["Detail"].default_value = 5
    Lk.new(geo.outputs["Position"], nz1.inputs["Vector"])
    nz3 = N.new("ShaderNodeTexNoise"); nz3.inputs["Scale"].default_value = 0.09; nz3.inputs["Detail"].default_value = 4
    nz3.inputs["Roughness"].default_value = 0.6
    Lk.new(geo.outputs["Position"], nz3.inputs["Vector"])
    nz2 = N.new("ShaderNodeTexNoise"); nz2.inputs["Scale"].default_value = 0.45; nz2.inputs["Detail"].default_value = 3
    Lk.new(geo.outputs["Position"], nz2.inputs["Vector"])
    m1 = _maprange(N, Lk, nz1.outputs["Fac"], 0.3, 0.7, -0.20, 0.20)
    m3 = _maprange(N, Lk, nz3.outputs["Fac"], 0.3, 0.7, -0.12, 0.12)
    m2 = _maprange(N, Lk, nz2.outputs["Fac"], 0.3, 0.7, -0.07, 0.07)
    # per-field brightness offset from the random attribute
    rf = _maprange(N, Lk, s2.outputs[1], 0.0, 1.0, -0.06, 0.06)
    sw = _math(N, Lk, "MULTIPLY", sw, _maprange(N, Lk, nz3.outputs["Fac"], 0.35, 0.65, 0.2, 1.3))
    val = _math(N, Lk, "ADD", rows, sw)
    val = _math(N, Lk, "ADD", val, tl)
    val = _math(N, Lk, "ADD", val, m1)
    val = _math(N, Lk, "ADD", val, m3)
    val = _math(N, Lk, "ADD", val, m2)
    val = _math(N, Lk, "ADD", val, rf)
    val = _math(N, Lk, "ADD", val, 1.0)
    bwi = _img(N, Lk, geo.outputs["Position"], 23.0)
    if bwi is not None:
        tx = _maprange(N, Lk, bwi, 0.0, 0.6, 0.78, 1.22)
        val = _math(N, Lk, "MULTIPLY", val, tx)
    cv = N.new("ShaderNodeCombineColor")
    for k in range(3):
        Lk.new(val, cv.inputs[k])
    mul = N.new("ShaderNodeMix"); mul.data_type = "RGBA"; mul.blend_type = "MULTIPLY"; mul.inputs[0].default_value = 1.0
    Lk.new(fcol.outputs["Color"], mul.inputs[6]); Lk.new(cv.outputs[0], mul.inputs[7])
    _haze(nt, mul.outputs[2], b, haze_emit)
    b.inputs["Roughness"].default_value = 0.95
    b.inputs["Specular IOR Level"].default_value = 0.25
    # a little relief on furrows for low sun
    bp = N.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = 0.25; bp.inputs["Distance"].default_value = 0.05
    Lk.new(rows, bp.inputs["Height"]); Lk.new(bp.outputs[0], b.inputs["Normal"])
    m.diffuse_color = (0.3, 0.25, 0.15, 1)
    return m


def mat_tracks(haze_emit=0.35):
    m = _new_mat("land_tracks")
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    b = N["Principled BSDF"]
    geo = N.new("ShaderNodeNewGeometry")
    nz = N.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 0.4; nz.inputs["Detail"].default_value = 6
    Lk.new(geo.outputs["Position"], nz.inputs["Vector"])
    cr = N.new("ShaderNodeValToRGB")
    cr.color_ramp.elements[0].position = 0.35; cr.color_ramp.elements[0].color = (0.115, 0.095, 0.072, 1)
    cr.color_ramp.elements[1].position = 0.7; cr.color_ramp.elements[1].color = (0.175, 0.150, 0.115, 1)
    Lk.new(nz.outputs["Fac"], cr.inputs[0])
    _haze(nt, cr.outputs[0], b, haze_emit)
    b.inputs["Roughness"].default_value = 0.95
    m.diffuse_color = (0.33, 0.28, 0.2, 1)
    return m


def _attr_mat(name, attr, rough, haze_emit, bump_scale=None, bump_str=0.0, noise_amt=0.15, lichen=False,
              trans=0.0):
    m = _new_mat(name)
    nt = m.node_tree
    N, Lk = nt.nodes, nt.links
    b = N["Principled BSDF"]
    geo = N.new("ShaderNodeNewGeometry")
    a = _attr(N, attr)
    nz = N.new("ShaderNodeTexNoise"); nz.inputs["Scale"].default_value = 0.6; nz.inputs["Detail"].default_value = 4
    Lk.new(geo.outputs["Position"], nz.inputs["Vector"])
    v = _maprange(N, Lk, nz.outputs["Fac"], 0.3, 0.7, 1 - noise_amt, 1 + noise_amt)
    cv = N.new("ShaderNodeCombineColor")
    for k in range(3):
        Lk.new(v, cv.inputs[k])
    mul = N.new("ShaderNodeMix"); mul.data_type = "RGBA"; mul.blend_type = "MULTIPLY"; mul.inputs[0].default_value = 1.0
    Lk.new(a.outputs["Color"], mul.inputs[6]); Lk.new(cv.outputs[0], mul.inputs[7])
    col = mul.outputs[2]
    if lichen:
        nl = N.new("ShaderNodeTexNoise"); nl.inputs["Scale"].default_value = 1.7; nl.inputs["Detail"].default_value = 6
        Lk.new(geo.outputs["Position"], nl.inputs["Vector"])
        lf = _maprange(N, Lk, nl.outputs["Fac"], 0.55, 0.68, 0.0, 0.7)
        mx = N.new("ShaderNodeMix"); mx.data_type = "RGBA"
        Lk.new(lf, mx.inputs[0]); Lk.new(col, mx.inputs[6]); mx.inputs[7].default_value = (0.30, 0.28, 0.13, 1)
        col = mx.outputs[2]
    _haze(nt, col, b, haze_emit)
    b.inputs["Roughness"].default_value = rough
    if bump_scale:
        nb = N.new("ShaderNodeTexNoise"); nb.inputs["Scale"].default_value = bump_scale; nb.inputs["Detail"].default_value = 3
        Lk.new(geo.outputs["Position"], nb.inputs["Vector"])
        bp = N.new("ShaderNodeBump"); bp.inputs["Strength"].default_value = bump_str
        Lk.new(nb.outputs["Fac"], bp.inputs["Height"]); Lk.new(bp.outputs[0], b.inputs["Normal"])
    if trans > 0:
        try:
            b.inputs["Subsurface Weight"].default_value = trans
            b.inputs["Subsurface Radius"].default_value = (0.2, 0.3, 0.1)
        except Exception:
            pass
    return m


# ======================================================================================
# mesh helpers for objects
# ======================================================================================
class _MB:
    def __init__(self):
        self.v, self.f, self.d = [], [], []

    def face(self, idx, data):
        self.f.append(tuple(idx)); self.d.append(data)

    def add_v(self, p):
        self.v.append(tuple(p))
        return len(self.v) - 1

    def build(self, name, mat, attr, link_fn, cname, smooth=False, sharp=None):
        me = bpy.data.meshes.new(name)
        me.from_pydata(self.v, [], self.f)
        me.update()
        me.materials.append(mat)
        a = me.attributes.new(attr, "FLOAT_COLOR", "FACE")
        flat = []
        for d in self.d[:len(me.polygons)]:
            flat.extend((d[0], d[1], d[2], 1.0))
        a.data.foreach_set("color", flat)
        if smooth:
            for p in me.polygons:
                p.use_smooth = True
            if sharp:
                try:
                    me.set_sharp_from_angle(angle=math.radians(sharp))
                except Exception:
                    pass
        ob = bpy.data.objects.new(name, me)
        link_fn(ob, cname)
        return ob


def _tree(mb, x, y, z, h, r, kind, col, rnd):
    if kind == "poplar":
        rings = [(0.10, 0.5), (0.35, 0.95), (0.65, 0.85), (0.88, 0.42)]
        c0 = 1.6
        ns = 6
    elif kind == "fruit":
        rings = [(0.32, 0.85), (0.58, 1.0), (0.84, 0.62)]
        c0 = 0.9
        ns = 5
    else:
        rings = [(0.22, 0.65), (0.45, 1.0), (0.72, 0.85), (0.93, 0.35)]
        c0 = 1.8
        ns = 6
    rot = rnd.uniform(0, 2 * math.pi)
    lean = (rnd.uniform(-0.04, 0.04) * h, rnd.uniform(-0.04, 0.04) * h)
    base = mb.add_v((x, y, z + c0 + (h - c0) * 0.02))
    R = []
    for ri_, (t, rr) in enumerate(rings):
        zz = z + c0 + (h - c0) * t
        ring = []
        for k in range(ns):
            a = rot + 2 * math.pi * (k + rnd.uniform(-0.2, 0.2)) / ns + 0.5 * ri_ * math.pi / ns
            j = rnd.uniform(0.72, 1.22) if kind != "poplar" else rnd.uniform(0.85, 1.12)
            ring.append(mb.add_v((x + lean[0] * t + math.cos(a) * r * rr * j, y + lean[1] * t + math.sin(a) * r * rr * j,
                                  zz + rnd.uniform(-0.08, 0.08) * (h - c0) / len(rings))))
        R.append(ring)
    top = mb.add_v((x + lean[0], y + lean[1], z + h))
    for k in range(ns):
        mb.face((base, R[0][(k + 1) % ns], R[0][k]), col)
    for ri in range(len(R) - 1):
        for k in range(ns):
            k2 = (k + 1) % ns
            mb.face((R[ri][k], R[ri][k2], R[ri + 1][k2], R[ri + 1][k]), col)
    for k in range(ns):
        mb.face((R[-1][k], R[-1][(k + 1) % ns], top), col)
    # trunk
    tw = 0.12 + 0.01 * h
    tb = [mb.add_v((x + dx, y + dy, z - 0.3)) for dx, dy in ((-tw, -tw), (tw, -tw), (0, tw))]
    tt = [mb.add_v((x + dx, y + dy, z + c0 + 0.5)) for dx, dy in ((-tw, -tw), (tw, -tw), (0, tw))]
    tc = (0.06, 0.045, 0.035)
    for k in range(3):
        mb.face((tb[k], tb[(k + 1) % 3], tt[(k + 1) % 3], tt[k]), tc)


def _rock(mb, x, y, z, s, sq, col, rnd):
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=2 if s > 2.2 else 1, radius=1.0)
    off = Vector((rnd.uniform(0, 100), rnd.uniform(0, 100), rnd.uniform(0, 100)))
    rot = rnd.uniform(0, 2 * math.pi)
    ca, sa = math.cos(rot), math.sin(rot)
    sx, sy = s * rnd.uniform(0.8, 1.3), s * rnd.uniform(0.7, 1.1)
    base = len(mb.v)
    for v in bm.verts:
        p = v.co
        d = 1.0 + 0.35 * noise.noise(p * 1.3 + off) + 0.12 * noise.noise(p * 3.1 + off)
        q = p * d
        q.z = q.z * sq
        if q.z < -0.2:
            q.z = -0.2 - (q.z + 0.2) * 0.3
        px, py = q.x * sx, q.y * sy
        mb.v.append((x + px * ca - py * sa, y + px * sa + py * ca, z + q.z * s))
    for f in bm.faces:
        mb.face([base + v.index for v in f.verts], col)
    bm.free()


def _house(mb, ground, cx, cy, ang, w, d, h, roof, wall_col, roof_col, pitch, hip=False, ruin=False):
    ca, sa = math.cos(ang), math.sin(ang)

    def P(u, v):
        return (cx + u * ca - v * sa, cy + u * sa + v * ca)

    corners = [P(-w / 2, -d / 2), P(w / 2, -d / 2), P(w / 2, d / 2), P(-w / 2, d / 2)]
    zs = [ground.z(x, y) for x, y in corners]
    zb = min(zs) - 0.4
    ze = max(zs) + h
    vb = [mb.add_v((x, y, zb)) for x, y in corners]
    ve = [mb.add_v((x, y, ze)) for x, y in corners]
    for k in range(4):
        mb.face((vb[k], vb[(k + 1) % 4], ve[(k + 1) % 4], ve[k]), wall_col)
    if ruin:
        return
    o = 0.45
    rh = (d / 2 + o) * math.tan(math.radians(pitch))
    zo = ze - o * math.tan(math.radians(pitch))
    # ridge along the long (u) axis
    if not hip:
        r0 = mb.add_v((*P(-w / 2 - o * 0.6, 0), ze + rh - o * math.tan(math.radians(pitch))))
        r1 = mb.add_v((*P(w / 2 + o * 0.6, 0), ze + rh - o * math.tan(math.radians(pitch))))
        e = [mb.add_v((*P(-w / 2 - o * 0.6, -d / 2 - o), zo)), mb.add_v((*P(w / 2 + o * 0.6, -d / 2 - o), zo)),
             mb.add_v((*P(w / 2 + o * 0.6, d / 2 + o), zo)), mb.add_v((*P(-w / 2 - o * 0.6, d / 2 + o), zo))]
        mb.face((e[0], e[1], r1, r0), roof_col)
        mb.face((e[2], e[3], r0, r1), roof_col)
        # gables
        g0 = mb.add_v((*P(-w / 2, 0), ze + (d / 2) * math.tan(math.radians(pitch))))
        g1 = mb.add_v((*P(w / 2, 0), ze + (d / 2) * math.tan(math.radians(pitch))))
        mb.face((ve[3], ve[0], g0), wall_col)
        mb.face((ve[1], ve[2], g1), wall_col)
    else:
        rl = max(0.0, w / 2 - d / 2)
        zr = zo + rh
        r0 = mb.add_v((*P(-rl, 0), zr))
        r1 = mb.add_v((*P(rl, 0), zr))
        e = [mb.add_v((*P(-w / 2 - o, -d / 2 - o), zo)), mb.add_v((*P(w / 2 + o, -d / 2 - o), zo)),
             mb.add_v((*P(w / 2 + o, d / 2 + o), zo)), mb.add_v((*P(-w / 2 - o, d / 2 + o), zo))]
        mb.face((e[0], e[1], r1, r0), roof_col)
        mb.face((e[2], e[3], r0, r1), roof_col)
        mb.face((e[1], e[2], r1), roof_col)
        mb.face((e[3], e[0], r0), roof_col)
    # soffit (underside) so roofs are not see-through from below
    mb.face((e[3], e[2], e[1], e[0]), (0.08, 0.075, 0.07))


# ======================================================================================
# main entry
# ======================================================================================
def _default_exclude(x, y):
    return abs(y + 18) < 45 or (-10 < x < 85 and -10 < y < 55)


def build_landscape(link_fn, terrain_height_fn, site_center=(37, 22), exclude_fn=None, seed=11, quality="final",
                    r_in=150.0, r_out=1500.0, terrain_obj=None, haze_emit=0.35):
    exclude_fn = exclude_fn or _default_exclude
    rnd = random.Random(seed)
    cx0, cy0 = site_center
    G = Ground(terrain_height_fn, terrain_obj, fallback_extent=r_out + 400, center=site_center)
    lift_f = G.dz + 0.05            # fields: +0.05 above terrain_height
    lift_t = G.dz + 0.09            # tracks sit a few cm higher than fields
    if not G.exact:
        lift_f, lift_t = 0.25, 0.30
    dens = 1.0 if quality == "final" else 0.5
    hfn = G.z

    def ok(x, y, margin=0.0):
        if exclude_fn(x, y):
            return False
        d = math.hypot(x - cx0, y - cy0)
        return d > r_in - margin

    # ------------------------------------------------------------ settlements first (they reserve land)
    villages = []
    tries = 0
    while len(villages) < 4 and tries < 400:
        tries += 1
        a = rnd.uniform(0, 2 * math.pi)
        dd = rnd.uniform(450, 1150)
        x, y = cx0 + dd * math.cos(a), cy0 + dd * math.sin(a)
        if not ok(x, y) or exclude_fn(x, y + 120) or exclude_fn(x, y - 120):
            continue
        if G.slope(x, y, 40) > 0.09 or terrain_height_fn(x, y) > 90:
            continue
        if any(math.hypot(x - v[0], y - v[1]) < 600 for v in villages):
            continue
        villages.append((x, y, rnd.uniform(0, math.pi), rnd.choice([150, 190, 230])))
    farm = None
    for _ in range(300):
        a = rnd.uniform(0, 2 * math.pi)
        dd = rnd.uniform(420, 850)
        x, y = cx0 + dd * math.cos(a), cy0 + dd * math.sin(a)
        if ok(x, y) and not exclude_fn(x, y + 80) and G.slope(x, y, 40) < 0.08 and \
                all(math.hypot(x - v[0], y - v[1]) > 350 for v in villages):
            farm = (x, y, rnd.uniform(0, math.pi))
            break
    reserved = [(v[0], v[1], v[3] + 40) for v in villages] + ([(farm[0], farm[1], 140)] if farm else [])

    # orchards (apricot / apple) next to villages
    orchards = []
    for (vx, vy, va, vr) in villages:
        ca, sa = math.cos(va), math.sin(va)
        for k in range(rnd.randint(2, 4)):
            u = rnd.choice([-1, 1]) * rnd.uniform(vr * 0.9, vr * 1.3)
            v = rnd.uniform(-vr * 0.6, vr * 0.6)
            ox, oy = vx + u * ca - v * sa, vy + u * sa + v * ca
            w, d = rnd.uniform(50, 90), rnd.uniform(70, 120)
            q = [(-w / 2, -d / 2), (w / 2, -d / 2), (w / 2, d / 2), (-w / 2, d / 2)]
            poly = [(ox + p[0] * ca - p[1] * sa, oy + p[0] * sa + p[1] * ca) for p in q]
            if all(ok(*p) for p in poly):
                orchards.append((poly, va))

    for poly, oa in orchards:
        ox = sum(p[0] for p in poly) / 4; oy = sum(p[1] for p in poly) / 4
        reserved.append((ox, oy, 0.5 * math.hypot(poly[2][0] - poly[0][0], poly[2][1] - poly[0][1]) + 6))

    def in_reserved(x, y, pad=0.0):
        return any(math.hypot(x - a, y - b) < r + pad for a, b, r in reserved)

    # ------------------------------------------------------------ sectors with their own block grids
    nsec = 7
    for _ in range(200):
        cuts = sorted(rnd.uniform(0, 2 * math.pi) for _ in range(nsec))
        gaps = [cuts[(k + 1) % nsec] - cuts[k] + (2 * math.pi if k == nsec - 1 else 0) for k in range(nsec)]
        if max(gaps) < 2.3 and min(gaps) > 0.45:
            break
    sectors = []
    for k in range(nsec):
        a0 = cuts[k]
        a1 = cuts[(k + 1) % nsec] + (2 * math.pi if k == nsec - 1 else 0)
        sectors.append(dict(a0=a0, a1=a1, ang=math.radians(rnd.uniform(-35, 35)) + (math.pi / 2 if rnd.random() < 0.3 else 0),
                            bw=rnd.uniform(200, 330), bh=rnd.uniform(130, 230), ox=rnd.uniform(0, 300), oy=rnd.uniform(0, 300)))

    def sector_of(x, y):
        a = math.atan2(y - cy0, x - cx0) % (2 * math.pi)
        for i, s in enumerate(sectors):
            lo, hi = s["a0"], s["a1"]
            if lo <= a < hi or lo <= a + 2 * math.pi < hi:
                return i
        return -1

    stats = {"slope": 0}
    fields = []        # (poly, crop, angle)
    blocks_all = []    # unshrunk quads of kept blocks (for rock exclusion)
    tracks = []        # list of polylines
    windbreaks = []    # list of (p0, p1, side_offset)
    R = r_out + 120
    for si, s in enumerate(sectors):
        ca, sa = math.cos(s["ang"]), math.sin(s["ang"])
        na, nb = int(R * 2 / s["bw"]) + 2, int(R * 2 / s["bh"]) + 2
        nodes = {}
        for ia in range(-na // 2 - 1, na // 2 + 2):
            for ib in range(-nb // 2 - 1, nb // 2 + 2):
                r2 = random.Random(hash((seed, si, ia, ib)) & 0xffffffff)
                u = ia * s["bw"] + s["ox"] + r2.uniform(-0.12, 0.12) * s["bw"]
                v = ib * s["bh"] + s["oy"] + r2.uniform(-0.12, 0.12) * s["bh"]
                nodes[(ia, ib)] = (cx0 + u * ca - v * sa, cy0 + u * sa + v * ca)
        # sector wedge (convex, inset 3 m so a gap/track runs along sector borders)
        a0, a1 = s["a0"], s["a1"]
        RR = 6000.0
        wedge = [(cx0, cy0)]
        nwa = max(2, int((a1 - a0) / 0.35) + 1)
        for k in range(nwa + 1):
            aa = a0 + (a1 - a0) * k / nwa
            wedge.append((cx0 + RR * math.cos(aa), cy0 + RR * math.sin(aa)))
        wedge = _inset(_ccw(wedge), 3.0)
        kept = {}
        for (ia, ib), p00 in nodes.items():
            if (ia + 1, ib + 1) not in nodes:
                continue
            q = [p00, nodes[(ia + 1, ib)], nodes[(ia + 1, ib + 1)], nodes[(ia, ib + 1)]]
            cxq = sum(p[0] for p in q) / 4; cyq = sum(p[1] for p in q) / 4
            if sector_of(cxq, cyq) != si and not any(sector_of(px, py) == si for px, py in q):
                continue
            dc = math.hypot(cxq - cx0, cyq - cy0)
            if dc < r_in - 120 or dc > r_out + 120:
                continue
            if dc > r_out - 250 and rnd.random() < (dc - (r_out - 250)) / 450.0:
                continue
            sls = sorted([G.slope(cxq, cyq, 30)] + [G.slope(px, py, 25) for px, py in q])
            if sls[2] > 0.30 or sls[-1] > 0.55:
                stats["slope"] += 1
                continue
            if rnd.random() < 0.07:          # left as pasture / steppe
                continue
            inner = _inset(_ccw(q), 3.0)
            if inner is None:
                continue
            P0, P1, P2, P3 = inner
            luv = math.hypot(P1[0] - P0[0], P1[1] - P0[1])
            lvv = math.hypot(P3[0] - P0[0], P3[1] - P0[1])
            along_u = rnd.random() < 0.6
            span = luv if along_u else lvv
            ts = [0.0]
            t = 0.0
            mode = rnd.random()
            while t < 1.0:
                if mode < 0.25:
                    wdt = rnd.uniform(60, 160)      # large collective field
                elif mode < 0.7:
                    wdt = rnd.uniform(18, 55)       # private strips
                else:
                    wdt = rnd.uniform(30, 90)
                t += wdt / span
                ts.append(min(t, 1.0))
            if len(ts) > 2 and (ts[-1] - ts[-2]) * span < 12:
                ts.pop(-2)
            ts[-1] = 1.0
            crop_run = None
            nkept = 0
            for a_, b_ in zip(ts[:-1], ts[1:]):
                g = 0.8 / span
                ta, tb = a_ + (g if a_ > 0 else 0), b_ - (g if b_ < 1 else 0)
                if tb - ta <= 0:
                    continue
                if along_u:
                    sub = [_lerp2(P0, P1, ta), _lerp2(P0, P1, tb), _lerp2(P3, P2, tb), _lerp2(P3, P2, ta)]
                    dirv = (P3[0] - P0[0], P3[1] - P0[1])
                else:
                    sub = [_lerp2(P0, P3, ta), _lerp2(P1, P2, ta), _lerp2(P1, P2, tb), _lerp2(P0, P3, tb)]
                    dirv = (P1[0] - P0[0], P1[1] - P0[1])
                parts = [sub]
                if rnd.random() < 0.3:     # split across
                    c = rnd.uniform(0.3, 0.7)
                    gg = 0.8 / (lvv if along_u else luv)
                    A, B_, C, D_ = sub
                    parts = [[A, B_, _lerp2(B_, C, c - gg), _lerp2(A, D_, c - gg)],
                             [_lerp2(A, D_, c + gg), _lerp2(B_, C, c + gg), C, D_]]
                cand = []
                for pp in parts:
                    # keep the longest run of the strip that avoids excluded / reserved ground
                    A, B_, C, D_ = pp
                    nseg = 6
                    good = []
                    for k in range(nseg):
                        t0, t1 = k / nseg, (k + 1) / nseg
                        seg = [_lerp2(A, D_, t0), _lerp2(B_, C, t0), _lerp2(B_, C, t1), _lerp2(A, D_, t1)]
                        mx = sum(p[0] for p in seg) / 4; my = sum(p[1] for p in seg) / 4
                        good.append(all(not exclude_fn(px, py) and not in_reserved(px, py, 8) for px, py in seg + [(mx, my)]))
                    best, cur = None, None
                    for k, gk in enumerate(good + [False]):
                        if gk and cur is None:
                            cur = k
                        elif not gk and cur is not None:
                            if best is None or k - cur > best[1] - best[0]:
                                best = (cur, k)
                            cur = None
                    if best is None:
                        continue
                    t0, t1 = best[0] / nseg + (0.004 if best[0] else 0), best[1] / nseg - (0.004 if best[1] < nseg else 0)
                    cand.append([_lerp2(A, D_, t0), _lerp2(B_, C, t0), _lerp2(B_, C, t1), _lerp2(A, D_, t1)])
                for pp in cand:
                    pp = _ccw(pp)
                    mx = sum(p[0] for p in pp) / len(pp); my = sum(p[1] for p in pp) / len(pp)
                    dd = math.hypot(mx - cx0, my - cy0)
                    if dd < 1:
                        continue
                    ux, uy = (mx - cx0) / dd, (my - cy0) / dd
                    # ring limits as tangent half-planes (convex clip keeps parcels convex)
                    hp_in = [(cx0 + ux * r_in - uy * 9000, cy0 + uy * r_in + ux * 9000),
                             (cx0 + ux * r_in + uy * 9000, cy0 + uy * r_in - ux * 9000),
                             (cx0 + ux * 9000 + uy * 9000, cy0 + uy * 9000 - ux * 9000),
                             (cx0 + ux * 9000 - uy * 9000, cy0 + uy * 9000 + ux * 9000)]
                    clipper = [hp_in] + ([wedge] if wedge is not None else [])
                    poly3 = [(x, y, 0.0) for x, y in pp]
                    for cp in clipper:
                        poly3 = _clip(poly3, _ccw(cp))
                        if len(poly3) < 3:
                            break
                    if len(poly3) < 3:
                        continue
                    pp = [(p[0], p[1]) for p in poly3]
                    if abs(_area(pp)) < 200:
                        continue
                    if any(math.hypot(px - cx0, py - cy0) > r_out + 150 for px, py in pp):
                        continue
                    if any(exclude_fn(px, py) for px, py in pp):
                        continue
                    if G.steep(pp):
                        stats["steep"] = stats.get("steep", 0) + 1
                        continue
                    if crop_run is None or rnd.random() < 0.55:
                        names = list(CROPS.keys())
                        crop_run = rnd.choices(names, weights=[CROPS[n][6] for n in names])[0]
                    fields.append((pp, crop_run, math.atan2(dirv[1], dirv[0])))
                    nkept += 1
            if nkept:
                kept[(ia, ib)] = q
                blocks_all.append(q)
        # tracks + windbreaks along grid lines adjacent to kept blocks
        for horiz in (True, False):
            lines = {}
            for (ia, ib) in nodes:
                if horiz:
                    a, b = (ia, ib), (ia + 1, ib)
                    adj = ((ia, ib - 1) in kept) or ((ia, ib) in kept)
                    key = ib
                else:
                    a, b = (ia, ib), (ia, ib + 1)
                    adj = ((ia - 1, ib) in kept) or ((ia, ib) in kept)
                    key = ia
                if adj and b in nodes:
                    lines.setdefault(key, []).append((a, b))
            for key, segs in lines.items():
                segs.sort()
                r2 = random.Random(hash((seed, si, horiz, key)) & 0xffffffff)
                is_track = r2.random() < (0.55 if horiz else 0.4)
                is_wind = r2.random() < 0.28
                run = []
                for a, b in segs:
                    pa, pb = nodes[a], nodes[b]
                    mid = ((pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2)
                    good = ok(*pa) and ok(*pb) and ok(*mid) and not in_reserved(*mid)
                    if good and (not run or run[-1] == pa):
                        if not run:
                            run.append(pa)
                        run.append(pb)
                    else:
                        if len(run) >= 2:
                            if is_track:
                                tracks.append((run, 3.0))
                            if is_wind:
                                windbreaks.append(run)
                        run = [pa, pb] if good else []
                if len(run) >= 2:
                    if is_track:
                        tracks.append((run, 3.0))
                    if is_wind:
                        windbreaks.append(run)

    # main tracks: from the highway corridor edge to each village / the farm
    for (vx, vy, va, vr) in villages + ([(farm[0], farm[1], 0, 80)] if farm else []):
        sx = vx + rnd.uniform(-150, 150)
        if -120 < sx < 200:
            sx = -120 if sx < 40 else 200
        sy = 30.0 if vy > cy0 else -66.0
        pts = []
        n = 14
        for k in range(n + 1):
            t = k / n
            x = sx + (vx - sx) * t + 40 * math.sin(t * math.pi * 2 + vx) * (1 - abs(2 * t - 1))
            y = sy + (vy - sy) * t
            pts.append((x, y))
        pts = [p for p in pts if not exclude_fn(*p)]
        if len(pts) >= 2:
            tracks.append((pts, 4.0))

    # village streets (same layout as the houses below)
    for (vx, vy, va, vr) in villages:
        ca, sa = math.cos(va), math.sin(va)
        nstreets = 3 if vr > 200 else 2
        for st in range(nstreets):
            off = (st - (nstreets - 1) / 2) * 70
            pts = []
            for k in range(9):
                u = -vr * 0.95 + 1.9 * vr * k / 8
                x, y = vx + u * ca - off * sa, vy + u * sa + off * ca
                if ok(x, y):
                    pts.append((x, y))
            if len(pts) >= 2:
                tracks.append((pts, 5.0))
        # cross street linking them
        pts = [(vx - (k - 2) * 45 * sa, vy + (k - 2) * 45 * ca) for k in range(5)]
        pts = [p for p in pts if ok(*p)]
        if len(pts) >= 2:
            tracks.append((pts, 5.0))

    for poly, oa in orchards:
        fields.append((poly, "fallow", oa))

    # village gardens
    for (vx, vy, va, vr) in villages:
        ca, sa = math.cos(va), math.sin(va)
        for k in range(int(vr / 9)):
            u = rnd.uniform(-vr, vr); v = rnd.choice([-1, 1]) * rnd.uniform(45, vr * 0.9)
            gx, gy = vx + u * ca - v * sa, vy + u * sa + v * ca
            if not ok(gx, gy):
                continue
            w, d = rnd.uniform(14, 26), rnd.uniform(28, 55)
            q = [(-w / 2, -d / 2), (w / 2, -d / 2), (w / 2, d / 2), (-w / 2, d / 2)]
            poly = [(gx + p[0] * ca - p[1] * sa, gy + p[0] * sa + p[1] * ca) for p in q]
            fields.append((poly, rnd.choice(["potato", "potato", "alfalfa", "ploughed", "harrowed"]), va + math.pi / 2))

    # ------------------------------------------------------------ build field mesh
    out = {"objects": {}, "faces": {}}
    D = Draper(G, lift_f)
    for poly, crop, ang in fields:
        if G.steep(poly):
            continue
        col, rsp, rc, ssp, sc, tram, _w = CROPS[crop]
        j = rnd.uniform(-0.12, 0.12)
        hue = rnd.uniform(-0.03, 0.03)
        c = (max(0.0, col[0] * (1 + j + hue)), max(0.0, col[1] * (1 + j)), max(0.0, col[2] * (1 + j - hue)))
        data = (c, (math.cos(ang), math.sin(ang), rsp), (rc, ssp, sc), (tram, rnd.random(), 0.0))
        D.add(poly, data)
    if D.faces:
        ob = D.build("land_fields", mat_fields(haze_emit), {
            "fcol": ("FLOAT_COLOR", lambda d: (d[0][0], d[0][1], d[0][2], 1.0), 4),
            "fdir": ("FLOAT_VECTOR", lambda d: d[1], 3),
            "fpar": ("FLOAT_VECTOR", lambda d: d[2], 3),
            "fpr2": ("FLOAT_VECTOR", lambda d: d[3], 3)}, link_fn, "landscape")
        out["objects"]["fields"] = ob
        out["faces"]["fields"] = len(ob.data.polygons)

    # ------------------------------------------------------------ tracks
    T = Draper(G, lift_t)
    for ti, (pts, w) in enumerate(tracks):
        for k in range(len(pts) - 1):
            (x0, y0), (x1, y1) = pts[k], pts[k + 1]
            dx, dy = x1 - x0, y1 - y0
            ln = math.hypot(dx, dy)
            if ln < 1:
                continue
            ux, uy = dx / ln, dy / ln
            nx, ny = -uy * w / 2, ux * w / 2
            e = w / 2
            q = [(x0 - ux * e + nx, y0 - uy * e + ny), (x0 - ux * e - nx, y0 - uy * e - ny),
                 (x1 + ux * e - nx, y1 + uy * e - ny), (x1 + ux * e + nx, y1 + uy * e + ny)]
            if G.steep(q):
                continue
            T.add(q, None, lift=lift_t + 0.004 * (k % 2), share=False)
    if T.faces:
        ob = T.build("land_tracks", mat_tracks(haze_emit), {}, link_fn, "landscape")
        out["objects"]["tracks"] = ob
        out["faces"]["tracks"] = len(ob.data.polygons)

    # ------------------------------------------------------------ windbreak rows
    mb = _MB()
    ntree = 0
    for run in windbreaks:
        kind = rnd.choice(["poplar", "poplar", "elm"])
        sp = 5.5 if kind == "poplar" else 8.0
        side = rnd.choice([-1, 1]) * 3.2
        for k in range(len(run) - 1):
            (x0, y0), (x1, y1) = run[k], run[k + 1]
            ln = math.hypot(x1 - x0, y1 - y0)
            ux, uy = (x1 - x0) / ln, (y1 - y0) / ln
            nx, ny = -uy, ux
            n = int(ln / sp)
            for i in range(n):
                if rnd.random() > 0.86 * dens + (0.14 if dens < 1 else 0) or rnd.random() < 0.08:
                    continue
                t = (i + 0.5) * sp + rnd.uniform(-1, 1)
                x, y = x0 + ux * t + nx * side, y0 + uy * t + ny * side
                if not ok(x, y):
                    continue
                if kind == "poplar":
                    h, r = rnd.uniform(13, 21), rnd.uniform(1.5, 2.3)
                    col = (0.028 * rnd.uniform(0.8, 1.2), 0.050 * rnd.uniform(0.85, 1.15), 0.016)
                else:
                    h, r = rnd.uniform(8, 12), rnd.uniform(3.0, 4.2)
                    col = (0.040 * rnd.uniform(0.8, 1.2), 0.060 * rnd.uniform(0.85, 1.15), 0.022)
                _tree(mb, x, y, hfn(x, y), h, r, kind, col, rnd)
                ntree += 1
    # orchards / village trees
    for (vx, vy, va, vr) in villages:
        for k in range(int(vr * 0.9 * dens)):
            a = rnd.uniform(0, 2 * math.pi); dd = vr * math.sqrt(rnd.random())
            x, y = vx + dd * math.cos(a), vy + dd * math.sin(a)
            if not ok(x, y):
                continue
            kind = "fruit" if rnd.random() < 0.7 else rnd.choice(["poplar", "elm"])
            if kind == "fruit":
                h, r = rnd.uniform(4, 6.5), rnd.uniform(2.0, 3.0)
            elif kind == "poplar":
                h, r = rnd.uniform(14, 22), rnd.uniform(1.6, 2.3)
            else:
                h, r = rnd.uniform(9, 13), rnd.uniform(3.2, 4.5)
            col = (0.045 * rnd.uniform(0.8, 1.25), 0.068 * rnd.uniform(0.85, 1.15), 0.024)
            _tree(mb, x, y, hfn(x, y), h, r, kind, col, rnd)
            ntree += 1
    for poly, oa in orchards:
        P0, P1, P2, P3 = poly
        lu = math.hypot(P1[0] - P0[0], P1[1] - P0[1]); lv = math.hypot(P3[0] - P0[0], P3[1] - P0[1])
        nu, nv = int(lu / 7.0), int(lv / 6.0)
        for i in range(nu):
            for j in range(nv):
                if rnd.random() < 0.1 or rnd.random() > dens + 0.15:
                    continue
                a_ = _lerp2(P0, P1, (i + 0.5) / nu); b_ = _lerp2(P3, P2, (i + 0.5) / nu)
                x, y = _lerp2(a_, b_, (j + 0.5) / nv)
                col = (0.042 * rnd.uniform(0.85, 1.2), 0.066 * rnd.uniform(0.9, 1.1), 0.022)
                _tree(mb, x, y, hfn(x, y), rnd.uniform(3.5, 5.0), rnd.uniform(1.6, 2.3), "fruit", col, rnd)
                ntree += 1
    if mb.f:
        mt = _attr_mat("land_trees", "tcol", 0.9, haze_emit, bump_scale=2.6, bump_str=0.9, noise_amt=0.35, trans=0.1)
        ob = mb.build("land_trees", mt, "tcol", link_fn, "landscape", smooth=True, sharp=35)
        out["objects"]["trees"] = ob
        out["faces"]["trees"] = len(ob.data.polygons)

    # ------------------------------------------------------------ rocks
    def in_block(x, y):
        for q in blocks_all:
            if _inside_convex(_ccw(q), x, y):
                return True
        return False

    bucket = {}
    for qi, q in enumerate(blocks_all):
        xs_, ys_ = [p[0] for p in q], [p[1] for p in q]
        for bx in range(int(min(xs_) // 200), int(max(xs_) // 200) + 1):
            for by in range(int(min(ys_) // 200), int(max(ys_) // 200) + 1):
                bucket.setdefault((bx, by), []).append(qi)

    def in_block_fast(x, y):
        for qi in bucket.get((int(x // 200), int(y // 200)), ()):
            if _inside_convex(_ccw(blocks_all[qi]), x, y):
                return True
        return False

    rk = _MB()
    nclusters = int(70 * dens)
    placed = 0
    attempts = 0
    while placed < nclusters and attempts < 4000:
        attempts += 1
        a = rnd.uniform(0, 2 * math.pi); dd = rnd.uniform(r_in + 20, r_out + 300)
        x, y = cx0 + dd * math.cos(a), cy0 + dd * math.sin(a)
        if not ok(x, y, 0) or in_block_fast(x, y) or in_reserved(x, y, 20):
            continue
        sl = G.slope(x, y, 20)
        if sl < 0.05 and rnd.random() < 0.6:
            continue
        placed += 1
        n = rnd.randint(3, 9)
        for k in range(n):
            px, py = x + rnd.gauss(0, 9), y + rnd.gauss(0, 9)
            if exclude_fn(px, py) or in_block_fast(px, py):
                continue
            s = rnd.uniform(0.7, 3.2) if k else rnd.uniform(2.0, 4.5)
            g = rnd.uniform(0.85, 1.15)
            col = (0.105 * g, 0.098 * g, 0.088 * g) if rnd.random() < 0.7 else (0.16 * g, 0.12 * g, 0.095 * g)
            _rock(rk, px, py, hfn(px, py) - s * 0.25, s, rnd.uniform(0.45, 0.8), col, rnd)
    for k in range(int(260 * dens)):
        a = rnd.uniform(0, 2 * math.pi); dd = rnd.uniform(r_in - 60, r_out + 300)
        x, y = cx0 + dd * math.cos(a), cy0 + dd * math.sin(a)
        if exclude_fn(x, y) or math.hypot(x - cx0, y - cy0) < 110 or in_block_fast(x, y) or in_reserved(x, y):
            continue
        s = rnd.uniform(0.4, 1.4)
        g = rnd.uniform(0.85, 1.15)
        _rock(rk, x, y, hfn(x, y) - s * 0.3, s, rnd.uniform(0.4, 0.7), (0.11 * g, 0.10 * g, 0.09 * g), rnd)
    if rk.f:
        mr = _attr_mat("land_rocks", "rcol", 0.8, haze_emit, bump_scale=3.0, bump_str=0.35, noise_amt=0.18, lichen=True)
        ob = rk.build("land_rocks", mr, "rcol", link_fn, "landscape", smooth=True, sharp=50)
        out["objects"]["rocks"] = ob
        out["faces"]["rocks"] = len(ob.data.polygons)

    # ------------------------------------------------------------ buildings
    bb = _MB()
    walls = [(0.42, 0.24, 0.16), (0.46, 0.30, 0.20), (0.36, 0.20, 0.15), (0.55, 0.53, 0.49), (0.62, 0.60, 0.55),
             (0.26, 0.25, 0.23), (0.40, 0.38, 0.34)]
    roofs = [(0.30, 0.085, 0.045), (0.25, 0.10, 0.06), (0.10, 0.19, 0.12), (0.33, 0.34, 0.35), (0.42, 0.43, 0.44),
             (0.42, 0.15, 0.07), (0.28, 0.28, 0.27), (0.14, 0.17, 0.30)]
    nb_ = 0
    for (vx, vy, va, vr) in villages:
        ca, sa = math.cos(va), math.sin(va)
        nstreets = 3 if vr > 200 else 2
        for st in range(nstreets):
            off = (st - (nstreets - 1) / 2) * 70
            spts = []
            for side in (-1, 1):
                u = -vr * 0.85
                while u < vr * 0.85:
                    u += rnd.uniform(24, 38)
                    v = off + side * rnd.uniform(11, 16)
                    hx, hy = vx + u * ca - v * sa, vy + u * sa + v * ca
                    if not ok(hx, hy) or rnd.random() < 0.12:
                        continue
                    w, d = rnd.uniform(8.5, 13), rnd.uniform(7, 10)
                    storeys = 1 if rnd.random() < 0.65 else 2
                    h = 3.1 * storeys + rnd.uniform(0.0, 0.6)
                    hip = rnd.random() < 0.35
                    ruin = rnd.random() < 0.04
                    _house(bb, G, hx, hy, va + rnd.uniform(-0.08, 0.08) + (math.pi / 2 if rnd.random() < 0.15 else 0),
                           w, d, h, None, rnd.choice(walls), rnd.choice(roofs), rnd.uniform(18, 30), hip, ruin)
                    nb_ += 1
                    # outbuilding / shed
                    if rnd.random() < 0.5:
                        sx_, sy_ = hx - sa * side * 14 + ca * rnd.uniform(-6, 6), hy + ca * side * 14 + sa * rnd.uniform(-6, 6)
                        if ok(sx_, sy_):
                            _house(bb, G, sx_, sy_, va, rnd.uniform(4, 7), rnd.uniform(3.5, 5), 2.5, None,
                                   rnd.choice(walls), rnd.choice(roofs[:5]), 12, False)
    if farm:
        fx, fy, fa = farm
        ca, sa = math.cos(fa), math.sin(fa)
        for k in range(rnd.randint(3, 5)):
            v = (k - 2) * 28
            u = rnd.uniform(-15, 15)
            hx, hy = fx + u * ca - v * sa, fy + u * sa + v * ca
            if not ok(hx, hy):
                continue
            ruin = rnd.random() < 0.3
            _house(bb, G, hx, hy, fa, rnd.uniform(48, 80), rnd.uniform(12, 16), rnd.uniform(4.0, 5.5), None,
                   rnd.choice([(0.55, 0.54, 0.5), (0.45, 0.44, 0.41), (0.40, 0.26, 0.18)]),
                   rnd.choice([(0.30, 0.30, 0.29), (0.36, 0.37, 0.38), (0.28, 0.12, 0.07)]), rnd.uniform(12, 18), False, ruin)
            nb_ += 1
        # silage pit walls / water tank
        _house(bb, G, fx + 60 * ca, fy + 60 * sa, fa, 6, 6, 9, None, (0.5, 0.5, 0.48), (0.3, 0.3, 0.3), 5, True)
    if bb.f:
        mbm = _attr_mat("land_buildings", "bcol", 0.75, haze_emit, noise_amt=0.08)
        ob = bb.build("land_buildings", mbm, "bcol", link_fn, "landscape")
        out["objects"]["buildings"] = ob
        out["faces"]["buildings"] = len(ob.data.polygons)

    # ------------------------------------------------------------ power line along the first main track
    main = [t for t in tracks if abs(t[1] - 4.0) < 1e-6 and len(t[0]) > 6]
    if main:
        pts = main[0][0]
        poles = []
        acc = 0.0
        nxt = 0.0
        for k in range(len(pts) - 1):
            (x0, y0), (x1, y1) = pts[k], pts[k + 1]
            ln = math.hypot(x1 - x0, y1 - y0)
            ux, uy = (x1 - x0) / ln, (y1 - y0) / ln
            while nxt <= acc + ln:
                t = nxt - acc
                x, y = x0 + ux * t - uy * 7.0, y0 + uy * t + ux * 7.0
                if ok(x, y):
                    poles.append((x, y, math.atan2(uy, ux)))
                nxt += 68.0
            acc += ln
        pm = _MB()
        conc = (0.40, 0.39, 0.37)
        tips = []
        for (x, y, a) in poles:
            z0 = hfn(x, y) - 0.5
            H = 10.5
            for (r0, r1, zz0, zz1) in ((0.16, 0.09, z0, z0 + H),):
                b0 = [pm.add_v((x + dx * r0, y + dy * r0, zz0)) for dx, dy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
                b1 = [pm.add_v((x + dx * r1, y + dy * r1, zz1)) for dx, dy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
                for k in range(4):
                    pm.face((b0[k], b0[(k + 1) % 4], b1[(k + 1) % 4], b1[k]), conc)
                pm.face(tuple(b1), conc)
            # cross-arm perpendicular to the line
            nx_, ny_ = -math.sin(a), math.cos(a)
            za = z0 + H - 0.45
            L_ = 1.0
            c = [(x + nx_ * L_ + dx, y + ny_ * L_ + dy) for dx, dy in ((-0.05, -0.05), (0.05, 0.05))]
            q0 = [pm.add_v((x - nx_ * L_ + ox, y - ny_ * L_ + oy, za + oz)) for ox, oy, oz in
                  ((-0.05 * math.cos(a), -0.05 * math.sin(a), -0.05), (0.05 * math.cos(a), 0.05 * math.sin(a), -0.05),
                   (0.05 * math.cos(a), 0.05 * math.sin(a), 0.05), (-0.05 * math.cos(a), -0.05 * math.sin(a), 0.05))]
            q1 = [pm.add_v((x + nx_ * L_ + ox, y + ny_ * L_ + oy, za + oz)) for ox, oy, oz in
                  ((-0.05 * math.cos(a), -0.05 * math.sin(a), -0.05), (0.05 * math.cos(a), 0.05 * math.sin(a), -0.05),
                   (0.05 * math.cos(a), 0.05 * math.sin(a), 0.05), (-0.05 * math.cos(a), -0.05 * math.sin(a), 0.05))]
            for k in range(4):
                pm.face((q0[k], q0[(k + 1) % 4], q1[(k + 1) % 4], q1[k]), (0.18, 0.18, 0.19))
            tips.append([(x - nx_ * 0.9, y - ny_ * 0.9, za + 0.18), (x, y, z0 + H + 0.12), (x + nx_ * 0.9, y + ny_ * 0.9, za + 0.18)])
        if pm.f:
            mp = _attr_mat("land_poles", "pcol", 0.7, haze_emit, noise_amt=0.1)
            ob = pm.build("land_poles", mp, "pcol", link_fn, "landscape")
            out["objects"]["poles"] = ob
            out["faces"]["poles"] = len(ob.data.polygons)
        if len(tips) > 1:
            cu = bpy.data.curves.new("land_wires", "CURVE")
            cu.dimensions = "3D"
            cu.bevel_depth = 0.012
            cu.bevel_resolution = 0
            for a_, b_ in zip(tips[:-1], tips[1:]):
                for w in range(3):
                    p0, p1 = Vector(a_[w]), Vector(b_[w])
                    if (p1 - p0).length > 120:
                        continue
                    sp = cu.splines.new("POLY")
                    nseg = 10
                    sp.points.add(nseg)
                    for i in range(nseg + 1):
                        t = i / nseg
                        p = p0.lerp(p1, t)
                        p.z -= 1.1 * 4 * t * (1 - t)
                        sp.points[i].co = (p.x, p.y, p.z, 1.0)
            mw = bpy.data.materials.get("land_wire") or bpy.data.materials.new("land_wire")
            mw.use_nodes = True
            mw.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.06, 0.06, 0.065, 1)
            mw.node_tree.nodes["Principled BSDF"].inputs["Metallic"].default_value = 0.6
            mw.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.5
            cu.materials.append(mw)
            ob = bpy.data.objects.new("land_wires", cu)
            link_fn(ob, "landscape")
            out["objects"]["wires"] = ob
            out["faces"]["wires"] = sum(len(s.points) - 1 for s in cu.splines) * 4

    out["faces"]["total"] = sum(v for k, v in out["faces"].items() if k != "total")
    out["exact_drape"] = G.exact
    out["villages"] = villages
    out["farm"] = farm
    out["fields"] = len(fields)
    out["stats"] = dict(stats, blocks=len(blocks_all), tracks=len(tracks), windbreaks=len(windbreaks))
    return out

