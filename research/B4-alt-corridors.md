# B4 — Alternative corridors and locations that could beat the M-4 for a first drive-thru

*Prepared 2026-10-10 for the premium drive-thru feasibility study (Armenia). Workstream B4 tests the founder's M-4 (Yerevan–Sevan) idea against the other road corridors out of Yerevan, Yerevan's own arterials, the satellite towns and the two second-tier cities. The revenue driver is unchanged: vehicles passing × capture rate × average ticket.*

**Status tags.** **VERIFIED**: I opened the primary or official source myself (URL in §6). **REPORTED**: a credible secondary source, such as a listing, OpenStreetMap or a Wikipedia page citing press reports (URL in §6). **ESTIMATE**: my own calculation, with formula and inputs shown. **ASSUMPTION**: my judgement, with the basis explained.

**Search note.** The shared web-search quota for this workflow was already used up when this task started; every web-search call was refused. All evidence below therefore comes from:
- primary documents I fetched directly: ADB project documents, Armstat bulletins and workbooks, Coffee House's branch page, and listing sites;
- OpenStreetMap extracts via the Overpass API;
- the Kontur population grid;
- sibling workstreams A1, A2 and B1 in this repository.

Items that a web search would normally have found are listed as gaps in §5. These include news on recent drive-thru openings, Yerevan municipal traffic data, list.am lease listings and Garni/Geghard visitor counts after 2019.

*Fact-check (10 Oct 2026): an adversarial fact-check re-opened the primary sources and ran the web searches that were unavailable to this workstream. Almost every transcribed number reproduces. The material corrections concern how counts are applied to sites: the Isakov count location, the M-2 and M-1 growth bases, and the resulting ranking. Corrections are marked inline as "Fact-check correction" and logged in §7.*

---

## 1. Executive summary

1. **Published traffic counts exist for the other corridors out of Yerevan, and they are newer than anything found for the M-4.** The M-4's last published count is from 2008 (B1). By contrast, ADB documents give:
   - **M-5** (west of the Zvartnots airport junction, km 12): **34,805 veh/day two-way (2021)**, +9 %/yr over 2016–21.
   - **M-2** (Artashat highway at the Yerevan edge, km 9.38): **37,831 (2018)**.
   - **M-1** (km 20.7, beyond Ashtarak, between the M-3 junction at km 18.8 and km 23.2): **18,635 (2017)**, then +12 %/yr over 2018–21 for "M1 just north of the city" (possibly a different counter).
   - Yerevan Road Police 24-h counts (May 2020): **Admiral Isakov Ave 40,052** (section AB only: the 1.4 km between the Monte Melkonian junction and Victory Bridge) and **Arshakunyats Ave 40,430**. ADB's 2023 base years of 44,100 and 44,500 are ADB adjustments (the COVID-period May 2020 count +10 %), not measurements.

   (All VERIFIED [1][2][3].) My 2025 estimates are:
   - M-2 edge ≈ **49,100** (46.5–51.5k)
   - Isakov section AB (east of Monte Melkonian) ≈ **46,800**
   - Arshakunyats ≈ **47,200**
   - M-5 west of the airport ≈ **43,100** (39.2–47.4k)
   - M-1 ≈ **25,200–33,100**, both ends weighted equally

   (ESTIMATE, §3.2.) The M-2, Isakov AB, Arshakunyats and M-5 figures match or exceed B1's base estimate for the M-4 Yerevan edge (≈42,000); the M-1 is lower. All five are **1.5–2.9× B1's Hrazdan–Sevan estimate (≈17,000)**.

   *Fact-check correction: the M-2 base was 51.5k (4.5 %/yr). That is above this file's own evidence: ADB reports 3.8 %/yr for 2014–18, and ADB's 2025 forecast is 49,600. It is now 37,831 × 1.038^7 ≈ 49.1k. The M-1 base was 33.1k, which is 31 % above ADB's own 2025 re-evaluation forecast (25,200) for km 11.8–23.2. The M-1 is now shown as a 25.2–33.1k range. The Isakov count does not cover the recommended site west of Monte Melkonian (see item 2).*
2. **Exposure test: urban-edge sites need about a third of the M-4 leisure segment's capture rate.** To reach 120 drive-thru transactions/day:
   - M-2 edge, Arshakunyats and M-5 sites need a capture of **0.53–0.57 %** of same-side light vehicles. The M-1 exit needs **0.75–0.98 %**.
   - The M-4 needs **0.70 %** at the Yerevan edge, **1.08 %** at Abovyan–Charentsavan and **1.72 %** at Hrazdan–Sevan. The model's current placeholder needs 1.36 %.

   (ESTIMATE, §3.7.) Caveat: an urban commuter may convert less often than a leisure driver, so the capture rates themselves are not interchangeable. Field stop-rate counts are needed (§5).

   *Fact-check correction: the earlier best figure was 0.49 % for "Isakov inbound (Malatia)". That figure applies only to Isakov section AB, east of the Monte Melkonian junction. This is the section the file itself says to avoid, and it loses 36 % of its traffic once the link road opens. The recommended western Isakov site (U05) is about 2.1 km west of the junction, outside the counted section. Its traffic and inbound split are unmeasured. Its documented floor is the M-5 km-12 series: ≈21,000 same-side light vehicles, 0.57 % capture. The M-2 now needs 0.53 % (2025 base 49.1k, was 51.5k). The M-1 needs 0.75–0.98 % (25.2–33.1k).*
3. **Urban demand is measurably less seasonal.**
   - National accommodation and food-service turnover in 2025 ran from **0.73× the monthly average (Feb) to 1.18× (Aug)**, a peak-to-trough ratio of 1.62 and a coefficient of variation of 0.13 (ESTIMATE from VERIFIED Armstat monthly data).
   - The model's current M-4 placeholder index runs from 0.66 to 1.46 (ratio 2.21, CV 0.25). B1 assumes 0.6–1.6 for the Sevan segments.
   - ADB's 2014 hourly counts on the western arterial show the lowest day at **93 % of the weekly average**, with flat traffic from 08:00 to 19:00 (VERIFIED [1]).
   - Long-distance and tourist flows are much more seasonal. In 2026, June–August monthly person-crossings were **1.47× the January–May average at Zvartnots, 1.54× at Bavra (M-1 north) and 1.69× at Bagratashen**. In older data (≈2005–09), the M-1 counter ran +19.7 % above AADT in July (VERIFIED/ESTIMATE). *Fact-check note: the July factor and the 2014 hourly profile are old (≈2005–09 and 2014). They are not current measurements.*
4. **Zvartnots is growing, but the airport is a modifier, not the main draw.**
   - Passengers: 5.33 M (2023), 5.25 M (2024), **5.62 M (2025, +7 %)** (REPORTED [7]). Armstat's air-passenger series shows **+12.1 % y/y in Jan–Aug 2026** (VERIFIED [5]).
   - Airport road movements: about **12–17k vehicle movements/day** (ESTIMATE), which is about a third of M-5 traffic.
   - Coffee House (24/7) and Paul already trade inside the terminal (VERIFIED [10] / REPORTED OSM).
   - Value comes from early-morning departures and from drivers waiting to collect arrivals, layered on top of the Ejmiatsin/Armavir commuter stream.
5. **Satellite-town growth is real but small. Kotayk's building boom is still mostly (≈84 %) household-built, but developer building is rising.**
   - Population change, 1 Jul 2025 → 1 Jul 2026: Masis +1.7 %, Ejmiatsin +1.5 %, Abovyan +1.4 %, Kotayk marz +1.4 %, Yerevan +0.5 %. Gyumri (−0.3 %) and Vanadzor (−0.4 %) are shrinking (VERIFIED [8]).
   - Floor area of new housing in Kotayk rose **5.4× between 2020 and 2024 (40,931 → 222,431 m²)**. 2024 was +43 % on 2023 (155,443 m²) and 15.2 % of the national 1,457,262 m² (18.2 % in 2023). Households financed 83.9 % of it in 2024 (186,528 m²), down from 97.7 % in 2023, because organisation-financed space rose 10× to 35,903 m² (VERIFIED [11]: Armstat handbook copy, public URL not located; national totals match [14]).

   *Fact-check correction: the earlier text read "4.4× from 2019 to 2023 (35,112 → 155,443 m²), 98 % household-financed". That was stale, and its source had no URL. The 2019 base of 35,112 m² is not in the 2025 handbook and remains unverified.*
   - No satellite town has the 3 km catchment of an inner-Yerevan arterial. Kontur puts Abovyan at ≈52k and Masis/Ejmiatsin at ≈22–38k, against 150–210k for Arshakunyats, Isakov, Halabyan or Tbilisian (ESTIMATE, Kontur 2023 grid).
6. **Gyumri and Vanadzor are not first-site material.**
   - Shirak has the country's **highest poverty rate (43.0 %, 2024)** and its average wage is 169,392 AMD, 47 % of Yerevan's (VERIFIED [12][13]).
   - Both cities are shrinking, and the M-1 traffic uplift ADB expected from Gyumri never happened (ADB 2020: "Gyumri's economy has not developed as hoped" [3]).
   - Coffee House (2 branches each) is already in both centres, and KFC is in Vanadzor. *Fact-check correction: the earlier text said "KFC in both centres". KFC's official list (sibling A3) is 12 Yerevan + Homplex Hyper Mall + Vanadzor. The Gyumri KFC appears only in OSM and is likely closed.*
7. **The M-2 south corridor has the highest measured interurban volume and the most white space, but carries specific risks.** On a 2025 basis it is level with the urban Isakov and Arshakunyats counts, not above them (≈22,600 same-side light vehicles; 0.53 % capture). *Fact-check correction: the 2025 base was 51.5k at 4.5 %/yr. It is now ≈49.1k at ADB's reported 3.8 %/yr.*
   - Zero cafés within 1 km of the Yerevan-edge site, and the nearest Coffee House is 4.6 km away (OSM/website).
   - Ararat marz is relatively affluent: wage 234,735 AMD, poverty 15.7 %.
   - But 8 % of traffic is trucks (2018), and **Meghri (Iran) border crossings fell 32 % y/y in Jan–Aug 2026** (ESTIMATE from VERIFIED [6]). The long-distance component is volatile; commuter traffic from Masis and Artashat is the stable base.
8. **A road project now under construction will move Isakov's volume.** ADB's Admiral Isakov–Arshakunyats link (opening assumed 2028) is forecast to cut Isakov traffic between Monte Melkonian junction and Victory Bridge by **36 % (44,100 → 28,198)** and to raise Arshakunyats north of the link by **15 % (44,500 → 51,100)** (VERIFIED [1]). Any Isakov site should therefore sit **west** of Monte Melkonian (Malatia → airport), where M-5 through-traffic is unaffected. But no count exists for that western stretch: all Isakov counts are from the section east of the junction.
   - Status: the civil works contract for the link and Komitas Park was signed on **1 May 2026**, and the supervision contract on 8 May 2026. The loan closes on 31 Mar 2028 (VERIFIED [22]).
   - Risks: construction disruption on Isakov and Arshakunyats near the junctions during 2026–28, and a possible slip past 2028.

   *Fact-check correction: the project status was listed as an unconfirmed gap. It is now confirmed from ADB's project data sheet (updated 30 Jul 2026). Note that 44,100 and 44,500 are ADB adjustments (the May 2020 count +10 %), not measurements.*
9. **Drive-thru white space is real, but Coffee House saturates the city centre.**
   - OSM shows **no food outlet tagged as a drive-through in Armenia**. The only known food drive-thru is Coffee House's M-4 unit at Ptghni (A2).
   - A **non-food "Onex Drive Thru"** (parcel pickup, with optional refuelling) was announced in 2026 at Admiral Isakov 7/7, next to a Flash station (REPORTED [23], search snippet only). So a Flash forecourt on Isakov already has a drive-thru partner.
   - Coffee House lists 52 branches, 51 of them with coordinates. 42 are in the Yerevan region, including the airport. The rest are Ejmiatsin ×2, Armavir, Abovyan, Gyumri ×2 and Vanadzor ×2 (VERIFIED [10]).
   - The corridor edges (M-2 south, M-1 north-west, M-5 west of Malatia) have 0–2 cafés within 1 km. Fuel stations line them densely (20–29 within 200 m of each corridor), which favours a **fuel-station hybrid**. Check whether Flash pads on Isakov are still free before assuming one there.

   *Fact-check correction: the earlier text said "51 geocoded branches, about 40 in Yerevan". The Onex item was not known when B4 was written. The food drive-thru white space still stands: English and Russian-language searches found no food drive-thru on these corridors.*
10. **Land costs appear to favour the edges, but the evidence is weak.** Asking prices from listings dated Mar–Oct 2026 (12 listings, mostly residential plots; REPORTED [16][17]; indicative only):
    - **$66–150/m²** for Kotayk suburban plots (Abovyan, Dzoraghbyur, Ptghni, Arinj, Hrazdan)
    - **$160–350/m²** at the Yerevan periphery (Avan, Ajapnyak, Nork-Marash)
    - **$380/m²** for commercial frontage in Erebuni
    - **≈$1,000/m²** in Arabkir

    A 2,000 m² drive-thru pad therefore costs ≈$0.13–0.30 M in Kotayk, $0.3–0.7 M at the city edge and $2 M+ in the inner city (ESTIMATE).

    *Fact-check correction (downgraded to indicative): not all listings are from Sep–Oct 2026. Ptghni was listed 30 Apr, the 10,000 m² Ajapnyak plot was edited 1 Apr, and Avan Duryan was added 26 Mar 2026. None of the 12 listings is on the four top-ranked corridors (Shengavit, Noragavit/Ayntap, Malatia/Parakar, Davtashen), and most are residential, not commercial road frontage. Land cost for the shortlisted sites is therefore unevidenced.*
11. **Ranked non-M-4 shortlist** (weighted score out of 5, §3.9). The top four lie within 0.25 points. **Treat their order as undetermined until site-specific counts exist.**
    1. **Arshakunyats Ave, Shengavit, north of the future link** (4.00). Feasibility depends on finding a plot. Expect link-road construction near the junction in 2026–28.
    2. **M-2 Artashat highway at the southern city edge (Noragavit–Ayntap, km 9–13)** (3.90).
    3. **M-5 western approach**: Admiral Isakov Ave west of Monte Melkonian → Yerevan boundary → Zvartnots junction, inbound side, ideally a fuel-station hybrid (3.85). This stretch is uncounted.
    4. **M-1 Ashtarak highway / Davtashen–Homplex exit** (3.75).
    5. **Tbilisian highway (Kanaker-Zeytun → Avan/Arinj)** (3.60). This catches M-4 and Arinj commuters inside the city, without the highway's seasonality.

    For comparison: M-4 Yerevan edge 3.05; M-4 Hrazdan–Sevan 1.85; Garni road 1.55.

    *Fact-check correction: the M-5 western approach was ranked #1 (4.05) on a Data score of 5. That score rested on counts taken east of Monte Melkonian, not at the recommended site. With Data cut to 3 it scores 3.85 and drops to #3. The M-1's White-space score was cut from 5 to 4, because KFC and Coffee House both sit at Homplex Hyper Mall, about 1.1 km from the exit point. That takes the M-1 from 3.85 to 3.75. The investor should not rely on the former 0.49 % Isakov capture figure.*
12. **Verdict on the M-4 idea.** The evidence does not support a *tourist-highway* M-4 site as the **first** unit. Its volume is a third of the urban edges'. Its seasonal swing is wider: peak-to-trough ≈2.2 on the model's placeholder and up to ≈2.7 under B1's assumptions, against ≈1.6 for urban food-service demand, with roughly double the coefficient of variation. It also competes with the established Coffee House drive-thru. The M-4's only competitive stretch is its **Yerevan edge**, which is a commuter site like the other exits but has the weakest traffic data and an incumbent. A first unit on a **year-round Yerevan exit corridor or arterial** (Arshakunyats, M-2 south, M-5 west or M-1 north-west; order undetermined) carries less risk and costs less to prove. The Sevan leisure peak can be tested later with a seasonal or modular unit. **Before land is committed**, the shortlist must be validated with 2-season classified counts and stop-rate observation (§5).

---

## 2. Key data table

| # | Metric | Value | Period | Status | Source |
|---|---|---|---|---|---|
| 1 | Admiral Isakov Ave, 24-h Road Police count (section AB only: 1.4 km between Monte Melkonian jn and Victory Bridge) | **40,052** two-way: inbound 22,718 / outbound 17,334; cars+taxis 92.7 % two-way, 95.1 % inbound. *Fact-check correction: this section is east of the junction. The recommended western site (U05) is ≈2.1 km west of it and is not counted.* | May 2020 | VERIFIED | [1] Table 1 |
| 2 | Arshakunyats Ave, 24-h Road Police count | **40,430** two-way: 19,845 inbound / 20,585 outbound; cars+taxis 95.1 % | May 2020 | VERIFIED | [1] Table 1 |
| 3 | Monte Melkonian Ave, 24-h count | 25,100 two-way | May 2020 | VERIFIED | [1] Table 1 |
| 4 | ADB base year without link: Isakov (AB) / Arshakunyats (CD) | 44,100 / 44,500 veh/day. These are ADB adjustments (May 2020 police count +10 %), not measurements | 2023 | VERIFIED (ADB estimate) | [1] Table 4 |
| 5 | ADB with Isakov–Arshakunyats link (opening assumed 2028) | Isakov AB 28,198 (−36 %); Arshakunyats CD 51,100 (+15 %); new link 15,902. Civil works contract signed 1 May 2026; supervision contract 8 May 2026; loan closing 31 Mar 2028 (*Fact-check correction: status confirmed, gap closed*) | 2023 base; status 2026 | VERIFIED (ADB estimate; ADB project data sheet) | [1] Table 5; [22] |
| 6 | M-5 "western main road", km 12 (~2 km west of airport access jn), two-way | 22,841 / 25,044 / 31,481 / **34,805** (light vehicles 97.7 % in 2021) | 2016 / 2017 / 2020 / 2021 | VERIFIED (Roads Dept data via ADB) | [1] Table 2 |
| 7 | Traffic growth: M-5 west of city; M-1 north of city | +9 %/yr; +12 %/yr | 2016–21; 2018–21 | VERIFIED | [2] fn 7 |
| 8 | M-1 automatic counter, km 20.7 (beyond Ashtarak, between the M-3 jn at km 18.8 and km 23.2; not the Davtashen/Homplex city exit) | 12,384 / 16,697 / **18,635** (light 96.7 %) | 2009 / 2013 / 2017 | VERIFIED | [3] App. 9 Table 2, ¶13 |
| 9 | M-2 automatic counter, km 9.38 (Yerevan edge) | 23,406 / 33,504 / 32,386 / **37,831** (light 92.1 %) | 2009 / 2013 / 2017 / 2018 | VERIFIED | [3] App. 9 Table 2 |
| 10 | M-2 km 16 (beyond Masis jn) as share of km 9.38 | 10,297 = 44 % | 2009 | VERIFIED | [3] |
| 11 | ADB 2025 forecasts (made 2020): M-1 km 11.8–23.2; M-2 km 9.3–13.1; M-2 km 13.1–28.9 | 25,200; 49,600; 23,200 | forecast for 2025 | VERIFIED (as forecast) | [3] Table 5 |
| 12 | Hourly/daily profile, western main road | 08:00–19:00 = 70 % of daily traffic; peak hour 6 % of ADT; lowest day = 93 % of weekly mean | 2014 counts | VERIFIED | [1] §6 |
| 13 | M-1 July traffic vs AADT (counter km 20.7) | +19.7 % | ~2005–09 | VERIFIED | [4] Vol II §32 |
| 14 | **2025 AADT estimates**: M-2 edge; Arshakunyats; Isakov section AB (east of Monte Melkonian); M-5 W of airport; M-1 | 49.1k (46.5–51.5); 47.2k (44.6–51.6); 46.8k (45.9–48.6); 43.1k (39.2–47.4); 25.2–33.1k (no single base). *Fact-check correction: M-2 was 51.5k (46.5–56.9) and is now 37,831 × 1.038^7. M-1 was 33.1k (25.5–35.7) and is now ADB forecast 25.2k to 33.1k, weighted equally.* | 2025 | ESTIMATE | §3.2 |
| 15 | Zvartnots passengers | 5,330,308 / 5,248,348 / **5,615,789** (+7 %) | 2023 / 2024 / 2025 | REPORTED | [7] (cites Hetq, Alphanews) |
| 16 | Air passengers, Armenia (all airlines) | 5,393.1k / **5,755.7k** (+6.7 %) / 4,243.4k Jan–Aug (+12.1 % y/y) | 2024 / 2025 / 2026 | VERIFIED | [5] |
| 17 | Border records at Zvartnots (entries + exits) | 4,995,620 / 5,407,286 / 3,756,160 Jan–Aug (+5.5 % y/y) | 2024 / 2025 / 2026 | VERIFIED | [6] |
| 18 | Summer factor: Jun–Aug monthly average ÷ Jan–May monthly average (person crossings) | Zvartnots 1.47; Bavra (M-1 N) 1.54; Bagratashen 1.69; Gyumri airport 1.31; Meghri (M-2 S) 1.07 | 2026 | ESTIMATE from VERIFIED | [6] |
| 19 | Meghri (Iran) border crossings y/y | −32.4 % (527,194 → 356,614) | Jan–Aug 2025 → 2026 | ESTIMATE from VERIFIED | [6] |
| 20 | Accommodation & food-service turnover, monthly index (mean = 1) | Jan 0.78, Feb 0.73, Mar 0.91, Apr 0.99, May 1.01, Jun 1.06, Jul 1.17, Aug 1.18, Sep 1.06, Oct 1.06, Nov 0.99, Dec 1.05 | 2025 | ESTIMATE from VERIFIED | [9] |
| 21 | Population 1 Jul 2026 (k): Yerevan; Abovyan; Ejmiatsin; Masis; Artashat; Ashtarak; Charentsavan; Nor Hachn; Armavir; Gyumri; Vanadzor | 1,149.5; 51.5; 48.9; 23.7; 22.8; 17.8; 24.1; 10.5; 30.3; 114.0; 77.7 | 1 Jul 2026 | VERIFIED | [8] |
| 22 | Population change 1 Jul 2025 → 1 Jul 2026 | Masis +1.7 %; Ejmiatsin +1.5 %; Abovyan +1.4 %; Kotayk +1.4 %; Armavir marz +1.2 %; Ararat marz +1.0 %; Yerevan +0.5 %; Gyumri −0.3 %; Vanadzor −0.4 % | 2025–26 | ESTIMATE from VERIFIED | [8] |
| 23 | Yerevan districts (k): Malatia-Sebastia; Shengavit; Nor Nork; Kentron; Erebuni; Ajapnyak; Arabkir; Kanaker-Zeytun; Avan; Davtashen | 151.2; 140.7; 137.8; 133.6; 130.0; 123.6; 120.0; 75.8; 59.0; 52.7 | 1 Jul 2026 | VERIFIED | [8] |
| 24 | Average gross wage by marz of employer (AMD/month) | Yerevan 357,583; Ararat 234,735; Kotayk 208,210; Armavir 195,606; Lori 177,340; Aragatsotn 170,768; Shirak 169,392; Gegharkunik 158,949 | Q2 2026 | VERIFIED | [12] |
| 25 | Poverty rate (national line) | Yerevan 16.9 %; Aragatsotn 7.6 %; Ararat 15.7 %; Armavir 27.0 %; Kotayk 24.8 %; Lori 20.4 %; Shirak 43.0 %; Gegharkunik 27.6 %; Syunik 6.2 % (lowest); Tavush 39.9 %. Intervals are wide (e.g. Kotayk 95 % CI 13.9–35.8 %; Aragatsotn 4.0–11.3 %) | 2024 | VERIFIED | [13] Table 2.1 |
| 26 | Dwellings put in operation, Kotayk | 40,931 / 97,787 / 103,272 / 155,443 / **222,431 m²** (2020–24). 2024 = 15.2 % of national 1,457,262 m² (2023: 18.2 %). Household-financed 97.7 % (2023) → 83.9 % (2024). *Fact-check correction: was "35,112 → 155,443 m² (4.4×), 2019 → 2023"; the 2019 base is unverified.* | 2020–24 | VERIFIED (handbook copy; URL not located) | [11] |
| 27 | Dwellings put in operation, Armenia | 304,201 (2020) → 855,604 (2023) → 1,457,262 m² (2024); 10,389 apartments in 2024 | 2020–24 | VERIFIED | [14] |
| 28 | Construction volume growth | +24.7 % y/y (AMD 471.6 bn) | Jan–Aug 2026 | VERIFIED | [15] |
| 29 | Kontur population within 3 km / 5 km | Halabyan 206k/490k; Tbilisian S 183k/427k; Davtashen bridge 175k/446k; Arshakunyats 172k/416k; Isakov mid 154k/401k; M-2 edge 61k/181k; M-5 airport jn 27k/140k; Abovyan 52k/70k; Gyumri 76k/100k; M-4 CH drive-thru 24k/94k | grid c. 2020–23 | ESTIMATE | [18], §3.5 |
| 30 | Food drive-throughs tagged in OSM, Armenia | 0. KFC 13 and Burger King 4 outlets in the extract, all in malls or the centre. Non-food "Onex Drive Thru" (parcel pickup) announced 2026 at Admiral Isakov 7/7, next to Flash | OSM Jun–Oct 2026; Onex 2026 | REPORTED (OSM; incomplete); Onex: REPORTED (search snippet only) | [19]; [23] |
| 31 | Coffee House branches | 52 listed, 51 with coordinates (Victory Park has none); 42 in the Yerevan region incl. the airport. Includes Zvartnots 24/7, M-4 Drive-Thru, Ejmiatsin ×2, Armavir, Abovyan, Tsaghkadzor, Gyumri ×2, Vanadzor ×2. Siblings A2/A5 use "52 listed / 57 claimed" | Oct 2026 | VERIFIED | [10] |
| 32 | Fuel stations within 200 m of corridor | M-5 Yerevan edge → Ejmiatsin (11.9 km): 21; M-2 edge → Artashat (21 km): 20; M-1 Yerevan edge → M-3 jn (~11 km): 29; H-3 Jrvezh → Garni (18 km): 7 | OSM Oct 2026 | REPORTED (OSM) | [19] |
| 33 | Cross-sections (lanes per carriageway, limit) | Isakov 3+3, 60; Arshakunyats 4+4, 50–60; Halabyan 3+3; Sebastia 3+3; Tbilisian 2+2, 60; Artashat hwy 2+2, 60; M-5 dual 2+2 to Armavir, 90; M-2 dual to Artashat (2–3 lanes, 90–100); M-1 ≈dual 2+2 to Gyumri, 90–100; H-3 single 1+1, 60 | OSM Oct 2026 | REPORTED (OSM) | [19] |
| 34 | Land asking prices, residential/commercial plots | Kotayk $66–150/m²; Yerevan periphery $160–350/m²; Erebuni frontage $380/m²; Arabkir $1,008/m². None on a shortlisted corridor; mostly residential. *Fact-check: downgraded to indicative only* | Mar–Oct 2026 (was "Sep–Oct") | REPORTED (12 listings; indicative) | [16][17] |
| 35 | Garni temple visitors | ≈390,000 (250,000 Armenians, 137,400 foreigners); ≈200,000 in 2013 | 2019 | REPORTED | [20] |
| 36 | Zvartnots expansion | $500 M terminal programme announced Oct 2025; concession extended to 2067 (Jan 2026), ≈$425 M investment | 2025–26 | REPORTED | [7] |

---

## 3. Detailed findings and analysis

### 3.1 Method

- **Traffic.** I looked for published counts for every corridor in scope. The best sources turned out to be two ADB documents I had not used before:
  - the Economic Analysis of the Yerevan Urban Development Investment Project (Sep–Nov 2023) [1];
  - the Tranche 1 Project Completion Report of the North–South Road Corridor programme (Jan 2020) [3].

  Both reproduce Roads Department automatic-counter series and Road Police counts. I brought these forward to 2025 with growth bands bracketed by observed growth (ESTIMATE, formulas in §3.2).
- **Catchment.** Population within 1/3/5/10 km of each candidate point comes from the **Kontur Population H3 grid for Armenia** (release 2023-11-01; 12,708 cells of about 0.7 km²; total 2.79 M against Armstat's 3.10 M). That is about **10 % below** Armstat at national level. Raw values are reported, not rescaled (ESTIMATE). Candidate points sit on the road itself (snapped to OSM geometry); coordinates are in `research/data/B4-candidate-sites.csv`.
- **Competition and road attributes.** I ran OpenStreetMap Overpass extracts (base timestamps 2026-06-01 to 2026-10-10) for fuel stations, cafés, fast food, restaurants, convenience stores and supermarkets, plus all motorway/trunk/primary roads (with lanes, maxspeed, oneway and link roads). I geocoded Coffee House's own branch list from its website [10]. OSM undercounts small cafés, so treat café and fast-food counts as **lower bounds**.
- **Income.** Armstat wages by marz (Q2 2026) and ILCS 2024 poverty rates. Wages are recorded by *employer* location, so suburbs that commute to Yerevan are understated.
- **Seasonality.** Armstat monthly accommodation and food-service turnover (2025), monthly border crossings by checkpoint (2026), the ADB hourly profile, and the ADB M-1 July factor.

### 3.2 Traffic evidence by corridor: counts and 2025 bridging

| Corridor / point | Latest count | Year | Growth evidence | 2025 estimate (low / base / high) | Formula |
|---|---|---|---|---|---|
| **M-5 western main road, km 12** (between airport jn and Ejmiatsin) | 34,805 | 2021 | +9 %/yr 2016–21 | 39.2k / **43.1k** / 47.4k | 34,805 × (1.03 / 1.055 / 1.08)^4 |
| **Admiral Isakov Ave, section AB** (Monte Melkonian jn → Victory Bridge, 1.4 km; the counted section, east of the recommended site) | 40,052 (police); ADB 2023 base 44,100 (= 2020 count +10 %) | 2020 / 2023 | ADB uses 3 %/yr | 45.9k / **46.8k** / 48.6k | 44,100 × (1.02 / 1.03 / 1.05)^2. *Fact-check correction: not applicable west of Monte Melkonian. That stretch (site U05) is uncounted; Monte Melkonian feeds 25,100 veh/day into the junction* |
| **Arshakunyats Ave** | 40,430 (police); ADB 2023 CD 44,500 | 2020 / 2023 | as above | 44.6k / **47.2k** / 51.6k | low/high from the 2020 count × (1.02 / 1.05)^5; base 44,500 × 1.03^2 |
| **M-2, km 9.38** (Artashat highway, Yerevan edge) | 37,831 | 2018 | 3.8 %/yr 2014–18 (ADB); table CAGR 3.35 % (33,163 → 37,831); ADB re-evaluation 4 % cars / 3 % goods | 46.5k / **49.1k** / 51.5k | 37,831 × (1.03 / 1.038 / 1.045)^7; ADB forecast 49,600. *Fact-check correction: the base was 51.5k at 4.5 %/yr, above every growth figure cited. The 2018 count is also a +16.8 % one-year jump from 2017 (32,386). The former 6 %/yr high case (56.9k) is dropped as unsupported* |
| **M-2, km 13–29** (Masis → Artashat) | 10,297 at km 16 | 2009 | ADB forecast | ≈ **23k** (20–28k) | ADB 2025 forecast 23,200 [3] (ASSUMPTION ±15 %) |
| **M-1, km 20.7** (beyond Ashtarak, between M-3 jn km 18.8 and km 23.2; a proxy for the Davtashen/Homplex exit, not a measurement there) | 18,635 | 2017 | "stalled" 2013–17 (ADB); +12 %/yr 2018–21 for "M1 just north of the city" (ADB; possibly another counter) | **25.2k – 33.1k** (equal weight); outer bound 35.7k | low: ADB 2025 re-evaluation forecast 25,200 (km 11.8–23.2) [3]; 18,635 × 1.04^8 = 25.5k; high: ×1.04 (2018) × 1.12³ (2021) × 1.05^4 = 33.1k; outer: 1.07^4. *Fact-check correction: 33.1k was the base, 31 % above ADB's forecast. It is now presented as a range with no single base. The city exit probably carries more, because it includes Ashtarak and M-3 traffic* |
| **M-4 Yerevan edge, km ~10** (comparator) | 21,505 | 2008 | network growth | 33k / **42k** / 54k | B1 |
| **M-4 Hrazdan E → Sevan W** (comparator) | none | — | — | 10k / **17k** / 27k | B1 |
| **H-3 Yerevan–Garni beyond Jrvezh** | **no count found** | — | — | 3k / **5k** / 8k | ASSUMPTION: ~15–20k residents along the road plus ≈390k Garni visitors/yr (≈1,070/day on average, ≈300–430 vehicles/day at 2.5–3.5 persons/vehicle). *Fact-check correction: was "350–450"; 1,068 ÷ 3.5 = 305 and ÷ 2.5 = 427* |
| **Tbilisian highway** (2+2 lanes) | **no count found** | — | — | 22k / **26k** / 29k | ESTIMATE: 4 lanes × 5,560–7,350 veh/lane/day (per-lane yields of Arshakunyats and Isakov AB on ADB's 2023 base, not 2025; slightly conservative) |
| **Halabyan / Sebastia / Davtashen bridge** (3+3 lanes) | **no count found** | — | — | 33k–44k | ESTIMATE: 6 lanes × same per-lane yield |
| **M-6 Vanadzor–Bagratashen** | 4,000 cars/day | 2023 | 2,800 in 2014 | ≈4.2–4.5k | B1 [14 there] |

Cross-check: in 2008 the M-2, M-4 and M-5 exit counters all read 21–21.5k [4] (M-2 20,965; M-4 21,505; M-5 21,471). By 2018–21 the M-2 (37.8k, +80 %) and M-5 (34.8k, +62 %) series had grown by 62–80 %. The M-5 figure compares two different counters (km 9.4 in 2008, km 12 in 2021), so it is only indicative. *Fact-check correction: the growth range was stated as 60–75 %.* That supports B1's M-4 edge base of 42k. It also shows that **the M-4 edge has no traffic advantage over the M-2 or M-5 edges**.

**Directional splits matter for a coffee concept.** On Isakov section AB (east of Monte Melkonian), inbound (to the centre) is **57 %** of two-way traffic (22,718 vs 17,334, May 2020) [1]. ADB found "no obvious explanation" and flagged it for checking. *Fact-check correction: the split west of the Monte Melkonian junction, where the recommended site is, is unmeasured. Do not carry the 57 % there.* Arshakunyats is balanced (49/51). Morning coffee demand sits on the inbound carriageway (ASSUMPTION, as in B1).

**Daily profile.** On the western arterial (2014 counts, slightly west of the M-1/M-2 intersection), 70 % of traffic falls between 08:00 and 19:00, the peak hour is only 6 % of daily traffic, and the weakest day is 93 % of the weekly mean [1]. Urban corridors therefore load a drive-thru steadily through the day and week. Leisure highways concentrate demand on weekends (B1).

### 3.3 Corridor-by-corridor assessment

#### (1) M-5: Yerevan – Zvartnots airport – Ejmiatsin – Armavir

- **Road.** Inside Yerevan it is Admiral Isakov Ave: 3+3 lanes, 60 km/h, dual carriageway, with 9 link roads within 600 m of the Malatia point (grade-separated junctions). West of the city boundary it becomes the Yerevan–Armavir highway: dual carriageway for 11.9 km to Ejmiatsin and 23 km to Armavir, 2+2 lanes, 90 km/h (OSM [19]).
- **Traffic.** 34,805 two-way at km 12 in 2021, ≈43k in 2025 (ESTIMATE). Isakov section AB (east of Monte Melkonian) ≈46.8k (2025). *Fact-check correction: the recommended site between Monte Melkonian and the city boundary (U05) has no count. The km-12 series (≈21,000 same-side light vehicles) is the documented floor; the rest is a gap (§5).* This is the corridor of commuters from Ejmiatsin, Armavir marz, Parakar and Malatia. ADB's 2014 origin–destination survey showed Armavir marz, the airport and Malatia-Sebastia as the main origins of inbound trips [1].
- **Airport.** 5.62 M passengers in 2025 (REPORTED [7]); +12.1 % air passengers in Jan–Aug 2026 (VERIFIED [5]). The airport road carries an estimated **12,300–17,300 vehicle movements/day** (ESTIMATE: 15,386 pax/day × 80–90 % by car/taxi ÷ 1.6–2.0 pax/vehicle × 2 movements). Summer person-crossings run 1.47× the Jan–May level (ESTIMATE [6]). A $500 M terminal expansion and concession extension to 2067 are reported [7].
- **Catchment.** Kontur 3 km / 5 km: Isakov mid (Malatia) 154k / 401k; Isakov west at the boundary 75k / 209k; airport junction 27k / 140k; Ejmiatsin east entrance 36k / 54k.
- **Income.** Malatia-Sebastia is Yerevan's most populous district (151.2k). The Yerevan average wage is 357,583 AMD. Armavir marz is weaker (195,606 AMD; poverty 27.0 %).
- **Competition.**
  - Coffee House is in the terminal (24/7) and at Malatia (141/1 Andranik St). Paul is at the airport (OSM).
  - Along the Isakov–Parakar strip there are 0–2 cafés within 1 km of the candidate points, but **15 fuel stations within 1 km** of the Malatia point (7 within 500 m) and **21 fuel stations within 200 m** of the Yerevan-edge → Ejmiatsin stretch. A dense fuel strip suits a hybrid.
- **Land.** Inside the city the frontage is built up, and land is the binding constraint. Parakar (Armavir marz) on the city-boundary side looks more available, but this needs field verification (gap).
- **Access.** Right-in/right-out only, because the median separates the carriageways. Pick the **inbound side** for commuters, or a junction with a U-turn/overpass.
- **Risk.**
  - The ADB link project will reroute Kentron-bound traffic off Isakov east of Monte Melkonian after ~2028 (−36 % on that section). Sites to the west are unaffected [1]. The civil works contract was signed on 1 May 2026 and the loan closes on 31 Mar 2028 [22]. Expect construction disruption near the junction during 2026–28 and a possible slip past 2028.
  - The inbound/outbound asymmetry needs re-counting. It was measured only east of Monte Melkonian.
  - A non-food Onex Drive Thru was announced in 2026 at a Flash station at Admiral Isakov 7/7 [23]. Check whether Flash pads on Isakov are still free before assuming a fuel-station hybrid here.
- **Seasonality.** Low for commuters, moderate for the airport component (≈1.3–1.5× summer).

#### (2) M-1: Yerevan – Ashtarak – Gyumri

- **Road.** In the city: Ashtarak highway (2–3 lanes per carriageway, 60 km/h). Beyond the edge it is a dual carriageway at 80–100 km/h almost to Gyumri (most of the Yerevan–Gyumri highway is mapped as one-way carriageways in OSM). The interchanges at Ashtarak (km 16.3), Kasakh bridge (km 17.1) and the M-3 junction (km 18.8) are grade-separated [3][19].
- **Traffic.** The counter at km 20.7 lies between the M-3 junction (km 18.8) and km 23.2, beyond Ashtarak. It does not measure the Davtashen/Homplex city exit, which probably carries more because it also has Ashtarak and M-3 traffic. The counter read 18,635 in 2017. ADB then reports +12 %/yr in 2018–21 for "M1 just north of the city", possibly from a different counter. My 2025 range is **25.2–33.1k**, weighted equally. The low end is ADB's own 2025 re-evaluation forecast for km 11.8–23.2 (ESTIMATE; a proxy for the exit). *Fact-check correction: the base was ≈33k (25.5–35.7k), 31 % above ADB's forecast.*
- **The corridor's own record shows two risks.**
  - ADB's 2020 completion report found growth "stalled" in 2013–17 (0.7× GDP).
  - It also found that "traffic has not diverted to Bavra and Gyumri's economy has not developed as hoped", and cut its M-1 forecasts sharply [3].

  Uncertainty is therefore wide. Bavra crossings (M-1 north end) were 954,974 in 2025 (+18.5 %) but only +0.8 % in Jan–Aug 2026 [6].
- **Catchment.** 3 km / 5 km: Ashtarak-highway point in Davtashen 114k / 278k; Yerevan exit at Homplex 27k / 94k; Ashtarak town 17.5k / 26k. Davtashen (52.7k, +1.3 %/yr) and Ajapnyak (123.6k) feed the city end. Ashtarak is a commuter town (ADB: "commuter settlement", 18,000 in 2016 [3]).
- **Income.** The Yerevan end has Yerevan incomes. Aragatsotn's employer wage is low (170,768 AMD), but it has the second-lowest poverty in Armenia (7.6 %, after Syunik at 6.2 %). *Fact-check correction: the text said "lowest". The marz intervals are wide (Aragatsotn 95 % CI 4.0–11.3 %), so small gaps between marzes should not drive site scores.*
- **Competition.** OSM shows **0 cafés and 0 fast-food outlets within 1 km** of the Davtashen and Homplex points. But **KFC and Coffee House both trade at Homplex Hyper Mall**, ≈1.1 km from the exit point (C03). 29 fuel stations sit within 200 m between the Yerevan edge and the M-3 junction. *Fact-check correction: the KFC at Homplex was not counted. The white space is thinner than a score of 5 suggests, and the White-space score is cut to 4 (§3.9).*
- **Seasonality.** M-1 July = 1.197× AADT (≈2005–09 counter data) [4]; Bavra summer factor 1.54× (long-distance flows).
- **Verdict.** A good second-tier exit corridor with some white space and strong reported 2018–21 growth. But its counted volume is weaker than the M-5 or M-2, its data are older, and the counter is not at the exit itself.

#### (3) M-2: Yerevan – Artashat – Ararat (south)

- **Road.** Arshakunyats Ave runs into the Artashat highway (2+2, 60 km/h), then the Yerevan–Meghri highway: dual carriageway for ≈21 km to Artashat (2–3 lanes, 90–100 km/h) and ≈17 km of dual onward to Ararat [19].
- **Traffic.** Counter at km 9.38: 37,831 in 2018, the highest measured interurban figure in the country. ADB forecast 49,600 for 2025; my base is **49.1k** (37,831 × 1.038^7; range 46.5–51.5k). On a same-side basis (≈22,600 light vehicles) the M-2 is level with Isakov AB and Arshakunyats, not above them. *Fact-check correction: the base was 51.5k at 4.5 %/yr. ADB reports 3.8 %/yr for 2014–18, and the table CAGR is 3.35 %.* Volume halves beyond the Masis junction: km 16 was 44 % of km 9.38 in 2009. ADB forecast ≈23k for 2025 on km 13–29 [3].
- **Mix.** 92 % light vehicles in 2018, so ≈3,000 trucks/day.
- **Catchment.** 3 km / 5 km: M-2 edge 61k / 181k; Arshakunyats south 114k / 303k; Masis junction 22k / 52k.
- **Settlements.** Masis 23.7k (+1.7 %), Artashat 22.8k, Ararat 17.8k, and Ararat marz 271.7k (+1.0 %). Ararat marz wage is 234,735 AMD (second only to Yerevan among the marzes covered here) and poverty is 15.7 %, which makes the commuter base relatively affluent.
- **Competition.** **0 cafés within 1 km** of the edge point and only 1 within 3 km. The nearest Coffee House is 4.6 km away. 20 fuel stations sit within 200 m from the edge to Artashat. This is the clearest white space among the high-volume corridors.
- **Risks.**
  - Truck share, plus the Iran-dependent long-distance component (Meghri crossings −32 % y/y in Jan–Aug 2026).
  - A weekend tourist component towards Khor Virap, Areni and Jermuk (ASSUMPTION; Meghri's summer factor is only 1.07×).
  - The urban edge here (Noragavit, Ayntap) is lower-amenity, light-industrial (ASSUMPTION; check in the field).

#### (4) Yerevan – Garni – Geghard (H-3)

- **Road.** Single carriageway 1+1 at 60 km/h for ≈17 km beyond Jrvezh [19]. Both directions are accessible from one site, which is the corridor's main advantage.
- **Traffic.** **No count found** (gap). Garni had ≈390k visitors in 2019 (REPORTED [20]). That is ≈1,070/day on average, or roughly 300–430 vehicles/day at 2.5–3.5 persons per vehicle including coaches (ESTIMATE). *Fact-check correction: the range was stated as 350–450; 1,068 ÷ 3.5 = 305 and ÷ 2.5 = 427. The conclusion is unchanged.* Add local traffic: Kontur counts only ≈12k people within 10 km of Garni and 35k within 3 km of Jrvezh. My order of magnitude is 3–8k AADT (ASSUMPTION).
- **Competition.** 19 restaurants within 1 km of Jrvezh and 18 within 200 m of the road. Tourist meals here are sit-down (khorovats and village restaurants).
- **Seasonality.** Strongly tourist-driven; likely at least as seasonal as the Sevan segments (ASSUMPTION; no monthly visitor data).
- **Verdict.** Not a first-site candidate: ≈5.6 % capture would be needed for 120 transactions/day.

#### (5) Yerevan arterials and exits

| Arterial (OSM point) | Cross-section | Count / estimate | 3 km / 5 km pop. (Kontur) | Cafés / fast food within 1 km (OSM) | Nearest Coffee House | Notes |
|---|---|---|---|---|---|---|
| Admiral Isakov Ave (Malatia, M-5; point U05, west of Monte Melkonian) | 3+3, 60 km/h, grade-separated | No count at this point. 40,052 (2020) and ≈46.8k (2025) are for section AB, ≈2.1 km east, between Monte Melkonian and Victory Bridge; documented floor = km-12 series ≈43k | 154k / 401k | 1 / 1; 15 fuel within 1 km | 1.8 km | Sit west of Monte Melkonian (link-road risk), but the volume there is unmeasured. *Fact-check correction: was "best counted urban corridor"* |
| Isakov west / city boundary | 3+3 | ≈ M-5 + airport (uncounted) | 75k / 209k | 0 / 3 | 1.9 km (airport) | Transition to Parakar; more land likely |
| Arshakunyats Ave (Shengavit, Yerevan Mall) | 4+4, 50–60 km/h | 40,430 (2020); ≈47.2k (2025); +15 % after 2028 | 172k / 416k | 12 / 26 | 1.2 km | Proven food demand (BK, KFC, Black Star, Cofix in mall cluster); dense competition; scarce plots |
| Artashat hwy south end | 2+2 | ≈ M-2 edge | 114k / 303k | 0 / 0 | 2.3 km | Transitional; check land |
| Sebastia St (M-1 in city, Malatia) | 3+3 | none (33–44k est.) | 153k / 415k | 5 / 6 | 1.6 km | Retail strip; Tashir 1 km |
| Arno Babajanyan St (EVN-1) | 2–3 per side | none | 130k / 288k | 5 / 4; 12 fuel within 1 km | 0.4 km | Coffee House Malatia adjacent |
| Halabyan St (Ajapnyak) | 3+3 | none (33–44k est.) | **206k / 490k** | 7 / 14 (117 cafés within 3 km) | 0.8 km | Largest catchment; saturated café market |
| Davtashen bridge (north end) | 3+3; 18 link roads within 600 m | none | 175k / 446k | 5 / 2 | 1.0 km | Complex interchange; Jazzve 0.3 km |
| Ashtarak hwy (Davtashen; M-1) | 2–3 per side | ≈ M-1 (≈33k) | 114k / 278k | 0 / 0 | 2.5 km | White space; growing district |
| Tbilisian hwy (Kanaker-Zeytun → Avan/Arinj) | 2+2, 60 km/h | none (22–29k est.) | 183k / 427k (south); 121k / 302k (north) | 8 / 2 (south); 0 / 1 (north) | 1.2 / 2.9 km | Feeds Arinj, Abovyan and the M-4 inside the city; no seasonality |
| Gai Ave / Tevosyan (Nor Nork; H-3 start) | 2+2 | none | 160k / 350k | 6 / 8; 12 fuel within 1 km | ≈0.4–1.0 km (Megamall) | Large district (137.8k) |

Sources: counts [1]; cross-sections, POIs [19]; population [18]; Coffee House [10]. "None" means no count found.

**Suitability judgement.**
- Every arterial is a dual carriageway with a median, so a site is right-in/right-out only (REPORTED OSM).
- A drive-thru needs a plot with frontage and room for a 8–12 car stacking lane (ASSUMPTION, typical drive-thru design).
- Such plots exist mostly at the **edges**: Isakov west, Artashat highway, Ashtarak highway, Tbilisian north. They are rare along Arshakunyats, Halabyan or Sebastia, where frontage is built up.
- Municipal approval of new curb cuts on primary arterials is an unverified constraint (gap).

#### (6) Fast-growing suburbs and satellite towns

| Town | Pop. 1 Jul 2026 (k) | Δ vs 2025 | Marz wage Q2 2026 (AMD) | Marz poverty 2024 | Kontur 3 km / 5 km | Food POIs within 1 km (café / fast food) | Coffee House present? | Comment |
|---|---|---|---|---|---|---|---|---|
| Abovyan | 51.5 | +1.4 % | 208,210 (Kotayk) | 24.8 % | 52k / 70k | 4 / 0 | Yes (centre, 0.5 km) + M-4 drive-thru 2.3 km from interchange | Largest satellite; M-4 interchange site = B1's segment |
| Ejmiatsin (Vagharshapat) | 48.9 | +1.5 % | 195,606 (Armavir) | 27.0 % | 38k / 56k | 4 / 7 | Yes ×2 | Pilgrim/tourist town; M-5 east entrance 36k within 3 km |
| Masis | 23.7 | +1.7 % | 234,735 (Ararat) | 15.7 % | 24k / 45k | 7 / 9 | No (nearest 10.6 km) | Fastest-growing town; on M-2 |
| Charentsavan | 24.1 | 0.0 % | 208,210 | 24.8 % | 19k / 23k | 0 / 1 | No | Stagnant; M-4 |
| Artashat | 22.8 | −0.9 % | 234,735 | 15.7 % | 25k / 35k | 0 / 1 | No | M-2 |
| Ashtarak | 17.8 | +0.6 % | 170,768 (Aragatsotn) | 7.6 % | 18k / 26k | 1 / 0 | No (nearest 8 km) | Commuter town on M-1 |
| Nor Hachn | 10.5 | +1.0 % | 208,210 | 24.8 % | 21k / 51k | 1 / 1 | No | Off-corridor |
| Arinj (village, Kotayk) | n/a (OSM 2022: 6.6k) | n/a | 208,210 | 24.8 % | 84k / 215k (abuts Avan / Nor Nork) | 0 / 0 | No | Cottage-building hotspot; plot asking price $150/m² |
| Armavir | 30.3 | +0.7 % | 195,606 | 27.0 % | 32k / 44k | 2 / 0 | Yes | End of M-5 dual carriageway |

Sources: [8][12][13][18][19][10]. "Δ" means 1 Jul 2025 → 1 Jul 2026.

**Commuter flows.**
- No current origin–destination data were found (gap). The evidence is indirect:
  - the ADB western-ring-road OD survey (2014) [1];
  - the ADB description of Ashtarak as a commuter settlement [3];
  - B1's commuter logic for Abovyan → Yerevan;
  - Kotayk's housing boom (4.4×, mostly self-built houses) [11].
- Suburban growth is **diffuse**: low-density houses spread over Kotayk villages. It does not create a dense new catchment around one point.
- **For a first drive-thru, the better play is to sit on the radial road where these commuters converge inside the city edge** (Tbilisian highway for Arinj/Abovyan/Nor Hachn; Artashat highway for Masis; Isakov/M-5 for Ejmiatsin/Parakar; Ashtarak highway for Ashtarak). That beats a site in a satellite town itself (ESTIMATE/ASSUMPTION).

#### (7) Second-tier cities: Gyumri and Vanadzor

| City | Pop. 2026 (k) | Δ y/y | Marz wage (AMD) | Poverty | Kontur 3 km | Competition in centre | Traffic evidence |
|---|---|---|---|---|---|---|---|
| Gyumri | 114.0 | −0.3 % | 169,392 (Shirak) | **43.0 %** | 76k | Coffee House ×2 (0.2 km), KFC, Tashir; 25 cafés within 1 km | No count. ADB 2020: M-1 Gyumri traffic and economy below expectations [3]. Shirak airport crossings 138,522 in 2025 [6] |
| Vanadzor | 77.7 | −0.4 % | 177,340 (Lori) | 20.4 % | 41k | Coffee House ×2, KFC, Tashir; 16 cafés / 25 fast food within 1 km | M-6 4,000 cars/day (2023) [B1]; M-3 Vanadzor 4,799 (2008) [4] |

Both cities have shrinking populations, weak incomes, low through-traffic and incumbents already present. They suit later, small-format (walk-up or kiosk) units at most. They are not suitable for a first drive-thru.

### 3.4 Competitor landscape (alternatives vs M-4)

- **Drive-thru.**
  - The only identified drive-thru is Coffee House's on the M-4 at Ptghni/Balahovit, 08:30–24:00 (A2; VERIFIED [10]). It sits 0.0 km from my "M-4a" point.
  - OSM has no food drive-through tags (a tag of `no` appears on KFC Moskovyan and Burger King Dalma). KFC's 13 and Burger King's 4 mapped outlets are all in malls or the centre (Yerevan Mall on Arshakunyats, Dalma on Tsitsernakaberd highway, Northern Ave, Komitas) [19].
  - **No evidence was found of a drive-thru on the M-5, M-2, M-1 or Tbilisian corridors.** This should be confirmed in the field and on Yandex/Google Maps, since web search was unavailable (gap).
- **Coffee House** has 51 geocoded branches. Their distance from candidate points:
  - 0.2–0.5 km in Ejmiatsin, Abovyan, Gyumri and Vanadzor centres;
  - 1.1 km at the airport junction and at Homplex (M-1 exit);
  - 1.2–1.9 km on the Arshakunyats, Isakov and Tbilisian south points;
  - **4.6 km at the M-2 edge, 8 km at Ashtarak and 10 km at Masis** [10].
- **Mall food clusters.** Yerevan Mall (Arshakunyats) and Dalma Garden Mall (Tsitsernakaberd) concentrate international QSR. They prove demand for fast food and coffee, but they are walk-in and mall-dwell formats.
- **Fuel stations.** The extract holds 614 fuel stations. The main brands mapped are CPS (73), Flash (52), Max Oil (36), RAN Oil (16), Orange (12) and Gastop (10) [19]. Fuel strips line every exit corridor; they are potential pad or kiosk partners, as B1 suggests for the M-4.

### 3.5 Population catchment (Kontur, raw, ≈10 % below Armstat nationally)

| Point | 1 km | 3 km | 5 km | 10 km |
|---|---|---|---|---|
| Halabyan St (Ajapnyak) | 15.7k | **206.1k** | **490.2k** | 1,043.8k |
| Tbilisian hwy south (Kanaker-Zeytun) | 31.4k | 182.7k | 426.6k | 946.2k |
| Davtashen bridge north | 25.5k | 175.0k | 445.5k | 999.9k |
| Arshakunyats mid (Shengavit) | 28.7k | 172.0k | 416.3k | 1,046.1k |
| Gai Ave / Nor Nork | 30.6k | 160.3k | 349.7k | 876.6k |
| Isakov mid (Malatia) | 6.1k | 153.8k | 401.2k | 969.7k |
| Sebastia St | 26.8k | 153.4k | 415.1k | 981.7k |
| Tbilisian hwy north (Avan–Arinj) | 13.7k | 121.1k | 301.5k | 842.4k |
| Ashtarak hwy (Davtashen) | 7.6k | 113.6k | 277.6k | 853.8k |
| Isakov west / boundary | 4.8k | 74.9k | 209.3k | 762.5k |
| M-2 Artashat hwy Yerevan edge | 12.5k | 60.8k | 181.3k | 661.0k |
| M-5 airport junction | 3.9k | 27.0k | 139.9k | 583.7k |
| M-1 Yerevan exit (Homplex) | 1.6k | 27.3k | 93.5k | 562.6k |
| Abovyan centre | 17.0k | 51.9k | 69.8k | 257.6k |
| Gyumri centre | 13.1k | 75.5k | 100.2k | 122.5k |
| **M-4 Coffee House Drive-Thru (Ptghni)** | 2.5k | 24.4k | 94.5k | 448.7k |
| **M-4 Abovyan interchange** | 1.5k | 41.5k | 79.5k | 261.1k |
| **M-4 Charentsavan** | 0.0k | 17.1k | 20.9k | 41.7k |
| **M-4 Sevan W** | 2.3k | 13.2k | 22.7k | 29.7k |

ESTIMATE. Method: sum of Kontur H3 cell populations whose centroids fall within the radius [18]. The full table, with POI counts, is in `research/data/B4-candidate-sites.csv`.

### 3.6 Land and lease indications

| Location | Plot | Asking price | $/m² | Listed | Source |
|---|---|---|---|---|---|
| Abovyan (Dzoraghbyur cottage area) | 500 m² residential | $33,000 | 66 | 28 Sep 2026 | [16] |
| Dzoraghbyur (Kotayk) | 1,166 m² | $99,000 | 85 | 30 Sep 2026 | [16] |
| Hrazdan | 600 m² | $54,000 | 90 | 28 Sep 2026 | [16] |
| Ptghni (next to M-4 drive-thru area) | 525 m² | $60,000 | 114 | 30 Apr 2026 | [16] |
| Arinj, Duryan St (front line, 20 m frontage) | 800 m² | $120,000 | 150 | 7 Oct 2026 | [16] |
| Avan, Duryan district (Yerevan) | 6,000 m² | $960,000 | 160 | edited 6 Oct 2026 | [17] |
| Ajapnyak G-1 district | 1,000 m² | $245,000 | 245 | 10 Sep 2026 | [16] |
| Avan, N. Safaryan St | 1,015 m² | $252,000 | 248 | edited 25 Sep 2026 | [17] |
| Nork-Marash | 1,000 m² | $285,000 | 285 | 28 Sep 2026 | [16] |
| Ajapnyak G-1 district | 10,000 m² | $3,500,000 | 350 | edited 1 Apr 2026 | [17] |
| Erebuni St, first line (commercial) | 250 m² | $95,000 | 380 | 7 Oct 2026 | [16] |
| Arabkir, A. Khachatryan St | 972 m² | $980,000 | 1,008 | 7 Oct 2026 | [16] |

All REPORTED as asking prices. The sample is small (12 listings) and residential-heavy, and myrealty's currency is assumed to be USD (the site's default). For a 1,500–2,500 m² drive-thru pad, the implied land cost (ESTIMATE) is:
- Kotayk suburbs: ≈$0.10–0.38 M
- Yerevan periphery: ≈$0.24–0.88 M
- inner city: >$1.5 M

**No commercial ground-lease listings were obtained** (list.am returned 403; gap). The model's ground-lease placeholder (AMD 1.3–1.8 M/month) is untested.

### 3.7 Exposure and required capture (comparable across sites)

Accessible same-side light vehicles = AADT 2025 × directional share × light-vehicle share. Required capture = 120 ÷ accessible vehicles. The 120 transactions/day figure is A2's mid-point for a well-sited unit.

| Site | AADT 2025 | Dir. share | Light share | Accessible light veh/day | Capture needed for 120 tx/day | Tx/day @0.5 % | Tx/day @1.0 % |
|---|---|---|---|---|---|---|---|
| M-5 Isakov Ave, inbound (Malatia) | 46,786 | 0.567 | 0.927 | 24,591 | **0.49 %** | 123 | 246 |
| M-2 Artashat hwy, Yerevan edge | 51,483 | 0.5 | 0.921 | 23,708 | **0.51 %** | 119 | 237 |
| Arshakunyats Ave | 47,210 | 0.5 | 0.951 | 22,448 | **0.53 %** | 112 | 224 |
| M-5 west of airport jn (km 12) | 43,117 | 0.5 | 0.977 | 21,063 | **0.57 %** | 105 | 211 |
| M-1 Ashtarak hwy / Yerevan exit | 33,096 | 0.5 | 0.967 | 16,002 | 0.75 % | 80 | 160 |
| Tbilisian hwy (no count; mid-estimate) | 25,800 | 0.5 | 0.93 | 11,997 | 1.00 % | 60 | 120 |
| H-3 Yerevan–Garni (ASSUMPTION) | 5,000 | 0.5 | 0.85 | 2,125 | 5.65 % | 11 | 21 |
| M-4 Yerevan edge (B1 base) | 42,000 | 0.5 | 0.82 | 17,220 | 0.70 % | 86 | 172 |
| M-4 Abovyan–Charentsavan (B1) | 27,000 | 0.5 | 0.82 | 11,070 | 1.08 % | 55 | 111 |
| M-4 Hrazdan E–Sevan W (B1) | 17,000 | 0.5 | 0.82 | 6,970 | 1.72 % | 35 | 70 |
| Model placeholder (16k × 0.55 access) | 16,000 | 0.55 | 1.0 | 8,800 | 1.36 % | 44 | 88 |

ESTIMATE. Light shares come from the counts cited in §2; the M-4 share is from B1. Read this as **exposure**, not forecast revenue.
- Urban commuters have more alternatives and shorter dwell, so their conversion per passing car could be lower than a weekend driver's on the way to Sevan. If urban capture were only half of highway capture, the urban edges would still match or beat the M-4 Abovyan–Charentsavan segment and clearly beat Hrazdan–Sevan.
- Drive-thru lane capacity, not exposure, caps peak throughput (≈40–60 cars/hour for a single lane; ASSUMPTION to be checked by the operations workstream).

### 3.8 Seasonality: urban vs tourist highway, quantified

| Indicator | Peak vs mean or base | Trough | Jun–Aug share of year | Source / status |
|---|---|---|---|---|
| Accommodation & food-service turnover, Armenia (mostly Yerevan) | Aug 1.18 | Feb 0.73 (peak/trough 1.62; CV 0.13) | 28.4 % | ESTIMATE from VERIFIED [9] |
| Western arterial, daily variation | — | weakest day 93 % of weekly mean | — | VERIFIED [1] |
| M-1 interurban counter | July +19.7 % vs AADT | — | — | VERIFIED [4] |
| Zvartnots person crossings | Jun–Aug 1.47× the Jan–May average | — | — | ESTIMATE from VERIFIED [6] |
| Bavra (M-1 north end) / Bagratashen | 1.54× / 1.69× | — | — | ESTIMATE from VERIFIED [6] |
| Meghri (M-2 south end) | 1.07× | — | — | ESTIMATE from VERIFIED [6] |
| Model placeholder (M-4) | Aug 1.46 | Jan 0.66 (ratio 2.21; CV 0.25) | 34.0 % | model `assumptions.json` (PLACEHOLDER) |
| B1 assumption, Sevan segments | Jul–Aug 1.3–1.6× AADT | Jan–Feb 0.6–0.8× | — | ASSUMPTION (B1) |

**Proposed urban seasonality index for the model (ASSUMPTION)**, derived from the 2025 hospitality turnover profile and damped slightly because turnover includes tourists and price effects:

Jan 0.80, Feb 0.77, Mar 0.92, Apr 0.99, May 1.01, Jun 1.05, Jul 1.14, Aug 1.15, Sep 1.05, Oct 1.05, Nov 0.99, Dec 1.06.

The M-4 Sevan-type index should stay near the current placeholder until counts exist.

**Why this matters.**
- At an equal annual total, the M-4 profile puts 34 % of the year's volume into three months, against ≈28 % for urban.
- Peak staffing (the model's threshold is 1.15) would be triggered for 3 months on the M-4 placeholder (Jun–Aug) and at most 1 month (Aug) on the proposed urban index.
- A highway unit also faces weather closures and weekend concentration (B1), which an urban unit does not.

### 3.9 Scoring and ranked shortlist

The weights are an ASSUMPTION reflecting the revenue driver and first-site risk:
- traffic exposure 25 %
- year-round stability 15 %
- catchment within 3 km 15 %
- income 10 %
- competition / white space 10 %
- access and land feasibility 15 %
- data confidence 10 %

Each criterion is scored 1–5 by the analyst from the evidence above (ASSUMPTION/ESTIMATE).

| Rank | Candidate | Traffic | Stability | Catchment | Income | White space | Access / land | Data | **Weighted** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **M-5 western approach**: Isakov west of Monte Melkonian → boundary → Zvartnots jn, inbound side (fuel-hybrid preferred) | 5 | 4 | 3 | 4 | 4 | 3 | 5 | **4.05** |
| 2 | **Arshakunyats Ave** (Shengavit, north of future link jn) | 5 | 5 | 4 | 4 | 2 | 2 | 5 | **4.00** |
| 3 | **M-2 Artashat highway, south edge** (Noragavit–Ayntap, km 9–13) | 5 | 3 | 2 | 4 | 5 | 4 | 4 | **3.90** |
| 4 | **M-1 Ashtarak highway / Davtashen–Homplex exit** | 4 | 4 | 3 | 4 | 5 | 4 | 3 | **3.85** |
| 5 | **Tbilisian highway** (Kanaker-Zeytun → Avan/Arinj) | 3 | 5 | 5 | 4 | 3 | 3 | 2 | **3.60** |
| reserve | M-2 at Masis interchange | 4 | 3 | 2 | 4 | 4 | 4 | 3 | 3.45 |
| reserve | Gai Ave / Nor Nork (H-3 start) | 3 | 5 | 4 | 3 | 3 | 3 | 2 | 3.35 |
| reserve | M-5 Ejmiatsin east entrance | 4 | 3 | 2 | 3 | 4 | 4 | 3 | 3.35 |
| — | Halabyan St (Ajapnyak) | 3 | 5 | 5 | 4 | 1 | 2 | 2 | 3.25 |
| — | Davtashen bridge | 3 | 5 | 4 | 4 | 2 | 2 | 2 | 3.20 |
| — | Abovyan (town / M-4 interchange) | 3 | 4 | 3 | 3 | 3 | 4 | 2 | 3.20 |
| comparator | **M-4 Yerevan edge (km 9–12, Ptghni)** | 4 | 4 | 2 | 3 | 2 | 3 | 2 | **3.05** |
| — | Gyumri | 2 | 4 | 4 | 1 | 3 | 3 | 1 | 2.65 |
| — | Vanadzor | 2 | 4 | 3 | 2 | 3 | 3 | 1 | 2.60 |
| comparator | **M-4 Hrazdan–Sevan (tourist segment)** | 2 | 1 | 1 | 2 | 3 | 3 | 1 | **1.85** |
| — | H-3 Yerevan–Garni | 1 | 1 | 1 | 3 | 3 | 2 | 1 | 1.55 |

**Sensitivity.**
- Arshakunyats (#2) ranks high on counted volume and stability, but scores 2 on access and land. If a ≥1,500 m² plot with safe stacking cannot be found along it, **M-2 south edge moves to #2**.
- If data confidence is dropped and its 10 points are moved to white space, the order becomes M-1 exit (4.05), M-2 edge (4.00), M-5 west (3.95), Arshakunyats (3.70). The top group is robust; the order within it is not.
- Even with stability weighted at zero, the M-4 tourist segment stays in the bottom two (with the Garni road). Its problem is volume, not just seasonality.

### 3.10 Critical comparison: the M-4 concept vs the best alternatives

| Dimension | M-4 tourist highway (Hrazdan–Sevan) | M-4 Yerevan edge (Ptghni) | Best alternatives (M-5 west, M-2 edge, Arshakunyats, M-1 exit) |
|---|---|---|---|
| Traffic evidence | None after 2008; base 17k (ESTIMATE) | 2008 count; base 42k (ESTIMATE) | Counts from 2017–2021 (VERIFIED); 33–52k (2025 ESTIMATE) |
| Same-side light vehicles/day | ≈7,000 | ≈17,200 | ≈16,000–24,600 |
| Capture needed for 120 tx/day | 1.72 % | 0.70 % | 0.49–0.75 % |
| Seasonality | Strong: placeholder 0.66–1.46; B1 0.6–1.6; 10–14 peak weekends | Moderate: commuter-dominated, plus leisure weekends | Low: urban index ≈0.77–1.15; weakest day 93 % of weekly mean |
| Catchment within 3 km | 13–17k | 24k | 27k (edge points) to 172k (Arshakunyats) |
| Incumbent drive-thru | No (but fuel and lakeside cafés) | **Coffee House Drive-Thru, 4.9★** | None known |
| Land | Cheap (Kotayk $66–150/m²) but needs 90 km/h deceleration lanes | Cheap–moderate | Edge $150–380/m²; inner city scarce and ≥$1,000/m² |
| Brand / marketing value | High in summer (Sevan, Dilijan, Tsaghkadzor trips) | Medium | High year-round visibility to Yerevan residents (the repeat base) |
| Key risk | Volume and seasonality; winter closures; tunnel works | Head-to-head with Coffee House at about half our price | Permitting curb cuts; land; queue spill-back onto arterials; lower per-car capture |

**Bottom line (critical).**
- The founder's intuition that the M-4 is the "high-traffic" road is **not supported**: the M-2 and M-5 exits measured as much traffic or more, and with newer data.
- The M-4's distinctive asset is the **summer leisure peak**. That is attractive for brand visibility, but as a first unit it is a worse risk: lower base volume, higher seasonality and an incumbent at the city end.
- The M-4 idea is best reframed as **"Yerevan exit-corridor drive-thru"**. The first unit goes where commuters converge year-round (M-5 west or M-2 south edge, with Arshakunyats if a plot exists). The M-4/Sevan opportunity is tested later with a modular or seasonal unit or a fuel-station kiosk once the format is proven.

---

## 4. Implications for the drive-thru concept (critical)

1. **Change the model's base-case traffic input, or run it for two site archetypes.**
   - The model's placeholder (16k AADT × 0.55 access × 1.8 % capture ≈ 158 transactions/day) resembles neither archetype.
   - Urban/edge archetype: 43–52k AADT, 0.5 directional share, 0.92–0.98 light share, and a flatter seasonality index (§3.8).
   - Highway leisure archetype: B1's 17–27k with the current seasonality.
   - Do not import the M-4's 1.8 % capture rate into urban sites without field evidence. Run 0.4–1.0 % as the urban sensitivity range (ASSUMPTION).
2. **Year-round demand beats peak demand for a first unit.** The urban profile keeps the summer share near 28 % (vs 34 %) and avoids a 2.2× peak-to-trough swing. That lowers cash-flow risk in year 1, when the ramp curve is also depressing volume. It also means the opening month (the model assumes May, to "catch the first summer") matters much less for an urban site.
3. **The airport is a modifier, not a reason.** The terminal already has 24/7 coffee. An M-5 site should be judged on the Ejmiatsin/Armavir/Malatia commuter stream (inbound side). Departures before 07:00 and drivers waiting for arrivals are a bonus daypart (ASSUMPTION).
4. **Lead with a fuel-station hybrid on an exit corridor.** All three top exit corridors have 20–29 fuel stations within 200 m. Co-locating on an inbound-side station:
   - shares the curb cut, permits and utilities;
   - cuts the land bill (C1 excludes land);
   - mitigates the arterial-access permitting risk.
5. **Avoid the Isakov section east of Monte Melkonian.** ADB's link project is forecast to take 36 % of its traffic. Arshakunyats north of the new junction gains 15 %. Check the 2026 construction status before any lease.
6. **Do not open first in a satellite town, Gyumri or Vanadzor.**
   - Satellite towns: growth is real (+1.4–1.7 %/yr) but thin, and incomes are lower. Sit on the radial road where their commuters converge.
   - Gyumri and Vanadzor: shrinking, poorer (Shirak poverty 43 %) and already served by Coffee House and KFC.
7. **Garni/Geghard (H-3) is not a drive-thru corridor.** It is low-volume, tourist-seasonal and dominated by sit-down restaurants.
8. **Disconfirming evidence to keep in view.**
   - Urban drive-thru demand is unproven in Armenia; there is no urban drive-thru, and 41 % of households own a car (A1).
   - Congestion can make a queue a liability.
   - Inner-city plots are scarce and expensive.
   - Coffee House can react quickly; it already runs 51 branches and one drive-thru.
   - The M-2's long-distance flows are volatile (Meghri −32 % in 2026).
   - The M-1's growth has disappointed before (ADB 2020).
   - Every 2025 volume here is an extrapolation of 2017–2021 counts, not a measurement.

---

## 5. Data gaps and how to verify them

| Gap | Why it matters | How to close it (agency / document / method) |
|---|---|---|
| **2022–2026 counter data for M-1 km 20.7, M-2 km 9.38, M-5 km 12 (and M-4 km 10.3)** | Replaces 2017–21 extrapolations with current AADT, monthly and day-of-week profiles | Formal request to the Roads Department / MTAI (the "Roads Department annual reports" ADB cites [1]). Ask for monthly and hourly ATC data by direction and vehicle class |
| **Road Police 24-h counts for Yerevan arterials** (Tbilisian, Halabyan, Sebastia, Babajanyan, Davtashen bridge, Gai, Artashat hwy) | Only Isakov, Arshakunyats and Monte Melkonian (2020) are published | Request through Yerevan Municipality (the 2020 counts came from a "letter from the head of road police to the first deputy mayor" [1]); Yerevan Traffic Management Centre camera counts |
| **Isakov–Arshakunyats link status** | ±15–36 % traffic shift from 2028 | ADB project page 54172-002 (progress reports); Yerevan Municipality capital programme |
| **Field classified counts and stop-rate observation** | Capture rate is the most uncertain driver | 2-season (Feb + Jul) 16-hour classified counts by direction at the top-5 sites. Stop-rate counts at comparable outlets: Coffee House M-4 drive-thru and the airport branch, plus fuel-station shops on the M-5 and M-2 (B1 protocol). Budget ≈ US$12–20k for 5 sites (ASSUMPTION) |
| **Existing drive-thrus (KFC, Burger King, local chains) in Yerevan** | Confirms white space | Yandex/Google Maps scan for "drive", "драйв", "դրայվ"; a field drive of the top-5 corridors; chain HQ inquiry |
| **Commercial plots and ground-lease rates on the edges** | Land is the binding constraint; the model rent is a placeholder | Broker survey (estate.am, myrealty, list.am agents); e-cadastre.am parcel ownership and land-use category; Yerevan Municipality land auctions; CPS/Flash/Max Oil pad-lease quotes |
| **Curb-cut, access and zoning rules on Yerevan primary arterials and M-roads** | Permitting may rule out arterial sites | Yerevan Municipality urban-development department; MTAI and Road Police access standards; planning lawyer opinion |
| **Commuter origin–destination flows (Kotayk, Ararat, Armavir → Yerevan)** | Choosing the side of the road and the corridor | MTAI Transport Master Plan 2020–2030 (draft) [2]; Yerevan bus-network study OD data (ADB/CDIA); mobile-operator origin–destination data purchase |
| **Garni/Geghard visitor counts 2023–2025 by month** | H-3 seasonality | Ministry of Education, Science, Culture and Sport / Historical-Cultural Reserve-Museums Agency ticket data; Tourism Committee |
| **Airport ground-transport mode share** | Size of the airport-road component | Armenia International Airports CJSC; Zvartnots parking and taxi-dispatch data; Yandex Go/GG trip volumes |
| **Recent per-town building permits (Arinj, Masis, Ejmiatsin, Ashtarak)** | Suburban growth hotspots | Armstat marz handbooks (Ararat, Armavir, Aragatsotn "in figures"); community building-permit registers |
| **Kontur grid vintage** | Catchments may miss post-2020 growth (Arinj, Davtashen, new Yerevan blocks) | Re-run with WorldPop 2025 or GHSL 2025 when available; cross-check with Armstat district totals |

---

## 6. Sources (all accessed 2026-10-10)

1. ADB. *Yerevan Urban Development Investment Project (RRP ARM 54172-002): Economic Analysis* (PDF created 28 Sep 2023, revised 14 Nov 2023). Table 1: May 2020 Road Police 24-h counts. Table 2: Roads Department counts at km 12, 2016–2021. §6: 2014 hourly profile. Tables 4–5: 2023 base with and without the link. https://www.adb.org/sites/default/files/linked-documents/54172-002-ea.pdf
2. ADB. *Yerevan Urban Development Investment Project (RRP ARM 54172-002): Sector Assessment (Summary) — Urban Transport* (Oct–Nov 2023). Footnote 7: M-5 +9 %/yr 2016–21, M-1 +12 %/yr 2018–21; Isakov–Arshakunyats link; draft Transport Master Plan 2020–2030. https://www.adb.org/sites/default/files/linked-documents/54172-002-ssa.pdf
3. ADB. *Completion Report: Armenia — North–South Road Corridor Investment Program (Tranche 1), Loan 2561* (Jan 2020). Appendix 9: ATC records for M-1 km 20.7 and M-2 km 9.38, 2009–18; 2009 PPTA counts; traffic forecasts; junction chainages; commentary on Gyumri and Bavra. https://www.adb.org/sites/default/files/project-documents/42145/42145-023-pcr-en.pdf (project page: https://www.adb.org/projects/42145-023/main)
4. ADB / PADECO. *TA 7208-ARM: Preparing the North–South Road Corridor Development Project — Final Report* (2010). Table 4-14: RDF counts 2005–08 for M-1, M-2, M-3, M-4, M-5 and M-6. Vol. II §32: M-1 July factor. https://www.adb.org/sites/default/files/project-documents/42145-01-arm-tacr.pdf
5. Armstat. *Socio-Economic Situation of RA*, section 1.2.4 Transport: Jan–Dec 2024 (https://armstat.am/file/article/sv_12_24r_124.pdf), Jan–Dec 2025 (https://armstat.am/file/article/sv_12_25r_124.pdf) and Jan–Aug 2026 (https://armstat.am/file/article/sv_08_26r_124.pdf). Air passengers incl. foreign airlines.
6. Armstat. *Socio-Economic Situation of RA*, section 5.1: border-crossing records by checkpoint. Jan–Aug 2026: https://armstat.am/file/article/sv_08_26r_510.pdf. Jan–Dec 2024–2025: https://armstat.am/file/article/sv_12_25r_510.pdf. Jan–Aug 2025: https://armstat.am/file/article/sv_08_25r_510.pdf. Monthly cumulative 2026 (Jan–Jul): https://armstat.am/file/article/sv_0[1-7]_26r_510.pdf
7. Wikipedia. "Zvartnots International Airport": statistics table (2023 and 2024 cite Hetq, 11 Jan 2025; 2025 cites Alphanews, 22 Jan 2026); expansion and concession items. Secondary source. https://en.wikipedia.org/wiki/Zvartnots_International_Airport
8. Armstat. *Permanent population of RA as of 1 July 2026* (https://armstat.am/file/article/population_01_07_26.pdf) and *as of 1 July 2025* (https://armstat.am/file/article/population_01_07_25.pdf). Marz, town and Yerevan district tables.
9. Armstat. *Socio-Economic Situation of RA*, section 1.2.6 Services, monthly issues Jan–Dec 2025 (e.g. https://armstat.am/file/article/sv_12_25r_126.pdf; months 01–11 at the same pattern, sv_MM_25r_126.pdf) and Jan–Aug 2026 (https://armstat.am/file/article/sv_08_26r_126.pdf). NACE I "accommodation and food service" monthly turnover.
10. Coffee House Company. Branches page: 51 branches with `data-coords`, hours and regions. https://coffeehouse.am/en/branches
11. Armstat. *Marz Kotayk of RA in Figures, 2024* (statistical handbook, data 2019–2023), construction chapter: dwellings put in operation by source of financing. Copy held by the study team in the shared scratchpad; Armstat regional-statistics publication series at https://armstat.am/en/?nid=82 (exact file URL not recorded; re-locate on Armstat before citing externally).
12. Armstat. Wage database: *Average monthly nominal wages by marz*, quarterly 2018–Q2 2026 and annual 2008–2025. https://www.armstat.am/file/doc/99571903.xlsx (database page: https://www.armstat.am/en/?nid=964)
13. Armstat. *Social Snapshot and Poverty in Armenia, 2025* (ILCS 2024), Ch. 2, Table 2.1: poverty by region. https://armstat.am/file/article/poverty_2025_en_2.pdf
14. Armstat. *Statistical Yearbook of Armenia 2025*, ch. 14 Construction, Tables 14.7–14.8: dwellings put in operation, apartments. https://armstat.am/file/doc/99563703.pdf
15. Armstat. *Socio-Economic Situation of RA, Jan–Aug 2026*, section 1.2.3 Construction. https://armstat.am/file/article/sv_08_26r_123.pdf
16. Estate.am land listings (accessed 2026-10-10): category page https://www.estate.am/en/land-spots-for-sale-s369 ; listings d122385 (Abovyan), d122018 (Dzoraghbyur), d122403 (Hrazdan), d122047 (Ptghni), d122365 (Arinj), d122217 (Ajapnyak), d122404 (Nork-Marash), d112856 (Erebuni), d120669 (Arabkir). Each is at https://www.estate.am/en/land-spot-for-sale-in-<place>-<id>, e.g. https://www.estate.am/en/land-spot-for-sale-in-arinj-d122365
17. MyRealty.am land listings: https://myrealty.am/en/land-for-sale/Duryan+disrtict/Avan/Yerevan/160026 ; https://myrealty.am/en/land-for-sale/N.+Safaryan+St/Avan/Yerevan/160623 ; https://myrealty.am/en/land-for-sale/G+1+dis./Ajapnyak/Yerevan/143326
18. Kontur. *Kontur Population: Armenia*, H3 hexagons (release 2023-11-01), CC BY 4.0. https://geodata-eu-central-1-kontur-public.s3.amazonaws.com/kontur_datasets/kontur_population_AM_20231101.gpkg.gz (HDX: https://data.humdata.org/dataset/kontur-population-armenia)
19. OpenStreetMap contributors, via the Overpass API (maps.mail.ru and overpass.private.coffee mirrors). POIs (amenity fuel/cafe/fast_food/restaurant, shop convenience/supermarket/bakery/mall, drive_through) and motorway/trunk/primary/secondary roads with lanes, maxspeed, oneway and link roads. Base timestamps 2026-06-01 (Vanadzor), 2026-07-15 (M-1 north) and 2026-10-10 (other areas). ODbL. https://www.openstreetmap.org
20. Wikipedia. "Temple of Garni": visitor numbers 2013 (cites Hetq) and 2019. Secondary source. https://en.wikipedia.org/wiki/Temple_of_Garni
21. Internal workstreams: `research/B1-m4-traffic.md` (M-4 AADT estimates, M-6 2023 figure, fuel-station counts); `research/A1-macro-consumer.md` (car ownership, registered vehicles); `research/A2-coffee-market.md` (Coffee House Drive-Thru, 80–150 transactions/day benchmark); `model/assumptions.json` (placeholders).

*Derived dataset produced for this workstream: `research/data/B4-candidate-sites.csv`. It holds coordinates, Kontur 1/3/5/10 km population, OSM POI counts, nearest Coffee House and adjacent-road attributes for 35 candidate and comparator points.*
