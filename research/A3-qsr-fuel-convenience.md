# A3 — Armenian QSR, existing drive-thrus, fuel-station retail and convenience competition

*Workstream A3 of the premium drive-thru coffee & food feasibility study (Armenia). Prepared 2026-10-10. All prices are in AMD unless stated. USD conversions use the CBA rate of AMD 361.93/USD (9 Oct 2026, taken from workstream A1).*

> **Method note and limitation (read first).** The shared web-search budget for this session was used up before this workstream's first query, so **no keyword searches (English, Armenian or Russian) could be run**. Everything below therefore comes from sources opened directly:
> - company websites and ordering platforms (kfcarmenia.com, wendys.am, dodopizza.am, karas.am, mrgyros.am, coffeehouse.am, maxoil.am, flashpetrol.am, cps.am, sas.am, yerevan-city.am, zovq.am, menu.am);
> - Glovo store pages for Yerevan;
> - Yandex Maps review data;
> - Armstat PDFs;
> - Wikipedia raw pages, used only as a secondary pointer;
> - an OpenStreetMap (OSM) Overpass snapshot of Armenia (timestamp 2026-10-10 10:23 UTC; 8,371 food, fuel, retail, bank and pharmacy objects);
> - the sibling workstreams A1, A2, B1 and B2.
>
> The **news sweep for drive-thru openings and closures in 2018–2026** ("դրայվ", "драйв", "авто-кафе", "кофе с собой на трассе") **was not carried out**. Section 5 gives the exact protocol for completing it. A follow-up session with a fresh search budget should run that sweep before the "only one drive-thru exists" finding is treated as final.
>
> **Fact-check pass (2026-10-10).** An adversarial fact-check re-opened the primary sources directly (company sites, Glovo, Yandex, Armstat PDFs, the CBA rate API, raw Wikipedia text). The search budget was also exhausted for this pass, and two Overpass mirrors timed out, so the news sweep and the OSM counts are **still unchecked**. Corrections are marked inline with **[FC]**. Section 7 has the full log.
>
> **Second fact-check pass (2026-10-10).** A further adversarial check re-tested 18 figures and claims against primary sources (Glovo product JSON, coffeehouse.am, Yandex, kfcarmenia.com, maxoil.am, flashpetrol.am, cps.am, Armstat PDFs, World Coffee Portal, B2's CSV). 9 held, 6 were corrected, 1 was downgraded and 2 were wrong. Its corrections are marked inline as *Fact-check correction: …*. **Section 7** logs both passes: the first pass's [FC] items (which previously had no central log) and this pass's 18 checks. The most material change: the mainstream QSR meal is **about 2,450–3,200 AMD at list prices** (not 1,700–3,200), so a 3,500–4,500 AMD premium basket is only **1.1–1.8× mainstream** (not 1.5–2.5×).

---

## 1. Executive summary

1. **The format is already taken on the M4, not just tested.** The only drive-thru found in Armenia is the **Coffee House Drive-Thru** at about official km 12.8 of the M4 (Ptghni/Balahovit). It sits on the Sevan-bound (right) side, 31 m from a TumOil LPG station (side cross-checked against B2's TumOil row). The company branch list gives hours of 08:30–24:00 (VERIFIED as a company claim), but Yandex Maps lists the same outlet as daily 09:00–23:00, so actual hours need a field check. *Fact-check correction: hours were tagged plain VERIFIED; the two sources conflict. Either way the incumbent does not open before 08:30, so the 07:00–08:30/09:00 early-commute daypart appears uncontested by the drive-thru (Max Cafe hours at km 12.2 not verified).* Evidence suggests it opened by **late 2024**: the first Yandex review is dated 4 Dec 2024 and the branch image was uploaded 14 Aug 2024 (ESTIMATE). In Oct 2025 a reviewer wrote "Думаю это первое Драйв фру в Армении" ("I think this is the first drive-thru in Armenia") (REPORTED).
2. **The incumbent drive-thru shows weak operations, not weak demand.** It is rated 4.9★ on 123 Yandex ratings. Its 17 written reviews average only **3.76★**, however, and **4 of the 5 written in Jun–Sep 2026 are 1–2★** for 20–60-minute waits, wrong orders and rude staff (REPORTED + ESTIMATE). Queues at peak are a positive demand signal. Speed and accuracy are the clearest way for a new entrant to stand out, but a fix is cheap for Coffee House.
3. **The Yerevan exit of the M4 is already a coffee cluster.** Within 2.3 km (official km 10.5–12.8) there are four coffee points: Ninja coffee (km 10.5, right side), **Max Cafe on both carriageways at km 12.2** (Max Oil), and the Coffee House Drive-Thru (km 12.8, right side) (VERIFIED/REPORTED). Beyond Abovyan, the corridor to Sevan has few branded coffee stops. Fuel stations are dense but have little food: B2 counts **40 deduplicated fuel sites within 150 m of the M4 between km 10.2 and 74.3** (22 Sevan-bound, 18 Yerevan-bound). Its raw file has 60 fuel rows for km 5.5–74 (Yerevan → Sevan); 57 OSM-mapped rows lie within 200 m, about 34 of them unbranded (REPORTED, OSM via B2). *Fact-check correction: this previously read "60 within 200 m of the M4 on OSM, 36 of them unbranded"; 2 of the 60 rows are 243 m and 338 m away, 1 is a cps.am pin not mapped in OSM, and the data stop at Sevan (km 74), not Dilijan.*
4. **Fuel retailers are moving into coffee and food, which is the biggest threat on the highway.**
   - **Max Oil** has 56 stations (VERIFIED), of which **10** station cards carry a "Max Cafe" tag (**11** including the km 12.2 left-side unit announced in news on 2 Jan 2026) **[FC: corrected from 11/12]**. Each sells "Max Coffee", an Italian blend, plus hot dogs, and the company says it will keep expanding. The rollout is still running: the Ayntap rebrand with a Max Cafe was announced on 1 Sep 2026, and the "10th rebranded station" (Bagratunyats 2/8) on 15 Jul 2026 (VERIFIED, maxoil.am news).
   - **Shell** is present as a licensed retail brand **[FC: added]**. The official shell.am site runs on Shell's global web platform and is not a placeholder. It advertises Shell V-Power fuels, shops, car wash and a **"Shell Café"** format: "Signature Espresso" and "Signature Lungo" blends, americano, and copy reading "relax on the road, enjoy coffee" (VERIFIED, shell.am page model). The station count is unknown; OSM shows 3, all in Yerevan.
   - **Flash** has 54 stations (VERIFIED). Under its "Flash 3.0" relaunch its mission is to turn stations into "stops where energy is restored". It expanded its **Express Shops** (coffee, "Hotsters", car goods, Wi-Fi) on 29 Jan 2026, including Tsaghkadzor, and shows an **Express Cafe** format as "opening soon".
   - **CPS** claims 101 stations but lists 53 (conflict), including Ptghni, Abovyan, Hrazdan, Sevan, Varser and Dilijan, and shows no food format online. That makes CPS the most natural **hybrid partner**.
5. **International QSR is present, but none of it is drive-thru.**
   - **KFC** (since 2007, operator Derjava) has **14 restaurants**: **12 inside Yerevan city, 1 at Homplex Hyper Mall (Proshyan, Kotayk, on the Yerevan–Ashtarak road edge) and 1 in Vanadzor** **[FC: corrected from "13 in Yerevan"]**. Its own ordering platform flags `drive_thru:false` (VERIFIED as a flag). The same configuration also sets `sitin:false`, even though the restaurants have seating, so the flag describes online-ordering modes, not physical lanes. "No KFC drive-thru lane" is therefore an ESTIMATE **[FC: tag downgraded]**.
   - **Burger King** (since Jan 2017, franchisee "Burger Arm") has about 5 outlets, in malls and on Northern Ave (REPORTED).
   - **Wendy's** opened in **Dec 2025** on Abovyan St (VERIFIED). Its franchisee Wen Restaurant has agreed to open **20 restaurants by 2030** (REPORTED). The number of units open in Oct 2026 could not be checked, because the wendys.am store API requires a login **[FC]**.
   - Also present: **Pizza Hut**, **Dodo Pizza** (Yerevan and Gyumri; Food Story LLC), **Cinnabon**, and Black Star Burger (1).
   - **No evidence** was found of McDonald's, Popeyes, Subway, Domino's, Papa John's, Starbucks or Dunkin'. Baskin-Robbins was present in the past and has left. [FC: the raw Wikipedia text of all 14 brand pages was re-checked and contains 0 mentions of Armenia. This is still only weak evidence of absence, because no news check was possible.]
6. **Wendy's is the most likely future drive-thru competitor in the suburbs** (ASSUMPTION). It brings US drive-thru know-how, a 20-unit pipeline and a well-known brand. A suburban "American-style" drive-thru could face it head-on within the 5-year model horizon.
7. **QSR prices are low, which caps a premium ticket.** Prices on Glovo, Oct 2026 (REPORTED):

   | Item | Price (AMD) |
   |---|---|
   | KFC Zinger | 1,300 |
   | KFC combos | 2,800–3,200 |
   | Tashir Pizza slice | 500–600 |
   | Tashir burger | 1,300–1,350 |
   | Mr. Gyros pita gyros | 1,250–2,390 |
   | Mr. Gyros combos | 2,480–2,780 list (Glovo -30% promo: 1,736–1,946) |
   | Karas shawarma | 1,260–1,740 |
   | SAS Food Court hot dog | from 350 |

   A mainstream QSR meal costs **about 2,450–3,200 AMD (US$6.8–8.8)** at list prices (ESTIMATE: Tashir chicken burger 1,300 + fries 650 + cola 500 = 2,450; Mr. Gyros combo 2,480; KFC combos 2,800–3,200). Mass coffee is 800–1,200 AMD (US$2.2–3.3; A2). A "premium" drive-thru basket of 3,500–4,500 AMD would sit only **1.1–1.8× above mainstream** (3,500/3,200 = 1.09; 4,500/2,450 = 1.84; midpoint 4,000/2,825 ≈ 1.4×) (ESTIMATE). *Fact-check correction: the low end of 1,700 AMD came from Mr. Gyros combos at 1,736–1,946, which are Glovo -30% promotional prices (list 2,480 / 2,640 / 2,780). The earlier "1.5–2.5×" was also inconsistent with the earlier range itself (1.09–2.65×). The premium step over mainstream QSR is therefore smaller than first stated: less of a price jump for customers to accept, but also less price headroom/differentiation for a "premium" positioning. Carry the 1.1–1.8× gap into the model's price-positioning input.*
8. **There is a coffee–food gap, but it is narrow.** The QSR chains' Glovo menus (KFC, Mr. Gyros, Karas, Grill.am) list **no hot coffee**. The coffee chains (Coffee House, Max Cafe) sell only light snacks (muffins, hot dogs). No operator combines barista coffee and a real hot breakfast or lunch with car service. This gap is the strongest differentiation. Incumbents could still close it quickly: Flash shows an Express Cafe as "opening soon" (no date given, so its timing is an ASSUMPTION), and Tashir already serves omelettes at 1,000–1,500 AMD.
9. **The market is growing, but growth slowed in 2025.**
   - Food and beverage service turnover (NACE 56) was **AMD 311.7 bn in 2024** (VERIFIED, Yearbook), ≈US$794 m at A1's 2024 average of 392.66 AMD/USD (ESTIMATE). Measured from 2019 (the pre-COVID base), real growth to 2024 is about **+64% (≈10%/yr)**, including the 2022–23 relocant spike; the nominal "tripling" since 2020 starts from the COVID trough (ESTIMATE; see 3.6).
   - The preliminary 2025 figure is **AMD 298.1 bn**, a real change of **+3.1%**. Restaurants and mobile food service (56.1) grew only **+1.8%**; bars and other catering (56.2/56.3) grew **+8.5%** (VERIFIED, operational series, which is revised upward later).
   - **Accommodation and food (section I) rebounded to +13.9%** in Jan–Aug 2026 (VERIFIED for section I). *Fact-check correction: section I includes hotels, which drive much of the tourism rebound, and Armstat does not publish NACE 56 for Jan–Aug 2026. The F&B-only 2026 trend is unknown (ASSUMPTION that it is positive); do not read +13.9% as food-service growth.*
   - About **69%** of OSM fast-food points are inside Yerevan (ESTIMATE).
10. **Delivery is consolidating and competes for "convenience" spend in town, less so on the highway.** Menu.am moved onto Yandex Eats technology in **Nov 2024** (operator "Yandex Eda AM" LLC) (VERIFIED). Glovo is active, showing fees of 49–699 AMD per store and "-40% on orders over 5,000 AMD" promotions, capped at 3,000 AMD off (REPORTED). Buy.am is active. No Wolt page for Armenia was found. Delivery is a strong substitute for a suburban drive-thru and a weak one on the highway.
11. **Grocery chains add 24/7 ready-food and coffee substitutes in towns.** Yerevan City has **≈63–66 branches** (the page data holds 67 records, 66 named, with at least one duplicate), including 2 in Abovyan, 2 in Hrazdan, Jrvezh and Nor Hachn, and runs a Food Court. Zovq has 28 branches. SAS has 12, of which 9 are open 24/7, plus SAS Food Court (all VERIFIED). OSM shows Carrefour ≥15, Evrika ≥14 and Parma ≥8 (REPORTED). Coffee-to-go at these chains could not be documented online and needs fieldwork.
12. **Bottom line for the concept.** Being "first American-style drive-thru on the M4" is not available. A highway unit would compete with (a) a cheaper, known drive-thru 1 km away, (b) fuel-station cafés that already own the stop and are spreading, and (c) lakeside restaurants at the destination. The evidence favours **(i) a fuel-station hybrid with CPS or an independent CNG station** at an interchange beyond the km 10–13 cluster, or **(ii) a suburban Yerevan drive-thru built around speed and hot food** before Wendy's scales. A standalone premium highway pad is the weakest option (ASSUMPTION, to be tested in the model).

---

## 2. Key data table

| # | Metric | Value | Period | Status | Source |
|---|---|---|---|---|---|
| 1 | Drive-thru food/coffee outlets found in Armenia | **1** (Coffee House Drive-Thru, M4 km ~12.8, Sevan-bound side) | Oct 2026 | ESTIMATE (company sites, OSM, Glovo and Yandex checked; news sweep **not** done) | [21][22][23] |
| 2 | Coffee House Drive-Thru hours and coordinates | Mon–Sun 08:30–00:00 per company list; **Yandex: daily 09:00–23:00**; 40.25929 N, 44.59761 E | Oct 2026 | VERIFIED (coordinates; hours as company claim) — hours conflict with Yandex; field-check. *Fact-check correction: was plain VERIFIED* | [21][22] |
| 3 | Coffee House Drive-Thru opening | ≤ Dec 2024 (first review 4 Dec 2024; branch image file dated 14 Aug 2024) | 2024 | ESTIMATE | [21][22] |
| 4 | Coffee House Drive-Thru ratings | 4.9★ on 123 ratings; 17 text reviews averaging 3.76★ (10×5, 2×4, 1×2, 4×1); 4 of 5 reviews in Jun–Sep 2026 are 1–2★ | Dec 2024–Oct 2026 | REPORTED / ESTIMATE (average) | [22] |
| 5 | KFC Armenia restaurants | 14 (**12 Yerevan city + 1 Homplex Hyper Mall, Proshyan/Kotayk + 1 Vanadzor** [FC: was "13 Yerevan"]); ordering-platform setting `drive_thru:false` (the same config has `sitin:false`, so this is an online-ordering flag, not proof that no lane exists); 13 of 14 open at 10:00 (Northern Ave at 09:00) and 12 of 14 close at 22:00–23:00 | Oct 2026 | VERIFIED (count, hours, flag) / ESTIMATE (no physical drive-thru) | [1] |
| 6 | KFC entry year and operator | 2007; Derjava | — | REPORTED | [15] |
| 7 | KFC prices (Glovo) | Zinger/Classic 1,300; Twister 1,300; Boxmaster 1,750; combos 2,800–3,200; 22-wing basket 5,800; Coca-Cola 0.5 l 550; no hot coffee listed | Oct 2026 | REPORTED | [2] |
| 8 | Burger King | ~5 outlets; first at Dalma Garden Mall, Jan 2017; franchisee "Burger Arm"; OSM shows 4 (Northern Ave 12, Dalma, Yerevan Mall) | 2017–2025 | REPORTED (Wikipedia + OSM; sources disagree on 2017 vs 2018) | [14][23] |
| 9 | Wendy's | 1st restaurant Dec 2025, Abovyan St, Yerevan | Dec 2025 | VERIFIED (company site) | [11] |
| 10 | Wendy's pipeline | 20 restaurants by 2030 (franchisee Wen Restaurant) | Agreement Jul 2025 | REPORTED | [12] |
| 11 | McDonald's, Popeyes, Subway, Domino's, Papa John's, Starbucks, Dunkin' | No presence found | Oct 2026 | ASSUMPTION (absence in OSM and in Wikipedia country lists; [FC] raw Wikipedia text re-checked: 0 Armenia mentions; no news check possible) | [16][23] |
| 12 | Dodo Pizza | Yerevan + Gyumri; FOOD STORY LLC; pizzas "from" 1,250–1,800; iced americano 800 | Oct 2026 | VERIFIED | [18] |
| 13 | Tashir Pizza | 29 OSM points (Yerevan ~22, Abovyan, Nor Hachn, Ejmiatsin, Artashat, Gyumri, Vanadzor, Kapan); slice 500–600, burger 1,300–1,350, khachapuri 1,500, hot dog 500 | Oct 2026 | REPORTED (OSM; Glovo) | [3][23] |
| 14 | Karas | 10 branches (9 Yerevan + Abovyan, Hanrapetutyan 1/70) | Oct 2026 | VERIFIED | [19] |
| 15 | Mr. Gyros | 17 branches; founded 1 May 2009; pita gyros 1,250–2,390; **combos 2,480–2,780 list** (Glovo -30% promo: 1,736–1,946). *Fact-check correction: 1,736–1,946 were promotional prices* | Oct 2026 | VERIFIED (count) / REPORTED (prices) | [20][5] |
| 16 | Mainstream QSR meal ticket | **≈2,450–3,200 AMD (US$6.8–8.8)** at list prices; a 3,500–4,500 AMD premium basket is **1.1–1.8×** this (midpoint ≈1.4×). *Fact-check correction: was 1,700–3,200 (US$4.7–8.8), low end based on promo prices* | Oct 2026 | ESTIMATE | [2][3][5] |
| 17 | Max Oil stations / with Max Cafe | 56 listed / **10 tagged (+ km 12.2 left per news of 2 Jan 2026 → ≈11)** [FC: was 11 / ≈12]; "50+ stations, 24/7" | Oct 2026 | VERIFIED | [24] |
| 18 | Flash stations | 54 listed (53 sell Premium/Regular/Diesel, 40 propane; no CNG listed) | Oct 2026 | VERIFIED | [25] |
| 19 | Flash Express Shop / Cafe | Shops sell coffee, "Hotsters", car goods, Wi-Fi; expansion announced 29 Jan 2026 (Yerevan Andranik 113/1, Tsaghkadzor); Express Cafe "opening soon" | Jan–Oct 2026 | VERIFIED | [25] |
| 20 | CPS stations | "101" claimed vs 53 listed (M4 corridor: Verin Ptghni, Abovyan, Hrazdan, Sevan, Varser, Dilijan) | page undated (~2020+) | VERIFIED (conflict) | [26] |
| 21 | Fuel stations in Armenia (OSM lower bound) | 861 (CPS 84, Flash 66, Max Oil 39, RAN Oil 20, Gastop 11, Gulf 6, Shell 3; 532 unbranded); 284 tagged CNG | Oct 2026 | REPORTED (OSM, incomplete) | [23] |
| 22 | Fuel stations along the M4, **Yerevan → Sevan (km 5.5–74)** | **40 deduplicated sites within 150 m, km 10.2–74.3** (22 Sevan-bound + 18 Yerevan-bound; B2 headline). Raw: 60 OSM/operator rows (36 unbranded; Max Oil 5, CPS 5, Flash 2, Pro Gas 2, Gas #1 2, others 1 each); 57 OSM-mapped rows ≤200 m, ≈34 of them unbranded. *Fact-check correction: was "60 within 200 m, Yerevan → Dilijan"* | Oct 2026 | REPORTED (OSM via B2) / ESTIMATE (recount) | [37] |
| 23 | Yerevan City / Zovq / SAS | ≈63–66 (page data: 67 records, 66 named, ≥1 duplicate) / 28 / 12 (9 of SAS open 24/7) | Oct 2026 | VERIFIED | [28][29][27] |
| 24 | Food & beverage service turnover (NACE 56) | 2020: 97.8 bn; 2021: 156.8; 2022: 202.0; 2023: 273.0; **2024: 311.7 bn AMD** (real +10.9%); ≈US$794 m at 392.66. Real 2020→24 ×2.57; vs 2019 ≈ ×1.64 (+64%, ≈10%/yr) | 2020–2024 | VERIFIED (AMD) / ESTIMATE (USD, real chain) | [30] |
| 25 | Food & beverage service, 2025 (preliminary) | **298.1 bn AMD**, real +3.1%; 56.1 restaurants 235.8 bn (+1.8%); 56.2/56.3 bars and other 62.3 bn (+8.5%) | 2025 | VERIFIED | [31] |
| 26 | Accommodation & food service volume (section I, **incl. hotels**) | 281.5 bn AMD, +13.9% y/y; Aug 2026 alone +20.4% y/y. No NACE 56 line in the 2026 release, so the F&B-only trend is unknown. *Fact-check correction: not evidence that F&B service itself rebounded* | Jan–Aug 2026 | VERIFIED (section I) / ASSUMPTION (F&B-only direction) | [33] |
| 27 | Menu.am → Yandex Eats | Migrated Nov 2024 (promotion 7 Nov–1 Dec 2024); operator "Yandex Eda AM" LLC | Nov 2024 | VERIFIED | [34] |
| 28 | SAS Food Court prices (Glovo) | Hot dog 350–1,400; shawarma 1,150–1,250; burger 1,300–2,700; sandwiches 750–1,700 | Oct 2026 | REPORTED | [9] |
| 29 | OSM fast-food points | 705 nationally; 488 (69%) in the Yerevan bounding box | Oct 2026 | REPORTED / ESTIMATE (share) | [23] |

---

## 3. Detailed findings and analysis

### 3.1 International QSR brands in Armenia (2025–2026)

| Brand | Status in Armenia | Units | Since | Operator / franchisee | Format / drive-thru | Evidence and status |
|---|---|---|---|---|---|---|
| **KFC** | Present | **14**: Bagratunyats 5/3, Erebuni Mall, Yerevan Mall, Homplex Hyper Mall (Proshyan), Komitas 29, Komitas 5a, Komitas 60/2, Mega Mall, Moskovyan 17/3, Northern Ave 1, Prospect Mall (Mashtots 5), Rio Mall, Tigran Mets 15, Vanadzor | 2007 | Derjava | Malls and high streets; **ordering platform `drive_thru:false`** (also `sitin:false`, so these are online-ordering modes); takeaway and delivery on. [FC] Homplex sits in Proshyan (Kotayk, postcode 2413), on the suburban Yerevan–Ashtarak road. It is KFC's one big-box/suburban unit and the most plausible place for a future lane. | VERIFIED [1]; REPORTED [15]. OSM also shows a Gyumri KFC that is not on the official list. The KFC site's own meta description still says "Yerevan, Gyumri and Vanadzor", which suggests the unit closed recently [FC]. The old domain kfc-armenia.com now serves a casino page, so do not cite it. |
| **Burger King** | Present | ~5 (OSM 4) | Jan 2017 (Wikipedia table; its prose says 2018) | "Burger Arm" | Mall food courts (Dalma Garden Mall, Yerevan Mall) + Northern Ave 12 | REPORTED [14][23]. The Glovo page exists but showed no menu on 10 Oct 2026 [10]. |
| **Wendy's** | Present (new) | 1 confirmed; **20 planned by 2030** | Dec 2025 | Wen Restaurant | City centre, Abovyan St; pickup and partner delivery | VERIFIED: wendys.am says "In December 2025, Wendy's opened its first restaurant in Yerevan, located on Abovyan Street in the city center" [11]. The pipeline is REPORTED [12]. |
| **Pizza Hut** | Present | OSM 4 (Northern Ave, Yerevan Mall, Rio Mall area, Malatia area) | ≤2018 (Wikipedia photo) | n/f | Restaurant | REPORTED [17][23] |
| **Dodo Pizza** | Present | Yerevan + Gyumri (OSM 3) | n/f | FOOD STORY LLC | Delivery and dine-in | VERIFIED [18] |
| **Cinnabon** | Present | OSM 2 (Northern Ave area, Abovyan 36) | n/f | n/f | Kiosk/café | REPORTED [17][23] |
| Black Star Burger (RU) | Present | OSM 1 (Yerevan Mall) | n/f | n/f | Food court | REPORTED [23] |
| **McDonald's** | **Not present** | 0 | — | — | — | ASSUMPTION: Armenia is not in Wikipedia's McDonald's country list and OSM has no POI [16][23] |
| Popeyes, Subway, Domino's, Papa John's, Taco Bell, Sbarro, Carl's Jr., Hardee's, Tim Hortons, Shake Shack, Costa | Not found | 0 | — | — | — | ASSUMPTION (as above) [16][23] |
| **Starbucks / Dunkin'** | Not present | 0 | — | — | — | ASSUMPTION (absence in Armenia); A2 covers the Starbucks entry risk. **Georgia launch: REPORTED** — World Coffee Portal, 17 Jul 2026, "Alshaya Group expands licensed Starbucks business with Georgia launch" (photo caption: Starbucks at Axis Towers, Tbilisi); exact opening date is paywalled [39]. *Fact-check correction: the first pass's [FC] note called the launch UNVERIFIABLE because the Wikipedia store list omits Georgia; that was the wrong test, and the trade-press report is consistent with A2's REPORTED tag* |
| Baskin-Robbins | Exited | 0 | — | — | — | REPORTED (Wikipedia: "previously been present") [17] |

**Reading.** The international QSR brands are clustered in **central Yerevan and malls**. None runs a drive-thru. KFC, the largest, opens 13 of its 14 restaurants at 10:00 (Northern Ave at 09:00), so it does not compete for **breakfast or early commutes**; a coffee-led drive-thru would open at 07:00. The Coffee House Drive-Thru also opens no earlier than 08:30 (company list; Yandex says 09:00), so 07:00–08:30 appears uncontested on the M4 drive-thru too (Max Cafe hours not verified; field-check). This is a real daypart gap, at least in the US sense (ASSUMPTION: Armenian breakfast-out demand is unproven; see A2).

### 3.2 Local QSR chains and price points

Glovo prices were observed on 10 Oct 2026. Glovo menus can carry a markup over in-store prices; A2 estimated about +10% for Cofix. KFC and Tashir prices look like round in-store prices.

| Chain | Units (status) | Core items and prices (AMD) | Coffee on Glovo? | Corridor presence | Sources |
|---|---|---|---|---|---|
| **Tashir Pizza** | 29 OSM points (REPORTED) | Pizza slice L 500 / XL 550–600; beef burger 1,350; chicken burger 1,300; fries 650; hot dog 500 / BBQ 1,000; Adjarian khachapuri 1,500; club sandwich 2,000; wraps 1,800; omelettes 1,000–1,500; fresh juice 1,200; Coca-Cola 0.5 l 500 | Only a "coffee cup" packaging fee (40 AMD), which implies coffee is sold in store | Abovyan (Hanrapetutyan Ave), Nor Hachn | [3][23] |
| **Karas** | 10 (VERIFIED) | Chicken shawarma 1,260; pork 1,370; mega shawarma 1,580–1,740; beef burger 1,790; club sandwich 2,050; lahmajo 480–690; khorovats 2,210–3,730 | No | **Abovyan** (Hanrapetutyan 1/70); OSM also shows Tsaghkadzor (not on official list) | [4][19] |
| **Mr. Gyros** | 17 (VERIFIED) | Pita gyros 1,250–2,390; plates 3,100–3,490; burgers 1,100–2,280; **combos 2,480–2,780 list** (Gyros Combo 2,480, Gyros Burger Combo 2,640, Nuggets combo 2,780; Glovo -30% promo 1,736–1,946); fries 790. *Fact-check correction: combos were reported at the -30% promo prices; other Mr. Gyros items were not re-checked for promo flags* | No | Yerevan only | [5][20] |
| **Grill.am** | OSM 6 | Chicken shawarma in bread 700 / lavash 1,000–1,500; kebab 1,000–1,100; khorovats 1,200–4,000 | No | Yerevan | [6][23] |
| **Tumanyan Shaurma** | OSM 6 | Shawarma M/L/XL 1,300–2,050; burgers 1,600; fries 650–1,500 | No | Yerevan (24/7 central units) | [7][23] |
| **Mic Mac Burgers** | n/f | Cheeseburger 2,150; combos 3,500–4,800 (premium burger) | No | Yerevan | [8] |
| **Black Angus** | OSM 3 (count unverified) | Site says "Best Burgers in town", 11:00–02:00, delivery in Yerevan ~1 h; prices n/f | n/f | Yerevan | [23]; blackangus.am |
| **Coffee House** (coffee) | 52 listed / 57 claimed | Americano 800; cappuccino and latte 1,000; iced latte 1,000; muffin 750 | Yes | Drive-Thru km 12.8; Abovyan; Tsaghkadzor | A2; [21] |
| **SAS Food Court** (grocery ready-food) | Inside 12 SAS stores | Hot dog 350; shawarma 1,150–1,250; burgers 1,300–2,700; sandwiches 750–1,700; pizza slice 400–500 | n/f | Yerevan only | [9][27] |
| Smokehouse; KFC-style local fried-chicken chain | **Not found** (OSM, Glovo top list) | — | — | — | Gap |

**Price ladder (ESTIMATE, AMD; USD at 361.93)**

| Basket | Low | High | USD | Example |
|---|---|---|---|---|
| Street/kiosk snack | 350 | 800 | 1.0–2.2 | SAS hot dog; lahmajo; shawarma in bread |
| Mass coffee | 800 | 1,200 | 2.2–3.3 | Coffee House, Dodo iced americano |
| Mainstream QSR meal | 2,450 | 3,200 | 6.8–8.8 | Tashir chicken burger + fries + cola (2,450); Mr. Gyros combo (2,480–2,780 list); KFC combo (2,800–3,200). *Fact-check correction: low end was 1,700 (US$4.7), based on Mr. Gyros -30% promo prices* |
| Premium burger meal | 3,500 | 4,800 | 9.7–13.3 | Mic Mac combos |
| Premium specialty coffee + food (A2) | 3,500 | 4,500 | 9.7–12.4 | Surf/FEIN-type latte + sandwich |

**Implication.** A premium drive-thru ticket of 3,500–4,500 AMD is only **1.1–1.8× a list-price mainstream QSR meal** (midpoint ≈1.4×; ESTIMATE), so it overlaps the top of mainstream QSR (KFC combos 2,800–3,200) and sits level with **premium-burger** spending (Mic Mac combos 3,500–4,800). The premium step is modest, which makes trial easier but gives the "premium" label little price room to signal quality; the product itself has to carry the difference. *Fact-check correction: this previously said the premium ticket competes "not with mainstream QSR"; at list prices the gap is too small to support that.* On the highway, a family car typically buys multiple items, which could justify a higher ticket per car (ASSUMPTION; measure it in intercepts).

### 3.3 Existing drive-thrus and "car window" services

| Name | Category | Location | Format | Opened | Performance indications | Status |
|---|---|---|---|---|---|---|
| **Coffee House Drive-Thru** | Coffee + pastry | M4 Yerevan–Sevan, Ptghni/Balahovit; 40.25929, 44.59761; about official km 12.8; **Sevan-bound side**, next to a TumOil LPG station | Drive-up window, apparently also walk-up; app/"system" pre-orders get priority (Jul 2025 review) | ≤ Dec 2024 | 4.9★/123 ratings; 17 reviews; "usually busy" around 13:00 (A2); several 20–60-minute waits in summer 2026 | VERIFIED (location; hours as company claim: Mon–Sun 08:30–00:00) [21]; Yandex lists daily 09:00–23:00 [22], so hours need a field check; REPORTED (reviews) [22]; side cross-checked against B2's TumOil row (32 m; serves Yerevan → Sevan) [37]; ESTIMATE (opening). *Fact-check correction: hours were tagged plain VERIFIED* |
| KFC (any unit) | QSR | — | Ordering platform shows `drive_thru:false` | — | — | VERIFIED flag; **no drive-thru** is an ESTIMATE [1]. [FC] The same config shows `sitin:false` although the restaurants have seats, so the flag covers online-ordering modes only. Check Homplex (Proshyan) in the field. |
| Max Cafe (10–11 units [FC: was 11–12]) | Fuel-station café | Max Oil stations, incl. M4 km 12.2 both sides | Walk-in café inside the station forecourt; "Max Drive" is a **premium fuel brand, not a drive-thru** | First unit: Avan (Babajanyan 15/1); M4 units 2025–Jan 2026 | n/f | VERIFIED [24] |
| Flash Express Shop / Express Cafe | Fuel-station shop/café | Several Flash stations, incl. Tsaghkadzor | Walk-in | Expanding since 29 Jan 2026 | n/f | VERIFIED [25] |
| Bank / pharmacy drive-throughs | — | None found. One OSM ATM (ID Bank, Yerevan centre) carries `drive_through=yes`, which looks like a tagging error for a sidewalk ATM | — | — | — | REPORTED (OSM) [23]; field check needed |
| OSM-wide check | — | 0 cafés or fast-food outlets tagged `drive_through=yes`; no POI names containing drive/драйв/դրայվ/авто-кафе except "Xdrive anticafe" (Ijevan; not a drive-thru) | — | — | — | REPORTED [23] |

**Review analysis for the Coffee House Drive-Thru** [22] (REPORTED; counts and averages are ESTIMATES)

| Date | ★ | Theme |
|---|---|---|
| 2024-12-04 | 1 | Staff |
| 2025-05-17 | 5 | "I drop in almost every day"; calm even at peak (commuter use) |
| 2025-05-24 | 5 | Best coffee, good service |
| 2025-07-16 | 5 | "Very convenient format! Glad our favourite café made a coffee drive" |
| 2025-07-20 | 4 | Good drinks; in rain, staff refused to let the customer drive up because "system" (app) orders had priority |
| 2025-07-30 | 5 | Good place for coffee |
| 2025-10-24 | 5 | "I think this is the first drive-thru in Armenia" |
| 2025-11-22 / 12-16 / 2026-01-07 / 02-11 | 5 | Staff, taste |
| 2026-06-15 | 1 | Rude staff, wrong orders |
| 2026-06-20 | 1 | "Lost almost an hour": about 20 min in the queue and about 40 min waiting for drinks; items out of stock |
| 2026-08-01 | 5 | Tasty coffee |
| 2026-08-02 | 2 | Wrong drinks, slow |
| 2026-09-05 | 1 | Orders batched; 20–30 min for a simple coffee |
| 2026-10-09 | 4 | Good coffee, dirty aprons |

What the reviews show:
- **Demand exists.** There are daily commuter users and peak-time queues.
- **The operating model breaks down in peak season.** Batching, under-staffing and pre-order priority conflicts with drive-up customers all appear in summer 2026.
- **Reference point (weak):** A2 cites a Coffee Like (Russia) franchisor claim for its "Автопавильон" (car-oriented pavilion) format of revenue "from" 1.217M RUB at a 392.7 RUB average check, ≈103 checks/day if monthly (1.217M / 392.7 / 30). This is **not a drive-through benchmark**: the franchisor never says drive-through, states no period, and says the figures do not guarantee returns. *Fact-check correction: previously called "A2's Russian Coffee Like drive-through benchmark", contrary to A2's own fact-check.* If the incumbent runs at anything like that scale, waits of 20–40 minutes would suggest throughput is constrained by the bar (one or two baristas), not by lane design (ASSUMPTION).

### 3.4 Fuel-station chains: footprint and food/coffee offer

| Chain | Stations | Food / coffee format | Coffee brand and price | Hot food | M4 Yerevan–Sevan–Dilijan presence | Sources and status |
|---|---|---|---|---|---|---|
| **CPS (City Petrol Service)** | "101" claimed; 53 in published table (37 Yerevan) | None visible online; offers car servicing and coupon sales | n/f | n/f | Verin Ptghni ("Boyni" plot); Abovyan (Arzni highway No. 1); Hrazdan (Vanatur); **Sevan, Yerevanyan hwy 29**; **Varser village**; Dilijan (Gorky 54/2). OSM: 5 on M4 | VERIFIED (conflict 101 vs 53) [26]; OSM [23] |
| **Flash (Flash Petrol)** | 54 listed; OSM 66 | **Express Shop** (coffee, "Hotsters", car goods, Wi-Fi); **Express Cafe "opening soon"**; Flash 3.0 relaunch announced at a 13 Sep 30th-anniversary event (year not shown on the page; probably 2025 — ESTIMATE) | n/f (field) | Hotsters (hot-dog style) | **Sevan (Yerevanyan hwy 1, 1/2)**; Abovyan (Yerevanyan 1/17); Hrazdan (Andranik 25); **Tsaghkadzor (Mher Mkrtchyan 10, Express Shop)**; Dilijan (Kamo 80/1); OSM: 2 on M4 within 200 m | VERIFIED [25] |
| **Max Oil** | 56 listed ("50+"); OSM 39 | **Max Cafe** in **10** tagged stations [FC: was 11]: Avan Babajanyan 15/1, Bagratunyats 2/8, Halabyan 73, Khorenatsi 112, Isakov 22/2, Ulnetsi 51/5, Nork 7th district 40/1, M4 km 12.2 right, Musaler and Ayntap (both in Ararat province). The km 12.2 left unit comes from news, not a station card. First Max Cafe at Avan; "Max Coffee developed and produced in Italy for the Armenian consumer"; also outdoor seating | Price n/f | Hot dogs, pastries, "fast food" | **M4 km 12.2 left and right (both with Max Cafe)**; Abovyan Yerevanyan 1/21; Balahovit; Charentsavan; Dilijan; Gavar (M10) | VERIFIED [24]. B2 records the km 12.2 left Max Cafe news as dated 2026-01-02 [37] |
| **RAN Oil** | OSM 20 | n/f | n/f | n/f | OSM: none on M4 | REPORTED [23] |
| **Gastop** | OSM 11 | n/f | n/f | n/f | Sevan/M10 junction (B2) | REPORTED [23][37] |
| **Gulf** | OSM 6 (Yerevan, Vanadzor) | n/f | n/f | n/f | None | REPORTED [23] |
| **Shell** | OSM 3 ("Shell Armenia", one tagged operator "Fakel"). [FC: corrected] shell.am is **not** a placeholder. It is the official "Shell Armenia" site on Shell's global platform; the 5 kB HTML shell renders client-side, and the page model at shell.am/.model.json carries the content. | **Shell Café** + shops + Shell Car Wash (shell.am/station-services/shell-cafe) | "Signature Espresso" / "Signature Lungo" blends made for Shell Café; espresso, americano, latte; price n/f | n/f | None found on the M4 | VERIFIED (brand and café format, shell.am); station count n/f (OSM 3, Yerevan). Operator (Fakel?) to be confirmed |
| **Gazprom Armenia** (CNG) | OSM 1 (Gyumri); real count n/f | n/f | n/f | n/f | n/f | Gap. The company sites (gazpromarmenia.am, armenia-tr.gazprom.ru) were unreachable |
| **Lukoil** | lukoil.am redirects to lukoil.com; no Armenian station list found; OSM 0 | — | — | — | — | Gap (possible exit) |
| Independents (CNG/LPG) | **532 of 861** OSM stations unbranded; 284 tagged CNG | Typically kiosk or vending (ASSUMPTION) | n/f | n/f | **36 of 60** M4 stations unbranded | REPORTED [23][37] |

**Why fuel stations matter so much in Armenia.** Natural-gas vehicles made up more than 77% of the fleet in 2014 (REPORTED, IANGV via Wikipedia [38]; old figure). B1 found CNG at 42% of transport fuel by weight in 2007. At CNG stations passengers commonly leave the car during filling (ASSUMPTION about current practice; B1 notes it). That creates a **5–10-minute captive dwell** which a station café monetises without any drive-thru lane (ASSUMPTION on duration; measure it). Flash's own Express Shop copy says: "while your car is being filled, you can recharge yourself" [25].

**M4 food and coffee points by official km (B2/OSM; R = Sevan-bound side, L = Yerevan-bound side)** [37]

| km | Side | Outlet | Note |
|---|---|---|---|
| 5.5–7.5 | R/L | Flash ×2, Max Oil ×2, CPS, Gaz-oil, fast-food ×3 | Inside the Yerevan city limit |
| 10.0 | L | CPS | — |
| 10.5 | R | Ninja coffee (fast_food) | — |
| **12.2** | **R + L** | **Max Oil + Max Cafe (both sides)** | Fuel-forecourt café |
| **12.8** | **R** | **Coffee House Drive-Thru** (next to TumOil LPG) | The only drive-thru |
| 15.8 | L | Max Oil (Abovyan) | Abovyan town: Karas, Tashir, Coffee House, Yerevan City ×2 |
| 17–22 | R/L | YVR Gas, Gas Group, Pro Gas ×2 (Nurnus service area at km 21.5) | — |
| 23–26 | R | Unnamed café; "Coffee island" | — |
| 31–39 | — | **No fuel station on ~8 km** (Charentsavan–Hrazdan; B1) | A gap, but no access points |
| 39.6–47 | R/L | NeftGroup; cafés | Hrazdan: CPS, Flash, Yerevan City ×2 |
| 51.2 | R + L | Gas #1 (both sides) | Proposed for a stop-rate count (B1) |
| 57.8–59.2 | R/L | AMA Gas, CPS ×2, Fenka, fast food | Sevan West / Lchashen |
| 60–73 | R/L | Lakeside cafés and taverns (Van, Khoren, "Take coffee and more") | Destination dining |
| 79–94 | — | Dilijan: 27 R / 20 L café-restaurant POIs (B1) | Destination |

### 3.5 Convenience and grocery chains (coffee-to-go and ready food)

| Chain | Units | Hours | Ready food / coffee | Corridor presence | Status |
|---|---|---|---|---|---|
| **Yerevan City** ("City" LLC; founded 2007) | **63** | Several branches 24 h ("24 ժամ" labels on the shops page) | In-store **Food Court**; clay-oven (tonratan) grill items, khinkali, French bakery; app and marketplace | **Abovyan ×2** (3rd microdistrict 7/2; Ogostosi 23), **Hrazdan ×2** (Z. Andranik 66, 187), **Jrvezh**, **Nor Hachn**, Yeghvard; Ayntap highway | VERIFIED [28] |
| **Zovq** (since 1999) | **28** | n/f | Iced coffee in the catalogue; to-go coffee n/f | OSM shows 1 Zovq on the M4 corridor (B2) | VERIFIED (count) [29] |
| **SAS** | **12**, all Yerevan; 9 open 24/7 | 24/7 at 9 | **SAS Food Court** (see 3.2); bagged and instant coffee in the catalogue | None outside Yerevan | VERIFIED [27][9] |
| Carrefour (MAF) | OSM ≥15 | n/f | n/f | n/f | REPORTED [23]; carrefour.am returned 403 |
| Evrika | OSM ≥14 | n/f | n/f | n/f | REPORTED [23] |
| Tsiran | OSM ≥19 | n/f | n/f | n/f | REPORTED [23] |
| Parma | OSM ≥8 | n/f | n/f | n/f | REPORTED [23] |
| Nor Zovq | OSM ≥5 | n/f | n/f | n/f | REPORTED [23] |

Coffee-to-go machines in supermarkets: **no online evidence found**. This needs a store audit (Section 5). OSM tags 2,330 convenience stores and 613 supermarkets nationally, and B2 shows 26 convenience shops within 200 m of the M4. Many corner shops sell instant "3-in-1" coffee and some run a small espresso machine (ASSUMPTION, typical regional practice; verify).

### 3.6 Foodservice market size and trends

**Armstat, NACE I and 56, AMD million, current prices** [30][31][32][33]

| Indicator | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 (prelim.) | Jan–Aug 2026 |
|---|---|---|---|---|---|---|---|
| Accommodation & food service (I) | 114,334 | 192,615 | 257,940 | 341,131 | 383,651 (yearbook) / 348,156 (prelim.) | 367,142 | 281,501 |
| Real index, % y/y (I) | 58.1 | 161.0 | 118.0 | 122.3 | 109.5 | 104.2 | **113.9** |
| **Food & beverage service (56)** | 97,848 | 156,813 | 201,991 | 272,985 | **311,712** (yearbook) / 282,344 (prelim.) | **298,072** | n/a (section I only) |
| Real index, % y/y (56) | 63.8 | 153.6 | 118.9 | 127.1 | 110.9 (yearbook) / 108.2 (prelim.) | **103.1** | — |
| – 56.1 restaurants & mobile food service | — | — | — | — | — | 235,799 (+1.8%) | — |
| – 56.2/56.3 event catering, bars, other | — | — | — | — | — | 62,273 (+8.5%) | — |
| F&B service per capita, AMD/yr | 33,040 | 52,936 | 68,029 | 92,091 | 102,750 | — | — |

**Caveat.** Armstat's operational monthly series is revised upward in the yearbook: 2024 went from 282.3 bn preliminary to 311.7 bn final, **+10.4%** (ESTIMATE). The 2025 preliminary 298.1 bn is therefore **not comparable** with 311.7 bn. Against the 2024 preliminary it is +5.6% nominal (ESTIMATE). In USD, 2025 is about **US$771 m** at the 2025 average of 386.82 (ESTIMATE; A1's rate).

**What the series says.**
1. Eating out roughly **tripled** in nominal terms from 2020 to 2024. The 2022–23 surge came with the relocant and tourism inflow (A1).
2. **2025 was a soft year for restaurants (+1.8% real)**, whereas bars and other catering grew +8.5%.
3. 2026 is re-accelerating: section I is up +13.9% in Jan–Aug and +20.4% in August.
4. No Armstat line exists for "fast food" or "coffee shops". Those would need SRC taxpayer data by NACE 56.10 and 56.30, or a Euromonitor purchase. **No public Euromonitor or Statista figure was opened** (search unavailable).

**Delivery platforms (2024–2026)**

| Platform | Status | Evidence | Status tag |
|---|---|---|---|
| **Yandex Eats** (incl. former Menu.am) | Menu.am "now powered by Yandex Eats technology"; operator "Yandex Eda AM" LLC; switch-over promotion 7 Nov–1 Dec 2024 | [34] | VERIFIED |
| **Glovo** | Active in Yerevan (food, groceries, pharmacy, shops); KFC 99% recommend, fee shown 49 AMD (probably the delivery fee), "-40% on orders over 5,000 AMD"; Tashir 92%, fee 99 AMD; SAS Food Court 98%, fee 699 AMD; Glovo Prime available | [2][3][9][10] | REPORTED |
| **Buy.am** | Active ("Restaurants", "Mall") | [35] | VERIFIED (site live) |
| Wolt | No Armenian city page (wolt.com/en/arm → 404) | [36] | REPORTED (weak evidence of absence) |
| Order volumes / GMV | Not found | — | Gap |

### 3.7 Who is the real competitive set?

| Dimension | **Highway drive-thru (M4, beyond Yerevan)** | **Suburban drive-thru (Yerevan NE districts, ring roads, exits)** |
|---|---|---|
| Direct same-format | **Coffee House Drive-Thru** (km 12.8 R; mass prices; known brand) | Coffee House Drive-Thru is the only one today; **Wendy's** (20 units by 2030) is the most plausible next drive-thru operator (ASSUMPTION) |
| Near-direct (same occasion, walk-in) | **Max Cafe km 12.2 (both sides)**; Flash Express Shop (Sevan, Abovyan, Hrazdan, Tsaghkadzor; Express Cafe coming); CPS/independent CNG kiosks; Ninja coffee | Coffee House (42 Yerevan kiosks); Cofix; Max Cafe ×7 at urban Yerevan stations (Avan, Bagratunyats, Halabyan, Khorenatsi, Isakov, Ulnetsi, Nork) [FC: was ×8; the Arshakunyats 28/7 card lists LPG only, with no Max Cafe]; Shell Café (Shell stations, Yerevan) [FC: added]; KFC 13; BK ~5; Tashir ~22; Mr. Gyros 17; Karas 9; shawarma kiosks |
| Destination substitutes | Lakeside restaurants and taverns (Sevan km 57–73), Dilijan cafés (≈47 POIs), Tsaghkadzor resort cafés, picnics and home-made coffee | Malls (food courts), SAS/Yerevan City food courts, office coffee |
| Delivery substitute | Weak (en route) | **Strong**: Glovo/Yandex Eats with -40% promotions |
| Price anchor | 800–1,200 AMD coffee; hot dog 350–1,000 | Same + QSR meal 1,700–3,200 |
| Who owns the "stop" | **Fuel stations** (CNG dwell, toilets, parking) | Malls and kiosks |

**How incumbents could respond (ASSUMPTIONS, each rated on available evidence)**

| Incumbent | Likely response | Capability | Speed |
|---|---|---|---|
| Coffee House | Fix drive-thru staffing; add a second drive-thru (e.g., Sevan-bound beyond Abovyan or the Yerevan-bound side); price promotions; FEIN premium line | High: 52 branches, roastery, app with pre-order already working | Months |
| Max Oil | Upgrade Max Cafe food and add a pickup window; has already put cafés on both M4 carriageways at km 12.2 and states it will keep expanding | High (owns land and stations) | Months |
| Flash | Roll out Express Cafe on corridor stations (Sevan, Abovyan, Hrazdan, Tsaghkadzor) | High (Flash 3.0 programme under way) | 6–12 months |
| CPS | Partner with a third-party café, or do nothing (no food concept visible) | Medium | Unknown; **partner opportunity** |
| Wendy's / KFC / BK | Suburban freestanding units with drive-thru lanes | Medium–high (franchise playbooks); constrained by Yerevan land and permits | 1–3 years |
| Tashir / Karas | Add coffee and breakfast at Abovyan/Hrazdan units; price war | Medium | Months |

---

## 4. Implications for the drive-thru concept (critical)

1. **The "first mover" thesis fails on the M4.** A same-format, well-known, cheaper competitor has operated at the Yerevan exit since about 2024. Any investor narrative claiming first-mover advantage on the corridor would be factually wrong. Differentiation has to come from **speed, accuracy, food and experience**, all of which incumbents can copy.
2. **The km 10–13 cluster should be avoided.** It already holds three coffee businesses and four coffee points, including Max Cafe on both carriageways. A new unit there would mostly cannibalise rather than create demand. If the highway is chosen, sites **after Abovyan** are less contested. B1's candidates are Charentsavan/Fantan (km 31), Hrazdan interchanges (39–47), Gagarin (54) and Sevan W (59). The trade-offs are lower traffic and more seasonality.
3. **Fuel stations are both the main competitor and the best channel.** They own the dwell time (CNG), toilets and permits. Max Oil and Flash are building their own cafés, and Shell already markets a "Shell Café" in Armenia [FC]; CPS has no visible concept and the largest network on paper (53–101 stations, 5 on the M4). **A CPS or independent-CNG hybrid** with a drive-up window could cut land and permit risk and inherit traffic. The model should run it as a scenario with rent or revenue share.
4. **A premium price has to be earned on a low price base.** Mass coffee is 800–1,200 AMD and a QSR meal 1,700–3,200 AMD. At a 3,500–4,500 AMD ticket, the format must deliver a visibly better product: hot breakfast and lunch, iced and signature drinks, and family bundles. The menu needs an entry tier (≤1,200 AMD coffee, ≤1,500 AMD food item) to avoid being a niche "special occasion" stop (ASSUMPTION; test with conjoint or intercepts).
5. **The coffee + hot-food combination is the clearest white space, but it is time-limited.** No QSR chain sells coffee in its delivery menu, and no coffee chain sells real hot meals. Flash's Express Cafe ("opening soon") and Max Cafe's "fast food" push could close the gap on the highway within 6–12 months.
6. **The suburban option carries a new, specific threat: Wendy's.** Wendy's arrived in Dec 2025 with a 20-unit plan. If Wen Restaurant opens freestanding units with lanes, a local "American-style" drive-thru meets the original American brand in its home format. Securing 1–2 prime suburban pads early (NE Yerevan exits, Avan/Nor Nork, Ajapnyak/Davtashen ring, Arshakunyats–airport road) is a timing play (ASSUMPTION).
7. **Throughput is the operational make-or-break, and the incumbent's reviews prove it.** Peak-season waits of 20–60 minutes at the Coffee House Drive-Thru show that a single-window, barista-bound format saturates. The model should cap capacity at realistic cars per hour (e.g., 30–45/h at peak per window with batch brewing and pre-order; ASSUMPTION to calibrate with equipment workstream C2). It should not assume US-style 100+ cars per hour.
8. **Market growth is real but cyclical.** Food and beverage service tripled in 2020–24, flattened in 2025 (+3.1%, restaurants +1.8%) and rebounded in 2026. The 5-year model should not extrapolate the 2022–23 surge. A base of +5–8% real per year with downside years is more defensible (ASSUMPTION, aligned with A1's macro view).
9. **Delivery apps blunt the suburban convenience edge.** With -40% Glovo promotions and Yandex Eats consolidation, the suburban drive-thru has to win the **"in the car anyway"** occasion (commute, school run), not the at-home occasion.
10. **Disconfirming evidence to watch.**
    - The Coffee House Drive-Thru's 4.9★ on 123 ratings and daily-commuter reviews suggest that **local customers accept the drive-thru format quickly**. This is positive for the concept but also for the incumbent.
    - Conversely, it remains the only drive-thru after about 2 years, and Coffee House has **not opened a second one** among its 52 branches. That could mean the economics are marginal (ASSUMPTION; ask the company).

---

## 5. Data gaps and how to verify them

| Gap | Why it matters | Verification method |
|---|---|---|
| **Complete inventory of drive-thrus and openings/closures 2018–2026** (news sweep not done) | Confirms or refutes "only one drive-thru" | Search news.am, armenpress.am, arka.am, banks.am, hetq.am, civilnet.am, mediamax.am, evnreport.com, plus Facebook/Instagram, for: "դրայվ թրու", "դրայվ-թրու", "ավտոսրճարան", "драйв-тру", "драйв фру", "авто-кафе", "кофе с собой на трассе", "drive-thru Yerevan", "drive through Armenia", 2018–2026. Check Yandex Maps and Google Maps "drive-through" attributes for Yerevan, Kotayk and Gegharkunik. Phone KFC (+374 11 505505), Wen Restaurant (Wendy's) and Burger Arm to ask about drive-thru plans. |
| Coffee House Drive-Thru: opening date, cars/day, ticket, seasonality, staffing | Direct demand benchmark on the M4 | Management interview. Fieldwork: count cars per hour, order-to-handover time and queue length, 3 weekdays + 2 weekend days × 3 dayparts, in summer and winter (as in A2). Plate sampling to infer origin. |
| **Fuel-station coffee prices, machines and dwell time** (Max Cafe, Flash Express, CPS, independents) | Price anchor on the highway; hybrid economics | Mystery shopping at M4 km 12.2 (both sides), Sevan CPS/Flash, Abovyan Max/Flash, Hrazdan, Gas #1 km 51. Record espresso/cappuccino price and size, machine brand (bean-to-cup vs barista), food range, seats, toilets. Time CNG fills (n ≥ 50). |
| Max Cafe and Flash Express unit counts and roll-out plans | Pace of incumbent response | Interviews; monitor maxoil.am/news and flashpetrol.am/news monthly; Flash Express Cafe launch date. |
| CPS real station count (101 vs 53) and openness to partnership | Hybrid scenario | Call CPS HQ (+374 60 703300). Request a list of M4 stations with plot sizes and any lease terms. |
| Gazprom Armenia CNG station count and retail offer; Lukoil status | Highway competitive map | Gazprom Armenia annual report. PSRC (psrc.am) CNG licence register. Site visits. |
| National fuel-station count (official) | Market structure | State Revenue Committee: number of taxpayers under NACE 47.30 (retail of automotive fuel), 2023–2025. Ministry of Economy / Market Surveillance Inspectorate registers. |
| Burger King count and prices; Wendy's prices, units, formats; Black Angus count; Tashir Pizza count | Suburban competitive set; price ladder | Store visits or menu photos. Yandex/Glovo menu capture. e-register.am company extracts (Burger Arm, Wen Restaurant, FOOD STORY LLC, Derjava). Ask Tashir Group. |
| Local fried-chicken or "Smokehouse"-type chains | Completeness | Glovo and Yandex Eats category scrape (chicken, burgers); 2GIS/Yandex chain pages. |
| Coffee-to-go in supermarkets (Yerevan City, SAS, Zovq, Carrefour) | Substitute pricing | Store audit of 10 stores, including Abovyan and Hrazdan Yerevan City. |
| Fast-food and coffee-shop turnover (NACE 56.10/56.30) and outlet counts | Market sizing | SRC request for turnover and taxpayer counts by 4-digit NACE, 2019–2025. Armstat special tabulation. Check whether Euromonitor Passport "Consumer Foodservice" covers Armenia (unknown); if not, use Georgia as a proxy, with caveats. |
| Delivery market size (orders, GMV) and app shares | Suburban substitute strength | Interviews with Glovo and Yandex Eda AM. Card-spend data by MCC 5814 from a bank (Ameriabank, Inecobank) or Idram/Telcell. |
| Shell-branded stations (OSM "Shell Armenia/Fakel") | [FC] The brand is confirmed present, with a "Shell Café" format (shell.am). It is an international fuel retailer with a strong convenience model | Site visit to OSM coordinates 40.1567, 44.4019 and 40.2344, 44.5524. Record station count, Shell Café coffee prices and machine type, and the operator/licensee. Check for expansion plans toward the M4. |

---

## 6. Sources

All accessed 2026-10-10 unless noted. Publication dates are given where the page shows them.

1. KFC Armenia, *Restaurants* (14 stores; platform settings `drive_thru:false`). https://www.kfcarmenia.com/en/stores
2. Glovo Yerevan, *KFC* store page (menu and prices). https://glovoapp.com/en/am/yerevan/stores/kfc-yrv
3. Glovo Yerevan, *Tashir Pizza*. https://glovoapp.com/en/am/yerevan/stores/tashir-pizza
4. Glovo Yerevan, *Karas*. https://glovoapp.com/en/am/yerevan/stores/karas-yvn
5. Glovo Yerevan, *Mr. GYROS*. https://glovoapp.com/en/am/yerevan/stores/mr-gyros-yrv
6. Glovo Yerevan, *Grill.am*. https://glovoapp.com/en/am/yerevan/stores/grillam
7. Glovo Yerevan, *Tumanyan Shaurma*. https://glovoapp.com/en/am/yerevan/stores/tumanyan-shaurma
8. Glovo Yerevan, *Mic Mac Burgers*. https://glovoapp.com/en/am/yerevan/stores/mic-mac-burgers-yrv
9. Glovo Yerevan, *SAS Food Court*. https://glovoapp.com/en/am/yerevan/stores/sas-food-court-yrv
10. Glovo Yerevan, *Burger King* page (no menu shown) https://glovoapp.com/en/am/yerevan/stores/burger-king-yrv ; food category listing https://glovoapp.com/en/am/yerevan/categories/food_1
11. Wendy's Armenia website and app bundle ("In December 2025, Wendy's opened its first restaurant in Yerevan, located on Abovyan Street…"). https://wendys.am/ (text in the site's JS asset bundle)
12. Verdict Food Service via Yahoo Finance, "Wendy's agrees to open 190 restaurants in Italy and Armenia", 16 Jul 2025. https://finance.yahoo.com/news/wendy-agrees-open-190-restaurants-084334852.html
13. Wikipedia, *Wendy's* (cites CivilNet, "Wendy's opens its first restaurant in Armenia", 5 Dec 2025, https://www.civilnet.am/en/news/990560/wendys-opens-its-first-restaurant-in-armenia/ — returned 403, not opened). https://en.wikipedia.org/wiki/Wendy%27s
14. Wikipedia, *List of countries with Burger King franchises* (Armenia: 2017, 5 outlets, "Burger Arm"; cites Dream Armenia, 14 Jan 2017). https://en.wikipedia.org/wiki/List_of_countries_with_Burger_King_franchises
15. Wikipedia, *List of countries with KFC franchises* (Armenia: 2007, 14, Derjava; cites kfcarmenia.com, accessed Jul 2026). https://en.wikipedia.org/wiki/List_of_countries_with_KFC_franchises
16. Wikipedia: *List of countries with McDonald's restaurants*; *Popeyes*; *Subway (restaurant)*; *Domino's*; *Papa John's*; *Starbucks*; *Taco Bell*; *Sbarro*; *Carl's Jr.*; *Hardee's*; *Tim Hortons*; *Shake Shack*; *Costa Coffee*. None mentions Armenia. https://en.wikipedia.org/wiki/List_of_countries_with_McDonald%27s_restaurants (and the respective article URLs)
17. Wikipedia: *Pizza Hut* (photo, Yerevan 2018); *Cinnabon* (Armenia listed); *Dodo Pizza* (Armenia listed); *Baskin-Robbins* ("previously been present… Armenia"). https://en.wikipedia.org/wiki/Pizza_Hut ; https://en.wikipedia.org/wiki/Cinnabon ; https://en.wikipedia.org/wiki/Dodo_Pizza ; https://en.wikipedia.org/wiki/Baskin-Robbins
18. Dodo Pizza Armenia: Yerevan menu https://dodopizza.am/yerevan ; contacts (FOOD STORY LLC) https://dodopizza.am/yerevan/contacts
19. Karas, *Branches* (10 listed). https://www.karas.am/am/contact
20. Mr. GYROS, home page ("17 branches"; founded 1 May 2009). https://www.mrgyros.am/
21. Coffee House Company, *Branches* (Drive-Thru, 40.259288803530474, 44.597612144949885; image file "screenshot-2024-08-14"). https://coffeehouse.am/en/branches
22. Yandex Maps, *Coffee House Drive-Thru* reviews (rating 4.9, 123 ratings, 17 reviews; review dates 4 Dec 2024–9 Oct 2026). https://yandex.com/maps/org/coffee_house_drive_thru/240062017669/reviews/
23. OpenStreetMap via the Overpass API (maps.mail.ru mirror), Armenia area query for amenity = fast_food/restaurant/cafe/fuel/pharmacy/bank/food_court/ice_cream, shop = convenience/supermarket/bakery/kiosk/coffee, and drive_through/drive_in tags. OSM base timestamp 2026-10-10T10:23:31Z; 8,371 elements. https://maps.mail.ru/osm/tools/overpass/api/interpreter (ODbL)
24. Max Oil: home https://www.maxoil.am/ ; stations https://www.maxoil.am/oil-stations ; Max Cafe https://www.maxoil.am/max-cafe ; fuel / Max Drive https://www.maxoil.am/fuel ; news "Max Cafe at Yerevan–Sevan highway 12.2 km left" https://www.maxoil.am/news-post/max-cafe-n-nor-hasts-eowm-erewan-sewan-mayrowghi-12-2km-dzakh ; first Max Cafe (Avan) https://www.maxoil.am/news-post/max-oil-expands-retail-presence-with-new-1-max-cafe
25. Flash Petrol: stations https://www.flashpetrol.am/am/stations ; Express Shop https://www.flashpetrol.am/am/express-shop ; Express Cafe https://www.flashpetrol.am/am/express-cafe ; about / Flash 3.0 https://www.flashpetrol.am/am/about ; news "Flash expands its Express Shops", 29 Jan 2026 https://www.flashpetrol.am/am/news/26 ; 30th-anniversary / Flash 3.0 launch https://www.flashpetrol.am/am/news/5
26. CPS (City Petrol Service): petrol-station network (101 claimed; table of 53) https://cps.am/am/content/chain-of-petrol-stations/ ; company profile https://cps.am/am/content/company-profile/
27. SAS Supermarket, *Our supermarkets* (12; 9 open 24/7). https://www.sas.am/about/our-supermarkets/
28. Yerevan City: *Branches* (63 records in page data) https://www.yerevan-city.am/shop/shops ; about https://www.yerevan-city.am/shop/about ; https://yerevan-city.am/llms.txt
29. Zovq Supermarkets, home page ("28 branches"; since 1999). https://zovq.am/
30. Armstat, *Statistical Yearbook of Armenia 2025*, ch. 16 "Trade and other services", tables 16.14, 16.16, 16.17. https://armstat.am/file/doc/99563713.pdf
31. Armstat, *Socio-economic situation of RA, January–December 2025*, section 1.2.6.2 Services (NACE 55/56/56.1/56.2–56.3). https://armstat.am/file/article/sv_12_25r_126.pdf
32. Armstat, *Socio-economic situation of RA, January–December 2024*, section 1.2.6.2 Services. https://armstat.am/file/article/sv_12_24r_126.pdf
33. Armstat, *Socio-economic situation of RA, January–August 2026*, section 1.2.6.2 Services (published Sep 2026). https://armstat.am/file/article/sv_08_26r_126.pdf
34. Menu.am landing page ("Рестораны Menu.am переехали в Яндекс Еду"; promotion valid 07.11.2024–01.12.2024; operator ООО «Яндекс Еда ЭйЭм»). https://menu.am/
35. Buy.am home page. https://buy.am/
36. Wolt, /en/arm → 404. https://wolt.com/en/arm
37. Sibling workstreams, this repository: B2 *M4 POIs* (`research/B2-m4-pois.csv`, OSM 2026-10-10, with maxoil.am cross-references); B1 *M4 traffic* (`research/B1-m4-traffic.md`); A2 *Coffee market* (`research/A2-coffee-market.md`); A1 *Macro & consumer* (`research/A1-macro-consumer.md`, incl. CBA AMD/USD 361.93 on 9 Oct 2026).
38. Wikipedia, *Natural gas vehicle* (Armenia NGV share > 77% in 2014, citing IANGV). https://en.wikipedia.org/wiki/Natural_gas_vehicle
