# C3: Labour market, wages and employment rules for a drive-thru in Armenia

*Prepared 2026-10-10 by analyst workstream C3. All AMD/USD conversions use the official Central Bank of Armenia (CBA) rate for 2026-10-09: **USD 1 = AMD 361.93** (VERIFIED, CBA SOAP API [S23], the same rate as workstream C2).*

**Status tags.**
- VERIFIED: an official or primary text I opened. This covers legal acts read on the IRTEK legal database, Armstat tables and the CBA API.
- REPORTED: a credible secondary source (news agency, PwC tax summary) or an employer's own job advertisement that I opened.
- ESTIMATE: my own calculation. The formula and inputs are shown.
- ASSUMPTION: analyst judgement. The basis is given.

**Method note and limits. Please read before using the numbers.**
- The general web-search budget for this session was exhausted before this workstream started. I therefore worked only by direct navigation of primary sources:
  - legal texts on irtek.am, an official-text legal database with version history;
  - draft laws on e-draft.am;
  - Armstat pages, PDFs and XLSX files;
  - the CBA API;
  - the full job.am RSS feed (1,197 live ads on 10 Oct 2026) and the individual ad pages;
  - staff.am search results (its embedded JSON);
  - the site search of the ARKA news agency (arka.am).
- arlis.am (the official legal portal) timed out on every attempt. Legal texts are therefore cited from IRTEK and should be cross-checked on arlis.am before signing contracts.
- list.am returned HTTP 403 (Cloudflare). hr.am did not respond. **No list.am or hr.am postings are included.**
- I have **no supplier or employer quotations**. Every salary below is an advertised figure or a statistic, not a negotiated offer.

---

## 1. Executive summary

1. **The statutory minimum wage does not constrain this business.** It is still **AMD 75,000/month** (AMD 450/hour for a 40-hour week), unchanged since 1 Jan 2023 (VERIFIED [S3]). No increase is enacted for 2026–27:
   - The 2021 government plan to reach AMD 85,000 "by 2026" was not implemented [S16].
   - A Jan-2025 draft (35-hour week plus an hourly minimum of AMD 515) is still "under discussion" [S9].

   Market pay for drive-thru roles is **2–3× the minimum**, so the minimum wage only matters for part-timers paid by the hour.
2. **Official hospitality pay is low but rising fast.**
   - Accommodation and food service activities: average gross wage **AMD 160,253/month in Jan–Aug 2026**. That is 51% of the national average of AMD 312,486.
   - It grew **+7.8% year on year**, against +5.6% nationally (VERIFIED [S17][S18]).
   - Kotayk marz averaged **AMD 208,210** in Q2 2026, against Yerevan's 357,583 (VERIFIED [S19]).
3. **Advertised pay, Sep–Oct 2026, 30 ads cited in §3.3 (Yerevan and Kotayk):**
   - baristas and cashiers: **AMD 140–210k/month**, or **7,000–12,000 per shift** plus tips and % of sales;
   - cooks: **235–350k/month**, or 12–15k per day;
   - cleaners: **135–300k**;
   - supervisors and managers: **200–450k**.

   The chains closest to the concept (Coffee House, Cofix, Gotcha, FEIN) **do not publish salaries**. Only 44% of job.am and 17% of staff.am hospitality ads show any pay (REPORTED [S24][S26]).
4. **Whether an advertised figure is gross or net is the largest single uncertainty in the labour budget.**
   - Almost no ad says which it is.
   - Across all 1,197 job.am ads, the five explicit statements split **2 net (blue-collar) to 3 gross**.
   - Budgeting ads as net, the base case here, makes payroll **about 27% higher** than reading them as gross. That is a swing of AMD 0.9–1.8m/month depending on the format.
5. **Payroll mechanics in 2026 (VERIFIED / REPORTED [S5][S6]).**
   - Deducted from the employee: personal income tax **20%**; funded-pension social payment **5%** of gross up to AMD 500k (for people born 1974 or later; above that, 10% minus AMD 25,000, capped at AMD 87,500); stamp duty **AMD 1,000**; universal health-insurance (UHI) premium **AMD 4,800** (gross AMD 200–500k) or **10,800** (above AMD 500k).
   - **The employer pays no mandatory contribution in 2026, so employer cost equals gross salary.**
   - Worked examples (employee born 1974 or later):

     | Net salary (AMD) | Gross = employer cost (AMD) | Cost per AMD 1 of net |
     |---|---|---|
     | 200,000 | 274,400 | 1.372 |
     | 250,000 | 341,067 | 1.364 |
     | 350,000 | 474,400 | 1.355 |
6. **A new employer health levy is coming.** The Ministry of Health's draft (e-draft 10624, under discussion) applies from the December 2026 payroll. For each employee earning **AMD 200,000 gross or less per employer**:
   - the employer pays **AMD 4,400/month** out of its own funds;
   - the employee pays AMD 2,000;
   - the state pays AMD 4,400 (REPORTED [S7][S14]).

   This creates a pay "notch" around AMD 200k gross. **Recommendation: pay full-time crew at least AMD ~207k gross**, which keeps net pay at AMD 149k or more and avoids the levy.
7. **Labour Code constraints that shape the roster (VERIFIED [S1]).**
   - Hours: 40 hours/week; 8 hours/day normal; 12 hours/day maximum including overtime; 11 hours of rest between shifts; 35 hours of weekly rest.
   - Premiums: overtime at least +50% (no more than 4 hours in any two days and 180 hours/year, normally with written consent); night work (22:00–06:00) at least +30%; work on the **13 non-working public holidays** at least 2×.
   - Annual leave: **20 working days** on a 5-day week, 24 on a 6-day week.
   - Probation: no more than 3 months.
   - **Workers under 18 may not do night work or overtime and may not sell energy drinks.** In practice, crew should be 18 or older.
8. **Staffing is the largest operating cost line.** Covering one position for 16–18 hours a day, 7 days a week, needs **3.1–3.5 full-time equivalents (FTE)**. Base-case employer payroll (2026 rules, ads read as net):

   | Format | Hours and staffing | FTE | AMD/month, base (range) | USD/month, base (range) |
   |---|---|---|---|---|
   | Lean | 07:00–22:00, 3 per shift | ≈10.3 | **3.3m** (2.8–3.9m) | **$9.1k** ($7.6–10.7k) |
   | Mid | 07:00–22:00, 4 per shift | ≈13.4 | **4.1m** (3.4–4.8m) | **$11.4k** |
   | Flagship | 06:00–23:00, 6 per shift + cleaner | ≈23 | **6.7m** (5.6–7.8m) | **$18.5k** |

   The financial model's current lean input (8 FTE, AMD 2.45m/month) is **about 26% too low** unless the roster is shaped to demand (about 21% fewer paid hours).
9. **A highway site depends on a thin local labour pool.**
   - On 10 Oct 2026, job.am listed **1,039 Yerevan jobs, against 34 in Abovyan, 4 in Yeghvard, 3 in Nor Hachn, 2 in Sevan, 1 in Hrazdan and 0 in Charentsavan** (VERIFIED snapshot [S24]).
   - Employers near Abovyan already advertise AMD 200–300k and **provide their own staff transport**. One M4-side restaurant cleaner job at Verin Ptghni pays "from AMD 300,000".
   - Shift changes at about 05:30 and 23:30 make staff transport a real cost: **AMD 0.3–0.6m/month (ASSUMPTION)**.
10. **There are no official figures on staff turnover.** The proxy is high:
    - In 2025 the accommodation and food sector created **8.9k jobs and eliminated 8.9k**, against about 47k payroll employees (VERIFIED [S21][S19]).
    - Plan for **60–100% annual crew turnover (ASSUMPTION)** and about AMD 79k per hire (job ad plus 40 paid training hours, ESTIMATE).

---

## 2. Key data table

| Metric | Value | Period | Status | Source |
|---|---|---|---|---|
| Statutory minimum monthly wage | AMD 75,000 | Effective 01.01.2023; current version (no later amendment) | VERIFIED | [S3] Law HO-66-N, Art. 1 |
| Minimum hourly tariff, 40-hour week (≤24-hour week / 36-hour week) | AMD 450 (750 / 500) | Same | VERIFIED | [S3] Art. 2 |
| Draft: 35-hour week and hourly minimum of AMD 515 | Not adopted; "under discussion" | Draft published Dec 2024/Jan 2025 | VERIFIED (draft text) | [S9] |
| Labour Code normal working week | 40 hours; 8 hours/day | Version 10.07.2026, and the version from 01.01.2027 | VERIFIED | [S1][S2] Art. 139 |
| Average monthly nominal wage, Armenia | AMD 312,486 (+5.6% y/y) | Jan–Aug 2026 | VERIFIED | [S17] |
| Average monthly nominal wage, Armenia | AMD 303,140 | 2025 | VERIFIED | [S17] |
| Average wage, accommodation and food service (NACE I) | AMD 160,253 (+7.8% y/y) | Jan–Aug 2026 | VERIFIED | [S18] |
| Average wage, NACE I | AMD 150,621 (2025); AMD 142,284 (2024) | Annual | VERIFIED | [S18] |
| Average wage, NACE I, by sex | Men AMD 183,003; women AMD 144,739 | June 2026 | VERIFIED | [S19] |
| Payroll employees, NACE I | 47,156 (56% women) | June 2026 | VERIFIED | [S19] |
| Average wage, Kotayk marz (Yerevan city) | AMD 208,210 (AMD 357,583) | Q2 2026 | VERIFIED | [S19] |
| Average wage in micro firms (1–9 employees) | AMD 145,114 | July 2026 | VERIFIED | [S19] |
| Personal income tax rate | 20% flat | From 01.01.2023, current | VERIFIED | [S5] Tax Code Art. 150 |
| Funded-pension social payment (born on or after 1 Jan 1974) | 5% of gross up to AMD 500k; above that, 10% minus AMD 25,000; cap AMD 87,500 (base cap AMD 1,125,000) | 2026 | REPORTED | [S6] PwC (reviewed 30 Jun 2026) |
| Stamp duty (military insurance fund) | AMD 1,000/month (gross ≤ AMD 1m); AMD 15,000 above | From Dec 2025 | REPORTED | [S6]; corroborated by [S13] |
| UHI premium withheld from employee (2026) | AMD 0 (gross ≤200k); 4,800 (200–500k); 10,800 (>500k) | From Dec-2025 payroll | REPORTED | [S6]; consistent with [S7][S13] |
| Full annual UHI package price | AMD 129,600/year (10,800/month) | Law HO-459-N of 17.12.2025 | REPORTED | [S12][S14] |
| Draft employer UHI levy (gross ≤ AMD 200k per employer) | Employer AMD 4,400 + employee AMD 2,000 + state AMD 4,400 per month | From Dec-2026 payroll, if adopted | REPORTED (draft) | [S7] Art. 22(2); [S14] |
| Mandatory employer social contributions | None in 2026 (employer cost = gross) | 2026 | VERIFIED (by absence in law) / REPORTED | [S6]; Armstat methodology note [S17] |
| Overtime / night / holiday premiums | ≥ +50% / ≥ +30% (22:00–06:00) / ≥ 2× | Current | VERIFIED | [S1] Arts. 148, 184, 185 |
| Annual minimum paid leave | 20 working days (5-day week); 24 (6-day week) | Current | VERIFIED | [S1] Art. 159 |
| Non-working public holidays | 13 days/year | Holidays Law, version from 24.07.2026 | VERIFIED | [S4] |
| Unemployment rate (Labour Force Survey) | 13.0% (prelim.); 12.3% a year earlier | Q2 2026 | VERIFIED | [S20] |
| Registered jobseekers per vacancy (state employment service) | 9 | June 2026 | VERIFIED | [S20] |
| Live job.am ads by location | Yerevan 1,039; Abovyan 34; Sevan 2; Hrazdan 1; Charentsavan 0 | 10 Oct 2026 snapshot | VERIFIED (site count) | [S24] |
| NACE I jobs created / eliminated | 8.9k / 8.9k | 2025 | VERIFIED | [S21] |
| Population: Abovyan / Hrazdan / Sevan / Charentsavan | 51.5k / 50.1k / 19.5k / 24.1k | 1 Jul 2026 | VERIFIED | [S22] |
| Employer cost per AMD 1 of net pay (net 200k / 250k / 350k) | 1.372 / 1.364 / 1.355 | 2026 rules | ESTIMATE | §3.5 |
| job.am posting price | AMD 21,900 per ad; AMD 59,900 for 3 | Oct 2026 list price | VERIFIED (list price) | [S25] |
| Labour cost, lean format (07–22, 3 per shift, ≈10.3 FTE) | AMD 3.31m/month ($9.1k); range 2.76–3.86m | 2026 rules, base wages | ESTIMATE | §3.9 |

---

## 3. Detailed findings and analysis

### 3.1 Minimum wage: level and outlook

- **Level (VERIFIED [S3]).** The Law on the Minimum Monthly Wage (HO-66-N, 17.12.2003) currently reads:
  - Art. 1: "the minimum monthly wage is set at AMD 75,000";
  - Art. 2: the minimum hourly rate for piece-rate or hourly workers is AMD 450 on a 40-hour week, AMD 750 on a week of up to 24 hours, and AMD 500 on a 36-hour week.

  The version history shows the last change came from HO-501-N (07.12.2022), effective 01.01.2023, with no later amendment. IRTEK's other acts were updated to Jul–Sep 2026, so the database is current. PwC also cites AMD 75,000 effective 1 Jan 2023 [S6].
- **What the minimum excludes.** Labour Code Art. 179 and Min-Wage Law Art. 4: the minimum is **gross**, before tax. Premiums, bonuses and allowances do not count towards it. At the minimum, an employee born 1974 or later takes home **AMD 55,250** (75,000 − 15,000 income tax − 3,750 pension − 1,000 stamp duty). ESTIMATE, rules in §3.4.
- **Planned increases.** None is enacted.
  - In November 2021 the Ministry of Labour said the minimum would reach AMD 85,000 "by 2026" (REPORTED [S16]). Only the 2023 step, to AMD 75,000, happened.
  - e-draft 8114 (Dec 2024/Jan 2025) would cut the normal week to 35 hours and raise the hourly minimum to AMD 515 (Min-Wage Law Art. 2) "while preserving pay". It is still listed as "under discussion" [S9]. The Labour Code version that IRTEK says takes effect on 01.01.2027 still sets 40 hours (Art. 139) [S2].
  - I could not check the draft 2027 state budget for a minimum-wage line. This is a gap (§5).
- **Relevance.** Minimum-wage risk is low for full-time staff. If the 35-hour reform were ever adopted, the effective hourly cost of salaried staff would rise by **about 14%** (40/35; ESTIMATE) because pay is kept while hours fall. Treat this as a low-probability tail risk for years 3–5 of the model.

### 3.2 Average wages: national, sector and region (Armstat, latest)

Armstat calculates wages from the State Revenue Committee (SRC) database of income tax and social payments. Figures are **gross**, cover employers with at least one paid employee, and include part-timers and external part-time staff [S17][S19].

| Indicator (AMD/month, gross) | Value | Period | Note |
|---|---|---|---|
| Armenia, all activities | 312,486 | Jan–Aug 2026 | +5.6% y/y; Aug 2026 = 314,196 |
| Armenia, all activities | 303,140 / 287,172 | 2025 / 2024 | +5.6% / +6.4% |
| Accommodation and food service (I) | **160,253** | Jan–Aug 2026 | +7.8% y/y (Jan–Aug 2025: 148,707); Aug 2026 = 165,472 |
| Accommodation and food service (I) | 150,621 / 142,284 | 2025 / 2024 | +5.9% in 2025 |
| I: men / women | 183,003 / 144,739 | June 2026 | Ratio 1.26 |
| Other services (S); education (P) | ≈157.4k; ≈178.9k | Jan–Jul 2026 | The only sectors near or below I (REPORTED by ARKA [S15], citing Armstat) |
| Kotayk marz / Yerevan / Gegharkunik | 208,210 / 357,583 / 158,949 | Q2 2026 | Kotayk ≈ two-thirds of the national average |
| Micro firms (1–9 employees) / large firms (250+) | 145,114 / 449,072 | July 2026 | Pay rises steeply with firm size |

How to read this:
1. Hospitality is the second-lowest-paid sector, at **51%** of the national average (ESTIMATE: 160,253 / 312,486).
2. Its wage growth is now **faster than the national average** (+7.8% against +5.6%). The model's base wage growth of 7% a year is reasonable; 8% is a prudent "conservative" case.
3. The **official sector average sits well below advertised full-time rates** (§3.3). Three things pull the average down: part-timers, micro-firms and the regions. Under-reporting also does: the Prime Minister has said shadow employment is highest among salaries below AMD 200,000 (REPORTED [S13]). A formal, full-time, premium employer should not budget at the Armstat average.

### 3.3 Job-board evidence (concrete postings, Sep–Oct 2026)

**Sample.**
- job.am: all 1,197 live ads in its RSS feed on 10 Oct 2026. 131 were hospitality or retail-service roles; **58 (44%) showed a numeric salary**, of which 47 were monthly, 9 daily and 2 hourly.
- staff.am: the "Tourism/Hospitality/HoReCa" category had 36 live ads, **6 (17%) with a salary**.
- list.am and hr.am were not reachable (see the method note).

All figures are advertised (REPORTED). The "Gross/net" column records what the ad itself says; "not stated" means the ad gives no indication.

| # | Role | Employer | Location | Advertised pay | Schedule | Posted | Gross/net | URL |
|---|---|---|---|---|---|---|---|---|
| P1 | Barista-cashier | Cofix Armenia | Yerevan | **Not disclosed** | 6/1, 8-hour shifts, 3 shifts (all required) | 08 Oct 2026 | — | https://job.am/en/job/barista-gandzapah-80047 |
| P2 | Barista-cashier | Coffee House Company | Yerevan | **Not disclosed** ("competitive") | 6-day; shifts 09:00–17:00 / 17:00–24:00 | 02 Oct 2026 | — | https://job.am/en/job/barista-gandzapah-79815 (also https://staff.am/en/jobs/sales-management/barista-cashier) |
| P3 | Cashier / customer service | FEIN by Coffee House | Yerevan | **AMD 7,000/day + tips + % of sales** | 6-day; 08:00–16:00 / 16:00–24:00 | 29 Sep 2026 | not stated | https://job.am/en/job/gandzapah-hachaxordneri-spasarkman-masnaget-71233 |
| P4 | Senior barista / manager | Coffinity | Yerevan (Arabkir) | **AMD 12,000/shift + tips + % of sales** | Shifts 09:00–21:00 | 11 Sep 2026 | not stated | https://job.am/en/job/avag-barista-menejer-73870 |
| P5 | Cashier-barista | Nero Bean | Yerevan | **From AMD 7,500/day** | 5-day, day shift | 12 Sep 2026 | not stated | https://job.am/en/job/gandzapah-barista-79043 |
| P6 | Sales assistant-barista | COFFEE BURMUNQ | Yerevan (Kentron) | **AMD 140,000 fixed + %** | Every other day, 09:00–21:00 (12 h) | 23 Sep 2026 | not stated | https://job.am/en/job/vacharoghuhi-barista-79329 |
| P7 | Cashier | SAS Food Court | Yerevan | **AMD 170,000–200,000/month** | 6-day; 09:00–17:00 / 17:00–01:00; **ride home after the evening shift** | 14 Sep 2026 | not stated | https://job.am/en/job/gandzapah-71700 |
| P8 | Cashier | Queen Burger | Yerevan (Kentron) | **AMD 200,000–210,000/month** | Shifts (tagged part-time) | 29 Sep 2026 | not stated | https://job.am/en/job/gandzapah-70159 |
| P9 | Restaurant cashier | Little Bali | Yerevan | **AMD 9,000/shift** (paid monthly) | 2/2; 12:00–22:30 | 05 Oct 2026 | not stated | https://job.am/en/job/gandzapah-restoranum-61076 |
| P10 | Cashier | Piazza Italia | Yerevan | **AMD 150,000–200,000/month** | 6-day; 8-hour shifts | 17 Sep 2026 | not stated | https://job.am/en/job/gandzapah-79191 |
| P11 | Cashier-seller | Brabion Flora Service | **Abovyan** | **AMD 8,000–10,000/day** | 5-day | 17 Sep 2026 | not stated | https://job.am/en/job/gandzapah-vacharogh-79249 |
| P12 | Fuel-station cashier | Gulf Armenia | Ashtarak | Not disclosed | **12-hour shifts 08:00–20:00 / 20:00–08:00, then 2 days off** | 23 Sep 2026 | — | https://job.am/en/job/gandzapah-vacharogh-q-ashtarak-79298 |
| P13 | Shawarma/grill cook | SAS Food Court | Yerevan | **AMD 235,000–270,000/month** | 6-day | 14 Sep 2026 | not stated | https://job.am/en/job/shaurmayi-manghali-xoharar-74250 |
| P14 | Senior cook | Arzhi | Yerevan | **AMD 300,000–350,000/month** | 6-day, 09:00–17:00 | 01 Oct 2026 | not stated | https://job.am/en/job/avag-xoharar-79775 |
| P15 | Cook | Checkin | **Abovyan** | **AMD 12,000–15,000/day** (hourly basis, paid every 15 days) | Shifts | 14 Sep 2026 | not stated | https://job.am/en/job/xoharar-79089 |
| P16 | Cook | DEMARIA LLC | Yerevan (Avan) | **AMD 12,000–15,000/day** | Shifts 09–21 / 10:30–22:30 / 12–24 | 28 Sep 2026 | not stated | https://job.am/en/job/xoharar-79609 |
| P17 | Pizza cook | Mozzo LLC | Yerevan (Arabkir) | **From AMD 1,000/hour** | 09:00–17:00 or 17:00–23:00 | 14 Sep 2026 | not stated | https://job.am/en/job/piccayi-xoharar-77108 |
| P18 | Waiter | Vega World | **Abovyan** | **From AMD 250,000/month** | 6-day, 11:00–23:00 in shifts | 15 Sep 2026 | not stated | https://job.am/en/job/matucogh-79141 |
| P19 | Waitress | SoHo Patisserie | Yerevan | **AMD 165,000–195,000/month** | 6-day, shifts | 27 Sep 2026 | not stated | https://job.am/en/job/matucogh-uhi-79594 |
| P20 | Cleaner | CreedRoomz | Yerevan | **AMD 135,000/month NET** ("մաքուր", i.e. "clean" or net) | 12-hour shifts (09:30–21:30 / 21:30–09:30), then 2 days off | 29 Sep 2026 | **NET** | https://job.am/en/job/maqruhi-71461 |
| P21 | Cleaner (roadside restaurant) | PRIME MEAT | **Verin Ptghni, M4, near Abovyan** | **From AMD 300,000/month** | Shifts, 10:30–23:00 | 10 Sep 2026 | not stated | https://job.am/en/job/maqruhi-78959 |
| P22 | Cleaner | Brabion Flora Service | **Abovyan** | **AMD 5,000–10,000/day** | 5-day | 03 Oct 2026 | not stated | https://job.am/en/job/maqruhi-79836 |
| P23 | Cleaner (apartments) | Artur Hovhannisyan (sole trader) | Yerevan | **AMD 220,000/month** | — | 23 Sep 2026 | not stated | https://staff.am/en/jobs/other-services/cleaner-apartment-cleaning-specialist |
| P24 | Night delivery coordinator (shift lead type) | PaPa Pizza | Yerevan | **AMD 286,000–350,000** (from AMD 11,000/day fixed + bonus) | 6-day, 02:00–10:00; **taxi paid by employer** | 10 Sep 2026 | not stated | https://job.am/en/job/araqman-hamakargogh-gisherayin-hertapox-42381 |
| P25 | Fuel-station manager | Max Station | Yerevan | **AMD 400,000–450,000/month** | Mon–Fri 08:00–16:20, Sat 09:00–12:00 | 17 Sep 2026 | not stated | https://job.am/en/job/benzalcakayani-karavarich-79250 |
| P26 | Front-desk supervisor | Messier 53 Hotel | Yerevan | **AMD 200,000–230,000/month** | 5-day | 30 Sep 2026 | not stated | https://job.am/en/job/front-desk-supervisor-79751 |
| P27 | Café manager | FEIN by Coffee House | Yerevan | **Not disclosed** ("competitive" + benefits) | Flexible | 24 Sep 2026 | — | https://staff.am/en/jobs/tourism/fein-cafe-manager-3 |
| P28 | Branch manager | Coffee House Company | Yerevan | **Not disclosed** | — | 05 Oct 2026 | — | https://staff.am/en/jobs/sales-management/manager-873 |
| P29 | Restaurant administrator | Thai Home | Yerevan | **AMD 150,000–200,000/month** | Full or part time | 08 Oct 2026 | not stated | https://job.am/en/job/administrator-80032 |
| P30 | Cashier-seller (furniture retail) | SHKAFF | Masis | AMD 200,000–250,000/month | 6-day | 10 Sep 2026 | **GROSS** ("registered salary, taxes included") | https://job.am/en/job/gandzapah-vacharogh-uhi-78965 |

**Pay conversions** (ESTIMATE):
- **P3**: 7,000 × 26 shifts = **AMD 182k/month** before tips.
- **P4**: 12,000 per 12-hour shift. On a 2/2 pattern (about 15 shifts) ≈ **AMD 180k**; at 26 shifts ≈ AMD 312k.
- **P9**: 9,000 × 15 shifts = **AMD 135k**.
- **P15/P16** cooks: 12–15k × 26 = **AMD 312–390k**; × 15 = AMD 180–225k.
- **P17**: 1,000/h × 8 h × 26 = **AMD 208k**.

**Gross or net?**
- The salary field never says. Across the whole 1,197-ad feed, only five ads say so in the text:
  - net: P20, and an assembly-worker ad quoting "AMD 88,500, taxes deducted (net)" (https://job.am/en/job/jermakargavorichneri-havaqman-artadramasi-ashxatakcuhi-79251, 17 Sep 2026);
  - gross: P30, a donor-agency programme manager ("salary includes taxes", https://job.am/en/job/cragreri-menejer-78647) and a Peace Corps facilitator ("AMD 25,562 gross per day", https://job.am/en/job/language-cultural-facilitator-lcf-79232).
- So there is **no reliable convention**. The two explicit blue-collar ads were net; the white-collar and formal-retail ones were gross.
- **Base case (ASSUMPTION): read hospitality ads as net.** Workers compare net, "on-hand" pay, and per-shift cash-like rates (P3–P5, P9) are almost certainly understood as net. The −27% "ads are gross" case is shown in §3.9 as a sensitivity.
- Verify by asking 3–5 operators directly (§5).

**Other patterns that matter for the concept** (REPORTED, from the ads above):
- **Pay structure.** A per-shift rate plus tips plus % of sales is common in coffee shops (P3, P4, P6). That makes it easy to tie part of pay to drive-thru throughput.
- **12-hour shifts on 2/2 or "every other day" patterns are widespread** (P4, P6, P9, P12, P20). They are legal only with summarised working-time accounting and a 12-hour daily cap that includes breaks (Labour Code Arts. 139(3) and 143; §3.6).
- **Late-shift transport and meals are standard benefits.**
  - P7 drives staff home after the evening shift; P24 pays a taxi.
  - Deda Bistro and Coffeeshop Company state "staff meals and transport are provided" (https://job.am/en/job/matucogh-matucoghuhi-79662, https://job.am/en/job/matucogh-matucoghuhi-79077).
  - Kotayk employers run their own buses: MODUS GRANUM in Yeghvard collects staff "from Yeghvard, Ashtarak and Yerevan" (https://job.am/en/job/hashvetar-hashvapah-71335); Bacon Product in Abovyan offers "transport to the factory and back" (https://job.am/en/job/krtser-produkt-menejer-79030).
- **Pay for managers in branded cafés is not public.** Comparable published anchors are a fuel-station manager at AMD 400–450k (P25), a mall director at AMD 500–600k (https://staff.am/en/jobs/business/mall-director, 11 Sep 2026) and a hotel front-desk supervisor at AMD 200–230k (P26).

**Derived planning wages (net, full-time, 2026; ASSUMPTION anchored on the ads):**

| Role | Low | Base | High | Anchor ads |
|---|---|---|---|---|
| Crew (barista, cashier, window) | 150k | **180k** | 210k | P3, P5, P7, P8, P10, P19 |
| Shift supervisor | 220k | **260k** | 300k | P4, P24, P26 |
| Store manager | 320k | **400k** | 480k | P25, mall director |
| Cook / food prep (if hot food) | 200k | **240k** | 280k | P13, P14, P15–17 |
| Cleaner (full time) | 120k | **140k** | 160k | P20, P22 (P21 is an outlier) |

### 3.4 Payroll tax mechanics in 2026, and what changes in 2027

| Item | Who bears it | Rate or amount (2026) | Status / source |
|---|---|---|---|
| Personal income tax | Employee (withheld by employer as tax agent) | **20%** of gross (flat since 01.01.2023). A 10% rate applies only to certified R&D/high-tech staff | VERIFIED [S5] Art. 150 |
| Funded-pension social payment | Employee, born on or after 1 Jan 1974 (not mandatory for older staff) | Gross ≤ AMD 500k: **5%**. Above: **10% × gross − AMD 25,000**, maximum AMD 87,500 (base cap AMD 1,125,000 = 15 × minimum wage) | REPORTED [S6]. Pension law text not opened (arlis down) |
| Stamp duty (military insurance fund) | Employee | **AMD 1,000/month** if gross ≤ AMD 1,000,000; AMD 15,000 above (from Dec 2025). Previously up to AMD 5,500 for AMD 200–500k earners; the AMD 4,500 cut was redirected to health insurance | REPORTED [S6][S13] |
| Universal health insurance (UHI) premium | Employee (2026) | Gross ≤ AMD 200k: **0** in 2026. AMD 200–500k: **AMD 4,800/month** (state adds 6,000). Above AMD 500k: **AMD 10,800** (the full package, AMD 129,600/year) | REPORTED [S6][S7][S12][S13] |
| Employer social / payroll contributions | Employer | **None in 2026.** Armenia moved employer social contributions into gross pay in 2013 (Armstat methodology note [S17]) | VERIFIED / REPORTED |
| **Draft from Dec-2026 payroll:** UHI for employees earning ≤ AMD 200k gross per employer | **Employer AMD 4,400** + employee AMD 2,000 (state AMD 4,400) | The employer also pays if a month's salary is too small to cover the premium | REPORTED (draft, e-draft 10624, "under discussion"; presented by the Minister on 21 Aug 2026) [S7][S14] |
| Possible 2027 rule for gross > AMD 200k | Employee | The PM said in Nov 2025 that from 1 Jan 2027 these earners "will pay the annual cost of the package". Draft 10624 keeps AMD 4,800 for workers moving from ≤200k into 200–500k, but its point (3) says "100% of the monthly rate if salary ≥ AMD 200,001" | **Ambiguous**, so treated as a sensitivity |

Legal basis for UHI:
- Law "On Universal Health Insurance" HO-459-N of 17.12.2025, amended by HO-135-N of 07.04.2026 [S7][S11].
- Phase 1 started on 1 Jan 2026 (state-funded groups plus employees earning more than AMD 200k). Employees earning AMD 200k or less join from **2027**, and the whole population by 2029 [S12][S14].
- Contribution rates are fixed in AMD and can change only by law [S8].

**Other employer obligations**:
- Pay wages at least monthly, by the 15th of the following month (Labour Code Art. 192 [S1]).
- Pay annual leave at average earnings at least 3 days before the leave starts (Art. 169).
- From **1 July 2027**, employment contracts are to be concluded through the state **digital employment-contract system** (Art. 102.1). Art. 95.1, added 13.02.2026, keeps paper only for foreigners awaiting residence documents [S1]. That is an inference from the text; verify with the Health and Labour Inspection Body.
- Sick pay: the employer-funded share (if any) of temporary-disability benefit was **not verified** (§5).

### 3.5 Employer cost per AMD of net salary: worked examples

**Formula.** In the gross band AMD 200,001–500,000, with the employee born 1974 or later:

Net = Gross × (1 − 0.20 − 0.05) − 1,000 (stamp duty) − 4,800 (UHI)

so Gross = (Net + 5,800) / 0.75. In 2026 the employer cost equals the gross. ESTIMATE, using the 2026 rules in §3.4; the calculation script is in the scratchpad.

| Target net (AMD) | Gross (AMD) | Income tax 20% | Pension | Stamp | UHI (employee) | **Employer cost (AMD)** | **Cost per AMD 1 net** | Employer cost (USD) |
|---|---|---|---|---|---|---|---|---|
| 200,000 | 274,400 | 54,880 | 13,720 | 1,000 | 4,800 | **274,400** | **1.372** | $758 |
| 250,000 | 341,067 | 68,213 | 17,053 | 1,000 | 4,800 | **341,067** | **1.364** | $942 |
| 350,000 | 474,400 | 94,880 | 23,720 | 1,000 | 4,800 | **474,400** | **1.355** | $1,311 |

Variants (ESTIMATE):
- **Employee born before 1974** (no mandatory pension): gross and cost = 257,250 (1.286); 319,750 (1.279); 444,750 (1.271).
- **2027 sensitivity: full AMD 10,800 premium withheld above AMD 200k**, with the employer holding net pay constant: 282,400 (1.412); 349,067 (1.396); 482,400 (1.378). That is **2–3% above 2026**.
- **Low-wage band under the 2027 draft.** Net AMD 140,000 needs gross AMD 190,667 (net = 0.75 × gross − 3,000). Employer cost is **AMD 195,067 (1.393)**, against AMD 188,000 (1.343) in 2026: **+3.8%**.
- **Notch at AMD 200,000 gross (2026).**
  - Gross 200,000 gives net 149,000; gross 200,001 gives net 144,201.
  - The employee's net is restored only at **gross 206,400**.
  - Under the 2027 draft, staying at or below AMD 200k also costs the employer AMD 4,400/month.
  - **Avoid gross pay between about AMD 195k and 207k** for full-time crew.
- **Net-pay range in one line (2026):** from AMD 150k to 350k net, employer cost is **1.36–1.39× net**. Below a net of about AMD 149k it is 1.34×.

### 3.6 Labour Code rules relevant to drive-thru operations

All VERIFIED from the IRTEK text of the Labour Code, version 10.07.2026–01.01.2027 [S1]. Article numbers are given for legal review.

| Topic | Rule (summary) | Article(s) | Operational implication |
|---|---|---|---|
| Normal hours | At most 40 hours/week and 8 hours/day. The maximum including overtime is 12 hours/day (breaks included) and 48 hours/week. Staff on 2+ contracts are limited to 12 hours/day in total | 139 | Two 8-hour shifts cover a 16-hour day. 9-hour shifts need summarised accounting |
| 5-day or 6-day week | A 5-day week is the default; a 6-day week (1 rest day) is allowed where needed | 142 | Leave entitlement depends on the choice (20 or 24 working days) |
| Summarised working time | Allowed where daily or weekly norms cannot be kept. Hours must not exceed the norm over the reference period, which is at most 6 months. Banned for under-18s. Excess hours are compensated by time off or overtime pay | 143 | Makes 9-hour, 12-hour and 2/2 rosters lawful if total hours stay within the norm |
| Breaks | 30 minutes to 2 hours, given no later than 4 hours into the shift. Breaks are unpaid and not working time. Where a break is impossible, the employee must be able to eat at work | 152 | Budget 8.5 hours on site per 8 paid hours, or stagger breaks |
| Rest | At least 11 hours between shifts; at least 35 hours of continuous weekly rest. Food-service businesses may set their own rest days; in continuous operations the 2 rest days must be consecutive | 154, 155 | Constrains closing-to-opening "clopen" shifts on an 06:00–23:00 schedule |
| Overtime | Only in exceptional cases or with written consent. At most 4 hours in 2 consecutive days and 180 hours/year. Banned for under-18s and for students on school days | 144–146 | OT cannot be a structural staffing tool |
| Night work | 22:00–06:00. Banned for under-18s. Pregnant women and parents of children under 3 only with consent | 148 | Shifts ending after 22:00 or starting before 06:00 attract the premium |
| Premiums | OT: at least +50% of the hourly rate. Night: at least +30% per hour | 184 | Night premium ≈ AMD 429 per hour on AMD 247.7k gross |
| Public holidays | No work on non-working holidays except where needed to serve the public. Work on scheduled holidays is paid **at least 2×**. Unscheduled rest-day or holiday work: at least 2×, or another paid day off | 156, 185 | 13 holidays add ≈ 3.6% to shift payroll if the unit opens every day |
| Annual leave | At least **20 working days** (5-day week) or **24** (6-day week), not reduced for part-time or summarised schedules. Paid at average earnings, at least 3 days before it starts. No cash in lieu except on termination | 158–159, 169–170 | Built into the FTE factor (§3.9) |
| Part-time | By agreement; paid pro rata; no cut to leave or seniority | 141, 187 | Peak-hour part-timers are legal. Hourly minimum AMD 450 [S3] |
| Minors and students | 16–18: at most 36 hours/week; 15–16: at most 24 hours. No night work, overtime or summarised accounting; 2 rest days a week; no probation. **Under-18s may not sell energy drinks, alcohol or tobacco.** Contracts with under-16s must be temporary | 17.1, 140, 91, 143, 148, 155, 257 | Recruit 18+ for crew. Students 18+ are ordinary part-timers |
| Probation | At most 3 months (up to 12 only where a law allows). Either side may end it with 3 days' written notice | 91–93 | Use the 3-month probation for all crew |
| Fixed-term contracts | Only where the nature of the work requires it. Renewal, or a re-hire for the same job within 1 month, turns the contract into an open-ended one | 95 | Avoid rolling fixed-term crew contracts |
| Resignation | 30 days' written notice by the employee (5 days in specific cases) | 112 | — |
| Dismissal notice and severance | Liquidation or redundancy: 2 months' notice and **1 month's average pay** as severance. Unsuitability or long illness: 14 days' notice (tenure under 1 year) up to 60 days, and severance of **10× average daily pay** (under 1 year) up to 44×. Missed notice is compensated per day | 113, 115, 129 | Budget about AMD 0.25m per redundant crew member, plus 2 months' notice |
| Wage payment | At least monthly, by the 15th of the next month; payslip on request | 192, 193 | — |
| Pre-holiday days | Shortened by 1 hour, **except for shift workers** | 147 | Not applicable to the shift crew |

**Public holidays (non-working days, VERIFIED [S4], Holidays Law version from 24.07.2026):**

| Date(s) | Holiday | Days |
|---|---|---|
| 31 Dec – 2 Jan | New Year | 3 |
| 6 Jan | Christmas | 1 |
| 27 Jan | Memorial Day of those who died defending the homeland | 1 |
| 28 Jan | Army Day | 1 |
| 8 Mar | Women's Day | 1 |
| 24 Apr | Genocide Remembrance | 1 |
| 1 May | Labour Day | 1 |
| 9 May | Victory and Peace | 1 |
| 28 May | Republic Day | 1 |
| 5 Jul | Constitution Day | 1 |
| 21 Sep | Independence Day | 1 |
| **Total** | | **13** |

The government may declare additional non-working days (Art. 39). Other listed days, such as Easter-linked feasts and regional days, are commemorative working days.

### 3.7 Labour availability, turnover and commuting for a highway site

**Market slack exists, but not where the site is.**
- Nationally, LFS unemployment was **13.0% in Q2 2026**, with participation at 59.9%, and **55.5% of the unemployed were long-term** (VERIFIED [S20]).
- Demand registered with the state employment service: 3,656 vacancies in June 2026, 9 registered jobseekers per vacancy. Kotayk had 173 vacancies (4.7%) and Gegharkunik 152 [S20].
- **Formal online hiring activity is concentrated in Yerevan.** On 10 Oct 2026, job.am's location filter counted Yerevan 1,039; Abovyan 34; Yeghvard 4; Nor Hachn 3; Sevan 2; Hrazdan 1; Gavar 1; Charentsavan 0; Tsaghkadzor 0 (VERIFIED [S24]).
- Local candidate pools by town population on 1 Jul 2026 [S22]:
  - Kotayk marz 299.1k: Abovyan 51.5k, Hrazdan 50.1k, Charentsavan 24.1k, Yeghvard 13.4k, Byureghavan 12.0k, Nor Hachn 10.5k.
  - Gegharkunik 217.3k: Sevan 19.5k, Gavar 18.8k.

**Distances along the M4** (internal workstream B2, OSM chainage [S27]):
- Abovyan interchanges are at about km 16 (≈10 km from the Yerevan city edge);
- Hrazdan interchanges at about km 40–48;
- the Sevan area at about km 60–74.

**Local wage competition (REPORTED, Abovyan-located ads):**
- industrial and logistics jobs: AMD 180–300k (Arzni poultry farm sorting worker AMD 180–240k; machine operators AMD 230–250k; delivery driver from AMD 250k);
- the M4-side PRIME MEAT restaurant at Verin Ptghni: **cleaner from AMD 300k**;
- Vega World: waiter from AMD 250k.

A drive-thru near Abovyan therefore competes with factory pay, **not with the Kotayk average of about AMD 208k gross**.

**Turnover.**
- Armenia publishes no hospitality turnover rate.
- Proxy (VERIFIED [S21]): accommodation and food created **8.9k jobs and eliminated 8.9k** in 2025 (7.4k and 7.5k in 2024), about 10% of all job flows. Against about 47k payroll employees in the sector [S19], that is roughly **19% gross job destruction a year** (ESTIMATE; the two surveys have different bases). That measures jobs, not people; worker quits come on top.
- **ASSUMPTION: 60–100% annual crew turnover and 25–40% for supervisors and managers.** This is typical of quick-service restaurants internationally and consistent with the daily-rate and shift-based contracts seen in the ads. Verify it in operator interviews.

**Commuting.**
- Shift changes for 06:00–23:00 trading fall at about 05:30 and 23:30. For 07:00–22:00 they fall at about 06:30 and 22:30.
- I could not verify inter-town minibus schedules at those hours (gap). Kotayk employers' habit of running their own buses (§3.3), and Yerevan restaurants' paid rides home, show that **employer transport is expected**.
- ASSUMPTION for a site between Abovyan and Hrazdan: a contracted 8–15-seat minibus making 3 runs a day costs **AMD 0.3–0.6m/month**. That covers a driver at AMD 200–300k (driver ads: https://job.am/en/job/varord-araqich-79513, from AMD 250k; https://staff.am/en/jobs/tourism/driver-109, AMD 200–300k) plus fuel and the vehicle. A site at the edge of Abovyan or Yerevan might manage with a per-shift taxi allowance.

### 3.8 Staffing model: method

| Element | Value | Basis |
|---|---|---|
| Operating format A | Open 07:00–22:00; staff on site 06:30–22:30 = **16 hours/day** as 2 × 8-hour shifts. Night hours 22:00–22:30 = 0.5 hours per position per day | ASSUMPTION (30 min to open, 30 min to close) |
| Operating format B | Open 06:00–23:00; on site 05:30–23:30 = **18 hours/day** as 2 × 9-hour shifts under summarised accounting. Night hours 05:30–06:00 and 22:00–23:30 = 2 hours per position per day | ASSUMPTION; Arts. 139, 143, 148 |
| Productive hours per FTE per year | 2,080 − 160 (20 days' leave) − 24 (3 sick days) − 16 (2 training days) = **1,880** | VERIFIED leave rule; sick and training days are ASSUMPTIONS |
| FTE needed per staffed position | A: 16 × 365 / 1,880 = **3.11**. B: 18 × 365 / 1,880 = **3.49** | ESTIMATE |
| Shift composition | n people per shift (3–6), of whom 1 is the shift supervisor; plus 1 salaried store manager on a 5-day week | ASSUMPTION |
| Premium uplift on shift payroll | Night 30% × night share, plus holidays 100% × 13/365. **A: +4.50%; B: +6.89%** | ESTIMATE (Arts. 184, 185; [S4]) |
| Wages | Net Low / Base / High from §3.3, grossed up under 2026 rules (§3.5). Ads read as net | ASSUMPTION |
| Not included | Meals and uniforms, transport, recruitment, overtime (all shown separately) | — |

Base-case gross wages, which equal employer cost in 2026:

| Role | Net (AMD) | Gross / employer cost (AMD) | USD |
|---|---|---|---|
| Crew | 180k | **247,733** | $684 |
| Supervisor | 260k | **354,400** | $979 |
| Manager | 400k | **552,571** | $1,527 |
| Cleaner | 140k | **188,000** | $519 |
| Cook | 240k | **327,733** | $906 |

### 3.9 Staffing cost scenarios (ESTIMATE, 2026 rules)

**Employer payroll cost per month, by people per shift, operating format and wage level** (AMD; USD in brackets; annual = 12×):

| Format | People/shift | FTE (crew + sup + mgr) | Low | **Base** | High | Base, annual |
|---|---|---|---|---|---|---|
| A (07–22) | 3 | 10.3 (6.2 + 3.1 + 1) | 2.76m ($7.6k) | **3.31m ($9.1k)** | 3.86m ($10.7k) | 39.7m ($110k) |
| A (07–22) | 4 | 13.4 (9.3 + 3.1 + 1) | 3.43m ($9.5k) | **4.12m ($11.4k)** | 4.79m ($13.2k) | 49.4m ($136k) |
| A (07–22) | 5 | 16.5 (12.4 + 3.1 + 1) | 4.11m ($11.4k) | **4.92m ($13.6k)** | 5.73m ($15.8k) | 59.0m ($163k) |
| A (07–22) | 6 | 19.6 (15.5 + 3.1 + 1) | 4.78m ($13.2k) | **5.72m ($15.8k)** | 6.66m ($18.4k) | 68.7m ($190k) |
| B (06–23) | 3 | 11.5 (7.0 + 3.5 + 1) | 3.11m ($8.6k) | **3.73m ($10.3k)** | 4.34m ($12.0k) | 44.7m ($124k) |
| B (06–23) | 4 | 15.0 (10.5 + 3.5 + 1) | 3.89m ($10.7k) | **4.65m ($12.9k)** | 5.41m ($15.0k) | 55.8m ($154k) |
| B (06–23) | 5 | 18.5 (14.0 + 3.5 + 1) | 4.66m ($12.9k) | **5.58m ($15.4k)** | 6.49m ($17.9k) | 66.9m ($185k) |
| B (06–23) | 6 | 22.0 (17.5 + 3.5 + 1) | 5.44m ($15.0k) | **6.50m ($18.0k)** | 7.56m ($20.9k) | 78.0m ($216k) |

**Mapping to the three formats used in the startup-cost and 5-year model:**

| Format | Configuration | FTE | Low / **Base** / High (AMD/month) | Loaded gross per shift FTE (Base) | Manager gross (Base) |
|---|---|---|---|---|---|
| **Lean** | A, 3 per shift | 10.3 (9.3 shift + 1 mgr) | 2.76m / **3.31m** / 3.86m | AMD 296,034 | AMD 552,571 (or 434,400 at net 320k) |
| **Mid** | A, 4 per shift (B, 4 per shift in brackets) | 13.4 (15.0) | 3.43 / **4.12** / 4.79m (3.89 / **4.65** / 5.41m) | AMD 286,746 (293,320) | 552,571 |
| **Flagship** | B, 6 per shift + 1 full-time cleaner | 23.0 | 5.63 / **6.69** / 7.75m | AMD 283,818 | 552,571 (+ cleaner 188,000) |

**Sensitivities** (ESTIMATE):
- **Ads read as gross** instead of net: Lean 2.41m, Mid 3.00m, Flagship 4.87m AMD/month. That is **27% lower** in each case.
- **2027 health-insurance rules.** With the full AMD 10,800 premium above AMD 200k and the employer keeping net pay unchanged: +2.3% (Lean, 3.39m), +2.5% (Mid, 4.22m), +2.8% (Flagship, 6.88m). If instead crew are paid at or below AMD 200k gross, the draft employer levy adds AMD 4,400 per such employee.
- **Demand-shaped roster.** Example for Lean: 2 core staff all day plus 1 peak helper for 6 hours (07–10 and 17–20) uses 38 instead of 48 position-hours a day, **−21% paid hours**. Lean shift FTE falls from 9.3 to about 7.4 (Mid 12.4 → about 9.8; Flagship 21.0 → about 16.6). It needs part-timers and good demand data.
- **Wage growth.** The sector grew +7.8% y/y in 2026 (§3.2). Model 7% base and 8% conservative.
- **Overtime.** Excluded. Each hour costs about AMD 2,144 at crew gross (1,429 + 50%). Capped at 180 hours per person per year.

**Labour-related costs outside payroll** (monthly):

| Item | Lean | Mid | Flagship | Basis |
|---|---|---|---|---|
| Meals and uniforms at AMD 15k per FTE | 155k | 201k | 345k | Model assumption; meals are a common benefit (§3.3) |
| Staff transport (highway site) | 300–600k | 300–600k | 450–700k | ASSUMPTION (§3.7) |
| Recruitment and onboarding at 60–100% turnover: AMD 79k per hire (AMD 21,900 job.am ad + 40 h × AMD 1,429/h) | 41–68k (6–10 hires/yr) | 53–88k | 91–152k | ESTIMATE [S25] |

**Comparison with current model inputs** (`model/assumptions.json`):

| Format | Model | This study (base) | Gap |
|---|---|---|---|
| Lean | 6 + 2 FTE at AMD 250k gross average + manager AMD 450k = **AMD 2.45m/month** | AMD 3.31m (10.3 FTE) | Model **26% lower** |
| Mid | AMD 3.98m | AMD 4.12m | 3% |
| Flagship | AMD 5.56m | AMD 6.69m | Model **17% lower** |

Reasons:
- The model's lean FTE count does not cover 2 shifts × 3 people × 7 days with leave.
- Supervisor and manager pay needs to rise if ads are net.

Recommended inputs:
- Lean: fte_base about 9.3 (or 7.4 if demand-shaped) and avg_gross about AMD 296k.
- Mid: 12.4 at about AMD 287k.
- Flagship: 21 at about AMD 284k plus a cleaner.
- Manager gross AMD 435–555k.
- Keep a "gross interpretation" toggle for the −27% case.

---

## 4. Implications for the drive-thru concept

1. **Labour will be the largest controllable operating cost, and its size depends on decisions not yet made.** Three choices move monthly payroll by 25–100%:
   - operating hours (06–23 costs about 13% more than 07–22 at the same crew size);
   - crew per shift (each extra person per shift adds about AMD 0.8–0.9m/month);
   - whether market pay is net or gross (27%).

   **The investment case should not be presented with a single labour number.** Show Lean, Mid and Flagship with the low/base/high band.
2. **Throughput per labour hour is the key operating metric.** At the base case (ESTIMATE):
   - a crew position-hour costs about **AMD 1,650** fully loaded: 247,733 / 173.3 h × (2,080 / 1,880) × 1.045;
   - a supervisor position-hour about AMD 2,365;
   - the Lean blend of 2 crew and 1 supervisor about **AMD 1,890**;
   - including the manager, about **AMD 2,270** (3.31m × 12 / 17,520 position-hours a year).

   So a Lean unit spends about **AMD 6,800 on labour for every operating hour** (3 × 2,270). For each AMD 1,000 of average order value, it needs about 6.8 orders an hour, every hour, just to cover payroll. The 5-year model should test its hourly-demand assumptions, especially off-peak, against this threshold. Demand-shaped rostering with part-time peak helpers is the main lever (−21% paid hours).
3. **Rosters must be compliant from day one.**
   - Common local practices are 12-hour "every other day" shifts and day-rate pay. They are lawful only with summarised working-time accounting, a 12-hour daily cap including breaks, 11 hours between shifts and correct night and holiday premiums.
   - A premium brand seeking investors should not carry shift-pattern or envelope-wage risk. The Health and Labour Inspection Body enforces these rules.
   - From 1 July 2027 every contract is expected to go through the state digital contract system, which makes informality more visible.
4. **Pay design around the AMD 200k gross notch.** The 2026 health-insurance rules and the 2027 draft make gross pay of about AMD 195–207k inefficient for both sides. Either pay crew at least about AMD 207k gross (net about AMD 150k), or keep part-timers well below AMD 200k and accept the AMD 4,400 employer levy from December 2026 if the draft passes.
5. **Under-18 staff are effectively excluded.** They cannot work after 22:00, cannot do overtime and cannot sell energy drinks. Recruit students aged 18 and over from Yerevan and Abovyan universities and colleges as peak part-timers.
6. **The highway location is a labour risk, not only a traffic opportunity.**
   - The formal hiring market outside Yerevan is very thin (Hrazdan: 1 live job.am ad; Sevan: 2).
   - Nearby factories and the roadside restaurant already pay AMD 200–300k and bus their staff in.
   - A site near Abovyan (≈km 16) can draw on Abovyan (51.5k people) and north-east Yerevan with a short shuttle. A site near Hrazdan or Sevan (km 40–74) depends on small towns, long commutes and very early starts.
   - **Location scoring should include a labour-access criterion:** travel time from Abovyan and north-east Yerevan, and the availability of shuttle routes.
7. **Turnover will be costly.** At 60–100% turnover, Lean recruits 6–10 crew a year, Flagship 14–23. Budget training time, a structured onboarding programme and retention pay: a speed or throughput bonus paid per shift, as local cafés already do with % of sales; meals; transport.
8. **Regulatory drift is mostly upward.** Planned or possible changes:
   - the 2027 health-insurance rules, +2–3% at constant net pay;
   - continuing wage growth of about 6–8% a year in hospitality;
   - a dormant 35-hour-week draft, a +14% hourly-cost tail risk.

   There is no near-term minimum-wage pressure. Model nominal labour-cost growth at 7% a year base, 8% conservative.

---

## 5. Data gaps and how to verify them

| Gap | Why it matters | How to verify |
|---|---|---|
| Gross vs net convention for hospitality ads | ±27% on payroll | Call 5 employers from §3.3 (FEIN/Coffee House, SAS Food Court, Queen Burger, Little Bali, Vega World) and ask "is AMD X on-hand or registered?". Ask Talentus HR or other recruiters for their hospitality salary-survey practice |
| Pay for café managers and shift supervisors at chains (Coffee House, Cofix, Gotcha, FEIN) | Manager line ≈ 15% of payroll | Confidential recruiter benchmark (Talentus HR, staff.am employer services). Candidate interviews during hiring. Mystery-shop the ads (P27, P28) |
| Funded-pension law text and current rates (5% / 10% − 25,000 / cap) | Gross-up accuracy | Read the Law "On Funded Pensions" Art. 7 on arlis.am (timed out); SRC tax calculator; or a tax adviser memo |
| Stamp-duty law amendment (AMD 1,000 from Dec 2025) | Small (AMD 0–4,500/month per employee) | Law "On Stamp Duty" on arlis.am; SRC clarification |
| Final 2027 health-insurance contribution split (draft 10624 is "under discussion"; >200k band ambiguous) | Employer levy of AMD 4,400 per low-paid employee; 2–3% cost at constant net | Track e-draft 10624 and National Assembly adoption; ask the UHI Fund (unif.am, hotline 8866) or the Ministry of Health in writing |
| Employer-paid share of sick leave (temporary-disability benefit) | About 0.3–1% of payroll | Law "On temporary disability and maternity benefits" on arlis.am; Unified Social Service |
| Minimum-wage line in the 2027 state budget and the new 2026–2031 Government Programme | Tail risk | Read the 2027 budget draft (minfin.am, parliament.am) and Government decision N 1236-A of 20.08.2026 |
| Status of the 35-hour-week draft (e-draft 8114) | +14% hourly-cost tail risk | National Assembly legislative tracker; Ministry of Labour |
| list.am and hr.am postings (not reached) | Wider sample, especially blue-collar and regional | Collect manually in a browser (list.am "Work → Job offers", filter Kotayk/Gegharkunik); 2–3 hours |
| Staff turnover in Armenian quick-service restaurants and coffee chains | Recruitment and training budget | Interview 3–5 operators (Coffee House, Tashir Pizza, Black Star, KFC Armenia franchisee, gas-station café operators); ask HR for annual turnover and average tenure |
| Commuting options at 05:30 and 23:30 on Yerevan–Abovyan–Hrazdan–Sevan | Transport budget and recruitment radius | Yerevan Municipality and Kotayk minibus route schedules; test-ride; quotes from 2–3 minibus operators for a contracted shuttle; Yandex Go fare checks at those times |
| Mandatory health certificates or medical checks for food handlers | Onboarding cost and time | Food Safety Inspection Body (fsis.am) and Ministry of Health regulations; cost from 2 Yerevan clinics |
| Cross-check of IRTEK legal texts on arlis.am | Legal certainty | Retry arlis.am, or ask counsel to confirm Labour Code Arts. 139–185 and the Holidays Law (version 24.07.2026) |

---

## 6. Sources

All accessed 2026-10-10 unless stated.

1. [S1] Labour Code of the Republic of Armenia (HO-124-N, 09.11.2004), version in force 10.07.2026–01.01.2027, IRTEK legal database: https://www.irtek.am/views/act.aspx?aid=150003
2. [S2] Labour Code, version effective 01.01.2027–01.07.2027 (Art. 139 unchanged), IRTEK: https://www.irtek.am/views/act.aspx?tid=202530
3. [S3] Law "On Minimum Monthly Wage" HO-66-N (17.12.2003), version from 01.01.2023, IRTEK: https://www.irtek.am/views/act.aspx?tid=171278 (reached via https://www.irtek.am/views/act.aspx?lid=377884)
4. [S4] Law "On Holidays and Memorial Days of the RA" HO-200 (2001), version from 24.07.2026 (as amended 03.07.2026), IRTEK: https://www.irtek.am/views/act.aspx?tid=202402
5. [S5] Tax Code of the RA, Art. 150 (income tax rates), version 01.09.2026–01.01.2027, IRTEK: https://www.irtek.am/views/act.aspx?aid=150068
6. [S6] PwC Worldwide Tax Summaries, "Armenia – Individual – Other taxes" (last reviewed 30 Jun 2026): https://taxsummaries.pwc.com/armenia/individual/other-taxes. Also "Taxes on personal income": https://taxsummaries.pwc.com/armenia/individual/taxes-on-personal-income
7. [S7] e-draft.am project 10624, Ministry of Health: draft amendments to the Law "On Universal Health Insurance" (HO-459-N of 17.12.2025), status "under discussion". Text: https://www.e-draft.am/projects/10624/about. Justification: https://www.e-draft.am/projects/10624/justification
8. [S8] e-draft.am project 9160, original draft Law "On Comprehensive (Universal) Health Insurance" (2025), Art. 13 (premium AMD 10,000–13,700/month range): https://www.e-draft.am/projects/9160/about
9. [S9] e-draft.am project 8114, drafts amending the Labour Code (35-hour week) and the Minimum Wage Law (hourly minimum AMD 450 → 515), comments dated 07.01.2025, status "under discussion": https://www.e-draft.am/projects/8114/about
10. [S10] e-draft.am project 10375, procedure for refunds of UHI premiums overpaid by tax agents (public comments 10.07.2026): https://www.e-draft.am/projects/10375
11. [S11] e-draft.am project 10280, government decision implementing UHI amendment law HO-135-N of 07.04.2026: https://www.e-draft.am/projects/10280
12. [S12] ARKA, "Парламент Армении утвердил законопроект об обязательном медстраховании…", 17 Dec 2025: https://arka.am/news/society/parlament-armenii-utverdil-zakonoproekt-ob-obyazatelnom-medstrakhovanii-reforma-vstupit-v-silu-s-202/
13. [S13] ARKA, "500 драмов в месяц за здоровье…", 5 Nov 2025 (stamp duty AMD 5,500 → 1,000; package AMD 129.6k/year; PM on shadow employment below AMD 200k): https://arka.am/news/society/500-dramov-v-mesyats-za-zdorove-v-armenii-snizyat-finansovuyu-nagruzku-medstrakhovaniya-na-naselenie/
14. [S14] ARKA, "Глава Минздрава представила проект включения в систему медицинского страхования работников с зарплатой менее 200 тыс. драмов", 21 Aug 2026: https://arka.am/news/society/glava-minzdrava-predstavila-proekt-vklyucheniya-v-sistemu-meditsinskogo-strakhovaniya-rabotnikov-s-z/
15. [S15] ARKA, "От 157 тыс. драмов до 1 млн драмов: как выглядит шкала зарплат в Армении", 7 Oct 2026 (Jan–Jul 2026 sector wages): https://arka.am/news/society/ot-157-tys-dramov-do-1-mln-dramov-kak-vyglyadit-shkala-zarplat-v-armenii/
16. [S16] ARKA, "Минимальная зарплата в Армении до 2026 года повысится до 85 тыс. драмов", 5 Nov 2021: https://arka.am/news/society/minimalnaya_zarplata_v_armenii_do_2026_goda_povysitsya_do_85_tys_dramov_/
17. [S17] Armstat, "Average monthly nominal wages, drams" (2026 monthly and 2000–2025 series; methodology notes): https://www.armstat.am/en/?nid=12&id=08001
18. [S18] Armstat, "Nominal wages/salaries by type of economic activity and public/non-public sectors (monthly)", XLSX: https://www.armstat.am/file/doc/99571893.xlsx (index page: https://www.armstat.am/en/?nid=964)
19. [S19] Armstat, "Socio-Economic Situation of RA, January–August 2026", section 1.4.2 (wages and employees by firm size, sector, sex, marz), PDF https://www.armstat.am/file/article/sv_08_26r_142.pdf and XLSX archive https://www.armstat.am/file/article/sv_08_26r_xlsx.7z (page: https://www.armstat.am/en/?nid=82&id=2841)
20. [S20] Armstat, same report, section 1.4.1 (LFS Q2 2026; labour demand by marz, June 2026): https://www.armstat.am/file/article/sv_08_26r_141.pdf
21. [S21] Armstat, "Vacant, newly created and eliminated jobs by sectors of economic activity (annual)", XLSX: https://www.armstat.am/file/doc/99571938.xlsx (page: https://www.armstat.am/en/?nid=1036)
22. [S22] Armstat, "Permanent Population of RA as of 1 July 2026": https://www.armstat.am/file/article/population_01_07_26.pdf (page: https://www.armstat.am/en/?nid=82&id=2826)
23. [S23] Central Bank of Armenia, exchange-rate web service, ExchangeRatesLatest (rates dated 2026-10-09, USD 361.93): https://api.cba.am/exchangerates.asmx
24. [S24] job.am RSS feed of all live ads (1,197 items, 10 Oct 2026): https://job.am/api/jobs/feed/. Location filter counts: https://job.am/en/jobs. Individual postings as listed in §3.3 (P1–P30) and in §3.3/§3.7 text
25. [S25] job.am employer pricing (AMD 21,900 per post; AMD 59,900 for 3 posts): https://job.am/en/pricing
26. [S26] staff.am listings: HoReCa category https://staff.am/en/jobs?category=9; keyword searches, e.g. https://staff.am/en/jobs?key_word=barista. Postings as cited
27. [S27] Internal workstream B2, M4 points of interest with OSM chainage (OpenStreetMap via Overpass, data timestamp 2026-10-10): /home/user/Drive-thru/research/B2-m4-pois.csv

*Calculation scripts (gross-up and staffing model) are in the session scratchpad (`c3calc/payroll.py`, `payroll2.py`, `staffing.py`, `sens.py`). They can be re-run with different net wages, hours or regimes.*
