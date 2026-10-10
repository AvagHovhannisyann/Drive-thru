# CHAMPA (ՃԱՄՓԱ): operations, launch and regulatory roadmap

*Workstream: operations and launch. Prepared 2026-10-10. Currency: AMD. USD at the CBA rate of 9 Oct 2026, **USD 1 = AMD 361.93** (C3[S23], C2[S1]). Scope: the first unit, the 171 m² mid-range prototype on a 3,256 m² M4 roadside plot (`design/layout.json`). Hours tested: the founder's brief of 07:00–23:00.*

**How to read this document**
- **Status tags** follow the research files:
  - **VERIFIED / REPORTED**: carried over from a research file. The file and its source number are given, e.g. "C5[7]" = `research/C5-regulations.md`, source 7 in its §6.
  - **ESTIMATE**: my own calculation. The formula is shown.
  - **ASSUMPTION**: my judgement. The basis is given.
- **Files used:** C5 (regulation), C3 (labour), C2 (equipment and supply), C6 (benchmarks), A4 (food), A5 (cultural fit) and C4 (tax), all read in full. None of these seven files has a section-7 fact-check log, so their values are used as published. Where a value was corrected in another file's fact-check (A1), I say so.
- **Other inputs:** the design geometry (`design/layout.json`) and the current model inputs (`model/assumptions.json`, many still marked PLACEHOLDER).
- **Not legal advice.** The permitting steps rest on C5's reading of Armenian statute. Section 15 lists the points that need written confirmation from an agency.
- **Month numbering:** **M1 = November 2026.** So M13 = Nov 2027 and M19 = May 2028.

---

## 1. Executive summary

1. **Labour, not equipment or rent, is what decides whether this unit works. At realistic M4 volumes it does not yet work.**
   - **Founder's brief** (07:00–23:00 all year, full prototype roster with 3 people on the floor at all times):
     - 14.1 FTE;
     - payroll **AMD 4.55m/month** (USD 12.6k);
     - **AMD 5.2m/month** including staff transport and meals (ESTIMATE, §4.5).
   - **Recommended roster** (a "minimum viable" roster with seasonal hours):
     - 11.6 FTE;
     - payroll **AMD 3.73m/month**;
     - **AMD 4.36m** all-in.
   - **What volume is needed:** to keep labour at or below 35% of receipts, the recommended roster needs **≈160–245 transactions/day** at an AMD 1,700–2,600 ticket.
   - **What volume is expected:** C6's benchmark-based base case for an M4 site is **≈110/day**. At that volume, labour is **51–78% of receipts**.
   - **Conclusion:** staffing has to flex with demand (part-time peak crew, seasonal hours). Even so, the volume gap stays the first thing the investment case must close.
2. **Service standard.**
   - **Benchmarks** (C6[16][17]; Black Rock ~90 s order-to-handoff, C6[5]):
     - US 2026 drive-thru average: 5:24 total visit, 4:04 service time, 1:40 at the window;
     - order accuracy 89.3%;
     - satisfaction falls to 84.9% once a visit passes 10 minutes.
   - **CHAMPA targets** (ASSUMPTION built on those benchmarks):
     - ≤45 s at the pickup window at peak;
     - ≤90 s order-to-handoff for drinks;
     - ≤3:30 from order point to exit;
     - ≥96% accuracy;
     - <2% of visits over 10 minutes.
3. **The 12.5-car stack is enough only if the windows clear 80–90 cars/hour at summer-weekend peaks.**
   - On C6's M/M/1 queue method, 48 arrivals/hour need 13 stack places at 60 cars/h capacity, but only 5 at 80/h.
   - 66 arrivals/hour need 15 places at 80/h and 9 at 90/h.
   - So orders must be fired to the bar at the order point or from the runner's tablet, not at payment. A written queue-overflow protocol must also keep cars off the deceleration lane (§5).
4. **Supply chain.**
   - **Coffee:** a local roaster on a 12-month contract with weekly delivery. Roasted-coffee imports pay 8% duty against 0% on green (C2[S6]).
   - **Dairy:** 3× a week, with a 1–2-day UHT buffer.
   - **Pastry:** frozen bake-off delivered weekly, dual-sourced (EAEU frozen + a Yerevan contract bakery) because of Russia supply-route risk (A5[14][15]).
   - **Packaging:** Oval Pack, with 4–6 weeks of stock. Only two cup SKUs are custom-printed, because the minimum order is 5,000 per SKU (C2[S43]).
   - Retail bean bags or merchandise are **not** sold inside the operating company: under catering turnover tax that income is taxed at 20% of turnover (C4[1] Art. 258).
5. **Technology is gated by fiscal compliance.**
   - Every payment point (window W1, café counter, each runner handheld, the app) needs a registered HDM (fiscal cash register) or a lawful e-HDM (electronic HDM).
   - Fines are AMD 500,000 for a missing HDM, and AMD 200,000 + 0.5% of the previous quarter's HDM turnover for each rule breach (C4[1] Art. 416). e-HDM rules start on 1 Jan 2027 (C4[6]).
   - **No POS vendor is selected without a live Armenian HDM/e-HDM demonstration** (C2 §4.9).
   - The CBA card-fee cap does not cover restaurant merchant category codes (C2[S24]), so plan on FastBank's list rates of 1.2% (local cards) and 2.2% (foreign), blended ≈1.35–1.6% (C2 §3.2.4).
6. **Regulatory critical path for the greenfield M4 plot.** The steps run:
   1. road-owner (MTAI) and Police agreement on access;
   2. land-designation change;
   3. **EIA Category B**;
   4. construction permit;
   5. build.

   C5 gives **12–20 months from land control to opening**, plus 6–9 months of contingency (C5 §3.10, §4.5). Plan dates:
   - M1: validation starts (Nov 2026);
   - M4: land option, conditional on access and zoning comfort letters;
   - M13: permit;
   - M13.5–M18.5: build;
   - M19: **soft launch** (May 2028, matching the model's May opening);
   - M20: grand opening (June 2028).
7. **The prototype as drawn has three permitting problems. Please send them to the design team now.**
   - **(a) Speed-change lanes are too short.** The layout shows 86 m (decel) and 121 m (accel) including tapers. The Armenian norm ՀՀՇՆ 32-01-2022 requires 90–110 m + 80 m taper (decel) and 140–230 m + 80 m taper (accel) (C5[5]).
   - **(b) Hard surface is about 1,870 m² excluding the building** (ESTIMATE from `layout.json`). That is above the 1,000 m² trigger for EIA Category B (C5[26]). Permeable parking, aisle and plaza would bring it to ≈970 m², marginally below.
   - **(c) The 8 m roadside pylon** may be treated as advertising. If so, it needs an MTAI permit and pays road tax of AMD 10,000/m²/yr, and the rule requiring ≥150 m from junctions could block it at the site's own entrance (C5[2]).
8. **Rules that shape day-to-day operation** (C5[10][11][16][17]):
   - **HACCP:** from 1 Jan 2027 an approved HACCP plan becomes part of food-safety (FSIB) registration, and registration must happen before trading.
   - **Medical books:** staff are examined on hiring and every 6 months.
   - **Menu boards:** they must show portion mass and final price.
   - **Cooks:** need vocational qualification evidence.
   - **Signage, menus and ads:** Armenian first (C5[20][21]).
9. **Marketing.**
   - **Lead with the Armenian ritual and speed, not "American".** Every handoff ends with *«Ճամփադ բաց»*.
   - **Maps:** Yandex, Google and 2GIS listings, plus an OpenStreetMap `drive_through=yes` tag. Armenia currently has zero tagged drive-thrus (A5[32]).
   - **Delivery apps:** no Glovo or Yandex Eats at a highway site.
   - **Roadside boards:** ≤27 m² each, MTAI permit, road tax.
   - **Partnerships:** Tsaghkadzor and Sevan hotels, employers' shuttle buses, and ride-hail drivers. Use fuel retailers only for cross-promotion; co-locating in unit 1 risks risk category IV and an EIA.
10. **Validate before buying land.**
    - **Months 1–3:** winter traffic counts, a five-day observation of Coffee House's M4 drive-thru, an intercept survey (n ≥ 600) and mystery shopping.
    - **Gate 0 (end of M3)** decides whether to proceed on the open M4 or switch to an interchange or urban-edge site. The switch saves ≈6–8 months of permitting (C5 §3.10 Scenario A, 8–11 months) and has better odds: A5 rates a standalone open-highway unit at ≈25–35% and an arterial hybrid at ≈50–60%.

---

## 2. Operating model at a glance

| Element | Specification for unit 1 | Basis |
|---|---|---|
| Format | Drive-thru-led hybrid: 2 order lanes (OP-A, OP-B) merging to one window lane; W1 = order confirm/payment, W2 = pickup; walk-up café counter with 12 seats; 2 accessible restrooms; terrace 62 m²; 25 parking stalls | `design/layout.json`; A5 §4.3 (walk-up and parking "not optional") |
| Stack | 12.5 cars from the pickup window; 5.5 behind the order points | `layout.json` circulation.capacity |
| Hours | 07:00–23:00 in summer; shorter hours in the shoulder seasons and winter (§3) | Founder brief; C3 §3.6 (night premium after 22:00) |
| Peak capacity target | ≥60 cars/h at launch; 80–90 cars/h on summer weekends | C6 §3.4–3.5; §5.3 below |
| Menu | Coffee plus Armenian hand-helds: 10–14 food SKUs, hot savoury hero item (breakfast lavash wrap), bake-off croissant, gata, zhingyalov hats; sweet iced drinks and batch lemonades | A4 §3.12; C2 §3.4 |
| Bar | 3-group espresso machine (drive-thru line) + 2-group (café and back-up); 2 grinders; ice machine; 2 blenders; cold-brew taps; batch brewer | `layout.json` building.equipment; C2 §3.1.3 |
| Food | 2 high-speed ovens + food finish; reach-in freezer; walk-in cooler 2.4 × 2.0 m | `layout.json`; C2 §3.1.4 |
| People | 11.6 FTE (recommended roster) incl. store manager and cleaner/porter; 3–7 on the floor depending on cars/hour | §4 |
| Tax regime | Catering turnover tax (12% of receipts − 9% of documented expenses, floor 3.5%) | C4[1] Art. 254, 258; model `tax_regime` |
| Suppliers | Local roaster; Marianna/Dili/Yeremyan-type dairy; EAEU frozen croissants + Yerevan bakery; Oval Pack; Alpha Food Service (Monin) | C2 §3.3; A4 §3.7 |

---

## 3. Opening hours and seasonal adjustments

**Evidence.**
- **Incumbent.** The Coffee House M4 drive-thru lists 08:30–24:00 on its site (A5 §3.3.4, citing A2/A3). A2's fact-check found Yandex showing "until 23:00" on 10 Oct 2026, so its hours may be seasonal.
- **Georgia.** Drive-thrus typically run 08:00–24:00, and 3 of them are 24/7 (A5[32]).
- **Demand shape (US data).** Coffee demand is concentrated in the morning. In ITE land use 937 the AM peak hour carries 14.2% of daily trips, against a PM peak of 6.5%. Land use 938 shows 22.2% against 8.4% (C6[20]).
- **Cost after 22:00.** Hours from 22:00 carry a ≥30% night premium (C3[S1] Art. 148, 184). A 23:00 close means a 23:30 staff exit, which needs employer transport (C3 §3.7).
- **Seasonality.** The model's monthly index runs from **0.66 in January to 1.46 in August** (`model/assumptions.json` seasonality_index, ESTIMATE/PLACEHOLDER pending B1 counts).

**Recommended hours** (ASSUMPTION: protect the morning and summer peaks and trim low-yield evening hours):

| Season (model index) | Sun–Thu | Fri–Sat | Café counter / seating | Notes |
|---|---|---|---|---|
| Summer, Jun–Aug (1.20–1.46) | 07:00–23:00 | 07:00–23:00 (test to 24:00) | 07:30–22:00 | Leisure peaks on Fri afternoon and Sat/Sun late morning to midday (A5 §3.3.4) |
| Shoulder, Apr–May and Sep–Oct (0.92–1.14) | 07:00–22:00 | 07:00–23:00 | 07:30–21:00 | Commuter AM peak 07:00–10:00 |
| Winter, Nov–Mar (0.66–0.92) | 07:00–21:00 | 07:00–22:00 | 08:00–20:00 | Drive-thru only after the café closes; snow protocol |

- **Never trade past 24:00.** That avoids the community night-operation permit (AMD 25,000–100,000/yr; C5[18] Art. 11). More importantly, it keeps the 11-hour rest rule workable for a two-team roster (C3[S1] Art. 154).
- **Public holidays.** Open on 11 of the 13 non-working holidays at **2× pay** (C3[S4], Art. 185). Close on 1 January and 6 January. Together with a few severe-weather days, that gives the model's 360 trading days (`open_days_per_year`).
- **Severe weather.** Sevan averages a January high of −2.8 °C and low of −13.0 °C (A5[27]). Close only when the Road Police close the M4. Otherwise run with a heated canopy and windows (C6 §3.10) and a snow-clearing contract (§13.4).
- **Review point:** decide on extended summer evenings (to 24:00) at the 90-day review (M22), using hourly POS data.

---

## 4. Staffing model and shift plan

### 4.1 Roles, grades and pay (C3 base wages, 2026 rules, job ads read as net)

| Role | What the role does | Grade and gross pay = employer cost (C3 §3.8) | Legal or design note |
|---|---|---|---|
| Store manager (1) | P&L, roster, suppliers, HACCP owner, community and FSIB contact; works the peak days | AMD 552,571/month (net 400k) | 5-day week |
| Shift lead (1 per shift, on the floor) | Runs W1 (order confirm, payment, headset) at low volume and expedites at W2 at peak; cash/HDM, safety, ritual quality | AMD 354,400 (net 260k) | **Recruit leads with cook qualification** so they can legally cover evening food (Law on Trade and Services Art. 12(6), C5[17]) |
| Barista (bar line) | Espresso, milk, cold station; owns the 3-group machine | AMD 247,733 (net 180k) | Baristas and cashiers are not in Art. 12(6) (C5 §4.8) |
| Food/bake-off (cook grade) | Bakes to the sales curve, griddles wraps, finishes food at the W2 shelf | AMD 327,733 (net 240k) | Vocational diploma, certificate or ≥1 year of work-based learning required (C5[17] Art. 12(6)) |
| Runner with tablet (peak) | Takes orders and payments in the stack on a handheld HDM-POS; queue care; delivers to pull-forward bays and café tables | Crew grade; part-time | Students aged 18+ (under-18s cannot work after 22:00, do overtime or sell energy drinks; C3[S1] Art. 148, 257) |
| Window presenter / café host (summer peaks) | Owns the W2 handoff and the *«Ճամփադ բաց»* ritual; café counter, restrooms, terrace | Crew grade; part-time | — |
| Cleaner/porter (1 FTE, 6-day week) | Restrooms, lot, terrace, bins, snow | AMD 188,000 (net 140k) | Public toilets at roadside service objects can be required by the planning assignment (APA) (C5[3] GD 2404-N §5(է)) |

**Pay design.**
- Keep full-time gross pay **out of the AMD 195–207k band**. Health-insurance rules create a notch there (C3 §3.5). All base grades above sit above it.
- Part-timers paid ≤AMD 200k gross trigger the **draft AMD 4,400/month employer levy from the December 2026 payroll**, if it is adopted (C3[S7]).
- Add a **per-shift speed and accuracy bonus**, as local cafés already pay % of sales (C3 §3.3, ads P3, P4, P6).

### 4.2 Deployment chart: who is on the floor at each volume

Capacity per configuration comes from C6 §3.4:
- speaker ordering and one window: 36–45 cars/h;
- runners with tablets: 60–80 cars/h;
- dual lanes + runners: 70–90 cars/h.

Bar capacity: a 2-group machine with two baristas sustains ≈60–90 milk drinks/h, and more than ≈100 drinks/h needs a 3-group or two machines (C2 §3.1.3, ASSUMPTION there).

| Cars per hour in the lane | Staff on floor | Positions (ASSUMPTION) |
|---|---|---|
| < 10 (late evening, winter) | 2 | Lead (W1, headset, W2) + barista/food |
| 10–20 | 3 | Lead (W1 + headset), barista, food/W2 |
| 20–35 | 4 | + runner with tablet in the stack; lead moves to expo/W2 |
| 35–50 | 5 | + barista 2 (cold/blended and café 2-group); open lane B |
| 50–70 | 6 | + runner 2 (second tablet, pull-forward delivery) |
| > 70 | 7 | + window presenter/café host |

**Expected peak loads** (ESTIMATE = daily transactions × AM-peak share of 14.2–22.2%, C6[20]; the summer-weekend factor of 2× is B1's ASSUMPTION as cited in C6 §3.4):

| Daily transactions | Weekday peak hour | Summer weekend peak hour (2×) |
|---|---|---|
| 110/day (C6 recommended M4 base) | 16–24 cars/h → 3–4 staff | 31–49 cars/h → 4–5 staff |
| 150/day (A2 top of range, as used by C6) | 21–33 cars/h → 4 staff | 43–67 cars/h → 5–6 staff |

### 4.3 Shift templates (recommended roster, "Case B")

Both main shifts are **8 paid hours with a staggered 30-minute unpaid break taken within the first 4 hours** (C3[S1] Art. 152).

| Team | Summer (07:00–23:00) | Shoulder (Sun–Thu to 22:00) | Winter (Sun–Thu to 21:00) |
|---|---|---|---|
| **Open team**: lead A, barista A | 06:30–15:00 | 06:30–14:30 (Fri–Sat to 15:00) | 06:30–14:00 (Fri–Sat to 14:30) |
| **Cook A** (food/bake-off) | 06:30–15:00 | 06:30–15:00 | 06:30–15:00 |
| **Close team**: lead B, barista B | 15:00–23:30 | 14:30–22:30 (Fri–Sat 15:00–23:30) | 14:00–21:30 (Fri–Sat 14:30–22:30) |
| Weekday peak helpers | Runner 07:00–11:00 and 16:00–20:00; barista 2 07:00–09:00 and 17:00–19:00 | Runner 07:00–10:00 | Runner 07:00–10:00 |
| Weekend peak helpers | Runner 10:00–20:00; barista 2 10:00–20:00; runner 2 11:00–19:00; cook 2 12:00–20:00 | Runner 10:00–18:00; barista 2 11:00–17:00; cook 2 12:00–18:00 | Runner 10:00–16:00 |

**Evening food.**
- After 15:00 on weekdays the hot menu narrows to bake-off items and pre-assembled wraps, finished by the cook-qualified lead.
- If legal counsel or FSIB confirms that reheating and assembly is not "cook" work under Art. 12(6), the lead no longer needs the qualification and recruitment gets easier (§15).

**Seasonal hours and contracts.** The costing in §4.5 assumes paid hours follow rostered hours across the seasons. There are two ways to achieve that:
- (a) Put the seasonal peak on **part-time and seasonal contracts**.
- (b) Use **summarised working-time accounting** with a reference period of up to 6 months (C3[S1] Art. 143). Longer summer weeks are then balanced against shorter autumn and winter weeks, for example on a Jul–Dec reference period. Counsel should confirm the design.

If full-time staff have to be paid 40 h/week regardless, the winter savings disappear and Case B costs about what Case C costs (≈AMD 4.5m all-in).

### 4.4 Labour-law rules built into the roster (C3[S1], VERIFIED)

- **Hours and rest:** 40 h/week and 8 h/day; 12 h/day maximum including overtime; **≥11 h between shifts**, so no close (23:30) followed by an open (06:30); **35 h continuous weekly rest**, with the 2 rest days consecutive in continuous operations (Art. 139, 154–155).
  - The roster keeps fixed open and close teams for each week, rotating weekly.
- **Overtime:** only exceptionally; ≤4 h in 2 days and ≤180 h/yr. It is **not** a staffing tool (Art. 144–146).
- **Premiums:** night (22:00–06:00) ≥+30%; holidays ≥2×.
- **Leave and probation:** 20 working days of leave on a 5-day week; probation ≤3 months (Art. 91–93, 159).
- **Under-18s:** effectively excluded (Art. 140, 148, 257).
- **Paperwork:**
  - **Medical (sanitary) books** before the first shift and every 6 months; the FSIB can bar staff without one (C5[16]).
  - **Photo name badges and uniforms** (C5[17] Art. 12(4)–(5)).
  - **From 1 July 2027**, employment contracts go through the state digital contract system (C3 §3.4, Art. 102.1; C3's inference, to be verified).

### 4.5 FTE and payroll: three cases (ESTIMATE)

**Method** (C3 §3.8 logic):
- Position-hours = on-site hours per position. This is conservative, because unpaid 30-minute breaks are not deducted.
- FTE = annual position-hours ÷ 1,880 productive hours per FTE.
- Cost = FTE × gross by grade × (1 + 30% × night-hour share + 13/365 holiday share).
- Store manager and cleaner are added at 1.0 FTE each.
- Transport = AMD 0.45m/month, the midpoint of C3's ASSUMPTION of 0.3–0.6m. Meals and uniforms = AMD 15,000/FTE/month (C3; model input).
- The calculation script is in the session scratchpad (`roster2.py`).

| Case | Hours | Position-hours/day (avg) | FTE (shift + manager + cleaner) | Payroll, AMD/month (USD) | + transport, meals | **All-in AMD/month** | All-in AMD/yr |
|---|---|---|---|---|---|---|---|
| **A. Founder brief, full prototype roster** (3 on the floor all hours + peak helpers + café host) | 07:00–23:00 all year | 62.1 | 12.1 + 2 = **14.1** | 4.55m ($12.6k) | 0.66m | **5.21m** | 62.6m |
| **B. Recommended: minimum viable roster + seasonal hours** (2 core all hours, cook on the open shift and weekend peaks, helpers at peaks) | §3 table | 49.6 | 9.6 + 2 = **11.6** | 3.73m ($10.3k) | 0.62m | **4.36m** | 52.3m |
| C. Minimum viable roster at 07:00–23:00 all year | 07:00–23:00 | 51.5 | 10.0 + 2 = 12.0 | 3.88m ($10.7k) | 0.63m | 4.51m | 54.1m |

- **Cross-check:** C3's own grid gives AMD 4.12m for 07:00–22:00 with 4 per shift, and 4.65m for 06:00–23:00 with 4 per shift. Cases A–C fall inside that envelope.
- **Gross-versus-net risk.** If hospitality job ads turn out to quote **gross** pay, payroll falls about 27%, to **AMD 2.73m** in Case B (C3 §3.9). That is the largest single uncertainty, and five phone calls to employers can resolve it (C3 §5).
- **Upward drift:** 2027 health-insurance rules add +2–3%; wages grow 7–8% a year (C3 §3.9, §4.8).
- **The hours cut matters less than the roster.** Case B saves only ≈AMD 0.15m/month compared with Case C. The large saving, ≈AMD 0.85m/month against Case A, comes from not keeping a cook and a third person on the floor in the off-peak.

### 4.6 Labour-economics test (red flag)

All-in labour as a share of receipts = annual labour ÷ (transactions/day × ticket × 360 days). Under catering turnover tax the company keeps the full customer-paid amount (C4 §3.11). ESTIMATE:

| Ticket (AMD) | Case B labour share at 83 tx/day | at 110 tx/day | at 150 tx/day | **tx/day for ≤35%** | tx/day for ≤30% |
|---|---|---|---|---|---|
| 1,700 (A4 base with food attach ≈1,540–1,860) | 103% | 78% | 57% | **244** | 285 |
| 2,000 | 88% | 66% | 48% | **208** | 242 |
| 2,600 (model base ticket) | 67% | 51% | 37% | **160** | 186 |

**Benchmarks:**
- US labour runs 21.0–26.9% of sales (C6[1][5]).
- C6 recommends 22–32% for Armenia.
- C6's realistic M4 base is ≈110 tx/day: 0.6% capture × 27,000 AADT × 0.55, plus 20 walk-ins (C6 §4.1).
- 83 tx/day is C6's result for 0.75% capture of B1's ≈11,000 same-side light vehicles.
- Case B costs **AMD ≈9,500 per trading hour**. For every AMD 1,000 of average ticket, the unit needs ≈9.5 orders every trading hour just to pay its people (compare C3 §4.2).

**Operational responses, in order of impact** (ASSUMPTION):
1. Start on the Case B roster with part-time peak crew, and add the full Case A roster only once 4 consecutive weeks average ≥200 tx/day.
2. Settle the gross-versus-net question before the budget is fixed.
3. Cross-train every crew member on bar, W2 and bake-off, so that two people can safely run the unit below 10 cars/h.
4. Lift the ticket through food attach and combos (A4 §3.11: a coffee + pastry combo at 1,900–2,600) rather than through headline drink prices.
5. If Gate 0 field counts point to <120 tx/day, **change the site or format**, not the roster. Options are an interchange or urban-edge site, or a smaller kiosk without a café (C6 §3.5 lean kiosk 45–65 m²).

### 4.7 Recruitment, training, retention and transport

- **Labour pool.**
  - On 10 Oct 2026 job.am listed 1,039 Yerevan jobs against 34 in Abovyan, 1 in Hrazdan and 2 in Sevan (C3[S24]).
  - A site near Abovyan (≈km 16) can draw on Abovyan (51.5k people) and north-east Yerevan (C3[S22], §4.6).
  - Competing local pay is AMD 200–300k at factories, and the M4 roadside restaurant at Verin Ptghni advertises a cleaner from AMD 300k (C3 P21). **Score candidate sites on labour access as well as traffic.**
- **Hiring channels:**
  - job.am at AMD 21,900 per post or 59,900 for 3 (C3[S25]);
  - staff.am;
  - colleges in Abovyan and Yerevan for 18+ part-timers;
  - a referral bonus (ASSUMPTION).
- **Turnover.** Plan for 60–100% annual crew turnover (C3 ASSUMPTION) at ≈AMD 79k per hire (ad + 40 paid training hours; C3 §3.9). That is 7–11 hires a year in Case B (ESTIMATE: 11.6 FTE × 60–100%, excluding the manager).
- **Training academy** (ASSUMPTION):
  - **Pre-opening:** 3–4 weeks for the opening team, including ≥40 paid hours per crew member (C3), with dry runs in the finished building.
  - **Curriculum:** HACCP basics and the hygiene plan; recipe cards and espresso calibration; the order-confirm, merge and sequence discipline; HDM/e-HDM handling; the ritual and service recovery; queue-overflow drills; first-line maintenance of the espresso machine, grinders and ice machine (C2 §4.4).
  - **Certification:** each position signed off before solo shifts. Leads must also hold the cook qualification and complete a HACCP course.
- **Pre-opening payroll** (ESTIMATE ≈AMD 5.7m):

  | Item | Calculation | AMD |
  |---|---|---|
  | Manager | 4 months × 552,571 | 2.21m |
  | Leads | 3 × 1.5 months × 354,400 | 1.59m |
  | Full-time crew and cooks | 6 × 1 month × ≈270k | 1.62m |
  | Part-timers | 4 × 40 h × AMD 1,429 | 0.23m |
  | Cleaner | 0.5 month | 0.09m |

  Recruitment ads ≈AMD 0.2m and medical exams (price not found, C5 §5) come on top. This fits inside the model's AMD 14M mid-range pre-opening placeholder.
- **Transport.** A contracted minibus around 06:00 and 23:30 from Abovyan and north-east Yerevan (C3 §3.7 ASSUMPTION: AMD 0.3–0.6m/month). Late-shift rides are a standard benefit locally (C3 P7, P24).

---

## 5. Service-speed standards

### 5.1 Benchmarks (C6)

| Benchmark | Value | Source |
|---|---|---|
| US drive-thru average 2026: total visit / service time (order → exit) / window time | 5:24 / 4:04 / 1:40; median under 4:25; slowest 10% at 9:56 or more | C6[16][17] (Intouch Insight, 2,145 visits) |
| Fastest brand 2026 | Tim Hortons 4:20 | C6[17] |
| Order accuracy | 89.3% overall; Starbucks 96%, Dutch Bros 94%; 43% of errors are customisation errors | C6[17] |
| Satisfaction cliff | 84.9% once a visit passes 10 min; 42.9% when the lane "felt frustrating" | C6[17] |
| Friendly service | Friendly visits 25 s faster (2026); accuracy 89% friendly vs 70% unfriendly (2025) | C6[17][18] |
| Order-to-handoff target | Black Rock ~90 s | C6[5] |
| Recommended Armenian mid-range unit | Window ≤60 s → ≥60 cars/h; order-to-handoff ≤3 min. Flagship ≤45–50 s → 70–80 cars/h | C6 §3.5 |
| Local failure mode | Coffee House M4: 20–60-minute waits and order errors in Jun–Sep 2026 reviews | A5 #27 (A3) |

### 5.2 CHAMPA targets (ASSUMPTION built on §5.1)

| Metric (measured by POS and lane timers) | Soft launch (M19–M21) | Steady state (from M22) |
|---|---|---|
| Window time at W2, peak hour | ≤60 s | **≤45 s** |
| Window time at W1 (confirm and pay) | ≤45 s | ≤35 s |
| Order-to-handoff, drinks only | ≤150 s | **≤90 s** |
| Order-to-handoff, with hot food | ≤180 s | ≤150 s (otherwise pull forward) |
| Service time, order point → exit | ≤4:30 | **≤3:30** (beats the 4:04 US average) |
| Total time, queue entry → exit: median / 90th percentile | ≤6:00 / ≤10:00 | ≤4:30 / ≤8:00 |
| Visits over 10 minutes | <5% | **<2%** |
| Order accuracy (mystery shop + complaints) | ≥93% | **≥96%** |
| Peak capacity (cars/h through W2) | ≥60 | 70 (weekday) / 80–90 (summer weekend) |
| Walk-up/café order-to-handoff | ≤3:00 | ≤2:00 |

### 5.3 Stack check: does the 12.5-car stack hold at peak? (ESTIMATE, C6 §3.4 M/M/1 method)

Places needed = ⌈ln 0.05 ÷ ln ρ⌉ − 1, where ρ = arrival rate ÷ service rate. This reproduces C6's figures, e.g. 45 arrivals/60 capacity → 10 places. Time in system = 60 ÷ (capacity − arrivals) minutes.

| Arrivals (cars/h) | Window capacity 45/h | 60/h | 80/h | 90/h |
|---|---|---|---|---|
| 31 (110 tx/day, summer weekend, low share) | 8 places, 4.3 min | 4, 2.1 min | 3, 1.2 min | 2, 1.0 min |
| 48 (110 tx/day, summer weekend, high share) | overload | **13, 5.0 min** | 5, 1.9 min | 4, 1.4 min |
| 66 (150 tx/day, summer weekend, high share) | overload | overload | **15, 4.3 min** | 9, 2.5 min |

**Reading.**
- A speaker-and-one-window lane (36–45 cars/h) **will** recreate the incumbent's failure on summer weekends.
- At 60 cars/h, 48 arrivals already overflow the 12.5-car stack.
- To hold every C6 scenario inside the plot, the unit needs **≈80–90 cars/h at W2, i.e. 40–45 s per car**. That is possible only if:
  1. the drink is fired to the bar when the order is taken, at the speaker or the runner's tablet, roughly 6 cars upstream of W2 (§6.1);
  2. payment is finished at W1 or on the tablet;
  3. hot-food orders taking longer than 45 s are pulled forward.
- Coffee demand comes in bursts, so treat these figures as minimums (C6 caveat).

### 5.4 Queue-overflow protocol (ASSUMPTION; no spill-back onto the road)

The law prohibits selling on the carriageway or shoulders, and entering or leaving the road at undesignated points (Law on Highways Art. 10(6), C5[1]). C6 §3.5 adds that the queue must never back into the deceleration lane.

| Trigger (camera or loop detector on the stack) | Action |
|---|---|
| Car 8 in the stack | Runner 1 deploys with a tablet into the double stack; lane B opens |
| Car 10 | Runner 2 deploys. Hot-food orders go to the 2 designated **pull-forward bays** nearest the exit. The lead calls in the on-call part-timer (paid call-in, ASSUMPTION) |
| Car 12 (end of plot stack) | The entrance marshal (porter or runner) directs new arrivals to park; orders are taken by tablet in the lot and delivered to the car or the counter. **The lane entry is closed with a sign before any car waits on the deceleration lane** |
| Any wait over 10 min | Service recovery: next-visit drink token via the app or a printed card (§10) |

---

## 6. Production-line layout logic

### 6.1 Car flow and ticket timing (from `design/layout.json`)

- **Route:** order points OP-A and OP-B (digital menu board + speaker) → 12.9 m merge → window lane (35.8 m) → **W1 (confirm and payment)** → **W2 (pickup)**, 8.2 m further on → exit loop past the parking aisle.
- **Distance:** from either order point to W2 is ≈38.5 m, about 6.4 car lengths at the layout's 6.0 m pitch (ESTIMATE from the geometry).
- **Firing time.** If orders fire at the speaker, the bar has 6 cars × 40–45 s = 4–4.5 minutes of lead time when the stack is full, and only the drive time (≈30–60 s, ASSUMPTION) when the lane is empty. So:
  - at full stack, the risk is **sequence errors**;
  - in a half-empty lane, the risk is **bar speed**.
- **The merge is where errors happen.** Two lanes zip into one, so the order sequence can flip.
  - The POS must re-sequence at W1. The order-confirm screen shows the order total plus a car descriptor (colour, type) entered by the order-taker.
  - The W1 operator confirms the sequence on the KDS before the drink reaches W2.
  - Customisation causes 43% of US errors (C6[17]). A **customer-facing order-confirm screen at each order point** is non-negotiable. The layout currently shows one only at W1.

### 6.2 Station map (east → west, following the car)

| Zone (inside the bar wall) | Equipment (`layout.json`) | Who | Logic |
|---|---|---|---|
| Opposite W1 | POS + order-confirm screen; headset base | Lead | Takes payment, confirms sequence, re-fires corrections |
| Espresso line | 3-group machine; 2 grinders + knock box | Barista 1 | Shots fire from the KDS as soon as the order is placed |
| Milk and finishing | Under-counter fridges ×4 (milk/cream); syrup rail; cup dispensers | Barista 1/2 | Shortest move from fridge to steam wand to lid |
| Cold station | Ice machine + bin; 2 blenders; cold-brew taps | Barista 2 | Sits beside W2, so iced drinks finish last and leave cold |
| Food | 2 high-speed ovens + food finish; reach-in freezer and fridge | Cook | Bakes to a 30–60 min sales curve; wraps griddled 60–90 s (A4 §3.12) |
| W2 handoff shelf | Bump screen; bag and carrier station | Presenter or lead | One shelf per car; bag check; ritual |
| Café counter | 2-group machine (back-up line); pastry case; café POS; pickup plane | Barista 2 or host | Walk-up flow kept separate from the lane; doubles as **redundancy if the 3-group fails** |
| Back of house | Walk-in cooler 2.4 × 2.0 m; dry store; dishwasher; 3-compartment sink; 2 hand-wash sinks; staff room with lockers | All | FSIB checklist: separate hand-wash sinks at the window and the prep line; staff changing room (C5[14]) |

### 6.3 Changes the operations team asks of the design team

1. **Order-confirm screens at OP-A and OP-B**, not only at W1. (§6.1)
2. **Two pull-forward bays**, signed and closest to the exit, for hot-food and mobile orders. (§5.4)
3. **Lane timers and a stack camera** with triggers at cars 8, 10 and 12. The camera must not read number plates without a personal-data assessment (C5 §3.8). (§5.4)
4. **Equipment brands with local service.** The Horeca LLC is an authorised Mahlkönig dealer and links La Marzocco, Victoria Arduino, Nuova Simonelli, Mahlkönig, Franke, Hoshizaki, Bravilor, Rational and Electrolux. **No Armenian service partner was found for Merrychef, TurboChef or Eversys** (C2[S2][S3]). Either specify locally serviced ovens or keep two speed ovens plus a spares kit worth 5–8% of equipment value (C2 §3.1.1).
5. **Freezer capacity.** Weekly frozen deliveries need ≈0.5–1 m³ of freezer space (C2 §3.3.6). Confirm that the reach-in freezer is enough or add one.
6. **Water treatment and a site water analysis** before the equipment specification (C2 §4.12).
7. **Sewer.** The FSIB checklist requires sanitary units "connected to a working sewer". A septic solution on a highway plot may be challenged (C5[14] item 1.4), so get FSIB's written view.
8. **The three permitting fixes in §13.3:** lane lengths, hard-surface area and pylon.

---

## 7. Supply chain

### 7.1 Supplier map

| Category | Candidate suppliers | Price basis | Delivery to an M4 site | Contract terms to seek (ASSUMPTION) |
|---|---|---|---|---|
| **Espresso blend** | AfroLab (wholesale form), Lumen, Nero Bean, Caffeine (Dilijan), Royal Armenia. **Not FEIN**: it belongs to the Coffee House group, the incumbent (C2[S38][S39]; A2 via C2) | Model AMD 12,000/kg, range 9,000–16,000 (C2 ASSUMPTION). Retail benchmarks AMD 8,900–20,300/kg imported, 22,000–23,600 local specialty (C2[S36][S37]). Roasted imports pay 8% duty (min €0.16/kg) vs 0% on green (C2[S6]) | **Weekly**; roasted coffee keeps 2–6 weeks (C2 §3.3.1) | 12-month price lock or a formula indexed to green coffee; roast date on every bag; 1 week of safety stock held by the roaster; co-branded "CHAMPA blend"; barista training and grinder calibration included. Coffee is under Data Matrix marking since 1 Mar 2025 (C4[11]); supplies arrive marked |
| **Milk** | Marianna, Dili, Yeremyan Products, Bonilat, Chanakh, Arzni, Ashtarak Kat (C2 §3.3.2; A4[26a]) | Model AMD 700/L (Marianna retail AMD 642–790/L; C2[S40]) | **3×/week** (C2 range 3–7×) **plus a 1–2-day UHT buffer** | HoReCa price list; route confirmation (Abovyan/Hrazdan); 1 L barista or UHT formats. Dairy under Data Matrix marking since 1 Jan 2026 (C4[11]) |
| Plant milk | Alpro Barista Oat (AMD 1,410/L retail), OraSi Barista, Nushanush (A4[19]) | AMD 1,300/L (C2 ASSUMPTION); costs ≈AMD 115 more than milk per drink (A4 §3.5) | With dry goods, fortnightly | Charge a **+AMD 200–300** surcharge (A4) |
| **Frozen bake-off croissant** | Russian producers Rus Bakery, GFC/Allegro, Gourmand (EAEU, duty-free); **no Armenian importer of premium frozen pastry identified** (C2[S45]) | RUB 23–60 ex-works (AMD 99–256); **landed ≈AMD 350** (C2 ESTIMATE, +40% freight) | **Weekly or fortnightly**, needs −18 °C storage (C2 §3.3.6) | **Dual source:** EAEU frozen plus a Yerevan contract bakery (AMD 400–500 wholesale, C2 ASSUMPTION). Russia–Armenia trade bans in Apr–Jun 2026 (A5 via A1) and McDonald's Kazakhstan's patty-supply exit (A5[14][15]) show the route risk |
| Armenian pastry (gata, ponchik shells, zhingyalov hats, lavash) | Grand Candy, Nor-Nar (Gavar gata), Zeytun, Levrim, Tnakan, Karas (Abovyan branch) (A4 §3.7) | Gata ≈AMD 300 per 100–120 g bought in (C2); bought-in local pastries run 45–67% food cost (A4 §3.11) | **Daily or 3×/week** with a day-old discount (C2 §3.3.6) | Wholesale price ≤60% of retail; return of unsold items for the first 8 weeks; MOQ and M4 delivery confirmed (A4 §5 gap) |
| **Packaging** | Oval Pack (Ovalplast, Yerevan); Art Global (C2[S43][S5]) | Hot cup AMD 13–16; double-wall 400 ml 32; lids 5–11; clear cold cup 20–25; carrier 80. **≈AMD 35–42 per drink, ≈8% of beverage COGS** (C2 ESTIMATE) | **Monthly**; hold **4–6 weeks** of stock | Custom print only on the **2 core SKUs** (double-wall 400 ml hot, 500 ml cold), since the MOQ is 5,000 per SKU and printing adds ≈17% (C2 §3.3.4). Others plain, with a printed sleeve (AMD 8). Ask whether prices include VAT (C2 gap 9). 2% environmental tax applies to self-imported plastics (C4[1] Art. 171) |
| Syrups | Monin via Alpha Food Service (≈3,000 HoReCa clients) (C2[S41]) | AMD 6,500/L (C2 ASSUMPTION); 12% duty outside the EAEU | Monthly | Test an EAEU syrup: 50–70% cheaper, quality risk (C2 §3.3.3) |
| Bottled tan, water | Aparan, Bonilat; Jermuk, Bjni (A4[20][21]) | Tan retail AMD 210–580; water 0.5 L AMD 170–250 | Weekly | **Bottled tan is a marked dairy product**: reselling it needs Data Matrix scanning at the HDM (C4[1] Art. 381(3.1)) |
| Ice (fallback) | Supermarkets | AMD 190–440/kg (C2[S40]) | Emergency | Keep 1 day of bagged ice in summer in case the ice machine fails |

### 7.2 Volumes and par levels (ESTIMATE)

Common inputs:
- 1.2 drinks per transaction (ASSUMPTION);
- C2's beverage mix and recipes (18 g double shot; 200–300 ml milk);
- milk waste ×1.10; coffee waste ×1.05 (C2 §3.4);
- food attach of 30–45% of orders (A4 ASSUMPTION), with croissants 45% of food items (C2).

| Item | At 110 tx/day | At 150 tx/day | Par / reorder rule |
|---|---|---|---|
| Espresso blend | ≈2.2 kg/day, ≈65 kg/month | ≈3.0 kg/day, ≈89 kg/month | Weekly order = 7 days' use + 3 days' safety |
| Milk | ≈26 L/day | ≈35 L/day | 3 drops a week (≈60–80 L per drop) + 50 L UHT buffer |
| Frozen croissants | ≈105–155 per week | ≈140–215 per week | 2–3 cases of 70–80 pieces per week |
| Cups, all sizes | ≈5,500 per 6 weeks | ≈7,600 per 6 weeks | Reorder at 3 weeks of cover |

The summer peak needs ≈1.5× par (model index 1.42–1.46 in Jul–Aug).

**Working capital:** the model's 10 days of COGS may be light given 4–6 weeks of packaging and the frozen buffer. Test 15–20 days (ASSUMPTION).

---

## 8. Inventory and waste control

1. **Counts.**
   - Daily: milk, pastry, fresh food and cups.
   - Weekly: full stock-take.
   - Monthly: variance report, targeting **<1.5% unexplained variance** (ASSUMPTION).
2. **Bake to the curve.** Small bake-off batches every 30–60 minutes, keyed to the POS hourly sales curve from the previous 4 weeks.
   - Stop baking croissants 90 minutes before close.
   - Wraps are assembled to order from mise-en-place prepped for 2–3 days at most.
3. **FEFO** (first-expiry, first-out) with date labels on everything opened. The walk-in cooler is organised by delivery day.
4. **Waste log in the POS**, by reason (expired, quality, remake, staff error).
   - Model target: **waste ≤2% of net sales** (`waste_pct`).
   - Under the general (VAT) regime, only up to **1% of gross income (2% for marked dairy)** of documented quality losses is deductible (C4[1] Art. 122(3)). Document every write-off as if that limit applied.
5. **Remakes.** Track them separately: they measure accuracy.
6. **Seasonal swing.** Raise pars before Sevan weekends (Friday deliveries) and cut them sharply from October. C2 warns that Sevan seasonality amplifies **both** stock-outs and waste (C2 §3.3.6).
7. **Theft and cash.** Cashless-first payments; HDM receipt for every sale (C4[1] Art. 381); cash drop at the lead's discretion; CCTV on the windows and the safe (ASSUMPTION).
8. **Supplier scorecard** each month: on-time rate, temperature on arrival, short-deliveries, price variance.

---

## 9. Quality control, food safety and HACCP

### 9.1 Legal frame (C5 §3.2)

- **HACCP is mandatory from day one** for catering (GD 827-N; the micro-enterprise deadline was 1 Jan 2023; C5[13]).
- **From 1 Jan 2027, the "approved HACCP plan" is part of FSIB registration** (HO-98-N; C5[11]). The opening in May 2028 falls under this rule.
- **Registration** with the FSIB happens **before activity**. It is free, and changes must be notified within 3 days (C5[10] Art. 17; C5[33] snund.am).
- **Inspections** use the weighted catering checklist (GD 1266-N Annex 3; C5[14]). They are capped at **≤1 a year for high-risk** operators, ≤1 in 3 years for medium and ≤1 in 5 for low (C5[30]). The risk class of a new drive-thru is unknown (C5 §5 #11).
- **Enforcement is real.** On 5 Oct 2026 the FSIB suspended a catering outlet for non-washable walls and **no staff changing room** (C5[35]).
- **Out-of-date rules.** The 2003 catering sanitary rules were **repealed in May 2022** (C5[15]). Consultants' checklists that cite them are obsolete.

### 9.2 HACCP plan outline (to be written by a consultant with the manager, M15–M17; ASSUMPTION on structure)

| Step | Hazard | Control point | Monitoring | Record |
|---|---|---|---|---|
| Receiving milk, dairy, frozen goods | Bacterial growth; thawing | Temperature on receipt; packaging; dates | Probe every delivery | Receiving log; reject slip |
| Cold storage (walk-in, under-counter, freezer) | Growth | Temperature limits set in the plan per the FSIB catering guide (C5[32]) | 2× daily + alarm | Temperature log |
| Bake-off and wrap cooking | Under-cooking (egg) | Core temperature and time on each oven program | Probe per batch at the start of a shift | Batch log |
| Hot holding at W2 | Growth | Maximum holding time per item | Timer labels | Discard log |
| Milk in use | Growth | Pitcher rotation; jug out of fridge ≤ set time | Shift checks | Shift checklist |
| Ice machine and water | Contamination; scale | Filter changes; weekly ice-bin sanitising; **uninterrupted potable water** (FSIB item 1.20) | Filter log; water test | Maintenance log |
| Allergens and labels | Undeclared allergens | Allergen matrix; **Armenian labels ≥3 mm** on pre-packed items (C5[10] Art. 9(2)) | Label check per delivery | Label file |
| Personnel | Contamination | **Valid medical book** (on hiring, every 6 months; C5[16]); hand-washing at separate sinks with hot water (FSIB items 1.5–1.6) | Manager check monthly | Medical-book register |
| Waste | Pests | Closed, cleanable containers (FSIB item 1.18); stored ≥10 m from the road edge (C5[1] Art. 13(16)) | Daily | Pest-control log |

### 9.3 Product quality routine (ASSUMPTION)

- **Every opening:** espresso calibration (dose, yield, time); grinder purge; water-filter check; milk-steaming check; photo of the reference drink in the shift app.
- **Recipe cards for every SKU,** showing **grams/ml on the menu board as the law requires** (C5[17] Art. 12(3)).
- **Monthly mystery shop** (speed, accuracy, temperature, ritual), plus a quarterly internal HACCP audit.
- **Supplier QA.** Approved-supplier list with certificates; **no roadside or open-market sourcing**. A4[39] found aflatoxins above EU limits in dried fruit from Yerevan open markets.

---

## 10. Customer-service rituals and standards

The rituals below are ASSUMPTIONS that apply the brand system, except where a source is cited.
- The brand's evidence point is that friendliness is also faster: friendly visits were 25 s quicker in 2026 (C6[17]).
- Starbucks' FY2025 reset shows hospitality, not a sterile speed box, protects traffic (C6 §3.2.3).

| Moment | Standard |
|---|---|
| Greeting (speaker, tablet, counter) | Armenian first: *«Բարի գալուստ ՃԱՄՓԱ»*. Switch to Russian or English when the guest does (relocants and tourists, A5 §3.6) |
| Order | Read back the order; customisations confirmed on the order-confirm screen; one suggestive upsell (combo or food). US beverage brands upsell in only 19.5% of visits (C6[17]) |
| Payment (W1 or tablet) | Contactless first; QR (Idram) shown on the screen; receipt (HDM/e-HDM) always issued (C4[1] Art. 381) |
| Handoff (W2) | Eye contact; name on cup; lid pressed; straw and napkins; carrier for 3+ drinks; then the blessing **«Ճամփադ բա՜ց»**, *"May your road be open"* (brand/naming-report.md). The sleeve repeats it |
| Queue care (car 8 or more) | Runner greets the queue, takes orders, and in winter offers a thimble of herbal tea. Herbal tea is low-cost (A4 §3.9) |
| Service recovery | More than 10 minutes, a wrong item or a complaint: fix on the spot plus a next-visit token. Owned by the lead without needing approval |
| Restrooms and terrace | Hourly checks logged. The 2 accessible restrooms are part of the roadside offer (GD 2404-N §5(է), (թ); C5[3]) |
| Regulars | Loyalty recognition at W1; "road regular" status after 10 visits/month |
| Uniform and badges | Brand uniform; **photo name badge** (C5[17] Art. 12(4)) |

---

## 11. Technology stack

### 11.1 Architecture

| Layer | Choice for unit 1 | Status and cost basis |
|---|---|---|
| POS + KDS (kitchen display) | Cloud POS with KDS for the bar and food lines, inventory, loyalty and web ordering. Candidates: **Poster** (USD 26/44/62 per month; +USD 19 per extra register; Poster Site USD 19/month; QR USD 7/month; loyalty included; C2[S34]), **iiko** (RUB 1,295–9,200/month ≈ AMD 5.5–39.3k; C2[S35]), R-Keeper, local systems | **Neither Poster's nor iiko's pages mention Armenian fiscalisation** (C2 §3.2.1). Selection gate in §11.3 |
| Fiscal devices | **New-generation HDM with integrated card terminal** (e.g. Newland N950, Android): AMD 85–95k new, AMD 60–125k range (C2[S33]). Units: W1, café counter, 2–3 runner handhelds = 4–5 devices ≈ AMD 0.24–0.63m (ESTIMATE). Banks can enable card acceptance on the HDM itself (FastBank; Ameriabank "POS via cash register"; C2[S26][S27]) | REPORTED prices. **Ask SRC to confirm in writing that handheld HDMs registered to the outlet can take payment in the lane** (C4[1] Art. 381(1)–(2): the HDM is registered at the outlet address and placed where payment happens) |
| e-HDM | For app and web orders and any future delivery. Law HO-309-N: e-HDM rules from **1 Jan 2027**; the Government will name the sectors where it is mandatory; AMD 500,000 fine for trading without it where required (C4[6]; C2[S32]). An SRC API exists (C2[S32c]) | Plan for e-HDM from day one |
| Product marking | POS must scan Data Matrix codes for **resale of marked goods** (bottled tan, packaged dairy drinks) (C4[1] Art. 381(3.1); C4[11]) | Required |
| Headsets | HME EOS HD/NEXEO or 3M/Clear-Com. **No Armenian dealer found**; placeholder USD 4,000–8,000 per lane → USD 8–16k for 2 lanes (C2 §3.2.3 ASSUMPTION). Radio-frequency approval of imported headsets needed | Gap: RFQ via EMEA distributors |
| Order-confirm and digital menu boards | 2 outdoor menu boards (2,500+ nit) + order-confirm screens at OP-A/OP-B + W1 customer display: placeholder USD 5,000–20,000 per lane → USD 10–40k (C2 ASSUMPTION). **Content must show mass/volume and final price, with Armenian first** (C5[17][20]) | Gap: local LED integrators |
| Runner tablets | Handheld HDM-POS devices (above); rugged cases; cold-weather spares (ASSUMPTION) | — |
| Lane timers, stack camera | Vehicle detection at the order points, W1 and W2; stack camera with triggers. No ANPR without a personal-data assessment (C5 §3.8) | Not priced (C2 gap 13) |
| Mobile order-ahead and loyalty | **Launch on a POS-native web app and loyalty** (e.g. Poster Site + loyalty; iiko loyalty in its Start/Pro tiers; C2[S34][S35]). Defer a custom white-label app (USD 15–60k build + 15–20% a year; C2 ASSUMPTION) until the unit-2 gate | Loyalty share benchmark: Dutch Bros 72–74% of transactions, Black Rock 63% of sales; **plan 10–30% by year 3 in Armenia** (C6 §3.10 ASSUMPTION) |
| App order rules | Time-slot pickup at W2 or the café shelf; **cap app orders per 5-minute slot** so they don't starve the lane (app-order priority was among the incumbent's failure modes; A5 §3.5) | ASSUMPTION |
| Back office | Shift-scheduling app with hours tracking (needed for summarised-hours accounting, overtime caps and night premiums), digital HACCP logs, accounting with TT expense tagging (C4 §3.5: deductible expenses must be documented) | ASSUMPTION |

**Technology capex for unit 1** (ESTIMATE from C2 placeholders):

| Item | USD |
|---|---|
| Order stations (3 × USD 800–1,500) | 2.4–4.5k |
| HDMs | ≈0.7–1.7k |
| Headsets | 8–16k |
| Boards | 10–40k |
| **Total** | **≈USD 21–62k (AMD 7.6–22.5m)**, before timers and installation |

**Software:** USD 50–150/month per site (C2 ASSUMPTION).

### 11.2 Payments and acquiring fees

| Method | Status in Armenia | Merchant cost |
|---|---|---|
| ArCa and Visa/Mastercard, in person | FastBank standard package: **1.2%** for cards from ArCa-member banks, **2.2%** for foreign cards. AMD 8,000/month if the turnover target is unmet (from 10 Sep 2026). Free installation within 3 days; AMD 50,000 fee if terminated within 1 year (C2[S26], VERIFIED). Ameriabank: case by case, minimum fee AMD 4,600/month, AMD 50,000 clawback within 1 year (C2[S27]) | **Blended ≈1.35%** (0.85 × 1.2% + 0.15 × 2.2%; C2 ESTIMATE); range 1.3–1.6%. Higher in a tourist-heavy summer |
| CBA fee cap (0.5% ArCa / 0.9% Visa-MC) | **Does not apply.** Restaurant and fast-food MCCs (5812/5814) are not on the annexed list (C2[S24], VERIFIED). The cap also covers only merchants with turnover ≤AMD 150m, which A1's fact-check notes a busy unit would exceed | Do not model it |
| Apple Pay | Live since 18 Jan 2022 with Acba, Ardshinbank, Ameriabank, Converse, Inecobank, Unibank. Works on any contactless terminal (C2[S30]) | Card rate |
| Google Pay | C2 did not verify it. A1 reports it live since Nov 2022, but A1's section-7 fact-check confirmed only Ameriabank's launch, on 15 Nov 2022 (A1[27]). A5 §3.3.5 cites A1 for "Apple Pay/Google Pay are live" | Card rate; test with each bank at launch |
| Idram QR | >22,000 QR points of sale; same-day settlement; **fee not published** (C2[S31]) | Request the merchant agreement |
| Telcell | Not researched (C2 gap 12) | Request |
| Online (app) | Ameriabank internet acquiring **1.5% ArCa / 2.7% Visa-MC**, VAT included; Apple Pay in-app supported (C2[S28], VERIFIED) | — |
| Cash | Allowed; HDM receipt mandatory | Handling cost |

**Model input recommendation.**
- The model carries 1.8% on a 75% card share (`card_fee_pct`, `card_share`, both PLACEHOLDER).
- Use **1.5% as the base** after a 2–3-bank tender. Keep 1.8% as the conservative case. That is consistent with A1's fact-checked base of 1.5–2% where the cap does not apply.
- In the tender, confirm the MCC assignment (5814) and negotiate below the 1.2% list rate at volume (C2 §4.8).

### 11.3 Selection gates for the technology (M2–M12)

1. **Live demo, by M10,** of POS → HDM/e-HDM fiscal receipt → bank terminal → KDS → loyalty, with an Armenian reference customer (C2 gap 10).
2. **SRC written confirmation** that the HDM set-up (handhelds in the lane, app e-HDM) is compliant (C4 §4.5).
3. **Headset RF approval** and a local service route (C2 gap 13).
4. **Bank tender closed by M12**, with the early-termination fee waived (ASSUMPTION).

---

## 12. Digital and local marketing

### 12.1 What we say

- **Message:** lead with **speed + local taste + the road blessing**, not "American".
  - A4 §4.1 and A5 §4.8: "American-style" should describe the service format. Imported concepts that did not localise have failed (Starbucks Israel and Australia; Dunkin' Poland; A5[24][25]).
  - The American cue is the *service standard*: published lane times and order accuracy.
- **Language** (Law on Advertising Art. 5; Law on Language Art. 4; C5[20][21]):
  - all paid advertising, signage and menu boards **Armenian first** (above or left);
  - foreign text is never larger or brighter;
  - Latin "CHAMPA" appears only as a **registered** trademark;
  - the Armenian wordmark ՃԱՄՓԱ leads everywhere.
  - Do not file *Ճամփադ բաց* as a plain word mark; use it inside composite marks (brand/naming-report.md).

### 12.2 Channels

| Channel | Plan (ASSUMPTION unless cited) |
|---|---|
| **Yandex Maps, Google Maps, 2GIS** | Claimed listings from the day the permit is issued: drive-thru attribute, seasonal hours, menu with **grams and prices** (legal requirement), lane-speed promise, photos. Coffee House's M4 drive-thru shows how visible a rating is: 4.9★ from 123 ratings but 17 text reviews averaging 3.76★ (A5 #27). Target ≥4.7★ with replies within 24 h. A4 lists 2GIS among the sources to check |
| **OpenStreetMap** | Tag the site `amenity=cafe` + `drive_through=yes` + brand tags. Armenia has **zero** tagged drive-thrus (A5[32]), and many navigation apps draw on OSM |
| **Instagram and TikTok** | Four content pillars: (1) *«Ճամփադ բաց»* road stories (Sevan, Tsaghkadzor, Dilijan), (2) the speed promise (lane-timer clips), (3) the local menu (Gavar gata, zhingyalov hats, sea-buckthorn, tarragon and apricot lemonades; A4 §3.12), (4) the crew. Captions Armenian first, with Russian/English lines. *No Armenian social-media usage data is in the files reviewed; channel weights are to be set from the intercept survey (§14)* |
| **Glovo / Yandex Eats** | **No at unit 1.** A highway site has no delivery catchment (C6 §3.3). Aggregator prices run ≈0–10% above in-store (A4 note), and every order needs an e-HDM receipt. Revisit for an urban-arterial unit |
| **Loyalty / web app** | Launch offer: 5th drink free; birthday drink; "road regular" tier. Target 10–30% of transactions by year 3 (C6 §3.10) |
| Receipt lottery | **Not verified** to exist in 2026 (C4 §3.9). Do not plan around it |

### 12.3 Roadside signage: what the rules allow (C5[2] GD 765-N; C4[1] Art. 190)

| Rule | Value |
|---|---|
| Permit | MTAI for interstate roads outside settlements, agreed with the **Police**. Electronic application with design, 2 site photos and, from 2026, **landowner consent** |
| Timing and validity | **Decision in 30 days**; compliance act within 7 days; valid **5 years** (+1-year extensions); lapses if not installed **within 6 months** |
| Geometry | Board **≤27 m²**; lower edge **≥2.2 m** above the road; **≥3.5 m** from the asphalt; **≥150 m** from junctions, bus stops and bridges; **200 m spacing** between 15–27 m² boards on roads above 60 km/h; refused where visibility is **under 350 m** |
| Upkeep | Inspection every 6 months; repaint yearly; crash repair within 15 days |
| Road tax | **AMD 10,000/m²/yr** on interstate roads outside settlements (C4[1] Art. 190). The prototype pylon (8 m × 2.2 m, two faces = 35.2 m²) would cost ≈AMD 352k/yr *if* classed as advertising (ESTIMATE) |
| Inside settlements | Community permit; local duty AMD 1,500/m²/month (own carrier pays 10%) (C5[18]) |

**Plan.**
- Two advance boards on the approach, ≤18 m² each, at ≈0.5–1 km and ≈250–300 m before the entrance. C6 §3.5 recommends ≥0.5–1 km of advance signage at 90 km/h (ASSUMPTION there).
- The second board must sit ≥150 m from the junction (ASSUMPTION on placement).
- Road tax ≈AMD 360k/yr (ESTIMATE: 2 × 18 m² × 10,000).
- **Apply in M15–M16 so the boards can be installed by M18.**
- The fascia sign on the building is a *signboard* (Law on Language Art. 1.1), not advertising. Get MTAI's view on the pylon early (§13.3).

### 12.4 Partnerships (ASSUMPTION; the offer depends on which carriageway is chosen, since access is right-in/right-out and serves one direction, C5[5])

| Partner | Offer | Fit |
|---|---|---|
| **Tsaghkadzor and Sevan hotels, guesthouses, beach operators** | QR pre-order "road breakfast box" sent with booking confirmations; staff coffee accounts; display of the lane-speed promise | Leisure drivers are the 2nd adopter segment (A5 §3.6) |
| **Employers along the M4 (Abovyan factories, logistics)** | Pre-ordered coffee for **shift buses** that already run (C3 §3.3: local employers bus their staff); invoiced monthly | Weekday base load; staff-recruitment channel too |
| **Ride-hail and taxi drivers** | "Road crew" card: low-ticket coffee + pastry at a set price at off-peak hours | Professional drivers are segment 3 (A5 §3.6) |
| **Fuel retailers** | **Cross-promotion only for unit 1**: a coupon on CNG or fuel receipts from stations without a café. Max Cafe (km 12.2), Flash and CPS run their own cafés and are competitors (A5 §1.5, citing A3; A4[27]). **Avoid co-locating unit 1 on a forecourt**: a café inside a fuel complex may be pulled toward risk category IV, and fuel storage ≥5 m³ is an EIA Category B trigger (C5 §3.3, §3.7). The fuel-station hybrid stays a format option for later units (A5: 45–55%) | Evidence of the format in the region: WOG ≈181 cups/point/day (A5 #25); 27 of Georgia's 72 Dunkin' outlets sit at forecourts (A5[32]) |
| Colleges in Abovyan and Yerevan | Part-time recruitment, student offer | Labour (C3 §4.5) |

### 12.5 Launch plan and budget (model: AMD 12M launch + 3% of net sales ongoing; C6 §3.3 calls this consistent)

| Phase | Months | Actions |
|---|---|---|
| Pre-launch | M17–M19 | Maps and OSM listings; Instagram/TikTok teasers (build film, crew stories); hotel and employer outreach; advance boards installed; waitlist with a free first drink |
| Soft launch | M19 (2 weeks) | Invite-only and local residents; limited menu; 07:00–21:00; lane timers live; daily fixes |
| Grand opening | M20 (June) | *«Ճամփադ բաց»* weekend; sampling; creators driving the Sevan route; loyalty sign-up push |
| Season 1 | M20–M22 | Weekend "Sevan run" content; lemonade and iced line; partner offers |
| Winter | M25–M29 | Commuter focus: breakfast wrap + coffee combo; New Year gata gift boxes (**check with SRC whether gift boxes count as catering or as 20% "other" income**; C4 §3.5(c)) |

Indicative split of the AMD 12M launch budget (ASSUMPTION):

| Use | Share | AMD |
|---|---|---|
| Paid social | 30% | 3.6m |
| Opening events and sampling | 20% | 2.4m |
| Creators and PR | 15% | 1.8m |
| Photo and video | 15% | 1.8m |
| Maps, OSM and listings set-up | 5% | 0.6m |
| Reserve | 15% | 1.8m |

Signage capex and road tax sit outside this budget.

### 12.6 Marketing KPIs (weekly)

- Transactions/day by daypart.
- Share of new vs repeat customers (loyalty).
- Maps rating and review count.
- Loyalty sign-ups and share of transactions.
- Food attach.
- Cost per acquired loyalty member.
- Partner-coded redemptions.

---

## 13. Armenian regulatory and permitting roadmap

### 13.1 Who decides what (C5 §3.1)

| Domain | Body |
|---|---|
| Land designation | Community council. Without a master plan: regional commission → MTAI → interagency commission, which must be unanimous; otherwise a Government committee decides (GD 1918-N; C5[9]) |
| APA (planning assignment), construction permit, final act, operating permit | Community head via e-permits (GD 596-N; C5[7]) |
| Special-regulation coordination (interstate road strip, Sevan basin) | Marzpetaran → Urban Development Committee (GD 2404-N, GD 792-N; C5[3][4]) |
| Road connection, building in the 70 m protection zone, traffic scheme | **MTAI** (state road body) + **Police**; Roads Department Foundation runs the network (Law on Highways Art. 13–15.3; C5[1]) |
| Road-safety audit | Certified auditor; in force for interstate roads from 1 Jan 2026. **Whether it applies to a private junction is unclear** (C5[1] Art. 19.2) |
| Roadside advertising | MTAI + Police (C5[2]) |
| EIA, Sevan, national park | Ministry of Environment expertise centre; Sevan NP SNCO; community council for EIA consent (C5[22]–[26]) |
| Food safety | FSIB / ՍԱՏՄ (snund.am) (C5[10][12][14]) |
| Fire and construction quality | Inspection Body for Urban Development, Technical and Fire Safety. **No separate fire-approval step found for category II** (C5 §3.8); the all-electric kitchen removes the gas-permit path |
| Tax, HDM, customs | SRC (C4) |
| Labour | Health and Labour Inspection Body (C3 §4.3) |
| Language | Language Committee (C5[21]) |
| Trademark | Intellectual Property Office (C5[36]; C4[13]) |

### 13.2 Step-by-step roadmap with durations, fees and plan dates

"Statutory" durations are VERIFIED in C5. "Realistic" durations are C5's ESTIMATE/ASSUMPTION. "Plan" puts each step on this project's calendar (M1 = Nov 2026).

| # | Step | Responsible body | Legal basis | Statutory time | Realistic (C5) | Fee | **Plan** |
|---|---|---|---|---|---|---|---|
| 0 | Company: LLC registration; **turnover-tax (TT) declaration within 20 days** (missing it makes the company a VAT payer for the year) | State Register (e-register.am); SRC | C4[17]; Tax Code Art. 254(1)(2) | Immediate (standard charter) / 2 business days | — | **Free** | M1 |
| 0a | Trademark filing ՃԱՄՓԱ / CHAMPA (composite marks; class 43 + related) | Intellectual Property Office | Law on Trademarks; State Duty Art. 18(4) | Not verified (C5 gap 20) | Months | **AMD 120k (1 class) – 150k (3 classes)**; Madrid CHF 653 base (C4[13][20]) | File M1; registered before signage is fabricated (M15) |
| 1 | Site due diligence: cadastre extract, designation, encumbrances, Land Code Art. 60 certificate, road-strip and **Sevan GIS overlays**, utilities | Cadastre Committee; community; MTAI | Land Code Art. 7, 60; GD 2404-N; GD 1563-N | — | 2–6 weeks | Small | M3–M4 |
| 2 | **Pre-consultation on access**: M4 category (IB or IC), right-in/right-out, technical conditions | MTAI / Roads Department Foundation; Police | Law on Highways Art. 13(16), 14(2),(4), 15.3 | **None found** | 1–3 months | None found | **M3–M5 (critical)** |
| 3 | Land control: option or ground lease, **conditional on access and zoning comfort letters** | Owner / community (auction for public land) | Land Code; GD 596-N §42–44 | Auction rules | 1–4 months | Price | Option M4; exercised at Gate 1 (M6) |
| 4 | **Land-designation change** (if agricultural) | Community → marzpet → regional commission → MTAI → interagency commission → council | Urban Development Law Art. 30(2); GD 1918-N | ≈28 working days + council session | **2–4 months** | **Cadastral-value difference** paid to the community (Land Code Art. 7(8)); site-specific | **M5–M7 (critical)** |
| 5 | **Junction design, traffic scheme, road-safety audit; MTAI + Police agreement** | Road designer; MTAI; Police; certified auditor | Law on Highways Art. 15.3, 19.2; ՀՀՇՆ 32-01-2022 | None found | 1–3 months | Design and audit fees (no data); **traffic equipment at the developer's cost** | **M5–M7 (critical)** |
| 6 | EIA screening: **written Ministry of Environment opinion** on whether site paving ≥1,000 m² triggers Category B | Ministry of Environment expertise centre | EIA Law Art. 12(4)(8)(գ) | — | — | — | M4–M5 |
| 7 | **EIA Category B** (if triggered): notice → hearing on working day 21–25 → **council consent ≤30 working days (veto possible)** → expertise ≤40 working days (+30) | Community; Ministry of Environment | EIA Law Art. 13, 16, 27 | ≈107 working days (+30) | **5–7 months** | **AMD 315,000** (300k + 15k) | **M8–M13 (critical)** |
| 8 | Sevan declaration and national-park agreement | Ministry of Environment / Sevan NP | Law on Lake Sevan Art. 25; GD 927-N; GD 1563-N | 1 month | 1–3 months; subzones 1–2 longer | — | **Not needed if the site is west of Hrazdan** (C5 §3.7). Sevan sites are phase 2 at best |
| 9 | Building design (category II; designer's guarantee letter replaces expertise) | Licensed designer | GD 596-N Annex 4 List 2 | — | 6–12 weeks | C1 soft costs | M8–M10 |
| 10 | **APA** with utility technical conditions | Community head (e-permits) | GD 596-N §47–53 | **10 days** (II); conditions 5 days | 2–4 weeks | **Free** | M9 (APA valid ≤1 year, so the permit is needed by M20) |
| 10a | Special-regulation coordination of the APA (road strip) | Marzpetaran; Urban Development Committee | GD 2404-N §4.2, 8; GD 792-N §12 | 3 + 5 + 15 = 23 working days | 1–2 months | — | M9–M10 |
| 11 | Water-use permit (only for a borehole or discharge) | Water Resources Management body | Water Code Art. 21, 30 | ≤50 working days | 2–3 months | Not checked | M9–M11 if needed |
| 12 | Utility connections: ENA power; water and sewer | ENA; Veolia Jur / community | PSRC rules (C1) | — | 2–4+ months | C1 | Apply M9; connected by M15–M17 |
| 13 | **Design approval + construction permit** (issued together) | Community head (e-permits) | Urban Development Law Art. 23; GD 596-N §100 | **5 days** (II) | 1–3 weeks | **AMD 15,000** (public building ≤200 m²; the 171 m² building qualifies) (Law on Local Duties Art. 11). hartak.am's AMD 75,000 is read as the Yerevan figure | **M13 (critical)** |
| 14 | Start-of-works notice | Community | GD 596-N §129 | ≥3 days before works | — | Free | M13 |
| 15 | Construction, including speed-change lanes inside the right-of-way | Contractor; road body acceptance | — | — | **4–6 months** (C1) | Lanes **AMD 27–43M** (C5 ESTIMATE) | **M13.5–M18.5 (critical)** |
| 16 | Roadside advertising permit (advance boards; pylon if classed as advertising) | MTAI + Police | GD 765-N | **30 days** + 7-day compliance act | 1–2 months | No permit fee found; **road tax AMD 10,000/m²/yr** | M15–M16; install by M18 |
| 17 | **Acceptance commission → final act + operating permit.** Operating before the operating permit is **prohibited** | Developer's commission; community head | Urban Development Law Art. 25; GD 596-N §147.2, 160–165 | 5 + ≤10 + 3 days | 3–6 weeks | Community fee (Yerevan reference AMD 100k + 50k for 100–500 m²) | **M18.5–M19 (critical)** |
| 18 | **FSIB registration with the HACCP plan**; HACCP system live; staff medical books | FSIB; clinics | Food Safety Law Art. 8, 10, 17; HO-98-N; GD 347-N | Before activity | 4–8 weeks pre-opening | **Free** (registration); exams no data | Plan written M15–M17; registration **M19 (critical)** |
| 19 | Community catering permit; waste contract; signage check; HDM registration at the outlet address | Community; SRC | Law on Local Duties Art. 11; Law HO-237-N; Tax Code Art. 380–381 | — | 2–4 weeks | **AMD 15,001–20,001/quarter** (100–200 m²; Abovyan draft AMD 18,000); waste **AMD 50–100/m²**; HDMs AMD 60–125k each | M18–M19 |
| 20 | **Catering TT declaration within 20 days of passing AMD 115M receipts** (calendar alert) | SRC | Tax Code Art. 254(7) | 20 days | — | — | When the threshold is crossed (year 1) |

### 13.3 Compliance check of the current prototype (ESTIMATE from `design/layout.json`; to the design team)

| Issue | Prototype | Rule | Gap | Fix |
|---|---|---|---|---|
| **Deceleration lane** | 86 m total (46 m parallel + 40 m taper) | **90–110 m full width + 80 m taper** (= 170–190 m) where flow is ≥50 vehicles/day (ՀՀՇՆ 32-01-2022 Table 31; C5[5]) | ≈84–104 m short | Lengthen. C5 sizes both lanes at 1,155–1,500 m², **AMD 27–43M**, above C1's allowance of 700–1,125 m² |
| **Acceleration lane** | 121 m total (71 m + 50 m taper) | **140–230 m + 80 m taper** (= 220–310 m); uphill toward Sevan points to the long end (C5 §3.5) | ≈99–189 m short | As above |
| **Impervious surface (EIA trigger)** | Site 3,256 m² − planting 1,216 m² − building 171 m² ≈ **1,870 m²** of hard surface (asphalt lanes and aisle, kerbed islands, basalt plaza) | Category B if "landscaping with **≥1,000 m²** impervious surface" (EIA Law Art. 12(4)(8)(գ); C5[26]). Applicability to private paving is unconfirmed (C5 gap 4) | ≈870 m² over | Permeable pavers on stalls and aisle (−655 m²) and plaza (−244 m²) → **≈970 m²**, just under. **Get the MoE written opinion before buying land.** Otherwise plan for the 5–7-month EIA and the council-veto risk |
| **Roadside pylon** | 8.0 m high, 2.2 m wide, ≈6.6 m from the deceleration-lane edge (meets the ≥3.5 m rule), at the site entrance | If classed as advertising: MTAI permit, **≥150 m from junctions**, road tax. The 18 m side-visibility zone of GD 2404-N also applies (C5[2][3]) | Classification open (C5 gap 8) | Ask MTAI at the pre-consultation (step 2). Fall-back: a fascia/tower signboard on the building plus 2 permitted advance boards |
| **Protection zone** | The whole plot lies ≈18–62 m from the road axis (ESTIMATE from the cross-section), i.e. **inside the 70 m interstate protection zone** | Building, access and non-traffic signs need road-owner agreement (Law on Highways Art. 13(6)) | — | Part of step 2/5. The Government list of objects permitted in protection zones (Art. 13(15.2)) was not found (C5 gap 3) |
| **Category II** | 171 m², single storey, no fuel | ≤300 m², ≤2 floors above ground → category II: guarantee letter, 10-day APA, 5-day permit (GD 596-N Annex 4) | Compliant | Keep the building ≤300 m² and fuel-free (C5 §4.2) |
| **Toilets and sewer** | 2 accessible restrooms + staff WC | Sanitary units "connected to a working sewer" (FSIB item 1.4); public toilets with treatment where there is no sewer (GD 2404-N §5(է)) | Depends on the plot | FSIB written clarification on a treatment unit (C5 gap 12) |
| **Food-safety design** | Staff room with lockers; 2 hand-wash sinks; 3-compartment sink | Changing room; separate hand-wash sinks with hot water; washable surfaces (C5[14][35]) | Compliant in concept | Specify washable finishes in the kitchen and bar |
| **Queue on the road** | 12.5-car stack + 5.5 behind the order points | No waiting or selling on the carriageway or shoulder (Law on Highways Art. 10(6)) | Depends on throughput | §5.3–5.4 |

### 13.4 Recurring compliance calendar (from opening)

| Frequency | Item | Source |
|---|---|---|
| Daily | HDM/e-HDM receipt for every sale; HACCP logs; product-mark scanning on resale | C4[1] Art. 381; C5 §3.2 |
| Monthly | Wages paid by the 15th of the following month; payslips on request | C3[S1] Art. 192–193 |
| Quarterly | **TT return and payment by the 20th of the following month**; community catering duty | C4[1] Art. 259–262; C5[18] |
| Half-yearly | **Medical books renewed**; roadside board technical inspection; property tax (1 Jun, 1 Dec; 0.3% of building cadastral value + land) | C5[16]; C5[2]; C4[1] Art. 229, 236 |
| Annually | TT/VAT regime choice by 20 Feb; board repainting; HACCP plan review; FSIB inspection readiness (≤1 a year if high risk); after-24:00 permit only if needed | C4 §3.5; C5[2][30] |
| Event-driven | FSIB notified of changes **within 3 days**; catering TT declaration within 20 days of passing AMD 115M | C5[10] Art. 17; C4[1] Art. 254(7) |
| Watch list | e-HDM sector decision (2027); HO-98-N HACCP guidelines; GD 596-N amendments (Apr, Jul, Oct 2026); EIA Law (4 amendments in 2026); health-insurance draft 10624 | C5 §3.10; C4 gap 10; C3[S7] |

### 13.5 Employment and tax set-up checklist

- **Structure:** LLC OpCo on **catering turnover tax** (C4 §3.11).
  - Retail, roastery or franchise activity goes in a separate VAT company.
  - Dividends: a resident HoldCo pays 0%; individuals pay 5% (C4[1] Art. 123(2)(1), 150(8)).
- **Documented expenses.** Payroll, rent, utilities and marketing must be documented to count toward the 9% TT deduction (C4 §3.5).
  - Capex and repairs on fixed assets do not count.
  - Get a written SRC clarification on whether wages and rent paid to an individual are deductible (C4 gap 1).
- **Payroll:**
  - withheld from the employee: income tax 20%; funded pension 5% (≤AMD 500k); stamp duty AMD 1,000; health insurance AMD 4,800 (gross AMD 200–500k);
  - **no employer contribution in 2026** (C3 §1.5);
  - 10% income tax withheld on rent paid to an individual landlord (C4[1] Art. 150(7)).
- **Employment contracts:**
  - digital-system contracts from 1 Jul 2027;
  - 3-month probation;
  - no rolling fixed-term contracts (they convert to open-ended; C3[S1] Art. 95);
  - summarised working-time accounting is written into contracts only where shifts exceed 8 h.

---

## 14. Month-by-month roadmap (M1 = Nov 2026)

### 14.1 Stage gates (investment committee)

| Gate | When | Pass criteria (ASSUMPTION, built on the cited evidence) | If failed |
|---|---|---|---|
| **G0: Validate** | End of M3 (Jan 2027) | Winter counts and the Coffee House observation support **≥120 tx/day** on a realistic capture (C6 §3.6: 0.3–1.3% of same-side light vehicles, base 0.7%). Survey shows stated drive-thru use and an acceptable ticket (A5 gap list). Gross-versus-net payroll question answered (C3) | Re-site to an interchange or urban-edge site (C5 Scenario A; A5 hybrid 50–60%) or to a smaller format |
| **G1: Secure** | M6 (Apr 2027) | MTAI/Police comfort letter on right-in/right-out access; designation path confirmed (community and interagency); MoE EIA screening opinion; Sevan GIS clear | Let the land option lapse |
| **G2: Commit capex** | M12.5 (Oct 2027) | EIA consent (or not required); APA issued; **summer 2027 counts** confirm G0; fixed-price construction bids within budget; POS/e-HDM demo passed; supplier contracts signed | Hold construction; re-bid or re-site |
| **G3: Open** | M19 (May 2028) | Operating permit; FSIB registration with HACCP plan; HDMs registered; team certified; dry runs hit ≥60 cars/h and ≤90 s drinks | Delay the soft launch, not the safety steps |
| **G4: Prove** | M25 (Nov 2028) and M30 (Apr 2029) | 6- and 12-month KPIs against targets (§14.5); unit-2 gates in `strategy/risk-expansion.md` | Fix or reformat unit 1 before any expansion |

### 14.2 Month-by-month plan

| Month | Calendar | Workstream actions |
|---|---|---|
| **M1** | Nov 2026 | LLC + TT declaration; trademark filing; brief the field team; **winter traffic counts start** (ATC on both carriageways at 3–5 candidate sites; B1 §5 protocol as cited by C6/A5); mystery shopping (Coffee House M4 drive-thru, Max Cafe km 12.2, Cofix, Surf, FEIN: menu boards, ticket, timings; C2 gap 15, A4 gap list); permit trail of the Coffee House Ptghni drive-thru via cadastre and community records (C5 §4.9) |
| **M2** | Dec 2026 | **Coffee House drive-thru 5-day observation** (3 weekdays + 2 weekend days × 3 dayparts; cars/h, service time, queue; licence-plate direction sampling; C6 gap list); intercept survey fieldwork starts (**n ≥ 600**, Yerevan + Kotayk + Gegharkunik, quotas by age and car ownership; drive-thru use, acceptable wait, Van Westendorp price ladder; A4/A5 gaps); supplier RFQs out (roasters, dairies, frozen pastry, Oval Pack, The Horeca/DR HORECA); call 5 employers on the gross/net pay question (C3 §5) |
| **M3** | Jan 2027 | 2–3 focus groups (Abovyan/Charentsavan/Hrazdan commuters; weekend Sevan drivers); site shortlist and **due diligence**; **MTAI/Roads Department pre-consultation opens**; **Gate 0** |
| **M4** | Feb 2027 | **Conditional land option**; MoE written opinion on the EIA trigger requested; FSIB written view on the sewer/treatment unit; bank acquiring tender issued |
| **M5** | Mar 2027 | **Designation-change file submitted** (GD 1918-N); junction design + traffic scheme + road-safety audit begin; POS vendors shortlisted |
| **M6** | Apr 2027 | MTAI/Police comfort letter; **Gate 1** → exercise the land option; concept design frozen against the §13.3 fixes |
| **M7** | May 2027 | Interagency commission / council decision on designation; MTAI + Police agreement on the junction; roaster and dairy contracts negotiated |
| **M8** | Jun 2027 | **EIA notification** (if required) → community hearing (working day 21–25); building design starts |
| **M9** | Jul 2027 | **Summer traffic counts** + Coffee House summer observation; APA requested (utility technical conditions) → ENA application; optional 2-week **pop-up price test** at an M4 fuel forecourt (A4 gap list; needs its own catering permit, FSIB registration and HDM; ASSUMPTION on feasibility) |
| **M10** | Aug 2027 | Council consent vote on the EIA (≤30 working days); APA special-regulation coordination; **POS/e-HDM live demo (gate)** |
| **M11** | Sep 2027 | EIA expertise (≤40 working days); construction tender (fixed price); equipment specification and quotes; trademark status check |
| **M12** | Oct 2027 | EIA conclusion (≈M14 if the +30 working days of expertise are used, which moves the permit and everything after it); bank tender closed; **Gate 2** |
| **M13** | Nov 2027 | **Design approval + construction permit (AMD 15,000)**; start notice; earthworks and foundations; speed-change-lane works agreed with the road body |
| **M14** | Dec 2027 | Building shell; off-site fabrication of the canopy and bar joinery (winter construction risk; ASSUMPTION); equipment ordered (EU spec) |
| **M15** | Jan 2028 | **Store manager hired**; HACCP consultant engaged; utilities connection works; signage artwork (Armenian first) approved; trademark must be registered before fabrication |
| **M16** | Feb 2028 | **Shift leads hired** (cook-qualified); advertising-board permit filed (30 days); app/loyalty build on the POS platform; Maps and OSM pre-listing |
| **M17** | Mar 2028 | **Crew, cooks and part-timers recruited** (job.am, staff.am, colleges); medical books; digital contracts; HACCP plan drafted; equipment installation; paving and lanes |
| **M18** | Apr 2028 | Training academy (3–4 weeks); tech installation (HDM registration with SRC, KDS, headsets, boards); boards installed; construction completes (≈M18.5); **acceptance commission** |
| **M19** | May 2028 | **Final act + operating permit → FSIB registration (with HACCP plan) → community catering permit** → dry runs → **soft launch** (2 weeks, 07:00–21:00, limited menu) → full hours |
| **M20** | Jun 2028 | **Grand opening**; summer roster; partner offers live |
| **M21–M22** | Jul–Aug 2028 | Summer peak: overflow protocol, daily pars, ice and milk buffers; **90-day review (M22)**: speed, accuracy, waste, menu engineering (drop low-margin items such as bought-in gata at 58% COGS, C2 §3.4) |
| **M23** | Sep 2028 | Shoulder hours; commuter campaign; first loyalty cohort analysis |
| **M24** | Oct 2028 | Winter readiness: snow-clearing contract; heated windows and boards checked; winter menu (herbal tea, hot chocolate; A4 §3.6); winter roster |
| **M25** | Nov 2028 | **6-month gate (G4a)**; **first medical-book renewals** for the opening team; staff-retention review |
| **M26–M29** | Dec 2028–Mar 2029 | Winter trough (model index 0.66–0.82): Case B roster at winter hours; cross-training; equipment preventive maintenance; New Year offers |
| **M30** | Apr 2029 | **12-month review (G4b)**: unit-economics restatement; season-2 plan; unit-2 decision per `risk-expansion.md` |

### 14.3 Gantt summary (critical path in bold)

| Task | Start month | Duration (months) | Owner |
|---|---|---|---|
| Company set-up, TT declaration, trademark filing | 1 | 1 | Founder / legal |
| Trademark examination to registration | 1 | 14 | IP attorney |
| **Winter traffic counts + Coffee House drive-thru observation** | **1** | **3** | **Strategy / field team** |
| Mystery shopping and receipt sampling | 1 | 2 | Ops lead |
| Intercept survey (n ≥ 600) + focus groups | 2 | 2 | Marketing |
| Supplier RFQs, bank tender, POS demos | 2 | 9 | Ops / procurement |
| **Gate 0** | **3.5** | **0.5** | **Board** |
| **Site due diligence** | **3** | **1.5** | **Real estate** |
| **MTAI / Police access pre-consultation** | **3** | **3** | **Road designer** |
| **Conditional land option → Gate 1 exercise** | **4** | **3** | **Real estate / legal** |
| MoE EIA screening opinion; FSIB sewer view | 4 | 2 | Permitting agent |
| **Land-designation change** | **5** | **3** | **Permitting agent** |
| **Junction design, road-safety audit, MTAI + Police agreement** | **5** | **3** | **Road designer** |
| **EIA Category B** | **8** | **5** | **Environmental consultant** |
| Building design (category II) | 8 | 3 | Architect |
| APA + special-regulation coordination | 9 | 2 | Architect / permitting |
| Summer traffic counts (+ optional pop-up test) | 9 | 2 | Strategy |
| ENA power and water/sewer connections | 9 | 7 | MEP engineer |
| Construction tender, equipment specification | 10 | 3 | Project manager |
| **Gate 2 + construction permit + start notice** | **12.5** | **1** | **Board / PM** |
| **Construction incl. speed-change lanes** | **13.5** | **5** | **Contractor** |
| Equipment procurement and installation | 14 | 4 | Ops / dealer |
| Store manager hired; HACCP plan | 15 | 3 | Ops lead |
| Advertising permit + board installation | 15 | 3 | Marketing |
| Recruitment (leads, crew, cooks), medical books | 16 | 2.5 | Store manager |
| Tech installation and HDM registration | 17 | 2 | IT / ops |
| Pre-launch marketing | 17 | 2.5 | Marketing |
| Training academy and dry runs | 18 | 1.5 | Training lead |
| **Acceptance → final act + operating permit** | **18.5** | **0.75** | **PM / community** |
| **FSIB registration with HACCP plan; catering permit** | **19.25** | **0.25** | **Store manager** |
| **Soft launch** | **19.5** | **0.5** | **Ops** |
| **Grand opening** | **20** | **0.25** | **Marketing / ops** |
| Summer peak operations + 90-day review | 20 | 3 | Ops |
| Winter readiness and winter operations | 24 | 6 | Ops |
| 6-month gate; medical-book renewals | 25 | 0.5 | Board / store manager |
| 12-month review and unit-2 decision | 30 | 1 | Board |

### 14.4 Scenario variants

| Variant | What changes | Opening |
|---|---|---|
| **Base (this plan)** | Greenfield M4; designation change; EIA triggered | Soft launch **M19 (May 2028)**; grand opening M20, which matches the model's `opening_month` = 5 |
| **Fast track** (C5 Scenario A: interchange or brownfield site, existing designation, access from a local road, <1,000 m² impervious or EIA not applicable) | Steps 4, 5 and 7 drop out; 8–11 months from land control (C5 §3.10) | Open as soon as built, ≈M12–M15 (Oct 2027–Jan 2028). A low-season opening gives 4–7 months to train before the first summer. That is an operational advantage, given the incumbent's failure mode was throughput (A5 §3.5) |
| **Slip** (C5 contingency +6–9 months: commission split, EIA extension, council objection, ENA delay) | Critical path moves to M25–M28 | Opening in Nov 2028–Feb 2029, a winter trough. **Open anyway on the Case B roster at winter hours** to learn and build the loyalty base; hold ≈60% of the launch budget for April–May 2029 (ASSUMPTION) |
| **Fail at G1** | No access comfort letter or designation path | Re-site. A5 and C6 both rank open-highway mid-carriageway pads as the weakest site type |

### 14.5 First 12 months of trading: KPI targets (ASSUMPTION unless cited)

| KPI | M19–M21 (launch) | M22–M24 | M25–M30 | Source of target |
|---|---|---|---|---|
| Transactions/day vs model ramp | Track against `ramp_curve` (base 0.55 → 1.0 over 12 months) | — | — | model (ASSUMPTION) |
| Payroll breakeven check | Hours rostered to the deployment chart | Labour ≤50% of receipts | **Labour ≤35%** or reformat | §4.6 |
| W2 window time, peak | ≤60 s | ≤45 s | ≤45 s | §5.2 |
| Drinks order-to-handoff | ≤150 s | ≤90 s | ≤90 s | C6[5] |
| Visits >10 min | <5% | <2% | <2% | C6[17] |
| Accuracy | ≥93% | ≥96% | ≥96% | C6[17] |
| Food attach | ≥25% | ≥30% | ≥35% | A4 §3.11 (30–45%) |
| Waste | ≤3% | ≤2% | ≤2% | model `waste_pct` |
| Maps rating | ≥4.5★ | ≥4.7★ | ≥4.7★ | §12.2 |
| Loyalty share of transactions | ≥5% | ≥10% | ≥15% | C6 §3.10 (10–30% by year 3) |
| Crew turnover (annualised) | — | ≤80% | ≤60% | C3 (60–100%) |
| FSIB/SRC findings | 0 | 0 | 0 | — |

---

## 15. Open issues to verify (owner → route)

| # | Issue | Why it matters | Route |
|---|---|---|---|
| 1 | Do job ads quote gross or net pay? | ±27% on payroll (C3) | Ops lead calls 5 employers (C3 §5), M2 |
| 2 | Does bake-off reheating and wrap assembly need cook qualification (Art. 12(6))? | Roster cost and hiring pool | Legal counsel + FSIB hotline 118 |
| 3 | Can handheld HDMs take payment in the lane? Is e-HDM mandatory for catering from 2027? | Fiscal fines | SRC written clarification (Tax Code Art. 306) |
| 4 | Pylon: advertising or signboard? | Permit, road tax, the ≥150 m junction rule | MTAI at the access pre-consultation |
| 5 | EIA applicability to private paving; whether speed-change lanes count | 5–7 months and a council veto | MoE expertise centre written opinion on a sketch |
| 6 | M4 category (IB or IC) at the site; connection procedure, fee and deadline; road-safety audit applicability | Critical path | MTAI legal department (C5 gaps 1–2) |
| 7 | Septic/treatment unit vs "connected to sewer" | Plot feasibility | FSIB written clarification |
| 8 | Medical-book and HACCP consultancy prices | Pre-opening budget | 2–3 clinics; 2–3 consultancies (C5 gap 13) |
| 9 | Wholesale coffee, milk and frozen-pastry quotes with M4 delivery | ≈45% of latte COGS is coffee (C2 gap 5) | RFQs, M2–M5 |
| 10 | Idram, Telcell and Google Pay merchant terms | Payment mix and cost | Merchant agreements |
| 11 | Headset dealer and RF approval; LED board integrators | Throughput tech | RFQs (C2 gap 13) |
| 12 | Gift boxes, bottled goods: catering (12%/9%) or "other" (20%)? | TT trap | SRC clarification with a product list (C4 gap 2) |
| 13 | 2026 local duty rates of the actual community | Opex | Community decisions (C4 gap 6; C5 gap 15) |
| 14 | Energy-drink age-of-sale rule | Rebel test line | arlis.am / FSIB (A4 gap) |

---

## 16. Sources used

**Research files.** All in `research/`. Each file's §6 holds the full source list; citations above give the file id and its source number.

| File | Topic | Sources cited here |
|---|---|---|
| **C5-regulations.md** | Regulation | [1] Law on Highways; [2] GD 765-N; [3] GD 2404-N; [4] GD 792-N; [5] ՀՀՇՆ 32-01-2022; [7] GD 596-N; [8] Land Code; [9] GD 1918-N; [10] Food Safety Law; [11] HO-98-N; [13] GD 827-N; [14] GD 1266-N; [15] MoH 31-N; [16] GD 347-N; [17] Law on Trade and Services; [18] Law on Local Duties; [19] Waste law; [20] Law on Advertising; [21] Law on Language; [22]–[26] Sevan and EIA acts; [27] State Duty; [28] Water Code; [30] Law on Inspections; [31] hartak.am; [32]–[35] snund.am; [36] Law on Trademarks |
| **C3-labor.md** | Labour | [S1] Labour Code; [S3] Minimum-wage law; [S4] Holidays law; [S7] e-draft 10624; [S22] Armstat population; [S23] CBA; [S24] job.am; [S25] job.am pricing; ads P1–P30 |
| **C2-equipment-supply.md** | Equipment and supply | [S1] CBA; [S2]/[S3] The Horeca; [S6] EAEU tariff; [S24] CBA Decision 27-N; [S26] FastBank; [S27]/[S28] Ameriabank; [S30] Apple Pay; [S31] Idram; [S32] e-HDM; [S33] HDM prices; [S34] Poster; [S35] iiko; [S36]–[S45] supplier price sources |
| **C6-benchmarks.md** | Benchmarks | [1]–[3] Dutch Bros; [5]/[6] Black Rock; [16]–[19] Intouch Insight; [20]/[21] Palm Beach County ITE tables and queuing code |
| **A4-food-preferences.md** | Food | [19]–[22] SAS catalogue; [26a] Ashtarak Kat; [39] aflatoxin study; menu and supplier sections |
| **A5-drivethru-cultural-fit.md** | Cultural fit | [14]/[15] McDonald's/Vkusno i tochka; [24]/[25] Starbucks/Dunkin'; [27] Sevan climate; [32] OSM drive-thru extraction; A3/A1 items as cited there |
| **C4-tax.md** | Tax | [1] Tax Code (Art. 59, 122, 171, 190, 229, 254–262, 380–381, 416); [6] HO-309-N; [11] GD 125-N marking; [13] State Duty; [17] e-register; [20] WIPO |

**Project files:**
- `design/layout.json`: geometry, stack capacity, equipment, windows, lane lengths;
- `model/assumptions.json`: hours, seasonality, ramp, card fee, waste, launch budget; several are PLACEHOLDER;
- `brand/naming-report.md`: the ritual and the trademark notes.

**Calculation scripts:** `roster2.py` and the stack and volume calculations, kept in the session scratchpad. All formulas are shown in §4.5, §4.6, §5.3 and §7.2.
