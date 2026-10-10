"""
Parametric site & building layout for the recommended mid-range drive-thru prototype.

Single source of truth for geometry. Both the Blender scene builder (design/3d/build_scene.py)
and the 2D drawing generator (design/drawings/make_drawings.py) read the JSON written by this
module, so renders, site plan, floor plan and elevations are dimensionally consistent.

Coordinate system (metres):
    x  -> east, along the highway frontage (site spans x = 0 .. SITE_W)
    y  -> north, away from the highway       (site spans y = 0 .. SITE_D)
    z  -> up
The highway runs east-west south of the site (y < 0). Traffic drives on the right, so the
near (north) carriageway carries WESTBOUND traffic: vehicles approach from the east, enter at
the east driveway (right-in) and leave from the west driveway (right-out). Cars are left-hand
drive, so the drive-thru circulates counter-clockwise with the building on the driver's left.

Run:  python3 design/site_layout.py   ->  writes design/layout.json
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path(__file__).with_name("layout.json")

# --------------------------------------------------------------------------------------
# Global parameters
# --------------------------------------------------------------------------------------
SITE_W = 74.0          # frontage length (m)
SITE_D = 44.0          # depth (m)

LANE_W = 3.5           # drive-thru lane width
HWY_LANE = 3.75        # highway lane width
CAR_PITCH = 6.0        # stacking length per queued car (industry planning norm 5.5-6.5 m)

# Building footprint (enclosed, gross external)
BLD_X0, BLD_X1 = 24.0, 43.0
BLD_Y0, BLD_Y1 = 24.0, 33.0
BLD_H_WEST, BLD_H_EAST = 4.2, 5.4       # parapet / roof underside heights (roof lifts to the east)
FFL = 0.15                               # finished floor level above site asphalt

# Roof plane (oversails the building)
ROOF = dict(x0=21.0, x1=46.4, y0=20.4, y1=36.6, z_nw=4.15, z_ne=4.55, z_sw=4.95, z_se=7.30, thickness=0.42,
            z_west=4.15, z_east=7.30, wall_top=3.55,
            form="hyperbolic paraboloid (ruled bilinear surface) - glulam/steel ruled framing, oak batten soffit")

# Brand tower and highway pylon
TOWER = dict(x=45.7, y=21.5, w=1.9, d=1.9, h=11.0)
PYLON = dict(x=71.2, y=1.6, w=2.2, d=0.7, h=8.0)


def arc(cx, cy, r, a0, a1, n=24):
    """Points on a circular arc, angles in degrees (counter-clockwise positive)."""
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((round(cx + r * math.cos(a), 3), round(cy + r * math.sin(a), 3)))
    return pts


def polyline_length(pts):
    return sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))


def point_at(pts, s):
    """Point and heading (deg) at distance s along a polyline."""
    acc = 0.0
    for i in range(len(pts) - 1):
        seg = math.dist(pts[i], pts[i + 1])
        if acc + seg >= s:
            t = (s - acc) / seg
            x = pts[i][0] + t * (pts[i + 1][0] - pts[i][0])
            y = pts[i][1] + t * (pts[i + 1][1] - pts[i][1])
            h = math.degrees(math.atan2(pts[i + 1][1] - pts[i][1], pts[i + 1][0] - pts[i][0]))
            return (round(x, 3), round(y, 3)), round(h, 2)
        acc += seg
    p, q = pts[-2], pts[-1]
    return q, round(math.degrees(math.atan2(q[1] - p[1], q[0] - p[0])), 2)


def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]


# --------------------------------------------------------------------------------------
# Highway (two carriageways, 2 x 2 lanes, central barrier) south of the site
# --------------------------------------------------------------------------------------
def highway():
    y_edge = -6.0                       # north edge of paved shoulder (6 m verge to boundary)
    sh_out, sh_in, median = 2.5, 0.75, 3.0
    n_c = {}                            # north carriageway (westbound)
    y = y_edge
    n_c["shoulder"] = (y - sh_out, y); y -= sh_out
    n_c["lane1"] = (y - HWY_LANE, y); y -= HWY_LANE
    n_c["lane2"] = (y - HWY_LANE, y); y -= HWY_LANE
    n_c["shoulder_in"] = (y - sh_in, y); y -= sh_in
    med = (y - median, y); y -= median
    s_c = {}
    s_c["shoulder_in"] = (y - sh_in, y); y -= sh_in
    s_c["lane2"] = (y - HWY_LANE, y); y -= HWY_LANE
    s_c["lane1"] = (y - HWY_LANE, y); y -= HWY_LANE
    s_c["shoulder"] = (y - sh_out, y); y -= sh_out
    x0, x1 = -900.0, 900.0
    return dict(x0=x0, x1=x1, north=n_c, median=med, south=s_c, y_edge=y_edge, y_far=y,
                speed_limit_kmh=90,
                note="Generic 2x2 divided interstate cross-section; confirm against actual M4 survey.")


def aux_lanes(hw):
    """Deceleration lane (east, entry) and acceleration lane (west, exit) on the near side."""
    y_out = hw["y_edge"]                 # outer edge of shoulder
    y_in = hw["north"]["lane1"][1]       # outer edge of lane 1 (= inner edge of shoulder)
    # aux lane occupies the shoulder plus 1.0 m of verge: y in [y_in, y_in+3.5]
    ya, yb = y_in, y_in + 3.5
    decel = dict(
        taper=[(150.0, ya), (110.0, yb)],          # 40 m taper (approach from east)
        full=[(110.0, ya), (64.0, ya), (64.0, yb), (110.0, yb)],
        length_total=86.0,
        note="Indicative: 40 m taper + 46 m parallel decel lane for 90 km/h; final per Armenian norms/Roads Dept.")
    accel = dict(
        full=[(11.0, ya), (-60.0, ya), (-60.0, yb), (11.0, yb)],
        taper=[(-60.0, yb), (-110.0, ya)],
        length_total=121.0,
        note="Indicative: 71 m parallel accel lane + 50 m taper; final per Armenian norms/Roads Dept.")
    return dict(decel=decel, accel=accel, y_inner=ya, y_outer=yb)


# --------------------------------------------------------------------------------------
# Site circulation
# --------------------------------------------------------------------------------------
def circulation():
    # Drive-thru centreline: entry throat -> east double stack (lanes A/B) -> merge -> window lane -> exit
    lane_a_x, lane_b_x = 59.75, 64.25    # centrelines of the two stacking lanes
    stack_y0, stack_y1 = 12.5, 27.0
    win_y = 35.35                         # window lane centreline (north facade at y=33 + 0.6 m kerb + 1.75)
    west_x = 12.25                        # west return lane centreline

    lane_a = [(lane_a_x, stack_y0), (lane_a_x, stack_y1)]
    lane_b = [(lane_b_x, stack_y0), (lane_b_x, stack_y1)]
    # merge curve from the double stack into the single window lane
    merge = [(62.0, 27.0)] + arc(54.0, win_y - 8.0, 8.0, 0, 90, 18)
    window_lane = [(54.0, win_y), (18.25, win_y)]
    nw_turn = arc(18.25, win_y - 6.0, 6.0, 90, 180, 16)
    west_lane = [(west_x, win_y - 6.0), (west_x, 9.0)]
    exit_curve = arc(6.25, 9.0, 6.0, 0, -90, 12)
    drive_path = ([(67.0, -2.0), (67.0, 6.0)] + arc(61.0, 6.0, 6.0, 0, 90, 8)[1:2] +
                  [(lane_a_x, 10.0)] + lane_a + merge[1:] + window_lane[1:] + nw_turn[1:] + west_lane[1:] +
                  [(west_x, 4.0), (7.0, 0.0), (7.0, -3.0)])

    windows = [
        dict(id="W1", label="Order confirm / payment", x=39.6, y=33.0, facing="north"),
        dict(id="W2", label="Pickup / hand-off", x=31.4, y=33.0, facing="north"),
    ]
    order_points = [
        dict(id="OP-A", lane="A", x=57.55, y=24.0, heading=90, note="digital menu board + speaker, left of lane A"),
        dict(id="OP-B", lane="B", x=62.0, y=24.0, heading=90, note="digital menu board + speaker on 1.0 m island"),
    ]
    preview_boards = [dict(x=57.55, y=15.0), dict(x=62.0, y=15.0)]

    # stacking capacity (cars), measured from pickup window back to the site entry
    window_to_merge = polyline_length([(31.4, win_y), (54.0, win_y)])
    merge_len = polyline_length(merge)
    stack_len = stack_y1 - stack_y0
    throat = 10.0
    capacity = dict(
        window_lane_cars=round(window_to_merge / CAR_PITCH, 1),
        merge_cars=round(merge_len / CAR_PITCH, 1),
        double_stack_cars=round(2 * stack_len / CAR_PITCH, 1),
        throat_cars=round(throat / CAR_PITCH, 1),
    )
    capacity["total_from_pickup_window"] = round(sum(capacity.values()), 1)
    capacity["behind_order_points"] = round(2 * (24.0 - stack_y0) / CAR_PITCH + throat / CAR_PITCH, 1)

    return dict(lane_a=lane_a, lane_b=lane_b, merge=merge, window_lane=window_lane, nw_turn=nw_turn,
                west_lane=west_lane, exit_curve=exit_curve, drive_path=drive_path, windows=windows,
                order_points=order_points, preview_boards=preview_boards, capacity=capacity,
                lane_width=LANE_W, car_pitch=CAR_PITCH,
                parking_aisle=dict(y0=9.0, y1=15.0, x0=11.0, x1=63.0, oneway="westbound", width=6.0))


# --------------------------------------------------------------------------------------
# Hard & soft landscape (raised kerbed elements over the asphalt base)
# --------------------------------------------------------------------------------------
def landscape():
    L = []
    # Frontage strip (between boundary and parking), split by entry/exit driveways
    L.append(dict(id="frontage_w", kind="planting", poly=rect(11.0, 0.0, 14.0, 4.0)))
    L.append(dict(id="frontage_c", kind="planting", poly=rect(14.0, 0.0, 58.5, 3.4)))
    L.append(dict(id="frontage_e", kind="planting", poly=rect(58.5, 0.0, 63.0, 9.0)))
    L.append(dict(id="frontage_ee", kind="planting", poly=rect(71.0, 0.0, 74.0, 44.0)))
    L.append(dict(id="frontage_ww", kind="planting", poly=rect(0.0, 0.0, 3.0, 44.0)))
    # North buffer
    L.append(dict(id="north_buffer", kind="planting", poly=rect(3.0, 37.6, 71.0, 44.0)))
    # Island between stacking lanes and building east side
    L.append(dict(id="stack_island", kind="planting",
                  poly=[(48.0, 15.5), (57.5, 15.5), (57.5, 26.5), (54.0, 30.4), (48.0, 30.4)]))
    # Narrow lane-separation island at order points (between lanes A and B)
    L.append(dict(id="op_island", kind="island", poly=rect(61.5, 19.0, 62.5, 26.0)))
    # Island inside the east loop (east of lane B)
    L.append(dict(id="east_island", kind="planting", poly=[(66.5, 12.0), (71.0, 12.0), (71.0, 37.6), (62.0, 37.6), (66.5, 31.0)]))
    # Island inside NW turn / west of terrace
    L.append(dict(id="west_island", kind="planting", poly=[(14.5, 15.5), (15.5, 15.5), (15.5, 29.0), (14.5, 29.0)]))
    # Parking end islands
    L.append(dict(id="park_end_w", kind="planting", poly=rect(14.0, 3.4, 16.0, 9.0)))
    L.append(dict(id="park_end_e", kind="planting", poly=rect(56.5, 3.4, 58.5, 9.0)))
    L.append(dict(id="park_n_end_e", kind="planting", poly=rect(45.5, 15.0, 48.0, 20.0)))
    # Pedestrian plaza (basalt pavers) in front of building + walkway east of building
    L.append(dict(id="plaza", kind="plaza", poly=[(15.5, 20.0), (48.0, 20.0), (48.0, 33.0), (43.0, 33.0),
                                                   (43.0, 24.0), (24.0, 24.0), (24.0, 33.0), (19.5, 33.0),
                                                   (15.5, 29.0)]))
    # Building pad (under footprint)
    L.append(dict(id="building_pad", kind="pad", poly=rect(BLD_X0, BLD_Y0, BLD_X1, BLD_Y1)))
    # kerb between window lane and building (0.6 m)
    L.append(dict(id="window_kerb", kind="island", poly=rect(BLD_X0 - 4.5, BLD_Y1, BLD_X1 + 5.0, BLD_Y1 + 0.6)))
    return L


def parking():
    stalls = []
    # South row (nose to highway): x 16.0 .. 56.5, stall depth 5.0 (y 4.0..9.0)
    x = 16.0
    i = 0
    south_types = ["std"] * 13 + ["ev", "ev"]
    w = (56.5 - 16.0) / len(south_types)
    for t in south_types:
        stalls.append(dict(id=f"S{i+1:02d}", type=t, x=round(x + w / 2, 3), y=6.45, w=round(w, 3), l=5.0, heading=90))
        x += w; i += 1
    # North row (nose to plaza): x 16.0 .. 45.5, y 15.0..20.0
    north = [("acc", 3.6), ("acc", 3.6)] + [("std", 2.6)] * 8 + [("long", 0)]
    x = 16.0
    for j, (t, wid) in enumerate(north):
        if t == "long":
            break
        stalls.append(dict(id=f"N{j+1:02d}", type=t, x=round(x + wid / 2, 3), y=17.5, w=wid, l=5.0, heading=-90))
        x += wid
    counts = {}
    for s in stalls:
        counts[s["type"]] = counts.get(s["type"], 0) + 1
    long_bay = dict(id="LV1", type="long_vehicle", poly=rect(16.0, 9.0, 34.0, 12.2),
                    note="Long-vehicle bay (minibus/campervan/coach drop-off) along aisle; time-limited")
    return dict(stalls=stalls, counts=counts, total=len(stalls), long_bay=long_bay)


# --------------------------------------------------------------------------------------
# Building: rooms (for floor plan), facade elements (for 3D + elevations)
# --------------------------------------------------------------------------------------
def building():
    x0, x1, y0, y1 = BLD_X0, BLD_X1, BLD_Y0, BLD_Y1
    mid = 28.0   # line between customer (south) band and production (north) band
    rooms = [
        dict(id="R1", name="Drive-thru bar & beverage line", x0=29.0, y0=mid, x1=x1, y1=y1,
             note="14 m linear line: cold bar | 2x espresso | POS/W1 | food finish | W2"),
        dict(id="R2", name="Back-of-house: dry store + walk-in cooler", x0=x0, y0=mid, x1=29.0, y1=y1),
        dict(id="R3", name="Walk-in café & order counter (12 seats)", x0=35.0, y0=y0, x1=x1, y1=mid),
        dict(id="R4", name="Guest restrooms (2 accessible, unisex) + baby change", x0=29.5, y0=y0, x1=35.0, y1=mid),
        dict(id="R5", name="Staff room, lockers & office", x0=x0, y0=y0, x1=27.0, y1=mid),
        dict(id="R6", name="Staff WC / mop sink / plant & IT", x0=27.0, y0=y0, x1=29.5, y1=mid),
    ]
    for r in rooms:
        r["area_m2"] = round((r["x1"] - r["x0"]) * (r["y1"] - r["y0"]), 1)
    gross = (x1 - x0) * (y1 - y0)

    # Equipment schedule placed in the bar (for floor plan + 3D cutaway). (x0,y0,x1,y1, height)
    equipment = [
        dict(tag="E01", name="Ice machine + bin", box=(41.6, 31.6, 42.9, 32.9), h=1.9),
        dict(tag="E02", name="Blender station (2x) + cold-brew taps", box=(40.0, 31.9, 41.5, 32.9), h=1.0),
        dict(tag="E03", name="Espresso machine 3-group (drive-thru)", box=(37.0, 31.9, 39.4, 32.9), h=1.05),
        dict(tag="E04", name="Grinders (2) + knock box", box=(36.1, 31.9, 36.9, 32.9), h=1.35),
        dict(tag="E05", name="POS + order-confirm screen at W1", box=(39.4, 32.2, 40.0, 32.9), h=1.1),
        dict(tag="E06", name="Espresso machine 2-group (café/back-up)", box=(36.6, 28.1, 38.6, 29.0), h=1.05),
        dict(tag="E07", name="Batch brewer + hot water tower", box=(35.2, 31.9, 36.0, 32.9), h=1.3),
        dict(tag="E08", name="Under-counter fridges (milk/cream) x4", box=(33.0, 31.9, 35.1, 32.9), h=0.9),
        dict(tag="E09", name="High-speed ovens (2) + food finish", box=(29.6, 31.9, 32.4, 32.9), h=1.15),
        dict(tag="E10", name="Hand-wash sinks (2) & 3-compartment sink", box=(29.2, 28.1, 31.6, 28.9), h=0.9),
        dict(tag="E11", name="Pastry display case (café counter)", box=(38.8, 28.1, 41.0, 29.0), h=1.3),
        dict(tag="E12", name="Café POS + pickup plane", box=(41.0, 28.1, 42.9, 29.0), h=1.1),
        dict(tag="E13", name="Walk-in cooler 2.4 x 2.0 m", box=(24.2, 30.8, 26.6, 32.8), h=2.4),
        dict(tag="E14", name="Dry storage shelving", box=(26.8, 31.8, 28.8, 32.8), h=2.0),
        dict(tag="E15", name="Dishwasher (undercounter) + drying rack", box=(31.7, 28.1, 33.5, 28.9), h=0.9),
        dict(tag="E16", name="Reach-in freezer + fridge", box=(24.2, 28.2, 26.0, 29.2), h=2.0),
        dict(tag="E17", name="Syrup & sauce rail / cup dispensers (back-counter)", box=(33.6, 28.1, 36.4, 28.9), h=1.0),
    ]
    # Facade openings: list of (facade, from, to, sill, head, kind)
    openings = [
        # north (drive-thru) facade y=33: two service windows in a continuous bronze strip
        dict(facade="N", a=30.4, b=32.4, sill=0.95, head=2.45, kind="service_window", id="W2"),
        dict(facade="N", a=38.6, b=40.6, sill=0.95, head=2.45, kind="service_window", id="W1"),
        dict(facade="N", a=33.0, b=38.0, sill=1.25, head=2.45, kind="glazing"),
        # south facade y=24: full-height glazing to café, entrance door
        dict(facade="S", a=35.0, b=43.0, sill=0.0, head=None, kind="curtain_wall"),
        dict(facade="S", a=40.2, b=42.2, sill=0.0, head=2.6, kind="door", id="D1"),
        dict(facade="S", a=31.0, b=32.0, sill=0.0, head=2.2, kind="door_solid", id="D2"),   # restroom lobby
        # east facade x=43: full glazing café corner
        dict(facade="E", a=24.0, b=28.0, sill=0.0, head=None, kind="curtain_wall"),
        dict(facade="E", a=28.6, b=32.6, sill=1.25, head=2.45, kind="glazing"),
        # west facade x=24: staff door + high window
        dict(facade="W", a=25.0, b=26.0, sill=0.0, head=2.2, kind="door_solid", id="D3"),
        dict(facade="W", a=29.5, b=32.5, sill=1.8, head=2.4, kind="glazing"),
    ]
    return dict(x0=x0, x1=x1, y0=y0, y1=y1, ffl=FFL, h_west=BLD_H_WEST, h_east=BLD_H_EAST,
                gross_m2=round(gross, 1), rooms=rooms, equipment=equipment, openings=openings,
                roof=ROOF, tower=TOWER, pylon=PYLON,
                pergola=dict(x0=15.8, y0=20.6, x1=23.6, y1=28.6, z=3.2, slat=0.08, spacing=0.30),
                order_canopy=dict(x0=56.9, y0=21.2, x1=66.6, y1=26.8, z_n=3.7, z_s=4.25, thickness=0.22),
                materials=dict(
                    cladding="Armenian volcanic tuff, sawn 900x300x30 mm, apricot/rose blend, stack bond, open 6 mm joints",
                    frames="Anodised aluminium, dark bronze (thermally broken)",
                    glazing="Low-iron double glazing, solar-control coating",
                    soffit="Thermally-modified oak / ash battens 70x30 mm @ 100 mm",
                    fascia="Folded aluminium 450 mm, dark bronze, integrated LED line",
                    plinth="Fair-faced concrete 300 mm",
                    paving="Basalt pavers 600x300 (plaza); asphalt (lanes); concrete kerbs",
                ))


def trees():
    T = []
    # north buffer row
    for i, x in enumerate([8, 15, 22, 29, 36, 43, 50, 57, 64]):
        T.append(dict(kind="tree_a" if i % 2 == 0 else "tree_b", x=x, y=41.2 + (0.6 if i % 2 else 0), s=1.0 + 0.08 * (i % 3), rot=i * 37))
    # east island
    T += [dict(kind="tree_a", x=69.0, y=20.0, s=1.05, rot=10), dict(kind="tree_b", x=68.5, y=30.0, s=0.95, rot=80)]
    # frontage
    T += [dict(kind="tree_small", x=x, y=1.7, s=0.9, rot=x * 11) for x in (20, 30, 40, 50)]
    # stack island + plaza
    T += [dict(kind="tree_small", x=51.0, y=19.0, s=0.85, rot=33), dict(kind="tree_small", x=51.5, y=26.5, s=0.8, rot=120)]
    T += [dict(kind="tree_a", x=17.4, y=22.2, s=0.75, rot=200)]
    # west strip
    T += [dict(kind="tree_b", x=1.5, y=y, s=0.9, rot=y * 7) for y in (10, 22, 34)]
    return T


def lights():
    poles = [(20, 12.0), (36, 12.0), (52, 12.0), (68.8, 9.0), (68.8, 33.0), (40, 39.5), (12.0, 39.5), (1.5, 16.0)]
    return [dict(x=x, y=y, h=7.0) for x, y in poles]


def cars():
    """Representative vehicle positions for renders (queue, parking, highway)."""
    C = []
    # queue: two at windows, others in window lane / merge / stack lanes
    C.append(dict(x=31.4, y=35.35, heading=180, kind="suv"))
    C.append(dict(x=39.6, y=35.35, heading=180, kind="sedan"))
    C.append(dict(x=46.6, y=35.35, heading=180, kind="sedan"))
    C.append(dict(x=55.4, y=33.0, heading=150, kind="hatch"))
    for k, y in enumerate([23.8, 17.6, 11.4]):
        C.append(dict(x=59.75, y=y, heading=90, kind=["sedan", "suv", "sedan"][k]))
    for k, y in enumerate([23.8, 17.6]):
        C.append(dict(x=64.25, y=y, heading=90, kind=["suv", "hatch"][k]))
    # parked
    park = [("S03", "sedan"), ("S04", "suv"), ("S07", "hatch"), ("S10", "sedan"), ("S14", "ev"),
            ("N01", "suv"), ("N04", "sedan"), ("N05", "sedan"), ("N08", "hatch")]
    return C, park


def build():
    hw = highway()
    aux = aux_lanes(hw)
    circ = circulation()
    land = landscape()
    park = parking()
    bld = building()
    queue_cars, parked = cars()

    site_area = SITE_W * SITE_D
    built = bld["gross_m2"]
    paved_lanes = None  # computed in drawings from polygons if needed
    summary = dict(
        site_w=SITE_W, site_d=SITE_D, site_area_m2=site_area, site_area_ha=round(site_area / 10000, 3),
        building_gross_m2=built, roof_plane_m2=round((ROOF["x1"] - ROOF["x0"]) * (ROOF["y1"] - ROOF["y0"]), 1),
        site_coverage_pct=round(100 * built / site_area, 1),
        parking=park["counts"], parking_total=park["total"],
        stacking=circ["capacity"],
        terrace_m2=round((23.6 - 15.8) * (28.6 - 20.6), 1),
    )
    data = dict(meta=dict(title="Recommended prototype — mid-range highway drive-thru", units="m",
                          generator="design/site_layout.py"),
                summary=summary, site=dict(w=SITE_W, d=SITE_D, poly=rect(0, 0, SITE_W, SITE_D)),
                highway=hw, aux=aux, circulation=circ, landscape=land, parking=park, building=bld,
                trees=trees(), lights=lights(), cars=dict(queue=queue_cars, parked=parked))
    OUT.write_text(json.dumps(data, indent=1))
    return data


if __name__ == "__main__":
    d = build()
    print(json.dumps(d["summary"], indent=1))
