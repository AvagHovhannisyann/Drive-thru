"""
C-001: CHAMPA Compact (lean first unit, co-located on a host fuel-station forecourt).
Site plan 1:200 and pavilion floor plan 1:50 on one A1 sheet, from design/3d/compact_geom.py (same geometry as the 3D scene).
Run: python3 design/drawings/make_compact_plan.py
"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "3d"))
import make_drawings as D  # noqa: E402
from compact_geom import BLD, HOST, LANE_W, LANE_X, LANE_Y, ORDER, ROOF, TOWER, WEST_X, WINDOW_X  # noqa: E402

CAR_M = 6.0  # stacking length per car (m), same convention as the prototype


def stack_counts():
    win_to_corner = LANE_X - WINDOW_X
    east_leg = LANE_Y - 3.0
    total = win_to_corner + east_leg
    order_to_window = win_to_corner + (LANE_Y - ORDER[1])
    behind_order = ORDER[1] - 3.0
    return dict(total_m=total, total_cars=total / CAR_M, between=order_to_window / CAR_M, behind=behind_order / CAR_M)


def site(sh):
    k = sh
    D.hatch_defs(k)
    k.rect(0, 0, 74, 44, fill="url(#hAsph)", sw=0.5)
    # highway edge & shared access
    k.line((-4, -1.0), (78, -1.0), sw=0.35)
    k.text(37, -3.2, "SHARED HIGHWAY ACCESS (EXISTING HOST STATION ENTRY / EXIT)", size=3.2, weight=700, fill=D.GREY)
    k.arrow([(67.5, -3.0), (67.5, 1.5)], sw=0.7)
    k.arrow([(7.0, 1.5), (7.0, -3.0)], sw=0.7)
    # host station (generic), hatched grey
    x0, y0, x1, y1 = HOST["canopy"]
    k.rect(x0, y0, x1, y1, fill="#e7e6e2", stroke=D.GREY, sw=0.3, dash="1.2 0.8")
    k.text((x0 + x1) / 2, (y0 + y1) / 2 + 3.2, "HOST FUEL CANOPY", size=3.2, weight=700, fill=D.GREY)
    for cx in (9.5, 15.17, 20.83, 26.5):
        k.rect(cx - 0.7, 12.3, cx + 0.7, 16.7, fill="#cfcdc7", stroke=D.GREY, sw=0.2)
    sx0, sy0, sx1, sy1 = HOST["shop"]
    k.rect(sx0, sy0, sx1, sy1, fill="#d9d7d1", stroke=D.GREY, sw=0.3)
    k.text((sx0 + sx1) / 2, (sy0 + sy1) / 2 + 1.0, "HOST SHOP", size=3.2, weight=700, fill=D.GREY)
    k.text((sx0 + sx1) / 2, (sy0 + sy1) / 2 - 2.0, "shared WCs", size=2.8, fill=D.GREY)
    # planting
    for (a, b, c, d) in [(68.6, 3.0, 73.8, 43.8), (40.0, 34.0, 68.4, 43.8), (0.2, 40.0, 39.8, 43.8), (46.0, 3.0, 64.5, 5.6), (33.0, 22.5, 41.4, 33.5)]:
        k.rect(a, b, c, d, fill="url(#hPlant)", sw=0.2)
    # CHAMPA island (pavers) + terrace
    k.rect(45.4, 15.6, 64.7, 29.9, fill="url(#hPavers)", sw=0.3)
    # roof outline
    k.rect(ROOF["x0"], ROOF["y0"], ROOF["x1"], ROOF["y1"], stroke=D.PRIMARY, sw=0.3, dash="2 1")
    # building
    k.rect(BLD["x0"], BLD["y0"], BLD["x1"], BLD["y1"], fill="url(#hTuff)", sw=0.5)
    k.rect(BLD["x0"] + 0.32, BLD["y0"] + 0.06, BLD["x1"] - 0.32, BLD["y1"] - 0.32, fill="#fff", sw=0.2)
    k.text((BLD["x0"] + BLD["x1"]) / 2, 26.2, "CHAMPA COMPACT", size=3.0, weight=800, fill=D.PRIMARY)
    k.text((BLD["x0"] + BLD["x1"]) / 2, 24.0, "90 m² · FFL +0.15", size=3.0)
    t = TOWER
    k.rect(t["x"] - t["w"] / 2, t["y"] - t["d"] / 2, t["x"] + t["w"] / 2, t["y"] + t["d"] / 2, fill="url(#hTuff)", sw=0.4)
    k.text(t["x"] - 1.2, t["y"] - 2.6, "TOWER 7.5 m", size=3.2, anchor="end")
    k.text(53.5, 17.0, "TERRACE · 3 TABLES · WALK-UP WINDOW", size=2.8, weight=700)
    # drive-thru lane
    hw = LANE_W / 2
    path = [(LANE_X, 3.0), (LANE_X, LANE_Y), (WEST_X, LANE_Y), (WEST_X, 6.0)]
    k.poly([(LANE_X + hw, 3.0), (LANE_X + hw, LANE_Y + hw), (WEST_X - hw, LANE_Y + hw), (WEST_X - hw, 6.0)], close=False, sw=0.3)
    k.arrow(path, sw=0.8)
    k.circle(ORDER[0], ORDER[1], 0.6, fill=D.ACCENT, stroke=D.INK)
    k.text(ORDER[0] - 1.2, ORDER[1] + 0.8, "ORDER POINT", size=2.9, anchor="end", weight=700)
    k.text(WINDOW_X, BLD["y1"] + 0.6, "PICKUP WINDOW", size=2.9, weight=700)
    for i, y in enumerate((15.6, 9.9, 4.2)):
        k.car(LANE_X, y, 90, fill="#fff")
    k.car(LANE_X, ORDER[1] + 0.6, 90, fill="#fff")
    k.car(WINDOW_X + 1.9, LANE_Y, 180, fill="#fff")
    # parking
    for i in range(8):
        xx = 46.6 + i * 2.6
        k.line((xx, 6.2), (xx, 11.2), sw=0.2)
    k.rect(46.7, 6.3, 49.1, 11.1, fill=D.GREEN, sw=0.1, opacity=0.6)
    k.text(55.7, 12.4, "7 STALLS (1 EV)", size=2.8, weight=700)
    # pylon
    k.rect(70.15, 1.42, 71.85, 1.98, fill="url(#hTuff)", sw=0.3)
    k.text(71.0, 0.2, "PYLON 6.2 m", size=2.6)
    # dimensions
    k.dim((0, 44), (74, 44), 3.0, "74.00")
    k.dim((74, 0), (74, 44), -3.0, "44.00")
    k.dim((BLD["x0"], BLD["y0"]), (BLD["x1"], BLD["y0"]), -2.8, "12.00")
    k.dim((BLD["x0"], BLD["y0"]), (BLD["x0"], BLD["y1"]), 2.8, "7.50")
    s = stack_counts()
    k.text(LANE_X + 3.2, 14.0, f"STACK ≈ {s['total_cars']:.0f} CARS", size=3.0, anchor="start", weight=800, fill=D.ACCENT, rot=-90)
    k.north_arrow(k.P(70, 50)[0], k.P(70, 50)[1], size=12)
    k.text(37, 50, "C-001a  SITE PLAN 1:200", size=4.2, weight=800)
    return s


def floor(fp):
    D.hatch_defs(fp)
    x0, x1, y0, y1 = BLD["x0"], BLD["x1"], BLD["y0"], BLD["y1"]
    wt = 0.32
    # walls
    fp.rect(x0, y0, x0 + wt, y1, fill="url(#hTuff)", sw=0.4)
    fp.rect(x1 - wt, y0 + 2.6, x1, y1, fill="url(#hTuff)", sw=0.4)
    fp.rect(x0, y1 - wt, WINDOW_X - 0.9, y1, fill="url(#hTuff)", sw=0.4)
    fp.rect(WINDOW_X + 0.9, y1 - wt, x1, y1, fill="url(#hTuff)", sw=0.4)
    fp.rect(WINDOW_X - 0.9, y1 - 0.18, WINDOW_X + 0.9, y1 - 0.12, fill=D.GLASS, sw=0.2)
    fp.rect(x0 + wt, y0, x1, y0 + 0.06, fill=D.GLASS, sw=0.25)
    fp.rect(x1 - 0.06, y0, x1, y0 + 2.6, fill=D.GLASS, sw=0.25)
    # zones
    zones = [
        ("1", "Walk-up counter, pastry case, POS 2", 49.4, 24.2, 59.0, 24.9, "#efe7da"),
        ("2", "Drive-thru line: cold bar · 3-group espresso · POS/W · oven", 50.6, 27.3, 59.4, 28.9, "#efe7da"),
        ("3", "Dry store + reach-in cooler/freezer", x0 + wt, 26.7, 50.4, y1 - wt, "#e3e1dc"),
        ("4", "Staff WC + mop sink (enclosed)", x0 + wt, 24.95, 50.4, 26.6, "#e3e1dc"),
    ]
    for zid, name, a, b, c, d, fill in zones:
        fp.rect(a, b, c, d, fill=fill, sw=0.25)
        fp.circle((a + c) / 2, (b + d) / 2, 0.32, fill="#fff", stroke=D.INK, sw=0.2)
        fp.text((a + c) / 2, (b + d) / 2 - 0.12, zid, size=2.8, weight=800)
    fp.rect(x0 + wt, 24.85, 50.5, 26.6, sw=0.35)                    # WC partition
    fp.rect(x0 + wt, 26.6, x1 - wt, 26.72, fill=D.PRIMARY, sw=0)   # teal back wall with menu screen
    fp.text(55.0, 26.0, "menu screen on teal back wall", size=1.9, fill=D.GREY)
    fp.text(WINDOW_X, y1 + 0.75, "PICKUP WINDOW W1", size=2.9, weight=700)
    fp.text(52.4, y0 - 0.9, "WALK-UP WINDOW", size=2.9, weight=700)
    fp.dim((x0, y1), (x1, y1), 1.6, "12.00")
    fp.dim((x1, y0), (x1, y1), -1.6, "7.50")
    fp.text(54.0, y1 + 3.5, "C-001b  PAVILION FLOOR PLAN 1:50", size=4.2, weight=800)
    leg = 21.2
    for zid, name, *_ in zones:
        fp.text(x0, leg - 0.9 - 0.75 * (int(zid) - 1) - 1.2, f"{zid}  {name}", size=2.9, anchor="start")


def main():
    sh = D.Sheet("C-001", "Compact variant: site & floor plan", 200, origin=(45, 395))
    s = site(sh)
    fp = D.Sheet("C-001", "", 50, origin=(40 + 0, 0))
    # place the 1:50 plan to the right: world x0 → paper 440 mm, y0 → paper 300 mm
    fp.ox = 470 - BLD["x0"] * fp.k
    fp.oy = 365 + BLD["y0"] * fp.k
    floor(fp)
    sh.defs += [d for d in fp.defs if d not in sh.defs]
    sh.el += fp.el
    notes = [
        "Lean first-unit format: 90 m² pavilion on a leased corner of a host fuel-station forecourt. Fuel canopy, shop and access are the host's and are shown dashed/grey.",
        f"Single drive-thru lane: 1 order point, 1 pickup window. Stacking ≈ {s['total_cars']:.1f} cars from the window to the forecourt entry at {CAR_M:.0f} m/car "
        f"({s['between']:.1f} between order point and window, {s['behind']:.1f} behind the order point). Overflow is held on the host forecourt, never on the highway.",
        "Below the 10–12-car design stack recommended for standalone pads (C6); acceptable only because the forecourt buffers overflow. Confirm with the host's traffic layout.",
        "Restrooms: shared with the host shop under the lease (staff WC inside the pavilion).",
        "Roof: small hyperbolic paraboloid, oak soffit, eaves 3.85–5.75 m; tower 7.5 m at the approach corner.",
        "Generic geometry for illustration; adapt to the host's title plan, utilities and the Roads Department's access conditions.",
    ]
    sh.title_block(notes)
    p = sh.save("C-001_compact_variant.svg")
    print(p, s)


if __name__ == "__main__":
    main()
