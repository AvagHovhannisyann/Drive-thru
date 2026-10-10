"""
Brand and architecture figures for the report (inline SVG logos, swatches, galleries, drawings, 3D viewer).
Each function returns HTML strings keyed by the <!--FIG:id--> placeholder they replace.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND_OUT = ROOT / "brand/out"
RENDERS = ROOT / "design/renders/final"
DRAW = ROOT / "design/drawings/out"
CFG = json.loads((ROOT / "brand/brand_config.json").read_text())


def _inline_svg(name: str) -> str:
    s = (BRAND_OUT / name).read_text()
    # make it responsive: keep viewBox, drop fixed size
    import re
    s = re.sub(r'\swidth="\d+"\sheight="\d+"', ' style="height:100%;width:auto;max-width:100%" role="img"', s, count=1)
    return s


def brand_figs(img) -> dict:
    """img(path, caption, alt=None, cls='img') comes from build_report (copies the asset)."""
    F = {}
    c = CFG["colors"]
    tiles = [("logo_bilingual.svg", "Primary bilingual lock-up (Armenian first)", c["light"]),
             ("logo_horizontal.svg", "Latin lock-up for maps, app stores and export markets", "#ffffff"),
             ("logo_horizontal_reverse.svg", "Reverse lock-up on basalt teal", c["primary"]),
             ("logo_stacked.svg", "Stacked lock-up for the tower and cups", c["light"])]
    cells = "".join(f'<figure style="margin:0"><div style="background:{bg};border:1px solid var(--line);border-radius:12px;padding:22px 26px;'
                    f'display:flex;align-items:center;justify-content:center;height:170px;box-sizing:border-box">{_inline_svg(f)}</div>'
                    f'<figcaption style="color:var(--ink-3);font-size:13px;margin-top:6px">{cap}</figcaption></figure>'
                    for f, cap, bg in tiles if (BRAND_OUT / f).exists())
    F["brand-logos"] = f'<div class="gallery">{cells}</div>'
    names = {"primary": ("Basalt teal", "Primary. Fascia, tower, cups, uniforms"), "accent": ("Apricot", "Accent. Symbol, calls to action, lane guidance"),
             "light": ("Lavash cream", "Backgrounds, packaging"), "tuff": ("Tuff rose", "Architecture: Armenian tuff cladding"),
             "ink": ("Road ink", "Body text"), "sky": ("Sevan sky", "Secondary: iced drinks, digital"), "bronze": ("Roast bronze", "Secondary: coffee retail, wood")}
    sw = "".join(f'<div class="sw"><div class="c" style="background:{c[k]}"></div><div class="t"><b>{n}</b>{c[k]} · {u}</div></div>'
                 for k, (n, u) in names.items())
    F["brand-swatches"] = f'<div class="swatches">{sw}</div>'
    F["brand-type"] = ('<div class="typespec">'
                       f'<div style="font-family:var(--font-display);font-weight:800;font-size:clamp(26px,4vw,40px);color:var(--brand)">CHAMPA · Unbounded 800</div>'
                       '<div lang="hy" style="font-family:\'Noto Sans Armenian\',sans-serif;font-weight:800;font-size:clamp(24px,3.6vw,36px);margin-top:6px">ՃԱՄՓԱ · Ճամփադ բաց։ · Noto Sans Armenian</div>'
                       '<p style="font-family:var(--font-body);font-size:16px;margin:10px 0 0">Manrope for body text, menus and the app. One family per script, three weights, '
                       'Armenian set at the same cap height as Latin so bilingual signs read as one line. All three are open-licence (SIL OFL) Google Fonts, so there are no font licence fees.</p></div>')
    apps = [("roadside_sign.png", "Roadside approach sign, 2 km out: bilingual, with services (WC) listed"),
            ("billboard.png", "Launch billboard: Armenian line leads, English secondary"),
            ("tex_menu_board.png", "Drive-thru menu board: Armenian names first, final prices in AMD"),
            ("app_screen.png", "Order-ahead and loyalty app: \"road kilometres\" stamp card"),
            ("uniforms.png", "Crew uniforms: apron, tee, cap and hi-vis runner vest"),
            ("tex_pylon_face.png", "Pylon face: brand, services and opening hours")]
    F["brand-applications"] = '<div class="gallery">' + "".join(img(BRAND_OUT / f, cap) for f, cap in apps) + "</div>"
    pk = RENDERS / "packaging.png"
    if not pk.exists():
        pk = ROOT / "design/renders/packaging.png"
    F["brand-packaging"] = img(pk, "Packaging family (Cycles render): hot cups with sleeve, iced cup, pastry box, kraft carry bag and retail \"Road Blend\" beans")
    flat = [("cup_wrap.png", "Hot-cup wrap"), ("sleeve.png", "Cup sleeve"), ("bag_front.png", "Carry bag"), ("box_top.png", "Pastry box lid")]
    F["brand-flats"] = '<div class="gallery">' + "".join(img(BRAND_OUT / f, cap) for f, cap in flat) + "</div>"
    return F


def arch_figs(img, copy_asset, layout: dict) -> dict:
    F = {}
    R = lambda n: RENDERS / n  # noqa: E731
    F["arch-hero"] = img(R("hero_dusk.png"), "Blue hour from the entry drive: tuff-clad pavilion, hyperbolic-paraboloid roof and 11 m beacon tower")
    F["arch-gallery-day"] = '<div class="gallery">' + "".join(img(R(f), c) for f, c in [
        ("hero_day.png", "Day view from the entry: order canopy (right) and pavilion"),
        ("aerial_day.png", "Bird's-eye view: dual order lanes merge into one pickup lane wrapping the building"),
        ("ararat_day.png", "Context: the pad on an Ararat-plain arterial, with Mount Ararat on the horizon"),
        ("plaza_day.png", "Walk-up plaza and café entrance; EV and accessible bays on the left"),
        ("terrace_day.png", "Shaded terrace (62 m²) facing south-west"),
        ("aerial_nw_day.png", "From the north-west: rooftop PV (≈99 panels) and service yard"),
    ]) + "</div>"
    F["arch-gallery-dusk"] = '<div class="gallery">' + "".join(img(R(f), c) for f, c in [
        ("drivethru_dusk.png", "Pickup lane at dusk: two service windows under the roof overhang"),
        ("interior_dusk.png", "Interior: walk-up counter, menu screens and 12 seats"),
        ("approach_dusk.png", "Approach at 50 mm: tower and pylon read from ≈200 m"),
        ("hero_night.png", "Night: lit fascia, tower beacon and canopy"),
        ("aerial_night.png", "Night aerial: lighting plan for lanes and parking"),
        ("plaza_dusk.png", "Plaza at dusk"),
    ]) + "</div>"
    F["arch-compact"] = '<div class="gallery">' + "".join(img(R(f), c) for f, c in [
        ("c_hero_day.png", "CHAMPA Compact (recommended first-unit format): 90 m² pavilion on a host fuel-station forecourt"),
        ("c_aerial_day.png", "Compact variant from above: single lane wraps the pavilion; fuel canopy and shop belong to the host"),
        ("c_walkup_day.png", "Walk-up window and terrace under the roof overhang"),
        ("c_window_day.png", "Pickup window on the north façade"),
        ("c_hero_dusk.png", "Compact variant at dusk"),
        ("c_aerial_dusk.png", "Compact variant at dusk, from above"),
    ]) + "</div>"
    cp = DRAW / "C-001_compact_variant.svg"
    if cp.exists():
        rel = copy_asset(cp)
        F["arch-compact-plan"] = (f'<figure class="img"><a href="{rel}" target="_blank" rel="noopener"><img src="{rel}" alt="C-001 compact variant site and floor plan" loading="lazy" style="background:#fff"></a>'
                                  '<figcaption>C-001 Compact variant: site plan 1:200 and pavilion floor plan 1:50. Click to open full size.</figcaption></figure>')
    cut = R("cutaway_day_annotated.png")
    if not cut.exists():
        cut = R("cutaway_day.png")
    F["arch-cutaway"] = img(cut, "Plan cut at 1.4 m: production line, drive-thru windows, café, restrooms and back of house")
    draws = [("A-001_site_plan", "A-001 Site plan 1:200 (3,256 m² plot)"), ("A-002_circulation", "A-002 Vehicle and pedestrian circulation, stacking"),
             ("A-101_floor_plan", "A-101 Floor plan 1:50 (171 m² GFA)"), ("A-201_elevations", "A-201 Elevations 1:100"),
             ("A-301_section", "A-301 Section 1:50 and roof geometry")]
    cells = []
    for f, cap in draws:
        p = DRAW / f"{f}.svg"
        if p.exists():
            rel = copy_asset(p)
            cells.append(f'<figure class="img"><a href="{rel}" target="_blank" rel="noopener"><img src="{rel}" alt="{cap}" loading="lazy" style="background:#fff"></a>'
                         f'<figcaption>{cap}. Click to open full size.</figcaption></figure>')
    F["arch-drawings"] = '<div class="gallery">' + "".join(cells) + "</div>"
    F["arch-viewer"] = (f'<figure style="margin:22px 0"><div class="viewer" id="viewer3d" data-src="assets/drive_thru.glb">'
                        '<div class="views"><button data-view="aerial">Aerial</button><button data-view="hero">Entry</button>'
                        '<button data-view="drive">Lane</button><button data-view="plan">Plan</button></div>'
                        '<div class="hint">Loading 3D model…</div></div>'
                        '<figcaption style="color:var(--ink-3);font-size:13.5px;margin-top:8px">Interactive model exported from the same parametric source as the drawings and renders (glTF, ≈3 MB). '
                        'Simplified materials; furniture and vegetation omitted.</figcaption></figure>')
    # dimensions table from layout
    site = layout.get("site", {})
    sw_, sd_ = int(site.get("w", 74)), int(site.get("d", 44))
    rows = [("Plot", f"{sw_} × {sd_} m = {sw_ * sd_:,} m²"),
            ("Building footprint", "19.0 × 9.0 m = 171 m² (GFA), floor level +0.15 m"),
            ("Roof", "Hyperbolic paraboloid, 25.4 × 16.2 m, corners at 4.15 / 4.55 / 4.95 / 7.30 m; 0.42 m edge"),
            ("Beacon tower", "1.9 × 1.9 m, 11.0 m high, tuff with illuminated symbol"),
            ("Order canopy", "9.7 × 5.6 m, 3.7–4.25 m clear"),
            ("Drive-thru", "2 order points → 1 pickup lane, 2 windows; stacking ≈ 12–13 cars from window to entry"),
            ("Parking", "25 stalls (21 standard, 2 EV, 2 accessible) + 1 long-vehicle bay"),
            ("Café", "12 seats inside, terrace 62 m², 2 accessible WCs"),
            ("Pylon", "2.2 × 0.7 m, 8.0 m high, at the site entry")]
    F["arch-dims"] = ('<div class="tscroll"><table><thead><tr><th>Element</th><th>Dimension</th></tr></thead><tbody>'
                      + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + "</tbody></table></div>")
    return F
