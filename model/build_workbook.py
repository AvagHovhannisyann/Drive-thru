"""
Generates the investor workbook with LIVE Excel formulas from model/assumptions.json.

Sheets
  Cover        purpose, how to use, colour legend, scenario summary (formulas)
  Inputs       every assumption: Conservative | Base | Optimistic | unit | status | source
  Capex        line items for Lean / Mid / Flagship, totals by depreciation class
  M_Cons, M_Base, M_Opt   60-month engines (one per scenario)
  Annual       5-year P&L, tax with loss carry-forward, cash flow, payback, NPV, IRR (per scenario)
  BreakEven    break-even transactions/day and passing vehicles/day + required-traffic grid
  Sensitivity  tornado (values from engine.py) + two-way grids (formulas)

Blue font = input, black = formula. Change Inputs and everything recalculates.
Run: python3 model/build_workbook.py  -> model/DriveThru_Financial_Model.xlsx
"""
from __future__ import annotations

import json
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter as COL
from openpyxl.worksheet.datavalidation import DataValidation

import engine

ROOT = Path(__file__).resolve().parent
A = json.loads((ROOT / "assumptions.json").read_text())
BRAND = json.loads((ROOT.parent / "brand/out/brand.json").read_text()) if (ROOT.parent / "brand/out/brand.json").exists() else {}
NAME = BRAND.get("name_latin", "Drive-thru")
OUT = ROOT / "DriveThru_Financial_Model.xlsx"

SCEN = ["conservative", "base", "optimistic"]
SC_COL = {"conservative": "D", "base": "E", "optimistic": "F"}
SHEET = {"conservative": "M_Cons", "base": "M_Base", "optimistic": "M_Opt"}

F_IN = Font(name="Calibri", color="1F4FB4", bold=False)
F_B = Font(name="Calibri", bold=True)
F_H = Font(name="Calibri", bold=True, color="FFFFFF")
F_T = Font(name="Calibri", bold=True, size=16)
FILL_H = PatternFill("solid", fgColor="2B3A2F")
FILL_IN = PatternFill("solid", fgColor="FFF6E8")
FILL_SUB = PatternFill("solid", fgColor="EEE9E0")
THIN = Side(style="thin", color="C8C2B8")
B_BOT = Border(bottom=THIN)
AMD = '#,##0;[Red]-#,##0'
AMDM = '#,##0.0,,"M";[Red]-#,##0.0,,"M"'
PCT = '0.0%'
PCT2 = '0.00%'

wb = Workbook()
ROW = {}       # input key -> row on Inputs
RANGE = {}     # special ranges


def header(ws, row, labels, widths=None):
    for i, l in enumerate(labels):
        c = ws.cell(row=row, column=i + 1, value=l)
        c.font = F_H
        c.fill = FILL_H
        c.alignment = Alignment(vertical="center", wrap_text=True)
    if widths:
        for i, w in enumerate(widths):
            ws.column_dimensions[COL(i + 1)].width = w


# ======================================================================================
# Inputs
# ======================================================================================
inp = wb.active
inp.title = "Inputs"
inp["A1"] = f"{NAME} — model inputs"
inp["A1"].font = F_T
inp["A2"] = "Blue cells are inputs. Status: VERIFIED (primary source) · REPORTED (secondary) · ESTIMATE (derived) · ASSUMPTION (judgement). See research/ for evidence files."
header(inp, 4, ["Key", "Input", "Unit", "Conservative", "Base", "Optimistic", "Status", "Source / basis"], [26, 46, 16, 15, 15, 15, 13, 90])
r = 5


def put_input(key, label, unit, vals, status, source, fmt=None):
    global r
    inp.cell(row=r, column=1, value=key)
    inp.cell(row=r, column=2, value=label)
    inp.cell(row=r, column=3, value=unit)
    for j, v in enumerate(vals):
        c = inp.cell(row=r, column=4 + j, value=v)
        c.font = F_IN
        c.fill = FILL_IN
        if fmt:
            c.number_format = fmt
    inp.cell(row=r, column=7, value=status)
    inp.cell(row=r, column=8, value=source)
    ROW[key] = r
    r += 1


def section(title):
    global r
    r += 1
    c = inp.cell(row=r, column=1, value=title)
    c.font = F_B
    for j in range(1, 9):
        inp.cell(row=r, column=j).fill = FILL_SUB
    r += 1


def scalar_or_scen(key):
    v = A[key]["value"]
    if isinstance(v, dict) and set(v) >= set(SCEN):
        return [v[s] for s in SCEN]
    return [v, v, v]


PCT_KEYS = {"vat_rate", "profit_tax_rate", "discount_rate", "traffic_growth", "accessible_share", "capture_rate", "capture_growth",
            "price_inflation", "cost_inflation", "wage_growth", "cogs_pct", "waste_pct", "card_share", "card_fee_pct", "marketing_pct",
            "repairs_maint_pct", "other_variable_pct", "utilities_variable_pct", "employer_oncost_pct", "maintenance_capex_pct"}

section("General")
for k in ["fx_amd_per_usd", "opening_month", "open_days_per_year", "vat_rate", "profit_tax_rate", "discount_rate"]:
    a = A[k]
    put_input(k, a["label"], a["unit"], scalar_or_scen(k), a["status"], a["source"] + (" — " + a["basis"] if a.get("basis") else ""),
              PCT2 if k in PCT_KEYS else ('#,##0.00' if k == "fx_amd_per_usd" else None))
put_input("tax_regime_tt", "Catering turnover-tax regime? (1 = TT, 0 = VAT + profit tax)", "flag",
          [1 if A.get("tax_regime", {}).get("value", "vat") == "catering_tt" else 0] * 3, A.get("tax_regime", {}).get("status", "ASSUMPTION"),
          A.get("tax_regime", {}).get("source", ""))
for k in ["tt_rate", "tt_deduction_rate", "tt_min_rate"]:
    if k in A:
        put_input(k, A[k]["label"], A[k]["unit"], [A[k]["value"]] * 3, A[k]["status"], A[k]["source"], PCT2)
# concept selector
put_input("concept_index", "Concept modelled (1 = Lean, 2 = Mid-range, 3 = Flagship)", "index", [2, 2, 2], "ASSUMPTION", "Recommended: Mid-range")
put_input("land_mode_lease", "Land via ground lease? (1 = lease, 0 = buy)", "flag", [1 if A["land_mode"]["value"] == "lease" else 0] * 3, "ASSUMPTION", A["land_mode"]["source"])
section("Demand")
for k in ["traffic_aadt", "traffic_growth", "accessible_share", "capture_rate", "capture_growth", "avg_ticket_amd", "other_transactions_day", "price_inflation"]:
    a = A[k]
    put_input(k, a["label"], a["unit"], scalar_or_scen(k), a["status"], a["source"] + (" — " + a["basis"] if a.get("basis") else ""),
              PCT2 if k in PCT_KEYS else '#,##0')
section("Seasonality index (traffic, mean = 1.00)")
RANGE["season_row0"] = r
for i, (m, v) in enumerate(zip(engine.MONTHS, A["seasonality_index"]["value"])):
    put_input(f"season_{i + 1}", f"Seasonality — {m}", "index", [v, v, v], A["seasonality_index"]["status"], A["seasonality_index"]["source"] if i == 0 else "", '0.00')
section("Opening ramp (capture multiplier by month since opening)")
RANGE["ramp_row0"] = r
for i in range(12):
    vals = [A["ramp_curve"]["value"][s][i] for s in SCEN]
    put_input(f"ramp_{i + 1}", f"Ramp — month {i + 1}", "x", vals, A["ramp_curve"]["status"], A["ramp_curve"]["source"] if i == 0 else "", '0.00')
section("Operating costs")
for k in ["cogs_pct", "waste_pct", "card_share", "card_fee_pct", "marketing_pct", "launch_marketing_amd", "repairs_maint_pct", "other_variable_pct",
          "utilities_variable_pct", "fixed_other_amd_month", "rent_amd_month", "land_property_tax_amd_year", "employer_oncost_pct",
          "staff_meals_uniforms_amd_month", "peak_season_threshold", "cost_inflation", "wage_growth", "maintenance_capex_pct", "working_capital_days"]:
    a = A[k]
    put_input(k, a["label"], a["unit"], scalar_or_scen(k), a["status"], a["source"] + (" — " + a["basis"] if a.get("basis") else ""),
              PCT2 if k in PCT_KEYS else ('0.00' if k == "peak_season_threshold" else '#,##0'))
section("Concept-dependent inputs (Lean | Mid-range | Flagship) — NOTE columns are concepts, not scenarios")
CON = ["lean", "mid", "flagship"]
for k, lab in [("fte_base", "Base FTE (crew)"), ("fte_peak_extra", "Extra FTE in peak months"), ("avg_gross_wage_amd", "Average crew gross wage (AMD/month)"),
               ("manager_gross_amd", "Store manager gross wage (AMD/month)")]:
    put_input(f"c_{k}", lab, "concept", [A["staffing"][c][k] for c in CON], "ESTIMATE", A["staffing"].get("_source", "See research/C3-labor.md"), '#,##0')
put_input("c_util_fixed", A["utilities_fixed_amd_month"]["label"], "AMD/month", [A["utilities_fixed_amd_month"]["value"][c] for c in CON],
          A["utilities_fixed_amd_month"]["status"], A["utilities_fixed_amd_month"]["source"], '#,##0')
put_input("c_preopen", A["pre_opening_costs_amd"]["label"], "AMD", [A["pre_opening_costs_amd"]["value"][c] for c in CON],
          A["pre_opening_costs_amd"]["status"], A["pre_opening_costs_amd"]["source"], '#,##0')
section("Depreciation lives (years; 0 = not depreciated)")
for cls, yrs in A["depreciation_years"]["value"].items():
    put_input(f"dep_{cls}", f"Life — {cls}", "years", [yrs] * 3, A["depreciation_years"]["status"], A["depreciation_years"]["source"] if cls == "building" else "")
inp.freeze_panes = "D5"


def I_(key, s="base"):
    """Absolute reference to an input cell for scenario s."""
    return f"Inputs!${SC_COL[s]}${ROW[key]}"


def CI(key):
    """Concept-dependent input selected by concept_index (base column holds the index)."""
    rr = ROW[key]
    return f"INDEX(Inputs!$D${rr}:$F${rr},1,Inputs!$E${ROW['concept_index']})"


# ======================================================================================
# Capex
# ======================================================================================
cx = wb.create_sheet("Capex")
cx["A1"] = f"{NAME} — startup investment by concept (AMD, excl. VAT)"
cx["A1"].font = F_T
cx["A2"] = "Line items with status tags. USD at the Inputs exchange rate. Detailed build-ups in the report (Phase 6)."
header(cx, 4, ["Line item", "Depreciation class", "Lean", "Mid-range", "Flagship", "Status", "Source / basis"], [52, 18, 16, 16, 16, 13, 80])
names = []
for c in CON:
    for it in A["capex"][c]:
        if it["name"] not in names:
            names.append(it["name"])
cr = 5
CAPEX_ROWS = (cr, cr + len(names) - 1)
for n in names:
    ref = None
    for c in CON:
        for it in A["capex"][c]:
            if it["name"] == n:
                ref = it
    cx.cell(row=cr, column=1, value=n)
    cx.cell(row=cr, column=2, value=ref["dep_class"])
    for j, c in enumerate(CON):
        amt = next((it["amd"] for it in A["capex"][c] if it["name"] == n), 0)
        cell = cx.cell(row=cr, column=3 + j, value=amt)
        cell.font = F_IN
        cell.fill = FILL_IN
        cell.number_format = AMD
    cx.cell(row=cr, column=6, value=ref.get("status", ""))
    cx.cell(row=cr, column=7, value=ref.get("source", ""))
    cr += 1
r0, r1 = CAPEX_ROWS
cx.cell(row=cr, column=1, value="TOTAL CAPEX").font = F_B
for j in range(3):
    c = cx.cell(row=cr, column=3 + j, value=f"=SUM({COL(3 + j)}{r0}:{COL(3 + j)}{r1})")
    c.font = F_B
    c.number_format = AMD
CAPEX_TOTAL_ROW = cr
cr += 1
cx.cell(row=cr, column=1, value="Pre-opening costs (from Inputs)")
for j in range(3):
    cx.cell(row=cr, column=3 + j, value=f"=Inputs!{COL(4 + j)}{ROW['c_preopen']}").number_format = AMD
PRE_ROW = cr
cr += 1
cx.cell(row=cr, column=1, value="TOTAL INVESTMENT (capex + pre-opening)").font = F_B
for j in range(3):
    c = cx.cell(row=cr, column=3 + j, value=f"={COL(3 + j)}{CAPEX_TOTAL_ROW}+{COL(3 + j)}{PRE_ROW}")
    c.font = F_B
    c.number_format = AMD
INV_ROW = cr
cr += 1
cx.cell(row=cr, column=1, value="TOTAL INVESTMENT (USD)").font = F_B
for j in range(3):
    c = cx.cell(row=cr, column=3 + j, value=f"={COL(3 + j)}{INV_ROW}/{I_('fx_amd_per_usd')}")
    c.font = F_B
    c.number_format = '"$"#,##0'
cr += 2
cx.cell(row=cr, column=1, value="Capex by depreciation class").font = F_B
cr += 1
CLASS_ROW = {}
for cls in A["depreciation_years"]["value"]:
    cx.cell(row=cr, column=1, value=cls)
    for j in range(3):
        cx.cell(row=cr, column=3 + j, value=f'=SUMIF($B${r0}:$B${r1},"{cls}",{COL(3 + j)}${r0}:{COL(3 + j)}${r1})').number_format = AMD
    CLASS_ROW[cls] = cr
    cr += 1


def CAPCLS(cls):
    rr = CLASS_ROW[cls]
    return f"INDEX(Capex!$C${rr}:$E${rr},1,Inputs!$E${ROW['concept_index']})"


INVEST = f"INDEX(Capex!$C${INV_ROW}:$E${INV_ROW},1,Inputs!$E${ROW['concept_index']})"
CAPEX_T = f"INDEX(Capex!$C${CAPEX_TOTAL_ROW}:$E${CAPEX_TOTAL_ROW},1,Inputs!$E${ROW['concept_index']})"

# ======================================================================================
# Monthly engines
# ======================================================================================
LINES = ["Month #", "Year", "Calendar month (1-12)", "Trading days", "Seasonality index", "Passing traffic (veh/day)", "Ramp multiplier",
         "Capture rate", "Transactions / day", "Average ticket (AMD, incl. VAT)", "Gross sales (incl. VAT)", "Net sales (excl. VAT)",
         "COGS + waste", "Card fees", "Marketing", "Repairs & maintenance", "Other variable", "Utilities", "Peak-season flag", "FTE",
         "Labour", "Ground rent", "Other fixed + land tax", "Total operating costs", "EBITDA", "Depreciation", "EBIT",
         "Cash before tax/capex adj.", "Cumulative cash (after investment)", "Payback flag"]
LR = {name: i + 3 for i, name in enumerate(LINES)}
NM = 60
ANNUAL = {}   # filled later; needed for cash rows (forward refs are fine in Excel)


def build_engine(s):
    ws = wb.create_sheet(SHEET[s])
    ws["A1"] = f"{NAME} — monthly engine — {s.upper()} scenario (AMD)"
    ws["A1"].font = F_T
    ws.column_dimensions["A"].width = 38
    ws.column_dimensions["B"].width = 14
    for name, rr in LR.items():
        ws.cell(row=rr, column=1, value=name)
    ws.cell(row=2, column=2, value="Units").font = F_B
    sc = SC_COL[s]
    def IN(k):
        return f"Inputs!${sc}${ROW[k]}"
    for m in range(1, NM + 1):
        c = 2 + m           # column index (C = month 1)
        L_ = COL(c)
        P = COL(c - 1)
        R = lambda name: f"{L_}{LR[name]}"
        f = {}
        f["Month #"] = m
        f["Year"] = f"=INT(({R('Month #')}-1)/12)+1"
        f["Calendar month (1-12)"] = f"=MOD({IN('opening_month')}-1+{R('Month #')}-1,12)+1"
        f["Trading days"] = f"=CHOOSE({R('Calendar month (1-12)')},31,28,31,30,31,30,31,31,30,31,30,31)*{IN('open_days_per_year')}/365"
        f["Seasonality index"] = f"=INDEX(Inputs!${sc}${RANGE['season_row0']}:${sc}${RANGE['season_row0'] + 11},{R('Calendar month (1-12)')})"
        f["Passing traffic (veh/day)"] = f"={IN('traffic_aadt')}*(1+{IN('traffic_growth')})^({R('Year')}-1)*{R('Seasonality index')}"
        f["Ramp multiplier"] = f"=IF({R('Month #')}<=12,INDEX(Inputs!${sc}${RANGE['ramp_row0']}:${sc}${RANGE['ramp_row0'] + 11},{R('Month #')}),1)"
        f["Capture rate"] = f"={IN('capture_rate')}*(1+{IN('capture_growth')})^({R('Year')}-1)*{R('Ramp multiplier')}"
        f["Transactions / day"] = f"={R('Passing traffic (veh/day)')}*{IN('accessible_share')}*{R('Capture rate')}+{IN('other_transactions_day')}*{R('Ramp multiplier')}"
        f["Average ticket (AMD, incl. VAT)"] = f"={IN('avg_ticket_amd')}*(1+{IN('price_inflation')})^({R('Year')}-1)"
        f["Gross sales (incl. VAT)"] = f"={R('Transactions / day')}*{R('Trading days')}*{R('Average ticket (AMD, incl. VAT)')}"
        f["Net sales (excl. VAT)"] = f"={R('Gross sales (incl. VAT)')}/(1+{IN('vat_rate')}*(1-{IN('tax_regime_tt')}))"
        f["COGS + waste"] = f"={R('Net sales (excl. VAT)')}*({IN('cogs_pct')}+{IN('waste_pct')})"
        f["Card fees"] = f"={R('Gross sales (incl. VAT)')}*{IN('card_share')}*{IN('card_fee_pct')}"
        f["Marketing"] = f"={R('Net sales (excl. VAT)')}*{IN('marketing_pct')}+IF({R('Month #')}<=3,{IN('launch_marketing_amd')}/3,0)"
        f["Repairs & maintenance"] = f"={R('Net sales (excl. VAT)')}*{IN('repairs_maint_pct')}"
        f["Other variable"] = f"={R('Net sales (excl. VAT)')}*{IN('other_variable_pct')}"
        f["Utilities"] = f"={CI('c_util_fixed')}*(1+{IN('cost_inflation')})^({R('Year')}-1)+{R('Net sales (excl. VAT)')}*{IN('utilities_variable_pct')}"
        f["Peak-season flag"] = f"=IF({R('Seasonality index')}>={IN('peak_season_threshold')},1,0)"
        f["FTE"] = f"={CI('c_fte_base')}+{R('Peak-season flag')}*{CI('c_fte_peak_extra')}"
        f["Labour"] = (f"=({R('FTE')}*{CI('c_avg_gross_wage_amd')}+{CI('c_manager_gross_amd')})*(1+{IN('wage_growth')})^({R('Year')}-1)"
                       f"*(1+{IN('employer_oncost_pct')})+{R('FTE')}*{IN('staff_meals_uniforms_amd_month')}")
        f["Ground rent"] = f"={IN('land_mode_lease')}*{IN('rent_amd_month')}*(1+{IN('cost_inflation')})^({R('Year')}-1)"
        f["Other fixed + land tax"] = f"={IN('fixed_other_amd_month')}*(1+{IN('cost_inflation')})^({R('Year')}-1)+{IN('land_property_tax_amd_year')}/12"
        f["Total operating costs"] = (f"=SUM({L_}{LR['COGS + waste']}:{L_}{LR['Utilities']})+{R('Labour')}+{R('Ground rent')}+{R('Other fixed + land tax')}")
        f["EBITDA"] = f"={R('Net sales (excl. VAT)')}-{R('Total operating costs')}"
        dep_terms = []
        for cls in A["depreciation_years"]["value"]:
            life = f"Inputs!$E${ROW['dep_' + cls]}"
            dep_terms.append(f"IF(AND({life}>0,{R('Month #')}<={life}*12),{CAPCLS(cls)}/MAX({life},1)/12,0)")
        f["Depreciation"] = "=" + "+".join(dep_terms)
        f["EBIT"] = f"={R('EBITDA')}-{R('Depreciation')}"
        # annual adjustments pulled from Annual sheet (tax, maintenance capex, delta WC) spread evenly
        f["Cash before tax/capex adj."] = (f"={R('EBITDA')}-(INDEX(Annual!$C${{TAX}}:$G${{TAX}},1,{R('Year')})+INDEX(Annual!$C${{TT}}:$G${{TT}},1,{R('Year')})"
                                            f"+INDEX(Annual!$C${{MCX}}:$G${{MCX}},1,{R('Year')})+INDEX(Annual!$C${{DWC}}:$G${{DWC}},1,{R('Year')}))/12")
        f["Cumulative cash (after investment)"] = (f"=-{INVEST}+{R('Cash before tax/capex adj.')}" if m == 1 else
                                                   f"={P}{LR['Cumulative cash (after investment)']}+{R('Cash before tax/capex adj.')}")
        f["Payback flag"] = f"=IF({R('Cumulative cash (after investment)')}>=0,{R('Month #')},999)"
        for name, val in f.items():
            cell = ws.cell(row=LR[name], column=c, value=val)
            if name in ("Capture rate",):
                cell.number_format = PCT2
            elif name in ("Seasonality index", "Ramp multiplier", "Trading days", "Transactions / day", "FTE"):
                cell.number_format = '0.0'
            elif name in ("Month #", "Year", "Calendar month (1-12)", "Peak-season flag", "Payback flag"):
                cell.number_format = '0'
            else:
                cell.number_format = AMD
        ws.column_dimensions[L_].width = 12.5
        ws.cell(row=2, column=c, value=f'=CHOOSE({L_}{LR["Calendar month (1-12)"]},"Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")&" Y"&{L_}{LR["Year"]}').font = F_B
    for name in ("Net sales (excl. VAT)", "EBITDA", "Total operating costs", "Cumulative cash (after investment)"):
        ws.cell(row=LR[name], column=1).font = F_B
    ws.freeze_panes = "C3"
    return ws


ENG = {s: build_engine(s) for s in SCEN}

# ======================================================================================
# Annual
# ======================================================================================
an = wb.create_sheet("Annual", 1)
an["A1"] = f"{NAME} — 5-year P&L and cash flow (AMD, nominal)"
an["A1"].font = F_T
an.column_dimensions["A"].width = 44
an.column_dimensions["B"].width = 4
for j in range(5):
    an.column_dimensions[COL(3 + j)].width = 16
an.column_dimensions["H"].width = 3
ROWS_A = ["Transactions (year)", "Transactions / day (avg)", "Average ticket (AMD incl. VAT)", "Gross sales (incl. VAT)", "Net sales (excl. VAT)",
          "COGS + waste", "Gross profit", "Gross margin %", "Labour", "Ground rent", "Utilities", "Card fees", "Marketing", "Repairs & maintenance",
          "Other variable", "Other fixed + land tax", "Total operating costs", "EBITDA before turnover tax", "TT deduction credit (incl. carried)",
          "Turnover tax (catering TT)", "EBITDA", "EBITDA margin %", "Depreciation", "EBIT", "Loss carried forward (opening)",
          "Taxable profit", "Profit tax", "Net income", "Net margin %", "Maintenance capex", "Working capital (closing)", "Δ Working capital",
          "Operating cash flow", "Free cash flow", "Cumulative FCF after investment"]
SUMMARY_ROWS = {}
TAXROW = {}
blk = 3
for s in SCEN:
    src = SHEET[s]
    an.cell(row=blk, column=1, value=f"{s.upper()} SCENARIO").font = Font(bold=True, size=13)
    for j in range(5):
        c = an.cell(row=blk, column=3 + j, value=f"Year {j + 1}")
        c.font = F_H
        c.fill = FILL_H
    rows = {name: blk + 1 + i for i, name in enumerate(ROWS_A)}
    rng = lambda line: f"{src}!$C${LR[line]}:$BJ${LR[line]}"
    yr = f"{src}!$C${LR['Year']}:$BJ${LR['Year']}"
    for name, rr in rows.items():
        an.cell(row=rr, column=1, value=name)
    for j in range(5):
        Y = j + 1
        L_ = COL(3 + j)
        P = COL(2 + j)
        R = lambda n: f"{L_}{rows[n]}"
        def SUMY(line):
            return f"=SUMIF({yr},{Y},{rng(line)})"
        f = {}
        f["Transactions (year)"] = f"=SUMPRODUCT(({yr}={Y})*{rng('Transactions / day')}*{rng('Trading days')})"
        f["Transactions / day (avg)"] = f"={R('Transactions (year)')}/SUMIF({yr},{Y},{rng('Trading days')})"
        f["Average ticket (AMD incl. VAT)"] = f"={R('Gross sales (incl. VAT)')}/{R('Transactions (year)')}"
        f["Gross sales (incl. VAT)"] = SUMY("Gross sales (incl. VAT)")
        f["Net sales (excl. VAT)"] = SUMY("Net sales (excl. VAT)")
        f["COGS + waste"] = SUMY("COGS + waste")
        f["Gross profit"] = f"={R('Net sales (excl. VAT)')}-{R('COGS + waste')}"
        f["Gross margin %"] = f"=IFERROR({R('Gross profit')}/{R('Net sales (excl. VAT)')},0)"
        for line in ("Labour", "Ground rent", "Utilities", "Card fees", "Marketing", "Repairs & maintenance", "Other variable", "Other fixed + land tax",
                     "Total operating costs", "Depreciation"):
            f[line] = SUMY(line)
        f["EBITDA before turnover tax"] = SUMY("EBITDA")
        tt = I_('tax_regime_tt', s)
        f["TT deduction credit (incl. carried)"] = (f"={tt}*({I_('tt_deduction_rate', s)}*({R('Total operating costs')}-{R('Repairs & maintenance')})"
                                                    f"+{R('Loss carried forward (opening)')})")
        f["Turnover tax (catering TT)"] = (f"={tt}*MAX({I_('tt_rate', s)}*{R('Gross sales (incl. VAT)')}-{R('TT deduction credit (incl. carried)')},"
                                           f"{I_('tt_min_rate', s)}*{R('Gross sales (incl. VAT)')})")
        f["EBITDA"] = f"={R('EBITDA before turnover tax')}-{R('Turnover tax (catering TT)')}"
        f["EBIT"] = f"={R('EBITDA')}-{R('Depreciation')}"
        f["EBITDA margin %"] = f"=IFERROR({R('EBITDA')}/{R('Net sales (excl. VAT)')},0)"
        f["Loss carried forward (opening)"] = "=0" if Y == 1 else f"=MAX(0,-({P}{rows['EBIT']}-{P}{rows['Loss carried forward (opening)']}))"
        f["Taxable profit"] = f"=(1-{tt})*MAX(0,{R('EBIT')}-{R('Loss carried forward (opening)')})"
        f["Profit tax"] = f"={R('Taxable profit')}*{I_('profit_tax_rate', s)}"
        f["Net income"] = f"={R('EBIT')}-{R('Profit tax')}"
        f["Net margin %"] = f"=IFERROR({R('Net income')}/{R('Net sales (excl. VAT)')},0)"
        f["Maintenance capex"] = "=0" if Y == 1 else f"={R('Net sales (excl. VAT)')}*{I_('maintenance_capex_pct', s)}"
        f["Working capital (closing)"] = f"={R('COGS + waste')}*{I_('working_capital_days', s)}/365"
        f["Δ Working capital"] = f"={R('Working capital (closing)')}" if Y == 1 else f"={R('Working capital (closing)')}-{P}{rows['Working capital (closing)']}"
        f["Operating cash flow"] = f"={R('EBITDA')}-{R('Profit tax')}-{R('Δ Working capital')}"
        f["Free cash flow"] = f"={R('Operating cash flow')}-{R('Maintenance capex')}"
        f["Cumulative FCF after investment"] = (f"=-{INVEST}+{R('Free cash flow')}" if Y == 1 else f"={P}{rows['Cumulative FCF after investment']}+{R('Free cash flow')}")
        for name, val in f.items():
            cell = an.cell(row=rows[name], column=3 + j, value=val)
            cell.number_format = PCT if "%" in name else ('#,##0' if name in ("Transactions (year)", "Transactions / day (avg)", "Average ticket (AMD incl. VAT)") else AMD)
    for name in ("Net sales (excl. VAT)", "EBITDA", "Net income", "Free cash flow"):
        an.cell(row=rows[name], column=1).font = F_B
    # Loss carry-forward fix: opening loss = cumulative unused losses
    ttf = I_('tax_regime_tt', s)
    for j in range(1, 5):
        L_ = COL(3 + j)
        P = COL(2 + j)
        an.cell(row=rows["Loss carried forward (opening)"], column=3 + j,
                value=(f"=IF({ttf}=1,MAX(0,{P}{rows['TT deduction credit (incl. carried)']}-({I_('tt_rate', s)}-{I_('tt_min_rate', s)})*{P}{rows['Gross sales (incl. VAT)']}),"
                       f"MAX(0,{P}{rows['Loss carried forward (opening)']}-{P}{rows['EBIT']}))"))
    # KPIs
    k0 = rows[ROWS_A[-1]] + 2
    kp = {
        "Total investment (capex + pre-opening)": f"={INVEST}",
        "Total investment (USD)": f"={INVEST}/{I_('fx_amd_per_usd', s)}",
        "Payback (months from opening)": f"=IF(MIN({src}!$C${LR['Payback flag']}:$BJ${LR['Payback flag']})>60,\"> 60\",MIN({src}!$C${LR['Payback flag']}:$BJ${LR['Payback flag']}))",
        "Residual value end-Y5 (book value of fixed assets)": "=" + "+".join(
            f"{CAPCLS(cls)}*MAX(0,1-5/MAX(Inputs!$E${ROW['dep_' + cls]},0.0001))*(Inputs!$E${ROW['dep_' + cls]}>0)" for cls in A["depreciation_years"]["value"]),
        "NPV @ discount rate (5 yrs + residual)": None,
        "IRR (5 yrs + residual)": None,
        "IRR (5 yrs, no residual)": None,
        "ROIC Year 3 (NOPAT / investment)": f"=(E{rows['EBIT']}-E{rows['Profit tax']})/{INVEST}",
        "Year-3 EBITDA (USD)": f"=E{rows['EBITDA']}/{I_('fx_amd_per_usd', s)}",
    }
    krow = {}
    for i, (name, val) in enumerate(kp.items()):
        rr = k0 + i
        krow[name] = rr
        an.cell(row=rr, column=1, value=name).font = F_B
    # cash flow row for NPV/IRR in hidden helper cells (I..N)
    cf_row = k0 + len(kp) + 1
    an.cell(row=cf_row, column=1, value="Cash flows for IRR: Y0 … Y5 (+ residual in Y5)")
    an.cell(row=cf_row, column=3, value=f"=-{INVEST}").number_format = AMD
    for j in range(5):
        L_ = COL(4 + j)
        val = f"={COL(3 + j)}{rows['Free cash flow']}" + (f"+C{krow['Residual value end-Y5 (book value of fixed assets)']}" if j == 4 else "")
        an.cell(row=cf_row, column=4 + j, value=val).number_format = AMD
    cf2 = cf_row + 1
    an.cell(row=cf2, column=1, value="Cash flows (no residual)")
    an.cell(row=cf2, column=3, value=f"=-{INVEST}").number_format = AMD
    for j in range(5):
        an.cell(row=cf2, column=4 + j, value=f"={COL(3 + j)}{rows['Free cash flow']}").number_format = AMD
    kp["NPV @ discount rate (5 yrs + residual)"] = f"=C{cf_row}+NPV({I_('discount_rate', s)},D{cf_row}:H{cf_row})"
    kp["IRR (5 yrs + residual)"] = f"=IFERROR(IRR(C{cf_row}:H{cf_row}),\"n/a\")"
    kp["IRR (5 yrs, no residual)"] = f"=IFERROR(IRR(C{cf2}:H{cf2}),\"n/a\")"
    for name, val in kp.items():
        c = an.cell(row=krow[name], column=3, value=val)
        c.number_format = PCT if ("IRR" in name or "ROIC" in name) else ('"$"#,##0' if "USD" in name else AMD)
    SUMMARY_ROWS[s] = dict(rows=rows, krow=krow)
    TAXROW[s] = (rows["Profit tax"], rows["Maintenance capex"], rows["Δ Working capital"], rows["Turnover tax (catering TT)"])
    blk = cf2 + 3

an.freeze_panes = "C3"
# patch engine cash formulas with Annual row numbers
for s in SCEN:
    ws = ENG[s]
    tax, mcx, dwc, ttr = TAXROW[s]
    rr = LR["Cash before tax/capex adj."]
    for m in range(1, NM + 1):
        c = ws.cell(row=rr, column=2 + m)
        c.value = c.value.replace("{TAX}", str(tax)).replace("{MCX}", str(mcx)).replace("{DWC}", str(dwc)).replace("{TT}", str(ttr))

# ======================================================================================
# Break-even
# ======================================================================================
be = wb.create_sheet("BreakEven", 2)
be["A1"] = f"{NAME} — break-even and required traffic (Year-2 cost base)"
be["A1"].font = F_T
be.column_dimensions["A"].width = 58
for j in range(3):
    be.column_dimensions[COL(3 + j)].width = 18
header(be, 3, ["Metric", "", "Conservative", "Base", "Optimistic"])
BE_LINES = ["Year-2 net sales", "Variable costs as % of net sales", "Fixed costs per year (labour, rent, fixed, utilities fixed)",
            "Net ticket (excl. VAT)", "Contribution per transaction", "Break-even receipts per year (after turnover tax)", "Break-even transactions/day (EBITDA = 0)",
            "Break-even transactions/day (EBIT = 0)", "Capture used (Y2)", "Accessible share used", "Non-highway transactions/day",
            "Break-even passing vehicles/day (two-way)", "Transactions/day for 4-year cash payback", "Passing vehicles/day for 4-year payback",
            "Modelled Year-2 transactions/day", "Safety margin vs EBITDA break-even"]
BER = {n: 4 + i for i, n in enumerate(BE_LINES)}
for n, rr in BER.items():
    be.cell(row=rr, column=1, value=n)
for j, s in enumerate(SCEN):
    L_ = COL(3 + j)
    R = SUMMARY_ROWS[s]["rows"]
    Y2 = lambda n: f"Annual!D{R[n]}"
    f = {}
    f["Year-2 net sales"] = f"={Y2('Net sales (excl. VAT)')}"
    f["Variable costs as % of net sales"] = (f"=({Y2('COGS + waste')}+{Y2('Card fees')}+{Y2('Repairs & maintenance')}+{Y2('Other variable')}+{Y2('Marketing')})/{Y2('Net sales (excl. VAT)')}"
                                             f"+{I_('utilities_variable_pct', s)}")
    f["Fixed costs per year (labour, rent, fixed, utilities fixed)"] = (f"={Y2('Labour')}+{Y2('Ground rent')}+{Y2('Other fixed + land tax')}+{Y2('Utilities')}"
                                                                        f"-{Y2('Net sales (excl. VAT)')}*{I_('utilities_variable_pct', s)}")
    f["Net ticket (excl. VAT)"] = f"={Y2('Average ticket (AMD incl. VAT)')}/(1+{I_('vat_rate', s)}*(1-{I_('tax_regime_tt', s)}))"
    f["Contribution per transaction"] = f"={L_}{BER['Net ticket (excl. VAT)']}*(1-{L_}{BER['Variable costs as % of net sales']})"
    Fx = f"{L_}{BER['Fixed costs per year (labour, rent, fixed, utilities fixed)']}"
    Vv = f"{L_}{BER['Variable costs as % of net sales']}"
    def R_for(target):
        # R solving after-tax EBITDA = target; TT: floor branch if it binds, else formula branch; VAT: (F+T)/(1-v)
        tr, td, tm, rm = I_('tt_rate', s), I_('tt_deduction_rate', s), I_('tt_min_rate', s), I_('repairs_maint_pct', s)
        Ra = f"(({Fx})+({target}))/(1-{Vv}-{tm})"
        Rb = f"((1-{td})*({Fx})+({target}))/(1-{Vv}-{tr}+{td}*({Vv}-{rm}))"
        floor_binds = f"({tr}*{Ra}-{td}*({Vv}*{Ra}+{Fx}-{rm}*{Ra})<={tm}*{Ra})"
        return f"IF({I_('tax_regime_tt', s)}=1,IF({floor_binds},{Ra},{Rb}),(({Fx})+({target}))/(1-{Vv}))"
    f["Break-even receipts per year (after turnover tax)"] = "=" + R_for("0")
    f["Break-even transactions/day (EBITDA = 0)"] = f"={L_}{BER['Break-even receipts per year (after turnover tax)']}/{L_}{BER['Net ticket (excl. VAT)']}/{I_('open_days_per_year', s)}"
    f["Break-even transactions/day (EBIT = 0)"] = "=" + R_for(Y2('Depreciation')) + f"/{L_}{BER['Net ticket (excl. VAT)']}/{I_('open_days_per_year', s)}"
    f["Capture used (Y2)"] = f"={I_('capture_rate', s)}*(1+{I_('capture_growth', s)})"
    f["Accessible share used"] = f"={I_('accessible_share', s)}"
    f["Non-highway transactions/day"] = f"={I_('other_transactions_day', s)}"
    f["Break-even passing vehicles/day (two-way)"] = (f"=MAX(0,{L_}{BER['Break-even transactions/day (EBITDA = 0)']}-{L_}{BER['Non-highway transactions/day']})"
                                                       f"/({L_}{BER['Accessible share used']}*{L_}{BER['Capture used (Y2)']})")
    tgt = f"{INVEST}/4/IF({I_('tax_regime_tt', s)}=1,1,(1-{I_('profit_tax_rate', s)}*0.6))"
    f["Transactions/day for 4-year cash payback"] = "=" + R_for(tgt) + f"/{L_}{BER['Net ticket (excl. VAT)']}/{I_('open_days_per_year', s)}"
    f["Passing vehicles/day for 4-year payback"] = (f"=MAX(0,{L_}{BER['Transactions/day for 4-year cash payback']}-{L_}{BER['Non-highway transactions/day']})"
                                                     f"/({L_}{BER['Accessible share used']}*{L_}{BER['Capture used (Y2)']})")
    f["Modelled Year-2 transactions/day"] = f"={Y2('Transactions / day (avg)')}"
    f["Safety margin vs EBITDA break-even"] = f"={L_}{BER['Modelled Year-2 transactions/day']}/{L_}{BER['Break-even transactions/day (EBITDA = 0)']}-1"
    for n, v in f.items():
        c = be.cell(row=BER[n], column=3 + j, value=v)
        c.number_format = PCT if ("%" in n or "Capture" in n or "share" in n or "margin" in n) else ('#,##0' if "AMD" not in n and ("day" in n or "vehicles" in n) else AMD)
# required traffic grid (base scenario)
g0 = BER[BE_LINES[-1]] + 3
be.cell(row=g0, column=1, value="Passing vehicles/day (two-way) needed for EBITDA break-even — BASE scenario cost structure & access/other tx").font = F_B
be.cell(row=g0 + 1, column=1, value="Rows: capture rate of accessible traffic · Columns: average ticket (AMD incl. VAT, Year-1 prices)")
caps = [0.008, 0.010, 0.012, 0.015, 0.018, 0.022, 0.026, 0.030, 0.035, 0.040]
ticks = [1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 4000]
be.cell(row=g0 + 2, column=2, value="capture \\ ticket").font = F_B
for j, t in enumerate(ticks):
    c = be.cell(row=g0 + 2, column=3 + j, value=t)
    c.font = F_IN
    c.number_format = '#,##0'
    be.column_dimensions[COL(3 + j)].width = 13
for i, cp in enumerate(caps):
    rr = g0 + 3 + i
    c = be.cell(row=rr, column=2, value=cp)
    c.font = F_IN
    c.number_format = PCT
    for j in range(len(ticks)):
        T = f"{COL(3 + j)}${g0 + 2}"
        CAP = f"$B{rr}"
        tnet = f"({T}*(1+{I_('price_inflation')})/(1+{I_('vat_rate')}*(1-{I_('tax_regime_tt')})))"
        tx = f"($E${BER['Break-even receipts per year (after turnover tax)']}/{tnet}/{I_('open_days_per_year')})"
        be.cell(row=rr, column=3 + j, value=f"=MAX(0,{tx}-{I_('other_transactions_day')})/({I_('accessible_share')}*{CAP})").number_format = '#,##0'
be.column_dimensions["B"].width = 16

# ======================================================================================
# Sensitivity (tornado from engine + two-way ticket x capture on Y3 EBITDA via formulas)
# ======================================================================================
se = wb.create_sheet("Sensitivity", 3)
se["A1"] = f"{NAME} — sensitivity of Year-3 EBITDA (base scenario)"
se["A1"].font = F_T
se["A2"] = "Tornado values are computed by model/engine.py (static, regenerate after changing inputs). Grid below is formula-driven."
header(se, 4, ["Driver (flexed)", "Low case EBITDA Y3", "High case EBITDA Y3", "Swing", "Base EBITDA Y3"], [40, 20, 20, 18, 18])
torn = engine.tornado(A, "base", A["concept"]["value"])
for i, t in enumerate(torn):
    rr = 5 + i
    se.cell(row=rr, column=1, value=t["label"])
    se.cell(row=rr, column=2, value=round(t["low"])).number_format = AMD
    se.cell(row=rr, column=3, value=round(t["high"])).number_format = AMD
    se.cell(row=rr, column=4, value=f"=ABS(C{rr}-B{rr})").number_format = AMD
    se.cell(row=rr, column=5, value=round(t["base"])).number_format = AMD
TOR_END = 5 + len(torn) - 1
ch = BarChart()
ch.type = "bar"
ch.title = "Year-3 EBITDA: low vs high case by driver"
ch.add_data(Reference(se, min_col=2, min_row=4, max_col=3, max_row=TOR_END), titles_from_data=True)
ch.set_categories(Reference(se, min_col=1, min_row=5, max_row=TOR_END))
ch.height, ch.width = 9, 18
se.add_chart(ch, "G4")

# ======================================================================================
# Cover
# ======================================================================================
cv = wb.create_sheet("Cover", 0)
cv["A1"] = f"{NAME} — highway drive-thru: 5-year financial model"
cv["A1"].font = Font(bold=True, size=20)
cv["A3"] = "Purpose: investment decision support for the first unit (recommended mid-range concept). All values AMD, nominal, excl. VAT unless stated."
cv["A4"] = "How to use: change blue cells on 'Inputs' (and 'Capex'); every other sheet recalculates. Concept switch: Inputs › concept_index."
cv["A5"] = "Evidence: every input carries a status tag and source; research files are in research/. Placeholders must be replaced by fieldwork (traffic counts, quotes)."
cv.column_dimensions["A"].width = 52
for j in range(3):
    cv.column_dimensions[COL(3 + j)].width = 18
header(cv, 7, ["Scenario summary", "", "Conservative", "Base", "Optimistic"])
summ = [("Total investment (AMD)", "Total investment (capex + pre-opening)", "k", AMD), ("Total investment (USD)", "Total investment (USD)", "k", '"$"#,##0'),
        ("Year-1 net sales", "Net sales (excl. VAT)", 1, AMD), ("Year-3 net sales", "Net sales (excl. VAT)", 3, AMD),
        ("Year-1 transactions/day", "Transactions / day (avg)", 1, '#,##0'), ("Year-3 transactions/day", "Transactions / day (avg)", 3, '#,##0'),
        ("Year-1 EBITDA", "EBITDA", 1, AMD), ("Year-3 EBITDA", "EBITDA", 3, AMD), ("Year-3 EBITDA margin", "EBITDA margin %", 3, PCT),
        ("Year-5 net income", "Net income", 5, AMD), ("Payback (months)", "Payback (months from opening)", "k", '0'),
        ("NPV (5 yrs + residual)", "NPV @ discount rate (5 yrs + residual)", "k", AMD), ("IRR (5 yrs + residual)", "IRR (5 yrs + residual)", "k", PCT),
        ("ROIC Year 3", "ROIC Year 3 (NOPAT / investment)", "k", PCT)]
for i, (lab, key, y, fmt) in enumerate(summ):
    rr = 8 + i
    cv.cell(row=rr, column=1, value=lab)
    for j, s in enumerate(SCEN):
        if y == "k":
            ref = f"=Annual!C{SUMMARY_ROWS[s]['krow'][key]}"
        else:
            ref = f"=Annual!{COL(2 + y)}{SUMMARY_ROWS[s]['rows'][key]}"
        c = cv.cell(row=rr, column=3 + j, value=ref)
        c.number_format = fmt
cv["A24"] = "Colour legend: blue = input · black = formula · cream fill = editable assumption."
cv["A25"] = "Prepared 2026-10 as part of the investor package. Not investment advice; validate inputs with fieldwork before committing capital."
# chart of base scenario annual net sales & EBITDA
Rb = SUMMARY_ROWS["base"]["rows"]
bc = BarChart()
bc.title = "Base scenario: net sales and EBITDA (AMD)"
bc.add_data(Reference(an, min_col=3, max_col=7, min_row=Rb["Net sales (excl. VAT)"]), from_rows=True, titles_from_data=False)
bc.add_data(Reference(an, min_col=3, max_col=7, min_row=Rb["EBITDA"]), from_rows=True, titles_from_data=False)
bc.height, bc.width = 8, 16
cv.add_chart(bc, "G7")

wb.save(OUT)
print("saved", OUT)
