"""
Builds model/assumptions.json — every model input with value(s), unit, status and source.

Status vocabulary (same as the research files):
  VERIFIED   primary/official source opened
  REPORTED   credible secondary source (news, listing, menu, supplier web price)
  ESTIMATE   derived calculation (formula in 'basis')
  ASSUMPTION analyst judgement (basis explained)
Scenario-dependent inputs carry {"conservative","base","optimistic"} values.
"""
import json
from pathlib import Path

OUT = Path(__file__).with_name("assumptions.json")


def S(c, b, o):
    return {"conservative": c, "base": b, "optimistic": o}


def I(value, unit, status, source, label=None, basis=""):
    return {"value": value, "unit": unit, "status": status, "source": source, "label": label or "", "basis": basis}


A = {}
# ---- general -------------------------------------------------------------------------
A["concept"] = I("mid", "", "ASSUMPTION", "Recommended concept", "Concept modelled")
A["fx_amd_per_usd"] = I(385.0, "AMD/USD", "ASSUMPTION", "PLACEHOLDER — replace with CBA rate", "Exchange rate")
A["opening_month"] = I(5, "month", "ASSUMPTION", "Open in May to catch first summer season", "Opening calendar month")
A["open_days_per_year"] = I(360, "days", "ASSUMPTION", "Closed ~5 days (New Year 1 Jan, Christmas 6 Jan, severe weather)", "Trading days per year")
A["vat_rate"] = I(0.20, "", "VERIFIED", "RA Tax Code art. 63", "VAT")
A["profit_tax_rate"] = I(0.18, "", "VERIFIED", "RA Tax Code art. 115", "Profit tax")
A["discount_rate"] = I(0.18, "", "ASSUMPTION", "AMD equity hurdle: CBA policy rate ~6.75% + SME/country/start-up premium", "Discount rate (AMD)")
# ---- demand ---------------------------------------------------------------------------
A["traffic_aadt"] = I(S(12000, 16000, 20000), "veh/day two-way", "ASSUMPTION", "PLACEHOLDER", "Passing traffic (AADT, two-way)")
A["traffic_growth"] = I(S(0.01, 0.025, 0.04), "/yr", "ASSUMPTION", "Motorisation trend", "Traffic growth")
A["accessible_share"] = I(S(0.50, 0.55, 0.60), "", "ASSUMPTION", "Right-in/right-out from one carriageway + some U-turn capture", "Share of traffic that can access")
A["capture_rate"] = I(S(0.012, 0.018, 0.025), "", "ASSUMPTION", "PLACEHOLDER", "Capture rate of accessible vehicles (Y1 steady state)")
A["capture_growth"] = I(S(0.03, 0.06, 0.10), "/yr", "ASSUMPTION", "Brand awareness build Y2-Y5", "Capture growth")
A["seasonality_index"] = I([0.66, 0.68, 0.80, 0.92, 1.02, 1.20, 1.42, 1.46, 1.14, 0.96, 0.82, 0.92], "index", "ESTIMATE",
                           "PLACEHOLDER", "Monthly traffic seasonality (mean = 1)")
A["ramp_curve"] = I(S([0.45, 0.55, 0.65, 0.72, 0.78, 0.83, 0.87, 0.90, 0.93, 0.95, 0.97, 0.98],
                      [0.55, 0.65, 0.74, 0.81, 0.86, 0.90, 0.93, 0.95, 0.97, 0.98, 0.99, 1.0],
                      [0.65, 0.75, 0.83, 0.89, 0.93, 0.96, 0.98, 1.0, 1.0, 1.0, 1.0, 1.0]), "", "ASSUMPTION",
                    "Typical new-unit ramp", "Opening ramp (capture multiplier, months 1-12)")
A["avg_ticket_amd"] = I(S(2200, 2600, 3000), "AMD incl. VAT", "ASSUMPTION", "PLACEHOLDER", "Average transaction value (per order)")
A["other_transactions_day"] = I(S(10, 20, 30), "tx/day", "ASSUMPTION", "Walk-in locals, staff of nearby businesses, pre-orders", "Non-highway transactions/day")
A["price_inflation"] = I(S(0.03, 0.035, 0.04), "/yr", "ASSUMPTION", "CBA inflation target 4% ±1.5", "Menu price growth")
A["cost_inflation"] = I(S(0.045, 0.04, 0.035), "/yr", "ASSUMPTION", "", "Non-labour cost inflation")
A["wage_growth"] = I(S(0.08, 0.07, 0.06), "/yr", "ASSUMPTION", "Nominal wage growth", "Wage growth")
# ---- costs ----------------------------------------------------------------------------
A["cogs_pct"] = I(S(0.33, 0.31, 0.29), "of net sales", "ESTIMATE", "PLACEHOLDER", "Food, beverage & packaging cost")
A["waste_pct"] = I(0.02, "of net sales", "ASSUMPTION", "Bakery shrink, spoilage", "Waste")
A["card_share"] = I(0.75, "of gross", "ASSUMPTION", "PLACEHOLDER", "Card/wallet share of payments")
A["card_fee_pct"] = I(0.018, "", "ASSUMPTION", "PLACEHOLDER", "Acquiring fee")
A["marketing_pct"] = I(0.03, "of net sales", "ASSUMPTION", "", "Ongoing marketing")
A["launch_marketing_amd"] = I(12_000_000, "AMD", "ASSUMPTION", "", "Launch marketing (months 1-3)")
A["repairs_maint_pct"] = I(0.015, "of net sales", "ASSUMPTION", "", "Repairs & maintenance")
A["other_variable_pct"] = I(0.01, "of net sales", "ASSUMPTION", "Cleaning chemicals, small wares, POS/app SaaS", "Other variable costs")
A["utilities_fixed_amd_month"] = I({"lean": 300_000, "mid": 480_000, "flagship": 700_000}, "AMD/month", "ESTIMATE", "PLACEHOLDER", "Utilities (fixed part)")
A["utilities_variable_pct"] = I(0.012, "of net sales", "ESTIMATE", "", "Utilities (variable part)")
A["fixed_other_amd_month"] = I(750_000, "AMD/month", "ASSUMPTION", "Insurance, accounting, security, waste, licences, IT, cleaning", "Other fixed costs")
A["land_mode"] = I("lease", "", "ASSUMPTION", "Ground lease preferred for capital efficiency", "Land: lease or buy")
A["rent_amd_month"] = I(S(1_800_000, 1_500_000, 1_300_000), "AMD/month", "ASSUMPTION", "PLACEHOLDER", "Ground lease")
A["land_property_tax_amd_year"] = I(600_000, "AMD/yr", "ESTIMATE", "PLACEHOLDER", "Land & property tax")
A["employer_oncost_pct"] = I(0.01, "of gross wages", "ASSUMPTION", "PLACEHOLDER", "Employer on-costs")
A["staff_meals_uniforms_amd_month"] = I(15_000, "AMD/FTE/month", "ASSUMPTION", "", "Staff meals & uniforms")
A["peak_season_threshold"] = I(1.15, "index", "ASSUMPTION", "Add seasonal staff when seasonality ≥ threshold", "Peak staffing threshold")
A["staffing"] = {
    "lean": {"fte_base": 6, "fte_peak_extra": 2, "avg_gross_wage_amd": 250_000, "manager_gross_amd": 450_000},
    "mid": {"fte_base": 10, "fte_peak_extra": 3, "avg_gross_wage_amd": 260_000, "manager_gross_amd": 600_000},
    "flagship": {"fte_base": 14, "fte_peak_extra": 4, "avg_gross_wage_amd": 270_000, "manager_gross_amd": 700_000},
}
A["depreciation_years"] = I({"building": 20, "site_works": 10, "equipment": 5, "technology": 3, "signage": 5, "soft": 5, "land": 0}, "years", "ASSUMPTION", "PLACEHOLDER", "Depreciation lives")
A["maintenance_capex_pct"] = I(0.01, "of net sales", "ASSUMPTION", "", "Maintenance capex (from Y2)")
A["working_capital_days"] = I(10, "days of COGS", "ASSUMPTION", "Inventory net of supplier credit", "Working capital")
A["pre_opening_costs_amd"] = I({"lean": 8_000_000, "mid": 14_000_000, "flagship": 20_000_000}, "AMD", "ASSUMPTION", "PLACEHOLDER", "Pre-opening (recruitment, training, trial ops)")


def item(name, amd, dep, status="ASSUMPTION", source="PLACEHOLDER"):
    return {"name": name, "amd": amd, "dep_class": dep, "status": status, "source": source}


A["capex"] = {
    "lean": [item("Modular building", 40_000_000, "building"), item("Site works", 30_000_000, "site_works"),
             item("Equipment", 25_000_000, "equipment"), item("Technology", 4_000_000, "technology"),
             item("Signage", 6_000_000, "signage"), item("Soft costs", 8_000_000, "soft"), item("Contingency", 10_000_000, "site_works")],
    "mid": [item("Building", 90_000_000, "building"), item("Site works", 55_000_000, "site_works"),
            item("Equipment", 40_000_000, "equipment"), item("Technology", 6_000_000, "technology"),
            item("Signage", 12_000_000, "signage"), item("Soft costs", 15_000_000, "soft"), item("Contingency", 20_000_000, "site_works")],
    "flagship": [item("Building", 150_000_000, "building"), item("Site works", 75_000_000, "site_works"),
                 item("Equipment", 55_000_000, "equipment"), item("Technology", 9_000_000, "technology"),
                 item("Signage", 18_000_000, "signage"), item("Soft costs", 22_000_000, "soft"), item("Contingency", 30_000_000, "site_works")],
}

if __name__ == "__main__":
    OUT.write_text(json.dumps(A, indent=1, ensure_ascii=False))
    print("wrote", OUT)
