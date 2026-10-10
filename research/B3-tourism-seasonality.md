# B3 — Tourism flows, seasonality and travel segments: Yerevan–Sevan corridor and Armenia

*Prepared 2026-10-10 for the premium drive-thru feasibility study. This file feeds the volume driver of the revenue model (vehicles passing × capture rate × average ticket). It supplies the monthly seasonality index, the customer-segment mix and the tourism context.*

**Status tags.**
- **VERIFIED**: I opened the primary or official file myself (URL given).
- **REPORTED**: a credible secondary source, such as news, Wikipedia, an ADB summary or a sibling research file (URL or file given).
- **ESTIMATE**: my own calculation; the formula and inputs are shown.
- **ASSUMPTION**: my judgement; the basis is stated.

**Method note.** The shared WebSearch budget for this session ran out before this topic started; the first search call was refused. I therefore did not run open web or news searches. Instead I worked from primary data that I could open directly:
- Armstat (National Statistical Committee) monthly reports, the international-tourism database and the ArmStatBank PxWeb API;
- the Central Bank of Armenia (CBA) balance of payments;
- the Migration and Citizenship Service border-crossing workbook;
- the ADB project page;
- OSRM routing on OpenStreetMap;
- Open-Meteo/ERA5 weather history.

Visitor counts for specific sites (Sevan beaches, Sevanavank, Tsaghkadzor, Dilijan), tour-bus counts and news reports of traffic surges are therefore mostly **gaps**. §5 says how to close each one. A follow-up session with search budget should start with those items.

---

## 1. Executive summary

1. **Armenia's inbound "tourist" count has plateaued at about 2.2–2.3 million a year since 2023, and 2026 is up again in H1.** VERIFIED, Armstat [1][2].

   | Year | Tourists | Note |
   |---|---|---|
   | 2019 | 1.89 m | |
   | 2020 | 0.36 m | |
   | 2023 | 2.32 m | peak, driven by Russian relocation |
   | 2024 | 2.21 m | |
   | 2025 | 2.26 m | |
   | H1 2026 | 1.04 m | +14.8 % y/y; Russia +23 %, Georgia +17 % |

   Travel receipts were **US$2.91 bn in 2025**, and H1 2026 was **+19.6 % y/y** (VERIFIED, CBA [10]).
2. **The headline count overstates the sightseeing market.**
   - The average stay in 2025 was **29 nights**.
   - **14 % of "tourists" are Armenian citizens**, mostly diaspora, with an average stay of 63 nights.
   - **41 % are Russian citizens** (average stay 25 nights).
   - Only **about 16 % (~0.37 m)** come from nationalities whose average stay is ≤18 nights, the classic short-stay sightseeing profile (ESTIMATE from VERIFIED [1]).
   - **≈0.6–1.0 m international visitor-trips a year pass Sevan** (point estimate ≈0.81 m; the 2023 International Visitor Survey found that 35.8 % of tourists visit Gegharkunik; REPORTED [18]). Most of them are long-stay and diaspora visitors. The short-stay sightseeing pool within that is ~0.37 m. *Fact-check correction: this bullet previously said the Sevan-passing day-tour segment "is a few hundred thousand people a year, not 2.3 million". That contradicted §3.6, which sizes it at 0.57–1.02 m, and appears to have conflated the ≤18-night pool (0.37 m) with all Sevan visitors.*
   - **Per-day spending is only moderately higher for sightseers** (IVS 2023, REPORTED [18]). The survey average was US$50.8/day. Leisure visitors spent US$61.8/day (≈1.2× the average and 1.5× visitors to friends and relatives, at US$42.1). Only package tourists (5.4 % of visitors) spent far more, at US$193/day (≈4×). *Fact-check correction: added; see §3.3.*
3. **Tourism is concentrated in Yerevan. The corridor regions capture only a small share.** VERIFIED [7][9].

   | Region | Hotel revenue share, 2025 | Accommodation + food-service turnover share, 2024 |
   |---|---|---|
   | Yerevan | 78 % | 81 % |
   | Kotayk (Tsaghkadzor, Abovyan, Hrazdan) | 7.6 % | 8.9 % |
   | Tavush (Dilijan) | 5.1 % | 2.1 % |
   | Gegharkunik (all of Lake Sevan) | **1.8 %** | **1.2 %** |

   The Sevan basin is a summer day-trip destination, not an overnight economy. Gegharkunik hotels nonetheless tripled from 39 to 118 between 2019 and 2025.
4. **Seasonality is pronounced, and it gets stronger the further a site is from Yerevan.** Each indicator below is shown with its peak-to-trough ratio (2024–25):

   | Indicator | Peak month (index) | Trough month (index) | Peak/trough | Status |
   |---|---|---|---|---|
   | Inbound tourists | Q3 = 36.5 % of the year | — | — | VERIFIED |
   | Bagratashen road crossings (Georgia) | Aug 164 | Feb 55 | 3.0× | ESTIMATE from VERIFIED [3] |
   | Gogavan road crossings | Aug 189 | Feb 43 | 4.4× | ESTIMATE from VERIFIED [3] |
   | National accommodation & food turnover | Aug 118 | Feb 73 | 1.6× | ESTIMATE from VERIFIED [4] |
   | Motor/household fuel retail | — | — | ~1.3× | ESTIMATE from VERIFIED [4] |
5. **My corridor seasonality index (mean = 100; ESTIMATE, built from components) has three variants by segment:**

   | Segment | Jan | Aug | Peak/trough | Jun–Aug share of annual traffic |
   |---|---|---|---|---|
   | **A. Yerevan edge–Charentsavan** | 86 | 125 | 1.5 (range 1.44–1.55) | 29 % |
   | **B. Hrazdan–Sevan** | 69 | 151 | 2.3 (range 2.0–2.7) | 34 % |
   | **C. Sevan–Dilijan** | 67 | 159 | 2.6 (range 2.2–3.0) | 35 % |

   - Segment A's July value (122) is close to the M-1 counter's +19.7 % in July (B1). That is only a **loose plausibility check**: the M-1 data are Roads Department figures of ~2005–09 (period inferred) for a different corridor with no Sevan or Tsaghkadzor leisure overlay. The real validation will be the 7-day summer and February counts (§5). *Fact-check correction: previously presented as a validation.*
   - The model placeholder (Jan 0.66, Aug 1.46) matches segment B. It overstates seasonality for a Yerevan-edge site.
6. **The Sevan beach season is short.** Coastal water reaches ~21 °C only in July–August (21.2 °C in both months of 2026), and it was 15.4 °C in October 2025 (VERIFIED, Armstat/Hydromet [6]). The swimming peak is about **8–12 summer weekends (~16–24 weekend days)**, ending around Independence Day (21 Sept). *Fact-check correction: this peak definition is now used consistently in §1.11 and §4.2, which previously said "~10–14 weekends" and "~10–14 weekend days".*

   Winter at Sevan (~1,940 m) is long and hard (ESTIMATE, Open-Meteo/ERA5 2016–25 [14]):

   | Indicator | Value |
   |---|---|
   | January mean temperature | −6.1 °C |
   | Frost days per year | ~160 |
   | Days per year with ≥1 cm snowfall | ~32 |
   | Days per year at or below −15 °C at the tunnel approach | ~20 |
7. **The Georgia link is a real but secondary contributor to M-4 traffic.**
   - Bagratashen, the main Georgia road crossing, recorded **1.40 m entries and 1.39 m exits in 2025** (≈7,650 persons/day two-way; VERIFIED [3]).
   - ADB says the crossing handles **80 % of Armenia's imports and exports** (REPORTED [12]). ADB does not say whether this is by value or volume, or which modes it covers.
   - OSRM puts Yerevan→Bagratashen via **M-4 Sevan–Dilijan–Ijevan at 3 h 26 min**, against 3 h 33 min via Aparan–Vanadzor–Alaverdi, a near tie (ESTIMATE [13]). Georgia traffic therefore splits between the M-4 and the M-3/M-6 route.
   - **Upper bound: ~1,200–2,100 Georgia-related vehicles/day two-way on the Sevan–Dilijan link.** Of these, ~400–700 are trucks, itself an upper-range figure (ESTIMATE, wide range). *Fact-check correction: previously a "base estimate". The 35–60 % M-4 share was applied to all Bagratashen crossers as if all were Yerevan-bound. But 58 % of 2025 entries (813,588 of 1,404,774) were on Armenian documents, and many are Tavush/Lori residents who never reach the Dilijan tunnel. The truck figure rests on applying ADB's unqualified 80 % to road tonnes (ASSUMPTION). See §3.6.*
8. **Commuters, not tourists, are the stable base close to Yerevan.**
   - The M-4 corridor towns had **167,262 residents on 1 Jan 2025**: Abovyan 50.6k, Hrazdan 49.5k, Charentsavan 24.1k, Sevan 19.7k, Byureghavan 11.8k, Nor Hachn 10.5k, Tsaghkadzor 1.1k (VERIFIED [9]).
   - Base estimate: **12–20k daily commuters to Yerevan**, or **≈3–8k car trips per direction per weekday** (ESTIMATE).
   - These commuters drive into Yerevan in the morning, on the Yerevan-bound carriageway.
9. **Domestic leisure is the swing segment, and its bottom-up size undercuts high corridor AADTs.**
   - Yerevan has ~142k car-owning households (ESTIMATE; the 41.2 % national household car-ownership rate is applied to Yerevan and household size is assumed at 3.3). If 50–75 % of them make 2–5 basin trips a year, they generate **0.14–0.53 m car round trips/yr**. An uplift of ×1.05–1.40 for other regions' households and taxis (ASSUMPTION) gives **~0.15–0.75 m**.
   - On the Hrazdan–Sevan segment that is **~5–24 % of B1's base AADT of 17,000**, not the 30–40 % that a "leisure highway" story implies. *Fact-check correction: previously "6–24 %": 0.15 m × 2 ÷ 365 = 822 passes/day = 4.8 %. The uplift for other regions and taxis is now shown explicitly, and the household count is labelled as using national car ownership.*
   - Either B1's AADT for that segment is high, or the corridor is more regional/business than leisure. Counts must settle this.
10. **2026 risk signals.**
    - Meghri (Iran) road crossings fell **31 % y/y in Jan–Jul 2026** (−32 % Jan–Aug; VERIFIED [3]). Over the same Jan–Jul period, Bagratashen was **+3.1 %** and Zvartnots **+11.6 %**. *Fact-check correction: the trend now uses Jan–Jul, which excludes the suspect August data. On a Jan–Aug basis, Bagratashen shows −1.3 %, so the sign flips.*
    - Russia supplies 40 % of tourists and is the main tourism exposure.
    - The August 2026 border figures look incomplete: entries fell 15–18 % y/y at Zvartnots and Bagratashen while air passengers rose 14 %. **Treat August 2026 as preliminary.**
11. **Bottom line for the concept.**
    - A Sevan-side site would earn about a third of its year in June–August. From December to March it would run at **about 62–91 % of average volume, roughly three-quarters on average** (B base 76 %, C base 73 %).
    - It would depend on **~8–12 summer weekends (~16–24 weekend days)** and on long-stay diaspora and Russian visitors. *Fact-check correction: previously "60–70 % of average from December to March" and "~10–14 summer weekends". Both are now aligned with this file's own index (§3.7) and with the peak definition in §1.6.*
    - A Yerevan-edge site has a flatter (~1.5×) profile, anchored by commuters, with leisure on top.
    - **Tourism alone does not justify a highway drive-thru. It is an upside layer on a commuter/regional base.**

---

## 2. Key data table

| # | Metric | Value | Period | Status | Source |
|---|---|---|---|---|---|
| 1 | Inbound tourists (UNWTO definition, ≥24 h) | 1,894,377 / 360,338 / 875,772 / 1,665,658 / 2,316,210 / 2,208,179 / **2,263,642** | 2019 / 2020 / 2021 / 2022 / 2023 / 2024 / 2025 | VERIFIED | [1] |
| 2 | Inbound tourists by quarter | 386,741 / 520,394 / 827,112 / 529,395 | 2025 Q1–Q4 | VERIFIED | [1] |
| 3 | Inbound tourists, 2026 YTD | Q1 453,138 (+17.2 %); Q2 588,460 (+13.1 %); H1 1,041,598 (+14.8 %) | H1 2026 | VERIFIED | [1][2] |
| 4 | Q3 share of annual tourists | 36.4 % / 35.1 % / 36.5 % | 2019 / 2024 / 2025 | ESTIMATE from VERIFIED | [1] |
| 5 | Tourists by citizenship (share) | Russia 921,704 (40.7 %); Armenia 319,285 (14.1 %); Georgia 288,578 (12.7 %); Iran 182,364 (8.1 %); USA 60,891 (2.7 %); China 45,004 (2.0 %); France 35,847; Germany 34,136; India 28,450; Ukraine 27,648; Italy 22,669 | 2025 | VERIFIED | [1][2] |
| 6 | H1 2026 by citizenship | Russia 416,743 (+23.3 %); Armenia 161,512 (+5.0 %); Georgia 150,322 (+17.2 %); Iran 81,180 (+4.0 %); China 17,733 (+13.8 %); Germany 17,487 (+41.5 %); USA 16,399 (−3.3 %); India 9,105 (−37 %) | H1 2026 | VERIFIED | [2] |
| 7 | Tourist nights; average stay | 65.7 m nights; 29 nights (Russia 25, Armenia 63, Georgia 31, Iran 29, USA 25, Germany 17, Italy 10, China 7) | 2025 | VERIFIED | [1] |
| 8 | Share of tourists from nationalities with average stay ≤18 nights | ~16 % (≈367k) | 2025 | ESTIMATE from VERIFIED | [1] |
| 9 | Average number of tourists present in the country on a given day | ≈180,000 (65.7 m nights ÷ 365) | 2025 | ESTIMATE | [1] |
| 10 | Travel credits (tourist spending in BoP) | US$1,528 m / 2,419 m / 3,116 m / 2,727 m / **2,911 m** (personal 2,465 m; business 446 m) | 2019 / 2022 / 2023 / 2024 / 2025 | VERIFIED | [10] |
| 11 | Travel credits by quarter | 501 / 698 / 997 / 714 (2025); 619 / 815 (2026 Q1–Q2, H1 +19.6 % y/y) | 2025–H1 2026 | VERIFIED | [10] |
| 12 | Spending per tourist-night; per tourist | ≈US$44 per night (≈AMD 17,150 at the 2025 average of AMD 387.01/USD; do not restate at today's 361.93); ≈US$1,290 per tourist. The survey-based daily spend is higher: US$50.8 (row 41) | 2025 | ESTIMATE | [10][1] |
| 13 | Border entries, all persons | 1.63 m / 3.39 m / 4.76 m / 4.75 m / **5.20 m** | 2021 / 2022 / 2023 / 2024 / 2025 | VERIFIED | [11] |
| 14 | Border entries by mode | Air 2,780,847; road 2,394,523 (Armenian citizens 1.28 m, foreigners 1.12 m); rail 26,377 | 2025 | VERIFIED | [11] |
| 15 | Road entries by quarter | 436,712 / 575,153 / 799,321 / 583,337 | 2025 | VERIFIED | [11] |
| 16 | Entries by checkpoint | Zvartnots 2,708,063; **Bagratashen 1,404,774**; Bavra 473,846; Meghri 404,644; Gogavan 111,127; Gyumri 70,288; Ayrum (rail) 26,377 | 2025 | VERIFIED | [3] |
| 17 | Bagratashen monthly entries (index, mean = 100) | Jan 72, Feb 55, Mar 79, Apr 79, May 97, Jun 108, **Jul 149, Aug 164**, Sep 109, Oct 103, Nov 88, Dec 98 | 2025 | ESTIMATE from VERIFIED | [3] |
| 18 | Checkpoint entries, 2026 vs 2025 | **Trend basis, Jan–Jul:** Zvartnots +11.6 % (1,647,307 vs 1,476,012); **Bagratashen +3.1 %** (770,658 vs 747,465); **Meghri −31.2 %**. **Jan–Aug, which includes the suspect August:** Zvartnots +7.1 %; Bagratashen −1.3 %; Bavra +0.5 %; Gogavan −7.1 %; Meghri −32.4 %; total +0.6 %. *Fact-check correction: Jan–Jul is now the trend figure. Implied August is Zvartnots −14.9 % and Bagratashen −18.3 %.* | Jan–Jul / Jan–Aug 2026 | VERIFIED (data) / ESTIMATE (change) | [3] |
| 19 | Air passengers (arrivals + departures) | 5,755.7k (+6.7 %); peak Aug 679.4k, trough Feb 294.4k | 2025 | VERIFIED | [5] |
| 20 | Air passengers, 2026 YTD | 4,243.4k (+12.1 %); Aug 775.2k (+14.1 %) | Jan–Aug 2026 | VERIFIED | [5] |
| 21 | Accommodation & food services turnover, monthly (index) | Jan 78, Feb 73, Mar 91, Apr 99, May 101, Jun 106, **Jul 117, Aug 118**, Sep 106, Oct 106, Nov 99, Dec 105 | 2025 | ESTIMATE from VERIFIED | [4] |
| 22 | Accommodation & food services, 2026 | Jan–Aug AMD 281.5 bn (+13.9 % y/y); Aug AMD 45.5 bn (+20.4 %) | Jan–Aug 2026 | VERIFIED | [4] |
| 23 | Retail sales of motor and household fuel (index) | Jan 81, Feb 84, Mar 99, Apr 95, May 98, Jun 101, Jul 108, Aug 108, Sep 100, Oct 99, Nov 101, Dec 127 (the Dec spike likely reflects household heating fuel) | 2025 | ESTIMATE from VERIFIED | [4] |
| 24 | Hotels by marz: count / revenue (AMD m) | Armenia 1,792 / 79,583; Yerevan 794 / 62,326; Kotayk 162 / 6,054; Tavush 198 / 4,027; **Gegharkunik 118 / 1,417** | 2025 (prelim.) | VERIFIED | [7] |
| 25 | Hotel growth, Gegharkunik / Kotayk / Tavush | Hotels 39→118 / 91→162 / 74→198; revenue ×1.9 / ×1.9 / ×2.7 | 2019→2025 | VERIFIED | [7] |
| 26 | Accommodation & food turnover by marz (AMD m) | Armenia 383,651; Yerevan 311,372 (81.2 %); Kotayk 34,172 (8.9 %); Tavush 8,085 (2.1 %); Gegharkunik 4,659 (1.2 %) | 2024 | VERIFIED | [9] |
| 27 | Corridor town populations | Abovyan 50,556; Hrazdan 49,547; Charentsavan 24,101; Sevan 19,652; Byureghavan 11,819; Nor Hachn 10,460; Tsaghkadzor 1,127; Dilijan 16,368; Ijevan 19,492 | 1 Jan 2025 | VERIFIED | [9] |
| 28 | Lake Sevan coastal water temperature (Big / Small Sevan) | Jul 21.2 / 20.3 °C; Aug 21.2 / 21.3 °C; Oct 2025 15.4 / 14.0 °C | 2025–2026 | VERIFIED | [6] |
| 29 | Air temperature, Gegharkunik / Kotayk / Yerevan (monthly mean, range across stations) | +14.5…+18.4 / +15.5…+24.2 / +26.0…+27.3 °C | Aug 2026 | VERIFIED | [6] |
| 30 | Sevan climate, model grid at 1,941 m | Jan −6.1 °C mean (−9.5 min); Aug 16.2 °C (21.6 max); ~160 frost days; ~58 ice days; ~144 cm snowfall; ~32 days ≥1 cm; ~9 days ≥5 cm | 2016–2025 average | ESTIMATE (ERA5 reanalysis via Open-Meteo) | [14] |
| 31 | Climate elsewhere on the corridor | Abovyan (1,411 m): Jan −2.6 °C, ~23 snow days. Hrazdan (1,758 m): Jan −6.3 °C, ~39 snow days. Tunnel approach (2,115 m): Jan −8.3 °C, ~20 days ≤−15 °C | 2016–2025 | ESTIMATE | [14] |
| 32 | Yerevan→Tbilisi travel time by route (free-flow, OSM) | Fastest 276.9 km / 4 h 33 min via Aparan–Vanadzor–Stepanavan–Gogavan; via M-4 Sevan–Dilijan–Ijevan–Bagratashen 298.8 km / 5 h 14 min; via Aparan–Vanadzor–Alaverdi–Bagratashen 287.4 km / 5 h 15 min | Oct 2026 | ESTIMATE (OSRM) | [13] |
| 33 | Yerevan→Bagratashen travel time by route | Via M-4 Sevan–Dilijan–Ijevan 212.2 km / 3 h 26 min; via Aparan–Vanadzor–Alaverdi 204.6 km / 3 h 33 min | Oct 2026 | ESTIMATE (OSRM) | [13] |
| 34 | Bagratashen's role in trade; May 2024 floods | "Handles 80 % of Armenia's imports and exports"; floods damaged M-6 and M-4 links to the crossing. ADB does not say whether the 80 % is by value or volume, or which modes it covers. *Fact-check: applying it to road tonnes (§3.6) is an ASSUMPTION.* | 2024 (page updated Oct 2024) | REPORTED (ADB) | [12] |
| 35 | Road freight | 13,513 kt total; imported 4,632 kt (+7.6 %); exported 826 kt (−11.1 %); domestic 8,055 kt | 2025 | VERIFIED | [5] |
| 36 | Ropeway passengers, all of Armenia | 0.3 m (0.6 m in 2019); network length 13.9 km | 2024 | VERIFIED | [7] |
| 37 | Lake Sevan public beaches | ~100k visitors in summer 2011 (2 beaches); ~200k in 2014 (11 beaches) | 2011, 2014 | REPORTED (Wikipedia citing RFE/RL, ArmeniaNow, 1tv; low reliability, outdated) | [15] |
| 38 | Tsaghkadzor ski season and lifts | Mid-December to March, upper slopes often into April; lifts from 1,969 m to 2,819 m | n.d. | REPORTED (Wikipedia) | [15] |
| 39 | Vardavar (water festival, 14 weeks after Easter, a Sunday) | 12 Jul 2026; 4 Jul 2027; 23 Jul 2028; 8 Jul 2029; 28 Jul 2030 | — | ESTIMATE (computed from the Easter date) | [15] |
| 40 | **Corridor seasonality index, segment B (Hrazdan–Sevan), base** | Jan 69, Feb 66, Mar 78, Apr 86, May 98, Jun 113, Jul 144, **Aug 151**, Sep 117, Oct 101, Nov 86, Dec 91 | Model use | ESTIMATE | §3.7 |
| 41 | Visitor spending per day (International Visitor Survey) | Average **US$50.8**. By purpose: leisure **US$61.8**; visiting friends and relatives US$42.1. By travel mode: package tour US$193 (5.4 % of visitors); independent US$48.1. By market: Russia US$46.7; Georgia US$35.0 | 2023 | REPORTED (IVS 2023, Tables 10–13; opened in fact-check) | [18] |
| 42 | Share of tourists visiting corridor marzes | **Gegharkunik 35.8 %** (Russia 38.1 %, Georgia 17.3 %, Iran 28.4 %, USA 40.9 %); Kotayk 31.8 %. Regional trips are mostly same-day excursions | 2023 | REPORTED (IVS 2023, Table 8, p. 24) | [18] |

---

## 3. Detailed findings and analysis

### 3.1 International arrivals, 2019–2026

**Definition caveat (important).** Armstat derives "tourists" from the border electronic management system: arrivals that meet the UNWTO ≥24 h and <1 year criteria [1]. The count includes:
- Armenian citizens resident abroad, i.e. the diaspora;
- long-stay Russian relocants;
- Georgians on family, trade and short-hop trips.

It does **not** measure leisure sightseeing.

| Year | Inbound tourists | y/y | Outbound tourists | Travel credits (US$ m) |
|---|---|---|---|---|
| 2019 | 1,894,377 | — | 1,867,888 | 1,528 |
| 2020 | 360,338 | −81 % | 309,978 | 287 |
| 2021 | 875,772 | +143 % | 432,591 | 784 |
| 2022 | 1,665,658 | +90 % | 1,065,912 | 2,419 |
| 2023 | 2,316,210 | +39 % | 1,550,427 | 3,116 |
| 2024 | 2,208,179 | −4.7 % | 1,679,240 | 2,727 |
| 2025 | 2,263,642 | +2.5 % | 1,725,590 | 2,911 |
| H1 2026 | 1,041,598 | +14.8 % (vs 907,135) | 686,277 | 1,434 (+19.6 %) |

Sources: [1] (Armstat workbook, last saved 8 Sept 2026), [2], [10]. All VERIFIED.

**Source conflict.** Wikipedia's 2019 figure is 1,932,230 [15]. Armstat's current workbook gives 1,894,377 [1]. I use Armstat, the official series after revision.

**Interpretation.**
- The 2022–23 surge was driven by Russia: 790k Russian tourists in 2022 and 1.14 m in 2023. The Russian count then fell to 938k in 2024 and 922k in 2025 [1].
- Non-Russian, non-Armenian demand grew steadily over the same period, for example:
  - China: 5.5k → 45.0k (2022 → 2025)
  - Italy: 4.5k → 22.7k
  - Germany: 23.7k → 34.1k
- H1 2026 shows renewed Russian growth (+23 %) and strong European growth (Germany +41 %, Italy +47 %). India and South Korea fell (−37 % and −35 %) [2].

### 3.2 Seasonality of arrivals, and monthly proxies

**Quarterly tourists** (VERIFIED [1]). My share calculations: Q1 17–20 %, Q2 21–23 %, **Q3 35–37 %**, Q4 22–23 %. Q3 accounts for 35.1–36.5 % in each year shown below.

| Quarter | 2019 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| Q1 | 364,489 | 435,775 | 386,741 | 453,138 |
| Q2 | 405,566 | 510,387 | 520,394 | 588,460 |
| Q3 | 689,097 | 775,083 | 827,112 | — |
| Q4 | 435,225 | 486,934 | 529,395 | — |

**No monthly tourist series is published by Armstat.** The Tourism Committee's monthly releases were not reachable (tourism.gov.am did not resolve, and search was unavailable). I built monthly proxies from Armstat monthly data [3][4][5]. Each index has mean = 100.

| Proxy (2025 unless noted) | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Peak/trough |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zvartnots entries (air) | 82 | 61 | 78 | 86 | 98 | 113 | 137 | 135 | 111 | 113 | 89 | 98 | 2.2 |
| Air passengers | 82 | 61 | 77 | 87 | 98 | 112 | 131 | 142 | 115 | 114 | 89 | 93 | 2.3 |
| International tourists (Zvartnots monthly profile rescaled to Armstat quarterly tourists, 2024–25 average) | 80 | 63 | 78 | 80 | 91 | 105 | 152 | 151 | 127 | 102 | 81 | 90 | 2.4 |
| Bagratashen entries (road, Georgia) | 72 | 55 | 79 | 79 | 97 | 108 | 149 | 164 | 109 | 103 | 88 | 98 | 3.0 |
| Bavra entries (road, Georgia via Gyumri) | 95 | 68 | 84 | 81 | 83 | 100 | 134 | 166 | 102 | 91 | 89 | 107 | 2.4 |
| Gogavan entries (road, Georgia via Tashir) | 79 | 43 | 69 | 67 | 87 | 100 | 177 | 189 | 101 | 99 | 93 | 96 | 4.4 |
| Meghri entries (road, Iran) | 64 | 66 | 107 | 99 | 102 | 141 | 114 | 98 | 96 | 103 | 96 | 114 | 2.2 |
| Accommodation & food turnover (nominal) | 78 | 73 | 91 | 99 | 101 | 106 | 117 | 118 | 106 | 106 | 99 | 105 | 1.6 |
| Motor and household fuel retail (nominal) | 81 | 84 | 99 | 95 | 98 | 101 | 108 | 108 | 100 | 99 | 101 | 127 | 1.6 (1.3 excluding Dec) |
| Road freight tonnes | 66 | 67 | 84 | 89 | 104 | 107 | 106 | 115 | 122 | 120 | 112 | 107 | 1.8 |

All rows are ESTIMATE, computed by me from VERIFIED monthly values [3][4][5]. Monthly border flows come from differencing Armstat's cumulative checkpoint tables (sections 5.1 of each monthly report). Each month is taken from the current-year table, and checkpoint flows reconcile exactly to the annual 2025 totals.

**Reading the proxies.**
- Long-distance road leisure (Bagratashen, Gogavan) is the most seasonal flow: July–August run 1.5–1.9 times the average.
- Urban consumption (accommodation & food, fuel) is far flatter.
- Iran-linked flows (Meghri) peak in spring (Nowruz in March) and June, not in August.

**Anomaly in August 2026 (flag).** Cumulative January–August 2026 checkpoint data imply that August 2026 entries fell **−15 % at Zvartnots and −18 % at Bagratashen** y/y. Over the same month, Armstat transport data show **air passengers +14.1 %** and accommodation & food turnover **+20.4 %** [4][5]. The August border records are probably incomplete preliminary data (the "*" flag in the source). Do not use them for trend analysis until the January–September 2026 report is out (about 5 Nov 2026).

### 3.3 Spending

| Indicator | Value | Status |
|---|---|---|
| Travel credits 2025 (total / personal / business) | US$2,910.7 m / 2,465.2 m / 445.5 m | VERIFIED [10] |
| Per tourist-night | 2,910.7 m ÷ 65.70 m nights = **US$44.3** (≈AMD 17,150 at AMD 387.01/USD, the 2025 average via A1) | ESTIMATE |
| Per tourist | 2,910.7 m ÷ 2,263,642 = **US$1,286** | ESTIMATE |
| Seasonality of spending | Q3 = 34.3 % of 2025 travel credits; Q1 = 17.2 % | ESTIMATE from VERIFIED [10] |
| Spending growth in 2026 | H1 travel credits +19.6 % y/y against tourists +14.8 %, so spending per tourist is rising | ESTIMATE |
| Survey daily spend, all visitors | **US$50.8/day** | REPORTED (IVS 2023 [18]) |
| By purpose | Leisure **US$61.8/day** (≈1.2× the average); visiting friends and relatives US$42.1/day (leisure ≈1.5× this) | REPORTED (IVS 2023 [18]) |
| By travel mode | Package tour **US$193/day** (≈3.8× the average) but only **5.4 % of visitors**; independent travellers US$48.1/day | REPORTED (IVS 2023 [18]) |
| By market | Russia US$46.7/day; Georgia US$35.0/day | REPORTED (IVS 2023 [18]) |

**Caveat.** The per-night figure is diluted by long-stay visitors: diaspora relatives staying with family and relocants living in rented flats. The 2023 International Visitor Survey (IVS) quantifies the gap [18]. The Tourism Committee, Armstat and the CBA ran it with the World Bank LEID project, and the CBA used it to revise travel credits for 2022–2024 (Meth.notes sheet of [10]). **Leisure visitors spend about 1.2–1.5× the average per day, not several times more.** Only package tourists, 5.4 % of arrivals, spend about 4× the average. For drive-thru purposes, a long-stay visitor behaves like a semi-resident. Use the IVS per-day spend by market and purpose to calibrate the tourist average ticket. *Fact-check correction: this paragraph previously said a short-stay sightseer "almost certainly spends several times more per day" and that "no post-2013 visitor survey was accessible". The 2023 IVS is public (cited by [10]) and contradicts both statements.*

### 3.4 Domestic tourism

- **No current official count of domestic trips was found.** Armstat's quality declaration lists "international and domestic tourism" as a product [17]. The only published data are the inbound/outbound workbook and hotel aggregates [1][7]. Hotel statistics (Armstat form "tourists registered in hotels") are collected quarterly, but by-marz guest counts are not on ArmStatBank [7][17]. (GAP)
- **Hotel capacity is a proxy for regional demand** (VERIFIED [7]):

  | Marz | Hotels, 2019 → 2025 | Hotel revenue, 2019 → 2025 (AMD m) | Hotel employees (2025) |
  |---|---|---|---|
  | Gegharkunik (Sevan) | 39 → 118 | 736 → 1,417 | 330 |
  | Kotayk (Tsaghkadzor) | 91 → 162 | 3,220 → 6,054 | 1,186 |
  | Tavush (Dilijan) | 74 → 198 | 1,506 → 4,027 | 510 |

- **Implication (ESTIMATE).** Assume average hotel revenue of AMD 25–40k per occupied room-night (ASSUMPTION). Gegharkunik's AMD 1.42 bn then equals only **~35–57k hotel room-nights a year** for the entire lake. That confirms the basin is overwhelmingly a **day-trip and own-cottage** destination. Unregistered rest houses, cottages and camping are not in these figures (ASSUMPTION).

### 3.5 Destinations on the corridor: Sevan, Tsaghkadzor, Dilijan

| Destination | Distance and time from Yerevan (OSRM, free flow) | What is known | Status |
|---|---|---|---|
| Sevan town / beaches | 63 km, ~59 min | Public beaches: ~100k visitors (2011) and ~200k (2014). Water ≥20 °C only in Jul–Aug. Gegharkunik hotel revenue AMD 1.4 bn (2025) | REPORTED [15] / VERIFIED [6][7] |
| Sevanavank monastery | 69 km, ~65 min | Active monastery, free entry, so no ticket data. One of the standard day-tour stops (ASSUMPTION). **No visitor count found** | GAP |
| Tsaghkadzor ski resort | 57 km, ~55 min (exit at Hrazdan, official km ~38–40) | Season mid-Dec to Mar. Town population 1,127. Kotayk hotel revenue AMD 6.05 bn (2025), the largest outside Yerevan. **No skier-day count found.** National ropeway statistics (0.3 m passengers in 2024) probably do not count ski lifts in a comparable way | REPORTED [15] / VERIFIED [7][9] |
| Dilijan | 97 km, ~93 min | Population 16,368. Tavush hotel revenue AMD 4.03 bn (2025, ×2.7 vs 2019). Resort and education hub. **No visitor count found** | VERIFIED [7][9] |

**Implication.** Tsaghkadzor traffic leaves the M-4 at the Hrazdan junction. A site **south of Hrazdan** sees ski traffic (winter weekends, New Year week). A site **beyond Hrazdan toward Sevan does not**. This is the main reason segment A's winter trough is shallower than segment B's.

### 3.6 Tours, routes to Georgia, freight

**Tour buses and organised tours.** No counts were found. The standard Yerevan day-tour "Sevan + Dilijan (Sevanavank, Haghartsin, Goshavank)" uses the M-4 through the tunnel, and its schedule is the stock product of Yerevan agencies (ASSUMPTION; verify via agency catalogues).

Sizing (ESTIMATE):
- **Visitors.** 2.26 m tourists × 25–45 % who visit Sevan at least once (ASSUMPTION) = **0.57–1.02 m visitor-trips per year**.
- **Vehicles.** Assume 25–40 % travel by coach or minibus at ~18 pax per vehicle, and 60–75 % by taxi, private car or rental at ~2.8 pax per vehicle (ASSUMPTIONS). That gives **≈135k–290k vehicle round trips per year**, or **≈370–790 per day on average** (≈560–1,200 per day in July–August).
- **Share of traffic.** On segment B, international traffic is **≈4–9 % of passes** at B1's base AADT of 17,000.
- **Drive-thru relevance.** Coaches cannot use a drive-thru lane. Coach groups stop at sit-down or monastery cafés, so only the car, taxi and rental part matters for a drive-thru.

**Yerevan–Tbilisi and Georgia traffic.**

| Route (OSRM free-flow, OSM data, queried 10 Oct 2026 [13]) | Distance | Time |
|---|---|---|
| Yerevan → Tbilisi via Ashtarak–Aparan–Spitak–Vanadzor–Stepanavan–**Gogavan** | 276.9 km | 4 h 33 min |
| Yerevan → Tbilisi via **M-4 Sevan–Dilijan–Ijevan–Noyemberyan–Bagratashen** | 298.8 km | 5 h 14 min |
| Yerevan → Tbilisi via Aparan–Spitak–Vanadzor–Alaverdi–Bagratashen | 287.4 km | 5 h 15 min |
| Yerevan → **Bagratashen** via M-4 Sevan–Dilijan–Ijevan | 212.2 km | **3 h 26 min** |
| Yerevan → Bagratashen via Aparan–Vanadzor–Alaverdi | 204.6 km | 3 h 33 min |

- **Revealed preference contradicts the model's fastest route.** Gogavan handled only 111k entries in 2025, against **1.40 m at Bagratashen** [3]. Travellers, buses and trucks overwhelmingly use Bagratashen: it is the main customs post, on the bus routes and with the better road, as ADB notes [12].
- **Two Bagratashen routes are almost tied.** The M-4 route through Sevan and Dilijan is 7 minutes faster than the Vanadzor–Alaverdi route on OSRM's free-flow speeds. The real split is unknown (GAP).
  - The May 2024 floods damaged M-6 sections (REPORTED [12]). That may have pushed traffic onto the M-4 for a period (ASSUMPTION).
  - The Dilijan tunnel rehabilitation proposed under ADB RIRSIP II (B1) may push traffic the other way in 2027–2030 (ASSUMPTION).
- **Sizing (ESTIMATE).**
  - Bagratashen two-way person crossings were 2.79 m in 2025, or ≈7,650 per day.
  - At ~2.2 persons per vehicle (ASSUMPTION; covers cars, minibuses with many passengers, and single-occupant trucks), that is ≈3,500 vehicle crossings per day.
  - With an M-4 share of 35–60 % (ASSUMPTION), **≈1,200–2,100 vehicles per day two-way on Sevan–Dilijan** are Georgia-linked, ×1.65 in August.
  - That is a large share (≈22–38 %) of B1's base AADT of 5,500 for the tunnel segment. It also implies that segment C has a stronger August peak than B1 assumed.
- **Freight (ESTIMATE).**
  - International road freight in 2025 was 5.46 Mt (imports 4.63 + exports 0.83) [5]. At ~20 t per loaded truck (ASSUMPTION) that is ≈750 loaded truck movements per day nationally.
  - ADB attributes ~80 % of trade to Bagratashen [12], giving ≈600 loaded trucks per day there plus empty returns.
  - With a 35–60 % M-4 share, that is **≈400–700 truck passes per day** on Sevan–Dilijan–Hrazdan–Yerevan.
  - Road freight is mildly seasonal (Jan–Feb ≈0.65 of average, Sep–Oct ≈1.2).

### 3.7 Corridor seasonality index (model input)

**Method (ESTIMATE).** Each corridor segment's monthly index is a weighted sum of segment-specific component profiles, renormalised to mean = 100. "Low" and "high" variants scale the amplitude of the leisure components by ×0.7 and ×1.3.

| Component (mean = 100) | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 Local, regional and commuter (non-leisure) | 85 | 87 | 97 | 98 | 100 | 102 | 105 | 104 | 104 | 103 | 104 | 111 | ASSUMPTION anchored on fuel retail 2024–25, without the household-fuel spike in Dec |
| C2a Leisure, Sevan/Dilijan-bound | 47 | 41 | 52 | 72 | 98 | 134 | 207 | 222 | 129 | 88 | 52 | 57 | ASSUMPTION: beach-season shape; peak above Gogavan's 189 because water is ≥20 °C only in Jul–Aug |
| C2b Leisure including Tsaghkadzor ski | 110 | 95 | 70 | 65 | 85 | 110 | 160 | 170 | 105 | 80 | 60 | 90 | ASSUMPTION: adds the Dec–Mar ski season and New Year week |
| C3 International tourists | 80 | 63 | 78 | 80 | 91 | 105 | 152 | 151 | 127 | 102 | 81 | 90 | ESTIMATE from VERIFIED [1][3] |
| C4 Georgia / long-distance | 78 | 60 | 80 | 80 | 90 | 103 | 148 | 166 | 111 | 104 | 87 | 94 | ESTIMATE: Bagratashen, average of 2024–25 [3] |
| C5 Freight / professional | 63 | 72 | 85 | 92 | 104 | 107 | 109 | 113 | 119 | 119 | 111 | 106 | ESTIMATE: Armstat road freight tonnes, 2024–25 [5] |

**Segment weights (share of annual vehicle passes; ASSUMPTION).** They are informed by the bottom-up sizing in §3.8 and by B1's vehicle mix (≈7 % minibuses, ≈10 % trucks).

| Segment | C1 | C2a | C2b | C3 | C4 | C5 |
|---|---|---|---|---|---|---|
| A. Yerevan edge–Abovyan–Charentsavan (official km 9–31) | 55 % | — | 20 % | 5 % | 7 % | 13 % |
| B. Hrazdan–Sevan (km 40–60) | 35 % | 30 % | — | 8 % | 10 % | 17 % |
| C. Sevan–Tsovagyugh–Dilijan (km 60–96) | 20 % | 30 % | — | 10 % | 22 % | 18 % |

**Result (mean = 100)** — this is the recommended model input:

| Segment / variant | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | Peak/trough | Jun–Aug share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A low | 86 | 84 | 90 | 91 | 97 | 104 | 118 | 121 | 108 | 102 | 96 | 105 | 1.44 | 28.6 % |
| **A base** | **86** | **84** | **88** | **88** | **96** | **104** | **122** | **125** | **108** | **101** | **94** | **104** | **1.50** | **29.3 %** |
| A high | 87 | 83 | 86 | 86 | 95 | 105 | 125 | 129 | 108 | 99 | 91 | 103 | 1.55 | 30.0 % |
| B low | 73 | 71 | 82 | 89 | 99 | 110 | 135 | 140 | 114 | 102 | 90 | 94 | 1.96 | 32.0 % |
| **B base** | **69** | **66** | **78** | **86** | **98** | **113** | **144** | **151** | **117** | **101** | **86** | **91** | **2.28** | **34.0 %** |
| B high | 64 | 61 | 74 | 84 | 98 | 116 | 154 | 162 | 119 | 100 | 82 | 87 | 2.66 | 36.0 % |
| C low | 72 | 68 | 80 | 86 | 97 | 110 | 141 | 148 | 115 | 103 | 88 | 92 | 2.20 | 33.3 % |
| **C base** | **67** | **62** | **76** | **83** | **97** | **113** | **150** | **159** | **118** | **102** | **84** | **88** | **2.56** | **35.2 %** |
| C high | 63 | 57 | 71 | 81 | 97 | 116 | 160 | 170 | 121 | 101 | 79 | 84 | 2.99 | 37.2 % |

**Validation.**
- Segment A base gives July = 122. The only measured Armenian interurban monthly factor is the M-1 automatic counter at **+19.7 % in July** (≈120; VERIFIED in B1, ADB 2010 data), so the two agree.
- Segment B base (Jan 69, Aug 151) is within 3–5 points of the model placeholder (0.66 … 1.46).
- **Recommendation.**
  - Keep the placeholder for a Sevan-side site.
  - Replace it with segment A for any site between the Yerevan edge and Charentsavan.
  - Use B-high or C-high as the downside case for a lakeshore or Dilijan site.

**Day-of-week and peak days (ASSUMPTION; no counts found).**
- Summer weekend days on segments B and C are likely 1.3–1.6× a summer weekday, so the peak day reaches ≈2.0–2.4× AADT.
- Winter weekends on segment A are boosted by Tsaghkadzor traffic.
- Commuter weekdays dominate segment A for 9–10 months of the year.
- Peak calendar events:
  - New Year week (31 Dec – 7 Jan, including Christmas on 6 Jan): Tsaghkadzor peak, segment A.
  - May holidays (1, 9 and 28 May): first Sevan trips.
  - Constitution Day (5 Jul) and **Vardavar** (12 Jul 2026, 4 Jul 2027).
  - Every July–August weekend.
  - Independence Day (21 Sept): end of season.
- The holiday list is REPORTED from Wikipedia [15] and needs checking against arlis.am.

### 3.8 Customer segments and rough sizing

| Segment | Who / when / direction | Rough size (annual or daily) | Share of passes (A / B / C) | Seasonality | Drive-thru fit | Status |
|---|---|---|---|---|---|---|
| **Daily commuters** (Abovyan, Byureghavan, Nor Hachn, Charentsavan, Hrazdan, Sevan → Yerevan) | Weekdays 07:00–09:30, Yerevan-bound; return 17:00–20:00 | Corridor towns 167k people (VERIFIED [9]). × 38–42 % employed (ASSUMPTION; LFS participation 59.9 %, unemployment 13 %, per C3) × 10–45 % commuting to Yerevan (falls with distance) = **12–20k commuters**. × 35–55 % by car ÷ 1.3 occupancy = **≈3.3–8.3k car trips per direction per weekday** | 40–55 % / 15–25 % / <10 % (within C1) | Flat (85–111) | **Best repeat base.** Morning coffee on the Yerevan-bound side; loyalty and app ordering | ESTIMATE |
| **Regional and business trips** (Gegharkunik/Tavush ↔ Yerevan: officials, traders, visiting relatives) | All week, both directions | Gegharkunik plus Tavush towns: Sevan, Gavar, Martuni, Vardenis, Chambarak, Dilijan, Ijevan ≈ 105k people (VERIFIED [9]) plus rural areas. Volume not quantified | 5–10 % / 15–20 % / 15–20 % (within C1) | Flat | Medium: mid-trip coffee and snack | ASSUMPTION |
| **Domestic leisure trippers** (Sevan beach, Sevanavank, Dilijan, Tsaghkadzor; cottage owners) | Sat–Sun mornings outbound, afternoons/evenings return; Jun–Aug peak; New Year/ski on A | Yerevan car-owning households ≈142k (1,141k residents ÷ ~3.3 per household × 41.2 % car ownership; ILCS 2024 via A1) × 50–75 % participation × 2–5 trips, plus other regions and taxis = **≈0.15–0.75 m car round trips/yr** (≈400–2,000 per day on average; ≈1,000–4,500 per day in Aug) | 20 % / 30 % / 30 % | Strong (Aug ≈2.2×, Feb ≈0.4×) | **High ticket, low frequency.** Families, groups, outbound morning on the Sevan-bound side; weather-sensitive | ESTIMATE |
| **International tourists, self-drive / taxi / rental** | Day tours from Yerevan; Georgia–Armenia road trippers | ≈0.4–0.75 m visitor-trips/yr by car or taxi (60–75 % of 0.57–1.02 m) ÷ 2.8 pax = **≈140–270k vehicle round trips/yr** | 3 % / 5 % / 6 % | Strong (Jul–Aug ≈1.5×) | Medium-high: novelty value of a US-style brand; card payment; English menu | ESTIMATE |
| **International tourists, coach/minibus** | Organised Sevan–Dilijan tours | ≈0.14–0.4 m visitor-trips/yr ÷ ~18 pax = **≈8–22k coach trips/yr** (≈20–60 per day) | 1–2 % / 2–3 % / 3–4 % | Strong | **Low for the lane**; possible walk-up or group pre-order | ESTIMATE |
| **Long-distance Georgia / Russia travellers** (Yerevan ↔ Tbilisi, Upper Lars) | All week, peaks Fri/Sun and Jul–Aug | ≈1,200–2,100 Georgia-linked vehicles/day two-way on Sevan–Dilijan, including ~400–700 trucks; thinner toward Yerevan as a share of traffic | 7 % / 10 % / 22 % | Strong (Aug ≈1.65×) | Medium: long-trip "coffee + food to go"; good fit at a fuel-station hybrid | ESTIMATE |
| **Professional drivers: trucks** | 24 h, cement and energy (Hrazdan) plus Georgia freight | ≈10 % of vehicles at an M-2 comparator (2009, B1) | 13 % / 17 % / 18 % (C5) | Mild | **Low for the lane** (height and turning); truck-bay walk-up coffee only | REPORTED (B1) / ASSUMPTION |
| **Professional drivers: marshrutka and taxi** | Scheduled minibuses Yerevan–Abovyan/Hrazdan/Sevan/Dilijan; intercity taxis (Yandex Go, Tbilisi shared taxis) | Minibuses ≈6.7 % of vehicles at the M-2 comparator (2009, B1); taxi share unknown | Part of C1 / C4 | Mild | Low-medium: price-sensitive, quick-stop habits; taxis may be frequent repeat buyers | REPORTED (B1) / GAP |
| **Families** (cross-cutting) | Summer school holidays (Jun–Aug), weekends, New Year | ILCS average household ≈3.3 persons (ASSUMPTION); most leisure trips are family trips (ASSUMPTION) | Within C2 | Strong | **High**: kids' items, food bundles, restrooms; drives ticket size | ASSUMPTION |

**Reconciliation check (critical).**
- Leisure at 30 % of B1's segment-B base AADT (17,000) would be ≈5,100 passes per day, or ≈2,550 round trips per day (≈0.93 m a year).
- My bottom-up range is 0.15–0.75 m. Including cottage owners' weekly summer trips, the realistic upper end is ~0.75–0.9 m.
- So **either** B1's base AADT for Hrazdan–Sevan is at the high end, **or** leisure's share is nearer 10–20 % and the regional/business share is larger. That would flatten segment B's index toward B-low.
- Both possibilities are testable with a summer-vs-February classified count (B1 §5).

---

## 4. Implications for the drive-thru concept (critical)

1. **Tourism is not a sufficient base for a highway unit.**
   - The headline 2.26 m tourists include ~0.32 m diaspora Armenians and ~0.92 m Russians with month-long stays.
   - The classic short-stay sightseeing market is ~0.37 m a year, and many of them travel by coach, which cannot use a drive-thru lane.
   - Gegharkunik's whole hotel economy is AMD 1.4 bn a year (1.8 % of national hotel revenue). Sevan is a day-trip lake, and day-trippers mostly carry their own food or eat at lakeside khorovats places (ASSUMPTION).
2. **A Sevan-side site will have a 2.0–3.0× peak-to-trough year.**
   - About 34–37 % of its annual traffic falls in June–August.
   - From December to March it runs at about 62–91 % of the annual average (B/C base).
   - Within the peak, demand is concentrated on ~10–14 summer weekend days a year (ASSUMPTION).
   - Fixed costs (rent, core staff, equipment lease) must be covered in about 7–8 weak months. Weekend-peak throughput needs a lane capacity of about 2.4× AADT-day.
3. **A Yerevan-edge or Abovyan-side site is structurally safer.** Its seasonality is ~1.5×, it has a winter Tsaghkadzor boost, and its weekday commuter base is ~3–8k car trips per direction. Leisure traffic adds summer upside. This supports B4's verdict ("Yerevan exit-corridor drive-thru").
4. **Choose a side, because direction matters.**
   - Commuter morning coffee is on the **Yerevan-bound** carriageway.
   - Leisure morning departures are on the **Sevan-bound** carriageway.
   - Evening returns (Sevan → Yerevan) are long, tired drives where food demand may be real but coffee demand lower (ASSUMPTION).
   - A median-separated dual carriageway (B1) means one site cannot serve both directions unless it sits at an interchange.
5. **Weather is a real operating constraint.**
   - Sevan and the tunnel approach (1,940–2,115 m) have ~32 snowfall days a year, ~58 ice days and ~8–20 days at or below −15 °C (ERA5).
   - Expect drive-thru-lane icing, canopy and snow-load design costs, and weekend demand that swings with weather.
   - Lake water is ≥20 °C only in July–August. A cool or rainy summer cuts the peak directly.
6. **The Georgia transit flow is a hidden plus for the Sevan–Dilijan segment, with risks attached.**
   - About 1.2–2.1k Georgia-linked vehicles a day pass, peaking in August, and they include long-distance drivers who want food to go.
   - They are vulnerable to the Dilijan tunnel works proposed under ADB RIRSIP II, to route shifts back to the M-6 after flood repairs, and to Upper Lars or political disruption.
   - A fuel-station hybrid captures this segment better than a standalone drive-thru (ASSUMPTION).
7. **Concentration risk on Russia.**
   - 41 % of tourists and the fastest 2026 growth (+23 % in H1) are Russian.
   - A1 notes worsening Armenia–Russia relations in 2026, which threatens both the tourist and the relocant base.
   - The Iran flow is already down 32 % (Meghri, Jan–Aug 2026).
   - European and Chinese growth (+40 % or more) is encouraging but small in absolute terms.
8. **Positive signals.**
   - Spending is rising: travel credits +19.6 % in H1 2026, accommodation & food turnover +20 % in August 2026.
   - Hotel stock in Kotayk, Tavush and Gegharkunik roughly doubled to tripled between 2019 and 2025.
   - Air traffic is +12 % YTD.
   - Corridor demand is growing even though the basin's share stays small.
9. **Model guidance.**
   - Use the segment-specific seasonality (§3.7).
   - Make the opening month matter: a May opening captures the first summer, as the model already assumes.
   - Stress-test with B-high and C-high.
   - Add a weekend-peak capacity check.
   - Do **not** add a separate "tourist uplift" on top of AADT. Tourist vehicles are already inside the counts.

---

## 5. Data gaps and how to verify them

| Gap | Why it matters | How to verify (agency / document / fieldwork) |
|---|---|---|
| Monthly international arrivals (Tourism Committee series, including same-day visitors) | Monthly tourist seasonality; trend after August 2026 | Tourism Committee (Ministry of Economy) monthly releases; the Armstat January–September 2026 report (section 4.2.1, due ~5 Nov 2026); NSS border statistics on request |
| Lake Sevan visitor counts (beaches, Sevanavank) by month and weekday | Leisure share and peak days on segments B and C | "Sevan National Park" SNCO (Ministry of Environment): beach entry, parking and concession reports. Sevan municipality paid-parking revenue. Road Police summer operation reports. **Fieldwork:** July weekend ANPR or plate-matching at the Sevan peninsula access and at the M-4 Sevan junctions |
| Tsaghkadzor skier-days / lift tickets by month | Winter boost on segment A | Tsaghkadzor ropeway operator; Tsaghkadzor municipality tourist-tax data; Kotayk regional administration |
| Dilijan visitor numbers | Segment C leisure share | Dilijan National Park; Tavush regional administration; Dilijan municipality |
| Hotel guests and nights by marz, quarterly | Overnight demand at Sevan, Tsaghkadzor and Dilijan | Armstat ("tourists registered in hotel facilities", quarterly form, per quality declaration 20.3): formal data request to the Balance of Payments and Foreign Trade Statistics Division (foreign_trade@armstat.am) |
| Domestic trip counts | Size of the domestic leisure segment | Armstat ILCS microdata (trip or holiday spending modules, if present); a commissioned intercept and online survey (n≈600) of Yerevan car owners on trip frequency to Sevan, Dilijan and Tsaghkadzor |
| Tour-bus volumes on Yerevan–Sevan–Dilijan | Coach share of international visitors | Survey of the top 15 Yerevan inbound agencies (departures per week by season); Sevanavank parking counts; Armstat travel-agency quarterly form (20.2) on request |
| Bagratashen traffic by vehicle class, and the M-4 vs M-6 route split | Segment C long-distance volume; truck share | State Revenue Committee (customs) vehicle-crossing data by type; NSS border-guard vehicle counts. **Fieldwork:** ANPR matching between the Dilijan tunnel north portal and Ijevan, and between Vanadzor and Alaverdi, on the same days |
| Weekend/weekday and hourly profiles on the M-4 | Peak capacity, staffing | Roads Department counters (data request, B1); Road Police camera counts; a 7-day video count in July and February at 3 stations |
| Visitor spending per day by segment (short-stay vs long-stay) | Average ticket for tourists | Tourism Committee or Armstat international visitor survey (latest is 2013; ask whether a newer one exists); CBA foreign-card POS data by MCC (restaurants/cafés) and by region on request |
| Winter closure log, M-4 Yerevan–Dilijan | Operating days, weather risk | Ministry of Emergency Situations daily road bulletins archive; Roads Department |
| Current holiday law (non-working days list) | Peak-day calendar | arlis.am, the Law "On Holidays and Memorial Days" with amendments (2021–2025) |

---

## 6. Sources

All accessed 2026-10-10 unless noted.

1. Armstat, *International tourism* database (nid=1039).
   - Workbook "Number of inbound and outbound tourists by quarter and year", 2006–2026Q2 (file last saved 8 Sept 2026): https://armstat.am/file/doc/99571403.xls
   - Workbook "Geographical distribution of tourists visiting the RA, 2020–2025" (by citizenship, nights, length of stay): https://armstat.am/file/doc/99571408.xlsx
   - Page: https://armstat.am/en/?nid=1039
2. Armstat, *Socio-Economic Situation of RA*, section 4.2.1 "International tourism".
   - Jan–Dec 2025 (published 5 Feb 2026): https://armstat.am/file/article/sv_12_25r_421.pdf
   - Jan–Jun 2026 (published 5 Aug 2026): https://armstat.am/file/article/sv_06_26r_421.pdf
3. Armstat, *Socio-Economic Situation of RA*, section 5.1, border records of entries/exits by checkpoint (source: NSS border electronic management system). Monthly cumulative files Jan 2024 – Aug 2026, e.g.:
   - https://armstat.am/file/article/sv_08_26r_510.pdf (Jan–Aug 2026, published 5 Oct 2026)
   - https://armstat.am/file/article/sv_12_25r_510.pdf (Jan–Dec 2024–2025)
   - https://armstat.am/file/article/sv_06_26r_510.pdf
   - https://armstat.am/file/article/sv_07_25r_510.pdf
   - Pattern: sv_MM_YYr_510.pdf
4. Armstat, *Socio-Economic Situation of RA*, section 1.2.6 "Trade and other services": monthly accommodation & food services turnover; retail via "other trade objects" (motor and household fuel). Monthly files Jan 2024 – Aug 2026, e.g.:
   - https://armstat.am/file/article/sv_08_26r_126.pdf
   - https://armstat.am/file/article/sv_12_25r_126.pdf
5. Armstat, *Socio-Economic Situation of RA*, section 1.2.4 "Transport": freight by mode, including road import/export; passengers, including air.
   - https://armstat.am/file/article/sv_08_26r_124.pdf
   - https://armstat.am/file/article/sv_12_25r_124.pdf
   - Monthly files for 2024–2026 follow the same pattern.
6. Armstat, *Socio-Economic Situation of RA*, section 5.5 "Hydrometeorological conditions" (data from the Hydrometeorology and Monitoring Centre, Ministry of Environment), including Lake Sevan coastal water temperature.
   - Aug 2026: https://armstat.am/file/article/sv_08_26r_550.pdf
   - Jul 2026: https://armstat.am/file/article/sv_07_26r_550.pdf
   - Oct 2025: https://armstat.am/file/article/sv_10_25r_550.pdf
7. ArmStatBank (Armstat PxWeb).
   - "Hotels by marzes, indicators and years", 2011–2025 (updated 25 Aug 2026): https://statbank.armstat.am/api/v1/en/ArmStatBank/4%20Transport%20and%20tourism/43%20Tourism/TT-tu-1-2025.px
   - "Indicators on operation of rope-ways" (TT-tr-et5.px)
   - "Share of exported, imported and intra-republican freight" (TT-tr-rt3.px)
   - Portal: https://statbank.armstat.am/pxweb/en/ArmStatBank/
8. Armstat, *Statistical Yearbook of Armenia 2025*, chapter "Trade and other services" (Tables 16.14, 16.16: food & beverage services AMD 311.7 bn in 2024): https://armstat.am/file/doc/99563713.pdf
9. Armstat, *Marz in figures 2025*: population as of 1 Jan 2025; accommodation & food service turnover by marz 2020–2024.
   - Gegharkunik: https://armstat.am/file/doc/99564398.pdf
   - Kotayk: https://armstat.am/file/doc/99564423.pdf
   - Tavush: https://armstat.am/file/doc/99564478.pdf
   - Yerevan: https://armstat.am/file/doc/99564358.pdf
10. Central Bank of Armenia, *Balance of Payments of RA (BPM6)*, quarterly and annual, travel credits/debits, personal/business (file last saved 30 Sept 2026): https://old.cba.am/stat/stat_data_eng/BOP_eng_for_site_BPM6_rev.xls
11. Migration and Citizenship Service (Ministry of Internal Affairs), "Սահմանահատում 2025" workbook: entries/exits 2021–2025, by mode, by quarter.
    - File: https://migration.mia.gov.am/api/assets/2bd5a69c-b4e1-498b-a41f-13c16cab9d82
    - Page: https://migration.mia.gov.am/սահմանահատում
12. Asian Development Bank, project 58405-001 *Resilient and Inclusive Road Sector Improvement Project II* (proposed; concept 7 Oct 2024; fact-finding 24 Nov – 12 Dec 2025). Covers May 2024 flood damage to the M-6/M-4 links to Bagratashen, "80 % of imports and exports", and the Dilijan/Pushkin tunnels: https://www.adb.org/projects/58405-001/main
13. OSRM public routing service (OpenStreetMap data), routes queried 10 Oct 2026. Free-flow model, not observed travel times: https://router.project-osrm.org/
14. Open-Meteo Historical Weather API (ERA5/ERA5-Land reanalysis), daily 2016–2025, grid points for Sevan (40.60 N 44.94 E, 1,941 m), the Dilijan tunnel approach (2,115 m), Hrazdan (1,758 m) and Abovyan (1,411 m). Reanalysis, not station data; snowfall is likely underestimated: https://archive-api.open-meteo.com/v1/archive
15. Wikipedia (secondary).
    - "Tsaghkadzor": ski season, lift elevations. https://en.wikipedia.org/wiki/Tsaghkadzor
    - "Lake Sevan": public-beach visitors 2011/2014, citing RFE/RL (8 Jul 2011), ArmeniaNow (30 Sept 2011) and 1tv (5 Jul 2015). https://en.wikipedia.org/wiki/Lake_Sevan
    - "Public holidays in Armenia": non-working days; Vardavar 14 weeks after Easter. https://en.wikipedia.org/wiki/Public_holidays_in_Armenia
    - "Tourism in Armenia": 2019 figure 1,932,230 (conflicts with Armstat). https://en.wikipedia.org/wiki/Tourism_in_Armenia
    - RFE/RL (Azatutyun), "'Public' beaches available at Armenia's lake", 8 Jul 2011 (opening of public beaches; no visitor figures): https://www.azatutyun.am/content/article/24259744.html
16. Sibling research files in this repository (secondary; their sources are listed there):
    - `research/B1-m4-traffic.md`: AADT estimates by segment, M-1 July +19.7 %, vehicle mix, dual-carriageway layout, ADB tunnel works.
    - `research/B4-alt-corridors.md`: urban seasonality comparison.
    - `research/A1-macro-consumer.md`: AMD/USD 2025 average 387.01, household car ownership 41.2 % (ILCS 2024), Yerevan population 1,141.1k, Armenia–Russia relations risk.
    - `research/C3-labor.md`: LFS participation 59.9 %, unemployment 13.0 % (Q2 2026).
17. Armstat, quality declarations "20.1 International and domestic tourism – quarterly" and "20.3 Tourists registered in hotels and hotel facilities – quarterly":
    - https://armstat.am/file/Qualitydec/eng/20.1.pdf
    - https://armstat.am/file/Qualitydec/eng/20.3.pdf
    - Index page: https://armstat.am/en/?nid=174
