# A4: Armenian Food & Beverage Preferences and Menu Localization for a Drive-Thru

*Research date: 2026-10-10. Analyst workstream A4 of the drive-thru feasibility study.*

*FX for USD conversions: 1 USD = 361.93 AMD (CBA official rate, 9 Oct 2026, taken from workstream A1). AMD prices include VAT unless stated.*

*Status tags:*
- *VERIFIED: a primary or official source that we opened (company website or own e-shop, official statistics, a peer-reviewed paper read in full).*
- *REPORTED: a credible secondary source (delivery-aggregator menu, Wikipedia, crowdsourced price site).*
- *ESTIMATE: our own calculation, with the formula shown.*
- *ASSUMPTION: a judgment, with its basis stated.*

> **Process note (read first).** The shared WebSearch budget for this run was used up before this workstream started; the first search returned "budget used up". Nothing in this file comes from a search engine or from memory. The evidence comes from four other routes:
> 1. **Direct fetches of known primary pages.** Glovo Yerevan store menus; SAS supermarket's own e-shop catalogue; Grand Candy's own e-shop; Karas, Max Oil and Ashtarak Kat websites; CRRC Caucasus Barometer 2024 online data; Numbeo.
> 2. **The PubMed literature database**, through which we read three Armenian dietary papers in full and three more as abstracts.
> 3. **Wikipedia**, for background only.
> 4. **The sibling workstreams** A1 (macro/consumer), A2 (coffee market), B1 (M4 traffic) and B2 (M4 points of interest).
>
> Several sites could not be reached: tashirpizza.am (HTTP 403), ponchikmonchik.am (522), kaghtsr.am and dustrmargo.am (DNS failure), marianna.am (503), yasaman.am (empty page), menu.am (Yandex captcha), Yandex Maps (timeout) and the OpenStreetMap Overpass mirrors (500/reset).
>
> As a result, the following are **not covered by any source** and are listed as gaps in §5: Mayak ponchik, Sevan roadside fish, crayfish, corn and gata prices, consumer surveys on coffee frequency, and any energy-drink age restriction.
>
> Glovo prices are delivery-platform prices. They may sit about 0–10% above in-store prices; A2 estimated about +10% for Cofix. We treat them as REPORTED and as an upper bound on in-store prices.

> **Fact-check (2026-10-10).** An adversarial check re-tested 22 claims against the primary sources (PMC papers, CRRC CB 2024, Armstat ILCS 2024, Numbeo, Grand Candy, SAS, Karas, Max Oil and Glovo menus). 16 were confirmed, 5 corrected and 1 downgraded. The main fix is the VAT basis of the §3.11 food-cost percentages (overstated by ≈1.2×); the average-ticket estimate is downgraded pending reconciliation with A2, A3 and C2. Corrections are marked inline as *Fact-check correction*; the full log is in §7.

---

## 1. Executive summary

1. **Armenians eat dough first. The menu should be built on hand-held baked goods, not on burgers or American breakfast plates.**
   - In the first nationally representative 24-hour recall (n = 1,400 adults), bread and flour products supply **53% of energy**. 1,230 of 1,400 respondents (88%) ate them on the recall day; the paper's text says about 96%.
   - **40%** ate biscuits, cakes, pastries or waffles that day. Mean energy intake is low, at 1,738 kcal/day (VERIFIED [35]).
   - In a Yerevan fast-food frequency survey (FFQ, autumn 2019, n = 423), **pastry was the most-consumed fast food** at 76 g/day, ahead of fried chicken (53 g), hot dog/burger (50 g) and shawarma (49 g). Dough-based items made up about 41% of fast-food grams (VERIFIED [34]; ESTIMATE for the share: pastry 76.1 + pancake/doughnut 41.4 + pie 35.0 + khachapuri 32.2 = 184.7 g ÷ 449.8 g for all 11 items = 41.1%; counting pizza 33.9 g as dough-based gives 48.6%, so 41% is the conservative definition). *Fact-check note: formula added; figure confirmed.*
2. **Eating out, and fast food in particular, is infrequent and low-spend. This is the main disconfirming evidence for a high-ticket concept.**
   - In the 2019 Yerevan FFQ, mean fast-food frequency was about **once a week** (range 0.38–1.93 per week). That is below the US benchmark the authors cite (2.07 per week), and the sample was 90% university-educated, so the true figure may be lower (VERIFIED [34]).
   - The household survey shows food away from home at only **2.8% of consumption nationally and 3.5% in urban areas** (≈1,709 / 2,293 AMD per person per month; ILCS 2024, via A1 [44]). *Fact-check note: figures confirmed against Armstat Tables 3.5–3.6, but they are a survey floor, not a hard cap. A1 shows 2024 food-service turnover implies ≈8,444 AMD per resident per month, about 5× the ILCS figure, because ILCS misses tourists, business spending and high-income non-response. For a highway site serving travellers, treat 2.8–3.5% as the typical household's willingness to spend, not as a ceiling on the ticket.*
   - In Caucasus Barometer 2024, **38%** of households say money is enough "for food only" or "not even for food". Only **19%** can afford durables or "anything" (VERIFIED [29]).
3. **The local price anchors for snack food are very low, and they are visible in supermarkets on the way.** All prices are AMD, Oct 2026:

   | Item | Price range | Examples (status) |
   |---|---|---|
   | Filled ponchik | 130–150 (round mini 80) | Grand Candy "Ponchikanoc" (VERIFIED [15]) |
   | Karkandak (piroshki-type pies) | 100–690 | — |
   | Gata | 250–430 per small piece | — |
   | Lahmajo | 480–1,000 | Café ceiling 2,200 at Jazzve |
   | Zhingyalov hats | 400–1,200 | — |
   | Imeruli khachapuri piece | 400–600 | — |
   | Shawarma | 1,150–1,350 standard; up to 2,350 double | — |
   | Hot dog | 300–1,400 | — |
   | Supermarket sandwich | 1,090–1,350 | — |
   | Café sandwich | 2,400–4,400 | — |

   Sources are REPORTED from Glovo and VERIFIED from the SAS and Grand Candy e-shops, §3.3. A drive-thru cannot charge a large premium for a commodity local pastry. The premium has to come from convenience, freshness, speed and bundling.
4. **American donuts have a low local price anchor, and that anchor makes them risky.** KFC Armenia already sells filled donuts at 650 AMD and Cofix at 880 AMD (Glovo). A Grand Candy ponchik costs 150 AMD. A US-style donut at 800–1,000 AMD is therefore **5–7 times the local ponchik price** (ESTIMATE). A "fresh-filled Armenian ponchik" at 350–450 AMD is the safer play (ASSUMPTION).
5. **The sweet iced-coffee niche is already served cheaply. A US-style menu and price level face strong local substitutes.**
   - Coffee House sells Kinder/Nutella drinks, frappés and shakes at 1,400 AMD, smoothies at 1,100 AMD, matcha at 1,000–1,300 AMD and protein shakes at 1,600 AMD (Glovo [7]). *Fact-check correction: matcha range was 1,000–1,100; cream-cheese matcha latte and sky matcha are 1,300.* It also runs an M4 drive-thru (A2).
   - Cofix lists 12 iced coffee SKUs on Glovo at 550–1,760 AMD [8].
   - SAS stocks **65 ready-to-drink iced coffee SKUs**, 28 of them Armenian-made, including Starbucks ready-to-drink coffee at 1,250 AMD for 220 ml (VERIFIED [23]).
6. **The energy-drink habit is visible, and retail prices put a ceiling on a Dutch Bros-style "Rebel" drink.**
   - SAS stocks about **75–85 energy-drink SKUs** within a 151–153 SKU "cocktails, energy drinks, low-alcohol beverages" category. Energy brands include Burn, Red Bull, Monster, Adrenaline Rush, Lit, Jaguar, Revo, Gorilla, Flash Up, Max Power and Boom. *Fact-check correction: was "energy/cocktail category holds 151 SKUs"; the category also contains alcoholic RTD brands (Absolut, Bacardi, Jack Daniel's, Smirnoff, Le Coq, Очаково, Santo Stefano, etc.), and summing energy-brand counts gives only ≈75–85.*
   - Retail prices run from **280 to 990 AMD** per can. A 250 ml Red Bull is 670 AMD and a 500 ml Monster is 990 AMD (VERIFIED [22]). KFC sells Burn at 800 AMD [6]. *Fact-check note: the Max Power 280 AMD lower bound was not on page 1 at re-check and could not be re-seen; the lowest re-confirmed can is Boom 450 ml at 340 AMD.*
   - A customised energy drink at 1,500–1,800 AMD is 2–3 times the price of a can. We estimate its food cost at about **33–40%** of the menu price when built on retail cans (Burn base ≈33%, Red Bull base ≈40%), against about 25% for lemonade (ESTIMATE, §3.11). *Fact-check correction: was 40–50% vs ≈30%; §3.11 compared VAT-inclusive cost with ex-VAT price and mis-added the Rebel cost (643, not 660 AMD).*
   - We could not verify any age-of-sale rule for energy drinks (gap).
7. **The health and alternative-milk trend is real and supplied locally.**
   - SAS lists **24 plant-milk SKUs, 5 of them barista grade**. Examples are Alpro Barista Oat at 1,410 AMD/L, OraSi Barista at 1,840–2,090 AMD/L, Valsoia, and Nushanush, a local almond milk.
   - It also stocks lactose-free milk (Parmalat, Lactel: 1,440–1,590 AMD/L) and protein croissants (VERIFIED [18][19][16]).
   - Oat milk costs about **115 AMD more per 150 ml drink** than Marianna whole milk (ESTIMATE). A 200–300 AMD surcharge covers it.
8. **Religious fasting is too rare to justify a dedicated Lent menu.** Among denomination members, only **4% "always/often" fast** when their religion requires it, and 83% never do (CB 2024, VERIFIED [32]). Vegetarian zhingyalov hats should be a year-round differentiator, not a Lent product.
9. **Sevan roadside food (fish, crayfish, gata) is a separate trade, sited further up the road.**
   - OSM shows a cluster of **10 roadside seafood stalls at M4 km ≈68–74**, past Sevan town towards Dilijan. This is beyond the high-volume Yerevan–Charentsavan stretch identified in B1 (REPORTED, OSM via B2 [47]).
   - Commercial fishing of the native Sevan trout (*ishkhan*) was stopped in **1976**, and Wikipedia's species page lists it as extinct under IUCN 3.1 (REPORTED [40]). Any "ishkhan" sold today is very likely farmed (ASSUMPTION).
   - Fish should **not** be on a drive-thru menu: only 2% of adults ate fish on the recall day [35], and fish brings odour, cooking-time and supply-legality risks.
   - Dried-fruit stands are a food-safety risk to avoid. A 2026 study found aflatoxin levels above EU limits in dried fruit from Yerevan open markets (VERIFIED abstract [39]).
10. **Local supply is deep enough to run an outsourced pastry model on day one.** Verified suppliers and brands:
    - **Bakery and pastry:** Grand Candy (19 Yerevan stores, 470 catalogue entries); SAS Sweet/SAS Product private label (52 bakery SKUs); Nor-Nar (Gavar gata); Zeytun; Levrim; Tnakan (ready pies); Karas (10 branches, including Abovyan on the M4 corridor; the Abovyan branch is in town at 1/70 Hanrapetutyan Ave, not on the highway frontage).
    - **Dairy:** Marianna, Ashtarak Kat (Ashtarak Milk LLC), Bonilat, Yeremyan Products, Aparan (tan) and others.
    - **Water:** Bjni, Jermuk, Noy, Byuregh, Aparan.

    The weak point is economics, not availability. Bought-in local pastries carry a food cost of about **37–56%** of the menu price at defensible menu prices. In-house wraps come in at about **29–33%** (24–28% with a purchasing discount) (ESTIMATE, §3.11). *Fact-check correction: was 45–67% and 29–39%. §3.11 compared a VAT-inclusive purchase cost with an ex-VAT menu price, overstating every food-cost % by ≈1.2×. On a consistent basis (cost ÷ VAT-inclusive menu price under the catering turnover tax C4 recommends for year 1, or ex-VAT ÷ ex-VAT under VAT) the levels fall; the ranking is unchanged.*
11. **Recommendation, as an assumption to be tested.** Use a "coffee + Armenian hand-held" menu of 10–14 food SKUs:
    - **Core items:**
      - Fresh-filled ponchik.
      - Mini Gavar-style gata.
      - Folded lahmajo.
      - Zhingyalov hats.
      - Cheese puff pastry (penovani-style).
      - **In-house breakfast lavash wraps:** egg, cheese and herbs, with a basturma option.
      - Croissant sandwiches.
    - **Price points:** 400–1,600 AMD per item; coffee + pastry combos at 1,900–2,600 AMD.
    - **Drinks to stress:** sweet iced lattes, batch lemonades with local flavours (sea buckthorn, tarragon, apricot), bottled tan and herbal teas. Add a "jezve-to-go" Armenian coffee as a local signature.
    - **Test only:** bagels, cold-brew branding and an energy "Rebel" line, as limited trials.

---

## 2. Key data table

| # | Metric | Value | Period | Status | Source |
|---|---|---|---|---|---|
| 1 | Share of energy from bread & flour products (adults) | 53% | 24HR survey, publ. May 2026 (data year not stated) | VERIFIED | Pipoyan et al. 2026 [35] |
| 2 | Adults eating bread/flour products on recall day | 88% (1,230/1,400, table); ≈96% (text) | as above | VERIFIED (internal inconsistency noted) | [35] |
| 3 | Adults eating biscuits/cakes/pastries/waffles on recall day | 40% | as above | VERIFIED | [35] |
| 4 | Mean energy intake, adults | 1,738 kcal/day (women 1,608, men 1,892) | as above | VERIFIED | [35] |
| 5 | Adults eating fish on recall day | 2% | as above | VERIFIED | [35] |
| 6 | Adults eating eggs (scrambled / boiled) on recall day | 17% / 10% | as above | VERIFIED / ESTIMATE (238 and 142 of 1,400) | [35] |
| 7 | Most-consumed fast foods in Yerevan (mean g/day) | Pastry 76.1; fried chicken 53.1; hot dog/burger 50.0; shawarma 49.3; pancake/doughnut 41.4; chips 36.2; pie 35.0; pizza 33.9; khachapuri 32.2; fries 27.9; popcorn 14.7 | FFQ autumn 2019, n = 423, ages 18–65 | VERIFIED | Pipoyan et al. 2022 [34] |
| 8 | Mean fast-food frequency, Yerevan adults | ≈1×/week (0.38–1.93) | 2019 | VERIFIED | [34] |
| 9 | Food away from home, share of consumption | 2.8% national; 3.5% urban (1,709 / 2,293 AMD/person/month). *Fact-check note: survey floor; A1's turnover-based figure is ≈8,444 AMD/resident/month (≈5×)* | ILCS 2024 | VERIFIED (via A1) | A1 [44] |
| 10 | Households: money enough only for food, or not even for food | 38% (12% + 26%) | CB 2024 (Jul–Oct 2024) | VERIFIED | CRRC [29] |
| 11 | Households owning a car | 46% (ILCS 2024: 41.2%) | CB 2024 | VERIFIED | CRRC [30]; A1 [44] |
| 12 | Fast "always/often" when religion requires (denomination members) | 4% (never: 83%) | CB 2024 | VERIFIED | CRRC [32] |
| 13 | Ponchik (filled donut), Grand Candy | 130–150 AMD (78–86 g); mini 80 AMD | Oct 2026 | VERIFIED | Grand Candy e-shop [15] |
| 14 | Donut at international chains | KFC 650 AMD; Cofix 880 AMD (Glovo) | Oct 2026 | REPORTED | Glovo [6][8] |
| 15 | Lahmajo | 480 (Karas) / 750 (Lebanese Kunji) / 900–1,000 (SAS Food Court) / 2,200 (Jazzve) AMD | Oct 2026 | REPORTED | Glovo [5][10][2][9] |
| 16 | Shawarma (chicken/pork, standard) | 1,150–1,350 AMD; L/XL 1,650–2,050; double 2,200–2,350 | Oct 2026 | REPORTED | Glovo [2][3] |
| 17 | Gata | Grand Candy round 175 g 300 AMD; SAS Sweet mini 350; Gavar gata 600 g 1,840 AMD | Oct 2026 | VERIFIED | [15][16] |
| 18 | Zhingyalov hats | 400 AMD (90 g, SAS); 1,200 AMD with cheese (SAS Food Court) | Oct 2026 | VERIFIED / REPORTED | [17][2] |
| 19 | Croissant (retail bakery) | 520–1,290 AMD (SAS Sweet); Coffeeshop Company 990 | Oct 2026 | VERIFIED | [16]; A2 [45] |
| 20 | Ready sandwich (supermarket) | 1,090–1,350 AMD (9 SKUs) | Oct 2026 | VERIFIED | SAS [17] |
| 21 | Hot dog | 300–1,400 AMD | Oct 2026 | REPORTED / VERIFIED | [2][4][12][16] |
| 22 | Tan (ayran-type yogurt drink) | Retail 210–580 AMD (20 SKUs); fast food 470–550 per 0.5 L | Oct 2026 | VERIFIED / REPORTED | SAS [20]; Glovo [3][5][2] |
| 23 | Fresh juice 0.5 L / lemonade / smoothie | 1,000–1,700 / 1,100–1,800 / 1,100 AMD | Oct 2026 | REPORTED | Glovo [2][7] |
| 24 | Energy drinks, retail | Burn 250 ml 510; Red Bull 250 ml 670; Monster 500 ml 990; Max Power 280 AMD. ≈75–85 energy-drink SKUs within a 151–153 SKU cocktails/energy/low-alcohol category. *Fact-check: Max Power 280 not re-seen on 10 Oct 2026; other prices re-confirmed* | Oct 2026 | VERIFIED (Max Power price unconfirmed) | SAS [22] |
| 25 | Ready-to-drink iced coffee SKUs at SAS | 65 (28 Armenian-origin); Starbucks RTD 1,250 AMD/220 ml | Oct 2026 | VERIFIED | SAS [23] |
| 26 | Plant-milk SKUs at SAS / barista-grade | 24 / 5; Alpro Barista Oat 1,410 AMD/L | Oct 2026 | VERIFIED | SAS [19] |
| 27 | Whole milk retail (Marianna 3.2%) | 610 AMD / 950 ml (≈642 AMD/L); Numbeo avg 592/L | Oct 2026 | VERIFIED / REPORTED | SAS [18]; Numbeo [28] |
| 28 | Mineral water | Jermuk 0.5 L 210 AMD (food court); Bjni 0.5 L 220–250 retail | Oct 2026 | REPORTED / VERIFIED | [2][21] |
| 29 | Grand Candy store network | 19 stores (Yerevan street addresses), incl. Ponchikanoc donut café, Mashtots 54 | Oct 2026 | VERIFIED | [15] |
| 30 | Max Oil network / Max Cafe on M4 | 50+ stations; Max Cafe at Yerevan–Sevan hwy km 12.2 (coffee, hot dogs, fast food) | Oct 2026 | VERIFIED | Max Oil [27]; B2 [47] |
| 31 | Roadside seafood stalls on M4 | 10 OSM shop=seafood points at km ≈68–74 (past Sevan town) | OSM 2026-10-10 | REPORTED | B2 [47] |
| 32 | Sevan trout (ishkhan) commercial fishing | Stopped by 1976 Council of Ministers resolution; IUCN 3.1 "extinct" (2019) per Wikipedia | 1976 / 2019 | REPORTED | Wikipedia [40] |
| 33 | Oat-milk extra cost per 150 ml drink | ≈115 AMD | Oct 2026 prices | ESTIMATE | (1,410 − 642) × 0.15 |
| 34 | Numbeo "combo meal at McDonald's or equivalent" | 3,825 AMD (2,895–4,990) | upd. 3 Oct 2026 | REPORTED | Numbeo [28] |

---

## 3. Detailed findings & analysis

### 3.1 Diet structure, breakfast and on-the-go habits

**What Armenians actually eat (individual-level evidence).** Pipoyan et al. (Frontiers in Nutrition, May 2026) report the first nationally representative individual 24-hour recall: n = 1,400 adults aged 18–80, covering 164 foods and dishes, including food eaten outside the home [35]. The paper does not state the fieldwork year.

| Food group | Consumers on recall day (table count / 1,400) | Text figure | Mean intake among consumers |
|---|---|---|---|
| Bread & flour products | 1,230 (88%) | "≈96%" | 300 g; first-grade wheat bread 175 g vs lavash 70 g (bread eaters outnumber lavash eaters 2.5:1) |
| Biscuits, cakes, pastries, waffles, cookies | — | 40% | — |
| Sugar, honey, confectionery | 865 (62%) | "73%" | 150 g; ice cream eaten by 20% |
| Milk & milk products | 836 (60%) | "70%" | 165 g; cheese ≈ half of all adults; matsun 17%; sour cream 8%; tan "a small number" |
| Meat & meat products | 704 (50%) | "55%" | 166 g; chicken 18%, sausages 14%, beef 13% |
| Fruits / vegetables | 609 (44%) / 705 (50%) | 47% / 55% | — |
| Juices | 404 (29%) | — | — |
| Scrambled eggs / boiled eggs | 238 (17%) / 142 (10%) | 18% / 11% | Popular: with tomato, sausage, cheese, green beans, greens |
| Fish | 28 (2%) | 2% | "Not typical… consumed only during certain occasions" |

Status: VERIFIED [35]. The table counts are slightly below the text percentages, probably because outliers were removed. We report both.

Energy: bread and flour supply 53% of energy, meat 13%, sugar and confectionery 8%, dairy 7%. The household-survey paper finds the same pattern: more than 50% of energy, protein and carbohydrate comes from cereals and bakery products. Over 2008–19 consumption of sweet bakery items fell substantially, and total energy intake fell from 2,051 to 1,790 kcal (VERIFIED [36]).

**Breakfast.** We found **no Armenian survey that measures the share of people who eat breakfast out of home or on the go**.
- **Qualitative evidence:**
  - Stepanyan et al. 2022 conclude that "irregular meal intake and omission of breakfast" are "widespread dietary practices". This is an author statement, not a measured rate (VERIFIED [36]).
  - A 2024 qualitative study in 21 schools (Yerevan, Shirak, Lori, Tavush; 94 participants) found that breakfast skipping, time constraints, financial barriers and taste preferences drive unhealthy eating among schoolchildren. Its recommendations include "highlighting the significance of breakfast" (VERIFIED abstract [37]).
- **Implication (ASSUMPTION).** Breakfast is a home meal built on bread, cheese, eggs and coffee, and it is often skipped. That cuts two ways for a commuter drive-thru:
  - **For:** a large unmet need among commuters.
  - **Against:** no established habit of buying breakfast. Ramp-up will be slow and needs price points close to home cost.

**On-the-go formats that already exist.** The market's grab-and-go formats are bakery counters (karkandak, gata, ponchik), shawarma and lahmajo shops, supermarket food courts (SAS Food Court lists about 300 items on Glovo [2]) and fuel-station cafés (Max Cafe [27]). We found no evidence of a breakfast-sandwich category:
- On Glovo Yerevan, the "Breakfast" filter returns **one** store (Jazzve) out of 33 food stores, and the "Bakery" filter returns six (REPORTED [33][1]).
- Jazzve's breakfast plates cost 1,900–4,800 AMD and are sit-down dishes [9].

Delivery-aggregator coverage is partial: menu.am has moved to Yandex Eats, which we could not access. Even so, this suggests breakfast-to-go is an under-supplied category (ASSUMPTION).

### 3.2 Eating-out frequency, fast-food attitudes and affordability

| Indicator | Value | Status / source |
|---|---|---|
| Fast-food frequency, Yerevan adults 18–65 (FFQ autumn 2019, n = 423) | Mean ≈ once per week (0.38–1.93/week). "All participants consumed at least one type of fast food." 7% consumed all 11 types regularly | VERIFIED [34] |
| Sample bias | 90% higher education; 66% refused the income question; 56% men; mean age 31.9 | VERIFIED [34]. Frequency is probably **overstated** for the general population (ASSUMPTION) |
| Comparators cited by authors | King County, US: 2.07/week; Iran: 1.67/week | VERIFIED [34] |
| Food away from home (ILCS 2024) | 2.8% of consumption nationally, 3.5% urban | VERIFIED via A1 [44] |
| Household economic situation (CB 2024) | Not enough for food 12%; food only 26%; food + clothes 42%; some durables 12%; anything 7% | VERIFIED [29] |
| Lacked money for food at least monthly in past 12 months (CB 2024) | 14% (daily 2%, weekly 4%, monthly 8%); never 68% | VERIFIED [31] |
| Household car ownership | 46% (CB 2024) vs 41.2% (ILCS 2024) | VERIFIED [30]; A1 [44] |

**Attitudes.**
- **Authors' stance.** The Yerevan fast-food paper frames fast food as a "major driver" of non-communicable diseases and says "the number of fast-food restaurants and selling points increased in the country" [34]. The 2026 diet paper calls for national dietary guidelines and nutrition education [35]. The public-health community is therefore critical of fast food, but we found no national regulation targeting fast-food outlets.
- **Trans-fat regulation.** Trans fats are regulated only in fats and oils, under EAEU TR CU 024/2011 (limit 2% of fat since Jan 2018); prepared foods are not covered [34].
- **What we found no data on.** No Armenian survey measures attitudes to "American" fast food, brand preferences or willingness to pay. None of MPG/Gallup International, Breavis or Ipsos published accessible studies (gap, §5).

**Affordability anchor.** A2 calculates that a 1,950 AMD cappuccino costs about 1.1 hours of average gross pay (314,196 AMD per month in Aug 2026 ÷ 173.3 h ≈ 1,813 AMD per hour). On the same basis (ESTIMATE):
- a 2,000 AMD drink + pastry combo costs about **1.1 hours** (2,000 ÷ 1,813);
- Numbeo's 3,825 AMD fast-food combo costs about **2.1 hours** (3,825 ÷ 1,813) [28].

These use **gross** wages. Take-home pay is about 25% lower after 20% income tax and 5% pension contribution, so the real burden is about a third higher (e.g., the combo ≈1.5 h and the Numbeo combo ≈2.8 h of net pay; ESTIMATE). *Fact-check correction: the hours basis was given as 177 h / 1,775 AMD/h and attributed to A2; A2 actually uses 173.3 h / 1,813 AMD/h. The Numbeo combo moves from 2.2 h to 2.1 h; conclusions unchanged.*

### 3.3 Grab-and-go foods: what is sold and at what price (Oct 2026)

| Item | Typical price range (AMD) | Observed examples (store, source, status) | Notes for drive-thru |
|---|---|---|---|
| **Ponchik (filled fried donut)** | 80–280 local; 650–880 at international chains | Grand Candy: vanilla 78 g 130, chocolate/caramel 78 g 150, fruit 86 g 150, round mini 32 g 80 ("Donut shop only" = Ponchikanoc, Mashtots 54) (VERIFIED [15]). SAS Food Court: chocolate 280, vanilla 230, pishki 100–200 (REPORTED [2]). KFC donut 650 [6]; Cofix donut 880, banana-Nutella 1,100 [8]; Yum-Yum packaged 710–850 (SAS [16]) | Hand-held and sweet; same-day shelf life. The low local price anchor is the key constraint. *Mayak not verified* |
| **Gata** | 250–430 per small piece; 990–1,840 per large loaf | Grand Candy round 175 g 300; traditional 1,770/kg; rural 1,650/kg (VERIFIED [15]). SAS Sweet curd mini gata 350, round 300 g 1,030, Gavar gata 600 g 1,840; Zeytun round 175 g 430; Nor-Nar Gavar gata with khoriz 350 g 920; Levrim matsun gata 500 g 990 (VERIFIED [16]). SAS Food Court layered gata 300 [2]; Art Lunch gata 100 g 250, gata with dates & walnut 650 [12] | Shelf life of days. Strong regional identity: **Gavar is the Sevan-basin town** and Tsovinar (south Sevan) has a triangular variant [42]. Ideal coffee pairing |
| **Karkandak / piroshki (savoury pies)** | 100–690 | SAS Food Court: cabbage 100, potato 150–280, cheese 200–270, meat 370–690, cheburek 870 [2]. Karas: potato or chicken 420 [5]. Art Lunch 280–650 [12]. SAS Product baked pies 210–450; Tnakan tiropita/kreatopita/spanakopita 570 [16] | Cheapest savoury hand-held. Many suppliers |
| **Khachapuri / cheese pastries ("penovani")** | Imeruli piece 400–600; Adjarian 750–1,800; Megruli whole 2,700–3,000 | Tashir: Imeretian 600, Adjarian 1,500–1,800 (REPORTED [4]). Karas: cheese 480, beef 530, BBQ 840, Adjarian 1,580 [5]. SAS Food Court: Imeruli piece 400, Megruli piece 450, layered cheese pie 270, shoti puri with cheese 350 [2]. SAS khachapuri gouda 520 [16]. Jazzve Adjarian 1,600 [9] | "Penovani" as a name was not found. The layered cheese pie is the nearest. Adjarian (open boat with egg) is **not** car-friendly |
| **Lahmajo** | 480–1,000 (café 2,200) | Karas 480, with cheese 690 [5]; Lebanese Kunji 750–900 [10]; SAS Food Court 900–1,000 [2]; Jazzve 2,200 [9] | Folded or rolled with greens, it is hand-held. Reheat 60–90 s (ASSUMPTION). Grease risk in a car |
| **Zhingyalov hats** | 400–1,200 | SAS "bread with jengyal" 90 g 400 (VERIFIED [17]); SAS Food Court with cheese 1,200 [2] | Vegetarian herb flatbread from Artsakh/Syunik, cooked about 10 min on a saj [43]. Differentiator vs Coffee House and fuel stations |
| **Lavash wraps (brdutch)** | 790–1,560 | Jazzve lavash rolls with cheese 1,500 [9]; Art Lunch "Mexican" wrap 790, Caesar roll 1,560 [12]; Tashir wraps 1,800 [4]; lavash 50 g ≈60 AMD retail [12] | Best canvas for an **Armenian breakfast wrap** (egg, cheese, herbs, basturma) |
| **Shawarma** | 1,150–2,350 | Tumanyan Shaurma: chicken M 1,300, pork M 1,400, XL 1,950–2,050, double 2,200–2,350, "with bread" 1,200–1,300 [3]. SAS Food Court 1,150–1,350, gyros 1,300–1,400 [2]. Glovo lists 12 shawarma outlets [14] | Very popular (49 g/day [34]) but needs a rotisserie and 2–4 min assembly. Saturated market; poor fit |
| **Hot dog** | 300–1,400 | Art Lunch 300 [12]; SAS Food Court 350 to 1,400 (Austrian sausage) [2]; SAS bakery hot dog 380 [16]; Tashir 500 / BBQ 1,000 [4] | Fuel-station staple (Max Cafe [27]). Low differentiation |
| **Sandwiches** | 750–1,700 mass; 2,400–4,400 café | SAS Product ciabatta/croissant sandwiches 1,090–1,350 (VERIFIED [17]); SAS Food Court 750–1,700 [2]; Art Lunch ciabatta 1,560 [12]; Tashir club 2,000 [4]; Jazzve club/Dijon 2,900–3,100 [9]; Coffeeshop Co sourdough 2,400–4,400 (A2 [45]) | A big gap between mass and café prices is where a drive-thru can position (1,300–1,800) |
| **Croissants** | 520–1,290 | SAS Sweet classic 750, cheese 710, Nutella 1,290; Grand Candy toffee croissant 700 (VERIFIED [15][16]); Coffeeshop Co 990 (A2) | Commodity. Margin depends on bake-off |
| **Bagels** | ≈160 (bread bagel) | "Sas Bakery" bagel 90 g 160 (VERIFIED [16]). Green Bean café is known for bagels (A2; not price-checked) | **No mass bagel culture found** |
| **Cinnamon rolls / buns** | 200–560 | SAS Sweet buns 200–420 [16]; Art Lunch cinnamon roll 180 g 560 [12] | Familiar "bulki" format |
| **Burgers (for reference)** | 950–3,950 | KFC 950–2,250, combos 2,800–3,200 [6]; Mic Mac 1,950–3,950, combos 3,500–4,800 [11] | Not core to a coffee drive-thru |

**Price-ladder synthesis (ESTIMATE from the table above):**
- Local sweet hand-held: 80–650.
- Local savoury hand-held: 100–1,200.
- Meat hand-held (shawarma/hot dog): 300–2,350.
- Ready sandwich: 1,090–1,800 (mass) and 2,400–4,400 (café).

**Recommended drive-thru food price band: 400–1,600 AMD.** Above about 1,800 AMD the product competes with full meals: Numbeo puts an inexpensive meal at 4,000 AMD and a fast-food combo at 3,825 AMD [28] (ASSUMPTION).

### 3.4 Beverages

| Beverage | Price evidence (AMD, Oct 2026) | Status / source | Relevance |
|---|---|---|---|
| **Armenian coffee (soorj/jezve)** | The dominant home and office format. About 89% of green imports come from robusta origins (A2). Cofix sells instant "coffee mix" at 550 (Glovo) | VERIFIED via A2 [45]; REPORTED [8] | We found no to-go jezve price benchmark at chains. A local signature item; needs a fast brewing method (ASSUMPTION) |
| **Espresso drinks, hot and iced** | Coffee House americano 800, cappuccino/latte 1,000, iced latte 1,000; Cofix iced latte 1,320 (Glovo); premium chains up to 1,950 | A2 [45]; [7][8] | Covered by A2. A2 recommends an affordable-premium iced latte at 1,600–1,800 |
| **Sweet flavoured drinks** (Kinder, Nutella, Oreo, frappé) | Coffee House frappé/shakes 1,400; Cofix Kinder/Nutella hot 770, iced 1,100, milkshakes 1,650 | REPORTED [7][8] | Strong youth signal: both chains run large sweet ranges |
| **Tea** | Coffee House black/green/herbal 550; citrus tea and "winter punch" 850; iced tea 600–950; matcha 1,000–1,300 (matcha latte 1,000, matcha raf 1,100, cream-cheese matcha latte / sky matcha 1,300). *Fact-check correction: was 1,000–1,100* | REPORTED [7] | Herbal (thyme/mint) is low-cost and on-trend |
| **Tan (salted yogurt drink)** | Retail 210–580 (Aparan 0.5 L 330; carbonated tan 290; Marianna 300 g 230); fast food 0.5 L 470–550; Tashir small 230 g 300 | VERIFIED [20]; REPORTED [3][4][5] | Zero prep. Pairs with savoury pastry. Low margin per unit (§3.11) |
| **Fresh juices** | 0.5 L: orange 1,200; banana mixes 1,000–1,700; Tashir fresh juices 1,200 | REPORTED [2][4] | Slow and labour-heavy. Fruit waste |
| **Lemonades** | SAS Food Court 1,100–1,800; Coffee House mojito 1,100, sea-buckthorn (chichkhan) 1,300 | REPORTED [2][7] | Batchable, high margin, summer peak |
| **Smoothies / protein shakes** | Coffee House smoothies 1,100, detox green 1,400, protein shakes 1,600 | REPORTED [7] | Health trend proxy |
| **Mineral and spring water** | Jermuk 0.5 L 210 (food court); Bjni 0.5 L 220–250, 1.5 L 360; Bonaqua 0.5 L 170; Noy 0.5 L 180–220; Evian 0.5 L 590 | REPORTED [2]; VERIFIED [21] | Traffic item for road trips |
| **Soft drinks** | Coca-Cola 0.5 L retail 420; fast food 500–550 | VERIFIED [24]; REPORTED [3][6] | Commodity |
| **Energy drinks** | Burn 250 ml 510; Red Bull 250 ml 670, 355 ml 920; Monster 500 ml 990; Adrenaline 449 ml 590; Lit 450 ml 680; Jaguar 450 ml 770; Max Power 250 ml 280; Boom 450 ml 340. KFC sells Burn 250 ml at 800 | VERIFIED [22] (Max Power 280 not re-seen at fact-check); REPORTED [6] | A cheap category of ≈75–85 SKUs, which anchors "Rebel" pricing. *Fact-check correction: the 151–153 SKU SAS category also includes alcoholic cocktails and low-alcohol RTDs* |
| **Ready-to-drink iced coffee** | 65 SKUs (28 Armenian-origin): Grand Candy "Tonus" 200 ml 150; Duet 190–210; Kaffa 250 ml 630; Starbucks RTD 220 ml 1,250, Black 270 ml 1,670; no cold-brew labels on page 1 | VERIFIED [23] | Iced coffee is mainstream at retail. The Starbucks brand is already on shelves |
| **Hot chocolate / cocoa** | Grand Candy cocoa 167 ml 140; Coffee House 600; Cofix 1,100 (Glovo) | VERIFIED [15]; REPORTED [7][8] | Winter and children |

**Iced coffee adoption among young people.** We found no survey. The indirect evidence points the same way:
- the two largest to-go chains keep full iced menus (Coffee House 4 iced teas plus iced coffee and shakes; Cofix 12 iced coffee SKUs) [7][8];
- 65 ready-to-drink iced coffee SKUs are listed in one supermarket chain [23];
- A2 characterises Coffee House as youth-oriented.

On this basis iced and sweet coffee is mainstream among young urban consumers (REPORTED/ASSUMPTION). How it is split by age is a gap.

### 3.5 Health and trend signals

| Signal | Evidence | Status |
|---|---|---|
| Plant milks | 24 SKUs at SAS. 5 barista-grade (Alpro Barista Oat 1,410/L; OraSi Barista hazelnut, almond, coconut, soy-banana 1,840–2,090/L). Valsoia 1,930/L; local Nushanush almond 1,440/L; Landessa oat-vegan RTD coffee 750 | VERIFIED [19][23] |
| Lactose-free milk | Parmalat 1,470–1,590/L; Lactel 1,440–1,490/L | VERIFIED [18] |
| Protein products | Coffee House protein shakes 1,600 (3 SKUs); Cofix protein ball 660; "1Attimo" protein croissant 50 g 1,650 | REPORTED [7][8]; VERIFIED [16] |
| Matcha | Coffee House 1,000–1,300; Cofix 1,100–1,320 (Glovo). *Fact-check correction: Coffee House was 1,000–1,100* | REPORTED [7][8] |
| Sugar-free soft and energy drinks | Coca-Cola Zero, Monster Zero/Ultra, Lit Original Zero on shelf | VERIFIED [22][24] |
| Public-health stance | Researchers stress low dietary diversity and push nutrition education and trans-fat monitoring | VERIFIED [34][35][36] |
| Counter-signal | Confectionery is eaten by 62–73% of adults on the recall day. Sweet bakery is a daily habit, so "healthy" will likely remain an add-on segment, not the core (ASSUMPTION) | VERIFIED [35] |

**Cost of an oat-milk option (ESTIMATE).**

| Component | Calculation | Result |
|---|---|---|
| Oat milk, 150 ml | 0.150 L × 1,410 AMD/L | 211.5 AMD |
| Whole milk, 150 ml | 0.150 L × 642 AMD/L | 96.3 AMD |
| **Extra cost per drink** | 211.5 − 96.3 | **≈115 AMD** |

Retail prices are used; HoReCa prices would be lower. A **200–300 AMD surcharge** is defensible.

### 3.6 Seasonal items and the Sevan roadside

| Item / season | Evidence | Status | Drive-thru fit |
|---|---|---|---|
| **Roadside fish and crayfish stalls** | 10 OSM shop=seafood POIs at M4 official km ≈68.1–74.1, both sides, past Sevan town towards Dilijan (e.g., "Seyrani mot", "GagArt") | REPORTED, OSM via B2 [47] | **No.** A separate, fresh-fish trade with odour, prep time and possible fishing-season and legality issues. Prices not obtained (gap) |
| **Ishkhan (Sevan trout)** | A 1976 Council of Ministers resolution stopped commercial fishing. Wikipedia's species page shows IUCN 3.1 "extinct" (2019 assessment), while the Lake Sevan page says "endangered". Hatcheries propagate related forms | REPORTED [40][41] (conflict noted) | **No.** Use "ishkhan" in branding at your peril. SAS sells farmed rainbow trout at 3,050 AMD/kg [25] |
| **Lake Sevan share of catch** | "Some 90% of the fish and 80% of the crayfish catch of Armenia" (undated) | REPORTED [41] | Context only |
| **Sevan beach tourism** | About 100,000 public-beach visitors (summer 2011); about 200,000 holidaymakers and 11 public beaches (2014). Old figures, low reliability | REPORTED [41] | Summer demand on the Sevan-bound carriageway (B1: July–Aug at 1.3–1.6 × AADT for Sevan segments, ASSUMPTION) |
| **Gata of the Sevan basin** | Gavar gata is a recognised style (SAS Gavar gata 600 g 1,840; Nor-Nar Gavar gata 350 g 920, "Gavar mijink" 480 g 1,760). Tsovinar (south Sevan) has a triangular gata without khoriz | VERIFIED [16]; REPORTED [42] | **Yes.** A "Sevan/Gavar gata" signature item that is long-life, hand-held and local |
| **Gata sellers at highway villages, corn, fruit and dried-fruit stands** | We obtained **no source** on M4 stands or prices. The best-known gata roadside trade is at Garni/Geghard (not the M4) [42] | Gap | Fieldwork (§5) |
| **Dried fruit** | Aflatoxin B1 and total aflatoxins in dried fruit from Yerevan **open (street) markets exceeded EU maximum limits**. Armenia has no national limit | VERIFIED abstract, Foods 2026 [39] | Use only certified suppliers. Avoid "roadside" sourcing |
| **Lent (Great Lent, ~7 weeks before Easter)** | 4% always/often fast; 9% at least sometimes; 83% never (CB 2024, denomination members) | VERIFIED [32] | A small niche. Zhingyalov hats work as a year-round vegetarian item |
| **New Year (31 Dec – 6 Jan)** | Gata is eaten at Candlemas (14 Feb) and other festivities [42]. We have no quantified seasonal sales data | REPORTED | Gift boxes of gata and ponchik (ASSUMPTION) |
| **Summer vs winter menu** | Coffee House already rotates a "winter punch" 850 and citrus tea 850 [7]. Summer brings iced and lemonade demand | REPORTED | Rotate 3–4 seasonal SKUs |

### 3.7 Supplier landscape

| Category | Brand / supplier | What we verified | Status / source |
|---|---|---|---|
| Bakery, pastry, confectionery | **Grand Candy** | 19 own stores, many with cafés, at Yerevan street addresses, including the Ponchikanoc donut café at Mashtots 54. 17 catalogue categories summing to 470 entries (ice cream 62, cakes & pastries 43, bakery 21, donuts & cocoa 6). Ponchik 130–150, gata 300 (175 g), croissant 700, RTD "Tonus" coffee 150. B2B/HoReCa supply not stated on site | VERIFIED [15][23] |
| Bakery (retailer private label) | **SAS Sweet / SAS Product / Sas Bakery** | 52 bakery SKUs: 15 croissants, 12 gata, 10 buns + 1 bagel, 10 pies, 2 khachapuri, 2 donuts. 9 ready sandwiches | VERIFIED [16][17] |
| Gata specialists | **Nor-Nar** (Gavar gata, gata with dates, gata roll); **Zeytun / Zeytun Sweet** (round gata, korzhik, croissants); **Levrim** (matsun gata) | Products and prices on the SAS shelf | VERIFIED [16] |
| Ready pies | **Tnakan** (tiropita, kreatopita, spanakopita 570; also "TNAKAN" ready dishes) | On SAS shelf | VERIFIED [16] |
| Lahmajo, khachapuri, pies | **Karas** (10 branches incl. Abovyan); **Tashir Pizza** | Karas branches VERIFIED [26]; menus REPORTED [4][5]; Tashir website blocked (403) | VERIFIED / REPORTED |
| Bakery brands named in the brief | **Kaghtsr, Yasaman, Mayak** | **Not verified**: kaghtsr.am DNS failure, yasaman.am empty page, Mayak no source | Gap |
| Dairy (milk) | **Marianna** (950 ml 3.2% 610; UHT 1 L 790; 500 ml 540; 200 ml 250; tan 300 g 230) | On SAS shelf; marianna.am unavailable (503) | VERIFIED [18][20] |
| Dairy | **Ashtarak Kat** (Ashtarak Milk LLC): milk 3.2% and 1.5% 1 L, matsun, kefir, sour cream, cottage cheese, drinkable yogurt; stocked at SAS, Nor Zovq, Parma, Yerevan City, Carrefour | Company site; no HoReCa/barista offer stated | VERIFIED [26a] |
| Dairy (others on shelf) | Bonilat, Yeremyan Products, Dili, Chanakh, Marila, Panatsea; imported Parmalat, Lactel, Prostokvashino | SAS milk category (24 of 49 SKUs visible) | VERIFIED [18] |
| Dairy (named in brief) | **Dustr Margo**, Tamara, Igit | Not found on SAS milk page; dustrmargo.am DNS failure | Gap |
| Tan | Aparan (6 SKUs), Bonilat (4), Champion, Ayg, Yeremyan, Sisian Kat, Marianna, Merci Milk, SAS | 20 SKUs | VERIFIED [20] |
| Plant milk | Alpro (incl. Barista Oat), Valsoia, OraSi Barista, Nushanush (local almond) | 24 SKUs | VERIFIED [19] |
| Water | Bjni, Jermuk (brand filter only), Arzni (filter only), Bonaqua, Aparan, Byuregh, Noy | 167 water SKUs in category | VERIFIED [21] |
| Energy drinks | Burn, Red Bull, Monster, Adrenaline Rush, Jaguar, Lit, Max Power, Boom, Revo, Gorilla (4), Flash Up (7) | ≈75–85 energy-drink SKUs within a 151–153 SKU "cocktails, energy drinks, low-alcohol beverages" category. *Fact-check correction: was "151 SKUs in cocktail/energy category"* | VERIFIED [22] (energy-SKU count is an ESTIMATE from brand-filter counts) |

**Supply implication (ASSUMPTION).** A pastry programme could be bought in daily from 2–3 suppliers: Grand Candy for ponchik and gata, Nor-Nar or Zeytun for Gavar gata, and Tnakan or an SAS-type bakery for pies. That lets the operator open without a bakery. However, contract terms, minimum order quantities, delivery to an M4 site, and whether frozen bake-off formats exist are all **unverified** (gap).

### 3.8 Competitive menu benchmarks relevant to food

| Competitor | Food offer | Price signals (AMD) | Source |
|---|---|---|---|
| Coffee House (incl. M4 drive-thru) | Sweets only on Glovo: cookie 600, muffin 750, tarts 850–1,050, brownie 1,050, tiramisu 1,300, cheesecake 1,700, macarons 750–850. No sandwiches on Glovo; FEIN sub-brand sandwiches 2,600–3,400 (A2) | Drinks 550–1,600 | REPORTED [7]; A2 [45] |
| Cofix | Donut 880, banana-Nutella donut 1,100, muffins 880, protein ball 660 (Glovo) | Coffee 550–1,760 | REPORTED [8] |
| KFC Armenia | Burgers 950–2,250, twisters 800–1,900, donuts 650 | Combos 2,800–3,200 | REPORTED [6] |
| Max Cafe (Max Oil) | "Max Coffee", hot dogs, fast food, cold drinks; on the Yerevan–Sevan highway at km 12.2 | No prices published | VERIFIED [27] |
| SAS Food Court | About 300 items: pastries 100–870, khachapuri 400–2,700, sandwiches 750–1,700, shawarma 1,150–2,150, lahmajo 900–1,000, omelettes 550–1,450, juices 1,000–1,700, lemonades 1,100–1,800, crepes 500–1,600 | Glovo: 98% rating, 1k+ ratings | REPORTED [2] |
| Jazzve | Breakfasts 1,900–4,800, Armenian breakfast 2,800, lahmajo 2,200, lavash cheese rolls 1,500 | Sit-down | REPORTED [9] |

**Gap in the market (ASSUMPTION).**
- **What is missing:** no operator combines (a) quality to-go coffee with (b) hot, freshly assembled Armenian hand-helds at mass-premium prices (1,000–1,600) on a car-first format.
- **What exists:** Coffee House sells sweets, not savoury food. Fuel stations sell hot dogs. Bakeries do not serve cars.
- **This is the most defensible food differentiation we found.** It is also easy to copy: Coffee House or Max Oil could add a pie warmer.

### 3.9 Drive-thru suitability matrix (scored 1–5; 5 = best)

The criteria follow common QSR design logic; every score is an **ASSUMPTION**:
- **Speed:** prep or reheat at or under 90 s scores 5.
- **Hand-held / car:** one hand, low drip and low crumbs scores 5.
- **Shelf life:** long life, low waste scores 5.
- **Margin:** the realistic gross margin at a defensible price (§3.11).
- **Local demand evidence:** taken from §3.1–3.3.
- **Differentiation:** distance from what Coffee House and fuel-station cafés already offer.

| Item | Speed | Hand-held / car | Shelf life | Margin | Local demand evidence | Differentiation | Total /30 | Verdict |
|---|---|---|---|---|---|---|---|---|
| Mini Gavar/Sevan gata (bought-in) | 5 | 4 | 5 | 3 | 5 | 4 | **26** | Core |
| Breakfast lavash wrap (egg, cheese, herbs; in-house) | 3 | 5 | 3 | 4 | 4 | 5 | **24** | Core (hero) |
| Fresh-filled ponchik | 5 | 3 (powder, filling) | 2 | 4 | 5 | 4 | **23** | Core (glaze, no powder) |
| Cheese puff pastry / khachapuri piece | 4 | 4 | 3 | 2 | 5 | 3 | **21** | Core |
| Zhingyalov hats (warm) | 4 | 4 | 2 | 3 | 3 | 5 | **21** | Core (signature) |
| Croissant sandwich (ham, cheese or chicken) | 4 | 4 | 3 | 3 | 4 | 3 | **21** | Core |
| Folded lahmajo | 4 | 3 | 3 | 2 | 5 | 3 | **20** | Test |
| Savoury karkandak (potato, cheese, meat) | 5 | 4 | 3 | 2 | 5 | 1 | **20** | Optional (cheap anchor) |
| Cookies / muffins | 5 | 5 | 4 | 4 | 3 | 1 | **22** | Add-on |
| US-style glazed / iced donut | 5 | 4 | 2 | 4 | 2 | 4 | **21** | Test, limited |
| Hot dog | 4 | 4 | 4 | 3 | 4 | 1 | **20** | No (fuel-station commodity) |
| Bagel sandwich | 3 | 4 | 3 | 3 | 1 | 3 | **17** | No (niche) |
| Shawarma | 2 | 3 | 3 | 3 | 5 | 1 | **17** | No |
| US breakfast sandwich (English muffin, egg, cheese, bacon) | 3 | 4 | 3 | 3 | 2 | 4 | **19** | Reformulate as lavash or matnakash |
| Adjarian khachapuri (open, egg yolk) | 2 | 1 | 2 | 3 | 4 | 2 | **14** | No |
| Sevan fish / crayfish | 1 | 1 | 1 | 2 | 2 | 3 | **10** | No |

| Drink | Speed | Car | Shelf / waste | Margin | Demand | Differentiation | Total | Verdict |
|---|---|---|---|---|---|---|---|---|
| Sweet iced latte / frappé | 4 | 5 | 4 | 5 | 5 | 2 | **25** | Core |
| Batch lemonade (sea buckthorn, tarragon, apricot) | 5 | 5 | 3 | 5 | 4 | 3 | **25** | Core (summer) |
| Herbal tea (thyme, mint) | 5 | 4 | 5 | 5 | 3 | 3 | **25** | Core (winter) |
| Bottled tan | 5 | 5 | 3 | 2 | 5 | 1 | **21** | Add-on |
| Mineral water (Jermuk/Bjni) | 5 | 5 | 5 | 2 | 5 | 1 | **23** | Add-on |
| Cold brew (batch) | 5 | 5 | 3 | 5 | 2 | 3 | **23** | Test (sell as "smooth iced coffee") |
| Jezve-to-go Armenian coffee | 2 | 4 | 5 | 5 | 5 | 5 | **26** | Signature (needs fast brewing method) |
| Energy "Rebel" (energy + syrup + ice) | 4 | 5 | 5 | 3 | 2 | 5 | **24** | Test, limited |
| Fresh-squeezed juice | 2 | 5 | 1 | 3 | 4 | 2 | **17** | No (offer bottled) |
| Milkshake (ice-cream based) | 3 | 5 | 3 | 4 | 4 | 2 | **21** | Optional (summer) |

*Fact-check note: all row totals re-added and correct. The Margin scores were set against the pre-correction §3.11 food-cost levels, which were overstated by ≈1.2× (VAT basis). The ranking of items holds, but re-scoring could raise Margin by about 1 point for bought-in gata and khachapuri. Verdicts are judgement calls and do not follow totals strictly (e.g., cookies at 22 are "Add-on" while lahmajo at 20 is "Test").*

### 3.10 American items: likely to resonate or flop?

| American item | Evidence for | Evidence against | Verdict (ASSUMPTION) |
|---|---|---|---|
| **Donuts** | Fried, filled dough is already loved: ponchik is a mass item, with a donut café run by the largest confectioner [15]. KFC and Cofix already sell donuts at 650–880 [6][8]. "Pancake/doughnut" averaged 41 g/day in the Yerevan FFQ [34] | The local price anchor is 80–150 AMD [15]. At 800–1,000 AMD a US donut is 5–7× the ponchik price. Short shelf life | **Resonates only as a reinterpreted ponchik** (fresh-filled to order, local fillings, 350–450 AMD). A small premium "American" line at 650–800 AMD for novelty |
| **Bagels** | One bakery bagel exists (160 AMD) [16]. Green Bean café is known for bagels (A2) | No mass bagel culture. Bread eaters prefer white wheat bread and lavash [35] | **Likely flop** as a core item. Keep at most one bagel SKU, aimed at expats |
| **Breakfast sandwiches** | Eggs and cheese are Armenian breakfast staples [35]. Commuter direction confirmed (B1). Breakfast skipping is reported as widespread [36] | No grab-and-go breakfast habit found. English muffins and bacon add supply risk and are unfamiliar | **Resonates if localised:** egg, cheese and herbs (plus optional basturma or sujukh) in lavash or matnakash at 1,200–1,600 AMD |
| **Cold brew** | Iced coffee is mainstream at retail (65 RTD SKUs) [23] and at chains [7][8]. Batch production suits speed | No cold-brew SKUs seen at SAS. The consumer taste is sweet and milky (A2) | **Product yes, label no:** use it as the base for sweet iced drinks rather than selling "black cold brew" |
| **Energy "Rebels" (Dutch Bros)** | Established energy category (≈75–85 SKUs, 11+ brands, within a 151–153 SKU cocktails/energy/low-alcohol category) [22]. *Fact-check correction: was "151 SKUs" as an energy category.* Night and long-distance drivers. Strong differentiation | Retail cans cost 280–990; a Rebel at 1,500–1,800 is 2–3× the price. Health framing [34][35]. Possible minors restriction unverified | **Limited test** (2–3 SKUs, sugar-free option). Do not make it the brand pillar |
| **Frappé / blended sweet drinks** | Already successful at Coffee House and Cofix [7][8] | Occupied niche at 1,100–1,650 | **Resonates**, but is not a differentiator |
| **Muffins and cookies** | Already sold at Coffee House and Cofix [7][8] | Commodity | Add-on only |
| **Pancakes / waffles** | Crepes 500–1,600 and Belgian waffles 800–2,300 at SAS Food Court [2] | Not car-friendly | No |

### 3.11 Indicative unit economics of localised items (ESTIMATE)

**Method.**
- Bought-in purchase cost is taken as about 75% of the observed retail price. That implies a 33% retail markup (ASSUMPTION; actual supplier quotes needed).
- Food cost % = cost ÷ **VAT-inclusive** menu price. This is the correct basis under the **catering turnover tax** that C4 recommends for year 1: TT replaces VAT, so the whole menu price is revenue, and TT (effective ≈5–6.5% of receipts) is a separate tax line, not food cost (C4 §1). Under the VAT regime the ratio is the same, because both sides go ex-VAT: input VAT on purchases from VAT-registered suppliers (Grand Candy, SAS, Marianna) is recoverable, so cost ÷ 1.2 and price ÷ 1.2 cancel.
- *Fact-check correction: the original method divided only the menu price by 1.2 ("net price") while leaving the VAT-inclusive purchase cost unchanged. That overstated every food-cost % by ≈1.2×. All percentages below are restated; the original figures are shown as "was". Align this basis with C2 (which reports COGS on both gross and net-of-VAT bases) and C4 before the figures go into the model.*

| Item | Cost basis | Cost (AMD) | Menu price (AMD, VAT-incl.) | Food + pack cost % of menu price | Comment |
|---|---|---|---|---|---|
| Ponchik, fresh-filled (bought-in shell) | Grand Candy 150 retail × 0.75 | ≈113 | 400 | **≈28%** (was ≈34%) | Good if customers accept 2.7× the Ponchikanoc price for fresh filling and convenience |
| Mini gata 175 g (bought-in) | 300 × 0.75 | ≈225 | 600 / 700 | **37.5% / 32%** (was 45% / 39%) | Thin margin. Negotiate or make a smaller 100 g piece |
| Zhingyalov hats 90 g (bought-in) | 400 × 0.75 | ≈300 | 750 | **40%** (was 48%) | Better made in-house (herbs + dough) |
| Lahmajo (bought-in) | Karas 480 × 0.75 | ≈360 | 800 | **45%** (was 54%) | Weak. Needs in-house production or a wholesale contract. *Fact-check note: the 480 AMD base is a restaurant's (Karas) Glovo delivery price, not a wholesale quote* |
| Cheese puff / khachapuri piece (bought-in) | 400–520 retail × 0.75 | 300–390 | 700 | **43–56%** (was 51–67%) | Weak at retail-derived cost |
| **Breakfast lavash wrap (in-house)** | Lavash 50 g 60 + 2 eggs 167 (Numbeo 1,004/12) + cheese 40 g 124 (Numbeo 3,099/kg) + herbs and veg 40 + oil 15 + wrap 50 | ≈456 (≈388 with a 15% purchasing discount; ≈395 if the discount is applied to ingredients only, not packaging) | 1,400 / 1,600 | **33% / 29%** (with discount 28% / 24%) (was 39% / 34%; with discount 33% / 29%) | Best food economics among localised items |
| Bottled tan 0.5 L | Aparan 330 × 0.75 | ≈248 | 500 | **≈50%** (was 60%) | Traffic item, not a profit item |
| Batch lemonade 400 ml | Ingredients 150–250 + cup and lid 80 (ASSUMPTION) | ≈280 | 1,100 | **≈25%** (was ≈31%) | High margin. Summer |
| Energy "Rebel" 400 ml | Red Bull 250 ml 670 × 0.75 + syrup 60 + cup and ice 80 = 642.5 | ≈643 | 1,600 | **≈40%** (≈33% on a Burn base: 510 × 0.75 + 140 = 522.5) (was ≈50% / ≈40%) | Weaker than coffee and lemonade. *Fact-check correction: cost was mis-added as ≈660; on the original (inconsistent) basis it would be ≈48%* |

**Takeaways (ESTIMATE).**
1. Low, visible retail anchors cap the margin on bought-in Armenian pastries (about 37–56% food cost for gata, zhingyalov, lahmajo and khachapuri at the lower menu price). In-house assembled items (wrap ≈24–33%) and drinks (lemonade ≈25%) carry the margin. The ranking is unchanged by the fact-check correction; only the levels fell.
2. A food attach scenario (**downgraded at fact-check; not a base-case model input**):
   - **Inputs (ASSUMPTION; no local data on attach rate):** 30–45% of orders include food, averaging 800 AMD per food item; average beverage ticket 1,300–1,500 AMD (A2).
   - **Formula:** average ticket = beverage + attach rate × 800 (1,300 + 0.30 × 800 = 1,540; 1,500 + 0.45 × 800 = 1,860).
   - **Result:** about **1,540–1,860 AMD**.
   - **Status:** ASSUMPTION-driven, unreconciled. *Fact-check correction (downgraded): the arithmetic holds, but the 800 AMD food item and the attach rate are unsupported, and the result contradicts the sibling workstreams: A2 §4.6 says hot savoury food "could raise the ticket to about 3,500–4,000 AMD"; A3 §4.4 plans around a 3,500–4,500 AMD ticket; C2 models 1,691 AMD per drink and 1,130 AMD per food item (croissant/wrap/gata mix). A4's own §3.12 menu prices the hero wrap at 1,400–1,700 and croissant sandwiches at 1,300–1,600, which is hard to square with an 800 AMD average food item. Using C2's inputs at 30–45% attach gives 1,691 + 0.30 × 1,130 ≈ 2,030 to 1,691 + 0.45 × 1,130 ≈ 2,200 AMD. A2/A3's 3,500+ looks optimistic given the affordability evidence in §3.2. Do not feed 1,540–1,860 into the model until A2, A3, A4 and C2 agree on one ticket build-up (drinks per car, price per drink, attach rate, price per food item).*

### 3.12 Recommended localised drive-thru menu (to test, ASSUMPTION)

| Slot | Item | Price (AMD) | Prep | Supply |
|---|---|---|---|---|
| Hero hot food | Armenian breakfast lavash wrap: egg, cheese and herbs; + basturma option (+300) | 1,400–1,700 | Griddle press 60–90 s | In-house; lavash from local bakery |
| Hot food | Zhingyalov hats (vegetarian), served warm | 800–1,000 | Reheat 60 s (if bought-in) or griddle | In-house (preferred) or buy-in |
| Hot food | Cheese puff pastry (penovani-style) / Imeruli piece | 600–800 | Oven reheat 90 s | Buy-in (negotiate wholesale) |
| Hot food | Folded lahmajo with greens and lemon | 800–900 | Reheat 60–90 s | Buy-in or par-bake |
| Sandwich | Croissant sandwich (ham-cheese / chicken) | 1,300–1,600 | Pre-made, warmed | Buy-in + in-house fill |
| Sweet | Fresh-filled ponchik (vanilla, chocolate, apricot, matsun cream) | 350–450 | Fill to order 20 s | Buy-in shells |
| Sweet | Mini Sevan/Gavar gata | 500–700 | None | Buy-in (Nor-Nar, Zeytun or Grand Candy type) |
| Sweet | Cookie / muffin | 500–700 | None | Buy-in |
| Coffee | Espresso range + **sweet iced lattes** (per A2 pricing) | 1,000–1,800 | Machine | — |
| Signature | **Jezve-to-go** Armenian coffee | 700–900 | Fast brewing device needed (unverified) | Local roaster |
| Cold | Batch lemonades (sea buckthorn, tarragon, apricot) | 1,000–1,300 | Pour 15 s | In-house |
| Cold | Bottled tan, Jermuk/Bjni | 300–600 | None | Distributors |
| Hot | Herbal tea (thyme, mint) / hot chocolate | 500–800 | 30 s | — |
| Test | Energy "Rebel" (2 SKUs incl. sugar-free); cold-brew-based iced drinks; 1 US-style donut | 650–1,800 | 30–45 s | — |
| Combos | Coffee + pastry; coffee + wrap | 1,900–2,600 | — | — |

---

## 4. Implications for the drive-thru concept (critical)

1. **"American-style" should describe the service format, not the menu.** The evidence shows a bread-and-pastry diet and once-weekly fast-food habits. Local substitutes cost 80–1,350 AMD and are available at every supermarket and bakery. An American menu (donuts, bagels, English-muffin sandwiches, black cold brew) is the weakest part of the founder's idea. The format itself — speed, a car lane, mobile ordering, consistent quality — is transferable.
2. **Food is a differentiator against Coffee House, but only if it is hot, savoury and fast.**
   - Coffee House, the incumbent on the M4, sells sweets but no savoury food on its delivery menu [7] (re-confirmed at fact-check: no sandwich items on Glovo).
   - Fuel-station cafés sell hot dogs [27].
   - A hot Armenian breakfast wrap and zhingyalov hats fill a real gap.

   **Disconfirming risk:** both incumbents can copy this cheaply within months (ASSUMPTION).
3. **The ticket is constrained.**
   - Households spend only 2.8–3.5% of consumption on food away from home, and 38% of households report money "enough only for food" or less [29][44]. *Fact-check note: the ILCS share is a survey floor for the typical household, not a hard cap. A1 shows 2024 food-service turnover implies ≈8,444 AMD per resident per month, about 5× the ILCS 1,709, because the survey misses tourists, business spending and high-income non-response. For a highway site serving travellers, this constraint is overstated.*
   - Food prices therefore need to sit at 400–1,600 AMD.
   - A ticket above about 2,000 AMD will be occasional among local households, except for summer leisure groups heading to Sevan (ASSUMPTION).
   - **Average ticket: unreconciled (downgraded at fact-check).** A4's build-up gives about 1,540–1,860 AMD, but it rests on an unsupported 800 AMD food item and attach rate. C2's inputs (1,691 per drink, 1,130 per food item) at 30–45% attach give about 2,030–2,200 AMD; A2 and A3 use 3,500–4,500 AMD, which looks optimistic given the affordability evidence. *Fact-check correction: was "Base case: average ticket about 1,500–1,900 AMD with food attach (ESTIMATE)". Do not use any of these as the base case until A2, A3, A4 and C2 agree one ticket build-up (§3.11).*
4. **Margins on local pastries are thin.**
   - Visible retail anchors cap them: bought-in gata, lahmajo and khachapuri run at about 37–56% food cost (ESTIMATE). *Fact-check correction: was 45–67%, which compared a VAT-inclusive cost with an ex-VAT price (§3.11).*
   - A credible plan needs **in-house assembly** (wraps, sandwiches) and **high-margin drinks** (lemonade, iced coffee, tea) to carry the P&L, plus negotiated wholesale contracts.
5. **Seasonality cuts both ways.**
   - **Summer:** cold drinks, lemonades and tan for Sevan-bound leisure traffic.
   - **Winter:** hot tea, gata and ponchik for commuters.
   - Lent is too small a segment to plan around (4% fast always or often [32]).
   - Sevan fish, crayfish, corn and dried fruit should stay with roadside specialists. Fish is an occasion food (2% daily [35]) and dried fruit carries aflatoxin risk [39].
6. **The Sevan end of the corridor is the wrong place for a daily-habit food business.**
   - The fish-stall cluster sits at km 68–74, past Sevan town. B1 shows the volume is near Yerevan (km 9–31).
   - A Sevan-adjacent site would rely on 10–14 summer weekends (B1) and on impulse buyers who already have strong local alternatives.
7. **The health trend is an add-on, not the core.**
   - Plant, lactose-free and protein options exist and should be offered: a 200–300 AMD oat surcharge covers the ≈115 AMD extra cost.
   - Daily confectionery use (62–73%) shows indulgence still dominates [35].
8. **Energy-drink "Rebels" are a risk.**
   - A Rebel at 1,500–1,800 AMD competes with 510–990 AMD cans.
   - Its food cost (≈33–40%) is worse than coffee's. *Fact-check correction: was ≈40–50% (VAT-basis error and a cost mis-added as 660 instead of 643 AMD; §3.11).*
   - Public-health framing is negative.
   - An age-of-sale rule may exist (unverified).
   - Test it, but do not anchor the brand on it.
9. **Starbucks brand awareness is already present through retail ready-to-drink coffee** (1,250 AMD/220 ml [23]). Combined with the Starbucks entry risk flagged in A2, this argues for a *local* brand story (Armenian coffee, gata, herbs) rather than a US pastiche that Starbucks could overtake.
10. **Evidence quality is moderate to weak on behaviour.**
    - The key consumer facts come from one 2019 Yerevan FFQ with an educated, male-skewed sample, and one 24HR survey with no stated year.
    - There are no surveys on coffee frequency, breakfast-out or drive-thru willingness.
    - The menu and price recommendations above are hypotheses. A pre-launch survey and a pop-up test should validate them (§5).

---

## 5. Data gaps & how to verify them

| Gap | Why it matters | How to verify (agency / document / fieldwork) |
|---|---|---|
| Coffee drinking frequency; soorj vs espresso; at-home vs out-of-home; iced-coffee use by age | Sizes beverage demand and the iced/sweet mix | Commission a survey: n ≥ 600, Yerevan + Kotayk + Gegharkunik, quotas by age and car ownership. Use CATI or online via MPG/Gallup International Armenia, CRRC-Armenia or a local agency (e.g., Breavis). Also request CRRC to add items to a future omnibus |
| Breakfast-out and on-the-go eating habits; willingness to pay for breakfast items | Hero-item sizing and attach rate | Same survey plus 2–3 focus groups (commuters from Abovyan, Charentsavan, Hrazdan). A 2-week pop-up price test at an M4 fuel station |
| Fast-food attitudes and frequency since 2019 | The FFQ is 7 years old and biased | Request the 24HR/FFQ microdata from the Center for Ecological-Noosphere Studies (Pipoyan et al.); ILCS microdata (Armstat) on food away from home by decile |
| **Mayak** ponchik (location, prices); Ponchik Monchik; **Kaghtsr**; **Yasaman**; **Dustr Margo**; **Tashir** in-store prices | Supplier shortlist and price anchors | Store visits and photographs of price boards (2 days). Supplier RFQ letters asking for wholesale prices, MOQs, delivery to M4 km 10–30, and frozen/bake-off availability. Yandex Maps / 2GIS listings checked manually |
| Wholesale (HoReCa) prices for pastries, dairy, plant milk, tan, water | Replaces the "75% of retail" assumption in §3.11 | RFQs to Grand Candy, Nor-Nar, Zeytun, Tnakan, Karas, Marianna, Ashtarak Kat, Aparan, Bjni, Jermuk Group and Alpro/Valsoia importers |
| Sevan roadside prices (sig/whitefish, crayfish, corn, fruit, gata) and seasonality | Seasonal-menu decisions and competitive context | Fieldwork on M4 km 60–75 on one summer weekend and one winter weekday: price photographs and vendor counts. For fishing seasons and quotas, check Ministry of Environment orders on arlis.am |
| Ishkhan conservation and legal sale status | Avoid regulatory or branding risk | IUCN Red List page for *Salmo ischchan*; Ministry of Environment (Sevan fish stock decisions) |
| **Energy-drink regulation** (age-of-sale, school restrictions, labelling) | Feasibility of the "Rebel" line | arlis.am (Law on Trade and Services; Law on Food Safety amendments); e-draft.am drafts; Food Safety Inspection Body |
| Speed benchmarks and the prep-time assumptions in §3.9 | Throughput and lane design | Time-and-motion trial in a test kitchen (n ≥ 50 orders per item); supplier specifications for high-speed ovens and fast Turkish/jezve brewing devices |
| Food attach rate and average ticket at comparable outlets | Revenue model | Mystery shopping and receipt sampling at Coffee House Drive-Thru (M4) and Max Cafe km 12.2 (receipt counts by hour); POS data partnership, if obtainable |
| OSM supply-side counts (bakeries, fast food by cuisine) | Competitive density | Re-run the Overpass query (amenity=fast_food, cuisine tags; shop=bakery) when the mirrors are available; the query is saved in the scratchpad |
| Consumer research by Ipsos, Breavis or MPG on food and beverages | Triangulation | Contact the agencies directly. Was not searchable in this run because the WebSearch budget was exhausted |
| Glovo vs in-store price gap | Price-anchor accuracy | Five-store in-person price check (Karas, Tashir, Tumanyan Shaurma, Coffee House, Cofix) |

---

## 6. Sources (all accessed 2026-10-10 unless noted)

1. Glovo Yerevan, Food category (store list, 33 stores; subcategory filters). https://glovoapp.com/en/am/yerevan/categories/food_1
2. Glovo, SAS Food Court menu (pastries, khachapuri, sandwiches, hot dogs, shawarma, lahmajo, omelettes, juices, lemonades, Jermuk, tan, crepes; 98% rating, 1k+ reviews). https://glovoapp.com/en/am/yerevan/stores/sas-food-court-yrv
3. Glovo, Tumanyan Shaurma menu. https://glovoapp.com/en/am/yerevan/stores/tumanyan-shaurma
4. Glovo, Tashir Pizza menu. https://glovoapp.com/en/am/yerevan/stores/tashir-pizza (tashirpizza.am returned HTTP 403)
5. Glovo, KARAS menu (lahmajo, khachapuri, pies, tan). https://glovoapp.com/en/am/yerevan/stores/karas-yvn
6. Glovo, KFC Armenia menu (burgers, twisters, donuts, Burn). https://glovoapp.com/en/am/yerevan/stores/kfc-yrv
7. Glovo, Coffee House menu (sweets, teas, matcha, lemonades, smoothies, shakes, protein shakes). https://glovoapp.com/en/am/yerevan/stores/coffee-house-yrv
8. Glovo, Cofix menu (coffee, iced coffee, donuts, muffins, milkshakes). https://glovoapp.com/en/am/yerevan/stores/cofix-yrv
9. Glovo, JAZZVE menu (breakfasts, sandwiches, lahmajo, lavash rolls). https://glovoapp.com/en/am/yerevan/stores/jazzve-yrv
10. Glovo, Lebanese Kunji menu (manakish, lahmajo, cheese pies). https://glovoapp.com/en/am/yerevan/stores/lebanese-kunji
11. Glovo, Mic Mac Burgers menu. https://glovoapp.com/en/am/yerevan/stores/mic-mac-burgers-yrv
12. Glovo, Art Lunch menu (gata, pies, cinnamon roll, ciabattas, lavash 50 g). https://glovoapp.com/en/am/yerevan/stores/art-lunch-yrv-yrv
13. Glovo, Diana's Bakeshop menu (cakes and slices 550–1,000). https://glovoapp.com/en/am/yerevan/stores/dianas-bakeshop-yrv
14. Glovo, Shawarma subcategory (12 outlets). https://glovoapp.com/en/am/yerevan/categories/food_1?type=shawarma_35119
15. Grand Candy e-shop (VERIFIED, company's own site):
    - homepage and category counts: https://grandcandy.am/en
    - stores (19): https://grandcandy.am/stores
    - Donuts and cocoa: https://grandcandy.am/product-category/donuts-and-cocoa
    - Bakery products (gata, croissant): https://grandcandy.am/product-category/bakery-products
16. SAS supermarket e-shop, Bakery category (52 SKUs). https://www.sas.am/en/catalog/vypechka/
17. SAS e-shop, Sandwich category (9 SKUs, incl. "bread with jengyal" 90 g). https://www.sas.am/en/catalog/drugie_gotovye_bljuda/
18. SAS e-shop, Milk category (24 of 49 SKUs visible). https://www.sas.am/en/catalog/moloko/
19. SAS e-shop, Non-dairy drinks (24 SKUs). https://www.sas.am/en/catalog/vochkatnayin/
20. SAS e-shop, Tan & okroshka (20 SKUs). https://www.sas.am/en/catalog/tan_okroshka/
21. SAS e-shop, Water (167 SKUs; pages 1–2 viewed). https://www.sas.am/en/catalog/voda/
22. SAS e-shop, "Cocktails, energy drinks, low-alcohol beverages" (151 SKUs at research, 153 at fact-check on 10 Oct 2026, of which ≈75–85 are energy drinks; page 1 viewed). https://www.sas.am/en/catalog/kokteyl_energeticheskiy_napitok/
23. SAS e-shop, Ice coffee (65 SKUs; page 1 viewed). https://www.sas.am/en/catalog/kholodnoe_kofe/
24. SAS e-shop, Refreshing drinks (302 SKUs; page 1 viewed). https://www.sas.am/en/catalog/osvezhayushchiy_napitok/
25. SAS e-shop, Fresh fish (rainbow trout 3,050 AMD/kg). https://www.sas.am/en/catalog/zhivaya_ryba/
26. Karas, branches page (10 branches). https://karas.am/am/contact
    - 26a. Ashtarak Kat (Ashtarak Milk LLC), product site. https://ashtarakkat.am/
27. Max Oil, company site (50+ stations; Max Cafe incl. Yerevan–Sevan highway km 12.2; Max Coffee, hot dogs). https://maxoil.am/
28. Numbeo, Cost of Living in Yerevan (AMD), last update 3 Oct 2026, 112 contributors. https://www.numbeo.com/cost-of-living/in/Yerevan?displayCurrency=AMD
29. CRRC Caucasus Barometer 2024 Armenia, ECONSTN (household economic situation); fieldwork 27 Jul–10 Oct 2024. https://caucasusbarometer.org/en/cb2024am/ECONSTN/
30. CRRC CB 2024 Armenia, OWNCARS. https://caucasusbarometer.org/en/cb2024am/OWNCARS/
31. CRRC CB 2024 Armenia, NOMONFD. https://caucasusbarometer.org/en/cb2024am/NOMONFD/
32. CRRC CB 2024 Armenia, RELFAST. https://caucasusbarometer.org/en/cb2024am/RELFAST/ (codebook, which confirms there are no eating-out, coffee or restaurant variables: https://caucasusbarometer.org/en/cb2024am/codebook/)
33. Glovo Yerevan, Food → "Breakfast" filter (one store listed: JAZZVE, 97%, 10 ratings) and "Bakery" filter (six stores). https://glovoapp.com/en/am/yerevan/categories/food_1?type=breakfast_35073 ; https://glovoapp.com/en/am/yerevan/categories/food_1?type=bakery_35389
34. Pipoyan D, Beglaryan M, Stepanyan S, Merendino N. "Trans-Fatty Acids in Fast-Food and Intake Assessment for Yerevan's Population, Armenia." *Foods* 2022;11(9):1294. Retrieved via PubMed/PMC (PMC9105336). [DOI](https://doi.org/10.3390/foods11091294)
35. Pipoyan D, Beglaryan M, Harutyunyan B, Pires SM. "Assessment of dietary patterns and macronutrient intake among the adult population of Armenia." *Frontiers in Nutrition* 2026 (publ. 20 May 2026). Retrieved via PubMed/PMC (PMC13229743). [DOI](https://doi.org/10.3389/fnut.2026.1840868)
36. Stepanyan S, Pipoyan D, Beglaryan M, Merendino N. "Assessing Dietary Intakes from Household Budget Survey in Armenia, 2008–2019." *Foods* 2022;11(18):2847. Retrieved via PubMed/PMC (PMC9498088). [DOI](https://doi.org/10.3390/foods11182847)
37. Aslanyan L, Demirchyan A. "Barriers to healthy eating practices among school-aged children in Armenia: A qualitative study." *Appetite* 2024 (abstract via PubMed). [DOI](https://doi.org/10.1016/j.appet.2024.107649)
38. Aneli S et al. "Impact of cultural and genetic structure on food choices along the Silk Road." *PNAS* 2022 (abstract via PubMed; background only). [DOI](https://doi.org/10.1073/pnas.2209311119)
39. Pipoyan D, Beglaryan M, Arshakyan Y, Harutyunyan B. "Occurrence, Dietary Exposure Scenarios and Risk Assessment of Aflatoxins from Dried Fruits and Chocolates in Armenia." *Foods* 2026;15(8):1329 (abstract via PubMed). [DOI](https://doi.org/10.3390/foods15081329)
40. Wikipedia, "Sevan trout". https://en.wikipedia.org/wiki/Sevan_trout
41. Wikipedia, "Lake Sevan". https://en.wikipedia.org/wiki/Lake_Sevan
42. Wikipedia, "Gata (food)". https://en.wikipedia.org/wiki/Gata_(food)
43. Wikipedia, "Zhingyalov hats". https://en.wikipedia.org/wiki/Zhingyalov_hats
44. Internal workstream A1, Macro & consumer (ILCS 2024 food away from home; wages; car ownership; FX). /home/user/Drive-thru/research/A1-macro-consumer.md
45. Internal workstream A2, Coffee & café market (Coffee House, Cofix, Coffeeshop Company prices; soorj vs espresso; affordability). /home/user/Drive-thru/research/A2-coffee-market.md
46. Internal workstream B1, M4 traffic (commuter vs leisure direction; seasonality). /home/user/Drive-thru/research/B1-m4-traffic.md
47. Internal workstream B2, M4 POIs from OpenStreetMap (shop=seafood cluster km 68–74; Max Cafe km 12.2; fast-food and café points). /home/user/Drive-thru/research/B2-m4-pois.csv

**Attempted but unavailable (no data used):**
- ponchikmonchik.am (HTTP 522)
- kaghtsr.am, dustrmargo.am (DNS failure)
- yasaman.am (empty page)
- marianna.am (HTTP 503)
- menu.am (Yandex captcha)
- Yandex Maps Coffee House Drive-Thru menu (timeout)
- Overpass API mirrors overpass-api.de, overpass.kumi.systems, private.coffee, maps.mail.ru (500/reset/504)

---

## 7. Fact-check log

*Adversarial fact-check, 2026-10-10. Sources re-opened directly; no WebSearch calls; no source was unreachable. Result counts: 16 confirmed, 5 corrected, 1 downgraded, 0 wrong, 0 unverifiable.*

| # | Claim | Result | Correction / evidence |
|---|---|---|---|
| 1 | 24HR recall (Pipoyan et al. 2026): n = 1,400; bread/flour 53% of energy; 1,230/1,400 (88%) table vs ≈96% text; 40% pastries; 1,738 kcal (W 1,608, M 1,892); fish 2% (28); scrambled eggs 238 (17%) (§1.1; §2 rows 1–6; §3.1) | Confirmed | PMC13229743 re-opened; every figure matches, including the text/table inconsistency (87.9% vs 96%). No fieldwork year; database cited as a 2023 Nutrients paper, so data are ≥3 years old (disclosed). Minor: Table 2 lists 142 under an "Eggs" group while the text says 11% ate boiled eggs, so labelling 142 as "boiled eggs" is approximate |
| 2 | Yerevan FFQ (Foods 2022), autumn 2019, n = 423: pastry 76.1 g/day, fried chicken 53.1, hot dog/burger 50.0, shawarma 49.3; ≈1×/week (0.38–1.93); King County 2.07; 90% higher education, 56% male, 66% refused income, mean age 31.9; trans fats ≤2% since Jan 2018 (§1.1–1.2; §2 rows 7–8; §3.2) | Confirmed | PMC9105336 re-opened; all values match (76.09, 53.09, 49.97, 49.26, 41.36; Iran 1.673; age 31.91). TR CU 024/2011 limit went from 20% to 2% in Jan 2018. Data are 7 years old (flagged in §4.10) |
| 3 | ESTIMATE: dough-based items ≈41% of fast-food grams (§1.1) | Confirmed | 76.1 + 41.4 + 35.0 + 32.2 = 184.7 g ÷ 449.8 g = 41.1%; with pizza 48.6%. Formula now shown inline in §1.1 |
| 4 | Food away from home 2.8% national, 3.5% urban (1,709 / 2,293 AMD/person/month, ILCS 2024) (§1.2; §2 row 9; §4.3) | Confirmed (caveat added) | Armstat Social Snapshot and Poverty 2025, Tables 3.5–3.6 (rural 604, 1.2%). Caveat added inline: A1 shows food-service turnover implies ≈8,444 AMD/resident/month (≈5× ILCS), so the share is a survey floor, not a hard cap on a highway-site ticket |
| 5 | CB 2024 ECONSTN: 38% food-only or less; 19% durables/anything. NOMONFD: 14% lacked food money at least monthly; 68% never (§1.2; §2 row 10; §3.2) | Confirmed | ECONSTN 12/26/42/12/7; NOMONFD 2/4/8 and 68. Fieldwork 27 Jul–10 Oct 2024 |
| 6 | Car ownership 46% (CB 2024) vs 41.2% (ILCS 2024) (§2 row 11; §3.2) | Confirmed | OWNCARS Yes 46 / No 54; ILCS 41.2% consistent with A1 and Armstat poverty_2025_en_4.pdf |
| 7 | Religious fasting: 4% always/often; 83% never (CB 2024 RELFAST) (§1.8; §2 row 12; §3.6) | Confirmed | Always 2, Often 2, Sometimes 5, Rarely 8, Never 83, DK/RA 1; asked of denomination members only |
| 8 | Grand Candy ponchik 130/150/150/80 AMD; 19 stores; US donut 5–7× ponchik; 400 AMD ponchik 2.7× (§1.3–1.4; §2 rows 13, 29; §3.3; §3.11) | Confirmed | grandcandy.am prices and 19 store addresses (incl. Mashtots 54) match. The 150 and 80 AMD items are "Ponchikanoc only"; 130 AMD vanilla is the widely available one. 800/150 = 5.3; 1,000/150 = 6.7; 400/150 = 2.67 |
| 9 | KFC donut 650, Burn 800; Cofix donut 880, banana-Nutella 1,100, milkshakes 1,650; Cofix 12 iced SKUs 550–1,760 (§1.4–1.5; §2 row 14; §3.8) | Confirmed | Glovo menus match. The 12 "Classic cold" items include iced matcha, Kinder and Nutella drinks, so not all are strictly coffee. REPORTED is correct |
| 10 | Coffee House: shakes/frappés 1,400; smoothies 1,100; matcha 1,000–1,100; protein shakes 1,600 (3 SKUs); no savoury food (§1.5; §3.4; §3.5; §3.8; §4.2) | **Corrected** | Matcha runs **1,000–1,300** (cream-cheese matcha latte and sky matcha 1,300; matcha latte 1,000; matcha raf 1,100). Fixed in §1.5, §3.4, §3.5. All other figures confirmed; no sandwich items. No effect on the decision |
| 11 | SAS energy drinks: Red Bull 670, Monster 990, Burn 510; "energy/cocktail category holds 151 SKUs"; "broad energy category (151 SKUs, 11+ brands)" (§1.6; §2 row 24; §3.4; §3.7; §3.10) | **Corrected** | Prices re-confirmed (plus Jaguar 770, Boom 340). The category is "Cocktails, energy drinks, low-alcohol beverages", now 153 SKUs, and includes alcoholic RTD brands; energy-brand counts sum to only **≈75–85 SKUs**. Fixed in §1.6, §2 row 24, §3.4, §3.7, §3.10 and source [22]. Max Power 280 AMD was not on page 1 and could not be re-seen (flagged in §1.6 and §2 row 24) |
| 12 | SAS RTD iced coffee: 65 SKUs, 28 Armenian; Starbucks RTD 1,250 AMD/220 ml (§1.5; §2 row 25; §3.4; §4.9) | Confirmed | "Ice coffee (65)", Armenia filter 28; Starbucks Cappuccino 220 ml 1,250 (5,682 AMD/L); 9 Starbucks SKUs |
| 13 | ESTIMATE: oat milk +≈115 AMD per 150 ml drink; Alpro Barista Oat 1,410/L; Marianna 642/L; 24 plant-milk SKUs, 5 barista (§1.7; §2 rows 26–27, 33; §3.5) | Confirmed | 0.15 × (1,410 − 642) = 115.2. Alpro on promotion at 1,140 (1–14 Oct 2026); using the regular price is right. With UHT Marianna at 790/L the gap is ≈93 AMD; conclusion holds |
| 14 | Numbeo Yerevan (upd. 3 Oct 2026): combo 3,825 (2,895–4,990); inexpensive meal 4,000; milk 592/L; eggs 1,004/12; cheese 3,099/kg (§2 rows 27, 34; §3.3; §3.11) | Confirmed | All values match; cheese 1,405.79/lb ÷ 0.4536 = 3,099/kg. 112 contributors. REPORTED is correct |
| 15 | Affordability: 1,950 AMD cappuccino ≈1.1 h of gross pay at "177 h, ≈1,775 AMD/h" per A2; 2,000 AMD combo ≈1.1 h; Numbeo combo ≈2.2 h (§3.2) | **Corrected** | Wage 314,196 AMD (Aug 2026) confirmed on Armstat. A2 uses **173.3 h → 1,813 AMD/h**, not 177 h. Recomputed: 2,000/1,813 = 1.10 h; 3,825/1,813 = **2.11 h**. Note added that these are gross; net pay is ≈25% lower (20% PIT + 5% pension), so the real burden is ≈⅓ higher. Conclusion unchanged |
| 16 | §3.11 unit economics: cost = 75% of retail; net price = menu ÷ 1.2; food cost % = cost ÷ net price → ponchik ≈34%, gata 45/39%, zhingyalov 48%, lahmajo 54%, cheese puff 51–67%, wrap 39/34%, tan 60%, lemonade ≈31%; headline "bought-in pastries 45–67%" (§1.10; §3.11; §4.4) | **Corrected** | Arithmetic correct, method inconsistent: a VAT-inclusive cost was divided by an ex-VAT price. Under VAT, input VAT is recoverable (cost ÷ 1.2 too); under the catering TT recommended by C4 for year 1, price is not divided by 1.2. Every % was overstated ≈1.2×. Restated: ponchik **≈28%**; gata **37.5/32%**; zhingyalov **40%**; lahmajo **45%**; cheese puff **43–56%**; wrap **33/29%** (28/24% with discount); tan **≈50%**; lemonade **≈25%**. Headline now **≈37–56%** for bought-in pastries and **≈24–33%** for the wrap. Fixed in §1.10, §3.11 method and table, §4.4. Also noted: lahmajo cost base is Karas's Glovo restaurant price, not a wholesale quote. Ranking unchanged; align tax basis with C2/C4 before modelling |
| 17 | Energy "Rebel": cost = 670 × 0.75 + 60 + 80 ≈ 660 AMD; ≈50% food cost at 1,600 (≈40% on Burn) (§1.6; §3.11; §4.8) | **Corrected** | 502.5 + 60 + 80 = **642.5**, not 660; ≈48% on the original basis. On a consistent tax basis: **≈40%** (Red Bull), **≈33%** (Burn: 522.5/1,600). Fixed in §1.6, §3.11, §4.8. Still weaker than coffee and lemonade |
| 18 | In-house wrap: 60 + 167 + 124 + 40 + 15 + 50 ≈ 457 AMD (≈388 with 15% discount); 39%/34% (33%/29%) (§3.11) | Confirmed (with caveats) | Recomputed 456.4 (rounding). The 15% discount was also applied to packaging (≈395 if ingredients only), and the VAT-basis issue (#16) applies: true cost ≈33%/29%, or 28%/24% with discount. Restated in §3.11 |
| 19 | Average ticket: beverage 1,300–1,500 + 30–45% × 800 = 1,540–1,860 AMD; §4 base case ≈1,500–1,900 (§3.11 takeaway 2; §4.3) | **Downgraded** | Arithmetic checks, but the 800 AMD food item and attach rate are unsupported ASSUMPTIONs and contradict A2 §4.6 (3,500–4,000 with food), A3 §4.4 (3,500–4,500), C2 (1,691/drink, 1,130/food item) and A4's own §3.12 menu prices. With C2 inputs at 30–45% attach: **≈2,030–2,200 AMD**. Base-case label removed in §3.11 and §4.3; do not model until A2, A3, A4 and C2 agree one ticket build-up |
| 20 | Karas 10 branches incl. Abovyan; lahmajo 480 (690 with cheese), khachapuri 480, tan 0.5 L 470; Max Oil 50+ stations, Max Cafe km 12.2; 10 OSM seafood stalls km ≈68–74 (§2 rows 15, 30–31; §3.6–3.8) | Confirmed | karas.am lists 10 branches; Glovo prices match; maxoil.am "50 and more" stations 24/7; B2 CSV has 10 shop=seafood points at km 68.1–74.1. The Karas Abovyan branch is in town (1/70 Hanrapetutyan Ave), not on the highway frontage (clarified in §1.10) |
| 21 | Aflatoxins above EU limits in Yerevan open-market dried fruit (Foods 2026, VERIFIED abstract); Sevan trout fishing stopped 1976; IUCN 3.1 extinct per Wikipedia (REPORTED) (§1.9; §3.6) | Confirmed | Crossref 10.3390/foods15081329 (Foods 15(8), 10 Apr 2026) abstract matches; small sample (5 dried-fruit composites). Wikipedia shows status EX, IUCN3.1 (Freyhof 2019). The 1976 Council of Ministers sentence carries a {{Citation needed}} flag, so it is weaker than presented |
| 22 | §3.9 suitability matrix totals (gata 26, wrap 24, ponchik 23 … fish 10; iced latte 25 … juice 17) (§3.9) | Confirmed | All 25 row totals re-added and correct. Scores are ASSUMPTIONs; verdicts do not strictly follow totals (cookies 22 "Add-on" vs lahmajo 20 "Test"). Margin scores relied on the overstated §3.11 food-cost levels; note added under the matrix that re-scoring could raise gata and khachapuri Margin |

**Fact-checker's overall assessment.** The primary-source data in A4 hold up well: almost every number, unit and date matched and the status tags are appropriate. The errors sit in A4's own analysis. Four matter for the investment decision: (1) the VAT basis of the §3.11 food-cost percentages; (2) the unreconciled average ticket; (3) presenting the ILCS food-away-from-home share as a hard constraint; (4) describing a mixed cocktails/energy/low-alcohol category as a 151-SKU energy category. Stale-data risks are disclosed (FFQ from 2019; 24HR survey with no fieldwork year).
