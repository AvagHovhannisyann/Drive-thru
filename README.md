# Armenia drive-thru feasibility study & investor package

Evidence-based feasibility study, brand identity, architectural concept and five-year financial model for a
drive-thru coffee & bakery chain in Armenia (initial idea: an American-style drive-thru on the M4 Yerevan–Sevan highway).

| Folder | What it contains |
|---|---|
| `research/` | 16 research files + gap-fill files. Every quantitative claim carries a status tag (VERIFIED / REPORTED / ESTIMATE / ASSUMPTION), a source URL, and an adversarial fact-check log (section 7). `B2-m4-pois.csv` and `data/` hold OpenStreetMap extracts. |
| `strategy/` | Concept & positioning, weighted location study, operations/launch/regulatory roadmap, risk register & expansion plan. |
| `model/` | Financial model: `engine.py` (Python reference), `make_assumptions*.py` → `assumptions*.json` (every input with status and source), `build_workbook.py` → `DriveThru_Financial_Model.xlsx` (live Excel formulas), `verify.py` (recalculates the workbook in LibreOffice and asserts it matches the Python engine). |
| `brand/` | Naming report, `brand_config.json`, `make_brand.py` → `out/` (logo suite SVG, packaging artwork, signage & menu-board textures, uniforms, roadside sign, app screen). |
| `design/` | `site_layout.py` (single geometric source of truth → `layout.json`), `drawings/` (scaled SVG sheets A-001…A-301), `3d/` (Blender 4.5 Cycles scene builder, render & GLB export scripts), `renders/` (final images). |
| `report/` | Investor report generator (HTML) and its published artifact files. |

## Reproduce

```bash
python3 design/site_layout.py                 # geometry -> design/layout.json
python3 brand/make_brand.py                   # brand assets (needs Playwright + Chromium)
python3 design/drawings/make_drawings.py      # drawing sheets
python3 design/3d/fetch_assets.py             # CC0 Poly Haven HDRIs/textures/models (~1.3 GB, not committed)
blender -b -P design/3d/render_views.py -- --mode day --views hero,aerial --samples 128 --pct 100
python3 model/build_workbook.py && python3 model/verify.py
python3 report/build_report.py
```

Concept-stage work: all costs are published list prices or estimates, not quotations; traffic for the M4 has no
public count since 2008 and must be verified by the fieldwork protocol in `research/B1-m4-traffic.md` before any
land commitment.
