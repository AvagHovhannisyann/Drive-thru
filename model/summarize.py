"""
Writes model/results_summary.json: the single source of truth for every financial number quoted in the report.
Reads the first existing of assumptions_final.json, assumptions_calibrated.json, assumptions.json.
Run: python3 model/summarize.py
"""
from __future__ import annotations

import json
from pathlib import Path

import engine

ROOT = Path(__file__).resolve().parent
SCEN = ("conservative", "base", "optimistic")


def load():
    for f in ("assumptions_final.json", "assumptions_calibrated.json", "assumptions.json"):
        p = ROOT / f
        if p.exists():
            return json.loads(p.read_text()), f
    raise FileNotFoundError("no assumptions file")


def r0(v, nd=0):
    return None if v is None else round(v, nd)


def main():
    a, src = load()
    fx = a["fx_amd_per_usd"]["value"]
    concept = a["concept"]["value"]
    out = {"assumptions_file": src, "fx_amd_per_usd": fx, "concept_modelled": concept, "tax_regime": a["tax_regime"]["value"],
           "note": "AMD nominal. Revenue = gross receipts incl. VAT-equivalent (catering turnover-tax regime: no VAT on sales). EBITDA is after turnover tax."}
    out["capex_by_concept"] = {}
    for c in ("lean", "mid", "flagship"):
        t = engine.capex_total(a, c)
        po = a["pre_opening_costs_amd"]["value"][c]
        out["capex_by_concept"][c] = {"capex_amd": r0(t["total"]), "pre_opening_amd": po, "investment_amd": r0(t["total"] + po),
                                      "investment_usd": r0((t["total"] + po) / fx), "by_class_amd": {k: r0(v) for k, v in t["by_class"].items()},
                                      "items": a["capex"][c]}
    out["scenarios"] = {}
    for s in SCEN:
        r = engine.run(a, s)
        out["scenarios"][s] = {
            "investment_amd": r0(r["investment"]), "investment_usd": r0(r["investment"] / fx),
            "years": [{k: (r0(y[k], 3) if k in ("ebitda_margin",) else r0(y[k], 1 if k in ("tx_per_day",) else 0))
                       for k in ("net", "turnover_tax", "cogs", "labour", "rent", "opex", "ebitda", "ebitda_margin", "dep", "ebit", "tax", "net_income",
                                 "ocf", "fcf", "transactions", "tx_per_day", "avg_ticket")} for y in r["years"]],
            "payback_month": r["payback_month"], "irr_5y_with_residual": r0(r["irr_5y_with_residual"], 4) if r["irr_5y_with_residual"] is not None else None,
            "irr_5y_no_residual": r0(r["irr_5y_no_residual"], 4) if r["irr_5y_no_residual"] is not None else None,
            "npv_amd": r0(r["npv"]), "residual_amd": r0(r["residual"]), "roic_y3": r0(r["roic_y3"], 4),
            "cum_cash_m60_amd": r0(r["months"][-1]["cum_cash"]),
            "breakeven": {k: (r0(v, 2) if isinstance(v, float) else v) for k, v in r["breakeven"].items()},
            "peak_month_tx_day": r0(max(m["tx_day"] for m in r["months"]), 1),
            "low_month_tx_day_y2": r0(min(m["tx_day"] for m in r["months"] if m["year"] == 2), 1),
        }
    caps = [0.004, 0.006, 0.008, 0.010, 0.012, 0.015, 0.020]
    ticks = [1600, 2000, 2400, 2800, 3200, 3600]
    out["required_vehicles_grid"] = {"captures": caps, "tickets_amd": ticks,
                                     "vehicles_per_day": [[r0(v) for v in row] for row in engine.required_traffic_grid(a, "base", concept, caps, ticks)]}
    out["tornado_y3_ebitda"] = [{k: (r0(v) if isinstance(v, float) else v) for k, v in t.items()} for t in engine.tornado(a, "base", concept)]
    keys = [k for k, v in a.items() if isinstance(v, dict) and "status" in v]
    out["assumptions"] = {k: {f: a[k].get(f) for f in ("label", "value", "unit", "status", "source", "basis")} for k in keys}
    out["staffing"] = a.get("staffing")
    (ROOT / "results_summary.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    b = out["scenarios"]["base"]
    print(f"[{src}] base: invest {b['investment_amd'] / 1e6:.0f}M AMD, Y3 EBITDA {b['years'][2]['ebitda'] / 1e6:.1f}M, payback {b['payback_month']}, "
          f"BE {b['breakeven']['tx_per_day_ebitda_breakeven']} tx/day")


if __name__ == "__main__":
    main()
