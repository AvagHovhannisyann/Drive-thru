"""
CHAMPA Compact: the lean first-unit format, co-located on a host fuel-station forecourt.

Same road, terrain, landscape, materials and brand assets as the reference prototype (build_scene.py),
but a 12.0 x 7.5 m (90 m2) pavilion with a single drive-thru lane (one order point, one window),
a walk-up window and a small terrace; restrooms, fuel and the highway access are shared with the host.
The host station is deliberately generic (no real brand).

  blender -b -P design/3d/compact_scene.py -- --mode day --views c_aerial,c_hero --samples 128 --pct 100 --out design/renders/final
"""
import math
import os
import sys
import time

import bpy
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_scene as B  # noqa: E402

from compact_geom import BLD, ROOF, TOWER, LANE_X, LANE_Y, LANE_W, WEST_X, ORDER, WINDOW_X, HOST, roof_z  # noqa: E402


def grid_surface(name, x0, x1, y0, y1, zfn, mat, n=24, cname="building", thick=0.0, mat_edge=None):
    verts, faces = [], []
    for j in range(n + 1):
        for i in range(n + 1):
            x = x0 + (x1 - x0) * i / n; y = y0 + (y1 - y0) * j / n
            verts.append((x, y, zfn(x, y)))
    for j in range(n):
        for i in range(n):
            a = j * (n + 1) + i
            faces.append((a, a + 1, a + n + 2, a + n + 1))
    mats = [mat]
    idx = [0] * len(faces)
    if thick > 0:
        base = len(verts)
        for (x, y, z) in list(verts):
            verts.append((x, y, z + thick))
        for j in range(n):
            for i in range(n):
                a = base + j * (n + 1) + i
                faces.append((a, a + n + 1, a + n + 2, a + 1))
        mats.append(mat_edge or mat)
        idx += [1] * (n * n)
        # edges
        ring = [(i, 0) for i in range(n)] + [(n, j) for j in range(n)] + [(i, n) for i in range(n, 0, -1)] + [(0, j) for j in range(n, 0, -1)]
        for k in range(len(ring)):
            i0, j0 = ring[k]; i1, j1 = ring[(k + 1) % len(ring)]
            a, b = j0 * (n + 1) + i0, j1 * (n + 1) + i1
            faces.append((a, b, base + b, base + a))
            idx.append(1)
    return B.mesh_obj(name, verts, faces, mats, cname, mat_idx=idx)


# ---------------------------------------------------------------- host fuel station (generic)
def build_host(M, night):
    white = B.principled("host_white", (0.78, 0.79, 0.8), rough=0.45)
    grey = B.principled("host_grey", (0.18, 0.19, 0.2), rough=0.5)
    band = B.principled("host_band", (0.16, 0.36, 0.55), rough=0.4)   # neutral blue band, no brand
    x0, y0, x1, y1 = HOST["canopy"]
    z = HOST["canopy_z"]
    B.box("host_canopy", x0, y0, z, x1, y1, z + 0.9, white, "host")
    B.box("host_canopy_band_s", x0 - 0.02, y0 - 0.02, z + 0.25, x1 + 0.02, y0 + 0.01, z + 0.6, band, "host")
    B.box("host_canopy_band_n", x0 - 0.02, y1 - 0.01, z + 0.25, x1 + 0.02, y1 + 0.02, z + 0.6, band, "host")
    soffit = B.principled("host_soffit", (0.85, 0.85, 0.85), rough=0.5, emission=(1, 1, 1), estr=2.5 if night else 0.0)
    B.box("host_soffit", x0 + 0.2, y0 + 0.2, z - 0.01, x1 - 0.2, y1 - 0.2, z, soffit, "host")
    for cx in (9.5, 26.5):
        for cy in (11.5, 17.5):
            B.box(f"host_col_{cx}_{cy}", cx - 0.25, cy - 0.25, 0.15, cx + 0.25, cy + 0.25, z, white, "host")
    for k, cx in enumerate((9.5, 15.17, 20.83, 26.5)):
        B.box(f"host_island_{k}", cx - 0.7, 12.3, 0.0, cx + 0.7, 16.7, 0.18, M["kerb"], "host")
        B.box(f"host_pump_{k}", cx - 0.35, 13.9, 0.18, cx + 0.35, 15.1, 1.95, white, "host")
        B.box(f"host_pump_top_{k}", cx - 0.37, 13.88, 1.6, cx + 0.37, 15.12, 1.95, band, "host")
    sx0, sy0, sx1, sy1 = HOST["shop"]
    B.box("host_shop", sx0, sy0, 0.0, sx1, sy1, 4.2, grey, "host")
    B.box("host_shop_glass", sx0 + 1.0, sy0 - 0.02, 0.3, sx1 - 4.0, sy0 + 0.05, 3.0, M["glass_dark"], "host")
    B.box("host_shop_door", sx1 - 3.5, sy0 - 0.02, 0.15, sx1 - 1.5, sy0 + 0.05, 2.6, M["glass_dark"], "host")
    B.box("host_shop_fascia", sx0 - 0.05, sy0 - 0.08, 3.4, sx1 + 0.05, sy0 + 0.02, 4.2, band, "host")
    if night:
        gl = B.principled("host_shop_glow", (0.9, 0.9, 0.85), rough=0.5, emission=(1, 0.95, 0.85), estr=2.0)
        B.box("host_shop_interior", sx0 + 1.0, sy0 + 0.3, 0.3, sx1 - 1.5, sy0 + 0.4, 3.0, gl, "host")
        for cx in (12, 24):
            for cy in (11, 18):
                ld = bpy.data.lights.new("host_light", "SPOT"); ld.energy = 1600; ld.spot_size = math.radians(120); ld.color = (1, 0.98, 0.95)
                lo = bpy.data.objects.new("host_light", ld); lo.location = (cx, cy, z - 0.1); B.link(lo, "lights_exterior")


# ---------------------------------------------------------------- site: paving, kerbs, planting, markings
def build_site(M):
    B.box("site_asphalt", 0, 0, -0.04, 74, 44, 0.03, M["asphalt"], "site")
    kh = 0.15
    # CHAMPA island: building plinth + terrace (pavers) inside the lane loop
    B.prism("champa_island", [(45.4, 15.6), (64.7, 15.6), (64.7, 29.9), (45.4, 29.9)], 0.0, kh, M["kerb"], M["pavers"])
    # planting strips
    for k, poly in enumerate([[(68.6, 3.0), (73.8, 3.0), (73.8, 43.8), (68.6, 43.8)],
                              [(40.0, 34.0), (68.4, 34.0), (68.4, 43.8), (40.0, 43.8)],
                              [(0.2, 40.0), (39.8, 40.0), (39.8, 43.8), (0.2, 43.8)],
                              [(46.0, 3.0), (64.5, 3.0), (64.5, 5.6), (46.0, 5.6)],
                              [(33.0, 22.5), (41.4, 22.5), (41.4, 33.5), (33.0, 33.5)]]):
        B.prism(f"kerb_pl_{k}", poly, 0.0, kh, M["kerb"], M["kerb"])
        B.prism(f"plant_{k}", B.offset_poly(poly, -0.16), 0.0, kh + 0.02, M["soil"], M["grass"])
    W, Y = M["paint_white"], M["paint_yellow"]
    z = 0.034
    # drive-thru lane edges (east leg, north leg, west leg)
    hw = LANE_W / 2
    B.strip("lane_e_out", [(LANE_X + hw, 3.0), (LANE_X + hw, LANE_Y + hw)], 0.12, z, W)
    B.strip("lane_n_out", [(LANE_X + hw, LANE_Y + hw), (WEST_X - hw, LANE_Y + hw)], 0.12, z, W)
    B.strip("lane_w_out", [(WEST_X - hw, LANE_Y + hw), (WEST_X - hw, 8.0)], 0.12, z, W)
    B.strip("lane_entry_text_bar", [(LANE_X - hw, 6.5), (LANE_X + hw, 6.5)], 0.35, z, W)
    B.strip("stop_window", [(WINDOW_X - 1.3, LANE_Y - hw), (WINDOW_X - 1.3, LANE_Y + hw)], 0.3, z, W)
    # parking (6 + 1 EV) south of the island, nose-in from the forecourt aisle
    for i in range(8):
        xx = 46.6 + i * 2.6
        B.strip(f"stall_{i}", [(xx, 6.2), (xx, 11.2)], 0.12, z, W)
    B.box("ev_bay", 46.7, 6.3, 0.03, 49.1, 11.1, z - 0.001, M["paint_green"], "markings")
    # chevrons on lane
    for k, (x, y, h) in enumerate([(LANE_X, 10.0, 90), (LANE_X, 26.0, 90), (60.0, LANE_Y, 180), (47.0, LANE_Y, 180), (WEST_X, 20.0, 270)]):
        hr = math.radians(h)
        d = Vector((math.cos(hr), math.sin(hr))); n = Vector((-d.y, d.x))
        p = Vector((x, y))
        B.strip(f"chev_{k}", [tuple(p - d * 0.9 + n * 0.7), tuple(p), tuple(p - d * 0.9 - n * 0.7)], 0.22, z, W)


# ---------------------------------------------------------------- the CHAMPA Compact pavilion
def build_pavilion(M, night):
    b = BLD
    f0 = b["ffl"]
    x0, x1, y0, y1 = b["x0"], b["x1"], b["y0"], b["y1"]
    wt = 0.32
    top = lambda x, y: roof_z(x, y) - 0.02  # noqa: E731
    # solid tuff walls: west, north (with window opening), east
    B.box("w_west", x0, y0, f0, x0 + wt, y1, top(x0, y1), M["tuff"], "building")
    B.box("w_east", x1 - wt, y0 + 2.6, f0, x1, y1, top(x1, y1), M["tuff"], "building")
    # north wall split around the pickup window (W) and a service door
    wx0, wx1 = WINDOW_X - 0.9, WINDOW_X + 0.9
    B.box("w_north_a", x0, y1 - wt, f0, wx0, y1, top(x0, y1), M["tuff"], "building")
    B.box("w_north_b", wx1, y1 - wt, f0, x1, y1, top(x1, y1), M["tuff"], "building")
    B.box("w_north_sill", wx0, y1 - wt, f0, wx1, y1, 1.05, M["tuff"], "building")
    B.box("w_north_head", wx0, y1 - wt, 2.25, wx1, y1, top(WINDOW_X, y1), M["tuff"], "building")
    B.box("win_glass", wx0, y1 - 0.18, 1.05, wx1, y1 - 0.12, 2.25, M["glass"], "building")
    B.box("win_frame", wx0 - 0.08, y1 - 0.02, 0.98, wx1 + 0.08, y1 + 0.12, 2.32, M["bronze"], "building")
    B.box("win_shelf", wx0, y1, 1.02, wx1, y1 + 0.38, 1.08, M["bronze"], "building")
    # south facade: full glazing with bronze mullions + walk-up window, east corner glazed too
    B.box("s_glass", x0 + wt, y0, f0, x1, y0 + 0.06, 3.3, M["glass"], "building")
    B.box("e_glass", x1 - 0.06, y0, f0, x1, y0 + 2.6, 3.3, M["glass"], "building")
    s = x0 + wt
    while s <= x1 + 0.01:
        B.box(f"s_mull_{s:.1f}", s - 0.04, y0 - 0.08, f0, s + 0.04, y0 + 0.08, 3.35, M["bronze"], "building")
        s += 1.5
    B.box("s_transom", x0 + wt, y0 - 0.08, 3.3, x1, y0 + 0.08, top(x1, y0), M["bronze"], "building")
    B.box("walkup_shelf", 51.2, y0 - 0.42, 1.0, 53.6, y0, 1.06, M["bronze"], "building")
    # interior (visible through the glazing): floor, counter, back wall in brand teal, menu screen, glow
    B.box("floor", x0 + wt, y0 + 0.06, f0 - 0.01, x1 - wt, y1 - wt, f0, M["floor_int"], "interior")
    B.box("counter", x0 + 1.4, y0 + 2.2, f0, x1 - 1.0, y0 + 2.9, f0 + 1.0, M["tuff_dark"], "interior")
    B.box("counter_top", x0 + 1.35, y0 + 2.15, f0 + 1.0, x1 - 0.95, y0 + 2.95, f0 + 1.05, M["counter"], "interior")
    B.box("backwall", x0 + wt, y0 + 4.6, f0, x1 - wt, y0 + 4.72, 3.2, M["primary"], "interior")
    mi = B.BRAND.get("textures", {}).get("menu_interior")
    B.image_plane("menu_int", mi, (x0 + x1) / 2, y0 + 4.58, 2.35, 3.6, 1.1, "S", emit=2.5 if night else 1.0, cname="interior")
    B.box("ceiling", x0 + wt, y0 + 0.06, 3.32, x1 - wt, y1 - wt, 3.36, M["oak"], "interior")
    for k in range(3):
        cx = x0 + 2.5 + k * 3.5
        B.box(f"pend_{k}", cx - 0.18, y0 + 1.2, 2.55, cx + 0.18, y0 + 1.56, 2.75, M["led_warm"], "interior")
    for k in range(3):
        if True:
            ld = bpy.data.lights.new(f"int_{k}", "POINT"); ld.energy = 120 if night else 90; ld.color = (1, 0.8, 0.6)
            lo = bpy.data.objects.new(f"int_{k}", ld); lo.location = (x0 + 2.5 + k * 3.5, y0 + 2.0, 2.9); B.link(lo, "lights_interior")
    # roof: hypar slab, oak soffit underneath, membrane on top, bronze fascia edge
    grid_surface("roof", ROOF["x0"], ROOF["x1"], ROOF["y0"], ROOF["y1"], roof_z, M["oak"], n=24, thick=ROOF["t"], mat_edge=M["membrane"])
    for (fx, side) in ((ROOF["y0"], "S"), (ROOF["y1"], "N")):
        pts = [(ROOF["x0"] + (ROOF["x1"] - ROOF["x0"]) * i / 24, fx) for i in range(25)]
        verts = [(x, y, roof_z(x, y) - 0.02) for x, y in pts] + [(x, y, roof_z(x, y) + ROOF["t"] + 0.05) for x, y in pts]
        faces = [(i, i + 1, 26 + i, 25 + i) for i in range(24)]
        o = 0.03 if side == "N" else -0.03
        verts = [(x, y + o, z) for (x, y, z) in verts]
        B.mesh_obj(f"fascia_{side}", verts, faces, [M["bronze"]], "building")
    if night:
        B.strip("roof_led_s", [(ROOF["x0"], ROOF["y0"] - 0.05), (ROOF["x1"], ROOF["y0"] - 0.05)], 0.05, 0.0, M["led_warm"], cname="building")
    # roof posts at the free corners (SE and SW overhang over the walk-up) and fascia wordmark
    for (px, py) in ((47.0, 20.0), (61.2, 20.0), (61.2, 31.0)):
        B.box(f"post_{px}_{py}", px - 0.09, py - 0.09, 0.15, px + 0.09, py + 0.09, roof_z(px, py), M["bronze"], "building")
    fw = B.BRAND.get("textures", {}).get("wordmark_fascia")
    B.image_plane("fascia_word_S", fw, 51.0, ROOF["y0"] - 0.035, roof_z(51.0, ROOF["y0"]) + ROOF["t"] / 2, 3.6, 0.22, "S", emit=5.0 if night else 0.0, offset=0.0)
    B.image_plane("fascia_word_N", fw, 52.0, ROOF["y1"] + 0.035, roof_z(52.0, ROOF["y1"]) + ROOF["t"] / 2, 3.6, 0.22, "N", emit=5.0 if night else 0.0, offset=0.0)
    # tower
    t = TOWER
    B.box("tower", t["x"] - t["w"] / 2, t["y"] - t["d"] / 2, 0.0, t["x"] + t["w"] / 2, t["y"] + t["d"] / 2, t["h"], M["tuff"], "building")
    B.box("tower_cap", t["x"] - t["w"] / 2 - 0.03, t["y"] - t["d"] / 2 - 0.03, t["h"], t["x"] + t["w"] / 2 + 0.03, t["y"] + t["d"] / 2 + 0.03, t["h"] + 0.08, M["bronze"], "building")
    logo = B.BRAND.get("textures", {}).get("logo_tower")
    for fac in ("S", "E", "N", "W"):
        if fac in ("S", "N"):
            yy = t["y"] - t["d"] / 2 if fac == "S" else t["y"] + t["d"] / 2
            B.image_plane(f"tower_logo_{fac}", logo, t["x"], yy, t["h"] - 0.9, 1.05, 1.05, fac, emit=3.0 if night else 0.0, offset=0.012)
        else:
            xx = t["x"] + t["w"] / 2 if fac == "E" else t["x"] - t["w"] / 2
            B.image_plane(f"tower_logo_{fac}", logo, xx, t["y"], t["h"] - 0.9, 1.05, 1.05, fac, emit=3.0 if night else 0.0, offset=0.012)
    # order point: menu board + speaker + small canopy (driver's left heading north)
    ox, oy = ORDER
    B.box("mb_post", ox - 0.14, oy - 1.15, 0.15, ox + 0.14, oy + 1.15, 2.55, M["bronze_matte"], "signage")
    mb = B.BRAND.get("textures", {}).get("menu_board")
    B.image_plane("mb_screen", mb, ox + 0.15, oy, 1.78, 2.05, 1.18, "E", emit=3.0 if night else 1.4)
    B.box("speaker", ox - 0.1, oy - 2.3, 0.15, ox + 0.22, oy - 1.85, 1.3, M["bronze_matte"], "signage")
    B.box("ord_canopy", ox - 0.4, oy - 3.0, 3.6, LANE_X + 1.9, oy + 2.0, 3.78, M["oak"], "building")
    B.box("ord_canopy_top", ox - 0.42, oy - 3.02, 3.78, LANE_X + 1.92, oy + 2.02, 3.86, M["bronze"], "building")
    for (px, py) in ((ox - 0.25, oy - 2.8), (ox - 0.25, oy + 1.8)):
        B.box(f"ord_post_{py:.1f}", px - 0.08, py - 0.08, 0.15, px + 0.08, py + 0.08, 3.6, M["bronze"], "building")
    # pylon at the shared entry (twin-tenant: CHAMPA panel)
    pl = B.BRAND.get("textures", {}).get("pylon_face")
    px, py, pw, pd, ph = 71.0, 1.7, 1.7, 0.55, 6.2
    B.box("pylon", px - pw / 2, py - pd / 2, 0.0, px + pw / 2, py + pd / 2, ph, M["tuff"], "signage")
    B.box("pylon_cap", px - pw / 2 - 0.03, py - pd / 2 - 0.03, ph, px + pw / 2 + 0.03, py + pd / 2 + 0.03, ph + 0.08, M["bronze"], "signage")
    for fac in ("S", "N"):
        yy = py - pd / 2 if fac == "S" else py + pd / 2
        B.image_plane(f"pylon_face_{fac}", pl, px, yy, ph - 2.0, 1.45, 3.65, fac, emit=2.2 if night else 0.0, offset=0.012)
    # terrace furniture
    tset = B.template("outdoor_table_chair_set_01", "outdoor_table_chair_set_01")
    for k, (tx, ty) in enumerate([(49.0, 17.6), (53.5, 17.6), (58.0, 17.6)]):
        B.instance(tset, f"terrace_set_{k}", tx, ty, 0.15, 90 * (k % 2), 1.0, "furniture")
    plant = B.template("planter_box_01", "planter_box_01")
    for k, px_ in enumerate((46.2, 63.9)):
        B.instance(plant, f"planter_{k}", px_, 16.4, 0.15, 0, 1.0, "furniture")


def build_greenery(M, quality):
    tA = B.template("island_tree_01", "island_tree_01_LOD1")
    tB = B.template("tree_small_02", "tree_small_02_LOD1")
    pts = [(70.5, 10, tB), (71, 22, tA), (70.6, 34, tB), (71.5, 41, tA), (46, 38.5, tB), (56, 40.5, tA), (64, 38, tB),
           (35.5, 25, tA), (37.5, 31.5, tB), (10, 41.5, tB), (25, 42, tA), (60.0, 4.2, tB), (49.0, 4.2, tB)]
    for k, (x, y, t) in enumerate(pts):
        B.instance(t, f"tree_{k}", x, y, 0.17, k * 47 % 360, 0.9 + 0.1 * (k % 3))
    grass = B.template("grass_medium_01", "grass_medium_01_LOD1")
    import random
    rnd = random.Random(5)
    if grass:
        for k in range(700 if quality == "final" else 150):
            x = rnd.uniform(-160, 230); y = rnd.uniform(46, 140)
            B.instance(grass, f"steppe_grass_{k}", x, y, B.terrain_height(x, y) - 0.05, rnd.uniform(0, 360), rnd.uniform(0.8, 1.5))
        for poly in ([(68.8, 3.2), (73.6, 43.6)], [(40.2, 34.2), (68.2, 43.6)]):
            (ax, ay), (bx, by) = poly
            for k in range(int((bx - ax) * (by - ay) * (0.5 if quality == "final" else 0.15))):
                B.instance(grass, f"gr_{ax}_{k}", rnd.uniform(ax, bx), rnd.uniform(ay, by), 0.17, rnd.uniform(0, 360), rnd.uniform(0.7, 1.1))
    for k in range(60):
        x = rnd.uniform(-450, 550); y = rnd.uniform(150, 600)
        B.instance(rnd.choice([tA, tB]), f"far_tree_{k}", x, y, B.terrain_height(x, y) - 0.2, rnd.uniform(0, 360), rnd.uniform(1.0, 1.6))


def build_cars(night):
    import cars as CARS
    lamp = {"head": B.MM["head"], "tail": B.MM["tail"]}
    C = B.CAR_COLORS

    def car(n, kind, col, x, y, h, lights=False):
        return CARS.make_car(n, kind, col, x, y, h, lights_on=lights, link_fn=B.link, mats=lamp, seed=hash(n) % 9973)
    # drive-thru: one at the window, one at the order point, three stacked
    car("dt_window", "suv", C[0], WINDOW_X + 1.9, LANE_Y, 180, night)
    car("dt_order", "sedan", C[5], LANE_X, ORDER[1] + 0.6, 90, night)
    for k, (y, kind) in enumerate([(15.6, "hatch"), (9.9, "sedan"), (4.2, "lada")]):
        car(f"dt_q{k}", kind, C[(k * 3 + 1) % len(C)], LANE_X, y, 90, night)
    # host forecourt
    for k, (x, y, h, kind) in enumerate([(12.33, 14.5, 90, "sedan"), (18.0, 14.2, 270, "suv"), (23.67, 14.8, 90, "van")]):
        car(f"fuel_{k}", kind, C[(k * 2 + 3) % len(C)], x, y, h, False)
    # parking
    for k, (i, kind) in enumerate([(1, "ev"), (3, "sedan"), (5, "hatch")]):
        car(f"park_{k}", kind, C[(k * 4 + 2) % len(C)], 47.9 + i * 2.6, 8.7, 90, False)
    hw = B.L["highway"]
    nl1 = sum(hw["north"]["lane1"]) / 2; nl2 = sum(hw["north"]["lane2"]) / 2
    sl1 = sum(hw["south"]["lane1"]) / 2; sl2 = sum(hw["south"]["lane2"]) / 2
    for i, (x, y, h, k) in enumerate([(120, nl1, 180, "sedan"), (-35, nl1, 180, "suv"), (78, nl2, 180, "ev"), (10, sl1, 0, "van"),
                                      (95, sl1, 0, "sedan"), (-70, sl2, 0, "lada"), (160, sl2, 0, "suv")]):
        car(f"h{i}", k, C[(i * 5 + 1) % len(C)], x, y, h, night)


def lights(night):
    if not night:
        return
    for k, (x, y) in enumerate([(44.5, 14.0), (66.0, 14.0), (44.5, 33.0), (66.0, 33.0), (56.0, 3.5), (36.0, 3.5)]):
        ld = bpy.data.lights.new(f"pole_{k}", "SPOT"); ld.energy = 4200; ld.spot_size = math.radians(115); ld.spot_blend = 0.5
        ld.color = (1.0, 0.86, 0.68)
        lo = bpy.data.objects.new(f"pole_{k}", ld); lo.location = (x, y, 7.8); B.link(lo, "lights_exterior")
        B.box(f"pole_mast_{k}", x - 0.08, y - 0.08, 0.0, x + 0.08, y + 0.08, 8.0, B.MM["steel_dark"], "site")
    for (x, y, z, e, tgt) in ((71.0, -0.8, 0.5, 450, (71.0, 1.7, 5.0)), (62.4, 18.6, 0.3, 380, (62.4, 20.6, 6.5))):
        ld = bpy.data.lights.new("wash", "SPOT"); ld.energy = e; ld.spot_size = math.radians(30); ld.color = (1, 0.8, 0.6)
        lo = bpy.data.objects.new("wash", ld); lo.location = (x, y, z); B.look_at(lo, tgt); B.link(lo, "lights_exterior")
    ox, oy = ORDER
    ld = bpy.data.lights.new("ord_light", "SPOT"); ld.energy = 220; ld.spot_size = math.radians(90); ld.color = (1, 0.82, 0.6)
    lo = bpy.data.objects.new("ord_light", ld); lo.location = (LANE_X, oy, 3.5); B.link(lo, "lights_exterior")


def cameras():
    c = {}
    c["c_aerial"] = B.add_camera("cam_c_aerial", (86.0, -27.0, 30.0), (44.0, 21.0, 0.0), lens=30)
    c["c_hero"] = B.add_camera("cam_c_hero", (63.2, 4.6, 1.65), (53.0, 22.5, 3.0), lens=22, shift_y=0.07)
    c["c_walkup"] = B.add_camera("cam_c_walkup", (42.0, 9.5, 1.6), (55.0, 22.5, 2.6), lens=24, shift_y=0.05)
    c["c_window"] = B.add_camera("cam_c_window", (63.5, 34.0, 1.45), (50.0, 30.5, 2.1), lens=24)
    c["c_top"] = B.add_camera("cam_c_top", (37.0, 22.0, 300.0), (37.0, 22.0, 0.0), ortho=82)
    return c


def build(mode="day", quality="final"):
    B.reset()
    B.MATS.clear(); B.TEMPLATES.clear(); B.COLLS.clear()
    night = mode in ("dusk", "night")
    B.set_haze(night)
    M = B.init_materials()
    B.MM.clear(); B.MM.update(M)
    terr = B.build_terrain(M)
    B.build_ararat()
    try:
        import terrain as TER
        TER.build_landscape(B.link, B.terrain_height, terrain_obj=terr, haze_emit=B.HAZE_EMIT[0], quality=quality)
    except Exception as ex:
        print("landscape module failed:", ex)
    B.build_highway(M)
    build_site(M)
    build_host(M, night)
    build_pavilion(M, night)
    build_greenery(M, quality)
    build_cars(night)
    lights(night)
    B.setup_world(mode)
    B.set_light_mode(night)
    return cameras()


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    arg = lambda k, d: argv[argv.index(k) + 1] if k in argv else d  # noqa: E731
    mode = arg("--mode", "day")
    views = arg("--views", "c_aerial").split(",")
    pct = int(arg("--pct", "50"))
    out = arg("--out", f"{B.ROOT}/design/renders/final")
    os.makedirs(out, exist_ok=True)
    cams = build(mode, arg("--quality", "final" if pct >= 100 else "preview"))
    B.render_settings(samples=int(arg("--samples", "64")), res=(1920, 1080), pct=pct)
    sc = bpy.context.scene
    for v in views:
        sc.camera = cams[v]
        sc.render.filepath = f"{out}/{v}_{mode}.png"
        t = time.time()
        bpy.ops.render.render(write_still=True)
        print(f"RENDERED {v} {mode} in {time.time() - t:.1f}s -> {sc.render.filepath}")
