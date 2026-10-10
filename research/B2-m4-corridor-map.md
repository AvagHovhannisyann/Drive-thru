# B2 — Site-level mapping of the M4 Yerevan–Sevan corridor

*Reconstructed verbatim from the B2 analyst's structured output (the analyst agent was prevented from writing this file directly). POI dataset: `research/B2-m4-pois.csv` (OpenStreetMap via Overpass, data timestamp 2026-10-10).*

## 1. Executive summary

- **Deliverable note.**
- The harness blocked the subagent from writing a findings .md file ("subagents should return findings as text"). So /home/user/Drive-thru/research/B2-m4-corridor-map.md was NOT created. The full findings are condensed in this output: summary, key_facts, implications and gaps.
- The POI dataset WAS written: /home/user/Drive-thru/research/B2-m4-pois.csv.
  - 430 rows; columns name, category, brand, lat, lon, side_or_direction_if_known, source.
  - Contents: 70 fuel objects, 55 food outlets and stalls, 25 hotels, 33 interchange-exit nodes, 33 median-crossing links and 18 speed cameras.
  - Each row carries official km, the side and direction it serves, distance to the carriageway, and its OSM id or operator source.
- **Method.**
- **Road data.** OpenStreetMap via Overpass (data timestamp 2026-10-10 09:38 UTC). Both carriageways of the M4 (ref Մ-4) and the M10 (Մ-10) were routed separately.
- **POIs.** Everything within 700 m was projected onto each carriageway. 'Right side' means the side that Yerevan→Sevan traffic can enter right-in/right-out; 'left side' serves Sevan→Yerevan traffic.
- **Other sources.** SRTM elevation (OpenTopoData); Armstat 2025 population PDFs; the Max Oil and CPS station locators for brands.
- **Limitation.** The shared web-search budget (200 calls) ran out mid-task. news.am, civilnet, spyur and list.am pages were blocked (403), so those items are tagged weak or snippet-only.
- **Chainage convention: use official km.**
- My OSM chainage starts at the Myasnikyan Ave / Acharyan St junction (40.2079, 44.5602).
- 64 OSM km-post (milestone) nodes on the Sevan-bound side read **official km = OSM chainage + 5.27 to 5.68 (median ≈ +5.5)** along the whole corridor. The Yerevan-bound posts count down, and each pair sums to 148 km, which matches the 148.2 km M4 length on hy.wikipedia.
- Independent check: Max Oil's 'Yerevan–Sevan highway 12.2 km' station pair pins exactly at OSM 6.65 (VERIFIED, operator map pin).
- Road Department references (U-turn closures at km 10.3–16.3, the LPG explosion at km 16.2 near Abovyan, resurfacing at km 51.1–68.0) are all consistent.
- The companion file B1 quotes 'OSM + 1.6' because it uses a different chainage origin. Reconcile through official km. **All km below are official.**
- **Road form (REPORTED, OSM).**
- **Official km ~9 to 73.8 is a divided highway:** two one-way carriageways, mostly 2 lanes each way (3 near Yerevan and at some interchanges), asphalt.
- **Speed limits (`maxspeed`):** mostly 90 km/h; 60 km/h at km ~9.5–11.6 (city edge); 70 at Varser (56.2–57.8) and around 66.4–67.1; 50–70 at the H-7 junction (72.9–73.1).
- **Median barriers:** guard rails are mapped in every 10-km band and jersey barriers in every band except km 60+, so treat the median as physically closed except at openings.
- **From km 73.8** (Tsovagyugh) the road becomes a single carriageway (2 lanes total) toward the Sevan pass and Dilijan tunnel.
- **Direct driveways:** OSM shows about 203 service driveways joining the M4 directly. Direct-frontage businesses are normal; it is not a controlled-access motorway.
- **Elevation (ESTIMATE, SRTM):** 1,233 m at official km 5.5 → 1,855 m at about km 29.5 (Charentsavan summit) → 1,780–1,850 m around Hrazdan → 1,900–1,940 m around Sevan.
- **Interchanges and exits (REPORTED, OSM; official km).**
- **Yerevan city-limit sign:** km 10.2 (40.2430, 44.5753).
- **Exit 2/3 Ptghni/Arinj, km 11.0–11.9:** grade-separated. H-1 to Abovyan old road; H-61 (int_ref AH82) eastern bypass to Arinj / M-15, so traffic from south of Yerevan joins the M4 here.
- **Exit 5/6 'Abovyan (west)', km 15.7–16.2:** full interchange with 8 ramps. H-6 to Abovyan and Nor Hachn.
- **Exit 7, km 16.9–17.2:** H-2 to Arzni.
- **Exit 10/11, km 31.0–31.6:** Charentsavan (west) / Fantan (east).
- **Exit 12 'Hrazdan', km 39.9–40.0.**
- **Exit 13/14, km 43.1–43.3:** Hrazdan centre / Kaghsi. Tsaghkadzor signage not verified.
- **Exit 15 'Hrazdan (east)', km 47.4–48.0.**
- **Exit 18/19, km 54.4–54.8:** Gagarin and the old Hrazdan road.
- **Exit 20, km 57.8:** Varser; at-grade.
- **Exit 21/22, km 59.5–60.1:** grade-separated **M10 split to Martuni**, plus Sevan.
- **Exit 24/25, km 63.5–65.0:** Sevan centre (H-29) / Lavanda City. Mixed: one bridge plus at-grade crossings, including a two-way crossing at 64.1.
- **Exit 26, km 66.6:** **Sevan peninsula / Sevanavank (H-78)**. At-grade right turn off the Sevan-bound carriageway; median U-turn at 66.8.
- **Exit 27, km 72.1:** Tsovagyugh; at-grade.
- **Exit 28, km 73.0:** **H-7 Tsovagyugh–Vardenis** (east shore); at-grade.
- About 10 of these are grade-separated.
- **Median openings (REPORTED, OSM).**
- About 20 at-grade openings, at official km 18.1, 19.2, 22.4–22.6, 25.9, 27.9, 39.4, 48.6, 51.0, 51.5, 53.0, 57.1, 57.8, 61.6, 63.5, 64.1, 65.2, 66.8, 72.1 and 73.0.
- **There are none between km 10.2 and 18.** That matches a reported Road Department closure of 4 U-turns at km 10+300, 12+150, 14+660 and 16+330, with traffic redirected to the Ptghni and Abovyan interchanges (news.am snippet; page blocked; date not confirmed).
- Speed cameras are mapped at about km 10.3, 10.9, 16.5, 18.1, 28.6, 40.5, 44.9 (both carriageways), 59.3 (both carriageways) and near 74.
- **Fuel stations (ESTIMATE from OSM, plus operator data; complete list in the CSV).**
- Between km 10.2 and 74.3, within 150 m of the carriageway, there are **22 sites on the Sevan-bound side and 18 on the Yerevan-bound side** (duplicates within 150 m merged). About 35 of 48 OSM fuel objects have no name, and most are small CNG/LPG stations: 16 CNG-only, about 13 more with CNG.
- **Named or confirmed brands by official km:**
  - Max Oil pair at 12.2 (VERIFIED);
  - TumOil at 12.8 (Sevan-bound side); Max Oil at 15.8 (Yerevan-bound side);
  - YVR Gas at 17.1 and Gas Group at 18.4 (both Sevan-bound side);
  - Pro Gas pair at 21.5; NeftGroup at 39.6 (Sevan-bound side); Gas #1 pair at 51.2;
  - AMA Gas at 57.9 (Yerevan-bound side); CPS N14-1 Varser at 58.1 (Sevan-bound side, VERIFIED pin); Fenka 24/7 at 58.4 (Sevan-bound side);
  - CPS at 59.2 and CPS N14-2 Sevan at 60.7 (both Yerevan-bound side; N14-2 is a cps.am pin not mapped in OSM).
- **On the M10:** Lux Oil and Gastop at the split; Flash at M10 km 6.5 and 13.5; Max Oil at M10 km 12.5; RAN Oil at 21.4.
- **Clusters:**
  - Ptghni–Abovyan, km 12.2–18.4;
  - Sevan west / Varser, km 56.8–59.3: 10 sites on the M4 plus 4 at the start of the M10, the densest on the route;
  - Tsovagyugh, km 72.1–74.0.
- **The only fuel gap** is km 25.0→39.6 Sevan-bound (14.6 km) and 41.5→25.0 Yerevan-bound (16.5 km), around Charentsavan.
- **Food, coffee and stalls (REPORTED, OSM ≤150 m; OSM under-maps kiosks).**
- **Coffee-tagged outlets:** only 4, all on the Sevan-bound side:
  - Ninja coffee, km 10.5;
  - Coffee Island, km 25.8;
  - Yasaman Sevan (24/7), km 68.2;
  - Take Coffee and More, km 73.0.
- **Max Cafe** sits at km 12.2. Max Oil's news of 2 Jan 2026 announces it on the Yerevan-bound side ('for drivers on the road', coffee and hot dogs, fast service), and its station card lists Max Cafe plus 'Max Drive' on the Sevan-bound side (VERIFIED). What 'Max Drive' means is unknown.
- **Side imbalance beyond km 17.5:** about 20 food outlets on the Sevan-bound side against about 7 on the Yerevan-bound side (ESTIMATE). Return traffic is under-served.
- **Tsovagyugh lakeshore, km 68.1–74.1:**
  - 10 seafood (fish) stalls mapped on both sides;
  - 24/7 restaurants (Yasaman, Karasar);
  - at km 74.0–74.2, the Tsovagyugh food court, a 24/7 supermarket, a services area and a Team Energy EV charger.
- **Other mapped stops:**
  - rest areas at km 24.2 (Yerevan-bound side) and 71.6 (Sevan-bound side, 'Voske Avaz');
  - lakeshore hotels and restaurants at km 64–67 (Best Western Bohemian, Harsnaqar, Arevik, Kharkish, Hakobi Mot);
  - the Pharaon / Multi Grand complex at km 12.
- **Not mapped:** no gata, corn or fruit stalls appear on the M4 in OSM; they must be field-counted.
- **Settlements (VERIFIED, Armstat).**
- **Towns at 1 Oct 2025:** Abovyan 51.0k (2.7 km from the M4, km ~15.7), Hrazdan 49.8k (3.8 km, km ~45), Charentsavan 24.1k (1.9 km, km ~30), Sevan 19.6k (1.2 km, km ~62.6), Byureghavan 11.9k (2.1 km, km ~18.3), Nor Hachn 10.4k (2.7 km, km ~16.4), Tsaghkadzor 1.1k (about 6–7 km, reached through Hrazdan).
- **Villages at 1 Jan 2025** (distance from the M4, nearest official km):
  - Arinj 7,626 (1.3 km, km 10)
  - Verin Ptghni 1,073 (on the road, km 10.9)
  - Ptghni 1,915 (0.6 km, km 11.8)
  - Balahovit 3,962 (1.0 km, km 12.6)
  - Arzni 3,417 (1.4 km, km 16.6)
  - Nor Geghi 7,048 (3.8 km, km 17.9)
  - Jraber 453 (km 25)
  - Fantan 911 (1.3 km, km 31)
  - Solak 2,002 (km 38.8)
  - Kaghsi 2,699 (0.5 km, km 41.4)
  - Lernanist 3,037 (km 43.9)
  - Gagarin 1,872 (0.8 km, km 54.3)
  - Varser 1,499 (km 57.9)
  - Lchashen 4,301 (2.0 km, via the M10)
  - Tsovagyugh 4,356 (1.5 km, km ~74)
- **Marz totals:** Kotayk 296.1k, Gegharkunik 217.2k (1 Oct 2025).
- **Source conflict:** OSM population tags citing 'Armstat 2022-01-01' are 8–20% lower (e.g., Abovyan 45,025). I trust Armstat 2025.
- **Cluster C1: Yerevan exit / Ptghni–Arinj (Exit 2/3).**
- **Location:** official km 10.4–12.2; zone centre 40.2473, 44.5837.
- **Best side:** Yerevan-bound side for the morning commute, or an interchange quadrant.
- **Exposure:** maximum. All Yerevan↔Kotayk/Sevan traffic passes, AH82 bypass traffic joins here, and the 60 km/h limit and speed cameras ease entry. About 73.5k residents within 5 km.
- **Saturation within 2 km:**
  - 5 fuel stations on the Sevan-bound side and 4 on the Yerevan-bound side;
  - 8 food outlets, 9 shops and 7 lodgings;
  - Max Cafe on both sides, Ninja coffee, a 24/7 Zovq supermarket, Arinj Mall and Multi Magic Mall.
- **Approach:** straight for about 2.1 km Sevan-bound; short Yerevan-bound (interchange curve).
- **Verify:** Yerevan-bound frontage at km 10.4–11.0; queuing space; Max Cafe's formats and volumes.
- **Cluster C2: Abovyan–Arzni interchanges (Exits 5/6/7). PREFERRED commuter site (ASSUMPTION).**
- **Location:** official km 15.1–17.5; centre 40.2883, 44.6085.
- **Best sides:**
  - Yerevan-bound, just north of Exit 7 (km 17.2–17.9), to intercept Hrazdan/Charentsavan/Byureghavan commuters before they disperse;
  - Sevan-bound, at km 15.1–15.7, before Exit 5;
  - or a quadrant of the 8-ramp Abovyan interchange, which both directions can reach.
- **Catchment:** about 98k residents within 5 km (ESTIMATE), the largest on the corridor.
- **Competition:** light. Fuel 3 on the Sevan-bound side and 2 on the Yerevan-bound side (Max Oil at 15.8 Yerevan-bound; unnamed at 15.8, YVR Gas at 17.1, Gas Group at 18.4, all Sevan-bound). Only 1 mapped food outlet.
- **Access:** no median openings (removed); 90 km/h.
- **Approach:** straight for about 1.5 km Sevan-bound and 4.7 km Yerevan-bound.
- **Verify:** land category and ownership; whether a new access can be permitted near the Exit 7 merge; Max Oil at 15.8 as a co-location host; LPG safety setbacks (the June 2024 explosion was at km 16.2).
- **Cluster C3: Kaputan–Jraber at-grade stretch.**
- **Location:** official km 18–28; centre 40.3378, 44.6336.
- **Traffic:** through traffic only. Both directions can reach a site at the median openings (km 22.4–22.6), but those openings face closure risk.
- **Competitors:** Pro Gas pair at 21.5; the 25.0 fuel pair; Coffee Island (25.8) and tea houses (25.9, 27.1), all on the Sevan-bound side.
- **Profile:** about 13k residents within 5 km; climbing grade of about 4% (ESTIMATE). Weak.
- **Cluster C4: Charentsavan/Fantan interchange (Exit 10/11). White space; contrarian option.**
- **Location:** official km 30.9–31.7; centre 40.4021, 44.6748.
- **Access:** a site in a ramp-served quadrant captures both directions plus Charentsavan (24.1k, 2.4 km away). About 27k residents within 5 km.
- **Competition:** none within 2 km (0 fuel, 0 food), and no fuel for 14.6–16.5 km.
- **Land:** farmland and forest strips (OSM).
- **Risks:**
  - zero existing roadside business is disconfirming evidence of stopping propensity;
  - 1,760–1,850 m elevation;
  - only 15–20 minutes from Yerevan.
- A fuel-plus-drive-thru service area fits better than a stand-alone unit.
- **Verify:** turning counts and quadrant land.
- **Cluster C5: Hrazdan south / Kaghsi (Exits 12–14).**
- **Location:** official km 39.4–43.3; centre 40.4731, 44.7476.
- **Co-location hosts:** existing fuel pairs on both sides at km 41.5 (with café and hotel) and 42.8/42.9.
- **Two-direction reach:** median opening at km 39.4 plus the grade-separated Exits 12 and 13/14.
- **Traffic:** Hrazdan (49.8k) commuters, Tsaghkadzor ski and summer traffic, Sevan through traffic.
- **Competitors:** NeftGroup at 39.6 and the ԱԽՏԱ restaurant at 40.1, both Sevan-bound side.
- **Approach:** straight for about 1.9 km Sevan-bound and 8.2 km Yerevan-bound.
- **Verify:** which exit is signed for Tsaghkadzor; forecourt depth.
- **Clusters C6 and C7 (secondary).**
- **C6, Hrazdan east (Exit 15):** official km 46.1–48.7; centre 40.5078, 44.8019. Only Kochor café (km 47.1, Yerevan-bound side) and 2 Yerevan-bound fuel stations. Weak stopping evidence.
- **C7, Gagarin (Exit 18/19):** official km 51–54.8; centre 40.5312, 44.8654. A 24/7 fuel pair at 53.7/53.8 and several median openings; only about 3.7k residents within 5 km. Fishermen blocked the road here in December 2023. Both are secondary.
- **Cluster C8: Sevan west / Varser / M10 split (Exits 20–22). PREFERRED fuel-hybrid leisure site (ASSUMPTION).**
- **Location:** official km 56.7–60.1; centre 40.5383, 44.9190.
- **Best sides:**
  - Sevan-bound side at CPS N14-1 (58.1) or Fenka 24/7 (58.4), **before the M10 split**, to intercept all traffic to the lake, Sevan town, the Dilijan direction and Gavar/Martuni/Vardenis;
  - Yerevan-bound side at AMA Gas (57.9) or CPS (59.2) for returns.
- **Stopping evidence:** 14 fuel stations within about 2 km, the strongest stop-to-fuel evidence on the corridor.
- **Other competitors:** a fast-food outlet at 57.8 (Yerevan-bound side); Kellers beerhouse at 60.2.
- **Access:** Exit 20 at-grade, a median opening at 57.8, Exit 21/22 grade-separated, a 70→90 km/h zone and cameras at 59.3.
- **Profile:** about 29k residents within 5 km; outside the mapped national park.
- **Approach:** straight for about 1.8 km Sevan-bound and 2.3 km Yerevan-bound.
- **Verify:** forecourt depth and queuing; lease appetite; post-resurfacing access geometry (works on km 51.1–68.0 end in late August 2026).
- **Cluster C9: Sevan east / peninsula (Exits 24–26). Avoid new builds.**
- **Location:** official km 62.7–66.9; centre 40.5594, 44.9916.
- **Tourism:** the heart of Sevan tourism, with the Sevanavank turnoff at 66.6, hotels and restaurants (Kharkish, Hakobi Mot, Arevik, Garden Inn, Best Western Bohemian), and at-grade crossings at 63.5, 64.1, 65.2 and 66.8.
- **Regulatory problem:** OSM places it **inside Sevan National Park** (relation 7845661, IUCN category II). The park covers the lake side of the M4 at about km 61–70.5 and both sides at about km 62.5 and 64–67.
- **Profile:** fuel only at 62.7–63.3; seasonal.
- Only a kiosk inside an existing legal hotel or restaurant looks realistic.
- **Cluster C10: Tsovagyugh lakeshore / H-7 junction. Credible seasonal second site.**
- **Location:** official km 68–74.2; centre 40.6102, 44.9544.
- **Stopping evidence:** the strongest impulse-stop evidence on the corridor:
  - 9–10 fish stalls;
  - a food court and a 24/7 supermarket;
  - 24/7 restaurants;
  - Take Coffee and More (73.0);
  - 7 fuel sites within 2 km.
- **Traffic:** catches Dilijan-direction through traffic and H-7 east-shore traffic.
- **Access:** from km 73.8 the road is a single carriageway, so one site serves both directions; the 50–70 km/h junction zone helps entry.
- **Land:** outside the mapped park from about km 71. Farmland on the Yerevan-bound side, wood on the Sevan-bound side.
- **Profile:** about 4.4k residents within 5 km; seasonal.
- **Verify:** park boundary; winter closures of the Sevan pass and tunnel; land; fish-stall informality and enforcement (police seized more than 90 kg of whitefish on the road on 6–8 Dec 2024).
- **News context (REPORTED).**
- **6 Jun 2024:** LPG tank explosion at the 'Gaz Oil' station near Abovyan. Road Department: km 16.2; 7 injured; km 16–18 closed until about 10:00.
- **10 Sep 2025:** bridge repair at km 19.8.
- **10 Jun 2026:** Charentsavan–Kaghsi km 32.58–36.0 closed nightly 20:00–08:00, with traffic moved to the opposite carriageway.
- **24 Jul 2026:** Gagarin→Sevan resurfacing on km 51.1–68.0, AMD 1.089bn, 237,721 m², finishing late August 2026.
- **Spyur (June 2025):** 'Drive & Coffee' at Myasnikyan Ave 53/10, on the M4's urban section, listed as not operating (snippet only).
- **Traffic context (cross-reference only, not re-verified here).**
- The sibling file B1 found no post-2008 public AADT.
- The 2008 Roads Department counter at official km 10+320 read 21,505 vehicles/day (ADB TA 7208, per B1).
- B1's 2025 ESTIMATES, two-way: about 42k at the Yerevan edge; about 27k Abovyan–Charentsavan; about 21k around Hrazdan; about 17k Hrazdan–Sevan; about 9k on the lakeshore; about 5.5k Sevan–Dilijan.
- B1 found 9 interchanges and about 18 median openings, consistent with my roughly 10 and 20.
- My site ranking holds directionally under those numbers: C1 and C2 have the most traffic and residents; C8 has the most stopping; C10 has the most impulse stops.

## 2. Key data table

| Metric | Value | Period | Status | Source |
|---|---|---|---|---|
| Official M4 km vs OSM chainage (origin: Myasnikyan/Acharyan junction, 40.2079, 44.5602) | Official km = OSM chainage + 5.5 (64 Sevan-bound km posts read +5.27 to +5.68). Yerevan-bound posts count down; each pair sums to 148 km. | OSM data 2026-10-10 | REPORTED | OSM highway=milestone nodes via Overpass; Max Oil '12.2 km' station pin = OSM 6.65 (https://www.maxoil.am/oil-station/abovyan-sevan-mayrughi-12-2-km-right) |
| M4 cross-section, Yerevan city limit (official km ~10.2) to Tsovagyugh (km ~73.8) | Divided highway, mostly 2 lanes per direction (3 near Yerevan), 90 km/h, guard rails and jersey barriers mapped; single carriageway from km 73.8 toward the Dilijan tunnel | 2026-10-10 | REPORTED | OpenStreetMap via Overpass (ways ref=Մ-4; barrier ways within 25 m) |
| Interchanges and exits between the Yerevan city limit and Tsovagyugh | 15 exit groups (OSM refs 2/3 to 28), about 10 grade-separated. M10 split at official km 59.5–60.1; Sevanavank turnoff (Exit 26) at km 66.6; H-7 east-shore junction at km 73.0 | 2026-10-10 | REPORTED | OSM motorway_junction nodes and link ways |
| At-grade median openings (U-turns) on the divided section | About 20 locations; none between official km 10.2 and 18 (Ptghni–Abovyan–Arzni) | 2026-10-10 | REPORTED | OSM short links joining both carriageways |
| Road Department closure of U-turns between Ptghni and Abovyan | 4 U-turns at km 10+300, 12+150, 14+660, 16+330 closed, with traffic redirected to the Ptghni and Abovyan interchanges | Date not confirmed (likely 2023–24) | REPORTED | https://news.am/hy/news/792301 (search snippet only; page blocked 403) |
| Fuel sites within 150 m of the M4, official km 10.2–74.3 | 22 on the Sevan-bound side, 18 on the Yerevan-bound side; mostly unbranded CNG/LPG (about 35 of 48 OSM fuel objects unnamed) | 2026-10-10 | ESTIMATE | OSM via Overpass; https://cps.am/am/stations-on-map/; https://www.maxoil.am/oil-stations |
| Longest stretch with no fuel (Charentsavan section) | 14.6 km Sevan-bound (official km 25.0→39.6); 16.5 km Yerevan-bound (41.5→25.0); 0 fuel and 0 food within 2 km of the Charentsavan/Fantan interchange (km 31.3) | 2026-10-10 | ESTIMATE | OSM via Overpass |
| Fuel density at the Sevan west / Varser / M10 split (2 km radius of official km 58.3) | 10 fuel sites on the M4 (5 each side) plus 4 at the start of the M10, including CPS N14-1 Varser (km 58.1, Sevan-bound side) and Fenka 24/7 (km 58.4, Sevan-bound side) | 2026-10-10 | ESTIMATE | OSM via Overpass; https://cps.am/am/stations-on-map/ |
| Max Cafe (fuel-retailer coffee and food) on the M4 | Opened at Yerevan–Sevan highway km 12.2, Yerevan-bound side ('for drivers on the road', fast service); station list also shows Max Cafe and 'Max Drive' on the Sevan-bound side | News dated 2026-01-02 | VERIFIED | https://www.maxoil.am/news-post/max-cafe-n-nor-hasts-eowm-erewan-sewan-mayrowghi-12-2km-dzakh ; https://www.maxoil.am/oil-stations |
| Max Oil station rebranding programme (Max Cafe concept) | 10th rebranded station opened (Bagratunyats 2/8, Yerevan); first Max Cafe at Avan, Babajanyan 15/1 | 2026-07-15 | VERIFIED | https://www.maxoil.am/news |
| Coffee-specialist outlets on the corridor (≤150 m, km 10.2–74.3) | 4 coffee-tagged outlets, all on the Sevan-bound side: Ninja coffee km 10.5, Coffee Island km 25.8, Yasaman Sevan 24/7 km 68.2, Take Coffee and More km 73.0. Plus Max Cafe at km 12.2 on both sides | 2026-10-10 | REPORTED | OSM via Overpass; maxoil.am |
| Food outlets by side beyond official km 17.5 | About 20 on the Sevan-bound side vs about 7 on the Yerevan-bound side (return traffic under-served) | 2026-10-10 | ESTIMATE | OSM via Overpass (café, restaurant, fast food, food court, pub ≤150 m) |
| Roadside fish stalls and food court, Tsovagyugh lakeshore | 10 seafood stalls (official km 68.1–74.1); food court, 24/7 supermarket, services and EV charger at km 74.0–74.2 | 2026-10-10 | REPORTED | OSM via Overpass |
| Sevan National Park overlap with the M4 roadside | Lake side of the M4 inside the park at official km ~61–70.5; both sides at ~62.5 and ~64–67 (covers the Sevanavank turnoff zone) | OSM 2026-10-10 | REPORTED | OSM relation 7845661 (protect_class=2), https://www.openstreetmap.org/relation/7845661 |
| Town populations: Abovyan / Hrazdan / Charentsavan / Sevan / Byureghavan / Nor Hachn / Tsaghkadzor | 51.0k / 49.8k / 24.1k / 19.6k / 11.9k / 10.4k / 1.1k | 1 Oct 2025 | VERIFIED | Armstat bulletin, https://www.armstat.am/file/article/population_01_10_25.pdf |
| Marz populations: Kotayk / Gegharkunik | 296.1k (161.6k urban) / 217.2k | 1 Oct 2025 | VERIFIED | https://www.armstat.am/file/article/population_01_10_25.pdf |
| Large villages next to the M4 | Arinj 7,626; Nor Geghi 7,048; Tsovagyugh 4,356; Lchashen 4,301; Balahovit 3,962; Arzni 3,417; Kaghsi 2,699; Ptghni 1,915; Gagarin 1,872; Varser 1,499 | 1 Jan 2025 | VERIFIED | Armstat, Marzes in Figures 2025: https://armstat.am/file/Map/MARZ_07.pdf (Kotayk), https://armstat.am/file/Map/MARZ_05.pdf (Gegharkunik) |
| Residents within 5 km of each candidate cluster centre | C2 Abovyan–Arzni ≈ 98k; C1 Ptghni/Arinj ≈ 73.5k; C6 Hrazdan east ≈ 53k; C8 Sevan west ≈ 29k; C4 Charentsavan ≈ 27k; C9 ≈ 19.7k; C3 ≈ 13k; C5 ≈ 7.7k; C10 Tsovagyugh ≈ 4.4k | 2025 | ESTIMATE | Sum of Armstat 2025 settlement populations whose OSM place node lies within 5 km |
| Elevation profile along the M4 | 1,233 m at official km 5.5 → 1,855 m at about km 29.5 (summit near Charentsavan) → 1,780–1,850 m around Hrazdan → 1,900–1,940 m at Sevan | SRTM 30 m | ESTIMATE | https://api.opentopodata.org/v1/srtm30m (69 points at 1-km spacing) |
| M4 resurfacing, Gagarin → Sevan | Official km 51+100–68+000; AMD 1,089.3m; 237,721 m²; about 65% complete; finish late August 2026 | Reported 2026-07-24 | REPORTED | https://armenpress.am/hy/article/1256377 |
| Charentsavan–Kaghsi works | Official km 32+580–36+000 closed nightly 20:00–08:00 from 10 Jun 2026; traffic moved to the opposite carriageway | June 2026 | REPORTED | https://armenpress.am/hy/article/1252667 |
| LPG station explosion near Abovyan | 'Gaz Oil' station, M4 km 16.2 (Road Department); 7 injured; km 16–18 closed overnight | 6–7 Jun 2024 | REPORTED | https://iravaban.net/en/480481.html ; https://www.osnmedia.ru/proisshestviya/shot-v-prigorode-armyanskogo-abovyana-vzorvalas-azs/amp/ |
| Drive-format coffee precedent on the M4 urban section | 'Drive & Coffee', Myasnikyan Ave 53/10, listed as not operating (cause unknown) | Directory updated 2025-06-10 | REPORTED | https://www.spyur.am/en/companies/53990 (search snippet only; page blocked) |
| Protest disruption risk | Fishermen opposing the whitefish ban blocked the Yerevan–Sevan road at Gagarin (official km ~54) | 2023-12-15 | REPORTED | https://www.ecolur.org/en/news/sevan/15263/ |

## 4. Implications for the drive-thru concept

- **A single roadside unit captures one direction.** The M4 is a divided highway with mapped barriers from the Yerevan edge to Tsovagyugh. Unless the site sits in an interchange quadrant or at a legal median opening, apply the capture rate to directional volume: about half the two-way AADT, to be measured. Policy is moving toward closing median U-turns: there are none left between km 10.2 and 18 after a reported Road Department closure. Any plan that depends on a median opening carries closure risk.
- **Match the side of the road to the demand stream.** Morning coffee demand comes from Abovyan/Hrazdan/Charentsavan commuters on the Yerevan-bound carriageway. Weekend-morning leisure traffic is Sevan-bound. Supply is lopsided: about 20 food outlets on the Sevan-bound side vs about 7 Yerevan-bound beyond km 17.5. The best gap for a commuter coffee unit is therefore the Yerevan-bound side at Abovyan–Arzni (C2, km ~17.2–17.9), or an interchange quadrant there. That catchment, about 98k residents within 5 km, is the largest year-round demand base on the corridor (ASSUMPTION/ESTIMATE).
- **The Yerevan exit (C1, km 10.4–12.2) is no longer empty.** Max Oil opened a driver-focused Max Cafe at km 12.2 in January 2026 and lists Max Cafe on the Sevan-bound side too. Nine fuel stations, Ninja coffee, a 24/7 supermarket and two malls sit within 2 km. Fuel majors are converging on the same idea: competition, but also proof of the format and a possible partner.
- **The fuel-station hybrid is the path of least resistance.** About 40 fuel sites already have permitted direct accesses, and most are small independent CNG/LPG operators who could host a pad. CNG fills create waiting time (ASSUMPTION; verify the practice of occupants leaving the vehicle). The June 2024 LPG explosion near Abovyan (km 16.2) shows the safety, setback and insurance burden of co-locating with LPG.
- **The best leisure-traffic site without a national-park problem is Sevan west / Varser (C8, km 56.7–60.1).** Fourteen fuel stations within about 2 km show established stopping. It intercepts traffic before it splits to Sevan town, the Dilijan direction and the M10 to Gavar/Martuni/Vardenis. Candidate hosts are CPS N14-1 and Fenka 24/7 (Sevan-bound side), and AMA Gas and CPS (Yerevan-bound side).
- **Keep the peninsula out of the base case.** The most touristic point, the Sevan east / Sevanavank turnoff (C9, km 62.7–66.9), lies inside the mapped Sevan National Park (OSM, IUCN category II). A premium new-build drive-thru there faces a likely regulatory block and extreme seasonality.
- **Tsovagyugh (C10, km 68–74) has the strongest impulse-stop evidence:** fish stalls, a food court and 24/7 restaurants. Single-carriageway access from km 73.8 means one site serves both directions, and it catches Dilijan through traffic. It suits a seasonal second unit, not the flagship.
- **The only competition gap is weak evidence of demand.** Charentsavan/Fantan (C4, km 25–41, zero fuel or food within 2 km of the interchange) has almost no roadside business at all. Treat that as disconfirming evidence of stopping propensity. A fuel-plus-drive-thru service area might work; a stand-alone premium drive-thru is high risk until counts and intercept surveys prove otherwise.
- **Size the format conservatively and expect disruption.** Beyond Hrazdan, volumes are lower and more seasonal (B1 estimates about 17k AADT Hrazdan–Sevan and about 9k on the lakeshore vs about 42k at the Yerevan edge; all estimates). Winters are severe at 1,750–1,940 m. Road works (2026 resurfacing and night closures) and protest blockades (Gagarin, December 2023) interrupt trade.
- **Access engineering drives land size.** At 90 km/h a new direct access will likely need deceleration and acceleration lanes plus about 60–80 m of off-carriageway stacking for a 10–12 car queue. Plan for at least 150–250 m of frontage (ASSUMPTION; legacy SNiP-based norms to be confirmed with the Roads Department), or take over an existing forecourt access.

## 5. Data gaps & how to verify them

- **No public AADT, directional split or hourly or seasonal profile for the M4.**
- Formal data request to the Roads Department Foundation (armroad.am) and MTAI (mtad.am) for automatic counter series for 2019–2026.
- Commission 7-day classified automatic/video counts at 4–6 screenlines (official km about 13, 31, 58, 72), repeated in July–August and January–February, with 15-minute profiles by direction.
- **No turning counts at the interchanges** (Exits 2/3, 5–7, 10/11, 12–14, 21/22, 26, 28), which quadrant sites depend on. Run peak video turning counts: weekdays 07:00–10:00 and 17:00–20:00; Saturday 09:00–13:00; Sunday 15:00–21:00.
- **Unclear legal status, signage and planned closures of the roughly 20 at-grade median openings.** Obtain the Road Department or Road Police traffic-organisation schemes. Retrieve the original news.am / Road Department notice on the four Ptghni–Abovyan U-turn closures; the page was blocked and its date is unconfirmed.
- **Unconfirmed access rules.** Speed-change lane lengths, setbacks and the road-protection zone for roadside services on interstate roads were not confirmed. Check the RA Law on Roads and the relevant government decisions on arlis.am, Roads Department 'technical conditions' for new accesses, and the urban.e-gov.am permit process.
- **The legal boundary of Sevan National Park and building restrictions** at C9, C10 and the M10 shore are known only from OSM. Check with the Ministry of Environment / Sevan National Park SNCO and e-cadastre.am parcel overlays.
- **Land availability, land category and prices per cluster were not verified.** list.am, myrealty and estate pages were blocked. Unverified, undated search snippets showed M4-frontage plots at Arzni (14,000 m² for USD 91.5k ≈ USD 6.5/m²; 3,000 m² for USD 55k) and Abovyan (3,000 m² for AMD 11m). Verify through the e-cadastre, brokers and site visits.
- **Brand, ownership, hours and volumes of about 35 unnamed fuel stations**, the potential co-location hosts, are unknown. Run a drive-through photo survey, check e-register.am and Spyur, and approach owners for lease appetite.
- **No competitor performance data.** Covers Max Cafe at km 12.2 (both sides; meaning of 'Max Drive' unknown), Ninja coffee, Coffee Island, Tsovagyugh food court and Take Coffee and More. Use mystery shopping, vehicles-entering-per-hour counts and receipt-number sampling.
- **Seasonal stalls (gata, corn, fruit, fish) are not in OSM.** Run a field census on two summer weekends and one winter weekend, with GPS, photos and vehicles stopping per hour at each cluster.
- **Visibility is unmeasured.** My approach-straightness figures (plan geometry only) ignore crests, structures and signs. Measure sight distance on site in both directions and check billboard rules.
- **Tsaghkadzor routing is unconfirmed:** which Hrazdan exit (12 or 13/14) is signed for Tsaghkadzor, and how large ski-season flows are. Verify on site and with Tsaghkadzor resort and community visitor statistics.
- **Winter operability above 1,750 m is unquantified,** including Sevan pass and Dilijan tunnel closures (ADB is preparing a tunnel rehabilitation, per B1). Obtain Roads Department closure logs and Hydromet climate normals for Hrazdan and Sevan.
- **Utility connections** (power, water, sewer) at C2, C4, C8 and C10 are unknown. Make connection inquiries to Electric Networks of Armenia, Veolia Jur and the communities.
- **Km-post offset needs a field check.** My official-km offset (+5.5) is backed by 64 OSM milestone nodes and the Max Oil pin. Confirm by recording physical km posts at each cluster during the site visit, and reconcile with B1's differently-anchored chainage (+1.6).
- **The web-search budget ran out mid-task**, and several sources (news.am, civilnet, spyur, list.am) were blocked. Re-run targeted searches in a follow-up session for: Road Department U-turn policy, the Sevan coastal construction regime 2025–26, drive-thru precedents in Armenia, and Google/Yandex review counts as proxies for stopping at C1, C2, C8 and C10.
