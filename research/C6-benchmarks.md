# C6 — US and international drive-thru operating benchmarks (design and financial calibration)

*Workstream C6 of the premium drive-thru coffee & food feasibility study (Armenia). Prepared 2026-10-10. USD figures are as reported. AMD conversions use the CBA rate of **AMD 361.93/USD** (9 Oct 2026, from workstream A1). Note: `model/assumptions.json` still carries a placeholder of 385.*

**Status tags.**
- **VERIFIED**: a primary or official source that I opened myself (SEC filing, company website, government document); URL given.
- **REPORTED**: a credible secondary source (news, industry study, franchisor marketing page); URL given.
- **ESTIMATE**: my own calculation; formula and inputs shown.
- **ASSUMPTION**: my judgement; basis explained.

> **Method note and limitation (read first).** The shared WebSearch budget for this session was already used up when this workstream started, so **no keyword search could be run** (English, Armenian or Russian). Every figure below comes from a source opened directly at a known address:
> - SEC EDGAR filings: Dutch Bros, Black Rock Coffee Bar, Starbucks, McDonald's, Restaurant Brands International (RBI) and Dunkin' Brands.
> - Company and franchisor websites: Scooter's, 7 Brew, Ziggi's, The Human Bean and the Chick-fil-A newsroom.
> - Intouch Insight drive-thru study pages (2025 and 2026).
> - Palm Beach County (Florida) trip-generation table built from ITE's Trip Generation Manual, plus its land-development code. These are the only public copies of ITE rates I could reach; ITE itself is paywalled.
> - delo.ua (WOG coffee volumes).
> - Sibling workstreams A1–A3, B1, B4, C1 and C3.
>
> Several items in the brief therefore **could not be verified** and are listed in §5 with a verification route: Starbucks' drive-thru share of transactions and revenue, store sizes and average ticket; 7 Brew's kiosk size and AUV; Tim Hortons highway sites; ITE Trip Generation Handbook pass-by tables; OKKO and Circle K cups per station; and brand-level QSR Magazine times. **None of these is filled in from memory.**

---

## 1. Executive summary

1. **Mature US coffee drive-thrus run at 25–31% shop-level margin on US$1.0–2.2 M per unit, which is roughly 3–10× an Armenian unit's likely sales.**
   - **Dutch Bros:** systemwide AUV **US$2.115 M** (FY2025) and **US$2.193 M** (trailing twelve months, TTM, to Q2 2026). Company-operated shop contribution **28.9%** (FY2025) and **30.6%** (Q2 2026) (VERIFIED, 10-K / earnings release).
   - **Black Rock Coffee Bar:** AUV **US$1.286 M**; store-level margin **29.2%** (FY2025) (VERIFIED).
   - **Scooter's Coffee:** franchised kiosks average **US$998,869** in sales and **US$134,457 EBITDA** (FY2025, Item 19 summary; REPORTED). That is **≈13.5% of sales** (ESTIMATE: EBITDA ÷ sales). The franchisor reports an average net profit margin of 14.6%. *Fact-check correction: 13.5% is my ratio of the two averages, not a reported margin. The pages opened do not say whether EBITDA is stated after the 6% royalty and 2% marketing fee, so that premise is an ASSUMPTION until the FDD Item 19 is read.*
   - At A2's 80–150 transactions/day and a 2,600 AMD ticket, an Armenian unit turns over roughly **US$0.2–0.4 M a year** (ESTIMATE). Fixed-cost leverage, and therefore margin, will be lower than in the US.
2. **The US cost structure of a beverage-led drive-thru is consistent across chains (all VERIFIED):**

   | Cost line (% of sales) | Dutch Bros FY2025 | Black Rock FY2025 |
   |---|---|---|
   | Beverage, food & packaging | 25.9% (26.1% in Q2 2026) | 28.1% |
   | Labor | 26.9% | 21.0% |
   | Occupancy | 16.6% (incl. "other") | 8.0% occupancy (rent + CAM + real-estate taxes) + 13.6% other store opex |
   | Advertising | 1.3–2.4% of sales (both chains) | |

   **Food raises cost of goods sold (COGS).** Dutch Bros says its new 2026 food program "typically carr[ies] a higher cost margin than beverages", which added to an 80 bp rise in COGS (VERIFIED, Q2 2026 10-Q).
3. **The leaders win on throughput design, not building size.**
   - Dutch Bros builds **800–1,000 sq ft (74–93 m²)** shops on lots of **≥25,000 sq ft (≈2,320 m²)**, with "multiple drive-thru lanes served by one window", "ample car stacking", an escape lane, a walk-up window and **runners with tablets** (VERIFIED).
   - Scooter's: **664 sq ft (62 m²)** kiosk, **≥½-acre (≈2,020 m²)** pad and a **minimum 10-car stack**. Scooter's **only takes roads at or below 45 mph (72 km/h)** (REPORTED).
   - Black Rock targets **~90 seconds order-to-handoff** (VERIFIED).
4. **Speed and accuracy benchmarks (Intouch Insight 2026, published 1 Oct 2026; 2,145 visits; REPORTED).**
   - Average visit **5:24 (324 s)**, service time **4:04**, window time **1:40**. Order accuracy **89.3%**.
   - Beverage brands lead on accuracy: **Starbucks 96%** and **Dutch Bros 94%**. Tim Hortons is fastest at **4:20**.
   - Satisfaction falls to **84.9% once a visit passes 10 minutes**. It is **42.9% when the lane "felt frustrating"**.
   - The Armenian M4 incumbent's 20–60-minute waits (A3) are therefore a measurable weakness that a challenger can attack.
5. **The design stack is 10–12 cars, and the service rate matters more than lane length.**
   - Palm Beach County code requires **7 queue spaces (≥4 before the menu board) + 1 after the window**, at 10×20 ft each, with a ≥10 ft bypass lane, which Table 6.B.3.A requires for every drive-through restaurant (VERIFIED). Scooter's requires ≥10 cars.
   - Queueing maths (M/M/1 model; ESTIMATE): at 45 cars/h arriving, a 60 cars/h window needs **10 places** to hold the queue 95% of the time. A 50 cars/h window needs **28**.
   - **Design for ≥60 cars/h (≤60 s per car at the window) and 10–12 stacked cars.** Do not try to fix slow service with asphalt.
6. **ITE trip rates (12th edition, via Palm Beach County, May 2026; VERIFIED as the county's adopted table, REPORTED as ITE data).**
   - **Land use 937 (coffee/donut shop with drive-through):** **600.5 trips/day per 1,000 sq ft**; AM peak 85.41, PM 39.00.
   - **Land use 938 (drive-through only, no seating):** **179 trips/day per drive-through lane**; AM peak 39.81.
   - **14% (937) to 22% (938) of daily trips fall in the single AM peak hour** (ESTIMATE). Coffee demand is far more peaked than traffic (≈6% peak-hour share on Yerevan arterials, B4).
7. **Capture-rate benchmark (ESTIMATE, wide band).**
   - **US mature:** a 2,000 sq ft land use 937 shop on a 20–40k AADT road converts **≈0.7–2.7% of passing vehicles as pass-by trips** (central ≈1.5%), and ≈1.5–3% including destination trips.
   - **Armenia:** after adjusting for a nascent drive-thru habit, a lower income-to-price ratio, and 90 km/h highway speeds, a defensible **mature** capture is **0.3–1.3% of same-side light vehicles on the M4** (base ≈0.7%) and **0.5–1.1% on urban-edge arterials** (base ≈0.75–0.8%).
   - **The model's base input (1.8% of AADT × 0.55) equals ≈2.4% of same-side light vehicles.** That is above the US-mature central value and should be cut to ≈0.6% (≈0.8% of same-side light vehicles) unless field counts at the Coffee House M4 drive-thru justify more.
8. **Regional fuel-station coffee is a sobering cross-check.** WOG (Ukraine, ~500 stations) sold **≈150 M coffee portions in 7 years** (delo.ua, Oct 2020; REPORTED). That is **≈117 cups per station per day** (ESTIMATE) at a captive fuel stop. In A2: the Russian Coffee Like car-pavilion format claims ≈103 checks/day; Coffee House averages ≈40–70 cups per branch per day.
9. **Menu mix.**
   - Beverages dominate: Starbucks company-operated sales are **73% beverages / 23% food / 4% other** (FY2025). Dunkin' U.S. was **58% coffee and beverages** (FY2019). Dutch Bros: **~50% coffee, ~25% energy, ~25% other** (2025). Black Rock: Fuel energy drinks are **~24% of revenue** (all VERIFIED).
   - **The ~25% energy-drink share does not transfer to Armenia.** Retail energy cans cost 280–990 AMD, health framing is negative and a minors issue exists (A4).
10. **Strategic signals from the leaders cut both ways.**
    - Starbucks' FY2024 10-K said it was expanding "particularly drive-thru formats". **The FY2025 10-K drops that wording.** Starbucks closed **627 stores in Q4 FY2025** and announced **~250 more North American closures in Sept 2026** under "Back to Starbucks". It raised labor hours. The North America margin fell from **19.8% to 11.5%**: about 3.1 pts deleverage, 2.4 pts restructuring and 1.8 pts "Back to Starbucks" investment, largely labor (VERIFIED). US comparable transactions turned positive in FY2026 (+3% to +4.3% per quarter).
    - McDonald's says the "vast majority" of new US openings will have a drive-thru (nearly 29,000 drive-thrus worldwide; VERIFIED).
    - Dutch Bros agreed to buy up to **65 Salad and Go drive-thru sites** (Aug 2026; VERIFIED).
    - **Lesson:** drive-thru real estate is valued, but hospitality and a walk-up or seating option matter. Black Rock has lobbies at **73%** of stores.
11. **Capex benchmarks are a ceiling, not a target.**
    - Black Rock: **US$860k per new store** (US$650k net of landlord allowances) in 2025.
    - Scooter's kiosk: total investment **US$1.16–1.35 M**.
    - Dutch Bros: ≤US$1.71 M per opening (C1).
    - **Black Rock targets ~40% cash-on-cash** at month 18 on a US$1.1 M AUV and ≥22% margin.
    - **In Armenia, sales will be about 1/5–1/10 of these units and payback will be much slower.** Capex has to be cut in proportion, not just by the C1 ratio (≈0.3–0.5× US).

---

## 2. Key data table

| # | Metric | Value | Period | Status | Source |
|---|---|---|---|---|---|
| 1 | Dutch Bros systemwide AUV / company-operated AUV | US$2.115 M / US$2.061 M | FY2025 | VERIFIED | [1] |
| 2 | Dutch Bros AUV (new TTM definition) systemwide / company-op | US$2.193 M / US$2.164 M | TTM to 30 Jun 2026 | VERIFIED | [2] |
| 3 | Dutch Bros shop count; openings | 1,136 (811 co-op, 325 franchise); 154 opened in 2025; 1,225 at 30 Jun 2026; ≥185 planned 2026 | Dec 2025 / Jun 2026 | VERIFIED | [1][2] |
| 4 | Dutch Bros co-op P&L (% of shop revenue) | Beverage, food & packaging 25.9; labor 26.9; occupancy & other 16.6; pre-opening 1.7; D&A 7.0; shop contribution 28.9 | FY2025 | VERIFIED | [1] |
| 5 | Same, Q2 2026 | 26.1 / 25.4 / 16.3 / 1.6 / 6.4; contribution 30.6 | Q2 2026 | VERIFIED | [2] |
| 6 | Dutch Bros long-run margin target | Co-op contribution ~30% | 2026 | VERIFIED | [1] |
| 7 | Dutch Bros drive-thru share of business | ~85% drive-thru, ~15% walk-up | 2025 | VERIFIED | [1] |
| 8 | Dutch Bros shop formats | Legacy ~500 sq ft; current ~800–1,000 sq ft (multiple lanes, one window, escape lane, walk-up); end-cap ~1,000–1,200 sq ft | 2025 | VERIFIED | [1] |
| 9 | Dutch Bros target lot | ≥25,000 sq ft (≈2,323 m²) | 2025 | VERIFIED | [1] |
| 10 | Dutch Bros menu mix (% of 2025 sales) | Coffee ~50%; Rebel energy ~25%; refreshments & other (incl. food) ~25% | 2025 | VERIFIED | [1] |
| 11 | Dutch Bros loyalty share of transactions | 72% (2025); 74% (H1 2026) | 2025–26 | VERIFIED | [1][2] |
| 12 | Dutch Bros pre-opening cost per new shop; capex per opening | US$180k; ≤US$1.71 M (US$241.1 M ÷ 141) | FY2025 | VERIFIED / ESTIMATE | [1], C1 |
| 13 | Dutch Bros advertising | US$39.0 M = 2.4% of total revenue; shop-level US$26.3 M = 1.7% of co-op revenue | FY2025 | VERIFIED + ESTIMATE | [1] |
| 14 | Dutch Bros food effect on COGS | Food "typically carr[ies] a higher cost margin than beverages"; COGS +80 bp y/y | Q2 2026 | VERIFIED | [3] |
| 15 | Dutch Bros transactions/day (implied) | ≈680–830 | FY2025 | ESTIMATE (AUV ÷ 365 ÷ assumed US$7.0–8.5 ticket; ticket not disclosed) | [1] |
| 16 | Black Rock AUV; store-level margin; Adj. EBITDA margin | US$1.286 M; 29.2%; 13.7% | FY2025 | VERIFIED | [5] |
| 17 | Black Rock store costs (% of total revenue) | Beverage, food & packaging 28.1; labor 21.0; occupancy 8.0; other store opex 13.6 | FY2025 | VERIFIED | [5] |
| 18 | Black Rock new-store investment | US$860k gross, ~US$650k net of TI allowances | 2025 | VERIFIED | [5] |
| 19 | Black Rock new-unit targets at 18 months | AUV US$1.1 M; store margin ≥22%; net capex US$0.6 M; cash-on-cash ~40% | Sep 2025 | VERIFIED | [6] |
| 20 | Black Rock service-time target; formats | ~90 s order-to-handoff; 100% have a drive-thru, 73% have lobbies; dual-lane + dual-bar can support >US$3 M | FY2025 | VERIFIED | [5] |
| 21 | Black Rock Fuel energy drinks share; digital; loyalty | ~24% of revenue; 16% of store revenue (Q4 2025); 63% of sales | FY2025 | VERIFIED | [5] |
| 22 | Starbucks company-operated sales mix | Beverages 73%, food 23%, other 4% | FY2025 | VERIFIED | [7] |
| 23 | Starbucks North America P&L | Product & distribution 27.9% of NA revenue; store opex 56.4% of NA co-op revenue (51.4% FY2024); NA operating margin 11.5% (19.8% FY2024); 13.6% in Q3 FY2026 | FY2025, Q3 FY2026 | VERIFIED | [7][9] |
| 24 | Starbucks US co-op stores; restructuring closures | 10,047 US co-op (Sep 2025); 627 closed in Q4 FY2025; ~1% of >18,000 NA (~250) to close in FY2026 | FY2025–26 | VERIFIED | [7][12] |
| 25 | Starbucks US comparable transactions | −4% FY2025; +3% Q1, +4.3% Q2, +4.2% Q3 FY2026 | FY2025–26 | VERIFIED | [7][10] |
| 26 | Starbucks advertising | US$869.5 M = 2.3% of total revenue (US$37,184 M) | FY2025 | VERIFIED + ESTIMATE | [7] |
| 27 | Starbucks drive-thru share of US transactions/revenue; store sizes; average ticket | **Not disclosed in any filing opened**; not verified | — | GAP | §5 |
| 28 | Scooter's franchised kiosk Item 19 (621 reporting) | Avg gross sales US$998,869; avg EBITDA US$134,457 (13.5%); net margin 14.6%; top quartile US$1,433,875 / US$273,683 (19.1%) | CY2025 | REPORTED (franchisor site citing FDD Item 19) | [23] |
| 29 | Scooter's kiosk design and site criteria | 664 sq ft (62 m²); pad ≥½ acre; ≥10-car stack; road speed ≤45 mph; 10-min drive-time pop ≥10,000; ≥6 staff parking | 2026 | REPORTED | [23] |
| 30 | Scooter's investment and fees | Kiosk US$1.16–1.35 M; end-cap US$0.66–1.07 M (incl. US$40k fee); royalty 6%; marketing 2% | 2026 FDD | REPORTED | [23] |
| 31 | 7 Brew scale | 700+ stands in 38 states; >1 M drinks/day; ~60 crew per stand; no third-party delivery | 2026 | REPORTED (company site) | [24] |
| 32 | 7 Brew drinks per stand per day | ≈1,260–1,430 | 2026 | ESTIMATE (1 M ÷ 700–792 stands) | [24] |
| 33 | Ziggi's | 100+ locations; investment US$0.56–2.0 M; café + DT, double-sided DT, single-sided DT models | 2026 | REPORTED | [25] |
| 34 | Dunkin' U.S. (pre-Inspire) | >50% of 9,630 US points with drive-thru; 58% of sales coffee & beverages; free-standing 1,200–2,500 sq ft; ad fund 5%; royalty 5.9% | FY2019 | VERIFIED | [15] |
| 35 | McDonald's drive-thru footprint | ~29,000 drive-thrus globally; >95% of ~13,700 US restaurants | FY2025 | VERIFIED | [13] |
| 36 | Tim Hortons | 4,586 restaurants in US & Canada; US$8.248 B global system sales; fastest drive-thru in 2026 study (4:20) | FY2025 / 2026 | VERIFIED / REPORTED | [14][17] |
| 37 | Chick-fil-A peak throughput | "Most" restaurants "sometimes serving over 100 cars per hour" at peak; tablet "Face-to-Face Ordering" | Mar 2021 | VERIFIED (company newsroom) | [27] |
| 38 | Chick-fil-A Elevated Drive-Thru | 4 lanes; 2–3× the vehicles of a standard drive-thru; kitchen 2× larger | Aug 2024 | VERIFIED | [27] |
| 39 | Intouch 2026: total / service / window time | 5:24 / 4:04 / 1:40; median <4:25; slowest 10% ≥9:56 | Jun–Jul 2026 | REPORTED | [16][17] |
| 40 | Intouch 2026: accuracy; satisfaction | 89.3% (Starbucks 96%, Dutch Bros 94%); 93.8% (Starbucks 99%) | Jun–Jul 2026 | REPORTED | [17] |
| 41 | Intouch 2025: lanes; cars in line; service time | 79% single lane, 20% two, 1% three; average cars in line 1.20; 4:15 | Jun–Jul 2025 | REPORTED | [18][19] |
| 42 | ITE 937 (coffee/donut + DT) | 600.50 trips/day per 1,000 sq ft; AM peak 85.41; PM 39.00 (12th ed.); 11th ed.: 533.57 / 85.88 / 38.99 | 12th ed. (2025) | VERIFIED (county table reproducing ITE) | [20] |
| 43 | ITE 938 (DT only, no seating) | 179 trips/day per DT lane; AM 39.81; PM 15.08 | 11th/12th ed. | VERIFIED (as above) | [20] |
| 44 | Pass-by % applied by Palm Beach County | 49% for 934, 937, 938; 61% for gas station with convenience store | May 2026 | VERIFIED (county policy, not ITE Handbook) | [20] |
| 45 | Coffee AM-peak-hour share of daily trips | 937: 14.2%; 938: 22.2%; fast food 934: 7.4% | ITE 12th ed. | ESTIMATE (AM rate ÷ daily) | [20] |
| 46 | Drive-through queuing code (Palm Beach County) | Restaurant: 7 spaces (≥4 before menu board) + 1 after window; 10×20 ft each; window space 9×20 ft; bypass ≥10 ft if >5 spaces; right-turn radius 25–30 ft | Supp. 32 (Oct 2025) | VERIFIED | [21] |
| 47 | WOG (Ukraine) coffee volume | ~150 M portions in 7 years; ~500 stations; ≥€10 M invested | Oct 2020 | REPORTED | [28] |
| 48 | WOG cups per station per day | ≈117 (2014–2020 average) | 2014–20 | ESTIMATE (150 M ÷ 7 ÷ 365 ÷ 500) | [28] |
| 49 | Recommended Armenian capture (mature), same-side light vehicles | M4 highway 0.3–1.3% (base ≈0.7%); urban edge 0.5–1.1% (base ≈0.75–0.8%) | 2026 | ESTIMATE / ASSUMPTION | §3.6 |
| 50 | Model base capture expressed on the same basis | ≈2.4% of same-side light vehicles (1.8% × 0.55 ÷ 0.41) | model v. Oct 2026 | ESTIMATE | assumptions.json, B1 |

---

## 3. Detailed findings & analysis

### 3.1 Why these benchmarks matter, and the basis of comparison

The model's revenue driver is passing vehicles × capture × ticket. Its cost lines are percentages of sales plus fixed costs. US filings give three things that can be transferred, with care:
1. **Ratios**: COGS, labor, occupancy, marketing and shop-level margin.
2. **Physical design norms**: building m², lot, lanes, stacking, windows and service time.
3. **Demand-shape facts**: peak-hour share, beverage/food mix and capture logic.

US **levels** do not transfer: AUV, transactions/day, ticket and capex. Each benchmark below is tagged with whether it transfers (§3.10).

Definitions differ, so compare with care:
- **Dutch Bros "shop contribution"** = revenue − beverage/food/packaging − labor − occupancy & other − pre-opening. It excludes D&A and all corporate overhead. Excluding pre-opening, the four-wall margin was **30.6%** in FY2025 (ESTIMATE: 100 − 25.9 − 26.9 − 16.6).
- **Black Rock "store-level profit"** excludes D&A and pre-opening [5].
- **Scooter's Item 19 "EBITDA"** is a franchisee figure *after* the 6% royalty and 2% marketing fee [23]. On a company-operated basis it is roughly **21.5%** for the average kiosk (ESTIMATE: 13.5% + 8%).
- **Starbucks segment operating margin** is after D&A, segment G&A and restructuring, so it is not a four-wall figure.

### 3.2 Company benchmarks

#### 3.2.1 Dutch Bros (the closest "American drive-thru" archetype) [1][2][3][4]

| Item | Value | Status |
|---|---|---|
| Shops | 1,136 at 31 Dec 2025 (811 co-op); 1,225 at 30 Jun 2026 | VERIFIED |
| AUV | US$2.115 M systemwide, US$2.061 M co-op (FY2025, shops open ≥15 months); US$2.193 M TTM Q2 2026 (new definition) | VERIFIED |
| Average daily sales | ≈US$5,795 systemwide AUV ÷ 365; co-op shops averaged US$40.1k per operating week (US$1,509.3 M ÷ 37,667 weeks), ≈US$5,720/day | ESTIMATE |
| Same-shop sales (co-op) | +7.4% FY2025 (ticket +2.0%, transactions +5.4%); +8.3% Q2 2026 (ticket +4.9%, transactions +3.4%) | VERIFIED |
| Channel | ~85% drive-thru, ~15% walk-up; "vast majority" have no lobby | VERIFIED |
| Throughput tools | "Runner" with tablet takes orders down the line; escape lanes let customers leave after the runner delivers; order-ahead in >95% of shops (2024) | VERIFIED |
| Shop size | ~800–1,000 sq ft current format (≈74–93 m²); ~500 sq ft legacy; lots ≥25,000 sq ft | VERIFIED |
| Sales density | ≈US$23–29k per m² of building per year (US$2.115 M ÷ 74–93 m²) | ESTIMATE |
| Menu mix (2025 sales) | Coffee ~50%, Rebel energy ~25%, teas/lemonades/smoothies/sodas/food ~25%; food program expanding in 2026 for the morning daypart | VERIFIED |
| Seasonality | Higher nominal sales in summer, so Q2–Q3 margins are higher | VERIFIED |
| Costs FY2025 (% co-op revenue) | COGS 25.9, labor 26.9, occupancy & other 16.6, pre-opening 1.7, D&A 7.0 → contribution 28.9% (FY2024: 29.7%) | VERIFIED |
| Advertising | 1.7% of co-op revenue at shop level; 2.4% of total revenue all-in | ESTIMATE from VERIFIED |
| Real estate | Build-to-suit (15-yr) and ground leases (20-yr); occupancy rising "as we shift… to a greater proportion of build-to-suit"; acquiring up to 65 Salad and Go sites (Aug 2026) | VERIFIED |
| Queue risk | 10-K risk factor: long lines "may lead to negative perceptions from neighboring businesses and residences… difficulties in obtaining or maintaining required permits" | VERIFIED |

*Interpretation.* Dutch Bros proves that a ~90 m² building with no seating can produce >US$2 M a year. The **lot and the lane system are the real asset**: ≥2,300 m² for a ~90 m² building, about 25:1. Its ~85% drive-thru dependence shows what a mature drive-thru habit looks like. Armenia does not yet have that habit.

#### 3.2.2 Black Rock Coffee Bar (IPO Sept 2025; drive-thru + lobby hybrid) [5][6]

| Item | Value | Status |
|---|---|---|
| Stores | 181 (7 states), 100% company-operated; 73% with lobbies; 36 openings planned for 2026 | VERIFIED |
| AUV | US$1.286 M (FY2025, comparable base = stores open ≥18 months); US$1.186 M FY2024 | VERIFIED |
| Average daily sales | ≈US$3,436 (US$200.1 M ÷ 8,319 store-weeks ÷ 7) | ESTIMATE |
| Store P&L (% total revenue) | COGS 28.1; labor 21.0; occupancy 8.0; other store opex 13.6 (incl. delivery commissions and card fees) → store-level margin 29.2% | VERIFIED |
| New-unit targets | AUV US$1.1 M at 18 months; mature margin ≥22%; net capex US$0.6 M; cash-on-cash ~40% | VERIFIED |
| Capex | US$860k gross / ~US$650k net of TI (2025); historical ~US$600k blended; Black Rock's own contribution US$230k (build-to-suit) up to the full project (ground lease) | VERIFIED |
| Service model | ~90 s order-to-handoff target; tablet line-busting; dual lanes "at certain locations"; dual-bar layout supports >US$3 M | VERIFIED |
| Format choice | "Drive-thru only formats are typically pursued in high-traffic commuter corridors"; lobbies preferred elsewhere | VERIFIED |
| Mix | Fuel energy drinks ~24% of revenue; "All-Day Breakfast" food; digital 16% of store revenue; loyalty 63% of sales | VERIFIED |
| Advertising | US$2.6 M ≈ 1.3% of revenue | ESTIMATE from VERIFIED |

*Interpretation.* Black Rock is the best template for an Armenian **hybrid**: a drive-thru plus a small lobby, at modest capex. It explicitly chooses drive-thru-only for **commuter corridors**. That maps to an Armenian urban-edge commuter site (B4), not to a leisure highway.

#### 3.2.3 Starbucks ("Back to Starbucks") [7]–[12]

| Item | Value | Status |
|---|---|---|
| Sales mix (co-op) | Beverages 73%, food 23%, other 4% (FY2025; 74/23 in FY2024) | VERIFIED |
| Stores | US 10,047 company-operated (28 Sep 2025); ~18,300 total North America locations | VERIFIED |
| Restructuring | 627 store closures in Q4 FY2025 (584 in North America); Sept 2026: ~1% of >18,000 NA coffeehouses (~250) to close; US$300 M charges | VERIFIED |
| Format language | FY2024 10-K: "continuing the expansion of our stores, particularly drive-thru formats". FY2025 10-K: that phrase removed; stores should give "a warm and welcoming environment" and "a seat for every occasion" | VERIFIED |
| Service model | "Green Apron Service model" live across all US company-operated stores in Q4 FY2025. Niccol letter: added labor hours at busy times improved "transactions, sales, and service times" | VERIFIED |
| Cost of the service reset | NA store opex 56.4% of co-op revenue (51.4% FY2024); NA operating margin 11.5% (19.8%); about 180 bp from "Back to Starbucks" labor | VERIFIED |
| Recovery | US comparable transactions −4% FY2025, then +3% / +4.3% / +4.2% in Q1–Q3 FY2026; NA Q3 FY2026 comps +8.1%, helped by "customer food attach and beverage modifications" and delivery | VERIFIED |
| Drive-thru share, store sizes, ticket, throughput targets, "Siren" equipment speed | Not disclosed in any filing opened; trade-press figures not verified | GAP |

*Interpretation.* The largest coffee operator has just shown that **throughput-only formats can erode brand and traffic**. Its fix was more labor and more hospitality. NA segment margin fell 8.3 pts in FY2025, of which about 1.8 pts was the "Back to Starbucks" labor investment; the rest was deleverage (≈3.1 pts) and restructuring (≈2.4 pts). Transactions recovered in FY2026. For Armenia, a premium positioning should not be "a faster kiosk". It should be speed *plus* a human, friendly exchange. Intouch 2026 shows friendly visits were also **25 s faster**.

#### 3.2.4 Scooter's Coffee (kiosk franchisor, closest to a "lean" unit) [23]

| Item | Value | Status |
|---|---|---|
| Network | 900+ locations; 768 franchised kiosks + 62 franchised end-caps (31 Dec 2025) | REPORTED |
| Kiosk | 664 sq ft (62 m²); "typically 650–700 sq ft"; end-cap 800–1,400 sq ft | REPORTED |
| Site | Pad ≥½ acre (≈2,020 m²); ≥10-car stack; full turning movements; **traffic speed ≤45 mph**; "highly trafficked morning commuter routes"; ≥6 staff parking spaces | REPORTED |
| Results (FY2025 Item 19) | 621 kiosks: avg sales US$998,869, EBITDA US$134,457 (13.5%), net margin 14.6%. Top quartile (156): US$1,433,875 sales, EBITDA US$273,683 (19.1%). End-caps (45): avg US$1,082,458 | REPORTED (FDD summary) |
| Investment | Kiosk US$1,163,650–1,345,750; end-cap US$658,898–1,068,525 (incl. US$40k fee) | REPORTED |
| Fees | Royalty 6%; marketing 2% of net sales | REPORTED |
| Implied transactions/day | ≈390–460 at an assumed US$6–7 ticket | ESTIMATE (ticket not disclosed) |

*Interpretation.*
- An average US kiosk earns **13.5% EBITDA after 8% in fees**, so the format is not a margin machine at US$1 M sales.
- **The ≤45 mph site rule matters.** A US franchisor that has run 768 kiosks screens out roads faster than 72 km/h. The M4 is posted at 90 km/h (B1).

#### 3.2.5 7 Brew, Ziggi's, The Human Bean [24][25][26]

- **7 Brew** (REPORTED, company site):
  - 38 stands in Jan 2023 → **700+ stands in 38 states** by 2026. Blackstone took a minority stake in 2024.
  - Serves **>1 M drinks/day** with an average of **~60 crew per stand** (45,000+ in total).
  - Has no third-party delivery and is not taking new franchise applications.
  - Drinks per stand per day ≈ **1,260–1,430** (ESTIMATE: 1 M ÷ 700–792; the sitemap lists 792 location pages, some possibly not yet open).
  - **Kiosk size, double-drive-thru layout and AUV could not be verified** (7 Brew's FDD; see §5).
- **Ziggi's**: 100+ locations; total investment **US$0.56–2.0 M**; three formats: café + drive-thru, double-sided drive-thru and single-sided drive-thru (REPORTED).
- **The Human Bean**: no royalty fee; 1% brand fee (REPORTED). No unit economics on the page.

#### 3.2.6 Dunkin', Tim Hortons, McDonald's, Chick-fil-A [13][14][15][27]

| Brand | Benchmark | Status |
|---|---|---|
| Dunkin' (FY2019, last public 10-K before the Inspire buyout) | >50% of 9,630 US points had drive-thrus. 58% of US sales came from coffee and beverages, 42% from food and other. Breakfast daypart defined as 5:00–11:00. Free-standing 1,200–2,500 sq ft; end-cap 1,000–2,000. Franchisee ad fund 5%; royalty 5.9%. "NextGen" design named, but its features (e.g., a mobile-order lane) are not described in the filings opened | VERIFIED |
| Tim Hortons (RBI) | 4,586 restaurants in US & Canada; global system sales US$8.248 B (2025); fastest drive-thru in Intouch 2026 (4:20) and 2025 (4:25). Highway/ONroute site data: not found | VERIFIED / REPORTED / GAP |
| McDonald's | ~29,000 drive-thrus worldwide; >95% of ~13,700 US restaurants; "adding additional drive thru lanes to increase capacity"; "Ready on Arrival" mobile-order prep rolled out in its top 6 markets by end-2025 | VERIFIED |
| Chick-fil-A | Restaurants "sometimes serving over 100 cars per hour" at peak, using tablet Face-to-Face Ordering and outside meal delivery (2021). Mobile Thru lanes in 300+ restaurants (2023). Elevated Drive-Thru (Aug 2024): 4 lanes, 2–3× the vehicle capacity, ~150 team members. Slowest brand in Intouch 2026 (7:06) yet 98% satisfaction | VERIFIED / REPORTED |

### 3.3 Unit P&L benchmarks and translation to an Armenian unit

| Line (% of net sales) | Dutch Bros FY2025 | Black Rock FY2025 | Scooter's kiosk FY2025 (franchisee) | Starbucks NA FY2025 | **Recommended Armenian range** (mid concept, mature year) | Basis for the Armenian range |
|---|---|---|---|---|---|---|
| Beverage, food & packaging (COGS) | 25.9% | 28.1% | n/d | 27.9% (product & distribution, % of NA revenue) | **31–36%** incl. 2% waste | ASSUMPTION. Beans, dairy alternatives, syrups and cups are imported at world prices, while Armenian mass to-go coffee sells at 800–1,200 AMD (US$2.2–3.3; A2) and even premium chains stop at about 1,950 AMD. A food share of 35–45% (vs 23% at Starbucks) adds cost (Dutch Bros Q2 2026 note). The model's 31% + 2% waste = 33% sits mid-range. |
| Labor | 26.9% (25.4% in Q2 2026) | 21.0% | n/d | Within 56.4% store opex | **22–32%** | ASSUMPTION. Wages are a fraction of US levels (C3: food-service average AMD 160k/month), but a 2-shift, 7-day crew is fixed and transactions/day are 1/5–1/8 of US. Labor is closer to a fixed cost; C3 builds the roster bottom-up. |
| Occupancy (rent, land tax) | 16.6% incl. "other" | 8.0% rent only | n/d | n/d | **8–15%** | ESTIMATE. Model base rent AMD 1.5 M/month ≈ 12–13% of AMD 140 M sales at 150 tx/day × 2,600 AMD × 360 days. |
| Marketing (ongoing) | 1.7% shop / 2.4% total | 1.3% | 2% fund + local | 2.3% (company total) | **3% ongoing + launch budget** | ASSUMPTION. A new brand has no awareness. US franchise funds run 1–5% (Human Bean 1%, Scooter's 2%, Dunkin' 5%). The model's 3% + AMD 12 M launch is consistent. |
| Card fees, delivery, other store opex | inside "occupancy & other" | 13.6% | n/d | n/d | **4–7%** | ASSUMPTION. Card share and fee from the model; no delivery at a highway site. |
| Royalty / brand fee | — (company-op) | — | 6% + 2% | — | 0% (own brand) | Own-brand concept. |
| **Shop-level EBITDA (four-wall)** | **28.9–30.6%** | **29.2%** (target ≥22% at 18 months) | 13.5% after fees (≈21.5% pre-fees) | NA operating margin 11.5% (after D&A, G&A) | **15–25% at maturity; ≤10% below ~100 tx/day** | ESTIMATE. Fixed labor and rent on 1/5–1/10 of US sales compress the margin. Test in the model. |

### 3.4 Speed, accuracy and throughput

**Industry service benchmarks (Intouch Insight with QSR Magazine).**

| Metric | 2025 study | 2026 study | Source / status |
|---|---|---|---|
| Visits, brands | 13 brands incl. Dutch Bros, Starbucks, Tim Hortons, Dunkin' | 2,145 shops (165/brand), 13 brands; beverage brands shopped **only at breakfast** | [16][17][18] REPORTED |
| Average total time | Classic segment 5:09 | **5:24 (324 s)**, fastest since 2018; median <4:25; slowest 10% ≥9:56 | REPORTED |
| Service time (order → exit) | 4:15 | **4:04 (244 s)** | REPORTED |
| Window time | n/r | **1:40 (100 s)** | REPORTED |
| Fastest brand | Taco Bell 4:16; KFC 4:21; Tim Hortons 4:25 | Tim Hortons 4:20 | REPORTED |
| Accuracy | Dutch Bros 96% (top); friendly 89% vs unfriendly 70% | **89.3%** overall; Starbucks 96%, Dutch Bros 94%; 43% of errors are customisation errors | REPORTED |
| Satisfaction | Chick-fil-A and Dutch Bros 98% | 93.8% (Starbucks 99%, Chick-fil-A 98%, Dutch Bros 97%); **84.9% once a visit passes 10 min**; 42.9% when the lane "felt frustrating" | REPORTED |
| Lane configuration | **79% single lane, 20% two lanes, 1% three lanes**; average cars in line 1.20 | n/r | [19] REPORTED |
| Suggestive selling | 57.5% | 51.6% overall; **beverage brands only 19.5%** | REPORTED |
| Voice AI | Accuracy 83% (82.5%) | 90.8% accuracy; 29.1% had to repeat part of the order | REPORTED |

**Throughput capacity per configuration (ESTIMATE; capacity = 3,600 s ÷ seconds per car at the bottleneck).**

| Configuration | Bottleneck time per car | Capacity (cars/h) | Evidence |
|---|---|---|---|
| Single lane, speaker order, pay and collect at one window | ~80–100 s (Intouch window time 100 s) | 36–45 | [16] |
| Single lane, runner/tablet order and pay in line, one pickup window | ~45–60 s | 60–80 | Dutch Bros / Black Rock practice [1][5]; 90 s order-to-handoff target |
| Two order lanes merging to one window + runners + escape lane | ~40–50 s at the window | 70–90 | Dutch Bros current format [1] |
| Multi-lane with outside delivery (QSR food) | — | >100 | Chick-fil-A [27] |

**Stacking needed is driven by service rate (ESTIMATE, M/M/1 queue, places needed to hold the queue 95% of the time).**

| Arrival rate (cars/h) | Window capacity 50/h | 60/h | 80/h |
|---|---|---|---|
| 30 | 5 cars (mean wait 3.0 min) | 4 (2.0 min) | 3 (1.2 min) |
| 40 | 13 (6.0 min) | 7 (3.0 min) | 4 (1.5 min) |
| 45 | **28 (12 min)** | **10 (4.0 min)** | 5 (1.7 min) |
| 50 | n/a (ρ≥1) | 16 (6.0 min) | 6 (2.0 min) |

*Caveat:* M/M/1 assumes random arrivals and exponential service times. Real coffee peaks are "bursty", so treat these as minimums.

**Armenian peak loads (ESTIMATE).**
- Base 150 transactions/day × 14–22% AM-peak share (ITE 937/938) → **21–33 cars/h** on a weekday.
- On a summer leisure weekend at 2× daily volume (B1 assumption) → **43–66 cars/h**. That is already above the 36–45/h of a speaker-and-one-window lane.
- **A mid/flagship unit therefore needs runner-based ordering (or dual order lanes) and ≥60 cars/h window capacity.** Otherwise the M4 weekend queue reaches 20+ cars, the failure now seen at Coffee House's M4 drive-thru (A3).

### 3.5 Site and building design norms → Armenian parameters

**US norms found.**

| Parameter | US benchmark | Status |
|---|---|---|
| Building | Dutch Bros 800–1,000 sq ft (74–93 m²); Scooter's kiosk 664 sq ft (62 m²); Dunkin' free-standing 1,200–2,500 sq ft (111–232 m²); Chick-fil-A elevated kitchen 2× standard | VERIFIED / REPORTED |
| Lot | Dutch Bros ≥25,000 sq ft (2,323 m²); Scooter's ≥½ acre (2,023 m²) | VERIFIED / REPORTED |
| Queue/stack | Palm Beach County: 7 spaces (≥4 before menu board) + 1 after the window, bypass lane if >5 spaces. Scooter's ≥10 cars. Dutch Bros "ample car stacking", escape lane | VERIFIED / REPORTED |
| Queue space size | 10 ft × 20 ft (3.05 × 6.1 m); window position 9 × 20 ft | VERIFIED [21] |
| Bypass lane | ≥10 ft (3.05 m) | VERIFIED [21] |
| Access/driveway | One-way ≥15 ft (4.6 m), two-way ≥25 ft (7.6 m); right-turn radius 25–30 ft (7.6–9.1 m) | VERIFIED [21] |
| Dual lanes | Palm Beach County allows dual lanes merging to one, with 4 spaces before each menu board. Dutch Bros "multiple drive-thru lanes served by one window". Only 21% of the US QSR drive-thrus Intouch evaluated in 2025 had more than one complete lane | VERIFIED / REPORTED |
| Windows | Dutch Bros: one drive-thru window + standard walk-up window. Chick-fil-A Makiki: dual lane + 3 walk-up windows | VERIFIED |

**Recommended Armenian design parameters (ASSUMPTION built on the benchmarks above; check against Armenian building norms and the RDF/MTAI access rules in C1/B1).**

| Parameter | Lean (kiosk) | Mid (recommended) | Flagship |
|---|---|---|---|
| Building, gross | 45–65 m² modular (Scooter's 62 m², Dutch Bros legacy 46 m²) | **90–120 m²**: beverage bar + hot-food prep (A4 food emphasis) + storage + staff WC | 140–180 m² incl. 25–40 seats or a terrace |
| Lot | 1,200–1,600 m² | **1,800–2,500 m²** (Dutch Bros/Scooter's ≈2,000–2,300 m²) | 2,500–3,500 m² |
| Lanes | 1 lane + bypass | **2 order lanes merging to 1 window, or 1 lane with 2 tablet runners**; separate bypass/escape lane | 2 lanes, 2 windows (pay/collect or two pickup points) + mobile-order pull-forward bays |
| Stack (window to queue end) | 8–10 cars (≈50–60 m) | **10–12 cars (≈60–75 m at 6.1 m/car)**, plus 1–2 spaces after the window | 14–16 cars combined |
| Lane width | ≥3.0 m (10 ft code minimum); 3.3–3.6 m preferred | 3.3–3.6 m per lane; bypass ≥3.0 m | as mid |
| Inside turning radius on the lane | ≥7.5 m | ≥7.5–9 m (25–30 ft) | ≥9 m |
| Walk-up window | Yes | Yes (Dutch Bros standard) | Yes + indoor counter |
| Target window time / capacity | ≤75 s → ~48 cars/h | **≤60 s → ≥60 cars/h**; order-to-handoff ≤3 min (Black Rock ~90 s) | ≤45–50 s → 70–80 cars/h |
| Highway-specific | Queue must never back up into the deceleration lane. The longest stack must fit inside the plot, with an overflow parking area. Advance signage ≥0.5–1 km ahead at 90 km/h | same | same |

### 3.6 Trip generation, pass-by and a defensible capture-rate range

**ITE inputs (12th edition rates, reproduced in Palm Beach County's May 2026 table [20]; VERIFIED).**

| ITE land use | Unit | Daily trips | AM peak hour | PM peak hour | Pass-by applied by Palm Beach County | AM peak share of daily (ESTIMATE) |
|---|---|---|---|---|---|---|
| 937 Coffee/donut shop with drive-through | per 1,000 sq ft | 600.50 (11th: 533.57) | 85.41 (85.88) | 39.00 (38.99) | 49% | 14.2% |
| 938 Coffee/donut drive-through, no seating | per drive-through lane | 179 | 39.81 | 15.08 | 49% | 22.2% |
| 934 Fast food with drive-through | per 1,000 sq ft | 448.12 | 33.24 | 31.60 | 49% | 7.4% |
| 936 Coffee/donut, no drive-through | per 1,000 sq ft | 485.48 (derived) | 91.02 | 31.53 | 45% | — |
| Gas station with convenience store | FDOT equation | — | — | 12.3 × FP + 15.5 × ksf | 61% | — |

Notes:
- (a) A "trip" is one vehicle movement in or out, so **customer vehicles ≈ trips ÷ 2**.
- (b) The 49% pass-by is **Palm Beach County's planning value**. ITE's Trip Generation Handbook pass-by tables for 937/938 could not be opened (paywalled; §5), and the handbook may show a higher share.
- (c) The 938 daily rate (≈90 customer vehicles per lane per day) is far below Dutch Bros or 7 Brew volumes. The ITE 938 sample evidently reflects small kiosks, and Palm Beach County notes small 12th-edition samples for some uses. Treat ITE rates as the *typical* US unit, not the leaders.

**Step 1 — US capture benchmark (ESTIMATE).**
- A 2,000 sq ft land-use 937 shop generates 600.5 × 2 = 1,201 trips/day, i.e. **~600 customer vehicles/day**.
- US coffee drive-thrus are typically sited on arterials. Assume AADT 20,000–40,000 (**ASSUMPTION**; no chain publishes an AADT threshold among the sources opened).
- Pass-by visits at 49–89% pass-by = 294–534 vehicles → **0.7–2.7% of two-way AADT**; central case (30k, ~70% pass-by) ≈ **1.4–1.5%**.
- Including diverted and destination trips: **1.5–3.0% of two-way AADT**.
- Cross-check: Dutch Bros at ≈680–830 transactions/day on an assumed 25–45k AADT site is ≈1.5–3.3%. So the leaders sit at the top of the ITE band (ESTIMATE).

**Step 2 — adjust for Armenia (ASSUMPTION; each factor explained).** Multiply the US central pass-by capture (1.5% of *accessible* vehicles; in the US both directions are accessible) by:

| Factor | Range | Why |
|---|---|---|
| Category maturity / habit | 0.5–0.8 | The US drive-thru habit is mature: 85% of Dutch Bros business is drive-thru, and loyalty apps drive 63–74% of transactions. Armenia has strong *to-go* coffee (Coffee House 57 branches, A2) but only one known drive-thru (A3), whose peak queues show demand exists. |
| Income-to-price | 0.7–0.9 | A premium cup is ≈1 hour of average food-service pay in Armenia vs minutes in the US (A2/C3). Offset: Armenian to-go coffee prices are low (800–1,200 AMD). |
| Speed / access | Highway 0.6–0.9; urban 0.9–1.0 | Scooter's rejects roads >45 mph. The M4 is a 90 km/h divided road with a guard-rail median and right-in/right-out access (B1). Urban edges are 60 km/h, often signalised. |
| Leisure uplift (Sevan-bound weekends) | Highway 1.0–1.3 | Discretionary trips have a higher stop propensity than commuter trips (ASSUMPTION, B1/B4). |

- Result, M4 highway: 1.5% × (0.21 to 0.84) = **0.3–1.3%** of same-side light vehicles; geometric mean ≈ **0.63%**.
- Result, urban-edge arterial: 1.5% × (0.32 to 0.72) = **0.5–1.1%**; geometric mean ≈ **0.71%**.

**Step 3 — regional reality checks.**

| Anchor | Value | Status |
|---|---|---|
| WOG fuel-station coffee (Ukraine), captive stop | ≈117 cups/station/day (2014–20 average) | ESTIMATE from REPORTED [28] |
| Coffee Like car-oriented pavilion (Russia) | ≈103 checks/day (franchisor "from" claim) | REPORTED (A2) |
| Coffee House average branch | ≈40–70 cups/day | ESTIMATE (A2) |
| B4: capture needed for 120 tx/day | 0.49–0.57% (urban edges); 0.75% (M-1 exit) | ESTIMATE (B4) |

The Step-2 ranges reproduce these anchors. At the B1 base of ~11,000 same-side light vehicles/day between Abovyan and Charentsavan, the outcomes are:

| Same-side light-vehicle capture | Transactions/day |
|---|---|
| 0.4% | 44 |
| 0.75% | 83 |
| 1.2% | 133 |
| 1.8% | 199 |

These exclude walk-ins (ESTIMATE). The middle of that range matches the regional anchors (≈80–150), and 1.8% does not.

**Step 4 — mapping to the model.**
- The model applies capture to AADT × 0.55 (accessible share), with no light-vehicle factor. The current base of **1.8%** is ≈**2.4% of same-side light vehicles** (1.8% × 0.55 ÷ (0.5 × 0.82)). **That is above the US-mature central benchmark.**
- The equivalent model inputs for the recommended same-side light-vehicle captures are **0.30% / 0.60% / 0.90%** (conservative / base / optimistic), i.e. 0.4% / 0.8% / 1.2% × 0.745.
- Alternatively, keep the current inputs but treat them as a **stretch case**, to be validated by field counts at the Coffee House M4 drive-thru and by stop-rate counts (B1 §5, B4 §5).

### 3.7 Demand curves: hour, day and season

| Pattern | Benchmark | Status | Use in the model |
|---|---|---|---|
| AM peak concentration | ITE 937: AM peak hour = 14.2% of daily trips; 938 (drive-through only) 22.2%; PM peak 6.5% / 8.4% | ESTIMATE from VERIFIED [20] | Size crew and lanes on a 15–22% peak hour (commuter site). Leisure sites may peak late morning/midday (Coffee House "usually busy around 13:00", A2) |
| Breakfast focus | Dunkin' defines breakfast as 5:00–11:00 and protects that daypart. Intouch shops beverage brands only at breakfast. Dutch Bros sees order-ahead and food as levers for the **morning** daypart | VERIFIED / REPORTED | The Yerevan-bound commuter side captures the morning; the Sevan-bound side captures weekend late mornings (B1) |
| Traffic profile vs coffee profile | Yerevan western arterial: peak hour ≈6% of ADT, 70% of traffic between 08:00 and 19:00 (B4) | VERIFIED (B4) | Coffee demand is 2–4× more peaked than traffic. Do not size the stack on average hourly flow |
| Seasonality | Dutch Bros: higher sales in summer (Q2–Q3). Dunkin': hot beverages up in fall/winter, iced in spring/summer | VERIFIED | Supports the model's summer-weighted index for the M4. The US amplitude is small; Armenian leisure amplitude is larger (B1/B4) |
| Weekday vs weekend | No primary benchmark found (ITE Saturday rates for 937 not in the county table) | GAP | Use B1/B4 assumptions until field counts are available |

### 3.8 Menu mix: beverage vs food, hot vs cold, energy

| Brand | Beverage share | Food share | Cold/energy | Status |
|---|---|---|---|---|
| Starbucks (co-op) | 73% | 23% | Cold share not disclosed; growth in "cold beverages" named as an initiative | VERIFIED [7] |
| Dunkin' U.S. | 58% coffee and beverages | ~42% food and other (by difference) | n/d | VERIFIED [15] |
| Dutch Bros | ~100% beverage-led (coffee ~50%, energy ~25%, other ~25% incl. small food) | Small; expanding in 2026 | Energy ~25% of sales | VERIFIED [1] |
| Black Rock | Mostly beverage | "All-Day Breakfast" (share n/d) | Fuel energy drinks ~24% of revenue | VERIFIED [5] |

*Translation.* An Armenian "coffee & food" unit should plan **55–70% beverage / 30–45% food** (ASSUMPTION; A4 food preferences). It should budget a higher blended COGS than beverage-only US chains. Energy-drink platforms (~25% in the US) should be modelled at **≤5–10%** (ASSUMPTION, A4).

### 3.9 Capex and returns benchmarks

| Brand | Capex per unit | Return metric | Status |
|---|---|---|---|
| Black Rock | US$860k gross; ~US$650k net of TI (2025); US$600k historical blended | ~40% cash-on-cash at 18 months on US$1.1 M AUV and ≥22% margin | VERIFIED [5][6] |
| Scooter's kiosk (franchisee) | US$1.16–1.35 M total initial investment | Avg EBITDA US$134k → ≈10–12% pre-tax cash yield on investment | REPORTED + ESTIMATE [23] |
| Dutch Bros | ≤US$1.71 M per opening (all capex ÷ openings); 2026 capex guidance US$350–370 M for ≥185 openings | Contribution ~30% on US$2.1 M AUV | VERIFIED + ESTIMATE [1][2], C1 |
| Ziggi's | US$0.56–2.0 M | n/d | REPORTED [25] |

*Rule-of-thumb check (ESTIMATE).*
- **Black Rock's target:** a 22% margin on US$1.1 M is US$242k a year on US$0.6 M net capex, i.e. ≈2.5-year payback.
- **Armenian equivalent:** 150 tx/day × 2,600 AMD × 360 days = **AMD 140 M (≈US$388k) sales**. At a 15–20% four-wall margin that is AMD 21–28 M (≈US$58–78k) a year.
- To match a ~2.5–4-year payback, all-in capex would need to be **≈AMD 50–110 M (US$0.14–0.30 M)** (AMD 21–28 M × 2.5–4 years). That is below C1's mid-range build, so the model should test lean and modular options seriously.

### 3.10 What transfers to Armenia and what does not

| Benchmark | Transfers? | Why |
|---|---|---|
| Cost **ratios** (COGS, labor, occupancy, marketing %) | **Partly** | Structure transfers; levels shift. COGS% is higher (imported inputs, lower prices, more food). Labor% depends on volume because the crew is quasi-fixed. |
| **AUV**, transactions/day (US$1–2.2 M; 400–830 tx/day) | **No** | US car dependency, habit, loyalty apps and 5–8× higher income. Armenian anchors are 40–150/day. |
| Capture rates (US 0.7–3% of AADT) | **Only with heavy adjustment** | See §3.6. The M4's speed and median access cut capture. |
| Building size (60–95 m² beverage-only) | **Yes, plus food space** | Physics of the bar is the same; add 20–30 m² if hot food is core. |
| Lot size (~2,000–2,300 m²) and stack (10–12 cars) | **Yes** | Queue geometry is universal. On a 90 km/h road, spill-back is a safety failure, not just a nuisance. |
| Runner/tablet ordering | **Yes, and cheaper** | Low Armenian wages make an extra runner affordable. It is the cheapest throughput lever. |
| Service-time targets (≤90 s order-to-handoff; ≤60 s window) | **Yes** | Directly addresses the incumbent's 20–60-minute waits (A3). |
| Energy-drink share (~25%) | **No** | Cheap retail cans, health framing, minors issue (A4). |
| Loyalty-app share (63–74%) | **Not at launch** | Needs a brand and scale. Plan for 10–30% by year 3 (ASSUMPTION). |
| ≤45 mph site rule (Scooter's) | **Yes, as a warning** | It argues against a mid-carriageway 90 km/h M4 pad, and for interchanges or slow urban edges. |
| Starbucks "Back to Starbucks" lesson | **Yes** | In a social coffee culture, a walk-up/terrace and friendliness matter. Friendly visits are faster *and* more accurate (Intouch 2026). |
| Build-to-suit lease economics | **No** | There is no Armenian developer market for build-to-suit drive-thru pads. The investor carries the capex (C1). |
| Climate | **Partly** | US Sun Belt vs Armenian winters; an M4 site at higher altitude needs canopy, heated windows and snow clearance (B1). |

---

## 4. Implications for the drive-thru concept (critical)

1. **The model's capture assumption is the biggest benchmark-driven risk.** The base of 1.8% of AADT × 0.55 is about 2.4% of same-side light vehicles, above what mature US coffee drive-thrus achieve on typical sites. **Recommended: base 0.6% (model basis), conservative 0.3%, optimistic 0.9%**, until fieldwork shows otherwise.
   - On B1's 27k AADT segment the recommended base yields ≈90 drive-thru transactions/day (27,000 × 0.55 × 0.6%) plus the model's 20 walk-ins, ≈110/day.
   - The current 1.8% input would give ≈290/day on the same segment.
   - ≈110/day sits inside A2's 80–150 range; ≈290/day is far above it.
2. **A US-style margin will not appear at Armenian volumes.** US four-wall margins of 25–31% rely on US$1–2 M AUVs. An Armenian unit at AMD 100–150 M sales carries fixed rent, a 7-day crew and utilities, so margins of **15–25% at maturity** are a realistic target. Below ≈100 tx/day the unit is near breakeven. The model's sensitivity tables should show that cliff explicitly.
3. **Design for throughput, not for show.**
   - Minimum standard: 10–12-car stack, bypass/escape lane, ≥60 cars/h window capacity, runners with tablets, and a walk-up window.
   - An 8-car lane with a speaker box and one window (36–45 cars/h) **will recreate the incumbent's failure** on summer weekends. The queue maths shows the stack explodes when window time exceeds ~70 s at peak arrivals of 45/h.
4. **A highway pad mid-carriageway is the weakest site type by benchmark logic.** It combines 90 km/h speeds, right-in/right-out access, leisure-only peaks and spill-back risk onto a deceleration lane. Every US kiosk franchisor seen screens these sites out. If the M4 is chosen, an **interchange or fuel-station hybrid** with low approach speed and internal circulation is the only benchmark-consistent option (aligned with A3/B4).
5. **Food is a differentiator and a margin cost.** US leaders run beverage-led menus (Dutch Bros ~100%, Starbucks 73% beverages). Armenian demand pushes food to 30–45% (A4). Plan COGS at 31–36% and kitchen space at +20–30 m², and keep the food menu narrow so window times stay ≤60 s. Customisation causes 43% of US order errors.
6. **The Starbucks reversal is a warning against a sterile "speed box".** Starbucks accepted a hit to NA margin (≈1.8 pts from labor investment, within an 8.3-pt FY2025 decline) to rebuild hospitality, and transactions recovered afterwards. For a premium Armenian brand, **friendliness plus speed** is the differentiator against Coffee House, Max Cafe and Flash. Budget labor accordingly rather than cutting crew to hit a US-style labor%.
7. **US capex levels (US$0.65–1.7 M) are irrelevant to returns in Armenia.** To reach a 2.5–4-year payback, all-in capex must stay near **AMD 50–110 M** for a mid unit at base volumes (§3.9). That points to modular or semi-modular buildings and a ground lease.
8. **Starbucks entry (A2) would bring a coffeehouse-first format, not a drive-thru-first one**, judging by its FY2025 strategy. That leaves the drive-thru niche to whoever executes speed well. The incumbent, Coffee House, can fix its operations cheaply, so the window may be short.

---

## 5. Data gaps & how to verify them

| Gap | Why it matters | How to verify |
|---|---|---|
| Starbucks drive-thru share of US company-operated transactions/revenue; drive-thru and pickup store sizes; average ticket; throughput targets; "Siren" equipment speed; pickup-only closures | Format and throughput calibration | Starbucks Investor Relations: 2022 Investor Day ("Reinvention") deck and transcript; FY2025–26 earnings-call transcripts (Q&A on drive-thru and Green Apron service times); Starbucks Stories newsroom (blocked to automated fetch; open manually) |
| 7 Brew kiosk size, double-lane layout, AUV, Item 19 | Lean/mid layout benchmark | 2025/2026 7 Brew FDD (Item 19, Item 8 site specs) from state franchise registries: California DFPI, Wisconsin DFI, Minnesota CARDS (free) |
| Dutch Bros, Black Rock and Scooter's average ticket and transactions/day | Converts AUV to car counts; makes the capture benchmark exact | Earnings-call transcripts and analyst-day decks (Dutch Bros 2024 investor day); Scooter's full FDD Item 19 tables |
| ITE Trip Generation Handbook pass-by tables for LU 937/938/945; ITE time-of-day and Saturday distributions | Pass-by % (49% county value vs handbook) and weekend factor | ITE TripGen12 web app licence (itetripgen.org) or ITE Trip Generation Handbook 3rd ed.; alternatively a recent US traffic impact study for a Dutch Bros/Starbucks site on a municipal planning portal |
| Typical AADT at US coffee drive-thru sites | Denominator of the US capture benchmark (assumed 20–40k) | Ask Scooter's/Ziggi's/Black Rock site criteria; or overlay Dutch Bros locations on state DOT AADT maps (e.g., Oregon/Arizona) for a 30–50 site sample |
| Tim Hortons highway (ONroute) volumes; RBI drive-thru share | Highway benchmark | RBI investor day materials; ONroute operator (Arcadian/HMSHost) disclosures |
| OKKO, Circle K and other fuel-station cups/day (post-2022) | European highway coffee benchmark | OKKO/WOG/UPG press offices; Couche-Tard annual report (Circle K) and investor presentations; NACS/ACS Europe studies |
| QSR Magazine brand-level drive-thru times (Starbucks, Dutch Bros, Dunkin') | Speed targets by brand | Purchase or download the Intouch 2026 Drive-Thru Study full report (brand tables) |
| Coffee House M4 drive-thru: cars/hour, service time, queue, weekend/summer factor | **The single most decisive calibration point** for Armenia | Fieldwork protocol in A2/A3/B1: 3 weekdays + 2 weekend days × 3 dayparts, summer and winter; licence-plate direction sampling |
| Armenian design norms for drive-through lanes, curb cuts and deceleration lanes | Converts US geometry to permit-ready design | Urban Development Committee (mud.am) norms; RDF/MTAI access permits for the M4; local architect pre-application |

---

## 6. Sources (all accessed 2026-10-10)

1. Dutch Bros Inc., Form 10-K FY2025, filed 13 Feb 2026. https://www.sec.gov/Archives/edgar/data/1866581/000186658126000006/bros-20251231.htm
2. Dutch Bros Inc., Q2 2026 earnings release (Ex. 99.1), 5 Aug 2026. https://www.sec.gov/Archives/edgar/data/1866581/000186658126000131/a2026-q2_ex991.htm
3. Dutch Bros Inc., Form 10-Q for Q2 2026, filed 6 Aug 2026. https://www.sec.gov/Archives/edgar/data/1866581/000186658126000133/bros-20260630.htm
4. Dutch Bros Inc., Form 8-K, 5 Aug 2026 (agreement to acquire up to 65 Salad and Go sites). https://www.sec.gov/Archives/edgar/data/1866581/000186658126000131/bros-20260805.htm
5. Black Rock Coffee Bar, Inc., Form 10-K FY2025, filed 4 Mar 2026. https://www.sec.gov/Archives/edgar/data/2068577/000162828026014380/brcb-20251231.htm
6. Black Rock Coffee Bar, Inc., final prospectus (424B4), 15 Sep 2025. https://www.sec.gov/Archives/edgar/data/2068577/000206857725000031/blackrockcoffee-424b4.htm
7. Starbucks Corp., Form 10-K FY2025 (FY ended 28 Sep 2025), filed 14 Nov 2025. https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm
8. Starbucks Corp., Form 10-K FY2024, filed 20 Nov 2024 ("particularly drive-thru formats" wording). https://www.sec.gov/Archives/edgar/data/829224/000082922424000057/sbux-20240929.htm
9. Starbucks Corp., Form 10-Q for Q3 FY2026, filed 29 Jul 2026. https://www.sec.gov/Archives/edgar/data/829224/000082922426000130/sbux-20260628.htm
10. Starbucks earnings releases:
    - Q4 FY2025 (29 Oct 2025): https://www.sec.gov/Archives/edgar/data/829224/000082922425000074/sbux-09282025xexhibit991.htm
    - Q1 FY2026 (28 Jan 2026): https://www.sec.gov/Archives/edgar/data/829224/000082922426000010/sbux-12282025xearningsrele.htm
    - Q2 FY2026 (28 Apr 2026): https://www.sec.gov/Archives/edgar/data/829224/000082922426000078/sbux-03292026xearningsrele.htm
    - Q3 FY2026 (29 Jul 2026): https://www.sec.gov/Archives/edgar/data/829224/000082922426000129/sbux-06282026xearningsrele.htm
11. Starbucks Form 8-K, Ex. 99.1 (B. Niccol letter on coffeehouse closures), 25 Sep 2025. https://www.sec.gov/Archives/edgar/data/829224/000082922425000067/exhibit991.htm
12. Starbucks Form 8-K (Item 2.05/7.01, ~1% North America closures), 24 Sep 2026. https://www.sec.gov/Archives/edgar/data/829224/000082922426000145/sbux-20260922.htm
13. McDonald's Corp., Form 10-K FY2025, filed 24 Feb 2026. https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm
14. Restaurant Brands International, Form 10-K FY2025, filed 20 Feb 2026. https://www.sec.gov/Archives/edgar/data/1618756/000161875626000017/qsr-20251231.htm
15. Dunkin' Brands Group, Form 10-K FY2019, filed 24 Feb 2020. https://www.sec.gov/Archives/edgar/data/1357204/000135720420000015/dnkn-20191228x10k.htm
16. Intouch Insight, "2026 Drive-Thru Study" press release, 1 Oct 2026. https://www.intouchinsight.com/press-releases/2026-drive-thru-study
17. Intouch Insight, "2026 Drive-Thru Study: Key Drive-Thru Trends from our Annual Report" (blog) and study page. https://www.intouchinsight.com/blog/drive-thru-trends ; https://www.intouchinsight.com/resources/studies/drive-thru/
18. Intouch Insight, 25th annual Drive-Thru Study press release, 1 Oct 2025. https://www.intouchinsight.com/press-releases/drive-thru-study-2025-press-release
19. Intouch Insight, "Is QSR drive-thru customer behavior changing?", 17 Oct 2025. https://www.intouchinsight.com/blog/qsr-drive-thru-customer-behavior
20. Palm Beach County Traffic Division, Trip Generation Rates:
    - ITE TGM 12th edition, updated 4 May 2026: https://discover.pbc.gov/engineering/traffic/PDF/Traffic%20Documents/Trip-Generation-Rates-ITE-12th-Edition.pdf
    - 11th edition table, 25 Jul 2022: https://discover.pbc.gov/engineering/traffic/PDF/Traffic%20Documents/Trip_Generation_Rates.pdf
21. Palm Beach County Unified Land Development Code, Article 6 (Parking, Loading and Circulation), Supplement 32, printed Oct 2025: Table 6.B.3.A Minimum Queuing Standards; Dimensions of Access Ways. https://pbc.gov/uldc/pdf/Article6.pdf
22. Institute of Transportation Engineers, Trip Generation Manual 12th edition information page (data paywalled). https://www.ite.org/technical-resources/topics/trip-and-parking-generation-v2/trip-generation-info/
23. Scooter's Coffee franchising pages (FY2025 Item 19 summary, real-estate criteria, cost, FAQ, drive-thru model):
    - https://franchising.scooterscoffee.com/
    - https://franchising.scooterscoffee.com/real-estate/
    - https://franchising.scooterscoffee.com/coffee-franchise-cost/
    - https://franchising.scooterscoffee.com/franchise-faq/
    - https://franchising.scooterscoffee.com/coffee-drive-thru-model-menu/
24. 7 Brew, About, FAQ and sitemap: https://7brew.com/about ; https://7brew.com/faq ; https://7brew.com/sitemap.xml
25. Ziggi's Coffee, Franchise page. https://ziggiscoffee.com/franchise/
26. The Human Bean, Franchise page. https://franchise.thehumanbean.com/
27. Chick-fil-A newsroom:
    - "The drive-thru experience is all a game of seconds" (1 Mar 2021): https://www.chick-fil-a.com/press-room/drive-thru-behind-the-scenes
    - "Mobile Thru" (5 Sep 2023): https://www.chick-fil-a.com/press-room/need-for-speed-mobile-thru
    - Elevated Drive-Thru (21 Aug 2024): https://www.chick-fil-a.com/press-room/chick-fil-a-opens-first-elevated-drive-thru-concept
    - Makiki drive-thru-focused restaurant (20 Jul 2023): https://www.chick-fil-a.com/press-room/first-chick-fil-a-drive-thru-focused-restaurant-on-oahu-to-open-on-thursday-july-27
28. Delo.ua, "Кофе от WOG: 7 лет на рынке и 10 млн евро инвестиций в проект" (Coffee from WOG: 7 years on the market and €10 M invested in the project), 1 Oct 2020. https://delo.ua/business/kofe-ot-wog-7-let-na-rynke-i-eur10-mln-investic-373432/
29. Wikipedia (pointers only, not used for figures): WOG (uk) https://uk.wikipedia.org/wiki/WOG ; OKKO (en) https://en.wikipedia.org/wiki/OKKO
30. Sibling workstreams, all in `/home/user/Drive-thru/research/`:
    - A1 (FX, income)
    - A2 (Armenian coffee market, Coffee Like, Coffee House throughput)
    - A3 (Coffee House M4 drive-thru reviews)
    - A4 (food and energy-drink preferences)
    - B1 (M4 traffic, speeds, access)
    - B4 (alternative corridors, required capture)
    - C1 (construction cost, Dutch Bros capex ratio)
    - C3 (wages)

    Also the financial model inputs: `/home/user/Drive-thru/model/assumptions.json`.
