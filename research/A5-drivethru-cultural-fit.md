# A5 — Can American-style drive-thru culture succeed in Armenia? Regional analogs and adoption evidence

*Workstream A5 of the premium drive-thru coffee & food feasibility study (Armenia). Research date: 2026-10-10. Prices in AMD unless stated; USD at AMD 361.93 (CBA, 9 Oct 2026, from A1).*

Every quantitative claim carries a status tag:

- **VERIFIED**: I opened the primary or official source (or the official dataset/API) myself; URL given.
- **REPORTED**: credible secondary source (news, Wikipedia citing a primary, franchisor marketing, crowd-sourced index, listing); URL given.
- **ESTIMATE**: my own calculation; formula and inputs shown.
- **ASSUMPTION**: a judgment call; basis explained.

Source numbers in [brackets] refer to Section 6. "A1"–"B1" refer to the sibling research files in `research/`, whose own sources are listed there.

> **Method note and limitation (read first).** The shared WebSearch budget for this workflow (200 calls) was **exhausted before this workstream ran its first query**. No keyword searches in English, Armenian or Russian were possible. To avoid inventing anything, everything below comes from (a) primary pages and datasets I could open directly by known URL (World Bank WDI API, CRRC Caucasus Barometer online data, Numbeo city pages, company/franchise sites, Wikipedia articles and the primary sources they cite), (b) my own **OpenStreetMap (Overpass API) extraction**, run on 10 Oct 2026, of every fast-food/café outlet tagged `drive_through=yes` and of the main international QSR brands in Armenia and comparator countries, and (c) the sibling workstreams A1–A4 and B1. As a result, several items the brief asked for, notably **drive-thru share of sales for Vkusno i tochka / Rostic's / Burger King in Russia, Starbucks/KFC drive counts in Kazakhstan, Orlen/Costa/Starbucks drive data in Poland, and Turkish/UAE drive shares, could not be sourced** and are listed as gaps with a verification protocol (Section 5). I did not fill them with remembered figures.

---

## 1. Executive summary

1. **The closest analog, Georgia, shows that drive-thru works in the Caucasus at Armenia's income level, but as an urban QSR habit, not a highway coffee habit.** Georgia's GDP per capita is **$9,692 vs Armenia's $9,474 (2025)** [VERIFIED: World Bank 13]. Household car ownership is **44% in Georgia vs 46% in Armenia; 37% in Tbilisi vs 42% in Yerevan (2024)** [VERIFIED: CRRC 8, 9]. Georgia nevertheless has **21 OSM-mapped drive-thrus** (McDonald's 11, Wendy's 7, Dunkin' 1, Subway 1, one local), **all 21 inside cities** (Tbilisi 15, Batumi 4, Kutaisi 1, Zugdidi 1), on urban arterials and city-exit roads; **none on an intercity highway** [VERIFIED dataset / ESTIMATE classification: OSM 32]. Car ownership is therefore *not* what holds Armenia back relative to Georgia. Across the region, drive-thru is **QSR-led**. Tagged stocks are Poland 459 (McDonald's 268, KFC 120 incl. one tagged "KFC Kołbaskowo"), Ukraine 88 (McDonald's 56), Kazakhstan 14 and Azerbaijan 5, almost all burger/chicken chains; coffee drive-thrus are a handful of small local outlets [OSM 32].
2. **Armenia has almost no drive-thru culture yet, mainly because the brands that create it never arrived.** OSM shows **0 outlets tagged drive-thru in Armenia** (the one real example, Coffee House Drive-Thru on the M4, is untagged; A2/A3). McDonald's has no current or former Armenian entry in Wikipedia's country lists, and OSM has no McDonald's in Armenia [REPORTED: 14; 32; A3]. International QSR units mapped per million people: **Georgia ≈ 38, Azerbaijan ≈ 5, Armenia ≈ 6** [ESTIMATE from OSM 32 and WB population 13]. Georgia alone has **72 mapped Dunkin'** outlets [OSM 32]. Armenia's drive-thru "culture" is a **supply gap more than a proven demand rejection**, but that also means **no one has educated the market** and the first mover pays for it.
3. **The only Armenian test is demand-positive and operations-negative.** The Coffee House Drive-Thru (M4 km ≈12.8, open since ≤ Dec 2024) has daily commuter regulars and peak queues. But **4 of 5 written reviews in Jun–Sep 2026 are 1–2★ for 20–60-minute waits and wrong orders** (A3). Locally, the binding constraint observed so far is **throughput, not willingness to use a lane**.
4. **In Russia, a car-oriented pavilion format is the franchisor's highest-claimed revenue format, but the evidence is franchisor marketing.** Coffee Like (Russia, 1,100+ points including acquired chains [18]; its own site says 900+ [17]) shows its "Автопавильон" (car-oriented pavilion) at **"from" RUB 1.217M "average revenue"** (no period stated; monthly assumed) at a **RUB 392.7 check**. Its walk-up standalone pavilion of the same 10 m² footprint shows **"from" RUB 0.74M at RUB 341**, and the network average was **RUB 450–500k/month (2022)** [REPORTED: 17, 18]. Taken at face value, that implies **+64% revenue and ≈ +43% transactions** for the car-oriented version [ESTIMATE]. Treat it as directional only. *Fact-check correction: the franchise page gives "от" (from) floor figures, states no period, and never calls the format a drive-thru or drive-up (reading it as a car lane is an inference). Its disclaimer calls the figures "for informational purposes" and says they "do not guarantee returns"; the word "illustrative" does not appear. This matches A2's corrected framing. The earlier wording "a car lane lifts coffee-kiosk sales" overstated the evidence.*
5. **In Ukraine and Georgia, roadside coffee became a mass category through fuel retailers, not standalone drive-thrus.**
   - **Ukraine:** WOG sold **> 70,000 cups/day across 386 WOG CAFE points (Oct 2020)**, about **180 cups per point per day**, and **≈150M portions in 7 years** [REPORTED: 19, a paid company placement ("Реклама") from 2020, before the full-scale war; ESTIMATE per point]. OKKO runs **~400 "Hot café" coffee points** at its stations [REPORTED: 22].
   - **Georgia:** **27 of the 72 mapped Dunkin' outlets (38%) sit within 60 m of a fuel station**, and 20 of the 30 adjacent stations are **Wissol** [ESTIMATE (unsaved OSM query): OSM 32; the count of 72 Dunkin' is confirmed in the saved CSV]. *Fact-check: source unreachable on 10 Oct 2026; treat as unverified. The fuel-station proximity extraction was not saved in `research/data/A5-osm-drivethru.csv` (no fuel-station rows, no proximity field) and every Overpass endpoint failed on re-run, so the 27/72 result could not be reproduced.*
   - The American-brand coffee format that scaled in Armenia's income twin appears to have done so largely **on forecourts** (subject to the unverified proximity estimate above), with walk-in service (1 of 72 tagged drive-thru). For the M4 this means **fuel chains own the roadside coffee stop**; A3 found Max Cafe, Flash and CPS already moving in.
6. **Car commuting is common among Yerevan's online respondents but low in the population as a whole, and Yerevan is not very congested.** Numbeo respondents report **car as main commute mode: Yerevan 40%** vs Tbilisi 26%, Almaty 32%, Baku 35%, Warsaw 28%, Moscow 28%, Dubai 82%. But Yerevan's sample is tiny (**n = 47, last updated Nov 2024**) [REPORTED: 1–7]. At population level, only **41–46% of households own a car** (A1 [ILCS]; [8]), and **taxis carried 28.1% of passengers carried by commercial (paid) transport in 2024** (A1, Armstat Yearbook 2025, table 15.4). *Fact-check correction: this was previously given as "28.1% of passenger trips". The statistic excludes private-car trips and walking, so it does not show that taxis carry 28% of all trips; the 2022 figure (1.3%) is not comparable because of a methodology break (from 2023 all e-receipt taxi trips are counted).* Yerevan's Numbeo traffic index (**104**) is the lowest of the comparators (Tbilisi 136, Baku 146, Almaty 148, Dubai 169, Moscow 214). Drive-thru's core promise, saving time in congested car commutes, is weaker in Yerevan than in the cities where it boomed [ASSUMPTION built on REPORTED indices].
7. **Barriers are real but mostly about price and seasonality, not culture per se.** Armenians *do* go out: **59% had been to a restaurant/fast-food place in the previous 6 months** (CB 2019, fieldwork Feb–Mar 2020; Georgia 52%) [VERIFIED: 10, 11]. But **31% of households ran short of money for food at least once in the previous 12 months** (CB 2024) [VERIFIED: 12], and food away from home is only **2.8% of household consumption** (ILCS 2024, A1/A4). Winter at Lake Sevan averages **−2.8°C max / −13.0°C min in January** (1991–2020 normals) [REPORTED: 27]. Cold does not prevent drive-thru use: drive formats operate in colder post-Soviet markets, for example 14 tagged drive-thrus in Kazakhstan including Astana, Karaganda and Pavlodar [32], and Russian car-oriented pavilions [17]. What cold does is shrink the leisure traffic a Sevan-road site depends on [ASSUMPTION].
8. **International failures share three causes that apply to Armenia:** premium import pricing against a strong local café culture, reliance on novelty or seasonal traffic, and fragile supply chains. Cases: **Starbucks Israel** (6 stores, ≈$6M loss, closed 2003); **Starbucks Australia** (closed 61 of 84 stores in 2008: "failed to truly understand Australia's café culture"); **McDonald's Bolivia** (8 outlets, closed 2002, "poor sales and high prices"); **McDonald's Montenegro** (a seasonal Budva outlet, closed for "lack of interest for a permanent location"); **McDonald's Kazakhstan** (24 outlets, exited Jan 2023 over Russian patty-supply restrictions); Dunkin' exits from Poland (2018), Sweden (2018) and South Africa (2019) [REPORTED: 14, 24, 25].
9. **Evidence-weighted verdict (confidence: medium-low).**
   - A **pure, standalone, premium "American" drive-thru on the open M4 highway** is the **weakest** form of the concept (ASSUMPTION; ≈ 25–35% subjective probability of reaching target unit economics).
   - A **drive-thru-led hybrid** has the best odds: a car lane **plus** walk-up window, a few seats or parking, an Armenian-priced core menu and hot food, sited on a **Yerevan arterial or city-exit road** or **co-located with a fuel station** (ASSUMPTION; ≈ 50–60%).
   - This matches where car-based coffee and food demand actually took root: Georgia (urban-arterial QSR lanes; Dunkin' on fuel forecourts, an unverified estimate), Russia (car-oriented pavilions, franchisor claims) and Ukraine (fuel-station cafés).
   - *Fact-check note: after the corrections in this file, the case for a hybrid rests mainly on car ownership (42% of Yerevan households [8]) and the Georgian urban-arterial pattern, and less on drive-uplift claims. The format probabilities are judgement and should not be used as model inputs.*
10. **First adopters (ranked).** (1) Daily car commuters aged ~20–40 on Yerevan exit corridors who already buy Coffee House to-go. (2) Weekend leisure drivers heading to Sevan, Tsaghkadzor and Dilijan (high ticket, strongly seasonal). (3) Professional drivers (taxi/ride-hail, delivery, freight): high frequency, low ticket. (4) Relocants, diaspora and tourists who know the format from Russia, the US, the UAE or Georgia (volatile). Families on day trips are a high-ticket segment when food is offered. [ASSUMPTION; basis in §3.6.]

---

## 2. Key data table

| # | Metric | Value | Period | Status | Source |
|---|---|---|---|---|---|
| 1 | GDP per capita, current US$: Armenia / Georgia / Azerbaijan / Kazakhstan / Russia / Türkiye / Poland / Ukraine / UAE | 9,474 / 9,692 / 7,411 / 14,692 / 17,547 / 18,599 / 28,420 / 5,866 / 50,274 (UAE 2024) | 2025 | VERIFIED | [13] |
| 2 | Population: Armenia / Georgia / Azerbaijan | 3.087 M / 3.936 M / 10.247 M | 2025 | VERIFIED | [13] |
| 3 | Households owning a car: Armenia (Yerevan / other urban / rural) | 46% (42 / 41 / 55) | CB 2024, fieldwork Jul–Oct 2024 | VERIFIED | [8] |
| 4 | Households owning a car: Georgia (Tbilisi / other urban / rural) | 44% (37 / 45 / 48) | CB 2024, fieldwork Apr–May 2024 | VERIFIED | [9] |
| 5 | Household car ownership, Armenia (official survey) | 41.2% | ILCS 2024 | VERIFIED (A1) | A1 [9] |
| 6 | Taxi share of passengers carried by commercial (paid) transport, Armenia (excludes private cars and walking) | 28.1% (2022 figure of 1.3% not comparable: methodology break) | 2024 | VERIFIED (A1) | A1 (Armstat Yearbook 2025, table 15.4). *Fact-check correction: was "taxi share of passenger trips"; this is not a share of all trips.* |
| 7 | Registered vehicles (all types): Armenia / Yerevan | 953,965 / 343,220 | as of 1 Sep 2024 (date to confirm) | REPORTED (A1) | A1 [32] |
| 8 | Main commute mode = car (Numbeo respondents): Yerevan / Tbilisi / Almaty / Baku / Warsaw / Moscow / Dubai | 40.4% / 25.6% / 31.8% / 34.9% / 27.6% / 28.1% / 82.4% | updates Nov 2024 – Aug 2026; n = 47 / 82 / 63 / 63 / 252 / 675 / 346 | REPORTED (crowd-sourced; low reliability for small n) | [1]–[7] |
| 9 | Numbeo Traffic Index: Yerevan / Tbilisi / Almaty / Baku / Warsaw / Moscow / Dubai | 104 / 136 / 148 / 146 / 123 / 214 / 169 | same | REPORTED | [1]–[7] |
| 10 | Average one-way car commute, Yerevan | 21.5 min (9.7 km); all modes 30.5 min | Nov 2024 | REPORTED (n = 47) | [1] |
| 11 | Went to a restaurant/pizzeria/fast food in past 6 months: Armenia / Georgia | 59% / 52% | CB 2019 (AM fieldwork Feb–Mar 2020, pre-COVID and 6.5 years old; GE Oct–Nov 2019) | VERIFIED (not a current demand measure) | [10], [11] |
| 12 | Households short of money for food at least once in past 12 months, Armenia | 31% (daily 2, weekly 4, monthly 8, less often 17; never 68) | CB 2024 | VERIFIED | [12] |
| 13 | Food away from home, share of household consumption, Armenia | 2.8% national; 3.5% urban | ILCS 2024 | VERIFIED (A1/A4) | A4 |
| 14 | Fast-food/café outlets tagged `drive_through=yes`: Armenia / Georgia / Azerbaijan | 0 / 21 / 5 | OSM snapshot 10 Oct 2026 | VERIFIED (dataset; lower bound) | [32] |
| 15 | Georgia drive-thrus by brand and city | McDonald's 11, Wendy's 7, Dunkin' 1, Subway 1, Adrenaline 1; Tbilisi 15, Batumi 4, Kutaisi 1, Zugdidi 1; 0 on intercity highways | OSM 10 Oct 2026 | VERIFIED dataset / ESTIMATE (road classification) | [32] |
| 16 | International QSR outlets mapped in OSM: Georgia / Armenia / Azerbaijan | 148 (Dunkin' 72, McD 28, Wendy's 22, KFC 18, BK 6, Costa 1, Starbucks 1) / 18 (KFC 13, BK 4, Wendy's 1) / 55 (McD 28, KFC 13, Starbucks 6, Costa 5, BK 3) | OSM 10 Oct 2026 | VERIFIED (dataset; mapping is incomplete) | [32] |
| 17 | International QSR outlets per million people: Georgia / Armenia / Azerbaijan / Kazakhstan | ≈ 37.6 / 5.8 / 5.4 / 5.9 | 2025–26 | ESTIMATE (row 16 ÷ row 2; Kazakhstan 122 ÷ 20.84 M) | [32], [13]. *Fact-check correction: Kazakhstan added from the saved CSV (KFC 50, Starbucks 34, BK 21, McDonald's-tagged 11, Costa 4, Wendy's 2).* |
| 17a | Georgian Dunkin' outlets within 60 m of a fuel station | 27 of 72 (38%); adjacent stations: Wissol 20, SOCAR 3, others 7 | OSM 10 Oct 2026 | ESTIMATE (unsaved OSM query; 72 count confirmed in CSV) | [32]. *Fact-check: source unreachable on 10 Oct 2026; treat as unverified (proximity extraction not saved; Overpass re-runs failed).* |
| 17c | Fast-food/café outlets tagged drive-thru, Ukraine; of which McDonald's | 88; McDonald's 56 (≥ 41% of its 135 outlets), KFC 7; 10 café/coffee-type (local, e.g., "Lysko Drive", "Kava Plus", "Lviv Croissants") | OSM 10 Oct 2026; outlet total 31 Dec 2025 | VERIFIED (dataset) / ESTIMATE (share) | [32], [14] |
| 17d | McDonald's units with a drive lane (OSM lower bound): Georgia / Ukraine / Azerbaijan | ≥ 41% (11/27) / ≥ 41% (56/135) / ≥ 6% (2/34) | 2025–26 | ESTIMATE (OSM tags ÷ company totals) | [32], [14] |
| 17e | Fast-food/café outlets tagged drive-thru, Poland | 459 (≈ 12.6 per million): McDonald's 268 (≥ 43% of 618), KFC 120 (119 + 1 tagged "KFC Kołbaskowo"), BK 13, Max 10, Popeyes 7; coffee ≈ 3 | OSM 10 Oct 2026 | VERIFIED (dataset) / ESTIMATE (ratios) | [32], [14], [13] |
| 17b | Fast-food outlets tagged drive-thru, Kazakhstan | 14 (ex-McDonald's "I'm" 5, KFC 3, BK 2, Hardee's 1, local 3); in cities/towns (Almaty, Astana, Aktobe, Karaganda, Pavlodar, Zhetysay, one in western KZ at 46.96 N 53.99 E); 0 coffee | OSM 10 Oct 2026 | VERIFIED (dataset; lower bound) | [32] |
| 18 | McDonald's outlets: Georgia / Azerbaijan / Türkiye / Poland / UAE / Ukraine / Armenia | 27 / 34 / 306 / 618 / 222 / 135 / 0 (no Armenian entry in current or former lists) | 31 Dec 2025 | REPORTED (Wikipedia citing McDonald's corporate) | [14] |
| 19 | McDonald's share of US business through drive-thru | ≈ 70% | 2017 | REPORTED (Wikipedia citing Quartz) | [16] |
| 20 | Coffee Like (RU) "Автопавильон" (car-oriented pavilion; page never says drive-thru): investment / "average revenue" / check | from RUB 2.0M / **from** RUB 1.217M (period not stated; monthly assumed) / RUB 392.7 | undated (2025–26 site) | REPORTED (franchisor claim; "for informational purposes", "do not guarantee returns") | [17]. *Fact-check correction: revenue is an "от" (from) floor figure, no period stated; drive lane is inferred, not stated.* |
| 21 | Coffee Like walk-up standalone pavilion: revenue / check | from RUB 0.74M (period not stated) / RUB 341 | same | REPORTED (franchisor claim) | [17] |
| 22 | Coffee Like network average revenue per point | RUB 450–500k/month; 920 points; group revenue RUB 5.6bn (2022), RUB 7.0bn (2023) | 2022–23 | REPORTED | [18] |
| 23 | Car-oriented-pavilion uplift vs walk-up pavilion (franchisor floor figures taken at face value) | Revenue +64%; transactions ≈ +43% | — | ESTIMATE (1.217/0.74; ÷ (392.7/341)); arithmetic correct, inputs are marketing "from" figures | [17] |
| 24 | WOG (Ukraine) coffee volume | > 70,000 cups/day; 386 WOG CAFE (incl. 14 Intercity train cafés, 4 airports, 1 city café); ≈ 150M portions since 2013; €10M+ invested | Oct 2020 (pre-full-scale-war) | REPORTED (company claim in a paid placement marked "Реклама") | [19] |
| 25 | WOG cups per point per day | ≈ 181 | Oct 2020 | ESTIMATE (70,000 / 386) | [19] |
| 26 | OKKO coffee points at stations | ~400 "Hot café" | undated (Wikipedia) | REPORTED | [22] |
| 27 | Coffee House Drive-Thru (M4 km ≈12.8) reviews | 4.9★ / 123 ratings; 17 text reviews avg 3.76★; 4 of 5 Jun–Sep 2026 reviews 1–2★ (20–60 min waits) | Dec 2024 – Oct 2026 | REPORTED (A3) | A3 [22] |
| 28 | Lake Sevan climate, January mean max / min; record lows | −2.8°C / −13.0°C; February record −26.2°C; absolute record −26.8°C (March) | 1991–2020 normals | REPORTED (Wikipedia citing NOAA/WMO) | [27]. *Fact-check correction: −26.2°C is the February record, not the absolute record low.* |
| 29 | Yerevan climate, January mean max / min; snowy days | 1.7°C / −7.8°C; ≈7 snowy days in January (22 a year) | 1991–2020 | REPORTED | [29] |
| 30 | Road deaths per 100,000: Armenia / Georgia / Azerbaijan / Türkiye / Poland / US | 13.6 (2021) / 12.4 (2019) / 17.2 (2021) / 6.7 (2019) / 5.0 (2022) / 14.2 (2021) | 2019–22 | REPORTED (Wikipedia citing WHO) | [30] |
| 31 | Starbucks: Israel exit / Australia closures / Kazakhstan stores / Russia exit | 6 stores closed 2003 (≈$6M loss) / 61 of 84 closed 2008 (another Wikipedia passage says 61 of 85) / 30 (first Dec 2015; OSM maps 34, so the Wikipedia count may be out of date) / 130 stores exited 2022 | various | REPORTED | [24] |
| 32 | McDonald's exits: Bolivia / Montenegro / Kazakhstan | 8 outlets, 1997–2002 ("poor sales and high prices") / 1 seasonal outlet 2004–07 ("lack of interest for a permanent location") / 24 outlets, 2016–Jan 2023 (supply restrictions) | — | REPORTED | [14], [15] |
| 33 | Suburb populations: Abovyan (M4) / Vagharshapat (M5) / Masis (M2) / Ashtarak (M1/Ashtarak hwy) | 46,434 / 44,837 / 20,081 / 15,686 | 2022 census | REPORTED (Wikipedia citing census) | [31] |

---

## 3. Detailed findings and analysis

### 3.1 Framing: what "drive-thru culture" requires

A drive-thru habit forms when four conditions hold together [ASSUMPTION; synthesis of the analog evidence below]:

1. **Car access** among the target group, not just the population average.
2. **A time or convenience penalty** for parking and walking in: congestion, scarce parking, bad weather, children in the car.
3. **A habitual, portable product** (coffee, burgers) at a **price compatible with frequent purchase**.
4. **Supply**: an operator that builds lanes at the right sites and delivers fast, reliable service. In most markets this was a global QSR brand teaching the behaviour.

The sections below test each condition for Armenia against the comparator markets.

### 3.2 Regional analogs

#### 3.2.1 Comparator overview

| Market | GDP/cap 2025 (US$) [13] | Car ownership / car commuting | Drive-thru evidence found (this session) | Who built the habit | Status |
|---|---|---|---|---|---|
| **Armenia** | 9,474 | HH car 46% (Yerevan 42%) [8]; Numbeo car commute 40% (n = 47) [1]; taxi 28.1% of passengers on commercial (paid) transport, not of all trips (A1) | 1 drive-thru (Coffee House, M4, ≤ Dec 2024; A2/A3); 0 OSM-tagged [32]; KFC (14): ordering platform flags `drive_thru:false`, but the same config sets `sitin:false` although restaurants have seats, so this is an online-ordering setting, not proof of no lane (A3); Wendy's first unit opened Dec 2025, current count unverified, 20 planned by 2030 (A3). *Fact-check correction: taxi wording, KFC flag caveat and Wendy's count aligned with A1/A3.* | Nobody yet; no McDonald's (absent from Wikipedia's current and former lists and from OSM) [14][32] | VERIFIED / REPORTED |
| **Georgia** | 9,692 | HH car 44% (Tbilisi 37%) [9]; Numbeo car commute 26% (n = 82) [2] | **21 OSM-tagged drive-thrus, all urban** (McD 11, Wendy's 7, Dunkin' 1, Subway 1, local 1) [32]; McDonald's 27 outlets [14]; Dunkin' 72 mapped [32]; Starbucks entered Jul 2026 via Alshaya (A2) | McDonald's (since 1999), Wendy's | VERIFIED (OSM) / REPORTED |
| **Azerbaijan** | 7,411 | Numbeo car commute 35% (n = 63) [4] | 5 OSM-tagged (McD 2 in Baku, 2 local Baku QSRs, 1 kebab house on a Karabakh road) [32]; McDonald's 34 outlets [14]; Starbucks 4 (Wikipedia) – 6 (OSM) [24][32] | McDonald's | VERIFIED (OSM) / REPORTED |
| **Kazakhstan** | 14,692 | Numbeo car commute (Almaty) 32% (n = 63) [3] | McDonald's operated 2016–Jan 2023 (24 outlets), then rebranded locally [14][15]; Starbucks 30 stores (first Dec 2015) [24] (OSM maps 34 [32]); 122 international-QSR units mapped in OSM (KFC 50, Starbucks 34, BK 21) [32]; **14 OSM-tagged drive-thrus, all QSR, all urban, none coffee** [32]; drive share of sales **not obtained** | KFC, McDonald's/"I'm", BK, Hardee's | VERIFIED (OSM) / REPORTED; share GAP |
| **Russia** | 17,547 | Numbeo car commute (Moscow) 28% (n = 675) [7] | Vkusno i tochka (ex-McDonald's, 850 restaurants taken over; 830 points Nov 2022; "980+" later) [14][15][36]; Rostic's 1,000+ (end-2024) [34]; Coffee Like car-oriented "Автопавильон" format (page never says drive-thru) [17]; McDonald's originally used walk-up windows because most families had no car [16]. **Drive-thru sales shares not obtained** | McDonald's/Vkusno i tochka, KFC/Rostic's, BK, kiosk chains | REPORTED; share data GAP |
| **Ukraine** | 5,866 | — | WOG > 70k cups/day at 386 cafés (2020) [19]; OKKO ~400 coffee points [22]; McDonald's 135 outlets [14]; **88 OSM-tagged drive-thrus** (McD 56, KFC 7, 10 small local coffee/café drives) [32] | Fuel retailers (WOG, OKKO) | REPORTED |
| **Türkiye** | 18,599 | — | McDonald's 306 outlets [14]; 75 OSM-tagged drive-thrus, clearly under-tagged (McD 8) [32] | Global QSR + fuel stations | REPORTED / GAP |
| **Poland** | 28,420 | Numbeo car commute (Warsaw) 28% (n = 252) [5] | McDonald's 618 outlets (Dec 2025) [14]; 550 (Apr 2024), 2024 revenue PLN 2.457bn [35]; Dunkin' entered 2015 and withdrew 2018 [25]; **459 OSM-tagged drive-thrus (McD 268, KFC 120; coffee ≈ 3)** [32]; drive share of sales not obtained | McDonald's, KFC/BK, fuel chains | VERIFIED (OSM) / REPORTED; share GAP |
| **UAE** | 50,274 (2024) | Numbeo car commute (Dubai) 82% (n = 346) [6] | McDonald's 222 outlets [14]; 50 OSM-tagged drive-thrus, clearly under-tagged (McD 9) [32] | Global QSR | REPORTED / GAP |

**Reading.**
- The comparators that look like Armenia on income and car ownership (Georgia, Azerbaijan, Ukraine) are exactly the ones where drive-thru remains a **minority format embedded in urban QSR**, or where roadside coffee was captured by **fuel retail** [19][22][32].
- The one market here where car commuting dominates (Dubai, 82% [6]) also has an income more than 5× Armenia's [13].
- Russia, Türkiye and Poland have national QSR estates of roughly 300–1,000+ units each (McDonald's 306 Türkiye and 618 Poland; Vkusno i tochka ~830–980 and Rostic's 1,000+ in Russia) [14][34][36]. Drive lanes form part of those estates, but their sales shares were not obtained (GAP). Armenia has no estate of that kind: KFC 14, BK ~5, Wendy's 1 confirmed (first unit Dec 2025; current count unverified) (A3).
- Kazakhstan, richer than Armenia, still shows only 14 tagged drive-thrus, all QSR [32] [ESTIMATE/ASSUMPTION built on the cited counts]. Its mapped international-QSR density (≈ 5.9 per million: 122 ÷ 20.84 M) is about the same as Armenia's (≈ 5.8) [ESTIMATE: 32, 13].

#### 3.2.2 Georgia: the closest analog

- **Macro twin.** GDP per capita is $9,692 vs $9,474 (2025) and urbanisation 61.2% vs 65.9% [VERIFIED: 13]. Car ownership is 44% vs 46% (2024), with the capital *lower* in Georgia (Tbilisi 37% vs Yerevan 42%) [VERIFIED: 8, 9]. Going out is slightly *less* common in Georgia (52% vs 59% visited a restaurant or fast-food place in the past 6 months, CB 2019) [VERIFIED: 10, 11].
- **Drive-thru stock (OSM, 10 Oct 2026)** [VERIFIED dataset: 32]:

| City | Drive-thrus tagged | Brands | Road context (major road within 120 m) | Hours (where tagged) |
|---|---|---|---|---|
| Tbilisi | 15 | McDonald's 8, Wendy's 6, Adrenaline 1 | Urban arterials and city-exit trunks: Kakheti Hwy (S5, airport/Kakheti exit) ×2, Gelovani Ave, Aghmashenebeli Alley (Mtskheta/E60 exit), Kartul-Amerikuli Megobroba Ave ×2, 26 May Sq ×2, Right Embankment, Kosmonavtebi Emb., Tsereteli Ave, Navtlughi St, Tornike Eristavi St | 08:00–24:00 typical; 3 are 24/7 |
| Batumi | 4 | McDonald's 1; Wendy's + Dunkin' + Subway sharing one site | City streets (Khimshiashvili, Abuseridze) | 09:00/10:00–01:00 |
| Kutaisi | 1 | McDonald's | City centre (Tbilisi St / Aghmashenebeli Sq) | 24/7 |
| Zugdidi | 1 | McDonald's | S1 trunk through town (Gamsakhurdia Ave) | 09:00–24:00 |
| **Intercity highways** | **0** | — | A few roadside cafés named "Drive", "Sky Drive" and "Mars Drive" exist (Kakheti; Georgian Military Road) but are **not** tagged as drive-thrus | — |

  *Road context is ESTIMATE: nearest `highway=motorway/trunk/primary/secondary` ways within 120 m, from OSM.*

- **Share of the McDonald's estate with a lane.** 11 of 28 mapped McDonald's (39%) are tagged drive-thru, i.e. ≥ 41% of the 27 outlets the company reports [ESTIMATE: 32, 14]. Untagged lanes exist in OSM, so this is a lower bound. A Georgian McDonald's store list should confirm it (GAP).
- **To-go coffee at scale, largely on forecourts.** Dunkin' has **72 mapped outlets** in Georgia, only one tagged drive-thru [32].
  - **27 of the 72 (38%) lie within 60 m of a fuel station.** The 30 adjacent stations are Wissol 20, SOCAR 3, Rompetrol/Lukoil/Portal/Go 1 each, and 3 unbranded [ESTIMATE (unsaved OSM query): 32]. *Fact-check: source unreachable on 10 Oct 2026; treat as unverified. The 72 Dunkin' count is confirmed in the saved CSV (27/72 = 37.5%), but the fuel-station proximity extraction was not saved and could not be re-run (all Overpass endpoints failed). The fuel-station-hybrid recommendation should not lean on this figure until it is re-extracted and saved.*
  - The arrangement looks like a fuel-retailer partnership. The operator relationship is **not verified** here (GAP).
  - An American-branded coffee-and-donut format can therefore reach scale in a market with Armenia's income. It did so as **walk-in kiosks, a large share of them apparently at fuel stations (unverified, see above)**, not as drive-thrus [ESTIMATE/ASSUMPTION]. Starbucks only arrived in **July 2026** (Tbilisi, Alshaya), and OSM shows 1 store (A2; [32]).
- **Mapping completeness check.** OSM brand counts track official totals closely: McDonald's Georgia 28 mapped vs 27 reported by the company [14]; KFC Armenia 13 mapped vs 14 on the company site (A3); McDonald's Azerbaijan 28 vs 34 [14]. Brand-level comparisons are therefore usable. Drive-thru *tags*, however, are a lower bound [ESTIMATE].
- **Implication.** In Georgia, drive-thru demand appeared where (a) a global QSR with a drive-thru playbook built freestanding units, (b) on **urban arterials and city exits**, (c) open **late** (to midnight or 24/7). Roadside coffee appears to have scaled through **forecourt kiosks** (Dunkin' at Wissol; proximity estimate unverified). Neither took the form of a standalone highway coffee drive-thru [ASSUMPTION]. This is the most transferable evidence for Armenia because the macro conditions are nearly identical.

#### 3.2.3 Russia: drive formats at scale, plus kiosk coffee

- **History.** Wikipedia records that McDonald's in Russia first used *walk-up windows* "because most families did not own cars" [REPORTED: 16]. The drive format followed motorisation; it did not lead it [ASSUMPTION].
- **Scale.** Vkusno i tochka took over McDonald's' **850 restaurants** in June 2022 (830 points in 62 regions in Nov 2022; "980+" in a later company figure) [REPORTED: 14, 15, 36]. Rostic's (ex-KFC Russia) reports **1,000+ locations** (end-2024) and 2023 revenue of RUB 20.17bn [REPORTED: 34].
- **Drive-thru share of sales:** **not found** (Russian Wikipedia pages carry no channel split; the Vkusno i tochka site returned 403). See Section 5.
- **Car-oriented coffee kiosks (Coffee Like, franchisor claims)** [REPORTED: 17, 18]:

| Format (Coffee Like) | Investment from | "Average revenue", **from** (period not stated; monthly assumed) | Avg. check | Area | Payback from |
|---|---|---|---|---|---|
| **"Автопавильон" (car-oriented pavilion; page never says drive-thru)** | **RUB 2.0M** | **RUB 1.217M** | **RUB 392.7** | 10 m² | 6 months |
| Café | RUB 2.1M | RUB 1.010M | RUB 400 | 30 m² | 8 months |
| Food truck | RUB 2.3M | RUB 0.822M | RUB 383.2 | 12 m² | 11 months |
| Standalone pavilion (walk-up) | RUB 1.65M | RUB 0.740M | RUB 341 | 10 m² | 9 months |
| Mini-café | RUB 1.0M | RUB 0.631M | RUB 335 | 10 m² | 6 months |
| Counter | RUB 1.0M | RUB 0.566M | RUB 330 | 6 m² | 7 months |
| *Network average (2022)* | — | *RUB 450–500k* | — | — | — |

  - The car-oriented pavilion is the chain's **highest-claimed revenue format**: 1.64× the walk-up pavilion of the same footprint and 2.4–2.7× the 2022 network average [ESTIMATE, on franchisor floor figures].
  - Transactions are ≈ +43% vs the walk-up pavilion: (1.217/0.740) ÷ (392.7/341) = 1.645 ÷ 1.152 ≈ 1.43 [ESTIMATE].
  - **Caveats:** these are undated franchisor marketing figures shown as "от" (from) values, with no period stated. The disclaimer says they are "for informational purposes" ("ознакомительный характер") and "do not guarantee returns". The format is called "Автопавильон"; the page never says drive-through or drive-up, so reading it as a car lane is an inference. Revenue/label pairing follows the page layout. Site selection bias is likely: car-oriented pavilions sit on the best roadside plots [ASSUMPTION].
  - *Fact-check correction: earlier wording called these "average monthly revenue" figures for a "drive-up" format "labelled 'illustrative'". The page shows floor ("from") figures, no period, no drive-thru wording and no "illustrative" label. The arithmetic (+64% revenue, ≈ +43% transactions) is correct, but the inputs are marketing floor claims. Aligned with A2's corrected framing.*
  - Network size: the franchisor site says "900+ кофеен" [17]; the 1,100+ figure in §1 comes from ru.wikipedia and includes chains acquired in 2024 (Coffee Moose, Gudmen and others) [18].
  - **Ticket context:** RUB 392.7 ≈ AMD 1,670 (A2's conversion; AMD 1,676 at CBA 4.2677 AMD/RUB, 9 Oct 2026), about **1.7–2.1× Armenia's mass to-go price** (800–1,000 AMD; A2). The Russian car-pavilion check is in line with Armenia's *premium* chains (1,600–1,950), not its mass market.

#### 3.2.4 Ukraine: highway coffee captured by fuel retail

- **WOG.** The "Найкавовіша кава" (most coffee coffee) project started on 1 Oct 2013 with Franke machines. By Oct 2020, WOG had **386 WOG CAFE** points (14 on Intercity trains, 4 at airports, 1 city café; the rest at stations). It sold **"more than 70 thousand portions of coffee every day"** and **"almost 150 million portions"** cumulatively, after **"more than €10 million"** invested over 7 years. A 2017 Nielsen study placed WOG first among fuel chains in the coffee category [REPORTED: 19 (Mind.ua, 2 Oct 2020)]. *Fact-check note: the Mind.ua item is labelled "Реклама" (paid company placement), so these are advertorial company claims; the data are from 2020, before the full-scale war, and 6 years old.* Later counts: 368 WOG Cafe / 245 WOG Market (en.wikipedia) and 345 WOG CAFE / 355 WOG MARKET (uk.wikipedia, citing Forbes.ua 2024) [REPORTED: 21, 23].
  - **Per point:** ≈ 70,000 / 386 ≈ **181 cups/day** [ESTIMATE]. The 386 includes 19 non-forecourt points (trains, airports, a city café), so this is not a pure forecourt average. That is above the 80–150 transactions/day A2 assumed for a well-sited Armenian unit, but it averages over a national network on main roads, in a market of 39 M people with a long-established "coffee at the pump" habit.
  - **Non-fuel conversion matters.** At WOG's flagship Kyiv–Chop highway complex (5 food concepts including McDonald's and WOG CAFE, 160 seats), non-fuel sales per fuel receipt ran **312% above** the network average in Oct 2024 [REPORTED: 20].
- **OKKO.** "Almost 400" Hot café coffee outlets at its stations; 32 A la minute fast-food restaurants (2014) [REPORTED: 22].
- **Drive-thru stock (OSM, 10 Oct 2026).** **88 tagged** fast-food/café drive-thrus [VERIFIED dataset: 32]:
  - **McDonald's 56**, i.e. ≥ 41% of its 135 Ukrainian outlets [ESTIMATE with 14]. That is the same lower-bound share as in Georgia (11 of 27).
  - KFC 7.
  - **10 café/coffee-type** outlets, all small local brands ("Lysko Drive", "Kava Plus", "Lviv Croissants", "Кав'ярня Max Drive", "Fresh & Panini", "Eaty").
  - The reported Ukrainian drive-coffee kiosk boom is therefore *visible* in OSM but small and fragmented. Its true size is a GAP: OSM under-tags small kiosks [ASSUMPTION].
- **Reading.** In Ukraine, which has a large, documented fuel-station coffee business [19][22], the winner was the **fuel retailer**, not a standalone drive-thru. The forecourt already has traffic, parking, toilets and a reason to stop [ASSUMPTION]. The Ukrainian drive-thru coffee kiosk scene shows up in OSM only as about 10 small local outlets. Its real scale, unit volumes and survival rates could **not** be documented this session (GAP).

#### 3.2.5 Kazakhstan and Azerbaijan

- **Kazakhstan.**
  - Starbucks has **30 stores** per Wikipedia, the first opened in Almaty on 18 Dec 2015 [REPORTED: 24]. OSM maps 34 [32], which suggests the Wikipedia count is out of date.
  - McDonald's operated 24 outlets from 2016 until **5 Jan 2023**. It closed because restrictions blocked burger-patty imports from Russia, and the local operator rebranded ("Мы открыты" → "Мен (имя)" → "I'm", Nov 2023) [REPORTED: 14, 15].
  - **Lesson for Armenia:** a QSR supply chain routed through Russia/EAEU is a strategic risk. Armenia itself saw Russian bans on Armenian agri-food in Apr–Jun 2026 (A1).
  - **OSM drive-thrus (10 Oct 2026): 14 tagged**, all QSR and all urban: the ex-McDonald's "I'm" chain 5, KFC 3, Burger King 2, Hardee's 1, local burger/kebab 3 (Almaty, Astana, Aktobe, Karaganda, Pavlodar, Zhetysay, and one in western Kazakhstan). **None is a coffee outlet** [VERIFIED dataset: 32]. That is ≈ 0.7 per million people (14 / 20.84 M) [ESTIMATE]. Tagging is incomplete, so treat it as a floor. Opening hours run late (to 24:00–04:00), as in Georgia.
  - Brand totals for KFC/BK in Kazakhstan were not obtained (the Overpass query timed out).
- **Azerbaijan.**
  - OSM shows **5 drive-thrus**: 2 McDonald's and 2 local QSRs in Baku, plus 1 kebab house on a Karabakh road. Mapped international QSR: McDonald's 28, KFC 13, Starbucks 6, Costa 5, BK 3 [VERIFIED dataset: 32]. McDonald's reports 34 outlets [14].
  - At a 10.2 M population this is ≈ 0.5 drive-thrus per million vs Georgia's 5.3 [ESTIMATE]. On OSM evidence drive-thru looks marginal in Azerbaijan, but tagging may be incomplete: only 2 of 34 McDonald's are tagged [ASSUMPTION].

#### 3.2.6 Türkiye, Poland, UAE, and the cross-country OSM extraction

For Türkiye, Poland and the UAE I could only verify outlet totals (McDonald's 306 Türkiye, 618 Poland, 222 UAE as of 31 Dec 2025 [14]) and the car-commute contrast (Dubai 82% vs Warsaw 28%) [5, 6]. **Drive-thru share of sales** for Costa/Starbucks/McDonald's in Poland, TAB Gıda (Burger King) in Türkiye and Americana in the UAE could not be sourced (no search budget; annual-report URLs unknown). These matter less for Armenia than Georgia/Russia/Ukraine, which are closer on income, car access and culture [ASSUMPTION].

**OSM cross-country extraction (10 Oct 2026)** [VERIFIED dataset: 32; per-million figures are ESTIMATES using WB 2025 population [13]]:

| Country | Fast-food/café outlets tagged `drive_through=yes` | Per million people | Of which coffee/café-type | McDonald's tagged / company total (lane share, lower bound) | Main brands among tagged drive-thrus | Where |
|---|---|---|---|---|---|---|
| **Armenia** | **0** (1 known untagged: Coffee House M4) | 0 (0.3 incl. Coffee House) | 0 (1) | — / 0 | — | M4 km ≈12.8 (A3) |
| **Georgia** | **21** | **5.3** | 1 (Dunkin', Batumi) | 11 / 27 (≥ 41%) | McDonald's 11, Wendy's 7 | All urban: Tbilisi 15, Batumi 4, Kutaisi 1, Zugdidi 1 |
| Azerbaijan | 5 | 0.5 | 0 | 2 / 34 (≥ 6%) | McDonald's 2 | Baku 4; 1 roadside kebab house |
| Kazakhstan | 14 | 0.7 | 0 | n/a (McD exited 2023; successor "I'm" 5) | "I'm" 5, KFC 3, BK 2 | All urban |
| Ukraine | 88 | 2.3 | 10 (small local brands) | 56 / 135 (≥ 41%) | McDonald's 56, KFC 7 | Mostly urban/peri-urban (not classified) |
| UAE | 50 | 4.3 | 8 (Starbucks 3, Costa 2, Dunkin' 1, local 2) | 9 / 222 (≥ 4%) | McDonald's 9, KFC 4, Starbucks 3 | Not classified; **clearly under-tagged** |
| Türkiye | 75 | 0.9 | 18 (all small local cafés/patisseries) | 8 / 306 (≥ 3%) | McDonald's 8, Kumrucu Hüseyin 4, BK 3; many local döner/kebab | Not classified; **clearly under-tagged** |
| **Poland** | **459** | **12.6** | ~3 (Starbucks 1, Costa 1, local 1) | 268 / 618 (≥ 43%) | McDonald's 268, KFC 119, BK 13, Max 10, Popeyes 7 | Not classified (national) |
| Russia | *Overpass query timed out repeatedly (server load); not obtained* | — | — | — | — | GAP |

**How to read this table.**
- OSM `drive_through` tags depend on how diligent local mappers are. The UAE and Türkiye rows (only 4% and 3% of McDonald's tagged) show that tag counts **understate** real stocks, sometimes by an order of magnitude.
- The tags are therefore only usable *within* well-mapped markets and as floors. Georgia, Ukraine and Poland reach a similar ≥ 41–43% McDonald's lane share, which suggests their tagging is reasonably complete for big brands [ASSUMPTION].
- **Poland is the instructive case.** At 3× Armenia's GDP per capita [13], it has the region's densest tagged stock (≈ 12.6 per million). Of 459 tagged drive-thrus, **≈ 99% are burger/chicken QSR**: McDonald's 268, KFC 119, BK 13, Max 10, Popeyes 7. Only ~3 coffee outlets are tagged [32]. Even in a mature Central European drive-thru market, the lane is a QSR asset, not a coffee one, at least on OSM evidence [ESTIMATE/ASSUMPTION].
- The robust conclusions are three:
  1. Wherever drive-thru exists in the region, it is **QSR-led**.
  2. Coffee drive-thrus are rare and local.
  3. Armenia is at **zero** on the QSR route that built the habit elsewhere.

#### 3.2.7 United States benchmark (for scale only)

- McDonald's: ≈ **70%** of US business through drive-thru (2017) [REPORTED: 16].
- US average drive-thru service time: **244.9 s** in the QSR 2024 study [REPORTED: 16, citing QSR]. Typical lane stacking holds 4–6 cars [16].
- Dutch Bros, the archetypal drive-thru-first coffee chain, grew from 61 shops (2004) to 1,002 (2025), with **US$1.17bn revenue (2024)**. "The vast majority" of its shops have no indoor seating [REPORTED: 26].
- Starbucks: in June 2020 it announced it would close up to 400 US/Canada stores over 18 months and shift to "convenience-led" formats with drive-thru and curbside pickup [REPORTED: 24].

These numbers describe a market with near-universal car commuting and ~9.5× Armenia's GDP per capita ($90,027 vs $9,474) [13]. **They should not be used to calibrate Armenian volumes** [ASSUMPTION].

### 3.3 Car culture and commuting in Armenia

#### 3.3.1 Who has a car

| Indicator | Armenia | Georgia | Source |
|---|---|---|---|
| HH owns a car (national) | 46% (CB 2024) / 41.2% (ILCS 2024) | 44% (CB 2024) | [8], [9]; A1 |
| Capital city | **Yerevan 42%** | Tbilisi 37% | [8], [9] |
| Other urban | 41% | 45% | [8], [9] |
| Rural | 55% | 48% | [8], [9] |
| Registered vehicles, all types | 953,965 (Yerevan 343,220); ≈ 310 per 1,000 residents | n/f | A1 (REPORTED + ESTIMATE) |
| Taxi share of passenger trips | 28.1% (2024; 1.3% in 2022, the jump partly reflects e-receipt recording) | n/f | A1 (VERIFIED) |

- **Reading.** Fewer than half of Yerevan households have a car [VERIFIED: 8]. A drive-thru can address at most ~40–45% of Yerevan households, and in practice a younger, higher-income subset [ASSUMPTION].
- Ride-hailing (taxi = 28% of trips) moves a large share of trips into cars that are **not** driven by the consumer. Taxi drivers are a potential repeat segment, but their passengers rarely stop [ASSUMPTION].
- Rural ownership is higher (55%), but rural incomes are lower. Corridor towns are poorer than Yerevan (Kotayk wage 58% of Yerevan; A1).

#### 3.3.2 Congestion and commuting

| City | Car as main commute mode | Avg one-way commute | Traffic Index | Contributors | Last update |
|---|---|---|---|---|---|
| **Yerevan** | **40.4%** | 30.5 min (car 21.5 min / 9.7 km; bus 52.2 min) | **104.4** | 47 | 28 Nov 2024 |
| Tbilisi | 25.6% | 38.0 min | 135.6 | 82 | 15 May 2026 |
| Almaty | 31.8% | 38.7 min | 148.4 | 63 | 4 Aug 2026 |
| Baku | 34.9% | 37.9 min | 146.1 | 63 | 4 Jan 2026 |
| Warsaw | 27.6% | 34.8 min | 122.7 | 252 | 13 May 2026 |
| Moscow | 28.1% | 50.5 min | 214.4 | 675 | 4 Jun 2026 |
| Dubai | 82.4% | 36.3 min | 169.4 | 346 | 17 Jun 2026 |

*All Numbeo [1]–[7]; REPORTED, crowd-sourced, respondents skew to internet-active, higher-income and expat users. Yerevan's n = 47 is too small for inference.*

- **Disconfirming signal.** Yerevan reports the *shortest* car commutes and the *lowest* congestion index of the comparators. Where congestion is low and on-street parking is easy enough, the drive-thru's time saving over "park and run in" shrinks [ASSUMPTION]. Central-Yerevan parking difficulty could **not** be quantified this session: paid-parking tariffs, space counts and enforcement are a GAP (Section 5).
- **Supportive signal.** Among the online/expat-skewed respondents, Yerevan has the highest car-commute share after Dubai (40%). That fits a premium target segment that commutes by car even if the population as a whole does not [ASSUMPTION].
- **Public transport is being upgraded**, which slightly weakens the car-commuting trend. Yerevan bought 749 buses in 2020–24; 64 bus routes ran 752 buses in 2026; e-ticketing became universal from 1 Jan 2025; minibus routes fell to 11 [REPORTED: 29].

#### 3.3.3 Suburban commuting corridors

| Suburb | Pop. (2022 census) | Radial road to Yerevan | Distance | Source |
|---|---|---|---|---|
| Abovyan | 46,434 (est. 47,546 in 2024) | **M4 / H1** (NE) | ~16 km | [31] |
| Vagharshapat (Ejmiatsin) | 44,837 | M5 (W) | 18–20 km | [31] |
| Masis | 20,081 | M2 (S) | 9–16 km (article inconsistent) | [31] |
| Ashtarak | 15,686 | Ashtarak hwy / M1 (NW) | 13–20 km (article inconsistent) | [31] |

- The four suburbs together hold ≈ **127k people**, spread over **four different radial roads** [ESTIMATE: sum]. The M4 corridor captures only Abovyan plus the smaller towns beyond (Charentsavan, Hrazdan; B1).
- A drive-thru strategy built on **commuter** traffic favours sites on **Yerevan's own exit arterials**, where several flows merge, over a single highway [ASSUMPTION].
- No census commuting matrix was found (GAP).

#### 3.3.4 Weekend and leisure trips (Sevan, Tsaghkadzor, Dilijan)

- B1 finds **no traffic count on the M4 since 2008**. It models summer-weekend peaks on Sevan-dominated segments at 1.5–2.5× a summer weekday, and Jan–Feb at 0.6–0.8× AADT. All of these are ASSUMPTIONS anchored only on police statements that summer-weekend volumes "rise significantly" (B1).
- The Coffee House Drive-Thru sits on the **Sevan-bound** side. Yandex shows it "usually busy around 13:00", a **midday** rather than a commute peak, and it stays open until midnight (A2/A3). That pattern fits a mixed leisure + commuter flow [ASSUMPTION].
- **Seasonality warning from an analog.** McDonald's opened a **seasonal outlet in Budva (Montenegro) in 2004 and closed it in 2007** for "the lack of interest for a permanent location" [REPORTED: 14]. A site sized on 10–14 summer weekends (B1) carries the same risk.

#### 3.3.5 Demand for convenience

- **To-go coffee is already mainstream.** Coffee House grew to **57 claimed / 52 listed branches** of takeaway espresso. Cofix (fixed-price, Israel) entered in Feb 2024, and 38 Yerevan cafés are tagged takeaway-only in OSM (A2).
- **Eating out has grown.** Food & beverage service turnover roughly **tripled in nominal terms in 2020–24**, flattened in 2025 (+3.1%) and rebounded in 2026 (A3, Armstat).
- **Delivery consolidated.** Menu.am moved onto Yandex Eats in Nov 2024 and Glovo is active (A3). No order-volume statistics for Armenia were found (GAP).
- **Cashless readiness is high.** 87% of cards are NFC-enabled, and Apple Pay/Google Pay are live (A1). That supports app pre-order and fast lane payment.

### 3.4 Barriers

| Barrier | Evidence | Direction | Strength | Status |
|---|---|---|---|---|
| **Sit-down / social coffee ritual** | Coffee is a "staple of every meal", brewed in a jezve at home and in the office; ≈ 89% of green imports are robusta for jezve coffee (A2). Out-of-home sit-down habit is real: 59% visited a restaurant or fast-food place in 6 months (CB 2019) [10] | Negative for *coffee* drive-thru (the home ritual is not what a lane sells); positive for out-of-home spending generally | Medium | VERIFIED / REPORTED |
| **Price sensitivity** | 31% of households short of money for food at least once in 12 months (CB 2024) [12]; food away from home 2.8% of consumption (ILCS 2024); average wage AMD 312k (Jan–Aug 2026; A1); mass to-go coffee 800–1,000 AMD vs premium 1,600–1,950 (A2) | Negative for a US-priced ticket | **High** | VERIFIED |
| **"Takeaway = lower quality" perception** | No survey found. Indirect: the market leader in to-go (Coffee House) is youth/mass-positioned and launched a separate premium sub-brand, FEIN, in Sept 2025 (A2), consistent with to-go being read as mass | Negative for a *premium* drive-thru positioning | Medium (unproven) | ASSUMPTION on REPORTED facts |
| **Winter on the highway** | Sevan January mean max −2.8°C, min −13.0°C; record low −26.2°C (Feb) [27]; Hrazdan January mean −6.9°C [28]; snow at Abovyan/Sevan in Dec 2025, roads kept open (B1) | Neutral to positive for *use* (customers stay in the car; drive-thrus operate in colder Astana, Karaganda and Pavlodar [32] and Russian drive pavilions exist [17]), negative for *volume* (fewer leisure trips) and *opex* (snow clearing, heated lane and menu board) | Medium | REPORTED + ASSUMPTION |
| **Road safety and queue spill-back** | Road deaths 13.6/100k (Armenia, 2021) vs 5.0 Poland, 6.7 Türkiye [30]. M4 runs at 90 km/h on dual carriageway with few median openings (B1). The incumbent's 20–60-min waits (A3) imply queues long enough to spill back | Negative for an open-highway pad (permit and liability risk); argues for stacking ≥ 8–10 cars off-carriageway | Medium–high | REPORTED + ASSUMPTION |
| **Low car access** | 42% of Yerevan households own a car [8]; taxi 28% of trips (A1) | Caps the addressable base; argues for walk-up + delivery + lane | High | VERIFIED |
| **No market education** | 0 OSM drive-thrus; no McDonald's [14][32]; only 1 known drive-thru (A3) | First-mover cost; slower ramp | Medium | VERIFIED (OSM) / REPORTED |
| **Supply-chain / geopolitics** | McDonald's Kazakhstan exit over Russian patty supply [14][15]; Russia–Armenia trade bans 2026 (A1) | Risk for imported-ingredient "American" menus | Medium | REPORTED |

### 3.5 Lessons from failed or struggling concepts

| Case | What happened | Stated or likely cause | Lesson for Armenia | Status |
|---|---|---|---|---|
| **Starbucks Israel** (2001–03) | Opened 6 of 80 planned stores; closed all in Apr 2003 after ≈ $6M losses | "On-going operational challenges", "difficult business environment"; widely attributed to strong local espresso culture [24] | A US coffee brand without local adaptation struggles against an entrenched local café culture | REPORTED |
| **Starbucks Australia** (2008) | Closed 61 of 84 stores; sold the rest in 2014 | "Failed to truly understand Australia's café culture" (Univ. of Sydney expert) [24] | Same: premium price + generic menu vs local café habits | REPORTED |
| **McDonald's Bolivia** (1997–2002) | 8 outlets closed | "Poor sales and high prices" [14] | An imported price point above local norms fails even with a famous brand | REPORTED |
| **McDonald's Montenegro** (2004–07) | Seasonal Budva outlet closed | "Lack of interest for a permanent location" [14] | Seasonal-tourist-only demand does not sustain a unit (relevant to Sevan) | REPORTED |
| **McDonald's Kazakhstan** (2016–23) | 24 outlets; exit Jan 2023 | Patty imports from Russia blocked [14][15] | Do not depend on a single cross-border supply route | REPORTED |
| **Dunkin' Poland / Sweden / South Africa / Canada** | Poland: re-entered Dec 2015, 5 stores by 2018, withdrew Aug 2018. Sweden bankrupt Jul 2018. South Africa closed by Feb 2019. Canada exit Sept 2018 | Poor performance; in Canada, competition from Tim Hortons [25] | Even US coffee/donut brands fail where a local champion owns the habit (here: Coffee House) | REPORTED |
| **Starbucks Russia** (2007–22) | 130 licensed stores closed; rebranded Stars Coffee | Geopolitical exit [24] | Brand-licence risk; the format survived under a local brand | REPORTED |
| **Coffee House Drive-Thru, M4** (2024–) | Still operating; 20–60-min waits and order errors in summer 2026 | Bar throughput, batching, app-order priority (A3) | Throughput and accuracy, not lane demand, are the local failure mode | REPORTED (A3) |

**Not found (GAP):** documented closures of drive-thru coffee kiosks in Russia, Ukraine or the Caucasus, and of highway drive-thrus in Georgia. These are the most directly relevant "failure" cases and should be researched (Section 5).

### 3.6 Which segment adopts first

| Segment | Size indicator | Evidence of fit | Ticket / frequency | First-adopter rank |
|---|---|---|---|---|
| **Car commuters 20–40 on Yerevan exit arterials** (NE: Nor Nork/Avan/Kanaker; W: Ejmiatsin road; S: Masis road) | Yerevan HH car 42% [8]; NE exit districts 272.6k residents (A1); Numbeo car commute 40% (n = 47) [1] | Coffee House regular: "I drop in almost every day" (A3); Coffee House to-go network shows the habit (A2); Georgian drive-thrus sit on exactly these arterials [32] | Low–mid ticket (coffee + pastry), high frequency | **1** |
| **Weekend leisure drivers** (Sevan, Tsaghkadzor, Dilijan) | Summer-weekend multipliers 1.5–2.5× (B1, ASSUMPTION) | Coffee House busy at 13:00 on the Sevan-bound side (A2/A3) | High ticket (multiple people, food), strongly seasonal | **2** |
| **Professional drivers** (taxi/ride-hail, delivery couriers, truckers) | Taxi 28.1% of passenger trips (A1) | Time-poor, in the car all day [ASSUMPTION] | Low ticket, very high frequency, price-sensitive | **3** |
| **Relocants, diaspora, tourists** | Net Russian entries +65,750 Jan–Aug 2026 (A1); Bagratashen entries 927,780 Jan–Aug 2026 (A1) | Familiar with drive formats from Russia, the US, the UAE or Georgia [ASSUMPTION] | Mid–high ticket, volatile | **4** (upside, not base) |
| **Families with children on day trips** | — | Drive-thru avoids unloading children; Georgian drive-thrus are food-led QSR [32] | High ticket if hot food is offered | Joint 2–3 if the menu includes food |

---

## 4. Implications for the drive-thru concept (critical)

1. **Do not base the case on "Armenians will adopt American drive-thru culture".**
   - The analog with the same income (Georgia) built ~21 drive-thrus over two decades of McDonald's presence, **all urban**, inside QSR restaurants with walk-in trade [32].
   - In Kazakhstan all 14 tagged drive-thrus are urban QSR, and none sells coffee [32]. In Ukraine, 63 of 88 tagged drive-thrus are McDonald's or KFC, and the coffee drives are about 10 small local outlets [32].
   - There is no evidence anywhere in the region of a **coffee-only, drive-only highway unit** succeeding at scale.
   - The three formats with regional scale evidence are **roadside drive kiosks** (Coffee Like, Russia: franchisor claims), **fuel-station cafés** (WOG/OKKO, Ukraine) and **forecourt coffee-and-donut kiosks** (Dunkin', 27 of 72 Georgian outlets next to fuel stations, mostly Wissol) [17][19][22][32].
2. **Location logic should flip from "highway" to "arterial/exit + fuel".** In Georgia the lanes sit on city arterials and exits (Kakheti Hwy, Gelovani Ave, Aghmashenebeli Alley) [32]. Armenia's equivalents are the **Yerevan ends** of the M4/H1 (Avan–Nor Nork), M5 (Ejmiatsin road), M2 (Masis/airport) and Ashtarak road. There commuter, urban and leisure flows combine in both directions (A1/B1) [ASSUMPTION].
3. **A walk-up window and some parking are not optional.** Only 42% of Yerevan households have a car [8], taxis carry 28% of trips (A1) and A2/A3 show strong walk-up to-go demand. A drive-only design throws away most of the addressable market [ASSUMPTION]. Coffee Like's portfolio supports this: its walk-up formats still earn RUB 0.57–1.0M/month [17].
4. **Price has to be Armenian, not American.** The Russian drive-kiosk check (≈ AMD 1,670) already equals Armenia's premium tier, and 31% of households report food-money shortfalls [12][17]. Base-case coffee pricing near **AMD 900–1,300** with premium upsell (iced or signature drinks, food bundles) is consistent with the evidence. A Starbucks-level AMD 2,000+ base is not (A2) [ASSUMPTION].
5. **Food is what converts a lane into a meal-level ticket.** 20 of 21 Georgian drive-thrus are burger/sandwich QSRs. The one coffee brand (Dunkin', Batumi) shares a site with Wendy's and Subway [32]. In Ukraine the highest non-fuel conversion came from a multi-concept food hall [20]. A coffee-only lane is a low-ticket business. Hot savoury items (A4) are needed to reach AMD 3,000+ per car [ASSUMPTION].
6. **Throughput is the make-or-break.** The incumbent's main weakness is 20–60-minute waits (A3). Design for ≥ 8–10 cars of off-road stacking, a pre-order lane, two production lines at peak, and a published service-time target (e.g., ≤ 4 minutes order-to-window, against a US average of ~4 minutes [16]) [ASSUMPTION].
7. **Seasonality must be modelled explicitly** for any Sevan-road unit. Use B1's multipliers, test a winter-trough scenario at 0.6× AADT, and require that year-round commuter demand alone covers fixed costs. The Montenegro case [14] is the cautionary analog [ASSUMPTION].
8. **The "American" brand promise is a liability under competition.** Starbucks is in Georgia since July 2026 and held talks in Armenia in Oct 2025 (A2). Wendy's plans 20 Armenian units by 2030 (A3). Imported concepts that did not localise failed (Starbucks Israel and Australia, Dunkin' Poland) [24][25]. Position on **speed + local taste + car convenience**, with American *service standards*, not American *identity* [ASSUMPTION].
9. **Disconfirming evidence to keep in view.**
   - Yerevan's low congestion index (104) and short car commutes [1] weaken the time-saving argument.
   - Armenia's international-QSR density is among the lowest of the comparators: ≈ 6 per million, similar to Azerbaijan's ≈ 5, against Georgia's ≈ 38 [32][13]. That may reflect structural unattractiveness for franchisors (market size, supply routes), not only white space [ASSUMPTION].
   - No survey shows willingness to use a drive-thru.
   - The one local drive-thru has 17 written reviews and 123 ratings after ~2 years (A3). That may indicate modest volumes [ASSUMPTION; review counts are a weak proxy].
10. **Upside evidence to keep in view.**
    - The incumbent is busy enough to queue (A3).
    - Drive kiosks are the best-performing format (franchisor claim) at Coffee Like, which INFOLine ranks as the leader in Russian grab-and-go coffee (cited by ru.wikipedia) [17][18].
    - Fuel-station coffee reached ~180 cups/day per point in Ukraine [19].
    - Yerevan's car-owning share is *higher* than Tbilisi's, where drive-thrus work [8][9].

**Evidence-weighted assessment.**

| Format | Supporting evidence | Opposing evidence | Subjective probability of hitting base-case unit economics | Confidence |
|---|---|---|---|---|
| Standalone premium drive-only unit on open M4 highway | Coffee House queues; leisure traffic | No regional precedent; seasonality; incumbent 1 km away; fuel cafés; safety/stacking; price | **≈ 25–35%** | Medium-low |
| Drive-thru-led hybrid (lane + walk-up + parking/seats) on a Yerevan exit arterial | Georgia urban-arterial pattern; Coffee Like drive-pavilion uplift; to-go habit; higher car ownership than Tbilisi | Low congestion; land/permit cost; Wendy's/KFC could add lanes | **≈ 50–60%** | Medium-low |
| Fuel-station hybrid (café + lane at a CNG/fuel forecourt on M4 or exits) | Ukraine WOG/OKKO scale; Georgia's Dunkin'-at-Wissol pattern (27/72 outlets at forecourts); CNG refuelling dwell (A3); traffic already stopping | Partner dependence; fuel chains building their own cafés (Max Cafe, Flash Express; A3) | **≈ 45–55%** | Medium-low |

*Probabilities are ASSUMPTIONS (analyst judgment) that synthesise the evidence above. They are meant to rank options, not to be used as model inputs.*

---

## 5. Data gaps and how to verify them

| Gap | Why it matters | How to verify |
|---|---|---|
| **Drive-thru share of sales** for Vkusno i tochka, Rostic's, Burger King Russia; McDonald's Georgia/Azerbaijan; KFC Kazakhstan; McDonald's/KFC/BK Poland (AmRest); TAB Gıda (BK Türkiye); Americana (UAE) | Calibrates the drive/walk-in split in a hybrid | (1) Annual reports: AmRest (amrest.eu, Investors), TAB Gıda (KAP disclosures), Americana (ADX/Tadawul filings). (2) Russian business press (RBC, Kommersant, Vedomosti) for "доля драйва" / "доля продаж через драйв". (3) Interviews with the McDonald's Georgia franchisee and the Wendy's Georgia operator (wendys.ge names "W-Geo Restaurants LTD" as copyright holder). Re-run in a session with search budget. |
| **Georgia drive-thru unit volumes and dayparts** | Closest analog for volumes | Field visit to 3 Tbilisi McDonald's/Wendy's drive-thrus (Kakheti Hwy, Gelovani Ave, Aghmashenebeli Alley): car counts per 15 min, 07:00–24:00, one weekday and one weekend day. Google/Yandex "popular times" capture. |
| **Russia OSM drive-thru stock; brand totals for KZ/UA/TR/PL/RU/AE** (queries timed out). Türkiye and UAE tags are clearly incomplete (McDonald's ≤ 4% tagged) | Cross-country density benchmark | Re-run the Overpass queries (documented in source [32]) off-peak, or download Geofabrik country extracts and run `osmium tags-filter <file> nwr/drive_through=yes`. For real stocks, use company store locators (McDonald's Poland/Türkiye/UAE restaurant finders filter by "McDrive/Drive-thru") and count. |
| **Documented failures of drive-thru coffee kiosks** (Russia, Ukraine, Caucasus) | Direct failure base rate | Search Russian/Ukrainian press for "закрылся драйв кофе", "кав'ярня drive закрилась", "автокофейня банкротство"; check Coffee Like/Coffee Moose franchisee closure rates (rusprofile.ru legal-entity liquidations). |
| **Willingness to use a drive-thru; takeaway quality perception** | Core cultural question, currently unmeasured | Commission a survey (n ≥ 600; Yerevan + Kotayk; quotas by car ownership and age) with CRRC-Armenia or MPG. Include stated drive-thru use, acceptable wait, price ladder (Van Westendorp) and perception of to-go vs sit-down quality. Add 2 focus groups (car commuters; weekend Sevan drivers). |
| **Central-Yerevan parking difficulty** (paid zones, tariffs, enforcement, space counts) | Drives the time-saving value proposition | Yerevan Municipality transport department; the paid-parking operator's tariff sheet; fieldwork: time-to-park counts at 10 central blocks at 08:30 and 18:30. |
| **Census commuting flows** (suburb → Yerevan) | Sizes the commuter segment by corridor | Armstat 2022 census tables on place of work / commuting (request special tabulation); mobile-operator origin-destination data (Team/Viva/Ucom) if purchasable. |
| **M4 and exit-road traffic counts and seasonality** | Volume driver | See B1 §5 fieldwork protocol (ATC counters, summer and winter, both carriageways). |
| **Dunkin' Georgia – Wissol relationship and forecourt unit economics** | Direct Caucasus analog for a fuel-station hybrid | Wissol Group / Dunkin' Georgia press materials; Georgian business press (bm.ge, forbes.ge); store visits at 3 Wissol-Dunkin' sites (transactions/hour, ticket). |
| **Sevan/Tsaghkadzor/Dilijan visitor volumes and weekend car flows** | Sizes the leisure segment | Tourism Committee of Armenia; Sevan National Park beach-entry and parking data; Tsaghkadzor ropeway ticket counts; police summer-operation reports (B1 §5). |
| **Whether Wendy's/KFC Armenia plan drive lanes** | Competitive timing in the suburbs | Ask Wen Restaurant and Derjava directly; watch Yerevan urban-planning permit filings. |
| **Delivery-app order volumes in Armenia** | Convenience-demand trend | Yandex Eats / Glovo press offices; SRC turnover for courier NACE codes. |
| **Coffee House Drive-Thru volumes** | Only local proof point | 5-day observation (A2/A3 protocol), summer and winter. |
| **Road-safety requirements for queue stacking** on national roads | Permitting and liability | Ministry of Territorial Administration and Infrastructure road-access rules; Road Police; compare with the A3/B1 site list. |

---

## 6. Sources

Accessed 10 Oct 2026 unless stated.

1. Numbeo, Traffic in Yerevan (last update 28 Nov 2024; 47 contributors). https://www.numbeo.com/traffic/in/Yerevan
2. Numbeo, Traffic in Tbilisi (15 May 2026; 82). https://www.numbeo.com/traffic/in/Tbilisi
3. Numbeo, Traffic in Almaty (4 Aug 2026; 63). https://www.numbeo.com/traffic/in/Almaty
4. Numbeo, Traffic in Baku (4 Jan 2026; 63). https://www.numbeo.com/traffic/in/Baku
5. Numbeo, Traffic in Warsaw (13 May 2026; 252). https://www.numbeo.com/traffic/in/Warsaw
6. Numbeo, Traffic in Dubai (17 Jun 2026; 346). https://www.numbeo.com/traffic/in/Dubai
7. Numbeo, Traffic in Moscow (4 Jun 2026; 675). https://www.numbeo.com/traffic/in/Moscow
8. CRRC, Caucasus Barometer 2024 Armenia (fieldwork 27 Jul–10 Oct 2024), OWNCARS and OWNCARS by settlement type. https://caucasusbarometer.org/en/cb2024am/OWNCARS/ ; https://caucasusbarometer.org/en/cb2024am/OWNCARS-by-SETTYPE/
9. CRRC, Caucasus Barometer 2024 Georgia (fieldwork 16 Apr–13 May 2024), OWNCARS and by settlement type. https://caucasusbarometer.org/en/cb2024ge/OWNCARS/ ; https://caucasusbarometer.org/en/cb2024ge/OWNCARS-by-SETTYPE/
10. CRRC, Caucasus Barometer 2019 Armenia (fieldwork 21 Feb–15 Mar 2020), ACTREST. https://caucasusbarometer.org/en/cb2019am/ACTREST/
11. CRRC, Caucasus Barometer 2019 Georgia (fieldwork 9 Oct–4 Nov 2019), ACTREST. https://caucasusbarometer.org/en/cb2019ge/ACTREST/
12. CRRC, Caucasus Barometer 2024 Armenia, NOMONFD. https://caucasusbarometer.org/en/cb2024am/NOMONFD/
13. World Bank, World Development Indicators API (NY.GDP.PCAP.CD, NY.GDP.PCAP.PP.CD, SP.POP.TOTL, SP.URB.TOTL.IN.ZS; last updated 8 Oct 2026). https://api.worldbank.org/v2/country/ARM;GEO;AZE;KAZ;RUS;UKR;TUR;POL;ARE;USA/indicator/NY.GDP.PCAP.CD?date=2023:2025&format=json
14. Wikipedia, "List of countries with McDonald's restaurants" (outlet counts per McDonald's corporate, 31 Dec 2025; former locations incl. Bolivia, Montenegro, Kazakhstan, Belarus, Russia). https://en.wikipedia.org/wiki/List_of_countries_with_McDonald%27s_restaurants
15. Wikipedia, "Vkusno i tochka" (EN). https://en.wikipedia.org/wiki/Vkusno_i_tochka
16. Wikipedia, "Drive-through" (McDonald's US ≈ 70%, citing Quartz 2017; QSR 2024 Drive-Thru Report timings; Russia walk-up windows). https://en.wikipedia.org/wiki/Drive-through
17. Coffee Like franchise site (format economics; "900+ coffee shops in Russia", 135+ cities). https://franchcoffeelike.ru/
18. Wikipedia (RU), "Coffee Like" (points 2014–2024; group revenue 2022–23; average revenue per point). https://ru.wikipedia.org/wiki/Coffee_Like
19. Mind.ua, "Кава від WOG: 7 років на ринку та 10 млн євро інвестицій у проєкт", 2 Oct 2020. https://mind.ua/news/20216521-kava-vid-wog-7-rokiv-na-rinku-ta-10-mln-evro-investicij-u-proekt
20. Forbes.ua, "Перший рік роботи найбільшого АЗК в Україні: очікування і реальність", 25 Nov 2024. https://forbes.ua/company/pershiy-rik-roboti-naybilshogo-azk-v-ukraini-ochikuvannya-i-realnist-25112024-24940
21. Wikipedia, "WOG (company)". https://en.wikipedia.org/wiki/WOG_(company)
22. Wikipedia, "OKKO". https://en.wikipedia.org/wiki/OKKO
23. Wikipedia (UK), "WOG". https://uk.wikipedia.org/wiki/WOG
24. Wikipedia, "Starbucks" (Israel 2003; Australia 2008/2014; Kazakhstan; Azerbaijan; Russia 2022; 2020 US convenience pivot). https://en.wikipedia.org/wiki/Starbucks
25. Wikipedia, "Dunkin' Donuts" (international exits). https://en.wikipedia.org/wiki/Dunkin%27_Donuts
26. Wikipedia, "Dutch Bros". https://en.wikipedia.org/wiki/Dutch_Bros
27. Wikipedia, "Sevan (town)" (climate table, NCEI/WMO 1991–2020; population). https://en.wikipedia.org/wiki/Sevan_(town)
28. Wikipedia, "Hrazdan" (climate table, NOAA). https://en.wikipedia.org/wiki/Hrazdan
29. Wikipedia, "Yerevan" (climate 1991–2020; Transportation section: buses, e-ticketing, minibuses). https://en.wikipedia.org/wiki/Yerevan
30. Wikipedia, "List of countries by traffic-related death rate" (WHO estimates). https://en.wikipedia.org/wiki/List_of_countries_by_traffic-related_death_rate
31. Wikipedia: "Abovyan" https://en.wikipedia.org/wiki/Abovyan ; "Vagharshapat" https://en.wikipedia.org/wiki/Vagharshapat ; "Masis (town)" https://en.wikipedia.org/wiki/Masis_(town) ; "Ashtarak" https://en.wikipedia.org/wiki/Ashtarak (2022 census figures).
32. OpenStreetMap contributors, via Overpass API (mirror maps.mail.ru/osm/tools/overpass), queries run 10 Oct 2026 (OSM base timestamps: AM 11:04, GE 11:00, AZ 11:06, KZ 11:08, UA and AE 11:14, TR 11:18, PL 11:24 UTC; Georgian Dunkin'–fuel proximity 11:14–11:16 UTC; RU timed out). The extracted POI lists are saved in `research/data/A5-osm-drivethru.csv`. Queries: all `amenity=fast_food|cafe|restaurant` with `drive_through=yes` per country (ISO3166-1 area); all outlets with `brand:wikidata` ∈ {Q38076 McDonald's, Q37158 Starbucks, Q524757 KFC, Q177054 Burger King, Q550258 Wendy's, Q847743 Dunkin', Q608845 Costa, Q175106 Tim Hortons, Q1585448 Hardee's}; major roads within 120 m of each Georgian drive-thru. ODbL. OSM coverage is incomplete and counts are lower bounds.
33. Sibling workstreams: `research/A1-macro-consumer.md`, `A2-coffee-market.md`, `A3-qsr-fuel-convenience.md`, `A4-food-preferences.md`, `B1-m4-traffic.md` (each with its own sources).
34. Wikipedia (RU), "Rostic's". https://ru.wikipedia.org/wiki/Rostic’s
35. Wikipedia (PL), "McDonald’s" (section on Poland: 435 outlets Dec 2019; 550 Apr 2024; 2024 financials). https://pl.wikipedia.org/wiki/McDonald%E2%80%99s
36. Wikipedia (RU), "Вкусно — и точка" (830 points in 62 regions, Nov 2022; 2022 loss, 2023 profit). https://ru.wikipedia.org/wiki/Вкусно_—_и_точка
