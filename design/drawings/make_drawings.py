"""
Scaled architectural drawing set (SVG) generated from design/layout.json.

Sheets (paper units = millimetres, so 1 mm on the sheet = scale/1000 m on site):
  A-001  Site plan                         1:250   (A1 landscape)
  A-002  Vehicle circulation & stacking    1:250   (A1 landscape)
  A-101  Ground floor plan                 1:50    (A1 landscape)
  A-201  Elevations (S, N, E, W)           1:100   (A1 landscape)
  A-301  Section A-A + roof geometry        1:100   (A1 landscape)

Run:  python3 design/drawings/make_drawings.py   -> design/drawings/out/*.svg
These are concept-design drawings (RIBA Stage 2 / schematic design), not for construction.
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
L = json.loads((ROOT / "design/layout.json").read_text())
BRAND = json.loads((ROOT / "brand/out/brand.json").read_text()) if (ROOT / "brand/out/brand.json").exists() else {}
OUT = Path(__file__).resolve().parent / "out"
OUT.mkdir(parents=True, exist_ok=True)

PROJECT = BRAND.get("name_latin", "Drive-thru Prototype")
PROJECT_HY = BRAND.get("name_armenian", "")
INK = "#1d1d1b"
GREY = "#8a8a86"
LIGHT = "#d9d6cf"
TUFF = BRAND.get("colors", {}).get("tuff", "#c98b6b")
ACCENT = BRAND.get("colors", {}).get("accent", "#d9772b")
PRIMARY = BRAND.get("colors", {}).get("primary", "#1f3b2d")
GLASS = "#9ec3cf"
GREEN = "#9bb57d"
ASPHALT = "#d8d8d4"
FONT = "Inter, 'Noto Sans Armenian', Arial, sans-serif"

A1 = (841, 594)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def roof_z(x, y):
    r = L["building"]["roof"]
    u = (x - r["x0"]) / (r["x1"] - r["x0"])
    v = (y - r["y0"]) / (r["y1"] - r["y0"])
    s = r["z_sw"] + u * (r["z_se"] - r["z_sw"])
    n = r["z_nw"] + u * (r["z_ne"] - r["z_nw"])
    return s + v * (n - s)


class Sheet:
    def __init__(self, number, title, scale, paper=A1, origin=(60, 520), plan=True):
        self.number, self.title, self.scale = number, title, scale
        self.W, self.H = paper
        self.ox, self.oy = origin
        self.k = 1000.0 / scale          # mm on paper per metre
        self.plan = plan
        self.el = []
        self.defs = []

    # world (m) -> paper (mm); for elevations x=horizontal metres, y=height metres
    def P(self, x, y):
        return (self.ox + x * self.k, self.oy - y * self.k)

    def pts(self, pts):
        return " ".join(f"{self.P(x, y)[0]:.2f},{self.P(x, y)[1]:.2f}" for x, y in pts)

    def add(self, s):
        self.el.append(s)

    def poly(self, pts, fill="none", stroke=INK, sw=0.25, dash=None, opacity=1.0, close=True, extra=""):
        tag = "polygon" if close else "polyline"
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<{tag} points="{self.pts(pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d} '
                 f'fill-opacity="{opacity}" stroke-linejoin="round" {extra}/>')

    def line(self, a, b, stroke=INK, sw=0.25, dash=None):
        (x1, y1), (x2, y2) = self.P(*a), self.P(*b)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def rect(self, x0, y0, x1, y1, **kw):
        self.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], **kw)

    def circle(self, x, y, r_m, fill="none", stroke=INK, sw=0.25, opacity=1.0, dash=None):
        cx, cy = self.P(x, y)
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r_m * self.k:.2f}" fill="{fill}" stroke="{stroke}" '
                 f'stroke-width="{sw}" fill-opacity="{opacity}"{d}/>')

    def text(self, x, y, s, size=2.5, anchor="middle", weight=400, fill=INK, rot=0, paper=False, family=FONT, ls=0):
        px, py = (x, y) if paper else self.P(x, y)
        r = f' transform="rotate({rot} {px:.2f} {py:.2f})"' if rot else ""
        self.add(f'<text x="{px:.2f}" y="{py:.2f}" font-family="{family}" font-size="{size}" text-anchor="{anchor}" '
                 f'font-weight="{weight}" fill="{fill}" letter-spacing="{ls}"{r}>{esc(s)}</text>')

    def ptext(self, x, y, s, **kw):
        self.text(x, y, s, paper=True, **kw)

    def prect(self, x, y, w, h, fill="none", stroke=INK, sw=0.25, rx=0):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def pline(self, x1, y1, x2, y2, stroke=INK, sw=0.25, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def dim(self, a, b, off, label=None, size=2.2, horizontal=None):
        """Dimension line between world points a,b offset perpendicular by off (m)."""
        (x1, y1), (x2, y2) = a, b
        dx, dy = x2 - x1, y2 - y1
        L_ = math.hypot(dx, dy)
        nx, ny = -dy / L_, dx / L_
        a2 = (x1 + nx * off, y1 + ny * off)
        b2 = (x2 + nx * off, y2 + ny * off)
        self.line(a, (a2[0] + nx * 0.3 * math.copysign(1, off), a2[1] + ny * 0.3 * math.copysign(1, off)), sw=0.13, stroke=GREY)
        self.line(b, (b2[0] + nx * 0.3 * math.copysign(1, off), b2[1] + ny * 0.3 * math.copysign(1, off)), sw=0.13, stroke=GREY)
        self.line(a2, b2, sw=0.18)
        for p in (a2, b2):
            px, py = self.P(*p)
            self.add(f'<line x1="{px - 1:.2f}" y1="{py + 1:.2f}" x2="{px + 1:.2f}" y2="{py - 1:.2f}" stroke="{INK}" stroke-width="0.35"/>')
        mx, my = (a2[0] + b2[0]) / 2, (a2[1] + b2[1]) / 2
        ang = -math.degrees(math.atan2(dy, dx))
        if ang > 90 or ang < -90:
            ang += 180
        px, py = self.P(mx, my)
        lab = label if label is not None else f"{L_:.2f}"
        self.add(f'<text x="{px:.2f}" y="{py - 0.8:.2f}" font-family="{FONT}" font-size="{size}" text-anchor="middle" '
                 f'fill="{INK}" transform="rotate({ang:.2f} {px:.2f} {py:.2f})">{esc(lab)}</text>')

    def arrow(self, pts, stroke=ACCENT, sw=0.6, head=1.6):
        self.poly(pts, stroke=stroke, sw=sw, close=False)
        (x1, y1), (x2, y2) = self.P(*pts[-2]), self.P(*pts[-1])
        ang = math.atan2(y2 - y1, x2 - x1)
        hx1 = x2 - head * math.cos(ang - 0.45); hy1 = y2 - head * math.sin(ang - 0.45)
        hx2 = x2 - head * math.cos(ang + 0.45); hy2 = y2 - head * math.sin(ang + 0.45)
        self.add(f'<polygon points="{x2:.2f},{y2:.2f} {hx1:.2f},{hy1:.2f} {hx2:.2f},{hy2:.2f}" fill="{stroke}"/>')

    def car(self, x, y, heading, label=None, fill="#ffffff", stroke=INK, l=4.7, w=1.85):
        h = math.radians(heading)
        c, s = math.cos(h), math.sin(h)
        def T(px, py):
            return (x + px * c - py * s, y + px * s + py * c)
        body = [T(-l / 2, -w / 2), T(l / 2 - 0.5, -w / 2), T(l / 2, -w / 2 + 0.35), T(l / 2, w / 2 - 0.35), T(l / 2 - 0.5, w / 2), T(-l / 2, w / 2)]
        self.poly(body, fill=fill, stroke=stroke, sw=0.2)
        ws = [T(0.55, -w / 2 + 0.15), T(1.15, -w / 2 + 0.25), T(1.15, w / 2 - 0.25), T(0.55, w / 2 - 0.15)]
        self.poly(ws, fill=LIGHT, stroke=stroke, sw=0.12)
        if label:
            self.text(x, y - 0.35, label, size=2.0, weight=700)

    def north_arrow(self, x, y, size=14, rot=0):
        self.add(f'<g transform="translate({x},{y}) rotate({rot})">'
                 f'<circle r="{size / 2}" fill="none" stroke="{INK}" stroke-width="0.3"/>'
                 f'<polygon points="0,{-size / 2 + 1} {size * 0.18},{size * 0.25} 0,{size * 0.12} {-size * 0.18},{size * 0.25}" fill="{INK}"/>'
                 f'<text y="{-size / 2 - 1.5}" font-family="{FONT}" font-size="3.2" text-anchor="middle" font-weight="700">N</text></g>')

    def scale_bar(self, x, y, metres=(0, 5, 10, 20, 30)):
        mx = metres[-1]
        self.prect(x, y, mx * self.k, 1.6, fill="#fff", sw=0.25)
        for i in range(len(metres) - 1):
            if i % 2 == 0:
                self.prect(x + metres[i] * self.k, y, (metres[i + 1] - metres[i]) * self.k, 1.6, fill=INK, sw=0)
        for m in metres:
            self.ptext(x + m * self.k, y + 5, f"{m}", size=2.2)
        self.ptext(x + mx * self.k + 4, y + 1.6, "m", size=2.2, anchor="start")
        self.ptext(x, y - 2, f"SCALE 1:{self.scale} @ A1", size=2.2, anchor="start", weight=700)

    def title_block(self, notes=None):
        W, H = self.W, self.H
        self.prect(10, 10, W - 20, H - 20, sw=0.5)
        x0 = W - 190
        self.prect(x0, H - 92, 180, 82, fill="#fff", sw=0.4)
        self.pline(x0, H - 66, x0 + 180, H - 66, sw=0.3)
        self.pline(x0, H - 40, x0 + 180, H - 40, sw=0.3)
        self.pline(x0 + 120, H - 40, x0 + 120, H - 10, sw=0.3)
        self.ptext(x0 + 5, H - 83, PROJECT.upper(), size=5.2, anchor="start", weight=800, ls=0.6)
        if PROJECT_HY:
            self.ptext(x0 + 5, H - 75.5, PROJECT_HY, size=3.4, anchor="start", weight=600, family="'Noto Sans Armenian', sans-serif")
        self.ptext(x0 + 5, H - 69, "Highway drive-thru prototype — concept design (RIBA Stage 2)", size=2.4, anchor="start", fill=GREY)
        self.ptext(x0 + 5, H - 56, self.title.upper(), size=4.2, anchor="start", weight=700)
        self.ptext(x0 + 5, H - 47, f"Scale 1:{self.scale} @ A1  ·  dimensions in metres unless noted", size=2.4, anchor="start", fill=GREY)
        self.ptext(x0 + 5, H - 31, "Status: CONCEPT — NOT FOR CONSTRUCTION", size=2.6, anchor="start", weight=700, fill=ACCENT)
        self.ptext(x0 + 5, H - 24, "Site geometry is a generic M4 roadside parcel; adapt to", size=2.2, anchor="start", fill=GREY)
        self.ptext(x0 + 5, H - 19, "topographic survey, title plan and Roads Dept. junction approval.", size=2.2, anchor="start", fill=GREY)
        self.ptext(x0 + 5, H - 13, "Date 2026-10  ·  Rev P1", size=2.2, anchor="start", fill=GREY)
        self.ptext(x0 + 150, H - 22, self.number, size=9, weight=800)
        if notes:
            y = 30
            self.ptext(x0, y - 6, "NOTES", size=3, anchor="start", weight=700)
            for n in notes:
                for chunk in wrap(n, 78):
                    self.ptext(x0, y, chunk, size=2.25, anchor="start")
                    y += 3.6
                y += 1.2

    def save(self, name):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W}mm" height="{self.H}mm" viewBox="0 0 {self.W} {self.H}">'
               f'<defs>{"".join(self.defs)}</defs><rect width="{self.W}" height="{self.H}" fill="#fbfaf7"/>' + "".join(self.el) + "</svg>")
        (OUT / name).write_text(svg)
        return OUT / name


def wrap(s, n):
    words, out, cur = s.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    return out


def hatch_defs(sh):
    sh.defs.append(f'<pattern id="hTuff" patternUnits="userSpaceOnUse" width="2" height="2" patternTransform="rotate(45)">'
                   f'<rect width="2" height="2" fill="{TUFF}"/><line x1="0" y1="0" x2="0" y2="2" stroke="#8a4f36" stroke-width="0.35"/></pattern>')
    sh.defs.append(f'<pattern id="hPlant" patternUnits="userSpaceOnUse" width="3" height="3">'
                   f'<rect width="3" height="3" fill="{GREEN}"/><circle cx="1" cy="1" r="0.35" fill="#6f8f55"/><circle cx="2.4" cy="2.2" r="0.3" fill="#6f8f55"/></pattern>')
    sh.defs.append('<pattern id="hPavers" patternUnits="userSpaceOnUse" width="3" height="1.5">'
                   '<rect width="3" height="1.5" fill="#bdbab3"/><path d="M0 0 H3 M0 0.75 H3 M0 0 V0.75 M1.5 0.75 V1.5" stroke="#9c988f" stroke-width="0.12"/></pattern>')
    sh.defs.append('<pattern id="hAsph" patternUnits="userSpaceOnUse" width="4" height="4">'
                   f'<rect width="4" height="4" fill="{ASPHALT}"/><circle cx="1" cy="1.3" r="0.12" fill="#b7b7b2"/><circle cx="3" cy="3.1" r="0.1" fill="#b7b7b2"/></pattern>')


# ======================================================================================
# A-001 SITE PLAN
# ======================================================================================
def site_plan(circulation_mode=False):
    num = "A-002" if circulation_mode else "A-001"
    title = "Vehicle circulation & stacking" if circulation_mode else "Site plan"
    sh = Sheet(num, title, 200, origin=(115, 318))
    hatch_defs(sh)
    hw = L["highway"]
    # highway context
    xa, xb = -12, 92
    sh.rect(xa, hw["y_far"], xb, hw["y_edge"], fill="#e9e8e4", stroke="none")
    for carr in (hw["north"], hw["south"]):
        for ln in ("lane1", "lane2"):
            y0, y1 = carr[ln]
            sh.rect(xa, y0, xb, y1, fill="#cfcfcb", stroke="none")
    med = hw["median"]
    sh.rect(xa, med[0], xb, med[1], fill=GREEN, stroke="none")
    sh.line((xa, (med[0] + med[1]) / 2), (xb, (med[0] + med[1]) / 2), sw=0.6, stroke=GREY)
    for carr in (hw["north"], hw["south"]):
        sh.line((xa, carr["lane1"][0]), (xb, carr["lane1"][0]), sw=0.18, dash="3,6", stroke="#fff")
        sh.line((xa, carr["lane2"][0] if carr is hw["north"] else carr["lane2"][1]), (xb, carr["lane2"][0] if carr is hw["north"] else carr["lane2"][1]), sw=0.25, stroke="#fff")
    aux = L["aux"]
    ya, yb = aux["y_inner"], aux["y_outer"]
    sh.poly([(64, ya), (xb, ya), (xb, yb), (64, yb)], fill="#c4c4bf", stroke=INK, sw=0.15)
    sh.poly([(11, ya), (11, yb), (xa, yb), (xa, ya)], fill="#c4c4bf", stroke=INK, sw=0.15)
    sh.text(80, (ya + yb) / 2 - 0.5, "DECELERATION LANE → (40 m taper + 46 m parallel, indicative)", size=2.0)
    sh.text(0, (ya + yb) / 2 - 0.5, "← ACCELERATION LANE (71 m + 50 m taper)", size=2.0)
    nl = hw.get("near_label", "WESTBOUND  ←  towards Yerevan")
    fl = hw.get("far_label", "EASTBOUND  →  towards Sevan")
    sh.text(50, sum(hw["north"]["lane1"]) / 2 - 0.6, nl, size=3.0, weight=700, fill="#555")
    sh.text(50, sum(hw["south"]["lane1"]) / 2 - 0.6, fl, size=3.0, weight=700, fill="#555")
    sh.text(50, (med[0] + med[1]) / 2 - 0.5, "CENTRAL RESERVE WITH SAFETY BARRIER — NO MEDIAN CROSSING AT SITE", size=2.0, fill="#3d5a2a")
    sh.text(xa + 2, hw["y_far"] - 3, "M4 INTERSTATE HIGHWAY (Yerevan – Sevan) — generic 2×2 divided cross-section, 90 km/h", size=2.6, anchor="start", weight=700)
    # site base
    S = L["site"]
    sh.rect(0, 0, S["w"], S["d"], fill="url(#hAsph)", stroke="none")
    # driveways
    sh.poly([(63.0, yb), (71.5, yb), (72.5, 0), (62.5, 0)], fill=ASPHALT, stroke=INK, sw=0.15)
    sh.poly([(2.5, yb), (11.5, yb), (11.0, 0), (3.0, 0)], fill=ASPHALT, stroke=INK, sw=0.15)
    for el in L["landscape"]:
        k = el["kind"]
        fill = {"planting": "url(#hPlant)", "island": "#e6e3dc", "plaza": "url(#hPavers)", "pad": "none"}[k]
        if k == "pad":
            continue
        sh.poly(el["poly"], fill=fill, stroke=INK, sw=0.3)
    # parking stalls
    for s in L["parking"]["stalls"]:
        x, y, w, l = s["x"], s["y"], s["w"], s["l"]
        sh.rect(x - w / 2, y - l / 2, x + w / 2, y + l / 2, stroke=INK, sw=0.15,
                fill={"acc": "#cfe0f3", "ev": "#d6ecd2"}.get(s["type"], "none"))
        lab = {"acc": "♿", "ev": "EV"}.get(s["type"], s["id"][1:])
        sh.text(x, y - 0.4, lab, size=1.7 if s["type"] == "std" else 2.4, fill=GREY if s["type"] == "std" else INK)
    lb = L["parking"]["long_bay"]
    sh.poly(lb["poly"], stroke=INK, sw=0.2, dash="1.5,1", fill="#f1ede4")
    sh.text(25, 10.2, "LONG-VEHICLE BAY 18 × 3.2 m (minibus / camper / coach drop-off)", size=1.9)
    # building
    b = L["building"]
    r = b["roof"]
    sh.rect(r["x0"], r["y0"], r["x1"], r["y1"], stroke=INK, sw=0.3, dash="2.5,1.2", fill="#efe7dc", )
    sh.rect(b["x0"], b["y0"], b["x1"], b["y1"], fill="url(#hTuff)", stroke=INK, sw=0.6)
    sh.rect(35.0, 24.0, 43.0, 28.0, fill=GLASS, stroke=INK, sw=0.3, opacity=0.9)
    t = b["tower"]
    sh.rect(t["x"] - t["w"] / 2, t["y"] - t["d"] / 2, t["x"] + t["w"] / 2, t["y"] + t["d"] / 2, fill=PRIMARY, stroke=INK, sw=0.4)
    p = b["pergola"]
    sh.rect(p["x0"], p["y0"], p["x1"], p["y1"], stroke=INK, sw=0.25, dash="1,0.8")
    oc = b["order_canopy"]
    sh.rect(oc["x0"], oc["y0"], oc["x1"], oc["y1"], stroke=INK, sw=0.3, dash="2.5,1.2")
    py_ = b["pylon"]
    sh.rect(py_["x"] - py_["w"] / 2, py_["y"] - py_["d"] / 2, py_["x"] + py_["w"] / 2, py_["y"] + py_["d"] / 2, fill=PRIMARY, stroke=INK, sw=0.3)
    sh.text(py_["x"] - 4.2, py_["y"] - 0.5, "PYLON 8.0 m", size=1.9, anchor="end", weight=700)
    # trees
    for tr in L["trees"]:
        rr = 2.4 * tr["s"] if tr["kind"] != "tree_small" else 1.7 * tr["s"]
        sh.circle(tr["x"], tr["y"], rr, fill="#7f9f63", opacity=0.55, stroke="#4f6b3a", sw=0.2)
        sh.circle(tr["x"], tr["y"], 0.15, fill="#4f6b3a", stroke="none")
    for lp in L["lights"]:
        sh.circle(lp["x"], lp["y"], 0.35, fill="#fff", stroke=INK, sw=0.25)
        sh.circle(lp["x"], lp["y"], 0.12, fill=INK, stroke="none")
    # order points / windows
    for op in L["circulation"]["order_points"]:
        sh.rect(op["x"] - 0.15, op["y"] - 1.1, op["x"] + 0.15, op["y"] + 1.1, fill=ACCENT, stroke=INK, sw=0.2)
        sh.text(op["x"] - 1.4, op["y"] + 2.2, op["id"], size=2.0, weight=700)
    for w in L["circulation"]["windows"]:
        sh.rect(w["x"] - 1.0, b["y1"] - 0.2, w["x"] + 1.0, b["y1"] + 0.25, fill=ACCENT, stroke=INK, sw=0.2)
        sh.text(w["x"], b["y1"] + 2.6 if circulation_mode else b["y1"] - 1.3, w["id"], size=2.2, weight=700)
    # drive path arrows
    c = L["circulation"]
    sh.arrow([(67.0, -1.0), (67.0, 6.0), (63.5, 9.0), (lane_x := 59.75, 11.5)], sw=0.5)
    sh.arrow([(64.25, 11.0), (64.25, 18.0)], sw=0.5)
    sh.arrow([(59.75, 13.0), (59.75, 18.0)], sw=0.5)
    sh.arrow([(50, 35.35), (44, 35.35)], sw=0.5)
    sh.arrow([(20, 35.35), (15.5, 33.5), (12.25, 29)], sw=0.5)
    sh.arrow([(12.25, 12), (12.25, 6), (7.0, 1.0), (7.0, -2.0)], sw=0.5)
    sh.arrow([(60, 12.0), (50, 12.0)], sw=0.4, stroke="#5b7fa6")
    sh.arrow([(30, 12.0), (16, 12.0), (12.5, 10)], sw=0.4, stroke="#5b7fa6")
    # pedestrian routes
    sh.poly([(30, 15.0), (30, 20.0), (41, 22.5), (41.2, 24.0)], stroke="#7a5c99", sw=0.35, dash="0.8,0.8", close=False)
    if circulation_mode:
        q = [(31.4, 35.35, 180), (39.6, 35.35, 180), (46.0, 35.35, 180), (52.2, 35.0, 168)]
        q += [(57.0, 33.6, 135), (60.2, 31.0, 105)]
        q += [(59.75, 24.0, 90), (59.75, 18.0, 90), (59.75, 12.0, 90), (64.25, 24.0, 90), (64.25, 18.0, 90), (64.25, 12.0, 90), (66.4, 5.0, 90)]
        for i, (x, y, h) in enumerate(q):
            sh.car(x, y, h, label=str(i + 1), fill="#fff4e6" if i < 2 else "#ffffff")
        cap = c["capacity"]
        sh.text(37, 40.3, f"QUEUE: {len(q)} CARS FROM PICKUP WINDOW TO SITE ENTRY (6.0 m per car) — no overspill onto the M4", size=2.8, weight=800, fill=ACCENT)
        # swept-path note
        sh.text(54.5, 31.0, "R 8.0", size=2.0, fill=GREY)
        sh.text(16.0, 31.0, "R 6.0", size=2.0, fill=GREY)
    # labels
    sh.text(33.5, 30.6, "BAR / PRODUCTION", size=2.3, weight=700)
    sh.text(39.0, 25.6, "CAFÉ", size=2.3, weight=700)
    sh.text(19.7, 24.8, "TERRACE", size=2.3, weight=700)
    sh.text(19.7, 23.4, "(pergola, 24 seats)", size=1.8)
    sh.text(37.0, 38.6 if not circulation_mode else 37.9, "PICKUP LANE (single, 3.5 m)", size=2.0, weight=700)
    sh.text(62.0, 9.2, "DUAL ORDER LANES", size=2.0, weight=700, rot=0)
    sh.text(37, 6.6, "VISITOR PARKING", size=2.2, weight=700, fill="#555")
    sh.text(45.6, 18.8, "TOWER 11.0 m", size=1.9, weight=700)
    sh.text(25.5, 26.3, "WC", size=2.0)
    # dimensions
    sh.dim((0, 0), (S["w"], 0), -9.5 + hw["y_edge"] - 25, label=f"{S['w']:.2f}", size=2.4)
    sh.dim((S["w"], 0), (S["w"], S["d"]), -4.0, label=f"{S['d']:.2f}", size=2.4)
    sh.dim((b["x0"], b["y0"]), (b["x1"], b["y0"]), -1.6, label=f"{b['x1'] - b['x0']:.2f}")
    sh.dim((b["x0"], b["y0"]), (b["x0"], b["y1"]), 4.6, label=f"{b['y1'] - b['y0']:.2f}")
    sh.dim((40.0, 0.0), (40.0, b["y0"]), 0.0, label=f"setback {b['y0']:.1f}")
    sh.dim((40.0, hw["y_edge"]), (40.0, 0.0), 0.0, label="verge 6.0")
    # property line
    sh.rect(0, 0, S["w"], S["d"], stroke="#b0412e", sw=0.5, dash="6,1.5,1,1.5")
    sh.text(1.2, S["d"] + 1.2, "PROPERTY BOUNDARY (indicative)", size=2.0, anchor="start", fill="#b0412e", weight=700)
    # utilities (indicative)
    if not circulation_mode:
        for (x, y, lab) in ((8.0, 40.5, "SEPTIC / PACKAGE WWTP"), (21.0, 31.6, "GREASE TRAP"), (70.0, 40.5, "TRANSFORMER 160 kVA"), (5.0, 30.5, "WATER TANK / BOREHOLE")):
            sh.rect(x - 1.2, y - 0.8, x + 1.2, y + 0.8, fill="#fff", stroke="#3b6ea5", sw=0.25)
            sh.text(x, y - 2.0, lab, size=1.7, fill="#3b6ea5", weight=700)
    # north arrow, scale
    sh.north_arrow(80, 60)
    sh.scale_bar(60, 560)
    # site data table
    sm = L["summary"]
    rows = [("Site area", f"{sm['site_area_m2']:,.0f} m² ({sm['site_area_ha']:.2f} ha)"),
            ("Building (GIA approx.)", f"{sm['building_gross_m2']:.0f} m²"),
            ("Roof canopy (plan)", f"{sm['roof_plane_m2']:.0f} m²"),
            ("Site coverage", f"{sm['site_coverage_pct']}%"),
            ("Parking", f"{sm['parking_total']} stalls ({sm['parking'].get('acc', 0)} accessible, {sm['parking'].get('ev', 0)} EV) + 1 long bay"),
            ("Drive-thru stacking", f"{sm['stacking']['total_from_pickup_window']:.0f} cars (pickup → entry)"),
            ("Behind order points", f"{sm['stacking']['behind_order_points']:.0f} cars (2 lanes)"),
            ("Terrace", f"{sm['terrace_m2']:.0f} m² under pergola")]
    x0, y0 = 651, 120
    sh.ptext(x0, y0 - 6, "SITE DATA", size=3.2, anchor="start", weight=800)
    for i, (k, v) in enumerate(rows):
        sh.ptext(x0, y0 + i * 6.2, k, size=2.5, anchor="start", fill=GREY)
        sh.ptext(x0 + 52, y0 + i * 6.2, v, size=2.5, anchor="start", weight=600)
    # legend
    lx, ly = 651, 190
    sh.ptext(lx, ly - 6, "LEGEND", size=3.2, anchor="start", weight=800)
    items = [("url(#hTuff)", "Building — tuff-clad enclosure"), (GLASS, "Glazed café (full-height curtain wall)"),
             ("#efe7dc", "Roof canopy outline (oak soffit, hypar)"), ("url(#hPavers)", "Basalt-paver plaza / terrace"),
             ("url(#hPlant)", "Planting — native steppe grasses, apricot trees"), ("#cfe0f3", "Accessible parking"),
             ("#d6ecd2", "EV charging (2 × 60 kW DC, phase 2)"), (ACCENT, "Order point / service window")]
    for i, (f, lab) in enumerate(items):
        sh.prect(lx, ly + i * 6.4 - 3, 7, 4, fill=f, sw=0.25)
        sh.ptext(lx + 10, ly + i * 6.4, lab, size=2.4, anchor="start")
    notes = [
        "1. Right-in / right-out access from the near carriageway only; the central barrier prevents left turns. "
        "Opposite-direction customers reach the site via the nearest grade-separated junction / U-turn (see location study).",
        "2. Auxiliary lane lengths are indicative for 90 km/h and must be confirmed against Armenian road design norms and "
        "the Roads Department connection permit.",
        "3. Building set back ≥ 20 m from the carriageway edge; confirm the statutory roadside protection strip for interstate roads.",
        "4. Utilities indicative: highway parcels typically lack sewer — allow for package treatment plant or sealed tank, borehole or "
        "community water, 0.4 kV connection ≈ 100–150 kW.",
    ] if not circulation_mode else [
        "1. Counter-clockwise circulation keeps the building on the driver's left (left-hand-drive fleet).",
        "2. Dual order lanes with tablet order-takers ('runners') at peak; digital menu boards + speakers OP-A/OP-B as back-up. Lanes merge "
        "before W1 (payment / order confirm) and W2 (hand-off).",
        "3. 13-car stack from pickup to entry; a further 4 cars can queue on the decel lane only in exceptional peaks — "
        "operating rule: open walk-in counter / extra runners when queue passes car 9.",
        "4. Separate bypass aisle lets parking customers avoid the drive-thru queue. Long-vehicle bay keeps coaches out of the lanes.",
        "5. Target service time ≤ 3:30 min order-to-hand-off; peak throughput 90–110 cars/hour with runners.",
    ]
    sh.title_block(notes)
    return sh.save(f"{num}_{'circulation' if circulation_mode else 'site_plan'}.svg")


# ======================================================================================
# A-101 FLOOR PLAN 1:50
# ======================================================================================
def floor_plan():
    b = L["building"]
    sh = Sheet("A-101", "Ground floor plan", 50, origin=(130 - b["x0"] * 20, 430 + b["y0"] * 20 - 20))
    hatch_defs(sh)
    x0, x1, y0, y1 = b["x0"], b["x1"], b["y0"], b["y1"]
    t = 0.35
    # roof outline
    r = b["roof"]
    sh.rect(r["x0"], r["y0"], r["x1"], r["y1"], stroke=GREY, sw=0.3, dash="3,1.5")
    sh.text(r["x0"] + 0.3, r["y1"] - 0.5, "ROOF EDGE ABOVE (hypar, oak soffit)", size=2.2, anchor="start", fill=GREY)
    # window lane & plaza context
    sh.rect(x0 - 4.5, y1 + 0.6, x1 + 4, y1 + 4.1, fill="#e7e6e1", stroke="none")
    sh.line((x0 - 4.5, y1 + 0.6), (x1 + 4, y1 + 0.6), sw=0.3)
    sh.text(x1 + 1.5, y1 + 2.5, "PICKUP LANE  ← direction of travel", size=2.6, anchor="end", weight=700, fill="#555")
    sh.car(36.5, y1 + 2.35, 180, fill="#ffffff")
    sh.rect(x0 - 4, y0 - 4, x1 + 5, y0, fill="url(#hPavers)", stroke="none", opacity=0.5)
    # walls (exterior)
    def wall_rect(ax0, ay0, ax1, ay1):
        sh.rect(ax0, ay0, ax1, ay1, fill="url(#hTuff)", stroke=INK, sw=0.5)
    # exterior walls with openings (simplified as segments)
    ops = b["openings"]
    for fac in ("N", "S", "E", "W"):
        segs = sorted([(o["a"], o["b"], o) for o in ops if o["facade"] == fac])
        a0, a1 = (x0, x1) if fac in ("N", "S") else (y0, y1)
        cur = a0
        # remove doors inside curtain walls
        cws = [s for s in segs if s[2]["kind"] == "curtain_wall"]
        rest = [s for s in segs if s[2]["kind"] != "curtain_wall" and not any(c[0] <= s[0] and s[1] <= c[1] for c in cws)]
        for (a, bnd, o) in sorted(cws + rest):
            if a > cur:
                if fac == "N": wall_rect(cur, y1 - t, a, y1)
                if fac == "S": wall_rect(cur, y0, a, y0 + t)
                if fac == "E": wall_rect(x1 - t, cur, x1, a)
                if fac == "W": wall_rect(x0, cur, x0 + t, a)
            # glazing / doors
            if o["kind"] in ("curtain_wall", "glazing", "service_window"):
                if fac in ("N", "S"):
                    yy = y1 - t / 2 if fac == "N" else y0 + t / 2
                    sh.line((a, yy - 0.04), (bnd, yy - 0.04), sw=0.25)
                    sh.line((a, yy + 0.04), (bnd, yy + 0.04), sw=0.25)
                    if o["kind"] != "curtain_wall":
                        sh.rect(a, y1 - t if fac == "N" else y0, bnd, (y1 - t) + 0.05 if fac == "N" else y0 + 0.05, fill=INK, stroke="none")
                else:
                    xx = x1 - t / 2 if fac == "E" else x0 + t / 2
                    sh.line((xx - 0.04, a), (xx - 0.04, bnd), sw=0.25)
                    sh.line((xx + 0.04, a), (xx + 0.04, bnd), sw=0.25)
            if o["kind"] == "service_window":
                sh.rect(a, y1, bnd, y1 + 0.42, fill="#fff", stroke=INK, sw=0.3)
                sh.text((a + bnd) / 2, y1 + 1.2, f"{o['id']} SERVICE WINDOW (sliding, 2.0 m)", size=2.0, weight=700)
            cur = bnd
        if cur < a1:
            if fac == "N": wall_rect(cur, y1 - t, a1, y1)
            if fac == "S": wall_rect(cur, y0, a1, y0 + t)
            if fac == "E": wall_rect(x1 - t, cur, x1, a1)
            if fac == "W": wall_rect(x0, cur, x0 + t, a1)
    # door swings
    def door(hx, hy, w, ang0, ang1, leaf=True):
        cx, cy = sh.P(hx, hy)
        rr = w * sh.k
        a0r, a1r = math.radians(ang0), math.radians(ang1)
        ex, ey = cx + rr * math.cos(a1r), cy - rr * math.sin(a1r)
        sx, sy = cx + rr * math.cos(a0r), cy - rr * math.sin(a0r)
        sh.add(f'<path d="M{sx:.2f},{sy:.2f} A{rr:.2f},{rr:.2f} 0 0,0 {ex:.2f},{ey:.2f}" fill="none" stroke="{INK}" stroke-width="0.18" stroke-dasharray="1,0.6"/>')
        sh.add(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{ex:.2f}" y2="{ey:.2f}" stroke="{INK}" stroke-width="0.4"/>')
    door(40.2, y0, 1.0, 0, 90); door(42.2, y0, 1.0, 180, 90)       # D1 double entrance
    door(x0, 25.0, 1.0, 90, 0)                                       # staff door
    # interior partitions
    part = [((x0 + t, 28.0), (35.0, 28.0)), ((29.5, y0 + t), (29.5, 28.0)), ((35.0, y0 + t), (35.0, 26.6)),
            ((29.0, 28.0), (29.0, y1 - t)), ((27.0, y0 + t), (27.0, 28.0)), ((32.25, y0 + t), (32.25, 26.4)),
            ((29.5, 26.4), (35.0, 26.4))]
    for a, bb in part:
        if a[0] == bb[0]:
            sh.rect(a[0] - 0.05, a[1], a[0] + 0.05, bb[1], fill="#bdb8ae", stroke=INK, sw=0.3)
        else:
            sh.rect(a[0], a[1] - 0.05, bb[0], a[1] + 0.05, fill="#bdb8ae", stroke=INK, sw=0.3)
    door(29.5 + 0.1, 26.4, 0.9, 0, -90); door(32.35, 26.4, 0.9, 0, -90)
    door(35.0, 27.0, 0.9, 90, 180)                                   # restroom lobby from café
    door(27.0, 26.0, 0.8, 90, 0); door(29.0, 30.0, 0.9, 0, 90)
    # fixtures in restrooms
    for (wx, wy) in ((30.3, 25.2), (33.1, 25.2)):
        sh.add(f'<ellipse cx="{sh.P(wx, wy)[0]:.2f}" cy="{sh.P(wx, wy)[1]:.2f}" rx="{0.22 * sh.k:.2f}" ry="{0.33 * sh.k:.2f}" fill="#fff" stroke="{INK}" stroke-width="0.25"/>')
        sh.rect(wx + 0.9, y0 + 0.4, wx + 1.5, y0 + 0.85, fill="#fff", sw=0.25)
        sh.circle(wx + 0.45, 24.9, 0.75, stroke=GREY, sw=0.15, dash="0.8,0.6")
    # equipment
    for e in b["equipment"]:
        bx = e["box"]
        sh.rect(bx[0], bx[1], bx[2], bx[3], fill="#f3efe7", stroke=INK, sw=0.25)
        sh.text((bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2 - 0.12, e["tag"], size=1.9, weight=700)
    # counters
    sh.rect(29.1, y1 - 1.05, x1 - 0.4, y1 - 0.4, stroke=INK, sw=0.25, dash="1,0.6")
    sh.rect(38.6, 28.05, x1 - 0.4, 29.05, fill="none", stroke=INK, sw=0.35)
    sh.rect(35.4, y0 + 0.4, x1 - 0.6, y0 + 0.85, fill="#e8dcc6", stroke=INK, sw=0.25)
    for i in range(6):
        sh.circle(35.9 + i * 1.1, y0 + 1.22, 0.2, fill="#fff", stroke=INK, sw=0.2)
    for (tx, ty) in ((37.0, 26.6), (40.2, 26.6)):
        sh.rect(tx - 0.45, ty - 0.45, tx + 0.45, ty + 0.45, fill="#e8dcc6", stroke=INK, sw=0.25)
        for (dx, dy) in ((-0.75, 0), (0.75, 0)):
            sh.circle(tx + dx, ty + dy, 0.22, fill="#fff", stroke=INK, sw=0.2)
    # room tags
    for rm in b["rooms"]:
        cx, cy = (rm["x0"] + rm["x1"]) / 2, (rm["y0"] + rm["y1"]) / 2
        if rm["id"] == "R1":
            cx, cy = 35.0, 30.6
        if rm["id"] == "R3":
            cx, cy = 39.0, 27.35
        if rm["id"] == "R4":
            cx, cy = 32.25, 27.2
        name = rm["name"].split(" (")[0]
        sh.text(cx, cy + 0.15, rm["id"] + "  " + name.upper()[:34], size=2.0, weight=700)
        sh.text(cx, cy - 0.45, f"{rm['area_m2']:.1f} m²", size=1.9, fill=GREY)
    # grids
    gx = [x0, 29.0, 35.0, x1]
    gy = [y0, 28.0, y1]
    for i, g in enumerate(gx):
        sh.line((g, y0 - 3.2), (g, y1 + 4.6), sw=0.13, dash="4,1,1,1", stroke=GREY)
        sh.circle(g, y0 - 3.8, 0.55, fill="#fff", stroke=INK, sw=0.25)
        sh.text(g, y0 - 4.0, str(i + 1), size=2.4, weight=700)
    for i, g in enumerate(gy):
        sh.line((x0 - 3.2, g), (x1 + 3.2, g), sw=0.13, dash="4,1,1,1", stroke=GREY)
        sh.circle(x0 - 3.8, g, 0.55, fill="#fff", stroke=INK, sw=0.25)
        sh.text(x0 - 3.8, g - 0.2, "ABC"[i], size=2.4, weight=700)
    # dimensions
    for i in range(len(gx) - 1):
        sh.dim((gx[i], y0), (gx[i + 1], y0), -2.0)
    sh.dim((x0, y0), (x1, y0), -2.8, label=f"{x1 - x0:.2f}")
    sh.dim((x1, y0), (x1, 28.0), -2.0)
    sh.dim((x1, 28.0), (x1, y1), -2.0)
    sh.dim((x1, y0), (x1, y1), -2.9, label=f"{y1 - y0:.2f}")
    # section mark
    sh.line((38.0, y0 - 2.5), (38.0, y1 + 4.4), sw=0.5, dash="6,1.5,1.5,1.5", stroke=ACCENT)
    sh.text(38.0, y0 - 3.1, "A", size=3.2, weight=800, fill=ACCENT)
    sh.text(38.0, y1 + 4.9, "A", size=3.2, weight=800, fill=ACCENT)
    # flows
    sh.arrow([(43.5, 22.6), (41.2, 23.4), (41.2, 24.6)], stroke="#7a5c99", sw=0.4)
    sh.text(44.4, 22.0, "GUEST ENTRY", size=2.0, anchor="start", fill="#7a5c99", weight=700)
    sh.arrow([(x0 - 2.0, 25.5), (x0 + 0.2, 25.5)], stroke="#3b6ea5", sw=0.4)
    sh.text(x0 - 2.2, 24.6, "STAFF / DELIVERY", size=2.0, anchor="end", fill="#3b6ea5", weight=700)
    # equipment schedule
    tx, ty = 651, 150
    sh.ptext(tx, ty, "EQUIPMENT SCHEDULE", size=3.2, anchor="start", weight=800)
    for i, e in enumerate(b["equipment"]):
        sh.ptext(tx, ty + 7 + i * 4.6, e["tag"], size=2.3, anchor="start", weight=700)
        sh.ptext(tx + 10, ty + 7 + i * 4.6, e["name"][:58], size=2.2, anchor="start")
    ry = ty + 7 + len(b["equipment"]) * 4.6 + 8
    sh.ptext(tx, ry, "ROOM SCHEDULE", size=3.2, anchor="start", weight=800)
    tot = 0
    for i, rm in enumerate(b["rooms"]):
        sh.ptext(tx, ry + 7 + i * 4.6, rm["id"], size=2.3, anchor="start", weight=700)
        sh.ptext(tx + 10, ry + 7 + i * 4.6, rm["name"][:50], size=2.2, anchor="start")
        sh.ptext(tx + 178, ry + 7 + i * 4.6, f"{rm['area_m2']:.1f}", size=2.2, anchor="end")
        tot += rm["area_m2"]
    sh.ptext(tx, ry + 7 + len(b["rooms"]) * 4.6 + 2, f"Gross external area {b['gross_m2']:.0f} m²  ·  net rooms ≈ {tot:.0f} m² (incl. walls)", size=2.3, anchor="start", weight=700)
    sh.north_arrow(80, 60)
    sh.scale_bar(60, 560, metres=(0, 1, 2, 5))
    notes = ["Linear 'production line' along the drive-thru façade: cold bar → espresso → POS (W1) → food finish → hand-off (W2); "
             "every station faces the window lane so staff never cross paths.",
             "Restrooms (2 accessible unisex + baby change) reached from the café lobby; essential differentiator on the Sevan road.",
             "Separate staff/delivery entrance on the west façade next to stores and the walk-in cooler.",
             "Finishes: polished concrete floor, tuff feature walls, oak soffit exposed in café, washable white panels in BOH (HACCP)."]
    sh.title_block(notes)
    return sh.save("A-101_floor_plan.svg")


# ======================================================================================
# A-201 ELEVATIONS 1:100
# ======================================================================================
def elevations():
    b = L["building"]
    r = b["roof"]
    sh = Sheet("A-201", "Elevations", 100, origin=(0, 0), plan=False)
    hatch_defs(sh)
    f0 = b["ffl"]
    WT = f0 + r["wall_top"]

    def elev(ox, oy, facade, title):
        # horizontal coordinate s in metres along facade as seen from outside (left->right)
        sh.ox, sh.oy = ox, oy
        if facade == "S":
            s0, s1 = r["x0"], r["x1"]; X = lambda s: s - s0; rz = lambda s: roof_z(s, r["y0"]); bz = lambda s: roof_z(s, b["y0"])
            span = (b["x0"], b["x1"]); tower_s = b["tower"]["x"]
        elif facade == "N":
            s0, s1 = r["x0"], r["x1"]; X = lambda s: s1 - s; rz = lambda s: roof_z(s, r["y1"]); bz = lambda s: roof_z(s, b["y1"])
            span = (b["x0"], b["x1"]); tower_s = b["tower"]["x"]
        elif facade == "E":
            s0, s1 = r["y0"], r["y1"]; X = lambda s: s - s0; rz = lambda s: roof_z(r["x1"], s); bz = lambda s: roof_z(b["x1"], s)
            span = (b["y0"], b["y1"]); tower_s = b["tower"]["y"]
        else:
            s0, s1 = r["y0"], r["y1"]; X = lambda s: s1 - s; rz = lambda s: roof_z(r["x0"], s); bz = lambda s: roof_z(b["x0"], s)
            span = (b["y0"], b["y1"]); tower_s = b["tower"]["y"]
        W_ = s1 - s0
        # ground
        sh.line((-3, 0), (W_ + 6, 0), sw=0.6)
        # tuff wall
        a, c = span
        sh.poly([(X(a), f0), (X(c), f0), (X(c), WT), (X(a), WT)], fill="url(#hTuff)", stroke=INK, sw=0.35)
        # joints
        z = f0 + 0.3
        while z < WT - 0.01:
            sh.line((X(a), z), (X(c), z), sw=0.08, stroke="#8a4f36")
            z += 0.3
        # clerestory glass
        sh.poly([(X(a), WT), (X(c), WT), (X(c), bz(c)), (X(a), bz(a))], fill=GLASS, stroke=INK, sw=0.25, opacity=0.85)
        n = max(1, round(abs(c - a) / 1.5))
        for i in range(1, n):
            s = a + (c - a) * i / n
            sh.line((X(s), WT), (X(s), bz(s)), sw=0.12)
        # openings
        for o in b["openings"]:
            if o["facade"] != facade:
                continue
            oa, ob_ = o["a"], o["b"]
            if o["kind"] == "curtain_wall":
                sh.poly([(X(oa), f0), (X(ob_), f0), (X(ob_), bz(ob_)), (X(oa), bz(oa))], fill=GLASS, stroke=INK, sw=0.3)
                m = max(1, round((ob_ - oa) / 1.6))
                for i in range(1, m):
                    s = oa + (ob_ - oa) * i / m
                    sh.line((X(s), f0), (X(s), bz(s)), sw=0.15)
                sh.line((X(oa), WT), (X(ob_), WT), sw=0.15)
            elif o["kind"] in ("glazing", "service_window"):
                sh.rect(X(oa), f0 + o["sill"], X(ob_), f0 + o["head"], fill=GLASS, stroke=INK, sw=0.3)
                if o["kind"] == "service_window":
                    sh.rect(X(oa) - 0.15, f0 + 0.9, X(ob_) + 0.15, f0 + 2.62, fill="none", stroke=INK, sw=0.45)
                    sh.text((X(oa) + X(ob_)) / 2, f0 + 2.85, o["id"], size=2.2, weight=700)
            elif o["kind"] in ("door", "door_solid"):
                sh.rect(X(oa), f0, X(ob_), f0 + o["head"], fill="#4a3b2c" if o["kind"] == "door_solid" else GLASS, stroke=INK, sw=0.3)
        # roof
        sh.poly([(X(s0), rz(s0)), (X(s1), rz(s1)), (X(s1), rz(s1) + r["thickness"]), (X(s0), rz(s0) + r["thickness"])],
                fill="#3a2c20", stroke=INK, sw=0.35)
        # tower (if visible on this elevation)
        tw = b["tower"]
        tA, tB = tower_s - tw["w"] / 2, tower_s + tw["w"] / 2
        if facade in ("S", "E", "W", "N"):
            beyond = facade == "N"
            sh.poly([(X(tA), 0), (X(tB), 0), (X(tB), tw["h"]), (X(tA), tw["h"])], fill="#e6d2c4" if beyond else "url(#hTuff)", stroke=GREY if beyond else INK, sw=0.4, dash="1.5,1" if beyond else None)
            sh.rect(X(tA) + 0.22, tw["h"] - 1.9, X(tB) - 0.22, tw["h"] - 0.42, fill=PRIMARY, stroke=INK, sw=0.25)
            sh.text((X(tA) + X(tB)) / 2, tw["h"] - 1.3, "LOGO", size=1.8, fill="#fff", weight=700)
        # levels
        for z, lab in ((0.0, "±0.00 site"), (f0, f"+{f0:.2f} FFL"), (WT, f"+{WT:.2f} wall top"),
                       (max(rz(s0), rz(s1)), f"+{max(rz(s0), rz(s1)):.2f} roof soffit (high)"),
                       (min(rz(s0), rz(s1)), f"+{min(rz(s0), rz(s1)):.2f} roof soffit (low)"), (tw["h"], f"+{tw['h']:.2f} tower")):
            sh.line((W_ + 0.6, z), (W_ + 2.2, z), sw=0.2)
            sh.text(W_ + 2.5, z - 0.1, lab, size=2.1, anchor="start")
        # scale figures
        for px in (X(a) - 2.0, X(c) + 1.2):
            sh.poly([(px, 0), (px + 0.25, 0), (px + 0.3, 0.9), (px + 0.35, 0), (px + 0.6, 0), (px + 0.5, 1.0), (px + 0.55, 1.45),
                     (px + 0.42, 1.5), (px + 0.42, 1.62), (px + 0.3, 1.78), (px + 0.18, 1.62), (px + 0.18, 1.5), (px + 0.05, 1.45), (px + 0.1, 1.0)],
                    fill=GREY, stroke="none")
        sh.text(W_ / 2, -2.6, title, size=3.4, weight=800)
        sh.dim((0, -0.6), (W_, -0.6), 0.0, label=f"{W_:.2f}")

    elev(60, 220, "S", "SOUTH ELEVATION — HIGHWAY FRONTAGE")
    elev(390, 220, "N", "NORTH ELEVATION — DRIVE-THRU WINDOWS")
    elev(60, 420, "E", "EAST ELEVATION — APPROACH (WESTBOUND TRAFFIC)")
    elev(330, 420, "W", "WEST ELEVATION — TERRACE")
    sh.ox, sh.oy = 0, 0
    sh.scale_bar(60, 560, metres=(0, 1, 2, 5, 10))
    mat = b["materials"]
    notes = [f"Cladding: {mat['cladding']}.", f"Frames: {mat['frames']}. Glazing: {mat['glazing']}.",
             f"Roof: {r['form']}; soffit {mat['soffit']}; fascia {mat['fascia']}.",
             "Clerestory band between tuff walls and roof soffit makes the roof read as a floating plane; LED reveal at the fascia for night identity.",
             "Signage subject to Armenian Law on Language (Armenian text primary) and outdoor-advertising permits."]
    sh.title_block(notes)
    return sh.save("A-201_elevations.svg")


# ======================================================================================
# A-301 SECTION 1:100
# ======================================================================================
def section():
    b = L["building"]
    r = b["roof"]
    sh = Sheet("A-301", "Section A-A & roof geometry", 50, origin=(50, 250), plan=False)
    hatch_defs(sh)
    f0 = b["ffl"]
    WT = f0 + r["wall_top"]
    xs = 38.0
    # section along y (south on left -> north on right)
    yL, yR = 14.0, 44.0
    X = lambda y: y - yL
    # ground profile
    sh.poly([(X(14.5), -0.4), (X(41), -0.4), (X(41), 0), (X(14.5), 0)], fill="#d9d4ca", stroke=INK, sw=0.4)
    # plaza raised
    sh.rect(X(20.0), 0, X(24.0), 0.15, fill="#bdbab3", stroke=INK, sw=0.3)
    # building cut walls
    sh.rect(X(b["y0"]), 0, X(b["y0"] + 0.35), f0, fill="#999", stroke=INK, sw=0.3)
    sh.rect(X(b["y0"]), 0, X(b["y1"]), f0, fill="#aaa", stroke=INK, sw=0.4)
    sh.rect(X(b["y1"] - 0.35), f0, X(b["y1"]), WT, fill="url(#hTuff)", stroke=INK, sw=0.6)
    # south curtain wall at x=38 (café) full height
    sh.rect(X(b["y0"]) , f0, X(b["y0"] + 0.06), roof_z(xs, b["y0"]), fill=GLASS, stroke=INK, sw=0.4)
    # service window in north wall
    sh.rect(X(b["y1"] - 0.35), f0 + 0.95, X(b["y1"]), f0 + 2.45, fill=GLASS, stroke=INK, sw=0.3)
    # clerestory north
    sh.rect(X(b["y1"] - 0.2), WT, X(b["y1"] - 0.14), roof_z(xs, b["y1"]), fill=GLASS, stroke=INK, sw=0.3)
    # partition at y=28 (café counter back wall)
    sh.rect(X(27.95), f0, X(28.05), WT, fill="#bdb8ae", stroke=INK, sw=0.3)
    # roof section
    pts = [(X(r["y0"]), roof_z(xs, r["y0"])), (X(r["y1"]), roof_z(xs, r["y1"])),
           (X(r["y1"]), roof_z(xs, r["y1"]) + r["thickness"]), (X(r["y0"]), roof_z(xs, r["y0"]) + r["thickness"])]
    sh.poly(pts, fill="#5a4330", stroke=INK, sw=0.6)
    # counters and equipment
    sh.rect(X(28.05), f0, X(29.05), f0 + 1.0, fill="#e8dcc6", stroke=INK, sw=0.3)
    sh.rect(X(31.9), f0, X(32.9), f0 + 1.05, fill="#ddd", stroke=INK, sw=0.3)
    sh.rect(X(24.4), f0, X(24.85), f0 + 1.05, fill="#e8dcc6", stroke=INK, sw=0.3)
    # car in window lane
    cx = X(35.35)
    sh.poly([(cx - 0.95, 0.18), (cx + 0.95, 0.18), (cx + 0.95, 0.95), (cx + 0.75, 1.45), (cx - 0.75, 1.45), (cx - 0.95, 0.95)], fill="#fff", stroke=INK, sw=0.3)
    # people
    for (py, h) in ((26.0, 1.75), (30.8, 1.7), (22.0, 1.65)):
        px = X(py)
        sh.poly([(px - 0.2, 0.15), (px + 0.2, 0.15), (px + 0.18, h * 0.85), (px - 0.18, h * 0.85)], fill=GREY, stroke="none")
        sh.circle(px, h * 0.93, 0.12, fill=GREY, stroke="none")
    # labels
    sh.text(X(26), 2.6, "CAFÉ", size=2.6, weight=700)
    sh.text(X(30.5), 2.6, "BAR LINE", size=2.6, weight=700)
    sh.text(X(35.35), 2.1, "PICKUP LANE", size=2.4, weight=700)
    sh.text(X(21.6), 2.4, "PLAZA", size=2.4, weight=700)
    sh.text(X(17.0), 0.6, "PARKING", size=2.4, weight=700)
    zc = roof_z(xs, r["y1"])
    sh.dim((X(r["y1"]) + 0.3, 0), (X(r["y1"]) + 0.3, zc), -1.6, label=f"clear {zc:.2f}")
    sh.dim((X(b["y0"]) - 0.3, 0), (X(b["y0"]) - 0.3, roof_z(xs, b["y0"])), 1.8, label=f"{roof_z(xs, b['y0']):.2f}")
    sh.dim((X(r["y0"]), -1.2), (X(b["y0"]), -1.2), 0.0, label=f"{b['y0'] - r['y0']:.2f} overhang")
    sh.dim((X(b["y1"]), -1.2), (X(r["y1"]), -1.2), 0.0, label=f"{r['y1'] - b['y1']:.2f} overhang")
    sh.text(X(27), -1.8, "SECTION A-A (through café, bar line and pickup lane, looking west)", size=3.4, weight=800)
    # roof geometry diagram (axonometric-ish corner heights)
    sh.ox, sh.oy = 330, 520
    k_save = sh.k
    sh.k = 4.0
    corners = {"NW": (r["x0"], r["y1"], r["z_nw"]), "NE": (r["x1"], r["y1"], r["z_ne"]), "SW": (r["x0"], r["y0"], r["z_sw"]), "SE": (r["x1"], r["y0"], r["z_se"])}
    def iso(x, y, z):
        u = (x - r["x0"]) * 0.866 - (y - r["y0"]) * 0.866
        v = (x - r["x0"]) * 0.5 + (y - r["y0"]) * 0.5 + z * 1.6
        return (u, v)
    for (x0_, y0_) in ((r["x0"], r["y0"]),):
        pass
    grid = []
    for i in range(11):
        for (a1, a2) in ((("SW", "NW"), ("SE", "NE")), (("SW", "SE"), ("NW", "NE"))):
            pa = [corners[a1[0]][j] + (corners[a1[1]][j] - corners[a1[0]][j]) * i / 10 for j in range(3)]
            pb = [corners[a2[0]][j] + (corners[a2[1]][j] - corners[a2[0]][j]) * i / 10 for j in range(3)]
            sh.line(iso(*pa), iso(*pb), sw=0.15, stroke="#7a5a3a")
    for nm, (x, y, z) in corners.items():
        u, v = iso(x, y, z)
        sh.line((u, v), iso(x, y, 0), sw=0.15, stroke=GREY, dash="1,1")
        sh.text(u, v + 0.6, f"{nm} +{z:.2f}", size=2.3, weight=700)
    sh.text(iso(r["x0"], r["y0"], 0)[0] + 8, iso(r["x0"], r["y0"], 0)[1] - 3.5, "ROOF: HYPERBOLIC PARABOLOID — straight ruled members, double curvature", size=2.6, weight=800)
    sh.k = k_save
    sh.ptext(330, 380, "ROOF GEOMETRY (not to scale)", size=3.2, weight=800)
    sh.ox, sh.oy = 0, 0
    sh.scale_bar(60, 560, metres=(0, 1, 2, 5))
    notes = ["Hypar roof is generated from straight members (ruled surface): glulam rafters on steel edge beams, timber cassette deck, "
             "insulated membrane roof, oak batten soffit. Low point NW (drainage to rainwater tank for irrigation).",
             f"Drive-thru clear height at pickup ≥ {roof_z(36, r['y1']):.2f} m (vans/minibuses); height bar at lane entry 3.2 m.",
             "Café volume opens to the soffit: up to ~6.5 m clear at the SE corner — the glazed 'lantern' visible from the highway.",
             "Tower (11.0 m) carries the SE roof corner and the illuminated brand mark — the long-range identifier for westbound traffic."]
    sh.title_block(notes)
    return sh.save("A-301_section.svg")


if __name__ == "__main__":
    for f in (site_plan(False), site_plan(True), floor_plan(), elevations(), section()):
        print(f)
