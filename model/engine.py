"""
Drive-thru financial model engine (Python reference implementation).

The investor workbook (model/build_workbook.py -> model/DriveThru_Financial_Model.xlsx) re-implements
the same logic with live Excel formulas; model/verify.py recalculates the workbook with LibreOffice and
asserts both implementations agree. Keep the two in sync.

All money in AMD (nominal), converted to USD at the fixed FX rate in assumptions for presentation.
Monthly engine over 60 months from opening; annual roll-ups for the 5-year P&L.
"""
from __future__ import annotations

import json
import math
from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load_assumptions(path: Path | None = None) -> dict:
    path = path or ROOT / "assumptions.json"
    return json.loads(path.read_text())


def scen(a: dict, key: str, s: str):
    """Scenario-dependent input: a[key] is either a scalar or {'conservative','base','optimistic'}."""
    v = a[key]["value"] if isinstance(a[key], dict) and "value" in a[key] else a[key]
    if isinstance(v, dict) and s in v:
        return v[s]
    return v


def val(a: dict, key: str):
    v = a[key]
    return v["value"] if isinstance(v, dict) and "value" in v else v


def ramp_factor(month_idx: int, ramp: list[float]) -> float:
    """month_idx 0-based from opening; ramp list gives capture multipliers for first months."""
    return ramp[month_idx] if month_idx < len(ramp) else 1.0


def irr(cashflows: list[float], lo=-0.99, hi=5.0, tol=1e-7) -> float | None:
    def npv(r):
        return sum(cf / (1 + r) ** i for i, cf in enumerate(cashflows))
    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo * f_hi > 0:
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        f_mid = npv(mid)
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi, f_hi = mid, f_mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def capex_total(a: dict, concept: str) -> dict:
    items = a["capex"][concept]
    total = sum(i["amd"] for i in items)
    by_class = {}
    for i in items:
        by_class[i["dep_class"]] = by_class.get(i["dep_class"], 0) + i["amd"]
    return dict(total=total, by_class=by_class, items=items)


def run(a: dict, s: str = "base", concept: str | None = None, overrides: dict | None = None) -> dict:
    """Run one scenario. overrides: {key: value} applied as scalars (used by sensitivity)."""
    a = deepcopy(a)
    if overrides:
        for k, v in overrides.items():
            a[k] = {"value": v}
    concept = concept or val(a, "concept")
    fx = val(a, "fx_amd_per_usd")
    regime = val(a, "tax_regime") if "tax_regime" in a else "vat"
    vat = val(a, "vat_rate") if regime == "vat" else 0.0   # under catering turnover tax receipts carry no VAT
    months = 60
    start_month = val(a, "opening_month")          # 1..12 calendar month of opening
    infl_price = scen(a, "price_inflation", s)
    infl_cost = scen(a, "cost_inflation", s)
    wage_growth = scen(a, "wage_growth", s)

    aadt = scen(a, "traffic_aadt", s)              # two-way vehicles/day passing the site (annual average)
    traffic_growth = scen(a, "traffic_growth", s)
    access_share = scen(a, "accessible_share", s)  # share of passing traffic that can legally/conveniently enter
    capture = scen(a, "capture_rate", s)           # share of accessible vehicles that purchase (steady state Y1)
    capture_growth = scen(a, "capture_growth", s)  # annual relative growth in capture from brand awareness Y2..Y5
    seasonality = val(a, "seasonality_index")      # 12 values, mean 1.0, applied to traffic
    ramp = scen(a, "ramp_curve", s)
    ticket0 = scen(a, "avg_ticket_amd", s)         # VAT-inclusive average transaction value (per vehicle/order)
    other_tx = scen(a, "other_transactions_day", s)  # walk-in locals, pre-orders, delivery, staff of nearby businesses
    open_days = val(a, "open_days_per_year") / 365.0

    cogs_pct = scen(a, "cogs_pct", s)              # of net sales: food, beverage, packaging
    waste_pct = val(a, "waste_pct")
    card_share = val(a, "card_share")
    card_fee = val(a, "card_fee_pct")
    marketing_pct = val(a, "marketing_pct")
    launch_mkt = val(a, "launch_marketing_amd")
    rm_pct = val(a, "repairs_maint_pct")
    other_var_pct = val(a, "other_variable_pct")

    staff = a["staffing"][concept]
    rent_m = scen(a, "rent_amd_month", s) if val(a, "land_mode") == "lease" else 0.0
    land_tax_y = val(a, "land_property_tax_amd_year")
    util_fixed = val(a, "utilities_fixed_amd_month")[concept]
    util_var_pct = val(a, "utilities_variable_pct")
    fixed_other = val(a, "fixed_other_amd_month")   # insurance, accounting, security, waste, licences, IT
    profit_tax = val(a, "profit_tax_rate")
    dep_life = val(a, "depreciation_years")
    disc = val(a, "discount_rate")
    maint_capex_pct = val(a, "maintenance_capex_pct")
    wc_days = val(a, "working_capital_days")

    cx = capex_total(a, concept)
    capex = cx["total"]
    pre_opening = val(a, "pre_opening_costs_amd")[concept]

    rows = []
    loss_cf = 0.0
    cum_fcf = -(capex + pre_opening)
    payback_month = None
    for m in range(months):
        cal = (start_month - 1 + m) % 12
        yr = m // 12
        days = DAYS_IN_MONTH[cal] * open_days
        traffic = aadt * (1 + traffic_growth) ** yr * seasonality[cal]
        cap = capture * (1 + capture_growth) ** yr * ramp_factor(m, ramp)
        tx_day = traffic * access_share * cap + other_tx * ramp_factor(m, ramp)
        ticket = ticket0 * (1 + infl_price) ** yr
        gross = tx_day * days * ticket
        net = gross / (1 + vat)
        cogs = net * (cogs_pct + waste_pct)
        card = gross * card_share * card_fee
        mkt = net * marketing_pct + (launch_mkt if m < 3 else 0) / (3 if m < 3 else 1) * (1 if m < 3 else 0)
        rm = net * rm_pct
        other_var = net * other_var_pct
        util = util_fixed * (1 + infl_cost) ** yr + net * util_var_pct
        # labour: base FTE + seasonal FTE in peak months (seasonality > 1.15)
        peak = seasonality[cal] >= val(a, "peak_season_threshold")
        fte = staff["fte_base"] + (staff["fte_peak_extra"] if peak else 0)
        wage = staff["avg_gross_wage_amd"] * (1 + wage_growth) ** yr
        mgr = staff["manager_gross_amd"] * (1 + wage_growth) ** yr
        labour = (fte * wage + mgr) * (1 + val(a, "employer_oncost_pct")) + fte * val(a, "staff_meals_uniforms_amd_month")
        rent = rent_m * (1 + infl_cost) ** yr
        fixed = fixed_other * (1 + infl_cost) ** yr + land_tax_y / 12
        opex = cogs + card + mkt + rm + other_var + util + labour + rent + fixed
        ebitda = net - opex
        dep = sum(amt / dep_life[cls] / 12 for cls, amt in cx["by_class"].items() if dep_life.get(cls, 0) > 0 and m < dep_life[cls] * 12)
        ebit = ebitda - dep
        rows.append(dict(m=m + 1, year=yr + 1, cal_month=MONTHS[cal], days=days, traffic=traffic, capture=cap,
                         tx_day=tx_day, ticket=ticket, gross=gross, net=net, cogs=cogs, card=card, marketing=mkt,
                         rm=rm, other_var=other_var, utilities=util, labour=labour, rent=rent, fixed=fixed,
                         opex=opex, ebitda=ebitda, dep=dep, ebit=ebit, fte=fte))
    # annual roll-up with tax (annual, loss carry-forward 5 yrs simplified as unlimited within horizon)
    years = []
    prev_net = 0
    for y in range(1, 6):
        R = [r for r in rows if r["year"] == y]
        agg = {k: sum(r[k] for r in R) for k in ("gross", "net", "cogs", "card", "marketing", "rm", "other_var",
                                                 "utilities", "labour", "rent", "fixed", "opex", "ebitda", "dep", "ebit")}
        agg["transactions"] = sum(r["tx_day"] * r["days"] for r in R)
        agg["tx_per_day"] = agg["transactions"] / sum(r["days"] for r in R)
        agg["avg_ticket"] = agg["gross"] / agg["transactions"]
        agg["ebitda_pre_tt"] = agg["ebitda"]
        if regime == "catering_tt":
            # Tax Code Art. 254(6)-(7), 258: TT = 12% receipts - 9% documented opex (excl. capex, depreciation, repairs), floor 3.5%;
            # unused deductions carry forward. TT replaces VAT and profit tax, so it is shown above EBITDA.
            credit = val(a, "tt_deduction_rate") * (agg["opex"] - agg["rm"]) + loss_cf
            tt = max(val(a, "tt_rate") * agg["gross"] - credit, val(a, "tt_min_rate") * agg["gross"])
            loss_cf = max(0.0, credit - (val(a, "tt_rate") - val(a, "tt_min_rate")) * agg["gross"])
            agg["turnover_tax"] = tt
            agg["ebitda"] = agg["ebitda_pre_tt"] - tt
            agg["ebit"] = agg["ebitda"] - agg["dep"]
            tax = 0.0
        else:
            agg["turnover_tax"] = 0.0
            taxable = agg["ebit"] - loss_cf
            if taxable < 0:
                loss_cf = -taxable
                tax = 0.0
            else:
                loss_cf = 0.0
                tax = taxable * profit_tax
        agg["tax"] = tax
        agg["net_income"] = agg["ebit"] - tax
        agg["maint_capex"] = agg["net"] * maint_capex_pct if y > 1 else 0.0
        wc = agg["cogs"] * wc_days / 365.0
        agg["delta_wc"] = wc - (years[-1]["wc"] if years else 0.0)
        agg["wc"] = wc
        agg["ocf"] = agg["ebitda"] - tax - agg["delta_wc"]
        agg["fcf"] = agg["ocf"] - agg["maint_capex"]
        agg["ebitda_margin"] = agg["ebitda"] / agg["net"] if agg["net"] else 0
        years.append(agg)
    # payback (monthly, approximate tax and maint capex pro-rata by year)
    cum = -(capex + pre_opening)
    for r in rows:
        y = years[r["year"] - 1]
        cash = r["ebitda"] - (y["turnover_tax"] + y["tax"] + y["maint_capex"] + y["delta_wc"]) / 12
        cum += cash
        r["cum_cash"] = cum
        if payback_month is None and cum >= 0:
            payback_month = r["m"]
    invest = capex + pre_opening
    flows = [-invest] + [y["fcf"] for y in years]
    # residual value at end of Y5: book value of building/site works (conservative; no goodwill)
    residual = sum(amt * max(0.0, 1 - 5 / dep_life[c]) for c, amt in cx["by_class"].items() if dep_life.get(c, 0) > 0)
    if val(a, "land_mode") == "buy":
        residual += cx["by_class"].get("land", 0)
    flows_tv = flows[:-1] + [flows[-1] + residual]
    npv = sum(cf / (1 + disc) ** i for i, cf in enumerate(flows_tv))
    nopat_y3 = years[2]["ebit"] - years[2]["tax"]
    result = dict(
        scenario=s, concept=concept, fx=fx, capex=capex, pre_opening=pre_opening, investment=invest,
        capex_items=cx["items"], capex_by_class=cx["by_class"],
        years=years, months=rows, payback_month=payback_month,
        irr_5y_with_residual=irr(flows_tv), irr_5y_no_residual=irr(flows), npv=npv, residual=residual,
        roic_y3=nopat_y3 / invest if invest else None,
        cash_flows=flows_tv,
    )
    result["breakeven"] = breakeven(a, s, concept, result)
    return result


def _after_tax_ebitda(a: dict, R: float, var_pct: float, F: float, regime: str) -> float:
    """Annual EBITDA (after turnover tax if TT regime) for receipts R (revenue line), variable % of R and fixed costs F."""
    E = var_pct * R + F
    pre = R - E
    if regime == "catering_tt":
        rm_share = val(a, "repairs_maint_pct") * R
        tt = max(val(a, "tt_rate") * R - val(a, "tt_deduction_rate") * (E - rm_share), val(a, "tt_min_rate") * R)
        return pre - tt
    return pre


def _solve_R(a, target, var_pct, F, regime):
    lo, hi = 0.0, 1e11
    for _ in range(200):
        mid = (lo + hi) / 2
        if _after_tax_ebitda(a, mid, var_pct, F, regime) < target:
            lo = mid
        else:
            hi = mid
    return hi


def breakeven(a: dict, s: str, concept: str, res: dict) -> dict:
    """Steady-state (Year-2 cost base) break-even in transactions/day and passing vehicles/day."""
    regime = val(a, "tax_regime") if "tax_regime" in a else "vat"
    vat = val(a, "vat_rate") if regime == "vat" else 0.0
    y2 = res["years"][1]
    uv = val(a, "utilities_variable_pct")
    var_pct = (y2["cogs"] + y2["card"] + y2["rm"] + y2["other_var"] + y2["marketing"]) / y2["net"] + uv
    fixed_y = y2["labour"] + y2["rent"] + y2["fixed"] + (y2["utilities"] - y2["net"] * uv)
    ticket_net = y2["avg_ticket"] / (1 + vat)
    days = val(a, "open_days_per_year")
    R_be = _solve_R(a, 0.0, var_pct, fixed_y, regime)
    R_be_ebit = _solve_R(a, y2["dep"], var_pct, fixed_y, regime)
    tx_be = R_be / ticket_net / days
    tx_be_ebit = R_be_ebit / ticket_net / days
    access = scen(a, "accessible_share", s)
    cap = scen(a, "capture_rate", s) * (1 + scen(a, "capture_growth", s))
    other = scen(a, "other_transactions_day", s)
    veh_be = max(0.0, tx_be - other) / (access * cap)
    # 4-year simple cash payback: after-tax EBITDA (less profit tax in VAT regime, approx.) >= investment / 4
    tax_adj = 1.0 if regime == "catering_tt" else (1 - val(a, "profit_tax_rate") * 0.6)
    R_t = _solve_R(a, res["investment"] / 4 / tax_adj, var_pct, fixed_y, regime)
    tx_target = R_t / ticket_net / days
    veh_target = max(0.0, tx_target - other) / (access * cap)
    return dict(variable_cost_pct_of_net=var_pct, fixed_costs_year=fixed_y, contribution_per_tx=ticket_net * (1 - var_pct),
                ticket_net=ticket_net, tx_per_day_ebitda_breakeven=tx_be, tx_per_day_ebit_breakeven=tx_be_ebit,
                vehicles_per_day_breakeven=veh_be, tx_per_day_4yr_payback=tx_target, vehicles_per_day_4yr_payback=veh_target,
                capture_used=cap, access_used=access, revenue_breakeven=R_be, regime=regime)


def required_traffic_grid(a: dict, s: str, concept: str, captures: list[float], tickets: list[float]) -> list[list[float]]:
    """Two-way vehicles/day needed for (after-tax) EBITDA break-even for each (capture, ticket) pair, Year-2 costs & prices."""
    base = run(a, s, concept)
    be = base["breakeven"]
    regime = be["regime"]
    vat = val(a, "vat_rate") if regime == "vat" else 0.0
    R_be = be["revenue_breakeven"]
    grid = []
    for c in captures:
        row = []
        for t in tickets:
            t_net = t * (1 + scen(a, "price_inflation", s)) / (1 + vat)
            tx = R_be / t_net / val(a, "open_days_per_year")
            row.append(max(0.0, tx - scen(a, "other_transactions_day", s)) / (be["access_used"] * c))
        grid.append(row)
    return grid


def tornado(a: dict, s: str, concept: str, metric="ebitda_y3") -> list[dict]:
    base = run(a, s, concept)
    def m(res):
        return res["years"][2]["ebitda"] if metric == "ebitda_y3" else res["npv"]
    b = m(base)
    tests = [
        ("Average ticket ±15%", "avg_ticket_amd", 0.15),
        ("Capture rate ±30%", "capture_rate", 0.30),
        ("Passing traffic ±20%", "traffic_aadt", 0.20),
        ("Accessible share ±20%", "accessible_share", 0.20),
        ("Labour cost ±20%", "_labour", 0.20),
        ("COGS ±3 pp", "cogs_pct", None),
        ("Rent ±30%", "rent_amd_month", 0.30),
        ("Seasonality amplitude ±30%", "_season", 0.30),
    ]
    out = []
    for label, key, pct in tests:
        vals = []
        for sign in (-1, 1):
            aa = deepcopy(a)
            if key == "_labour":
                for c in aa["staffing"].values():
                    c["avg_gross_wage_amd"] *= 1 + sign * pct
                    c["manager_gross_amd"] *= 1 + sign * pct
                r = run(aa, s, concept)
            elif key == "_season":
                si = val(aa, "seasonality_index")
                aa["seasonality_index"] = {"value": [1 + (x - 1) * (1 + sign * pct) for x in si]}
                r = run(aa, s, concept)
            elif key == "cogs_pct":
                r = run(aa, s, concept, overrides={key: scen(a, key, s) + sign * 0.03})
            else:
                r = run(aa, s, concept, overrides={key: scen(a, key, s) * (1 + sign * pct)})
            vals.append(m(r))
        out.append(dict(label=label, low=vals[0], high=vals[1], base=b))
    out.sort(key=lambda d: -abs(d["high"] - d["low"]))
    return out


if __name__ == "__main__":
    a = load_assumptions()
    for s in ("conservative", "base", "optimistic"):
        r = run(a, s)
        y = r["years"]
        print(s, f"capex {r['investment']/1e6:.0f}M AMD", [f"{x['net']/1e6:.0f}/{x['ebitda']/1e6:.0f}" for x in y],
              "payback m", r["payback_month"], "IRR", r["irr_5y_with_residual"])
