"""
Corridor map (theme-aware inline SVG) from OpenStreetMap data (research/data/*.json, research/B2-m4-pois.csv).
Classes are styled by the report CSS (.m-road-m4, .m-poi-fuel ...), so the map follows light/dark themes.

Usage: from make_maps import corridor_svg; svg = corridor_svg(sites=[...], competitors=[...])
OSM data © OpenStreetMap contributors (ODbL).
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "research/data"

BBOX = [40.13, 44.43, 40.66, 45.12]   # lat0, lon0, lat1, lon1
W, H = 1000, 760


def proj(lat, lon):
    lat0, lon0, lat1, lon1 = BBOX
    k = math.cos(math.radians((lat0 + lat1) / 2))
    sx = W / ((lon1 - lon0) * k)
    sy = H / (lat1 - lat0)
    s = min(sx, sy)
    x = (lon - lon0) * k * s
    y = H - (lat - lat0) * s
    return x, y


def path_from(coords):
    pts = [proj(c["lat"], c["lon"]) for c in coords]
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def rings(members):
    """Join outer member ways of a multipolygon into closed rings."""
    segs = [[(p["lat"], p["lon"]) for p in m["geometry"]] for m in members if m.get("role") == "outer" and "geometry" in m]
    out = []
    while segs:
        ring = segs.pop(0)
        changed = True
        while changed and ring[0] != ring[-1]:
            changed = False
            for i, sg in enumerate(segs):
                if sg[0] == ring[-1]:
                    ring += sg[1:]; segs.pop(i); changed = True; break
                if sg[-1] == ring[-1]:
                    ring += sg[::-1][1:]; segs.pop(i); changed = True; break
        out.append(ring)
    return out


def corridor_svg(sites=None, competitors=None, title="M-4 Yerevan–Sevan corridor", bbox=None, roads_file="roads.json", places_file="places.json", pois=True):
    global BBOX
    BBOX = bbox or [40.13, 44.43, 40.66, 45.12]
    roads = [e for e in json.loads((DATA / roads_file).read_text())["elements"] if e["type"] == "way"]
    places = json.loads((DATA / places_file).read_text())["elements"]
    el = []
    # lake
    sevan = json.loads((DATA / "sevan.json").read_text())["elements"] if (DATA / "sevan.json").exists() else []
    lake_members = [{"role": "outer", "geometry": w["geometry"]} for w in sevan if "geometry" in w]
    for e in [{"type": "relation", "members": lake_members}]:
        if e["type"] == "relation":
            for ring in rings(e.get("members", [])):
                pts = [proj(a, b) for a, b in ring]
                el.append('<path class="m-water" d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + ' Z"/>')
    # roads (minor first)
    order = {"Մ-4": 3, "Մ-1": 2, "Մ-2": 2, "Մ-5": 2, "Հ-3": 1}
    for rank in (1, 2, 3):
        for e in roads:
            ref = e["tags"].get("ref")
            if order.get(ref, 0) == rank and "geometry" in e:
                cls = "m-road-m4" if ref == "Մ-4" else ("m-road-m" if rank == 2 else "m-road-h")
                el.append(f'<path class="{cls}" d="{path_from(e["geometry"])}"/>')
    # POIs
    pois = list(csv.DictReader(open(ROOT / "research/B2-m4-pois.csv"))) if pois else []
    for p in pois:
        cat = p["category"]
        x, y = proj(float(p["lat"]), float(p["lon"]))
        if cat == "fuel":
            el.append(f'<circle class="m-poi-fuel" cx="{x:.1f}" cy="{y:.1f}" r="2.6"><title>{p["name"]} (fuel)</title></circle>')
        elif cat in ("cafe", "fast_food", "restaurant"):
            el.append(f'<rect class="m-poi-food" x="{x - 2.2:.1f}" y="{y - 2.2:.1f}" width="4.4" height="4.4"><title>{p["name"]} ({cat})</title></rect>')
        elif cat == "road:interchange_exit":
            el.append(f'<circle class="m-poi-jct" cx="{x:.1f}" cy="{y:.1f}" r="1.6"/>')
    # towns
    for e in places:
        if e["type"] != "node":
            continue
        t = e["tags"]
        name = t.get("name:en") or t.get("name")
        if not name:
            continue
        x, y = proj(e["lat"], e["lon"])
        if not (0 < x < W and 0 < y < H):
            continue
        pl = t.get("place")
        if pl == "city":
            el.append(f'<circle class="m-city" cx="{x:.1f}" cy="{y:.1f}" r="5"/><text class="m-label-city" x="{x + 8:.1f}" y="{y + 5:.1f}">{name}</text>')
        elif pl == "town":
            el.append(f'<circle class="m-town" cx="{x:.1f}" cy="{y:.1f}" r="3"/><text class="m-label" x="{x + 6:.1f}" y="{y + 4:.1f}">{name}</text>')
    # competitors (e.g. existing drive-thru)
    for c in competitors or []:
        x, y = proj(c["lat"], c["lon"])
        el.append(f'<g class="m-comp"><path d="M{x:.1f},{y - 9:.1f} l7,12 h-14 z"/><text class="m-label-comp" x="{x + 10:.1f}" y="{y + 3:.1f}">{c["label"]}</text></g>')
    # candidate sites
    for i, s in enumerate(sites or []):
        x, y = proj(s["lat"], s["lon"])
        cls = "m-site-top" if s.get("rank") == 1 else "m-site"
        dx = s.get("dx", 14)
        anchor = "start" if dx >= 0 else "end"
        el.append(f'<g class="{cls}"><circle cx="{x:.1f}" cy="{y:.1f}" r="11"/><text class="m-site-num" x="{x:.1f}" y="{y + 4.5:.1f}">{s["id"]}</text>'
                  f'<text class="m-label-site" x="{x + dx:.1f}" y="{y + 4:.1f}" text-anchor="{anchor}">{s["label"]}</text></g>')
    # scale bar (10 km)
    sl, so = BBOX[0] + 0.02, BBOX[1] + 0.03
    x0, y0 = proj(sl, so)
    x1, _ = proj(sl, so + 10 / (111.32 * math.cos(math.radians(sl))))
    el.append(f'<g class="m-scale"><line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y0:.1f}"/><text x="{(x0 + x1) / 2:.1f}" y="{y0 - 6:.1f}">10 km</text></g>')
    el.append(f'<text class="m-credit" x="{W - 8}" y="{H - 8}" text-anchor="end">Map data © OpenStreetMap contributors (ODbL)</text>')
    return (f'<svg class="corridor-map" viewBox="0 0 {W} {H}" role="img" aria-label="{title}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect class="m-bg" width="{W}" height="{H}"/>' + "".join(el) + "</svg>")


if __name__ == "__main__":
    r = corridor_svg(bbox=[39.95, 44.2, 40.36, 44.78], roads_file="region.json", places_file="region.json", pois=False, title="Yerevan region")
    (ROOT / "report/_map_region.svg").write_text(r)
    svg = corridor_svg(competitors=[{"lat": 40.2593, "lon": 44.5976, "label": "Coffee House drive-thru"}])
    (ROOT / "report/_map_test.svg").write_text(svg)
    print("ok", len(svg))
