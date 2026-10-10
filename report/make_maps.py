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

BBOX = (40.13, 44.43, 40.62, 45.02)   # lat0, lon0, lat1, lon1
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


def corridor_svg(sites=None, competitors=None, title="M-4 Yerevan–Sevan corridor"):
    roads = json.loads((DATA / "roads.json").read_text())["elements"]
    places = json.loads((DATA / "places.json").read_text())["elements"]
    el = []
    # lake
    for e in places:
        if e["type"] == "relation":
            for m in e.get("members", []):
                if m.get("role") == "outer" and "geometry" in m:
                    el.append(f'<path class="m-water" d="{path_from(m["geometry"])}"/>')
    # roads (minor first)
    order = {"Մ-4": 3, "Մ-1": 2, "Մ-2": 2, "Մ-5": 2, "Հ-3": 1}
    for rank in (1, 2, 3):
        for e in roads:
            ref = e["tags"].get("ref")
            if order.get(ref, 0) == rank and "geometry" in e:
                cls = "m-road-m4" if ref == "Մ-4" else ("m-road-m" if rank == 2 else "m-road-h")
                el.append(f'<path class="{cls}" d="{path_from(e["geometry"])}"/>')
    # POIs
    pois = list(csv.DictReader(open(ROOT / "research/B2-m4-pois.csv")))
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
    x0, y0 = proj(40.15, 44.46)
    x1, _ = proj(40.15, 44.46 + 10 / (111.32 * math.cos(math.radians(40.15))))
    el.append(f'<g class="m-scale"><line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y0:.1f}"/><text x="{(x0 + x1) / 2:.1f}" y="{y0 - 6:.1f}">10 km</text></g>')
    el.append(f'<text class="m-credit" x="{W - 8}" y="{H - 8}" text-anchor="end">Map data © OpenStreetMap contributors (ODbL)</text>')
    return (f'<svg class="corridor-map" viewBox="0 0 {W} {H}" role="img" aria-label="{title}" xmlns="http://www.w3.org/2000/svg">'
            f'<rect class="m-bg" width="{W}" height="{H}"/>' + "".join(el) + "</svg>")


if __name__ == "__main__":
    svg = corridor_svg(competitors=[{"lat": 40.2593, "lon": 44.5976, "label": "Coffee House drive-thru"}])
    (ROOT / "report/_map_test.svg").write_text(svg)
    print("ok", len(svg))
