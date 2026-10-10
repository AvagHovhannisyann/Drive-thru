"""
Assembles the investor package (HTML artifact) from:
  report/fragments/*.html   chapter text (written from research/ and strategy/ evidence)
  model/ engine results      figures computed live from model/assumptions_final.json (or assumptions.json)
  design/renders, design/drawings/out, brand/out   images
Output: report/site/index.html + report/site/assets/*  (publish the folder as one artifact)

Figure placeholders in fragments (<!--FIG:id-->) are replaced by generated charts/images.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "report"))
sys.path.insert(0, str(ROOT / "model"))
import charts as C  # noqa: E402
import engine  # noqa: E402
import frame  # noqa: E402
from make_maps import corridor_svg  # noqa: E402
import figs_design  # noqa: E402

SITE = ROOT / "report/site"
ASSETS = SITE / "assets"
FRAG = ROOT / "report/fragments"
BRAND = json.loads((ROOT / "brand/out/brand.json").read_text())
NAME, NAME_HY = BRAND["name_latin"], BRAND["name_armenian"]
FX = 361.93

CHAPTERS = [
    ("summary", "Executive feasibility report"),
    ("market", "Market & competition"),
    ("location", "Location feasibility"),
    ("concept", "Concept & positioning"),
    ("brand", "Brand identity"),
    ("architecture", "Architecture & 3D"),
    ("investment", "Startup investment"),
    ("financials", "Five-year financial model"),
    ("operations", "Operations & launch"),
    ("risk", "Risks & expansion"),
    ("decision", "Investment recommendation"),
    ("evidence", "Evidence & data gaps"),
]


def amd(v, unit="M"):
    if unit == "M":
        return f"{v / 1e6:,.0f} M AMD"
    return f"{v:,.0f} AMD"


def usd(v):
    d = v / FX
    return f"${d / 1e6:,.2f}M" if abs(d) >= 1e6 else f"${d / 1e3:,.0f}k"


def copy_asset(src: Path, name: str | None = None) -> str:
    ASSETS.mkdir(parents=True, exist_ok=True)
    dst = ASSETS / (name or src.name)
    if src.suffix.lower() == ".png" and src.stat().st_size > 900_000:
        from PIL import Image
        im = Image.open(src).convert("RGB")
        dst = dst.with_suffix(".jpg")
        im.save(dst, quality=86, optimize=True, progressive=True)
    else:
        shutil.copy(src, dst)
    return f"assets/{dst.name}"


def img(src, caption, alt=None, cls="img"):
    p = Path(src)
    if not p.exists():
        return f'<figure class="{cls}"><div class="callout">Missing image: {p.name}</div></figure>'
    rel = copy_asset(p)
    return f'<figure class="{cls}"><img src="{rel}" alt="{C.esc(alt or caption)}" loading="lazy"><figcaption>{caption}</figcaption></figure>'


def load_results():
    for f in ("assumptions_final.json", "assumptions_calibrated.json", "assumptions.json"):
        p = ROOT / "model" / f
        if p.exists():
            a = json.loads(p.read_text())
            src = f
            break
    res = {s: engine.run(a, s) for s in ("conservative", "base", "optimistic")}
    return a, res, src


def figures(a, res):
    F = {}
    S = [("Conservative", "--s2", "conservative"), ("Base", "--s1", "base"), ("Optimistic", "--s3", "optimistic")]
    yrs = ["Y1", "Y2", "Y3", "Y4", "Y5"]
    F["fin-revenue"] = C.grouped_bars(yrs, [(n, v, [y["net"] for y in res[k]["years"]]) for n, v, k in S],
                                      "Revenue by year (AMD, receipts)", "Three scenarios; nominal AMD", fmt=lambda v: f"{v / 1e6:,.0f}M")
    F["fin-ebitda"] = C.grouped_bars(yrs, [(n, v, [y["ebitda"] for y in res[k]["years"]]) for n, v, k in S],
                                     "EBITDA by year (after turnover tax)", "Negative bars are operating losses", fmt=lambda v: f"{v / 1e6:,.1f}M")
    months = [f"M{r['m']}" for r in res["base"]["months"]]
    F["fin-cumcash"] = C.lines(months, [(n, v, [r["cum_cash"] for r in res[k]["months"]]) for n, v, k in S],
                               "Cumulative cash after the initial investment", "Payback is where a line crosses zero",
                               fmt=lambda v: f"{v / 1e6:,.0f}M", x_every=6, ref_line=(0, "Payback line"))
    base = res["base"]
    y1 = [r for r in base["months"] if r["year"] <= 2]
    F["fin-monthly"] = C.lines([f'{r["cal_month"]}' for r in y1], [("Transactions/day", "--s1", [r["tx_day"] for r in y1])],
                               "Base case: transactions per day, first 24 months", "Opening ramp and seasonality",
                               fmt=lambda v: f"{v:,.0f}", x_every=2, end_labels=False, area_first=True)
    caps = [0.004, 0.006, 0.008, 0.010, 0.012, 0.015, 0.020]
    ticks = [1600, 2000, 2400, 2800, 3200, 3600]
    grid = engine.required_traffic_grid(a, "base", a["concept"]["value"], caps, ticks)
    F["fin-breakeven-grid"] = C.heatmap([f"{c * 100:.1f}%" for c in caps], [f"{t:,}" for t in ticks], grid,
                                        "Passing vehicles per day needed to break even (EBITDA = 0)",
                                        "Base cost structure; rows = capture of accessible traffic, columns = average order value (AMD)",
                                        fmt=lambda v: f"{v / 1000:,.0f}k" if v >= 1000 else f"{v:,.0f}", row_title="Capture", col_title="Average order (AMD)",
                                        steps=[15000, 25000, 40000, 60000])
    torn = engine.tornado(a, "base", a["concept"]["value"])
    F["fin-tornado"] = C.tornado([(t["label"], t["low"], t["high"]) for t in torn], torn[0]["base"],
                                 "What moves Year-3 EBITDA most", "Base case; one driver flexed at a time",
                                 fmt=lambda v: f"{v / 1e6:,.0f}M")
    # capex stacked by class for the three concepts
    concepts = [("Lean", "lean"), ("Mid-range", "mid"), ("Flagship", "flagship")]
    classes = [("Building", "building"), ("Site works & access", "site_works"), ("Equipment", "equipment"), ("Technology", "technology"),
               ("Signage", "signage"), ("Soft costs", "soft")]
    cols = ["--s1", "--s2", "--s3", "--seq-3", "--seq-5", "--ink-3"]
    tot = {c: engine.capex_total(a, c) for _, c in concepts}
    F["capex-stack"] = C.stacked_bars([n for n, _ in concepts],
                                      [(cn, cols[i], [tot[c]["by_class"].get(ck, 0) for _, c in concepts]) for i, (cn, ck) in enumerate(classes)],
                                      "Startup capex by concept (AMD, incl. non-recoverable VAT)", "Excludes land purchase (ground lease) and pre-opening costs",
                                      fmt=lambda v: f"{v / 1e6:,.0f}M")
    si = a["seasonality_index"]["value"]
    F["seasonality"] = C.lines(engine.MONTHS, [("Seasonality index", "--s1", si)], "Monthly traffic seasonality used in the model",
                               "1.00 = annual average", fmt=lambda v: f"{v:.2f}", end_labels=False, ref_line=(1.0, "Average"))
    return F


def map_figs():
    F = {}
    ch_dt = {"lat": 40.2593, "lon": 44.5976, "label": "Coffee House drive-thru"}
    F["map-competitors"] = ('<figure style="margin:22px 0">' + corridor_svg(competitors=[ch_dt], title="M-4 Yerevan–Sevan corridor") +
                            '<figcaption style="color:var(--ink-3);font-size:13.5px;margin-top:8px">M-4 corridor from the Yerevan edge to Sevan. '
                            'Orange: fuel stations; blue: cafés, fast food and restaurants within 200 m of the road (OSM extract, B2); '
                            'red triangle: the existing Coffee House drive-thru at Ptghni (A2).</figcaption></figure>')
    sites_file = ROOT / "strategy/sites.json"
    if sites_file.exists():
        sites = json.loads(sites_file.read_text())
        F["map-sites"] = ('<figure style="margin:22px 0">' + corridor_svg(sites=sites, competitors=[ch_dt], bbox=[39.95, 44.2, 40.62, 45.05],
                                                                       roads_file="region.json", places_file="region.json", pois=False,
                                                                       title="Candidate sites around Yerevan") +
                          '<figcaption style="color:var(--ink-3);font-size:13.5px;margin-top:8px">Scored candidate sites (numbers match the scoring table). '
                          'Filled marker: recommended first site. Road network © OpenStreetMap contributors.</figcaption></figure>')
    return F


def fragment(cid):
    p = FRAG / f"{cid}.html"
    if p.exists():
        return p.read_text()
    title = dict(CHAPTERS)[cid]
    return f'<section class="ch" id="{cid}"><h2>{title}</h2><div class="callout">Chapter in preparation.</div></section>'


def build(extra_figs=None):
    if SITE.exists():
        shutil.rmtree(SITE)
    ASSETS.mkdir(parents=True)
    a, res, src = load_results()
    F = figures(a, res)
    F.update(figs_design.brand_figs(img))
    F.update(figs_design.arch_figs(img, copy_asset, json.loads((ROOT / "design/layout.json").read_text())))
    F.update(map_figs())
    F.update(extra_figs or {})
    body = []
    hero = ROOT / "design/renders/final/hero_dusk.png"
    if not hero.exists():
        hero = ROOT / "design/renders/hero_dusk.png"
    if not hero.exists():
        hero = next(iter(sorted((ROOT / "design/renders").glob("*.png"))), None)
    hero_src = copy_asset(hero, "hero.png") if hero else ""
    body.append(f'<header class="hero"><img src="{hero_src}" alt="{NAME} drive-thru prototype at blue hour">'
                f'<div class="over"><div class="eyebrow">Investment proposal · feasibility study · October 2026</div>'
                f'<h1>{NAME} <span class="hy" lang="hy">{NAME_HY}</span></h1>'
                f'<p>A drive-thru coffee and bakery chain for Armenia — market evidence, site selection, brand, architecture, '
                f'five-year financials and a go/no-go recommendation.</p></div></header>')
    for cid, _ in CHAPTERS:
        html = fragment(cid)
        for fid, fig in F.items():
            html = html.replace(f"<!--FIG:{fid}-->", fig)
        body.append(html)
    body.append(f'<footer class="foot">Prepared October 2026. Figures in AMD at {FX} AMD/USD (CBA, 9 Oct 2026). '
                f'Model inputs: <code>model/{src}</code>. Evidence files: <code>research/</code>. '
                'Map data © OpenStreetMap contributors. 3D assets: Poly Haven (CC0).</footer>')
    html = frame.page(f"{NAME} Drive-Thru Study", f"{NAME} — Armenian drive-thru coffee & bakery chain: feasibility, brand, architecture and financials",
                      CHAPTERS, "\n".join(body), f'{NAME} <span class="hy" lang="hy" style="font-weight:700">{NAME_HY}</span>')
    (SITE / "index.html").write_text(html)
    return SITE / "index.html"


if __name__ == "__main__":
    print(build())
