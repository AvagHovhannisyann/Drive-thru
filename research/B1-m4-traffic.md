# B1 — Traffic volumes and road characteristics on the M-4 corridor (Yerevan – Abovyan – Hrazdan – Sevan – Dilijan)

*Prepared 2026-10-10 for the premium drive-thru feasibility study (Armenia). This is the main traffic input to the revenue driver: vehicles passing × capture rate × average ticket.*

**Status tags.** **VERIFIED**: I opened the primary or official source myself (URL given). **REPORTED**: a credible secondary source, such as news, a project-document summary or OpenStreetMap (URL given). **ESTIMATE**: my own calculation, with formula and inputs shown. **ASSUMPTION**: my judgement, with the basis explained.

**Chainage convention.** "Official km" means the M-4 kilometre post, with km 0 in central Yerevan. I derived chainage from OpenStreetMap (OSM) geometry and calibrated it against the 128 M-4 milestone nodes in OSM (64 pairs): **official km ≈ OSM chainage + 1.6 km**. The offset is consistent to ±0.2 km between km 11 and km 80. A second check is the ADB statement that the Dilijan tunnel sits at official km 80–83 [4]; OSM puts it at 79.1–81.4, which gives official 80.7–83.0.

---

## 1. Executive summary

1. **No current official AADT for any M-4 segment is publicly available.** I found no 2015–2026 count for the M-4 in ADB, EIB, World Bank, JICA or Ministry documents, or in news. The newest published **M-4** counts are Roads Department automatic-counter figures for **2005–2008** [1].
   - Yerevan exit, official km 10+320: **21,505 vehicles/day (2008)**; the peak was 25,386 in 2007, so the 2008 count is **15 % below 2007**.
   - Dilijan tunnel approach, km 80+300: **783/day (2008)**, against 2,301 in 2006. This series is erratic and has low reliability.
   (VERIFIED [1])

   *Fact-check correction: the "no post-2008 data" point applies to the M-4 only. Post-2008 counts from the same Roads Directorate network are published for the M-2 and M-1 Yerevan exits (2009–18) in ADB's January 2020 completion report [25].*
2. **Counters still run. Post-2008 data are published for the M-2 and M-1 exits, but not for the M-4.**
   - ADB's 2020 completion report publishes Roads Directorate automatic counts for 2009–18 [25]. The **M-2 Yerevan exit (km 9.38) grew 6.1 %/yr over 2008–18**, and the **M-1 exit (km 20.7) grew 5.4 %/yr over 2008–17**. Both grew about 7–8 %/yr in 2009–13/14 (VERIFIED inputs; growth rates are ESTIMATES).
   - A 2023 ADB document quotes later growth from the same network: **M-1 north of Yerevan +12 %/yr (2018–2021)** and **M-5 west of Yerevan +9 %/yr (2016–2021)** (VERIFIED [2]).
   - The M-4 series very likely exists at the Road Department Fund (RDF). **The single most valuable next step is a formal data request to RDF and the Ministry of Territorial Administration and Infrastructure (MTAI)** for monthly and hourly M-4 counts from 2009 to 2026.

   *Fact-check correction: the original said counter data were "not published" at all. That is true only for the M-4.*
3. **My 2025 estimate for the Yerevan edge (official km ~10) is 33,000–54,000 AADT two-way. The base of ≈ 42,000 is deliberately conservative** (ESTIMATE, low–medium confidence).
   - Method: the 2008 count of 21,505 grown at 2.5 / 4.0 / 5.5 % per year for 17 years.
   - The rates are bracketed by observed growth: 3.9 %/yr on Armenian M-roads in 2005–08 [1]; 6.1 %/yr at the M-2 exit (2008–18) and 5.4 %/yr at the M-1 exit (2008–17) [25]; 4.0 %/yr on the M-6 in 2014–23 [14]; 9–12 %/yr on the M-1/M-5 near Yerevan in 2016–21 [2]; and ≈5.5 %/yr growth in the registered vehicle fleet in 2006–18 [1][17].
   - **Paths anchored to comparators give more.** Indexing the M-4 to the published M-2 and M-1 exit series gives **≈44,000–55,000 (mid ≈48,000)**. Growing the 2007 count instead of the depressed 2008 one gives **≈51,000** (§3.3). The 42,000 base sits at the low end of every comparator path. The high case (54,000) is better supported than the low case (33,000), which is now a stress case.

   *Fact-check correction: (a) the original treated the 42,000 base as central, but it is grown from the lowest of the last three counts; it is kept here only as an explicitly conservative planning figure. (b) The fleet rate was originally given as ≈7 %/yr (2006–20). That figure is inflated by the one-off 2020 registrations under the EEU import regime and by Artsakh-registered vehicles; the 2006–18 trend is 5.5 %/yr.*
4. **Traffic falls sharply with distance from Yerevan** (ESTIMATE, low confidence, base case):
   - ~27,000 AADT between Abovyan and Charentsavan
   - ~21,000 around Hrazdan
   - ~17,000 from Hrazdan to Sevan
   - ~9,000 on the Sevan lakeshore bypass
   - ~5,500 from Sevan to Dilijan through the tunnel

   These segment shares are my assumptions. They follow the large junction-by-junction drop-offs that ADB **estimated** on the M-1 near Yerevan (−30 % and −57 % after the first junctions) [1]. They must be replaced by counts.

   *Fact-check correction: the original called these drop-offs "measured"; they are ADB consultant estimates. A measured M-2 pair shows km 16 carrying only 44 % of the km 9.38 volume in 2009 [25]. Decay beyond the Yerevan edge may therefore be steeper than assumed here, so the segment volumes beyond Abovyan are, if anything, optimistic relative to S1.*
5. **From the Yerevan edge to Tsovagyugh, the M-4 is a 2+2-lane dual carriageway with an extensive median guard-rail** (official km ~9–74, 64.7 km; OSM [23]).
   - The posted limit is mostly **90 km/h**, with short 60–70 km/h zones.
   - There are **9 grade-separated interchanges** between Yerevan and Sevan, plus about **18 at-grade median openings / U-turn points**.
   - From Tsovagyugh to Dilijan it is a **single carriageway with one lane each way**, through the 2,337 m tunnel (40 km/h, 4.5 m height limit).
6. **Consequence for the revenue model: a roadside site serves one direction only**, unless it sits at an interchange or median opening. Halve the two-way AADT, then apply the light-vehicle share (≈80–89 %, base 85 % [1][25]). In the base case, a site between Abovyan and Charentsavan sees about **11,600 addressable light vehicles per day on its own side** (ESTIMATE).

   *Fact-check correction: the light-vehicle share was originally 78–86 % (×0.82), giving ≈11,200. A second classified count near a Yerevan exit (M-1 km 20.7, 2009: 88.7 % light) shows that range was low (§3.5).*
7. **The side of the road decides the market.** Morning commuter coffee demand (Abovyan/Hrazdan → Yerevan) is on the **Yerevan-bound** carriageway. Weekend-morning leisure demand (Yerevan → Sevan) is on the **Sevan-bound** carriageway. The evening return flows have low coffee propensity (ASSUMPTION). A site close to Sevan relies on seasonal leisure; a site close to Yerevan relies on commuters.
8. **Seasonality is real but only partly measured.**
   - On the M-1, July traffic is **+19.7 % above AADT**, and May is close to the annual average (VERIFIED [1], Roads Department monthly data; the source does not state the period).
   - For the Sevan-dominated segments I assume July–August at 1.3–1.6× AADT and January–February at 0.6–0.8× (ASSUMPTION). The only evidence for weekend surges is a qualitative police remark from **2014**: weekend volumes to Sevan "rise significantly" in summer [13]. It gives no numbers.

   *Fact-check correction: the original cited this 12-year-old source in the present tense, with no date. The 1.5–2.5× summer-weekend factors in §3.6 are unsupported until fieldwork measures them.*
9. **No Yerevan–Sevan expressway or widening project was found for 2025–2030.** Current works are resurfacing (medium repairs): km 51+100–68+000 (16.9 km of road, 20.7 km of carriageway; AMD 1.09 bn, finishing Aug 2026) [6], km 32.6–36.0 [7] and Tsovagyugh–tunnel (under way by Sept 2026) [9]. ADB is preparing a **Dilijan tunnel rehabilitation** (proposed; the US$165 m is the ADB loan, not the total programme cost) [3][4]. It may cause multi-year traffic management on the Sevan–Dilijan link, which works against a Sevan–Dilijan site.
10. **There are disconfirming signals for an "M-4 highway site" thesis.**
    - Between Hrazdan and Sevan, volumes are probably 30–50 % of the Yerevan-edge flow; on the Sevan lakeshore, 15–30 %.
    - Entering a site from a 90 km/h carriageway needs deceleration and acceleration lanes, and permits for them.
    - The leisure peak is concentrated in about 10–14 summer weekends (ASSUMPTION).
    - OSM already shows **37 fuel stations within 200 m of the road** between the Yerevan edge and Sevan (OSM 7.5–57.7). From the Yerevan edge to the tunnel there are about 52 fuel stations and about 34 café, fast-food or restaurant outlets.
    - **A drive-thru already operates in S1.** The Coffee House Drive-Thru sits at about official km 12.8 on the Sevan-bound side (40.25929, 44.59761) and has operated since at least late 2024. It is part of a coffee cluster with Max Cafe (km 12.2, both carriageways) and Ninja coffee (km 10.5) (VERIFIED in sibling workstream A3 [27]).

    *Fact-check correction: the original omitted this incumbent, the most decision-relevant competitor on the corridor.*
11. **Before any land commitment:** run a 2-season, 6-station classified count with ANPR matching, plus intercept surveys at existing fuel/café stops (protocol in §5; budget ≈ US$18–35k, an ASSUMPTION to be quoted). In parallel, request the RDF counter data and Road Police speed-camera (ANPR) counts. OSM shows at least 7 enforcement cameras on the dual-carriageway section.

---

## 2. Key data table

| # | Metric | Value | Period | Status | Source |
|---|---|---|---|---|---|
| 1 | AADT, M-4 Yerevan exit (official km 10+320, near Verin Ptghni / Yerevan boundary) | 19,484 / 22,877 / 25,386 / **21,505** veh/day | 2005 / 2006 / 2007 / 2008 | VERIFIED | [1] Table 4-14 (Armenian Roads Directorate) |
| 2 | AADT, M-4 km 80+300 (Dilijan tunnel south approach) | 1,455 / 2,301 / 961 / **783** veh/day (erratic) | 2005–2008 | VERIFIED (low reliability) | [1] Table 4-14 |
| 3 | Comparable AADTs, 2008: M-1 km 20+700; M-5 km 9+400; M-2 km 9+380 | 11,620; 21,471; 20,965 | 2008 | VERIFIED | [1] |
| 4 | Average growth at Armenian M-route count stations | 3.9 %/yr (+12 %, +7 %, −5 % year on year) | 2005–2008 | VERIFIED | [1] §37, §155 |
| 5 | Traffic growth, M-1 just north of Yerevan | +12 %/yr | 2018–2021 | VERIFIED (ADB citing counts) | [2] fn 7 |
| 6 | Traffic growth, M-5 just west of Yerevan | +9 %/yr | 2016–2021 | VERIFIED | [2] fn 7 |
| 6a | Post-2008 counter AADT at comparable exits: M-2 km 9.38; M-1 km 20.7 | M-2: 23,406 (2009), 33,163 (2014), 32,386 (2017), 37,831 (2018) → **6.1 %/yr 2008–18** (7.2 %/yr 2009–14). M-1: 12,384 (2009), 16,697 (2013), 18,635 (2017) → **5.4 %/yr 2008–17** (7.8 %/yr 2009–13) | 2009–2018 | VERIFIED (counts, fact-check) / ESTIMATE (CAGR) | [25] ATC records 2009–18. *Fact-check correction: row added; the original said no post-2008 counts were published* |
| 7 | M-6 Vanadzor–Bagratashen traffic (after reconstruction) | 2,800 → 4,000 cars/day (+4.0 %/yr) | 2014 → 2023 | VERIFIED (Government) | [14] |
| 8 | July traffic vs AADT, M-1 automatic counter km 20.7; May ≈ AADT | +19.7 % (factor 0.835 to AADT) | ARD monthly data (period not stated in the source; ~2005–09 is my inference) | VERIFIED | [1] Vol. II §32 |
| 9 | Peak-hour share of daily traffic, M-2 km 16 near Yerevan (comparable) | 7.8 % (5.9–7.7 % at other M-2 sites) | May/Oct 2009 | VERIFIED | [1] Table 4-15 |
| 10 | Vehicle mix, M-2 km 16 (comparable for the M-4 Yerevan exit) | Cars 74.3 %, pickups 7.7 %, minibuses 6.7 %, buses 1.3 %, trucks 10.0 % | 2009 | VERIFIED | [1] Table 4-15 |
| 10a | Vehicle mix, M-1 km 20.7 (Yerevan exit) | Cars 83.0 %, pickups 5.7 % (light vehicles 88.7 %); peak hour 8.1 % | 23 Jul 2009 | VERIFIED (fact-check) | [1] Vol. II Table 3-1. *Fact-check correction: row added; the original called M-2 km 16 the only such count* |
| 11 | Registered vehicles, Armenia | 330,000 (end-2006) → 630,170 (2018) → 850,691 (2020). The 2020 figure includes 32,446 Artsakh-registered vehicles and a one-off 34 % jump after the 2020 switch to a single EEU import tax. **Underlying trend 2006–18: 5.5 %/yr** | 2006, 2018, 2020 | VERIFIED [1] (2006, est.) / REPORTED [17] (2018, 2020) | [1] Tbl 3-2; [17] Tbl 2. *Fact-check correction: the original tagged [17] VERIFIED and implied 7 %/yr* |
| 12 | Registered vehicles, Kotayk / Gegharkunik / Tavush / Yerevan | 68,499 / 53,979 / 33,379 / 319,626 | 2020 | REPORTED (UNDP-EU donor report compiling Traffic Police data) | [17] Tbl 3. *Fact-check correction: retagged from VERIFIED* |
| 13 | **Estimated AADT, Yerevan edge (km ~10)** | **33,000–54,000 (base 42,000, explicitly conservative; comparator-anchored paths give ≈44,000–55,000, mid ≈48,000)** | 2025 | ESTIMATE | §3.3. *Fact-check correction: base labelled conservative; comparator range added* |
| 14 | **Estimated AADT, Abovyan–Charentsavan (km 17–31)** | **18,000–40,000 (base 27,000)**; M-2 decay analogue (44 %) gives ≈18,500, a downside | 2025 | ESTIMATE | §3.4 |
| 15 | **Estimated AADT, Hrazdan E – Sevan W (km 48–59)** | **10,000–27,000 (base 17,000)** | 2025 | ESTIMATE | §3.4 |
| 16 | **Estimated AADT, Tsovagyugh–Dilijan (tunnel)** | **2,600–10,800 (base 5,500)** | 2025 | ESTIMATE | §3.4 |
| 17 | Cross-section, Yerevan edge → Tsovagyugh (official km ~9.1–73.9) | Dual carriageway, 2 lanes/direction (3 lanes on ~2 km) | Oct 2026 OSM | REPORTED (OSM) | [23] |
| 18 | Cross-section, Tsovagyugh → Dilijan (official km ~73.9–95.9) | Single carriageway, 1 lane/direction | Oct 2026 OSM | REPORTED (OSM) | [23], [22] (1st class to tunnel, 2nd class after) |
| 19 | Posted speed limit, dual-carriageway section | 90 km/h on 60.4 of 64.7 km (Sevan-bound); 60–70 km/h zones near Yerevan edge, Charentsavan, Varser, Tsovagyugh | Oct 2026 OSM | REPORTED (OSM) | [23] |
| 20 | Grade-separated interchanges, Yerevan edge → Sevan (km 9–60) | 9 full + 3 partial | Oct 2026 OSM | ESTIMATE (from OSM) | §3.8 |
| 21 | At-grade median openings / U-turns (Yerevan edge → Tsovagyugh) | ~18 locations (~28 crossover links) | Oct 2026 OSM | ESTIMATE (from OSM; may be incomplete) | §3.8 |
| 22 | Dilijan (Sevan) tunnel | 2,337 m; 40 km/h; maxheight 4.5 m; official km 80–83 | OSM Oct 2026; ADB Nov 2025 | REPORTED (OSM) / VERIFIED (ADB km) | [23], [4] |
| 23 | Elevation, Yerevan start → Sevan → tunnel → Dilijan | 1,049 m → ~1,925 m → ~2,010 m → ~1,260 m; Abovyan–Charentsavan climb averages +2.8 % (1 km maxima ~6 %); tunnel–Dilijan descent averages −5.3 % | SRTM 90 m | ESTIMATE | [24] |
| 24 | M-4 medium repair, km 51+100–68+000 (Gagarin – Sevan) | 16.9 km of road (16.9 km left carriageway + 3.8 km right = 20.7 km in total), AMD 1,089.3 m, 237,721 m², ~65 % done, finishing late Aug 2026 | 24 Jul 2026 | REPORTED | [6]. *Fact-check correction: the original gave 20.7 km as the road length; it is carriageway length* |
| 25 | M-4 night closures, km 32+580–36+000 (Charentsavan–Kaghsi), Sevan-bound | 20:00–08:00 from 10 Jun 2026; traffic moved to the opposite carriageway | Jun 2026 | REPORTED | [7], [8] |
| 26 | ADB RIRSIP II (Pushkin + Dilijan tunnels, M-6) | US$165 m ADB loan (not the total programme cost), *proposed*; concept 7 Oct 2024; fact-finding 24 Nov–12 Dec 2025 | 2024–2026 | VERIFIED | [3], [4] |
| 27 | Old ADB plan: M-4 Yerevan–Sevan–Dilijan widening, grade separation (118 km) | US$131.5 m (not implemented as a package; no current project found) | ADB TSDS 2020 (c. 2008–09) | REPORTED (cited in ADB TA 7208 §120; TSDS not opened) | [1] §120. *Fact-check correction: retagged from "VERIFIED (as cited)"* |
| 28 | PM statement on congestion | "traffic congestion on interstate highways has already become commonplace"; vehicles exceed road capacity | 6 Aug 2026 | REPORTED | [12] |
| 29 | Fuel stations within 200 m of the M-4 | 37 between Yerevan edge and Sevan W (OSM 7.5–57.7); 10 on Sevan–Tsovagyugh; 5 Tsovagyugh–tunnel; 3 tunnel–Dilijan (55 from the Yerevan edge to Dilijan; 74 including the urban section) | Oct 2026 OSM | REPORTED (OSM; incomplete) | [23]. *Fact-check: A3 cites 60 and B2 cites 40 merged sites (150 m, km 10.2–74.3); the differences are in scope and buffer; see §3.10* |
| 30 | Recent accident example | Minibus rollover, km 50, 8 injured | 8 Oct 2026 | REPORTED | [11] |
| 31 | Existing drive-thru and coffee cluster on the M-4 (S1) | Coffee House Drive-Thru, official km ~12.8, Sevan-bound side (40.25929, 44.59761), open since ≤ late 2024; Max Cafe km 12.2 (both carriageways); Ninja coffee km 10.5 (Sevan-bound) | Oct 2026 | VERIFIED (in A3: company branch list) | [27]. *Fact-check correction: row added; the original omitted the incumbent* |

---

## 3. Detailed findings and analysis

### 3.1 What official traffic data exist, and why the gap matters

**Roads Department automatic counters (2005–2008).** The ADB TA 7208 final report (PADECO, 2010) reproduces the Armenian Roads Directorate's automatic counter data: ten counters on six interstate routes [1]. The M-4 had two:

| Counter | Location (my interpretation) | 2005 | 2006 | 2007 | 2008 | CAGR 2005–08 |
|---|---|---|---|---|---|---|
| M4 10+320 | Yerevan city boundary at Verin Ptghni (OSM ≈ 8.7 km). This is the "city exit" screenline toward Abovyan / Sevan | 19,484 | 22,877 | 25,386 | 21,505 | +3.3 %/yr (+14 %/yr in 2005–07; −15 % in 2007–08) |
| M4 80+300 | South approach to the Dilijan tunnel (OSM ≈ 78.7 km) | 1,455 | 2,301 | 961 | 783 | erratic |

Source: [1] Table 4-14 (VERIFIED). The report says a figure "Interstate Roads Traffic Volume 2008" showed AADT on every interstate section. I checked every image page of the 186-page PDF and the figure is **not** in the public file. The segment-by-segment 2008 map therefore remains unavailable (GAP).

Interpretation:
- The Yerevan-exit series looks plausible overall, but **2008 is 15 % below 2007** (21,505 / 25,386 − 1 = −15.3 %). Across the network, M-route traffic fell only 5.2 % in 2007–08 (91,766 → 86,977) [1]. The M-4 drop is about three times the network decline, and part of it may be a counter anomaly. Because §3.3 grows only from the 2008 value, the base rests on the lowest of the last three counts (see the base-year sensitivity in §3.3).
  *Fact-check correction: the original said 2008 was "slightly below" 2007.*
- The Dilijan-tunnel series swings by a factor of 3 between years. This is typical of counter faults or partial-year data. I treat it as a **lower bound** only.
- In 2008 the M-4 Yerevan exit was the **busiest counter in the country** (21,505), essentially tied with the M-5 (21,471) and M-2 (20,965) exits and almost double the M-1 exit (11,620) [1]. It was also the busiest in 2007 (25,386, against 24,551 on the M-2 and 23,202 on the M-5).
  *Fact-check correction: the original said "second-busiest".*

**Evidence that counting continues.** ADB's 2023 sector assessment for the Yerevan Urban Development Investment Project states: "Traffic on the M5 western corridor just west of the city boundary grew by 9 % per year in 2016–2021. Traffic on the M1 just north of the city grew at 12 % per year in 2018–2021" [2] (VERIFIED). These figures can only come from continuing RDF/MTAI counter data. The same document says "recent urban traffic estimates are not available" and cites a draft MTAI **Transport Master Plan 2020–2030** (2021) [2]. That plan very likely contains M-4 volumes, but it is not public (GAP).

**Published post-2008 counts at comparable Yerevan exits.** ADB's completion report for the North–South corridor programme, tranche 1 (Jan 2020) [25], publishes Roads Directorate automatic traffic counts for 2009–18:

| Counter | 2009 | 2013 | 2014 | 2017 | 2018 | Growth |
|---|---|---|---|---|---|---|
| M-2 km 9.38 (Yerevan exit; 2008 = 20,965) | 23,406 | — | 33,163 | 32,386 | 37,831 | +7.2 %/yr 2009–14; **+6.1 %/yr 2008–18** |
| M-1 km 20.7 (Yerevan exit; 2008 = 11,620) | 12,384 | 16,697 | — | 18,635 | — | +7.8 %/yr 2009–13; **+5.4 %/yr 2008–17** |

Counts are VERIFIED (fact-check opened [25]); growth rates are ESTIMATES. The report has no M-4 series, so the narrower claim stands: no post-2008 **M-4** count is published.

*Fact-check correction: the original treated all post-2008 counter data as unpublished and assumed 2009–15 stagnation. These published series show sustained growth of about 7 %/yr at the two comparable exits in 2009–14.*

**Government statements without M-4 numbers.**
- The Prime Minister's 2024 report gives a single figure: M-6, 2,800 → 4,000 cars/day, 2014 → 2023 [14] (VERIFIED).
- In August 2026 the PM said congestion on interstate highways "has already become commonplace" and that vehicle numbers exceed road capacity, but gave no M-4 figures [12] (REPORTED).

**What I searched without success.** Searches covered English, Armenian ("երթևեկության ինտենսիվություն", "Երևան-Սևան ճանապարհ") and Russian ("интенсивность движения трасса Ереван Севан"). They found **no** news item, police release or ministry figure giving vehicle counts on the Yerevan–Sevan road or "X thousand cars to Sevan" on a weekend. Police releases in 2020–21 report weekend enforcement statistics only (e.g., drunk drivers), not volumes. ADB 58405 IEEs (Nov 2025), ADB 56317 RRP (Nov 2024) and the EU/World Bank TEN-T Indicative Action Plan brochure also contain no M-4 counts.

### 3.2 Growth evidence for bridging 2008 → 2025/26

| Indicator | Value | Period | Status | Source |
|---|---|---|---|---|
| M-route counter growth (network) | 3.9 %/yr | 2005–08 | VERIFIED | [1] |
| M-4 Yerevan exit counter | +3.3 %/yr (2005–08), +14 %/yr (2005–07), −15 % (2007–08) | 2005–08 | VERIFIED (calc.) | [1] |
| M-2 Yerevan exit counter (km 9.38) | +6.1 %/yr (20,965 → 37,831); +7.2 %/yr in 2009–14 | 2008–18 | ESTIMATE from VERIFIED counts (fact-check) | [25] |
| M-1 Yerevan exit counter (km 20.7) | +5.4 %/yr (11,620 → 18,635); +7.8 %/yr in 2009–13 | 2008–17 | ESTIMATE from VERIFIED counts (fact-check) | [25] |
| M-6 Vanadzor–Bagratashen | +4.0 %/yr (2,800→4,000); a weak analogue, since it is a newly reconstructed border road | 2014–23 | VERIFIED | [14] |
| M-5 west of Yerevan | +9 %/yr | 2016–21 | VERIFIED | [2] |
| M-1 north of Yerevan | +12 %/yr | 2018–21 | VERIFIED | [2] |
| Registered fleet | **330,000 → 630,170 = +5.5 %/yr (underlying trend)**. Excluding Artsakh vehicles, 2006–20 is +6.7 %/yr; including them, 330,000 → 850,691 = +7.0 %/yr, which is inflated | end-2006 → 2018 (2020) | ESTIMATE from VERIFIED [1] and REPORTED [17] inputs; definitions may differ (registered vs active) | [1], [17]. *Fact-check correction: 2020 includes 32,446 Artsakh-registered vehicles and a 34 % one-off jump from the 2020 EEU single import tax, which "cannot increase at the same rate after 2020" [17]; use ≈5.5 %/yr* |
| Real GDP | +6.8 % avg 2017–19; −7.2 % 2020; +5.8 % 2021; +12.6 % 2022; +8.3 % 2023 (≈ +46 % 2016→2023) | 2017–23 | VERIFIED | [5] |
| Vehicle numbers "roughly one million by some estimates" | ~1.0 m (no source named; not used as a bound) | Dec 2025 | REPORTED (weak; newspaper) | [19] |
| Transport demand elasticity | Low before 2008: GDP per capita +17.5 %/yr in AMD vs traffic +3.9 %/yr | 2001–08 | VERIFIED | [1] §37 |

**How I read this.**
- Growth at the Yerevan exits has been sustained, not just recent:
  - about 7–8 %/yr in 2009–13/14 at the M-2 and M-1 exits [25];
  - 5.4–6.1 %/yr over 2008–17/18 [25];
  - 9–12 %/yr in 2016–21 [2].

  *Fact-check correction: the original said 2008–16 growth was "much slower" because of 2009–15 stagnation. The published counts [25] contradict that.*
- Applying 9–12 % to the whole 2008–2025 span would still be wrong. However, 5–6 %/yr over 2008–18 is observed at two comparable exits.
- The 2022–23 influx of people and capital from Russia raised Yerevan-area traffic [5]. Part of that effect has since faded.

### 3.3 Estimating 2025 AADT at the Yerevan edge (screenline S1)

**Formula:** AADT₂₀₂₅ = AADT₂₀₀₈ × (1 + g)^17, with AADT₂₀₀₈ = 21,505 [1].

| Scenario | g (%/yr) | Rationale | AADT 2025 | AADT 2026 |
|---|---|---|---|---|
| Low | 2.5 | **Stress case.** Below the 2005–08 network rate and below every published comparator; reflects only peak-hour capacity limits. *Fact-check correction: the original "2009–15 stagnation" rationale was removed, because published counts show ~7 %/yr growth in 2009–14 [25]* | 32,700 | 33,500 |
| Base | 4.0 | **Conservative.** Equal to the 2005–08 M-route rate (3.9 %) and the 2014–23 M-6 rate (4.0 %), but below the 5.4–6.1 %/yr observed at the M-1 and M-2 exits over 2008–17/18 [25]. *Fact-check correction: the original "mid-way between low-growth 2008–15 and high-growth 2016–23" rationale was removed* | 41,900 | 43,600 |
| High | 5.5 | Close to the M-1/M-2 exit rates over 2008–17/18 (5.4–6.1 %/yr) [25] and the 2006–18 fleet trend (5.5 %/yr). Consistent with 9–12 %/yr near Yerevan since 2016. *Fact-check correction: originally "about 0.8 × fleet growth (7 %/yr)"; the 7 % fleet rate is inflated* | 53,400 | 56,400 |

**Status:** ESTIMATE, low–medium confidence. **Range used: 33,000–54,000; base 42,000 (2025). The base is explicitly conservative.**

**Base-year and comparator sensitivity (ESTIMATE, added at fact-check).**

| Path | Formula | AADT 2025 |
|---|---|---|
| 2007 base instead of 2008, at 4 %/yr | 25,386 × 1.04^18 | ≈51,400 |
| M-4 indexed to the M-2 exit to 2018, then 3–5 %/yr | 21,505 × 37,831 / 20,965 = 38,800 (2018); × 1.03^7 to × 1.05^7 | ≈47,700–54,600 |
| M-4 indexed to the M-1 exit to 2017, then 3–5 %/yr | 21,505 × 18,635 / 11,620 = 34,500 (2017); × 1.03^8 to × 1.05^8 | ≈43,700–51,000 |

Every comparator-anchored path lands between 44,000 and 55,000 (mid ≈48,000). I keep **42,000 as the planning base** for two reasons. First, it is conservative for a land decision. Second, decay beyond the Yerevan edge may be steeper than assumed (§3.4), which offsets part of the S1 upside further out. An investor who uses ≈48,000 instead would raise the S1 flows by about 14 %. The RDF data request remains essential either way.

*Fact-check correction: the original presented 42,000 as a central estimate, grown from a 2008 value that is 15 % below 2007. The comparators support a higher number.*

**Cross-check by fleet growth (ESTIMATE).**
- Inputs:
  - The fleet was about 363k at end-2008, linearly interpolated from ADB's 330k at end-2006 and 380k at end-2009 [1].
  - It reached about 0.85–1.0 m in 2020–25 [17][19].
  - That is a factor F ≈ 2.3–2.7.
  - The traffic-to-fleet elasticity e is 0.6–0.8 (ASSUMPTION; many registered vehicles are inactive or re-exported).
- Formula A, traffic factor = F^e: 2.3^0.6 = 1.65 to 2.7^0.8 = 2.21, which gives 21,505 × factor = **35,400–47,600**.
- Formula B, traffic factor = 1 + e × (F − 1): 1.78 to 2.36, which gives **38,300–50,800**.
- **Result: about 35,000–51,000.** This is a wide band, not a tight confirmation of the 42,000 base.
- Both fleet endpoints are weak. The 0.85 m figure (2020) is inflated by one-off EEU import registrations and Artsakh vehicles [17]. The 1.0 m figure is an unsourced newspaper estimate [19].

*Fact-check correction: the original used 370k for 2008, showed no formula, gave a factor of 1.8–2.2 and a result of 39,000–47,000, and called it "consistent with the base case".*

**Capacity sanity check (ESTIMATE).**
- The section has 2 lanes per direction, with at-grade side accesses near Yerevan.
- Practical capacity is about 1,700–1,900 veh/h/lane (ASSUMPTION, typical for multilane highways with roadside friction), or about 3,600 veh/h per direction.
- With a peak-hour share K = 7.8 % [1] and a peak-direction share D = 0.58 (ASSUMPTION), the base 42,000 AADT gives about 1,900 veh/h in the peak direction. That is about 53 % of capacity on an average day. At the comparator-anchored 48,000 it would be about 2,170 veh/h, or 60 %.
- Summer Sunday-evening inbound peaks at 1.5–2× average would reach saturation. This fits the PM's "congestion commonplace" remark [12], although that remark is not M-4 specific.

### 3.4 Segment profile Yerevan → Dilijan (ESTIMATE)

**Method.**
- Segment AADT = share × Yerevan-edge AADT.
- The shares are **ASSUMPTIONS**. They draw on three things:
  - ADB's **estimated** drop-offs on the M-1 near Yerevan: volume after the Ashtarak junction was 70 % of the section before, and 43 % after the M-3 intersection [1] Vol. II §33. These are consultant estimates, not counts;
  - catchment sizes from Armstat at 1 Oct 2025 [26]: Abovyan 51.0k; Byureghavan 11.9k; Nor Hachn 10.4k; Charentsavan 24.1k; Hrazdan 49.8k; Sevan 19.6k. For Dilijan I use 17,045 (OSM tag, vintage unverified; not in the B2 extract);
  - the regional fleets of Kotayk (68,499), Gegharkunik (53,979) and Tavush (33,379) [17] (REPORTED).
- *Fact-check correction (decay).* The original called the 70 %/43 % shares "ADB-measured". The measured pairs point to faster decay than the 65 % base share for S2, although Abovyan itself sits at about km 16 on the M-4:
  - the only measured M-1 pair is km 20.7 (16,582) against km 30 (6,165), which is 37 % [1] Vol. II Table 3-1;
  - on the M-2, "traffic at km16 was 44 % of that at km9.38 in 2009" [25] ¶14, a 56 % drop within about 7 km of the Yerevan edge.

  Treat 44 % as a downside cross-check for S1 → S2: 0.44 × 42,000 ≈ 18,500, close to the S2 low case.
- *Fact-check correction (populations).* The original used OSM tags (Abovyan 45,025; Byureghavan 9,142; Nor Hachin 9,197; Charentsavan 20,368; Hrazdan 39,957; Sevan 18,870). These were 12–20 % below Armstat 2025. The impact is low, because the shares are judgement-based.
- The low case pairs the low share with the low screenline (33k). The high case pairs the high share with the high screenline (54k). This deliberately gives wide ranges.

| Seg | Official km (approx.) | Description | Share of S1 (low / base / high) | AADT 2025 two-way (low – **base** – high) | Per direction, base | Light vehicles per direction, base (×0.85; was ×0.82) |
|---|---|---|---|---|---|---|
| S1 | 9–16 | Yerevan edge → Abovyan interchanges | 100 % | 33,000 – **42,000** – 54,000 | 21,000 | ~17,900 (was ~17,200) |
| S2 | 17–31 | Abovyan → Charentsavan (climb +2.8 %) | 55 / 65 / 75 % | 18,200 – **27,300** – 40,500 | 13,650 | ~11,600 (was ~11,200) |
| S3 | 32–39 | Charentsavan → Hrazdan W | 50 / 60 / 70 % | 16,500 – **25,200** – 37,800 | 12,600 | ~10,700 (was ~10,300) |
| S4 | 40–47 | Through Hrazdan (3 interchanges) | 40 / 50 / 60 % | 13,200 – **21,000** – 32,400 | 10,500 | ~8,900 (was ~8,600) |
| S5 | 48–59 | Hrazdan E → Sevan W (Gagarin, Varser) | 30 / 40 / 50 % | 9,900 – **16,800** – 27,000 | 8,400 | ~7,100 (was ~6,900) |
| S6 | 60–73 | Sevan lakeshore bypass → Tsovagyugh | 15 / 22 / 30 % | 5,000 – **9,200** – 16,200 | 4,600 | ~3,900 (was ~3,800) |
| S7 | 74–96 | Tsovagyugh → tunnel → Dilijan (single carriageway) | 8 / 13 / 20 % | 2,600 – **5,500** – 10,800 | 2,700 | ~2,300 (was ~2,200) |

*Fact-check correction: I recomputed the last column at a light-vehicle share of 85 %, up from 82 % (+3.7 %; see §3.5). The two-way AADT columns are unchanged. If S1 is re-anchored to the comparator-based ≈48,000 (§3.3), all columns scale by about 1.14. If decay follows the M-2 analogue, S2 and beyond fall toward the low shares.*

**Cross-check, S7.** The 2005–08 tunnel counts (783–2,301), grown by a factor of 1.5–2.5, give 1,200–5,700. My S7 range overlaps this but the base (5,500) sits at its top. I keep 5,500 as base for three reasons, all ASSUMPTIONS: Dilijan's growth as a resort and education hub (e.g., the Central Bank and UWC campuses); higher Armenia–Georgia/Russia road trade since 2022; and the fact that the 2008 counter data look faulty. **Conflict flagged: trust neither number until counted.**

**Seasonal and weekly adjustment for the model.** See §3.6. The S5–S7 segments are leisure-dominated, and their summer-weekend peaks may be 2–3 times a winter weekday. A site there needs seasonal staffing and should not be sized on AADT alone.

### 3.5 Directional split, peak hour, vehicle mix

- **Daily directional split:** about 50/50 over 24 h on a commuter/leisure corridor, because most trips return the same day (ASSUMPTION). Peak-hour directional splits are likely 55–65 % (ASSUMPTION):
  - weekday AM: Yerevan-bound on S1–S4;
  - weekend AM: Sevan-bound on S1–S6;
  - Sunday PM: Yerevan-bound.
- **Peak-hour factor:** 7.8 % of daily traffic at M-2 km 16 near Yerevan, 8.1 % at M-1 km 20.7 (Jul 2009), and 5.9–7.7 % on rural M-2 sections (2009 counts) [1] (VERIFIED, comparable roads). For the model, use 7.5–9 % for S1–S3 and 6–8 % for rural segments on weekdays (ASSUMPTION). Weekend leisure peaks are sharper.
- **Vehicle mix:** there are at least two Armenian classified counts near Yerevan exits.
  - M-2 km 16 (2009): cars 74.3 %, pickups 7.7 %, minibuses 6.7 %, buses 1.3 %, 2-axle trucks 3.6 %, 3-axle 4.2 %, 4+ axle 2.2 % [1] Table 4-15 (VERIFIED, comparable).
  - **M-1 km 20.7 (23 Jul 2009):** cars 83.0 % + pickups 5.7 % = **88.7 % light vehicles**; peak hour 8.1 % [1] Vol. II Table 3-1 (VERIFIED at fact-check).
  - The automatic-counter records in [25] put light vehicles at 92 % (M-2 km 9.38, 2018) and 97 % (M-1 km 20.7, 2017). The ATC classes probably include minibuses, so these are not strictly comparable.
  - The M-2 carries Iran-bound freight, so the M-4 truck share is probably similar or lower. Heavy users on the M-4 are the Hrazdan cement and power plants, Sevan, and Georgia-bound traffic via Dilijan (ASSUMPTION).
  - **Addressable light vehicles (cars + pickups/SUVs) ≈ 80–89 %** of AADT, **base 85 %** (ASSUMPTION based on [1][25]).

  *Fact-check correction: the original called M-2 km 16 "the only" classified count near a Yerevan exit and used 78–86 % (×0.82). That range sat below every other Yerevan-exit observation. The per-direction flows in §3.4 and §4.2 are recomputed at ×0.85 (+3.7 %).*
  - Minibuses (marshrutkas), about 7 %, are unlikely drive-thru customers. Yerevan–Sevan minibuses run about every 15–30 min in season (travel blogs; not verified).
- **Rail competition:** a weekend summer electric train Yerevan–Sevan–Shorzha has run since June 2022, with 1 return trip per day and fares of AMD 600–1,000 [20] (REPORTED). Its modal impact is negligible.

### 3.6 Weekday vs weekend, summer vs winter

| Factor | Value | Status | Basis |
|---|---|---|---|
| May ≈ AADT on interstate roads | ~1.00 | VERIFIED | [1] (RDF monthly data) |
| July / AADT, M-1 km 20.7 | 1.197 | VERIFIED | [1] |
| July–Aug / AADT, S1–S3 (commuter + leisure) | 1.15–1.30 | ASSUMPTION | M-1 anchor plus Sevan leisure overlay |
| July–Aug / AADT, S5–S7 (leisure-dominant) | 1.30–1.60 | ASSUMPTION | Lake Sevan is the principal summer destination for Yerevan residents; police reported a strong summer-weekend rise in **2014** (qualitative, no numbers) [13] |
| Jan–Feb / AADT, S1–S3 | 0.80–0.90 | ASSUMPTION | Snow events at Abovyan/Sevan [18]; road stays open |
| Jan–Feb / AADT, S5–S7 | 0.60–0.80 | ASSUMPTION | Low tourism; tunnel open year-round |
| Weekend day / weekday, S1–S3 | 0.85–1.05 (summer weekends up to 1.3) | ASSUMPTION | Commuting replaced by leisure |
| Summer weekend day / summer weekday, S5–S7 | 1.5–2.5 | ASSUMPTION (unsupported) | The only evidence is a qualitative police remark from 2014 [13]. *Fact-check correction: treat as unsupported until the §5 fieldwork measures it; do not size capacity or staffing on it* |

**There is no measured weekday/weekend or monthly profile for the M-4** (GAP). The fieldwork in §5 is designed to measure it.

### 3.7 Road geometry by segment (OSM, data timestamp 2026-10-10 09:41 UTC [23])

| Segment (official km) | Carriageway | Lanes / direction | Posted speed (OSM) | Junction type | Other |
|---|---|---|---|---|---|
| Yerevan urban: Heratsi → Myasnikyan Ave → Acharyan St (~1.6–9.1) | Dual, kerb/jersey median (≈3 km mapped) | 3 (short 2- and 4-lane bits) | 60 (70 on 0.7 km) | At-grade, **≥6 signalised junctions** (Tsarav Aghbyur, Acharyan 1st lane, Babajanyan, Acharyan 2nd lane, Mashtots), several grade-separated ramps on Myasnikyan | Many fuel stations (19 within 200 m); urban congestion |
| Yerevan edge → Abovyan (9.1–16) | Dual | 2 (3 on ~1 km) | 60 → 90 | Grade-separated at 9.1, 11.1, 15.7, 16.7; side accesses at 10.2, 13.0, 14.8 | ADB counter site at km 10.3; Yerevan sign at OSM 8.65 |
| Abovyan → Charentsavan (17–31) | Dual, median guard-rail | 2 | 90 (70 on ~5.2 km Yerevan-bound, official km ~23.7–28.9) | **5 median openings** (18.1, 19.3, 22.4, 25.9, 28.0); slip ramps at 21.5 | Sustained climb: 1,400 → 1,840 m, average +2.8 %, 1 km maxima 5–6 % |
| Charentsavan → Hrazdan (31–39) | Dual | 2 | 90 | Grade-separated at 31.1 (Fantan/Charentsavan); **no median opening, no fuel station on ~8 km** | Night closures km 32.6–36.0 in Jun 2026 [7] |
| Hrazdan (39–48) | Dual | 2 | 90 | Grade-separated at 39.3 (Hrazdan), partial 43.2, full 47.4 (Hrazdan East) | Speed cameras OSM 38.9 and 43.3 |
| Hrazdan E → Sevan W (48–60) | Dual | 2 | 90 (70 on ~1.6 km at Varser) | Median openings 48.6, 51.0, 51.5, 52.9, 57.1; grade-separated 54.3 (Gagarin/Tsaghkunk), 59.4 (Sevan W / Lchashen) | Highest fuel density (13 stations in 10 km); resurfacing km 51.1–68.0 (2026) [6] |
| Sevan lakeshore → Tsovagyugh (60–74) | Dual (ends at ~73.9) | 2 | 90 (70 on ~0.7 km Yerevan-bound) | Mostly at-grade: openings 61.4, 63.5, 64.7, 66.7, 72.1, 73.0; slip ramps 63.0, 63.5 | Restaurant strip on lake side (13 F&B outlets on Tsovagyugh-bound side vs 3 opposite) |
| Tsovagyugh → tunnel (74–80.7) | **Single** | 1 | 90 → 70 → 50 | At-grade (Semyonovka old-pass road at 73.9) | Climb to ~2,010 m |
| Dilijan tunnel (80.7–83.0) | Single bore | 1 | 40 | — | 2,337 m, height limit 4.5 m, lit; ADB rehab proposed [3][4] |
| Tunnel → Dilijan (83–96) | Single | 1 | 90 / 60 urban | At-grade (Semyonovka N 83.9; T-10-23 91.8) | Descent averages −5.3 % (SRTM); 47 F&B outlets near Dilijan |

**Median barrier.** OSM maps 24.4 km of guard-rail that I could classify as median, meaning both carriageways lie within 40 m on its left. It maps a further 33 km of guard-rail near the carriageways but unclassified, likely median where the carriageways separate. This is along the 51 km Yerevan edge–Sevan section, and the Sevan–Tsovagyugh stretch adds 4.3 km median plus 11.1 km unclassified (ESTIMATE from [23]). **Practical reading:** the median is largely barriered, and crossings are possible only at the openings and interchanges listed. **Verify on the ground**: OSM barrier mapping is incomplete, and some openings may have been closed for safety.

**Winter.** All interstate roads remained open during the late-December 2025 snowfall, with snow reported at Abovyan and Sevan and crews clearing and sanding [18] (REPORTED). The tunnel is the year-round route. The old Sevan pass road (Semyonovka) is a seasonal mountain road; ADB's description of the analogous Pushkin pass bypass says it is usable only in summer [4]. I found **no record of winter closures of the M-4 Yerevan–Sevan section** in the sources reviewed (GAP: request the Rescue Service / RDF closure log).

**Toll status.** The M-4 is not tolled; OSM tags toll=no on the Dilijan streets [23]. No toll plan was found. ADB studied tolling only for the North–South corridor in 2010 [1].

**Speed enforcement (OSM).** Cameras are tagged at OSM km 14.9 (90), 16.6 (90), 27.1 (70), 38.9, 43.3 (90, both directions), 57.7 (70, both directions), 78.9 (50), 89.6 (50) and 93.2 (50) [23] (REPORTED). These cameras are a potential **source of vehicle counts** if Road Police data can be obtained.

### 3.8 Junction table, km chainage and coordinates (OSM [23]; official km = OSM + 1.6)

"GS" means grade-separated (ramps on both carriageways). "MO" means an at-grade median opening (U-turn or crossing). "Side" means right-in/right-out access to one carriageway only. The motorway_junction exit refs are those mapped in OSM.

| # | Official km (≈) | OSM km | Lat, Lon | Type | Place / roads | Notes |
|---|---|---|---|---|---|---|
| 1 | 9.1–9.5 | 7.53–7.90 | 40.2379, 44.5637 | GS + 2 MO | Yerevan city edge (Avan/Arinj); exit ref 0 | Acharyan St becomes the Yerevan–Dilijan Hwy; speed changes 60/70 → 90 |
| 2 | 10.2 | 8.57–8.65 | 40.2426, 44.5743 | Side + bridge | T-6-8, Verin Ptghni; Yerevan boundary | Site of 2005–08 RDF counter (km 10+320) |
| 3 | 11.1–11.9 | 9.47–10.33 | 40.2470, 44.5832 | GS (bridge 9.80) | Exits 2–3, Verin Ptghni / Ptghni | 4 ramps |
| 4 | 13.0 | 11.43 | 40.2604, 44.5978 | Side (Yerevan-bound) | T-6-40 Balahovit / Mayakovski | |
| 5 | 14.8 | 13.23–13.26 | 40.2763, 44.6005 | Side, both sides | Karmir Banaki St, Getamej / Abovyan W | |
| 6 | 15.7–16.2 | 14.12–14.62 | 40.2834, 44.6052 | **GS (full, 8 ramps)** | Exits 5/6 "Abovyan (West)" | Main Abovyan access; fuel both sides |
| 7 | 16.7–17.2 | 15.15–15.63 | 40.2918, 44.6108 | GS (bridge 15.42) | Exit 7, Abovyan E / Arzni / Nor Geghi / Kotayk | |
| 8 | 18.1 | 16.46–16.51 | 40.3020, 44.6181 | MO ×2 | Byureghavan | Speed camera 16.6 |
| 9 | 19.3 | 17.65 | 40.3114, 44.6248 | MO | Byureghavan | |
| 10 | 21.5–21.9 | 19.92–20.32 | 40.3291, 44.6366 | Slip ramps (service areas, both sides) | Nurnus ("Pro Gas" both sides) | |
| 11 | 22.4–22.6 | 20.82–20.97 | 40.3373, 44.6336 | MO ×2 + side road | Nurnus | Rest area mapped at 22.7 (OSM 22.66) |
| 12 | 25.9 | 24.31 | 40.3625, 44.6415 | MO | Jraber / Argel | "Coffee island" café at OSM 24.2 (Sevan-bound side) |
| 13 | 27.4 | 25.83 | 40.3730, 44.6502 | Side | Charentsavan S | |
| 14 | 28.0 | 26.36 | 40.3776, 44.6516 | MO | Charentsavan | Speed camera 27.1 (70) |
| 15 | 31.1–31.8 | 29.47–30.15 | 40.4002, 44.6729 | **GS (6 ramps, bridge 29.77)** | Exits 10 "Fantan" / 11 Charentsavan–Alapars | |
| 16 | 39.3–40.0 | 37.73–38.41 | 40.4607, 44.7276 | **GS + 2 MO (bridge 38.29)** | Exit 12 "Hrazdan" | Main Hrazdan / Tsaghkadzor access |
| 17 | 43.2 | 41.55–41.81 | 40.4823, 44.7625 | Partial GS (bridge 41.64) | Exits 13/14, Hrazdan centre / Lernanist | |
| 18 | 44.6–45.2 | 42.99–43.55 | 40.4907, 44.7754 | Side | Hrazdan / Makravan | Speed cameras 43.3 |
| 19 | 47.4–48.1 | 45.78–46.45 | 40.5070, 44.8005 | **GS (4 ramps)** | Exit 15 "Hrazdan (East)" | |
| 20 | 48.6 | 46.99–47.06 | 40.5136, 44.8129 | MO ×2 | Jrarat | |
| 21 | 51.0 | 49.44 | 40.5234, 44.8378 | MO | Jrarat / Gagarin | Accident km 50, 8 Oct 2026 [11] |
| 22 | 51.5 | 49.92 | 40.5247, 44.8418 | MO + side | Gagarin ("Gas #1" both sides) | Start of 2026 resurfacing km 51.1 [6] |
| 23 | 52.9 | 51.30–51.41 | 40.5295, 44.8583 | MO ×2 | Gagarin | |
| 24 | 54.3–54.9 | 52.73–53.27 | 40.5344, 44.8737 | **GS (7 ramps, bridge 52.95)** | Exits 18/19, Gagarin / Tsaghkunk / Geghamavan | |
| 25 | 55.7 | 54.11 | 40.5399, 44.8885 | Side | Geghamavan | |
| 26 | 57.1–57.8 | 55.51–56.19 | 40.5403, 44.9048 | MO ×3 (bridge 55.60) | Varser | 70 km/h zone; 5 fuel stations |
| 27 | 59.4–60.1 | 57.81–58.54 | 40.5367, 44.9318 | **GS (8 ramps, bridge 58.15)** | Exits 21/22, Sevan W / Lchashen; toward Gavar–Martuni | Speed cameras 57.7 (70) |
| 28 | 61.4–62.3 | 59.76–60.65 | 40.5364, 44.9541 | MO + side roads | Sevan town (Sayat-Nova St) | |
| 29 | 63.0 | 61.39–61.47 | 40.5431, 44.9706 | Slip ramp | Exit 23, Gomadzor / Sevan E | |
| 30 | 63.5–64.2 | 61.94–62.56 | 40.5466, 44.9752 | Slip + MO ×2 | Exit 24, Lavanda City | |
| 31 | 64.7–65.2 | 63.10–63.63 | 40.5541, 44.9850 | MO + side | Exit 25, Tsamakaberd / Azatutyun St | |
| 32 | 66.7 | 65.06–65.27 | 40.5679, 44.9990 | MO + side | Exit 26, Dzknorsner St | Lakeside restaurant strip |
| 33 | 72.1 | 70.48–70.53 | 40.6013, 44.9582 | MO | Exit 27 | |
| 34 | 73.0–73.1 | 71.41–71.49 | 40.6091, 44.9547 | At-grade + MO ×2 | Tsovagyugh; Tsovagyugh–Vardenis road (north shore) | "Take coffee and more" café (Tsovagyugh-bound side) |
| 35 | 73.9 | 72.29–72.35 | 40.6168, 44.9524 | At-grade | Semyonovka–Tsovagyugh road (old Sevan pass); **end of dual carriageway** | EV chargers / services mapped |
| 36 | 80.7–83.0 | 79.09–81.43 | 40.6535, 44.8922 (S portal) → 40.6733, 44.8830 (N portal) | Tunnel | Dilijan (Sevan) tunnel | 2,337 m, 40 km/h |
| 37 | 83.9 | 82.34 | 40.6793, 44.8758 | At-grade | Semyonovka (north), ref 31 | |
| 38 | 91.8 | 90.19 | 40.7113, 44.8511 | At-grade | T-10-23, Dilijan, ref 32 | |
| 39 | 95.9 | 94.26 | 40.7394, 44.8652 | Urban junctions | Dilijan centre (Gorky / Kalinin / Myasnikyan St) | |

Data notes:
- The full machine-readable lists are kept in the analyst scratchpad: 825 records of connecting ways and tagged nodes, and 427 POIs within 400 m (225 within 200 m).
- Interchanges were classified automatically (ramps on both carriageways = GS; a carriageway-to-carriageway link under 130 m = MO), then reviewed by hand.

### 3.9 Planned upgrades and works, 2025–2030

| Item | Status / date | Traffic implication | Status | Source |
|---|---|---|---|---|
| Medium repair km 51.1–68.0 (Gagarin–Sevan): 16.9 km of the left carriageway plus 3.8 km of the right (20.7 km in total), AMD 1.089 bn. *Fact-check correction: originally given as a 20.7 km section; the road span is 16.9 km* | ~65 % done by 24 Jul 2026; completion late Aug 2026 | Temporary lane closures; better surface | REPORTED | [6] |
| Medium repair km 32+580–36+000 (Charentsavan–Kaghsi) | Night closures from 10 Jun 2026; contraflow | Night disruption only | REPORTED | [7][8] |
| Medium repair Tsovagyugh → Dilijan tunnel (~6 km) | Under way by 22 Sep 2026 (start date not stated) | Single-carriageway works: delays | REPORTED | [9] |
| Thermoplastic re-marking, Yerevan–Sevan | Aug 2026 | — | REPORTED | [10] |
| ADB RIRSIP II: Dilijan and Pushkin tunnel rehabilitation, M-6 flood repairs (US$165 m ADB loan) | Proposed; fact-finding Nov–Dec 2025; approval date not set | Multi-year works in the Dilijan tunnel. For Pushkin, ADB plans light-vehicle diversion over the old pass in summer only, heavy vehicles diverted regionally. If replicated at Dilijan (ASSUMPTION), Sevan–Dilijan flows would be disrupted c. 2027–2030 | VERIFIED | [3][4] |
| M-4 Yerevan–Sevan–Dilijan widening/grade separation (118 km, US$131.5 m) in ADB's Transport Sector Development Strategy 2020 | c. 2008–09 plan; **no evidence of implementation or a current project** | None expected by 2030 | REPORTED (cited in ADB TA 7208 §120; TSDS not opened). *Fact-check correction: retagged from "VERIFIED (as cited)"* | [1] §120 |
| 2025 national programme: 504.5 km of roads, 135 km interstate | 2025 completed; no M-4 projects named | — | REPORTED | [15] |
| Yerevan–Sevan expressway / new alignment | **None found** | — | — | (searches) |

### 3.10 Proxies: roadside supply (fuel and food density) and catchments

POIs within 200 m of the M-4, from OSM, by side. "R" is the right-hand side when travelling toward Sevan/Dilijan; "L" is the Yerevan-bound side.

| Segment (OSM km) | Fuel R/L | Café / fast food / restaurant R/L | Convenience / supermarket R/L |
|---|---|---|---|
| Yerevan urban (0–7.5) | 7 / 12 | 12 / 9 | 5 / 2 |
| Yerevan edge–Abovyan (7.5–16) | 8 / 5 | 6 / 3 | 6 / 2 |
| Abovyan–Charentsavan (16–29.4) | 3 / 2 | 4 / 0 | 3 / 1 |
| Charentsavan–Hrazdan W (29.4–37.7) | 0 / 0 | 0 / 1 | 0 / 0 |
| Hrazdan (37.7–47) | 3 / 3 | 2 / 1 | 1 / 0 |
| Hrazdan E–Sevan W (47–57.7) | 8 / 5 | 0 / 1 | 2 / 1 |
| Sevan–Tsovagyugh (57.7–71.5) | 5 / 5 | 13 / 3 | 5 / 0 |
| Tsovagyugh–tunnel (71.5–79.1) | 3 / 2 | 0 / 0 | 1 / 0 |
| Tunnel–Dilijan (79.1–94.3) | 2 / 1 | 27 / 20 | 5 / 6 |

Source: [23] (REPORTED; OSM POI coverage in Armenia is incomplete).

Reading the table:
- Fuel stations cluster where traffic is high (near Yerevan) and where Sevan-bound drivers stop before the lake (Gagarin–Varser).
- CNG became Armenia's main transport fuel by the late 2000s, at 42 % of consumption by weight in 2007 [1]. CNG refuelling makes passengers leave the vehicle, so fuel-station stops already capture coffee demand (ASSUMPTION on behaviour). Fuel stations are both the main competitors and the natural partners (the hybrid option).
- **There is already a drive-thru and a coffee cluster at the Yerevan exit.** The OSM table above misses the most decision-relevant competitor.
  - The **Coffee House Drive-Thru** sits at about official km 12.8 (OSM ≈ 11.2), Sevan-bound side, at 40.25929, 44.59761, next to a TumOil LPG station. It has operated since at least late 2024 (VERIFIED in sibling A3 from the company branch list [27]).
  - **Max Cafe** operates at km 12.2 on both carriageways, and **Ninja coffee** at km 10.5 on the Sevan-bound side [27].
  - All three are in S1, the segment with the best M-4 traffic.

  *Fact-check correction: the original omitted these competitors.*
- **Fuel-station totals differ between workstreams.**
  - This table gives 55 fuel stations within 200 m from the Yerevan edge to Dilijan: 52 up to the tunnel, and 74 if the urban section is included.
  - A3 cites 60 within 200 m "Yerevan → Dilijan" (OSM via B2).
  - B2 counts 40 merged sites within 150 m for official km 10.2–74.3.
  - The differences come from the start point (urban section in or out), the buffer (150 m vs 200 m) and whether duplicate OSM objects (node plus area) are merged. All three agree on the order of magnitude: roughly 40–60 roadside fuel sites outside central Yerevan. Use B2's merged list for site-level work (*fact-check reconciliation*).

---

## 4. Implications for the drive-thru concept (critical)

1. **The best M-4 traffic is close to Yerevan, where land and competition are urban-like.** On the evidence, S1–S2 (official km 9–31, Yerevan edge to Charentsavan) carries 1.5–2.5 times the volume of the Hrazdan–Sevan stretch. An "M-4 site at Sevan" bets on the weakest and most seasonal part of the corridor's volume profile. *Fact-check note: this conclusion stands and is strengthened. Comparator-anchored estimates put S1 above the 42k base, and decay beyond Abovyan may be steeper than assumed (§3.3, §3.4).*
2. **Dual carriageway plus median barrier means one-side capture.** For the model, use **per-direction light-vehicle flow**, not two-way AADT. Base cases at a light-vehicle share of 85 %:
   - S2 (Abovyan–Charentsavan): about 11,600 vehicles/day per side
   - S5 (Hrazdan–Sevan): about 7,100
   - S6 (Sevan lakeshore): about 3,900
   - S7 (Sevan–Dilijan): about 2,300

   At an illustrative capture of 1 % (to be set by the capture-rate workstream), S2 gives about 116 cars/day and S6 about 39 cars/day. At sibling C6's recommended M-4 base of about 0.7 % of same-side light vehicles, S2 gives about 81/day and S6 about 27/day. That gap decides viability.

   *Fact-check correction: the original figures, at ×0.82, were 11,000 (11,200) / 6,900 / 3,800 / 2,200 and 110 / 38 cars/day (§3.5).*
3. **Interchange-adjacent parcels can serve both directions.** Candidates: Verin Ptghni (km 11.1), Abovyan W/E (km 15.7, 16.7), Charentsavan/Fantan (31.1), Hrazdan (39.3, 47.4), Gagarin (54.3) and Sevan W (59.4). These parcels are also where local town traffic adds to through traffic. Drivers would have to leave the highway, so signage and visible access matter; detour tolerance is ASSUMPTION-driven, so test it in intercepts.
   - **The Yerevan-exit cluster (km 10.5–12.8) already has an incumbent drive-thru**: Coffee House, at km ~12.8 on the Sevan-bound side. Max Cafe sits on both sides at km 12.2. A Sevan-bound site at Verin Ptghni (km 11.1) or Abovyan W (km 15.7) would compete with them head-on [27].

   *Fact-check correction: the original candidate list omitted the incumbent.*
4. **Direction-of-demand mismatch.**
   - Commuter coffee peaks (07:00–09:30) are on the Yerevan-bound carriageway between Hrazdan/Abovyan and Yerevan.
   - Leisure coffee (weekend 08:00–12:00) is on the Sevan-bound carriageway.
   - A single-side site captures only one of these.
   - Weekday afternoons and the Sunday-evening return to Yerevan (heavy, but fatigued drivers wanting to get home) are uncertain markets (ASSUMPTION).
5. **Seasonality risk.** Sevan-side segments probably see winter weekday volumes at 30–40 % of summer-weekend volumes (ASSUMPTION; to be measured). Fixed costs must be covered in about 7 low months.
6. **Access engineering and permits.**
   - Posted speed is 90 km/h on about 93 % of the dual section.
   - New right-in/right-out access requires deceleration and acceleration lanes and RDF/Road Police approval.
   - On the Abovyan–Charentsavan climb (+2.8 % average), trucks are slow and merging is harder.
   - These are cost and timing risks (ASSUMPTION; regulation to be confirmed by the permits workstream).
7. **Works risk on Sevan–Dilijan.** The proposed ADB Dilijan tunnel rehabilitation could restrict or divert traffic for years. The single-carriageway section is also undergoing resurfacing in 2026. **Avoid committing to S7 until the tunnel works schedule is known.**
8. **Competition is entrenched at stopping points.** There are 37 fuel stations between the Yerevan edge and Sevan W, and lakeside restaurants on the Sevan bypass. A standalone drive-thru must win against fuel-station cafés that already capture the "stop." **It must also win against an existing drive-thru.** The Coffee House Drive-Thru has operated at official km ~12.8 (Sevan-bound, S1) since at least late 2024, next to Max Cafe (km 12.2, both sides) and Ninja coffee (km 10.5) [27]. *Fact-check correction: the original omitted the incumbent drive-thru.* A **fuel-station hybrid** (co-locating at an existing CNG/petrol station with ramps) may give higher capture at lower capex. The Charentsavan–Hrazdan stretch (official km 31–39) has **no services on ~8 km**, a potential gap but also no access points.
9. **Data risk is the largest risk.** The whole volume chain rests on a single 2008 counter and assumed decay shares. The ranges are wide: S2 runs from 18k to 40k AADT. The 2008 count is 15 % below 2007, and comparator-anchored paths give 44–55k for S1. The 42k base therefore probably errs low near Yerevan, while the decay shares may err high further out (*fact-check*). **Do not commit land or sign a lease before the §5 counts.** At minimum, use the RDF counter data request and a 7-day video count at the shortlisted site.
10. **Upside signals.** National traffic growth near Yerevan has been strong: 5.4–6.1 %/yr over 2008–17/18 at the M-1 and M-2 exits [25] and 9–12 %/yr in 2016–21 [2], with GDP +46 % in 2016–23 [5]. Interstate congestion is officially acknowledged [12]. No competing expressway is planned that could bypass roadside sites before 2030. If growth continues at 3–5 %/yr, S1–S3 volumes rise by about 15–28 % over the 5-year model horizon (ESTIMATE: 1.03^5 = 1.16; 1.05^5 = 1.28), less any peak capacity constraint.

---

## 5. Data gaps and how to verify them

### 5.1 Gaps

| Gap | Why it matters | How to close it (agency / document / method) |
|---|---|---|
| Current (2019–2026) AADT for each M-4 segment | Core revenue driver | **Formal letter to the "Road Department" Fund (RDF, armroad.am, info@armroad.am) and MTAI** requesting automatic-counter data for M-4 stations (km 10+320, km 80+300 and any newer ones): monthly AADT 2009–2026, hourly profiles, class mix. The 2023 ADB citation of M-1/M-5 growth [2] shows such data exist, and ADB's 2020 completion report [25] publishes M-1/M-2 counter data for 2009–18 |
| MTAI Transport Master Plan 2020–2030 (draft, 2021) | Likely contains a national traffic model and counts | Request from MTAI Transport Policy Department or ADB Armenia Resident Mission (cited in [2]) |
| Road Police / "Safe Road" speed-camera counts | Every camera records each vehicle | Request hourly counts for cameras at OSM km 14.9, 16.6, 27.1, 38.9, 43.3, 57.7 from the Road Police of the Ministry of Internal Affairs |
| 2008 interstate traffic-volume map | Gives the historical segment profile | Request the full ADB TA 7208 report with appendices from ADB or MTAI; the public PDF lacks the figure [1] |
| Weekday / weekend, month-by-month and hourly profiles | Staffing and seasonal revenue | Fieldwork (§5.2) plus RDF monthly data |
| Sevan visitor flows (cars/day on peak weekends) | Leisure share of S5–S7 | Tourism Committee / Sevan National Park beach-entry data; municipality paid-parking data; police summer operation reports. **WebSearch budget for this session was exhausted before these could be searched**; to be completed in a follow-up |
| Accident hotspots by km | Safety, access approval | Road Police accident database by km for 2022–2025; RDF black-spot list |
| Winter closure log (M-4 Yerevan–Dilijan) | Operating days | Rescue Service (MES) daily road bulletins archive; RDF |
| Dilijan tunnel works schedule and traffic management plan | S6–S7 risk | ADB project 58405-001 documents (RRP, Dilijan IEE when disclosed); RDF |
| Status of median openings (legal vs informal, planned closures) | Site access both ways | Drive survey plus RDF design drawings |
| Official census populations of corridor towns | Catchment check | **Mostly closed at fact-check:** §3.4 now uses the Armstat 1 Oct 2025 bulletin [26]. Dilijan is still an OSM tag of unverified vintage |
| Speed-limit legal basis (90 km/h outside settlements, etc.) | Access design | Government Decision on Road Traffic Rules (arlis.am); my fetch of the act timed out |

### 5.2 Traffic-count fieldwork protocol (to complete before land commitment)

**Objectives:** per-direction classified volumes, hourly and daily profiles, seasonal factors, the share of through vs local traffic, and the empirical stop rate at existing roadside outlets.

**Stations (6 screenlines, plus a site-specific one):**

| Station | Official km (≈) | Location rationale |
|---|---|---|
| A | 10–11 | Replicates the RDF counter (km 10+320) for calibration against 2005–08 |
| B | 20–27 | Abovyan–Charentsavan (S2); candidate commuter site |
| C | 33–37 | Charentsavan–Hrazdan (S3) |
| D | 49–53 | Hrazdan–Sevan (S5); Sevan-bound leisure |
| E | 62–70 | Sevan lakeshore bypass (S6) |
| F | 75–79 | Tsovagyugh–tunnel (S7) |
| G | Shortlisted parcel | Turning-movement and ramp counts at the nearest interchange or median opening |

**Timing:**
- **Peak season:** 7 consecutive days (Mon–Sun) in mid-July to mid-August, including one weekend with fine weather.
- **Low season:** 7 days in late October–November or February.
- Avoid public holidays unless they are measured separately; also record one holiday weekend, such as Vardavar (July), as a peak-day test.

**Methods:**
1. **Continuous automatic counts (24 h × 7 days, both directions, by class).** Use pole- or overpass-mounted **video with automated classification**, or side-fire radar. Do not use pneumatic tubes across 90 km/h dual carriageways, for safety reasons.
2. **Manual classified verification counts.** Two 16-hour days per station (06:00–22:00), one weekday (Tue–Thu) and one weekend day. Use 6 classes: car, SUV/pickup, minibus, bus, light truck, heavy truck. Count in 15-minute bins and record occupancy for a sample.
3. **ANPR plate matching between stations A, C, D and F** (anonymised, hashed plates). This measures through traffic vs local and how far trips extend (e.g., the share of Yerevan-edge vehicles reaching Sevan), replacing the assumed shares in §3.4.
4. **Stop-rate counts at 3–4 existing fuel/café stops** (e.g., the Nurnus service areas at km 21.5, Gagarin "Gas #1" at km 51.5, and a lakeside café near km 66–73). Count entries vs passing flow by hour. This gives an observed capture benchmark per side.
5. **Intercept survey at those stops:** about 150–200 interviews per site per season, weekday plus weekend. Cover trip purpose, origin–destination, frequency, coffee/food purchase, spend, preferred stop time, and whether the respondent would use a drive-thru and on which side.
6. **Travel-time runs** (GPS, 4 runs per peak) to document congestion and weaving at candidate accesses.

**Permissions:** RDF and Road Police notification or permission for roadside equipment; data protection for ANPR (hash at source, no image retention).

**Indicative cost (ASSUMPTION; obtain 3 quotes from Armenian survey and engineering firms):**

| Item | Basis | US$ |
|---|---|---|
| Video/radar 7-day counts, 7 stations × 2 seasons | ~US$300–600 per station-week, including AI classification | 4,200–8,400 |
| Manual counts, 6 stations × 2 days × 16 h × 2–4 enumerators × 2 seasons | ~US$4–6/enumerator-hour plus supervision | 4,000–9,000 |
| ANPR matching (4 stations, 2 days each season), processing | Equipment rental plus analysis | 2,500–6,000 |
| Stop-rate counts and intercepts, 4 sites × 2 seasons | Interviewers, questionnaire, coding | 3,000–6,000 |
| Design, permits, QA, reporting | Traffic engineer | 4,000–6,000 |
| **Total** | | **≈ 18,000–35,000** |

A **lean pre-screen** for a single shortlisted parcel, with one 7-day video count, two manual days and one stop-rate site, would cost about US$4,000–8,000 (ASSUMPTION).

**Outputs for the model:**
- per-direction hourly light-vehicle flows by day type and season, giving seasonal and weekly indices;
- through/local split;
- an observed stop rate at comparable outlets, which bounds the capture rate.

---

## 6. Sources (all accessed 2026-10-10)

1. ADB / PADECO. *TA 7208-ARM: Preparing the North–South Road Corridor Development Project — Final Report*, Vols I–IV (May 2010; PDF dated June 2010). Tables 4-14 (RDF counts 2005–08) and 4-15 (2009 counts); Vol. II §32–39 (seasonality, growth, fleet); §120 (M-4 investment plan); Table 2-10 (CNG). https://www.adb.org/sites/default/files/project-documents/42145-01-arm-tacr.pdf
2. ADB. *Yerevan Urban Development Investment Project (RRP ARM 54172-002): Sector Assessment (Summary) — Urban Transport* (Oct–Nov 2023). Footnote 7 (M-1/M-5 growth). https://www.adb.org/sites/default/files/linked-documents/54172-002-ssa.pdf
3. ADB. *Project 58405-001: Resilient and Inclusive Road Sector Improvement Project II* (project page, last PDS update 9 Oct 2024; fact-finding Nov–Dec 2025). https://www.adb.org/projects/58405-001/main ; also EWS summary https://ewsdata.rightsindevelopment.org/projects/ADB-58405-001/
4. ADB. *RIRSIP II — Initial Environmental Examination (Rehabilitation of the Pushkin Tunnel; joint Dilijan/Pushkin survey annexes)*, Nov 2025, Parts 1–5. §23 gives the Dilijan tunnel at M-4 km 80–83. https://www.adb.org/sites/default/files/project-documents/58405/58405-001-iee-en.pdf (parts _0 to _3 likewise)
5. ADB. *Report and Recommendation of the President: Resilient and Inclusive Road Sector Improvement Project (56317-001)*, Nov 2024 (GDP growth 2017–2023). https://www.adb.org/sites/default/files/project-documents/56317/56317-001-rrp-en.pdf ; project page https://www.adb.org/projects/56317-001/main
6. Armenpress. "Երևան-Սևան-Իջևան ավտոմայրուղու 20,7 կիլոմետրանոց հատվածը ենթարկվում է միջին նորոգման" (24 Jul 2026). https://armenpress.am/hy/article/1256377
7. Armenpress. "Երևան-Սևան ճանապարհի մի հատվածում երթևեկությունը կկազմակերպվի հանդիպակաց գոտով" (10 Jun 2026). https://armenpress.am/hy/article/1252667
8. NewsArmenia. "Участок трассы Ереван–Севан закроют для транспорта на 10 часов" (10 Jun 2026). https://newsarmenia.am/news/armenia/uchastok-trassy-erevan-sevan-zakroyut-dlya-transporta-na-10-chasov/
9. Verelq. "На трассе Ереван—Севан начался ремонт 6-километрового участка" (22 Sep 2026). https://verelq.am/ru/node/177752
10. Armenpress. "Միջին նորոգման ծրագրի շրջանակում գծանշվում է Երևան-Սևան ճանապարհը" (10 Aug 2026). https://armenpress.am/hy/article/1257590
11. Armenpress. "Երևան-Սևան ճանապարհին միկրոավտոբուս է կողաշրջվել․ կա 8 տուժած" (8 Oct 2026). https://armenpress.am/hy/article/1262267
12. ARKA. "Armenian government has allocated 15.65 billion drams for road construction and repairs" (6 Aug 2026). https://arka.am/en/news/economy/armenian-government-has-allocated-15-65-billion-drams-for-road-construction-and-repairs/
13. ARKA. "Дорожная полиция Армении ужесточит проверки на трассе Ереван-Севан" (18 Jul 2014). https://arka.am/news/society/dorozhnaya_politsiya_armenii_uzhestochit_proverki_na_trasse_erevan_sevan/
14. Office of the Prime Minister of RA. Press release, report of N. Pashinyan (28 Feb 2024). M-6 traffic intensity. https://www.primeminister.am/en/press-release/item/2024/02/28/Nikol-Pashinyan-Report/
15. Armenpress. "Government-funded road renovation and reconstruction exceeds 500 km in 2025" (18 Mar 2026). https://armenpress.am/en/article/1244989
16. Armenpress. "Pashinyan highlights strategic road upgrades" (15 Apr 2026). https://armenpress.am/en/article/1247464
17. UNDP-EU EU4Climate. *Reforms of Yerevan Transport System in the Context of Low-Carbon Development* (2021). Tables 2–3: registered vehicles 2018 and 2020. The 2020 total includes 32,446 Artsakh-registered vehicles. This is a secondary donor report compiling Traffic Police data, so it is tagged REPORTED. https://euneighbourseast.eu/wp-content/uploads/2021/07/report-yerevan-transport_eng.pdf
18. 1lurer (Public TV). "Ինչ իրավիճակ է ՀՀ ճանապարհներին" (27 Dec 2025). https://www.1lurer.am/hy/2025/12/27/1/1439792
19. Aravot / "Փաստ". Article on Yerevan congestion and vehicle growth (18 Dec 2025). https://www.aravot.am/2025/12/18/1529412/
20. Iravaban.net. "Գործարկվել է Երևան-Սևան-Շորժա էլեկտրագնացքը" (19 Jun 2022). https://iravaban.net/386900.html
21. Wikipedia (ru). "Автодорога М4 (Армения)" (length 148.2 km). https://ru.wikipedia.org/wiki/Автодорога_М4_(Армения)
22. Wikipedia (hy). "Մ 4 ճանապարհ (Հայաստան)" (1st class to the Dilijan tunnel, 2nd class beyond). https://hy.wikipedia.org/wiki/Մ_4_ճանապարհ_(Հայաստան)
23. OpenStreetMap contributors. Relation 7065693 (M-4) with member ways, connecting ways, tagged nodes (milestones, speed cameras, motorway_junction), barriers and POIs. Extracted via Overpass API (maps.mail.ru mirror); OSM base timestamp 2026-10-10T09:41:31Z. ODbL. https://www.openstreetmap.org/relation/7065693
24. OpenTopoData. SRTM 90 m elevation API, 95 points sampled at 1 km along the M-4. https://api.opentopodata.org/v1/srtm90m
25. ADB. *Completion Report: Armenia — North–South Road Corridor Investment Program (Tranche 1), Loan 2561* (Jan 2020). The appendix table "Automatic Traffic Count Records 2009–18" (Armenian Roads Directorate) covers M-2 km 9.38 and M-1 km 20.7; ¶14 compares M-2 km 16 with km 9.38 (2009). Added at fact-check, 10 Oct 2026. https://www.adb.org/sites/default/files/project-documents/42145/42145-023-pcr-en.pdf
26. Armstat. *Population of the Republic of Armenia as of 1 October 2025* (statistical bulletin). Added at fact-check, 10 Oct 2026. https://www.armstat.am/file/article/population_01_10_25.pdf
27. Sibling workstream A3, `research/A3-qsr-fuel-convenience.md` (10 Oct 2026). Coffee House Drive-Thru location and hours (VERIFIED there from the company branch list), Max Cafe km 12.2 and Ninja coffee km 10.5. Added at fact-check.

*Search note: the shared web-search quota for this workflow was used up partway through the task. Remaining items (Sevan visitor counts, the MTAI master plan, Road Police data) were not searched and are listed in §5.1 for follow-up.*

---

## 7. Fact-check log

*Adversarial fact-check, 10 Oct 2026.*

**Sources re-opened (15):** ADB TA 7208 (full PDF), ADB 54172 SSA, ADB RRP 56317, the ADB 58405 page and IEE, the UNDP-EU report, the PM's press release, ARKA ×2, Armenpress ×4, Verelq and Aravot.

**Uncited primary documents also used (2):** ADB PCR 42145-023 [25] and the Armstat Oct-2025 bulletin [26].

**Result.** Every quoted number matched its source, and all the ESTIMATE arithmetic recomputed correctly. The problems were in interpretation and calibration.

**Net effect.** Near Yerevan (S1–S2), volumes are probably higher than the 42k base, which is now labelled conservative. Beyond Abovyan, decay may be steeper. The "Yerevan edge beats Sevan" conclusion stands and is strengthened. The RDF data request and fieldwork remain essential before any land commitment.

| # | Claim | Result | Correction / evidence |
|---|---|---|---|
| 1 | M-4 counter km 10+320 AADT 19,484 / 22,877 / 25,386 / 21,505 (2005–08); km 80+300 1,455 / 2,301 / 961 / 783 | Confirmed | TA 7208 Table 4-14 (Armenian Roads Directorate) matches exactly |
| 2 | In 2008 the M-4 Yerevan exit was the "second-busiest counter", level with the M-2 and M-5 | **Wrong** | 2008: M-4 21,505 > M-5 21,471 > M-2 20,965. M-4 was the busiest, by a hair, in 2007 too (25,386 vs 24,551 / 23,202). Fixed in §3.1 |
| 3 | 2008 "slightly below" 2007, in line with the 5 % network fall | Corrected | −15.3 % (21,505 / 25,386), three times the −5.2 % network decline. 2007 base at 4 %/yr gives ≈51,400 in 2025. Fixed in §1 item 1, §3.1 and §3.3 (base-year sensitivity added) |
| 4 | Recent counter data unpublished; 2009–15 "stagnation" justified the low/base growth | **Wrong** | ADB PCR 42145-023 (Jan 2020) publishes 2009–18 counts. M-2 km 9.38: 23,406 → 37,831 (6.1 %/yr 2008–18). M-1 km 20.7: 12,384 → 18,635 (5.4 %/yr 2008–17). Both grew about 7 %/yr in 2009–14. Claim restricted to the M-4; stagnation rationale dropped. §1 items 1–2, key data row 6a, §3.1, §3.2, §3.3, §5.1, source [25] |
| 5 | M-1 +12 %/yr (2018–21), M-5 +9 %/yr (2016–21) | Confirmed | ADB 54172-002 SSA fn 7, quoted exactly |
| 6 | 2025 Yerevan-edge AADT 32,700 / 41,900 / 53,400; base 42k | Corrected | Arithmetic correct, but the calibration is weak. Comparator-indexed paths give M-2 47,700–54,600, M-1 43,700–51,000 and 2007 base ≈51,400; all are ≥ 44k. The 42k base is kept but labelled **explicitly conservative** (comparator mid ≈48k). The low case becomes a stress case. §1 item 3, key data row 13, §3.3, §4.9 |
| 7 | Fleet 330,000 → 850,691 = +7.0 %/yr; basis of the high case; source VERIFIED | Corrected | 2020 includes 32,446 Artsakh vehicles and a one-off 34 % jump (EEU import tax). 2006–18 trend = 5.5 %/yr (630,170 in 2018); 6.7 %/yr excluding Artsakh. UNDP-EU is a secondary source, so it is retagged REPORTED (rows 11–12). High-case rationale re-based on the comparator exits |
| 8 | Light vehicles 78–86 %; M-2 km 16 is "the only" classified count near a Yerevan exit | Corrected | M-1 km 20.7 (23 Jul 2009) shows 88.7 % light, peak hour 8.1 % (TA 7208 Vol II Table 3-1). PCR ATC shows 92 % / 97 %. Share widened to 80–89 %, base 85 %. Per-direction flows recomputed: S1 17,900, S2 11,600, S3 10,700, S4 8,900, S5 7,100, S6 3,900, S7 2,300 (§1 item 6, §3.4, §3.5, §4.2) |
| 9 | July = +19.7 % above AADT at M-1 km 20.7; "~2005–09" | Confirmed | TA 7208 Vol II §32. The period is not stated in the source and is now labelled as inferred. The M-1 is a weak analogue for Sevan leisure seasonality |
| 10 | Decay shares follow drop-offs "ADB measured" on the M-1 (70 % / 43 %) | Corrected | These are ADB consultant estimates. The measured M-1 pair is km 20.7 vs km 30 = 37 %. On the M-2, km 16 = 44 % of km 9.38 (2009, PCR ¶14). Relabelled "estimated"; 44 % added as a downside check (S2 ≈18,500). §1 item 4, §3.4 |
| 11 | Segment table S2–S7 and per-direction flows; 1 % capture S2 ≈110, S6 ≈38 | Confirmed | Arithmetic recomputes. Section cross-references in key data rows 13–16 fixed. C6's 0.7 % base capture added (S2 ≈81/day, S6 ≈27/day at ×0.85) |
| 12 | Fleet cross-check 370k → 0.85–1.0 m, elasticity 0.6–0.8 → 39,000–47,000 | Downgraded | No formula shown; end-2008 interpolation ≈363k. F^e gives 35,400–47,600; 1 + e(F−1) gives 38,300–50,800. Widened to ≈35–51k; not a tight confirmation. Both fleet endpoints are weak (§3.3) |
| 13 | Capacity check 42,000 × 7.8 % × 0.58 ≈ 1,900 veh/h ≈ 53 % of capacity | Confirmed | Recomputed exactly. A 48k variant (≈60 %) added |
| 14 | M-6 2,800 → 4,000 cars/day 2014–23 (+4.0 %/yr) | Confirmed | PM press release, 28 Feb 2024. Flagged as a weak analogue (newly reconstructed border road) |
| 15 | Real GDP +6.8 % avg 2017–19 … +8.3 % 2023 (≈ +46 %) | Confirmed | ADB RRP 56317. ADB is secondary for national accounts (Armstat is primary) |
| 16 | Dilijan tunnel at M-4 km 80–83; RIRSIP II US$165 m proposed; Pushkin diversion | Confirmed | IEE ¶23 and the project page match. US$165 m is the ADB loan amount, not the total programme cost; wording fixed in §1 item 9, row 26 and §3.9 |
| 17 | Medium repair km 51+100–68+000: 20.7 km, AMD 1,089.3 m, 237,721 m² | Corrected | 20.7 km is carriageway length (16.9 km left + 3.8 km right); the road span is 16.9 km. Fixed in §1 item 9, row 24 and §3.9 |
| 18 | Night closures km 32+580–36+000; Tsovagyugh–tunnel repair "started Sep 2026" | Confirmed | Armenpress 1252667; Verelq 177752. The start date is not stated, so this now reads "under way by 22 Sep 2026" |
| 19 | PM (6 Aug 2026): congestion "commonplace" | Confirmed | ARKA quote exact. The M-4 is not named |
| 20 | Police: weekend volumes to Sevan "rise significantly" [13]; basis for 1.5–2.5× | Downgraded | ARKA, 18 Jul 2014: qualitative, no numbers, 12 years old. Now dated in the text. The 1.5–2.5× factor is marked unsupported until fieldwork (§1 item 8, §3.6) |
| 21 | Vehicle numbers "roughly one million" (Dec 2025), REPORTED (weak) | Confirmed | Aravot/"Փաստ", 18 Dec 2025; no source named. No longer used as a cross-check bound |
| 22 | Old ADB TSDS M-4 widening 118 km, US$131.5 m, "VERIFIED (as cited)" | Downgraded | TA 7208 §120 confirms the figures, but the TSDS was not opened, so it is retagged REPORTED (row 27, §3.9) |
| 23 | Roadside supply: 37 / 52 fuel, 34 F&B; "a standalone drive-thru must win against fuel-station cafés" | Corrected | Sums are internally consistent. B1 had omitted the incumbent **Coffee House Drive-Thru** at official km ~12.8, Sevan-bound (40.25929, 44.59761, since ≤ late 2024), plus Max Cafe km 12.2 and Ninja coffee km 10.5 (A3). These are now added to §1 item 10, row 31, §3.10, §4.3 and §4.8. Fuel totals reconciled with A3 (60) and B2 (40 merged, 150 m) in §3.10 |
| 24 | Catchment populations from OSM tags (Abovyan 45,025; Charentsavan 20,368; Hrazdan 39,957; Sevan 18,870) | Corrected | Armstat 1 Oct 2025: Abovyan 51.0k, Hrazdan 49.8k, Charentsavan 24.1k, Sevan 19.6k (also Byureghavan 11.9k, Nor Hachn 10.4k per B2). Replaced in §3.4; §5.1 gap updated. Low impact |
| 25 | Fieldwork budget US$18–35k; 1.03^5 / 1.05^5; 90 km/h on 93 %; 64.7 km dual | Confirmed | Line items sum to 17,700 / 35,400; all internally consistent |
