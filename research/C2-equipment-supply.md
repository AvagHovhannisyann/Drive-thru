# C2 — Equipment, Technology, Supply Chain & Cost of Goods
## Premium drive-thru coffee & food unit, Armenia (M4 Yerevan–Sevan corridor or alternative)

*Prepared: 2026-10-10. Analyst workstream C2. All AMD/USD conversions use the official Central Bank of Armenia (CBA) rate for 2026-10-09: **USD 1 = AMD 361.93; EUR 1 = AMD 405.58; GBP 1 = AMD 478.65; RUB 1 = AMD 4.2677; UAH 1 = AMD 8.0592; AUD 1 = AMD 252.45** [S1].*

**Status tags used:** VERIFIED = an official or primary source I opened (CBA, bank tariff documents, legal texts). REPORTED = a credible secondary source, or a supplier/retailer web price (opened, or seen as a search snippet where noted), with URL. ESTIMATE = my own calculation (formula and inputs shown). ASSUMPTION = analyst judgement (basis given).

**Important caveats**
- **No supplier quotations were obtained.** Every equipment and ingredient price below is a published list or retail price. Negotiated HoReCa or dealer prices will be different: usually lower for consumables, and often higher for imported equipment once dealer margin, freight and service are added.
- **Web-search budget.** The research session hit its web-search limit (200 calls, shared across agents) before a few items could be searched. These are: iiko and R-Keeper partners in Armenia, HME/3M headset pricing, Telcell QR fees, Google Pay acceptance, and EU-spec refrigeration, dishwasher and water-treatment prices. They are listed in Section 5 with a verification route.

---

## 1. Executive summary

1. **One credible local channel for the core espresso stack, with no published prices.** The Horeca LLC (Yerevan) is an authorised Mahlkönig dealer [S3]. Its site links La Marzocco, Victoria Arduino, Nuova Simonelli, Franke, Hoshizaki, Bravilor, Santos, Hamilton Beach, Rational and Electrolux Professional. It claims a spare-parts department, warranty and service technicians, and more than 700 projects since 2015 [S2]. **I found no Armenian dealer or service partner for Eversys, WMF, Schaerer, Merrychef or TurboChef.** For a flagship design that relies on super-automatics or speed ovens, that is a material uptime risk. No Armenian dealer publishes equipment prices, so formal quotes are mandatory.
2. **Duties are favourable for the bar, less so for refrigeration.** The EAEU Common External Tariff (CET) rates are [S6][S7]:
   - 0%: commercial coffee machines (HS 8419 81 200 0), commercial dishwashers (8422 19), water-filtration equipment (8421 21) and other commercial food-heating equipment (8419 81 800 0).
   - 10%: ice machines and other refrigeration (8418 69 000 8), refrigerated display counters (8418 50 190 0) and microwave ovens (8516 50).
   - 5%: domestic-type blenders (8509 40).
   - Import VAT is 20% [S8]. Speed ovens (microwave plus impingement) could fall under 0% or 10%, so a classification ruling is needed.
   - ESTIMATE: landed cost ≈ **1.30× the foreign ex-VAT price for 0%-duty items and ≈1.43× for 10%-duty items**. Formula: ×1.08 freight/insurance (ASSUMPTION) × (1+duty) × 1.20 VAT. VAT is recoverable only if the company is VAT-registered.
3. **US-spec equipment is not usable as-is.** Most US list prices are for 115/208 V, 60 Hz units. Armenia runs on 230/400 V, 50 Hz (ASSUMPTION; standard, confirm with ENA). EU or international-spec units must be ordered, so US prices are benchmarks only.
4. **Core bar and kitchen equipment, landed, before installation, technology and building (ESTIMATE):**
   - **Lean ≈ USD 45–52k (AMD 16.4–18.8m).**
   - **Mid-range ≈ USD 78–89k (AMD 28–32m).**
   - **Flagship ≈ USD 168–181k (AMD 61–66m).**
   - Roughly 71–85% of each total rests on published list prices (lean 72–80%, mid 71–81%, flagship 79–85%). The rest (refrigeration, warewashing, water treatment, smallwares) are ASSUMPTION ranges.
   - About one-sixth of each figure is import VAT, which can be reclaimed if the company is VAT-registered.
   - *Fact-check correction: the lean total was USD 37.8–43.5k (AMD 13.7–15.7m). It rested on a stale Kyiv retail price for the Nuova Simonelli Appia Life (UAH 150,800 ≈ USD 3,358). That price is VAT-inclusive, and Kofemarket's own USD display implies about 28.5 UAH/USD against about 44.9 today. Current US list is USD 8,505–8,990, which gives ≈USD 11.0–11.7k landed instead of 4.35k. Current E80 prices (USD 3,049–3,199) add a further ≈USD 0.8–1.2k. The lean total is therefore about 20% higher. Mid (was 77.3–88.0k) and flagship (was 166.8–180.3k) change by less than 1%: the higher Merrychef e2s and TurboChef Sota prices are offset by removing double-counted Russian VAT on the EK43. The original "75–85% on list prices" was also wrong: the original figures gave 66–85%. See §3.1.6 and §7.*
5. **The 2026 card-fee cap does not apply under a restaurant MCC, but could apply under a bakery MCC.** CBA Board Decision 27-N (9 Feb 2026) caps POS fees at **0.5% for ArCa cards and 0.9% for Visa/Mastercard**. The cap only covers merchants with prior-year turnover up to AMD 150m whose MCC appears on an annexed list [S24]. **The list contains retail MCCs but no restaurant or fast-food codes (5811–5814)** (VERIFIED by reading Appendix 1).
   - *Fact-check correction: the original "probably does not apply" was too absolute. Appendix 1 does list MCC 5462 (Bakeries) and 5499 (Misc. food stores). Clause 7 extends the caps to newly created entities with a listed MCC, so a new company faces no prior-year turnover test in year 1. If the acquirer assigns 5462 to a coffee & bakery unit, the 0.5%/0.9% cap could apply in year 1, against the 1.35% modelled below. Treat this as an upside to test with acquirers, not as settled. Under 5814 the cap does not apply.*
   - Published standard rates: FastBank 1.2% for cards from ArCa-member banks and 2.2% for foreign cards [S26]. Ameriabank sets POS rates case by case [S27]. Ameriabank online acquiring is 1.5% ArCa and 2.7% Visa/MC [S28].
   - **Model a blended 1.3–1.6% card cost.** ESTIMATE: 85% local cards at 1.2% plus 15% foreign at 2.2% = 1.35%. A tourist-heavy Sevan corridor pushes this up.
6. **Fiscal compliance is moving to electronic cash registers (e-HDM).** Law HO-309-N (adopted 3 Jul 2026) sets the e-HDM regime from **1 Jan 2027**. The Government defines the sectors where e-HDM is mandatory, and trading without one where it is required is fined **AMD 500,000** (VERIFIED in sibling C4 on arlis.am). An amendment to Government Decision 1257-N on e-receipt details also applies from 1 Jan 2027 [S32]. Every payment point (window, kiosk, app) needs its own registered HDM or e-HDM (C4). **Any POS chosen must integrate with the State Revenue Committee's (SRC) HDM/e-HDM interface.** Physical new-generation HDM devices sell for about AMD 60–125k (REPORTED) [S33].
   - *Fact-check correction: the earlier text treated the e-HDM mandate as a Tax Code draft (first reading May 2026, "adoption not verified"). C4 verified on arlis.am that HO-309-N is adopted law that sets the e-HDM regime from 1 Jan 2027. Only the list of sectors is still to be set by Government decision.*
7. **Coffee cost is the largest unverified COGS input.** No Armenian roaster publishes a wholesale price list. Retail benchmarks in Yerevan:
   - Imported or mass-market 1 kg bean bags: **AMD 8,910–21,380** (Lavazza Crema e Gusto 16,450; Ararat Oro 12,090; Melitta 14,790 regular, 11,090 on a 25% promotion; Tonino Lamborghini Espresso 21,380) [S36]. *Fact-check correction: the range was given as 8,900–20,300, with Melitta at its promotional price.*
   - Local specialty single-origin retail: **AMD 22,000–23,600/kg** [S37].
   - Model input: **AMD 12,000/kg for a wholesale espresso blend** (ASSUMPTION; range 9,000–16,000).
   - Roasted-coffee imports pay **8% duty (minimum €0.16/kg)**, while green arabica pays 0% [S6]. That structurally favours buying from a local roaster or roasting in-house.
8. **Dairy and packaging are well documented locally.**
   - Marianna 3.2% milk retails at **AMD 610 per 950 ml (≈642/L) and AMD 790 per 1 L UHT** [S40]. Alpro Barista Oat is **AMD 1,410/L** (promo 1,140) [S40].
   - Local manufacturer Oval Pack lists hot paper cups at **AMD 13–16 each**, double-wall 400 ml at **32**, lids at **5–11** and clear PET cold cups at **20–25** [S43].
   - Packaging comes to about **AMD 35–42 per milk or cold drink (19 for an espresso; mix average ≈AMD 38), ~8% of beverage COGS** (ESTIMATE).
9. **Recipe-level COGS (ESTIMATE, base inputs).** Percentages below are COGS (VAT-inclusive input prices) divided by the VAT-inclusive menu price. That is the correct ratio whether the company pays VAT and recovers input VAT, or pays turnover tax on gross receipts:
   - Espresso 13%, americano 21%, cappuccino 28%, latte 29%, iced latte 22%, cold brew 17%, signature flavoured latte 34%, hot chocolate 38%, lemonade 26%.
   - Croissant 39%, full breakfast wrap 48% (35% for a cost-engineered version), bought-in gata 49%.
   - **Blended beverage COGS ≈ 27% of revenue (26.6%).**
   - **Total blended ≈ 29.5% of revenue at a 75/25 beverage/food revenue mix, and ≈31% at the 60/40 mix that siblings C6/A4 recommend.** Food is margin-dilutive.
   - *Fact-check correction (method error): this section stated beverage ≈32% and total ≈35% "of net revenue", and told a VAT payer to use the net figure. Ingredient and packaging inputs are VAT-inclusive retail or wholesale prices (SAS, Yerevan City, Oval Pack). A VAT payer recovers that input VAT, so ex-VAT COGS ÷ ex-VAT price equals the gross ratio. The "net" column divided VAT-inclusive costs by VAT-exclusive prices and overstated COGS by about 6 pp. Under the catering turnover-tax regime that C4 recommends (no output VAT; TT ≈5–6.5% of receipts, modelled separately), the relevant figure is likewise ≈29.5% of receipts. The ≈35% figure applies only if output VAT is paid and no input VAT is recoverable.*
   - *Fact-check correction (mix): the 75/25 split conflicts with C6 and A4, which plan an Armenian coffee & food unit at 55–70% beverage / 30–45% food, and C6 sets blended COGS at 31–36%. At 60/40 the unit COGS above give ≈31.3% of revenue. Align the base mix with C6/A4, or state why food would be only 25%.*
10. **Yerevan price ceiling (REPORTED, partly stale listings).**
    - Espresso ≈ AMD 950; cappuccino 1,000–1,600; latte 1,000–1,900; iced latte ≈ 2,100; croissant 750–900.
    - Market leader **Coffee House (57 branches claimed, including outside Armenia; 52 listed per A2)** [S47] prices lattes around **AMD 1,000–1,400**. Specialty cafés (FEIN, Surf Coffee) charge **1,500–2,200**.
    - **Coffee House already runs a drive-thru on the M4 itself (Ptghni/Balahovit)**, with cappuccino/latte at about AMD 1,000 and iced latte at 1,000 on Glovo (Oct 2026) (A2).
    - A premium drive-thru priced at AMD 1,600–2,100 for milk drinks sits at the top of the market. The target latte (1,700) and iced latte (2,000) are about 70–100% above the incumbent drive-thru on the same corridor. The concept must justify that premium with speed, quality and food, not just "American style".
    - *Fact-check correction: the original omitted Coffee House's existing M4 drive-thru (documented in A2) and cited "57 branches" without qualification. The site says 57 "throughout Armenia and beyond" in one place and 56 in another; A2 counts 52 listed branches.*
11. **M4 supply logistics are workable but add cost and stock-out risk (ASSUMPTION).**
    - Milk needs delivery 3–7 times a week.
    - A frozen bake-off pastry model (weekly delivery) is more robust than daily fresh pastry for a site outside Yerevan.
    - No Armenian importer of frozen butter viennoiserie was identified. Russian (EAEU, duty-free) frozen croissants list at **RUB 23–60 each (≈AMD 100–255)** ex-works [S45].

---

## 2. Key data table

| Metric | Value | Period | Status | Source |
|---|---|---|---|---|
| USD/AMD official rate | 361.93 | 2026-10-09 | VERIFIED | [S1] CBA API |
| EUR/AMD; RUB/AMD | 405.58; 4.2677 | 2026-10-09 | VERIFIED | [S1] |
| USD/AMD two years earlier | 387.29 (AMD ≈7.0% stronger since: 387.29/361.93 − 1; the AMD price of a dollar fell 6.5%) | 30 Sep 2024 | VERIFIED | [S50] CBA API. *Fact-check correction: upgraded from a CEIC snippet (REPORTED) to the CBA official rate; "6.5% stronger" corrected to ≈7.0% appreciation* |
| EAEU duty: commercial coffee machines (8419 81 200 0) | 0% | 2026 | REPORTED | [S6][S7] |
| EAEU duty: other commercial food-heating equipment (8419 81 800 0) | 0% | 2026 | REPORTED | [S6] |
| EAEU duty: ice makers/other refrigeration (8418 69 000 8) | 10% | 2026 | REPORTED | [S6] |
| EAEU duty: refrigerated display counters (8418 50 190 0) | 10% | 2026 | REPORTED | [S6] |
| EAEU duty: microwave ovens (8516 50 000 0) | 10% | 2026 | REPORTED | [S6] |
| EAEU duty: commercial dishwashers (8422 19 000 0) | 0% | 2026 | REPORTED | [S6] |
| EAEU duty: water filtration (8421 21 000 9) | 0% | 2026 | REPORTED | [S6] |
| EAEU duty: blenders/mixers, domestic type (8509 40) | 5% | 2026 | REPORTED | [S6] |
| EAEU duty: roasted arabica (0901 21 000 1) vs green arabica (0901 11 000 1) | 8% (min €0.16/kg) vs 0% | 2026 | REPORTED | [S6] |
| EAEU duty: paper cups (4823 69 900 0); plastic lids (3923 50); syrups (2106 90 980 8); frozen bakery (1905 90 900 0) | 10%; 6.5%; 12%; 10% (min €0.09/kg) | 2026 | REPORTED | [S6] |
| Armenia VAT (standard and import) | 20%; EAEU-origin goods duty-free, VAT self-assessed by the 20th of the following month | reviewed 30 Jun 2026 | REPORTED | [S8] PwC |
| La Marzocco Linea PB AV 2-group | USD 19,710–25,690 (US; 25,690 = AV with scales); GBP 11,748 ex-VAT (UK) ≈ USD 15,537 | undated listings, accessed Oct 2026 | REPORTED | [S9][S10]. *Fact-check correction: the S9 Coffee Machine Depot URL for USD 19,710 now returns 404; EspressoParts shows USD 25,690. The GBP price is from UK retailer sitegems.etailsystems.com, not the AU/CA URLs cited earlier* |
| Victoria Arduino Eagle One 2-group | USD 18,450–22,550 (US) | undated, accessed Oct 2026 | REPORTED | [S11] |
| Nuova Simonelli Aurelia Wave 2-group volumetric | USD 12,015–12,700 (US) | undated | REPORTED | [S12] |
| Nuova Simonelli Appia Life 2-group V | USD 8,505–9,450 (US list: KaTom/Voltage 8,505; Majesty/Voltage 8,990; Black Rabbit 9,450) ≈ AMD 3.08–3.42m | accessed 10 Oct 2026 | REPORTED | [S13b]. *Fact-check correction: was UAH 150,800 ≈ USD 3,358 (Kyiv retail) [S13]. That price is stale: the same page shows USD 5,291.23, implying ≈28.5 UAH/USD against ≈44.9 today. It also includes 20% Ukrainian VAT. Replace it with an EU/dealer quote* |
| Eversys Cameo C'2 / Enigma E'4 | USD 19,350–23,470 / 32,000–46,615 (US) | undated | REPORTED | [S14] |
| Franke A600 / A800 | USD 14,032 / 13,052–13,889 (US) | undated | REPORTED | [S15] |
| Mahlkönig E80 Supreme (E80T) | USD 3,049–3,199 (US); RUB 322–368k (RU, incl. 22% Russian VAT; ≈USD 3,113–3,560 ex-RU-VAT) | 10 Oct 2026 (US) | REPORTED | [S16][S17]. *Fact-check correction: US price was USD 2,609–2,899 (stale)* |
| Mahlkönig EK43 | RUB 362,425–366,240 incl. 22% Russian VAT ≈ USD 4,274–4,319; ex-RU-VAT ≈ USD 3,503–3,540 (RU) | undated | REPORTED | [S17]. *Fact-check correction: RU retail includes Russian VAT, and EAEU exports are zero-rated, so landing it with Armenian VAT on top double-counted VAT (≈USD 1,000 overstatement). The EK43 page itself could not be re-opened (connection reset)* |
| Merrychef eikon e2s | USD 10,305 (US; item flagged "View Replacement Item"); GBP 5,353 ex-VAT (UK, unverified) | 10 Oct 2026 | REPORTED | [S18]. *Fact-check correction: USD 9,918 was the price of the suggested replacement, the Merrychef conneX 12, not the e2s* |
| TurboChef Sota single mag / Bullet | USD 13,430 (US; after the 3% increase of 1 Aug 2026) / GBP 9,888 ex-VAT (UK) | 10 Oct 2026 | REPORTED | [S19]. *Fact-check correction: was USD 13,039, the pre-increase price* |
| Hoshizaki cuber with bin (US models) | USD 4,200–6,360 | undated | REPORTED | [S20] |
| Vitamix The Quiet One | USD 1,492.95 (vitamix.com) | accessed Oct 2026 | REPORTED | [S21] |
| Bunn ICB Twin batch brewer | USD 1,915–2,830 | undated | REPORTED | [S22] |
| Landed-cost multiplier (0% duty / 10% duty) | ≈1.30× / ≈1.43× foreign ex-VAT price | — | ESTIMATE (1.08 × (1+d) × 1.20) | — |
| Core equipment package, landed (lean / mid / flagship) | USD 45–52k / 78–89k / 168–181k (AMD 16.4–18.8m / 28.1–32.1m / 60.7–65.7m) | Oct 2026 prices | ESTIMATE + ASSUMPTION | §3.1.6. *Fact-check correction: was USD 38–43k / 77–88k / 167–180k; lean understated by ≈20% (Appia Life price)* |
| CBA POS fee cap (ArCa / Visa-MC) | 0.5% / 0.9%; only listed MCCs with prior-year turnover ≤ AMD 150m, or newly created entities with a listed MCC (clause 7); restaurant MCCs (5811–5814) not listed, but bakery 5462 and misc. food 5499 are | effective from 1 Mar each year; decision 9 Feb 2026 | VERIFIED | [S24]. *Fact-check correction: the cap could apply in year 1 if the acquirer assigns MCC 5462* |
| FastBank POS standard rate | 1.2% (ArCa-member banks' cards), 2.2% (foreign/non-member cards); AMD 8,000/month if turnover target unmet (from 10 Sep 2026) | page updated 27 Apr 2026 | VERIFIED | [S26] |
| Ameriabank POS | Rates case by case; minimum monthly fee AMD 4,600 (Yerevan); AMD 50,000 fee if terminated within 1 year | effective 3 Apr 2026 | VERIFIED | [S27] |
| Ameriabank internet acquiring | 1.5% ArCa; 2.7% Visa/MC (VAT incl.); Apple Pay supported | effective 27 Apr 2026 | VERIFIED | [S28] |
| Idram QR network | >22,000 points of sale; merchant fee not published | 2024–2025 | REPORTED | [S31] |
| Apple Pay in Armenia | Live since 18 Jan 2022 (Acba, Ardshinbank, Ameriabank, Converse, Inecobank, Unibank) | 2022 | REPORTED | [S30] |
| e-HDM legal change | Law HO-309-N (adopted 3 Jul 2026) sets the e-HDM regime from 1 Jan 2027; Government defines mandatory sectors; AMD 500,000 fine for trading without e-HDM where required; Decision 1257-N amendment from 1 Jan 2027 | 2026 | REPORTED [S32]; VERIFIED in C4 (arlis.am) | [S32]; C4. *Fact-check correction: no longer "draft"; aligned with C4* |
| New-generation HDM device price | ≈AMD 60k–125k (e.g., Newland N950 AMD 85–95k) | undated listings | REPORTED (snippets) | [S33] |
| Poster POS | USD 26 / 44 / 62 per month (Mini/Business/Pro, annual billing); +USD 19 per extra register | accessed Oct 2026 | REPORTED | [S34] |
| iiko POS (RU tariffs) | From RUB 1,295 / 4,000 / 7,400 / 9,200 per month (≈AMD 5.5k / 17.1k / 31.6k / 39.3k) | undated | REPORTED | [S35] |
| Imported/mass-market 1 kg coffee beans, Yerevan retail | AMD 8,910–20,280 (Lavazza Crema e Gusto 16,450) | accessed 10 Oct 2026 | REPORTED | [S36] |
| Local specialty roaster, 1 kg retail (Caffeine, Dilijan) | AMD 22,000–23,600 | accessed 10 Oct 2026 | REPORTED | [S37] |
| Wholesale espresso blend (model input) | AMD 12,000/kg (range 9,000–16,000) | — | ASSUMPTION | §3.3.1 |
| Marianna milk 3.2% | AMD 610 / 950 ml; 790 / 1 L UHT | accessed 10 Oct 2026 | REPORTED | [S40] |
| Alpro Barista Oat 1 L | AMD 1,410 (promo 1,140, 1–14 Oct 2026) | Oct 2026 | REPORTED | [S40] |
| Monin syrup 0.7 L, Yerevan retail | AMD 4,900–5,880 | undated, accessed Oct 2026 | REPORTED | [S41] |
| Paper hot cup 300/400 ml (Oval Pack) | AMD 13 / 15–16 each (case of 600–700) | accessed 10 Oct 2026 | REPORTED | [S43] |
| Double-wall 400 ml cup; lids 82–95 mm | AMD 32; AMD 5–11 | accessed 10 Oct 2026 | REPORTED | [S43] |
| Clear PET cold cup 500 ml; clear lid 95 mm | AMD 20–25; AMD 8–10 | accessed 10 Oct 2026 | REPORTED | [S43] |
| Frozen butter croissant (Russian producers, ex-works) | RUB 23–60 (≈AMD 100–255) per 65–80 g piece | undated | REPORTED | [S45] |
| Yerevan menu prices: cappuccino / latte / iced latte / croissant | AMD 1,000–1,600 / 1,000–1,900 / ~2,100 / 750–900 | 2025–2026 (some stale) | REPORTED | [S46] |
| Blended beverage COGS | ≈32% of net-of-VAT price (≈27% of VAT-inclusive) | Oct 2026 inputs | ESTIMATE | §3.4 |
| Total blended COGS (75/25 bev/food) | ≈35% of net revenue | Oct 2026 inputs | ESTIMATE | §3.4 |

---

## 3. Detailed findings & analysis

### 3.1 Equipment

#### 3.1.1 Who sells and services professional equipment in Yerevan

| Company | What was found | Brands (as stated or linked) | Service claim | Status |
|---|---|---|---|---|
| **The Horeca LLC**, 88 Anastas Mikoyan St., office 29, Yerevan; +374 60 87 87 87; founded 2015 | Turnkey kitchen/bar projects (AfroLab roastery, Coffee House, Baguette & Co, Kong, Black Star Burger, Alexander Hotel); "700+ completed projects" | **Authorised Mahlkönig dealer since 2019** [S3]. The homepage "Our Brands" section links La Marzocco, Victoria Arduino, Nuova Simonelli (Appia Life), Franke, Hoshizaki, Bravilor, Santos, Hamilton Beach, Rational, Electrolux Professional, Fimar, Robot Coupe, Probat, Carpigiani, Irinox, Moretti/Alfa Forni and others [S2] | "Huge spare part stock", online spare-part ordering, warranty and post-warranty service, professional technicians, separate tech-support and spare-parts lines [S2] | VERIFIED (dealer page) / REPORTED (company claims) |
| **DR HORECA LLC** (Davtashen) | Equipment supplier to restaurants, hotels and cafés | FIMAR, Bartscher, Rational, Fagor, Paderno, Electrolux, Gaber (official/exclusive per directory) | Not stated | REPORTED (Spyur search snippet; page blocked) [S4] |
| **Arahet Development** | Directory lists it as a B2B coffee company: professional coffee equipment, capsule machines, vending, coffee-machine spares, espresso-machine rental | Not stated | Spare parts listed | REPORTED (snippet) [S5] |
| **Art Global LLC** | Directory: coffee-machine installation, paper cups for hot drinks, plastic cup lids | Not stated | Installation | REPORTED (snippet) [S5] |
| Eversys, WMF, Schaerer, Merrychef, TurboChef | **No Armenian distributor or service partner found** in English/Russian/Armenian searches | — | — | Gap: ask each manufacturer for the territory partner (likely Georgia, Russia or UAE) |

**Assessment.** Choosing La Marzocco, Victoria Arduino, Nuova Simonelli, Mahlkönig, Franke, Hoshizaki or Bravilor gives a local warranty and spares route through The Horeca. Choosing Eversys, WMF or Schaerer super-automatics, or Merrychef/TurboChef speed ovens, means either a cross-border service contract or training an in-house technician plus a critical-spares kit. That should be costed. ASSUMPTION: 3–5% of equipment value per year for service and spares, plus a spares kit at 5–8% of equipment value at opening.

#### 3.1.2 Import regime (EAEU)

| HS code (EAEU CN FEA) | Description | CET duty | Source |
|---|---|---|---|
| 8419 81 200 0 | Coffee makers and other appliances for hot drinks (industrial/commercial) | **0%** | [S6][S7] |
| 8516 71 000 0 | Electro-thermic coffee/tea makers (domestic type) | 8.5% | [S6] |
| 8419 81 800 0 | Other equipment for cooking/heating food (commercial) | **0%** | [S6] |
| 8516 50 000 0 | Microwave ovens | **10%** | [S6] |
| 8418 69 000 8 | Other refrigerating equipment (incl. ice makers) | **10%** | [S6] |
| 8418 50 190 0 | Refrigerated display counters, other | 10% | [S6] |
| 8422 19 000 0 | Dishwashing machines, non-household | **0%** | [S6] |
| 8421 21 000 9 | Water filtering/purifying equipment | **0%** | [S6] |
| 8509 40 000 0 | Food grinders/mixers/juicers (domestic type) | 5% | [S6] |
| 8471 30 / 8517 62 | Tablets/computers; network equipment | 0% | [S6] |

Notes:
- **Goods of EAEU origin (e.g., Russian or Belarusian) are duty-free.** Customs does not collect VAT on them. The importer self-assesses VAT by the 20th of the following month [S8].
- **Import VAT 20%** [S8]. ASSUMPTION (standard EAEU practice, confirm with a broker): the import VAT base is customs value plus duty.
- The duty rates above are shown on alta.ru, a Russian commercial tariff database that replicates the EAEU CET. The 22% VAT shown there is the Russian rate and does not apply to Armenia.
- **Speed-oven classification risk.** Merrychef and TurboChef combine microwave and convection/impingement heating. Customs could classify them as 8516 50 (10%) or 8419 81 800 0 (0%). Recommendation: request a preliminary classification decision from the SRC before ordering.
- Whether Armenia retains any national exemptions from the CET for these lines was not verified (gap).

**Landed-cost formula (ESTIMATE).** Landed AMD = foreign ex-VAT price × FX × 1.08 (freight and insurance, ASSUMPTION for EU groupage by road) × (1 + duty) × 1.20 (import VAT). The result is ≈1.296× at 0% duty, ≈1.361× at 5% and ≈1.426× at 10%. Customs-broker fees, dealer margin, installation and commissioning come on top. If the operating company is VAT-registered, the 20% is recoverable and the economic cost falls to ≈1.08–1.19×.

#### 3.1.3 Espresso machines and super-automatics: list-price benchmarks

All prices are published retail or list prices from foreign dealers (REPORTED). US units are 60 Hz and must be ordered in EU/INT spec. "Landed" applies the formula above (0% duty).

| Model | Published price | AMD equiv. | Landed AMD (ESTIMATE) | Fit for drive-thru (ASSUMPTION) |
|---|---|---|---|---|
| Nuova Simonelli Appia Compact 2gr S | UAH 95,875 (Kyiv) [S13] | 772,676 | ~1.00m | Budget only. Lower thermal stability and throughput |
| Nuova Simonelli Appia Life 2gr V | UAH 150,800 (Kyiv) [S13] | 1,215,327 | ~1.58m | Lean option. Reliable workhorse with a local dealer |
| Nuova Simonelli Aurelia Wave 2gr volumetric | USD 12,015–12,700 (US) [S12] | 4.35–4.60m | 5.64–5.96m | Mid option, ergonomic, high-volume |
| La Marzocco Linea PB AV 2gr | USD 19,710 (US) [S9]; GBP 11,748 ex-VAT (UK) [S10] | 5.62–7.13m | 7.29–9.25m | Mid/flagship. Strong resale value. Dutch Bros is *reported* by a consumer blog to use La Marzocco [S23] (weak source) |
| Victoria Arduino Eagle One 2gr | USD 18,450–22,550 (US) [S11] | 6.68–8.16m | 8.65–10.58m | Mid/flagship, energy-efficient |
| Franke A600 / A800 (super-auto) | USD 14,032 / 13,052–13,889 (US) [S15]; UK GBP 9,999.99 / 12,999.99 incl. VAT | 4.72–5.08m | 6.12–6.58m | Consistency with low-skill staff. Local link via The Horeca |
| Eversys Cameo C'2 (super-auto) | USD 19,350–23,470 (US) [S14] | 7.00–8.49m | 9.08–11.01m | High consistency. **No local service found** |
| Eversys Enigma E'4 (super-auto, high-volume) | USD 32,000–46,615 (US) [S14] | 11.58–16.87m | 15.0–21.9m | Flagship throughput. **No local service found** |

Prices for La Marzocco KB90 and Victoria Arduino Black Eagle (Maverick), WMF 5000 S+ and Schaerer Coffee Soul/Skye were not obtained (gap).

**Throughput logic (ASSUMPTION, industry rule of thumb, not verified).** A 2-group traditional machine with two baristas typically sustains about 60–90 milk drinks per hour at peak. Above about 100 drinks per hour (a dual-lane flagship), either a 3-group machine, two machines, or a super-automatic with dual steam/milk systems is needed. Validate against the demand model from workstream B.

#### 3.1.4 Grinders, brewers, ovens, ice, blenders: list-price benchmarks

| Item | Published price | Duty | Landed AMD (ESTIMATE) | Notes |
|---|---|---|---|---|
| Mahlkönig E80 Supreme (now E80T) | USD 2,609–2,899 (US) [S16]; RUB 322,050–368,350 (RU) [S17] | 0% (ASSUMPTION: 8509/8438 classification to confirm) | 1.22–1.36m (US basis); 1.78–2.04m (RU basis) | Workhorse for high-volume espresso. Local authorised dealer |
| Mahlkönig EK43 | RUB 362,425–366,240 (RU) [S17] | as above | ~2.0m | Batch brew, cold brew and retail grinding |
| Mahlkönig E65S GbW | RUB 255,000–320,150 (RU) [S17] | as above | ~1.41–1.77m | Alternative to the E80 |
| Bunn ICB Twin / ICB TF Twin | USD 1,915–2,830 (US) [S22] | 0% | 0.90–1.33m | Check 50 Hz availability. Bravilor (Dutch, linked by The Horeca) is the likely local alternative; price not obtained |
| Merrychef eikon e2s | USD 9,918 (US) [S18]; GBP 5,353 ex-VAT (UK) [S18] | 0% or 10% (classification risk) | 3.32–4.65m (0%); 3.65–5.12m (10%) | **No local service partner found** |
| TurboChef Sota single mag / Bullet | USD 13,039 (US) / GBP 9,888 ex-VAT (UK) [S19] | 0% or 10% | ~6.1m (0%); ~6.7m (10%) | Webstaurant shows a 3% manufacturer increase from 1 Aug 2026 |
| Hoshizaki cubers with bin (US KM series) | USD 4,200–6,360 [S20] | 10% | 2.17–3.28m | US units are 115 V/60 Hz. Use EU models (e.g., IM series via The Horeca); EU price not obtained |
| Vitamix The Quiet One | USD 1,492.95 [S21] | 5% | ~0.74m | — |
| Blendtec Stealth 885 | AUD 2,495 incl. GST (AU) [S21] | 5% | ~0.86m | — |
| Cold-brew system (Toddy commercial or immersion bags) | Not obtained | — | ASSUMPTION USD 300–1,500 | Gap |
| Undercounter refrigeration, freezer, reach-in | Not obtained | 10% | ASSUMPTION (see packages) | Gap |
| Undercounter dishwasher/glasswasher | Not obtained | 0% | ASSUMPTION | Gap |
| Water filtration/softening/RO (BWT, Everpure etc.) | Not obtained | 0% | ASSUMPTION | Important: hard water causes scale damage to espresso boilers. Get a water analysis for the site (Veolia Jur or a well) |

**Sanity check on sourcing route.** Russian retail prices for Mahlkönig grinders are about 30–50% above US retail once converted (E80 Supreme ≈ USD 3,800–4,340 vs USD 2,600–2,900). Buying through Russia is not cheaper than EU-direct despite the EAEU duty-free status. The price advantage of an EU-direct order (via The Horeca or direct import) should be tested with quotes.

#### 3.1.5 Utilities and installation implications (ASSUMPTION, confirm with workstream on utilities and with ENA)

High-output 2–3 group espresso machines, speed ovens and ice machines typically need **3-phase 400 V** supply. ASSUMPTION: total connected load for a mid-range bar plus kitchen is roughly 25–45 kW. Specify a water supply with filtration and a floor drain. Ice machines also need ventilation clearance. These drive the electricity connection request to ENA.

#### 3.1.6 Equipment package estimates (core bar and kitchen equipment only)

Landed, excluding installation, building, HVAC, POS/tech, signage, furniture and vehicles. Formula as in 3.1.2. Line items marked ESTIMATE use the published prices above. ASSUMPTION lines are analyst ranges with no Armenian or foreign price verified.

**Lean** (single lane, container/kiosk, about 250–350 drinks a day: ASSUMPTION)

| Item | Status | USD | AMD m |
|---|---|---|---|
| Espresso: NS Appia Life 2gr V (UA retail reference) | ESTIMATE | 4,352 | 1.58 |
| Grinders: 2 × Mahlkönig E80 Supreme (USD 2,750 avg, US reference) | ESTIMATE | 7,128 | 2.58 |
| Ice machine with bin (US reference low, 10% duty) | ESTIMATE | 5,988 | 2.17 |
| Speed oven: Merrychef e2s (UK ex-VAT reference) | ESTIMATE | 9,174 | 3.32 |
| Blender: Vitamix Quiet One | ESTIMATE | 2,032 | 0.74 |
| Refrigeration (2 undercounter + 1 freezer) | ASSUMPTION | 4,000–6,000 | 1.45–2.17 |
| Warewashing (3-sink + undercounter glasswasher) | ASSUMPTION | 2,500–4,000 | 0.90–1.45 |
| Water filtration/softening | ASSUMPTION | 800–1,500 | 0.29–0.54 |
| Cold-brew kit | ASSUMPTION | 300–800 | 0.11–0.29 |
| Smallwares (pitchers, scales, tampers, knock boxes) | ASSUMPTION | 1,500–2,500 | 0.54–0.90 |
| **Total** | | **37,800–43,500** | **13.7–15.7** |

**Mid-range** (single lane with high-throughput bar, about 400–600 drinks a day: ASSUMPTION)

| Item | Status | USD | AMD m |
|---|---|---|---|
| Espresso: La Marzocco Linea PB AV 2gr (UK reference) | ESTIMATE | 20,136 | 7.29 |
| Grinders: 2 × E80 Supreme + 1 × EK43 (RU reference) | ESTIMATE | 12,667 | 4.58 |
| Batch brewer: Bunn ICB TF Twin | ESTIMATE | 3,668 | 1.33 |
| Ice machine with bin (US reference high, 10% duty) | ESTIMATE | 9,067 | 3.28 |
| Speed oven: Merrychef e2s (US reference) | ESTIMATE | 12,854 | 4.65 |
| Blenders: 2 × Vitamix Quiet One | ESTIMATE | 4,063 | 1.47 |
| Refrigeration | ASSUMPTION | 6,000–10,000 | 2.17–3.62 |
| Warewashing | ASSUMPTION | 4,000–7,000 | 1.45–2.53 |
| Water treatment | ASSUMPTION | 1,500–3,000 | 0.54–1.09 |
| Cold-brew system | ASSUMPTION | 800–1,500 | 0.29–0.54 |
| Smallwares | ASSUMPTION | 2,500–4,000 | 0.90–1.45 |
| **Total** | | **77,300–88,000** | **28.0–31.8** |

**Flagship** (dual lane, >120 drinks/hour peak: ASSUMPTION)

| Item | Status | USD | AMD m |
|---|---|---|---|
| Super-automatic: Eversys Enigma E'4 (US reference mid, USD 40k) | ESTIMATE | 51,840 | 18.76 |
| Traditional machine for backup and signature drinks: LM Linea PB 2gr | ESTIMATE | 20,136 | 7.29 |
| Grinders: 2 × E80 Supreme + EK43 | ESTIMATE | 12,667 | 4.58 |
| Batch brewer | ESTIMATE | 3,668 | 1.33 |
| Ice machines: 2 × with bin (10% duty) | ESTIMATE | 18,134 | 6.56 |
| Speed ovens: TurboChef Sota + Merrychef e2s | ESTIMATE | 29,752 | 10.77 |
| Blenders: 3 × Vitamix | ESTIMATE | 6,095 | 2.21 |
| Refrigeration (dual-lane line) | ASSUMPTION | 10,000–15,000 | 3.62–5.43 |
| Warewashing | ASSUMPTION | 6,000–9,000 | 2.17–3.26 |
| Water treatment (2 lines) | ASSUMPTION | 3,000–5,000 | 1.09–1.81 |
| Cold-brew/nitro | ASSUMPTION | 1,500–3,000 | 0.54–1.09 |
| Smallwares | ASSUMPTION | 4,000–6,000 | 1.45–2.17 |
| **Total** | | **166,800–180,300** | **60.4–65.3** |

About one-sixth of each total is import VAT (lean ≈ USD 6.3–7.2k, mid ≈ 12.9–14.7k, flagship ≈ 27.8–30.0k). It is recoverable only by a VAT payer. Add installation and commissioning (ASSUMPTION 5–10%), a critical-spares kit (5–8%) and, if no local service exists, a service contract.

### 3.2 Technology

#### 3.2.1 Fiscal compliance (HDM / e-HDM)

- Armenia requires sales to be fiscalised through cash registers (HDMs). Law **HO-309-N of 3 July 2026** extends the HDM receipt rules to **electronic HDMs**. A draft amendment to Government Decision 1257-N would apply from **1 January 2027**: the e-receipt number must appear on related tax invoices and invoice-receipts, and adjustments must propagate (REPORTED, iravaban.net, 26 Aug 2026) [S32].
- On 20 May 2026 a Tax Code draft passed the parliamentary economic committee in first reading. It would make the e-HDM an alternative to a physical HDM and make its use mandatory for organisations and individual entrepreneurs in cases and deadlines to be specified (REPORTED, ARKA) [S32b]. Final adoption status was not verified.
- An SRC API exists. Third-party developer tools show this: a PHP package for the Armenian e-HDM API (updated Dec 2025) and a WooCommerce plugin that issues receipts "through the tax service API" (REPORTED) [S32c].
- **Implication.** The POS must either drive a certified new-generation HDM device or issue e-HDM receipts through the SRC interface. Confirm that the chosen POS vendor has a working Armenian fiscal integration. Neither Poster's pricing page nor the iiko tariff page mentions Armenia [S34][S35].
- **Hardware.** New-generation HDM devices with an integrated card terminal (e.g., Newland N950, Android) sell for about **AMD 85,000–95,000 new**. Listings range from AMD 30,000 (used) to 125,000 (REPORTED, snippets; listings not opened) [S33]. In 2019 the SRC set the regulated sale price at AMD 60,000, with AMD 160,000 kept for some categories (REPORTED, 2019) [S33]. Banks can enable card acceptance directly on a new-generation HDM: FastBank says so explicitly [S26], and Ameriabank prices "POS service via the merchant's cash register" [S27].

#### 3.2.2 POS / restaurant software

| System | Published price | Armenian presence and fiscal integration | Status |
|---|---|---|---|
| Poster (joinposter.com) | Mini USD 26, Business USD 44 (includes KDS, modifiers, promotions, delivery), Pro USD 62 per month (annual billing; monthly billing about 10% higher); +USD 19 per extra register; Poster Site (ordering website) USD 19/month; QR USD 7/month; loyalty included | Pricing page does not mention Armenia or fiscalisation [S34] | REPORTED |
| iiko | From RUB 1,295 (Mini) / 4,000 (Start) / 7,400 (Pro, open API) / 9,200 (Enterprise) per month ≈ AMD 5.5k / 17.1k / 31.6k / 39.3k [S35] | Russian dealer price list. Armenian partner and HDM integration **not verified** (search budget exhausted) | REPORTED (RU) |
| R-Keeper | Not obtained | Not verified | Gap |
| Local Armenian POS | Not obtained | Not verified | Gap |

ASSUMPTION for modelling: software at USD 50–150 per month per site plus USD 800–1,500 hardware per order station (tablet or terminal, printer, cash drawer) and a KDS screen per production line. Replace with quotes.

#### 3.2.3 Drive-thru specific technology (gaps; no prices verified)

- **Headset systems (HME EOS HD / NEXEO, 3M/Clear-Com).** No Armenian dealer or price was found before the search budget ran out. Radio-frequency approval of imported wireless headsets in Armenia should also be checked. ASSUMPTION placeholder: USD 4,000–8,000 per lane.
- **Order-confirmation board and outdoor digital menu boards** (high-brightness, 2,500+ nit, weatherproof). Not priced. ASSUMPTION placeholder: USD 5,000–20,000 per lane, depending on the number of screens and the content management system.
- **Mobile ordering and loyalty.** POS-native options are the cheapest route: Poster Site at USD 19/month with loyalty included [S34]; iiko loyalty in Start/Pro tiers [S35]. A custom white-label app was not priced. ASSUMPTION: USD 15,000–60,000 build plus 15–20% a year maintenance. Get quotes from Armenian studios.
- **Online payments for the app.** Ameriabank internet acquiring charges **1.5% (ArCa) and 2.7% (Visa/Mastercard), VAT included**, and supports Apple Pay in-app (effective 27 Apr 2026) (VERIFIED) [S28].

#### 3.2.4 Card acquiring and wallet payments

| Item | Finding | Status |
|---|---|---|
| CBA fee cap (Decision 27-N, 9 Feb 2026) | Maximum 0.5% (ArCa) and 0.9% (two largest international schemes). Monthly maximum AMD 4,600 (Yerevan) / 3,000 (regional towns) / 1,000 (villages) when monthly POS turnover is ≤ AMD 50,000. Interchange capped at 0.2%. **Applies only to merchants with annual turnover ≤ AMD 150m whose MCC is on Appendix 1.** Appendix 1 lists retail MCCs (4812, 5013–5999, 8043) but **no eating places or fast-food codes (5812/5814)** [S24]. ArmInfo commentary on the decision [S25] | VERIFIED |
| FastBank standard package | 1.2% for ArCa/Visa/MC from ArCa-member banks; 2.2% for international/non-member cards. AMD 4,600/month fee if POS turnover ≤ AMD 50,000. From 10 Sep 2026, AMD 8,000/month (terminal) or 5,000 (HDM-POS) if the turnover requirement is not met. Free installation within 3 business days. AMD 50,000 fee for termination within 1 year [S26] | VERIFIED (page updated 27 Apr 2026) |
| Ameriabank | POS rates case by case. AMD 5,000/month service fee if POS turnover < AMD 1m/month. Minimum monthly fee AMD 4,600 (Yerevan). AMD 50,000 activation fee clawback if terminated within 1 year [S27] | VERIFIED (effective 3 Apr 2026) |
| Evocabank | The 0.2% "via POS terminal" line on its tariff page is a **cardholder cash-withdrawal fee**, not a merchant rate. No merchant acquiring rates are published [S29] | VERIFIED |
| ACBA, Ardshinbank, Inecobank merchant rates | Not published or not found | Gap |
| Apple Pay | Live in Armenia since 18 Jan 2022 with six banks (Acba, Ardshinbank, Ameriabank, Converse, Inecobank, Unibank) [S30]. Works at any contactless terminal | REPORTED |
| Google Pay | Not verified in this pass | Gap |
| Idram QR | Unified QR infrastructure; QR codes at >22,000 points of sale; same-day settlement; Idram says it charges "the lowest possible commission", the same regardless of funding source. **Rate not published** [S31] | REPORTED |
| Telcell QR/wallet | Not researched (search budget) | Gap |

ESTIMATE for the model: blended card cost = 0.85 × 1.2% + 0.15 × 2.2% = **1.35% of card sales**. Use 1.3–1.6% as the range. A tourist-heavy Sevan corridor raises the foreign-card share in summer.

### 3.3 Supply chain

#### 3.3.1 Coffee

| Source | Product | Price | Status |
|---|---|---|---|
| Yerevan City (supermarket chain, online) [S36] | Lavazza Crema e Gusto Classico 1 kg | AMD 16,450 | REPORTED (retail, 10 Oct 2026) |
| | Lavazza Crema e Aroma 1 kg / Qualità Oro 1 kg | AMD 18,640 / 20,280 | REPORTED |
| | Mövenpick Caffè Crema/Espresso 1 kg | AMD 14,750 | REPORTED |
| | Melitta BellaCrema Espresso 1 kg | AMD 11,090 | REPORTED |
| | Ararat Oro (medium roast) 1 kg / Ararat Opera (dark) 1 kg | AMD 12,090 / 8,910 | REPORTED |
| | Italcaffè Excelso 1 kg | AMD 8,990 | REPORTED |
| Caffeine (specialty roastery, Dilijan) [S37] | Single origins (Ethiopia Yirgacheffe G2, Peru organic, Guatemala decaf), 1 kg | AMD 22,000–23,600 (250 g: 6,400–6,800) | REPORTED (Shopify catalogue, 10 Oct 2026) |
| jur.am (snippet) | Hayk Coffee N30, 1 kg beans | AMD 12,200 (special price) | REPORTED (snippet, undated) |
| Local roasters with wholesale offers | **AfroLab Roastery** (Pushkin St., "Order for your business", wholesale registration form; part of Collective Group) [S38]; **FEIN** (Coffee House group's roastery café); **Lumen Coffee** (Giesen roaster); **Nero Bean**; **Royal Armenia** (mass-market roaster) [S39] | **No wholesale price lists published** | Gap: request quotes |

**Model input (ASSUMPTION): AMD 12,000/kg** for a quality local-roasted espresso blend at wholesale. Range AMD 9,000 (commodity blend) to 16,000 (specialty-grade blend). Basis:
- Wholesale normally sits well below the roaster's own retail bag price (AMD 22–23.6k/kg for single origins).
- It should sit near or below supermarket prices for imported Italian blends (AMD 11–20k), which carry the 8% (minimum €0.16/kg) roasted-coffee duty plus 20% VAT.

Supply: a weekly delivery from Yerevan is sufficient. Roasted coffee keeps 2–6 weeks in valve bags.

#### 3.3.2 Dairy and plant milks

| Product | Retail price (SAS.am, 10 Oct 2026) [S40] | AMD per litre |
|---|---|---|
| Marianna 3.2%, 950 ml | 610 | 642 |
| Marianna 3.2% UHT, 1 L | 790 | 790 |
| Bonilat 3.2%, 900 ml | 680 | 756 |
| Chanakh 3.2%, 950 ml | 640 | 674 |
| Marila 2.5%, 0.95 L | 780 | 821 |
| Parmalat 3.5% UHT, 1 L | 1,650 (promo 1,290) | 1,650 |
| Yerevan City: Marianna 3.2% 750 ml / 1.5% lactose-free 750 ml [S36] | 900 / 930 | 1,200 / 1,240 (premium line) |
| Alpro Barista Oat, 1 L | 1,410 (promo 1,140, 1–14 Oct 2026) | 1,410 |
| Alpro almond / soy, 1 L | 1,670 / 1,440 | — |
| Président whipping cream 35%, 200 ml | 1,680 (promo 1,420) | 8,400 |

- **Model input (ESTIMATE):** whole milk at **AMD 700/L**, the midpoint of Marianna's 642–790 retail range. ASSUMPTION: a HoReCa discount (typically 5–15%) roughly offsets choosing a consistent barista-grade product. Sensitivity range AMD 600–850.
- Oat milk at AMD 1,300/L (ASSUMPTION; 8% below regular retail). Plant milk is usually charged as a +AMD 200–300 upcharge, which protects margin.
- Local dairies to approach for HoReCa contracts and delivery routes: Marianna (Ashtarak-Kat group), Dili, Yeremyan Products, Bonilat, Chanakh, Arzni.

#### 3.3.3 Syrups, sauces, powders

| Product | Price | Status |
|---|---|---|
| Monin syrups 0.7 L (TheHouse.am; SAS Grenadine 0.7 L; Noyantun Caramel 0.7 L) | AMD 4,900–5,880 per bottle ≈ 7,000–8,400/L. TheHouse lists Maple Spice 1 L at 5,600 | REPORTED [S41] |
| Monin importer | **Alpha Food Service CJSC**: importer/distributor since 2005, ~3,000 HoReCa/bakery/retail clients, ~100 brands; runs The House and The Bake House retail stores | REPORTED [S41] |
| Barinoff syrup 1 L (Russian, EAEU duty-free) | RUB 306–365/L in Russia ≈ AMD 1,300–1,560/L. Availability in Armenia not verified | REPORTED [S42] |
| Hot chocolate powder: Caffè Vergnano 1 kg / Elza 250–325 g | AMD 14,500/kg / ≈11,200–12,000/kg (retail) | REPORTED [S40] |
| Cocoa powder (various) | AMD 9,800–12,900/kg (retail) | REPORTED [S40] |
| Sugar 1 kg | AMD 410–480 (retail) | REPORTED [S40] |

Model inputs (ASSUMPTION):
- Monin at AMD 6,500/L (wholesale, about 10–20% below retail). Syrups from outside the EAEU carry 12% duty.
- Hot chocolate powder at AMD 12,000/kg.
- A move to an EAEU-origin syrup brand could cut syrup cost by about 50–70%. Quality and brand-fit risk would need testing.

#### 3.3.4 Packaging (local manufacturer list prices, Oval Pack / Ovalplast, Yerevan) [S43]

| Item | Pack price | Per unit (AMD) |
|---|---|---|
| Paper cup 100 ml (espresso), TB-1008, 60 mm | 18,900 / 2,700 | 7.0 |
| Paper cup 300 ml, TB-1005 / TB-1004, 80 mm | 9,100 / 700; 9,800 / 700 | 13.0; 14.0 |
| Paper cup 400 ml, TB-1002, 84 mm / TB-1000, 90 mm | 9,000 / 600; 10,400 / 650 | 15.0; 16.0 |
| Double-wall paper cup 250 ml, TB-1009 (standard / custom-printed, MOQ 5,000) | 9,200 / 400 | 23 / 27 |
| Double-wall paper cup 400 ml, TB-1001 | 8,320 / 260 | 32.0 |
| Paper cup 500 ml, TB-0001; paper cold cup 500 ml, TB-0010 | 10,800 / 600; 12,960 / 480 | 18.0; 27.0 |
| White lids 82 mm / 86 mm / 90 mm / 92 mm / 60 mm | 2,000–3,600 / 400; 4,000 / 400; 4,400 / 400; 2,400 / 400; 2,100 / 300 | 5–9; 10; 11; 6; 7 |
| Clear PET cup 500 ml (95 mm), BTP-1130 / BTP-1140; 380 ml | 4,000 / 200; 5,000 / 200; 3,800–4,800 / 200 | 20; 25; 19–24 |
| Clear lid 95 mm (flat/with hole) | 3,200–4,000 / 400 | 8–10 |
| Cup sleeve (250 × 52 mm), BB-0019 | 400 / 50 | 8 |
| 3-cup carrier, BB-0025 | 800 / 10 | 80 |

Cross-checks: Complex.am retails double-wall 400 ml cups at AMD 56–60 each in small packs. OfficePro sells 50 × 400 ml cups for AMD 1,950 (39 each) [S44]. Oval Pack's case prices are therefore the right wholesale benchmark. Whether Oval Pack's prices include VAT is not stated (gap). Straws, paper bags and napkins were not priced. ASSUMPTION: a straw is AMD 10, and paper bag or wrap is AMD 15–30.

**Packaging per drink (ESTIMATE).** Espresso cup + lid + stirrer = 19. Cappuccino 300 ml cup + lid + sleeve + misc = 35. 400 ml hot = 38. Cold cup + lid + straw = 41. For custom-printed branded cups, apply about +17% (Oval Pack's own printed-cup premium of 27 vs 23 AMD) and a 5,000-unit MOQ per SKU.

#### 3.3.5 Bakery and food

| Item | Price | Status |
|---|---|---|
| SAS Sweet classic croissant (fresh, in-store bakery) | AMD 750 retail; filled variants 710–1,290 | REPORTED [S40] |
| PAUL café, Yerevan, croissant / almond croissant | AMD 900 / 1,400 (menu) | REPORTED, Feb 2026 [S46] |
| Frozen butter croissants, Russian producers (EAEU, duty-free) | Rus Bakery 65 g: RUB 1,850 per 80 pcs = RUB 23 (≈AMD 99); GFC "Allegro Foods" 80 g: RUB 2,225 per 70 pcs = RUB 32 (≈AMD 136); Gourmand 65 g: RUB 4,797 per 80 = RUB 60 (≈AMD 256) | REPORTED (undated) [S45] |
| Armenian distributor of frozen viennoiserie (Bridor, Délifrance, Lantmännen Unibake, Vandemoortele) | **None identified** | Gap |
| Gata: SAS Sweet round 300 g / Zeituni 175 g / curd mini gata | AMD 1,030 (3,433/kg) / 430 (2,457/kg) / 350 | REPORTED [S40] |
| Lavash: tandoor 550 g / single tandoor sheet | AMD 820 (1,491/kg) / 197 | REPORTED [S40] |
| Eggs (10 pcs) | AMD 990–1,180 (99–118 each) | REPORTED [S40] |
| Butter 82% | AMD 5,500–8,790/kg (Anchor, Valio, Président) | REPORTED [S40] |
| Cheese: Lori / Chechil / Gouda (Dili) / Mozzarella | AMD 3,450–5,150 / 5,433–5,990 / 5,990 / 3,890–5,580 per kg | REPORTED [S40] |
| Ham (Miratorg 400 g) / turkey breast (Ferrarini) | AMD 6,975/kg / 11,800/kg | REPORTED [S40] |
| Lemons (Uzbek) / oranges | AMD 1,570/kg / 1,580/kg | REPORTED [S40] |
| Bagged ice (fallback if the ice machine fails) | AMD 190–440/kg | REPORTED [S40] |

Model inputs:
- **Croissant (ESTIMATE): AMD 350 landed** for an 80 g frozen butter croissant. That is about AMD 135–255 ex-works, plus about 40% for frozen freight and handling (ASSUMPTION), plus bake energy. Alternative: buy fresh from a local bakery at an assumed AMD 400–500 wholesale (ASSUMPTION; the retail benchmark is 750).
- **Gata: AMD 300 per 100–120 g piece**, bought in (ASSUMPTION; about 15–25% below retail per kg).

#### 3.3.6 Delivery frequency feasible on the M4 corridor (ASSUMPTION; confirm with suppliers' route maps)

| Category | Shelf life / storage | Feasible frequency to an M4 site | Comment |
|---|---|---|---|
| Fresh milk | 5–10 days chilled (pasteurised); UHT months | 3–7× per week (or 2× per week with a UHT buffer) | Ask Marianna/Dili whether the Abovyan/Hrazdan/Sevan route is served daily. Keep 1–2 days of UHT as safety stock |
| Coffee | 2–6 weeks | Weekly | Low risk |
| Frozen pastry | Months at −18 °C | Weekly or fortnightly | Requires about 0.5–1 m³ of freezer space |
| Fresh pastry, gata | 1–3 days | Daily, or 3× per week with day-old discounting | Higher waste risk outside Yerevan |
| Sandwich/wrap ingredients | 3–7 days | 2–3× per week | Or central prep in Yerevan with a daily shuttle |
| Packaging, syrups, dry goods | Months | Fortnightly or monthly | Ties up working capital. Store 4–6 weeks of cups |

The approximate distance from Yerevan to Sevan (≈60–65 km) is an ASSUMPTION to be confirmed by the site workstream. Strong summer seasonality toward Lake Sevan amplifies stock-out risk in peaks and waste risk off-season.

### 3.4 Recipe-level COGS (ESTIMATE)

**Inputs** (status in brackets):
- Espresso blend AMD 12,000/kg [ASSUMPTION]; coffee waste factor 1.05 [ASSUMPTION].
- Whole milk AMD 700/L [ESTIMATE from REPORTED retail]; milk waste 1.10 for hot drinks and 1.05 for cold [ASSUMPTION].
- Monin-type syrup AMD 6,500/L [ASSUMPTION from REPORTED retail]; hot chocolate powder AMD 12,000/kg [ASSUMPTION from REPORTED retail]; sugar AMD 450/kg [REPORTED]; lemons AMD 1,570/kg [REPORTED].
- Own ice AMD 5 per drink [ASSUMPTION]; packaging per §3.3.4 [REPORTED unit prices].
- Doses [ASSUMPTION, standard specialty practice]: 9 g single shot, 18 g double for all milk drinks and americano, 22 g for a 450 ml cold brew (about 150 ml concentrate plus water and ice).
- Menu prices are **target prices including 20% VAT** [ASSUMPTION, positioned against REPORTED Yerevan benchmarks]. COGS% is shown on both the gross (VAT-inclusive) and net-of-VAT price. **Use the net figure if the company is a VAT payer.**

| Item | Recipe basis | Ingredients AMD | Packaging AMD | **COGS AMD** | COGS USD | Target price AMD | COGS % gross | **COGS % net of VAT** |
|---|---|---|---|---|---|---|---|---|
| Espresso 30 ml | 9 g coffee | 113 | 19 | **132** | 0.37 | 1,000 | 13.2% | **15.9%** |
| Americano 350 ml | 18 g coffee, hot water | 229 | 38 | **267** | 0.74 | 1,300 | 20.5% | **24.6%** |
| Cappuccino 300 ml | 18 g + 200 ml milk | 381 | 35 | **416** | 1.15 | 1,500 | 27.7% | **33.3%** |
| Latte 400 ml | 18 g + 300 ml milk | 458 | 38 | **496** | 1.37 | 1,700 | 29.2% | **35.0%** |
| Iced latte 450 ml | 18 g + 230 ml milk + ice | 401 | 41 | **442** | 1.22 | 2,000 | 22.1% | **26.5%** |
| Cold brew 450 ml | 22 g coffee (steeped), ice | 284 | 41 | **325** | 0.90 | 1,900 | 17.1% | **20.5%** |
| Signature flavoured latte 400 ml | Latte (280 ml milk) + 25 ml syrup + AMD 60 topping (ASSUMPTION) | 665 | 38 | **703** | 1.94 | 2,100 | 33.5% | **40.2%** |
| Hot chocolate 350 ml | 30 g powder + 280 ml milk | 576 | 38 | **614** | 1.70 | 1,600 | 38.4% | **46.0%** |
| Lemonade 450 ml | 130 g lemons, 30 g sugar, 15 ml fruit syrup, soda, mint (AMD 20), ice | 350 | 41 | **391** | 1.08 | 1,500 | 26.1% | **31.3%** |
| Butter croissant (bake-off) | Frozen 80 g, landed (§3.3.5) | 355 | 15 | **370** | 1.02 | 950 | 38.9% | **46.7%** |
| Breakfast wrap (full) | Lavash 80 g, 2 eggs, cheese 40 g, ham 40 g, veg 40 g, sauce 15 g, butter 5 g, 5% waste | 1,017 | 30 | **1,047** | 2.89 | 2,200 | 47.6% | **57.1%** |
| Breakfast wrap (cost-engineered) | Lavash 80 g, 1 egg, cheese 40 g, veg 30 g, sauce, butter, 5% waste | 598 | 30 | **628** | 1.73 | 1,800 | 34.9% | **41.8%** |
| Gata (bought in, 100–120 g) | Local bakery | 300 | 15 | **315** | 0.87 | 650 | 48.5% | **58.2%** |

*Food COGS excludes labour and oven energy beyond the AMD 5 bake allowance. Wrap veg is priced at AMD 1,500/kg and sauce at AMD 3,000/kg (ASSUMPTION).*

**Sensitivity: latte 400 ml COGS % of net price at AMD 1,700**

| Coffee AMD/kg → / Milk AMD/L ↓ | 9,000 | 12,000 | 16,000 |
|---|---|---|---|
| 600 | 28.7% | 32.7% | 38.0% |
| 700 | 31.0% | **35.0%** | 40.3% |
| 850 | 34.5% | 38.5% | 43.8% |

**Blended margins (ESTIMATE).**
- Beverage mix (ASSUMPTION, typical drive-thru skew to milk and iced drinks): espresso 4%, americano 15%, cappuccino 13%, latte 18%, iced latte 16%, cold brew 6%, flavoured latte 16%, hot chocolate 5%, lemonade 7%. Result: average ticket per drink AMD 1,691; average COGS AMD 449; **COGS 26.6% of gross / 31.9% of net-of-VAT revenue.** Packaging averages AMD 38 per drink (8.4% of beverage COGS).
- Food mix (ASSUMPTION): croissant 45%, cost-engineered wrap 30%, gata 25%. Average price AMD 1,130; COGS AMD 434; **38.4% gross / 46.0% net.**
- **Total blended COGS: 29.5% gross / 35.4% net at a 75/25 beverage/food revenue split.** It is 34.7% net at 80/20 and 36.1% at 70/30.

**Yerevan market price benchmarks (REPORTED, many listings undated or stale)** [S46]:

| Item | Observed prices (AMD) | Venue / source |
|---|---|---|
| Espresso | 950 | Surf Coffee X Tumanyan (Yandex Maps menu) |
| Americano | 1,000; 1,200 regular / 1,600 large | Jeffrey's Coffee; FEIN by Coffee House (Tripadvisor) |
| Cappuccino | 1,000–1,200; 1,200; 1,500; 1,600; 1,500–2,200 | Jeffrey's; The Green Bean (2025 listing); FEIN; Surf Coffee; The Coffee |
| Latte | 1,000 / 1,400 (two sizes); 1,500 / 1,800; 1,900 | Coffee House Cafe; FEIN; Ground Zero (older review) |
| Iced latte | 2,100; (Coffee House 900, stale listing) | Surf Coffee; Coffee House (Yandex) |
| Flavoured latte | Raspberry Latte 2,200; Spanish latte 1,000 / 1,400 (Coffee House), 1,800–2,200 (FEIN) | Surf; Coffee House; FEIN |
| Specialty espresso/filter (guide range) | 1,000–1,800 | Armenia Spirit guide, 2026 |
| Croissant | 900 (almond 1,400) | PAUL (restonews.am, Feb 2026) |
| Croissant (supermarket bakery) | 750 | SAS Sweet |
| Gata (supermarket) | 350–1,030 | SAS |

**Recommended target menu ranges (VAT-inclusive, ASSUMPTION, premium-convenience positioning):**

| Item | Range (AMD) |
|---|---|
| Espresso | 900–1,100 |
| Americano | 1,200–1,500 |
| Cappuccino | 1,400–1,700 |
| Latte 400 ml | 1,600–1,900 |
| Iced latte | 1,800–2,200 |
| Cold brew | 1,700–2,100 |
| Signature flavoured latte | 1,900–2,300 |
| Hot chocolate | 1,400–1,800 |
| Lemonade | 1,300–1,700 |
| Croissant | 800–1,100 |
| Breakfast wrap | 1,800–2,400 |
| Gata | 500–800 |

---

## 4. Implications for the drive-thru concept (critical)

1. **Gross margin is healthy on drinks and thin on food.**
   - Drinks run about 68% gross margin on net revenue: blended beverage COGS ≈ 32% of net, before card fees (~1.35%) and waste.
   - Food at 42–58% net COGS dilutes the total. The full breakfast wrap and bought-in gata are the weakest items.
   - Food should be priced and engineered as an attach item: cost-engineered recipes, bake-off pastry and limited SKUs. Do not build a broad hot-food menu, which also slows the window.
2. **Flavoured and iced drinks are the profit engine.** Iced latte (27% net COGS) and cold brew (21%) earn more per cup than hot chocolate (46%) or the flavoured latte (40%) at the assumed prices.
   - Syrup cost (Monin carries 12% duty) is the swing factor on flavoured drinks. Price the syrup add-on explicitly (≥ AMD 200–300), or test an EAEU-origin syrup.
3. **Premium pricing risk.** At AMD 1,600–2,100 per milk drink, the concept prices above the dominant chain, Coffee House (57 branches; lattes around AMD 1,000–1,400 in listings), and level with specialty cafés.
   - On a highway, convenience can carry a premium. Commuters and repeat local traffic, however, will compare against Coffee House.
   - Model a downside price scenario about 15% lower. At a latte price of AMD 1,450, net COGS rises from 35% to 41%.
4. **Equipment strategy should follow serviceability, not brand prestige.**
   - The only verified local service channel covers La Marzocco, Victoria Arduino, Nuova Simonelli, Mahlkönig, Franke, Hoshizaki and Bravilor (The Horeca).
   - A flagship built on Eversys plus TurboChef/Merrychef has no verified local service. One breakdown during summer peak on the M4 could close the window for days.
   - Mitigations: dual machines (redundancy); a spares kit; a service-level agreement that names a response time; staff trained on first-line maintenance.
5. **Do not budget from US catalogues.** US 60 Hz models need EU/INT equivalents. Prices for those (especially ice machines and refrigeration) are unverified. EU-direct pricing appears 20–30% below US retail for La Marzocco (UK ex-VAT ≈ USD 15.5k vs US USD 19.7k).
   - Treat the package totals as ±20%. Get at least 2–3 quotes (The Horeca, DR HORECA, and a direct EU distributor) before investment committee.
6. **The VAT position materially changes economics.**
   - On equipment, about 17% of landed cost is import VAT, recoverable only by a VAT payer.
   - On revenue, COGS% is about 5 percentage points higher on a net-of-VAT basis.
   - The tax-regime choice (VAT versus turnover tax) is outside this workstream. It must be fixed before the 5-year model is built.
7. **FX helps capex but the risk is two-sided.** The AMD has appreciated about 6.5% against the USD since Sep 2024 (387.29 → 361.93). Imported equipment, imported coffee, Monin syrups and Alpro are cheaper in AMD today. A reversal would raise the 50–60% of beverage COGS that is imported (coffee, syrups, plant milk, part of the packaging resin and paper).
8. **Card cost is not capped for this business.** Do not assume the 0.5/0.9% caps that are widely reported in Armenian media. They exclude restaurant MCCs. Negotiate with 2–3 banks: at expected volumes (several million AMD per month), rates below the 1.2% list are plausible but unverified. Watch for the AMD 50,000 early-termination clauses and minimum monthly fees.
9. **Fiscal and technology integration is a gating item.** e-HDM rules are changing (law July 2026; implementing rules from Jan 2027). Select a POS only after a live demonstration of Armenian HDM/e-HDM fiscalisation, bank-terminal integration and KDS.
   - A drive-thru also needs headsets, an order-confirmation board and speed-of-service timers. None of these were priced, and no local HME/3M partner was found. Imported wireless headsets may need frequency approval.
10. **Supply chain: favour bake-off and long-life buffers on the M4.**
    - Fresh pastry and fresh milk from Yerevan on a 60+ km run (ASSUMPTION) raise stock-out and waste risk. Seasonality around Lake Sevan makes this worse.
    - Recommended: frozen pastry with weekly delivery, a UHT milk buffer, and 4–6 weeks of packaging stock (a working-capital need).
    - No Armenian importer of premium frozen viennoiserie was found. Options are a direct import from Russia (EAEU, duty-free) or contract production with a Yerevan bakery.
11. **Local roasters are a structural advantage.** The 0% duty on green versus 8% (minimum €0.16/kg) on roasted coffee favours sourcing from AfroLab, FEIN, Lumen, Nero Bean or Caffeine, or later roasting in-house (Probat is linked by The Horeca).
    - A co-branded local roast also supports the premium story better than imported Italian blends.
12. **Water quality is a hidden capex and opex item.** Scale is the main killer of espresso boilers, so filtration and softening are not optional. A site water analysis is needed: municipal (Veolia Jur) or well water if the site is off-grid on the M4.

---

## 5. Data gaps & how to verify them

| # | Gap | Why it matters | How to verify (agency / document / supplier) |
|---|---|---|---|
| 1 | **Dealer quotations** for espresso machines, grinders, ice machines (EU spec), refrigeration, warewashing, water treatment | Equipment capex is ±20% without them | RFQ with an identical BOM to The Horeca LLC (+374 60 87 87 87, product@thehoreca.com), DR HORECA (+374 44 878710), Arahet Development and Art Global. Request a parallel EU quote (e.g., La Marzocco/Victoria Arduino Italian distributors) DAP Yerevan |
| 2 | Armenian service partner for Eversys, WMF, Schaerer, Merrychef, TurboChef | Uptime risk | Email each manufacturer's export team for the territory partner covering Armenia (often Georgia/Russia/UAE). Request SLA terms |
| 3 | HS classification of speed ovens (0% vs 10%) and commercial blenders | 10% duty swing | Request a preliminary classification decision from the SRC (Customs) with the spec sheets. Confirm import VAT base (customs value + duty) and customs fees with a licensed broker |
| 4 | National exemptions or deviations from the EAEU CET for Armenia | Could lower duty | SRC customs department / arlis.am (Government decisions on tariff privileges); broker |
| 5 | **Wholesale coffee prices** | Largest COGS input (~45% of latte COGS) | RFQ to AfroLab (wholesale registration form on afrolab.am), FEIN/Coffee House roastery, Lumen, Nero Bean, Caffeine (Dilijan), Royal Armenia: price per kg for espresso blend and cold-brew coffee at 30–60 kg/month, delivery terms to the M4 site |
| 6 | HoReCa milk price and delivery route | ~45% of milk-drink COGS; daily logistics | Request HoReCa price lists and route schedules from Marianna, Dili, Yeremyan Products, Bonilat. Ask about 1 L barista/UHT formats |
| 7 | Frozen viennoiserie importer in Armenia, landed price | Croissant COGS and food quality | Ask Alpha Food Service and other HoReCa importers. Get Russian producer quotes (Rus Bakery, GFC, Allegro) DAP Yerevan incl. reefer freight via Upper Lars. Compare with a contract bake from a Yerevan bakery |
| 8 | Syrup wholesale price (Monin via Alpha Food Service) and EAEU alternatives | Flavoured-drink margin | RFQ to Alpha Food Service; sample Barinoff/Russian brands through a local importer |
| 9 | Packaging: VAT treatment, custom-print pricing, straws, bags, carriers | ~8% of beverage COGS | RFQ to Oval Pack (+374 10 720 059) for branded cups (MOQ 5,000), plus Art Global; compare with Chinese/Turkish imports (10% duty) |
| 10 | **POS with Armenian HDM/e-HDM integration**: iiko, R-Keeper, Poster, local systems | Legal compliance; operations | Ask vendors for live references in Armenia; confirm with the SRC the e-HDM integration spec and the timeline of the Tax Code amendment (first reading May 2026); review HO-309-N and Gov. Decision 1257-N on arlis.am |
| 11 | Negotiated card acquiring rates (Ameria, ACBA, Ardshinbank, Evoca, Inecobank, FastBank) | 1–2% of revenue | Formal tender with projected monthly volume; confirm MCC assignment (5814) and confirm the CBA cap does not apply |
| 12 | Idram and Telcell QR merchant fees; Google Pay availability | Payment mix and cost | Request merchant agreements from Idram (IDBank) and Telcell; check Google Pay support with issuing banks |
| 13 | Headsets (HME/3M), order-confirmation and menu boards, timers; RF approval | Drive-thru capex and throughput | RFQ via HME/3M EMEA distributors; local AV/LED-signage integrators in Yerevan; check frequency rules with the telecom regulator |
| 14 | White-label app cost | Loyalty/digital strategy | Quotes from 2–3 Yerevan studios vs POS-native modules (Poster Site, iiko loyalty) |
| 15 | Current menu prices at Coffee House, Jazzve, The Green Bean, Coffeeshop Company, Surf | Price positioning | Mystery-shop or photograph menu boards at 5–8 outlets in Oct–Nov 2026; check delivery apps (Yandex Eats, Menu.am) |
| 16 | Electricity load and utility costs for the equipment set | Connection capex and opex | Spec sheets from the chosen equipment → load schedule → ENA connection application (other workstream) |
| 17 | Site water quality | Filter specification and maintenance cost | Lab test of the site water (Veolia Jur supply or well) |

---

## 6. Sources (all accessed 2026-10-10 unless noted)

1. [S1] Central Bank of Armenia, official exchange rates web service (ExchangeRatesLatest, rates dated 2026-10-09): https://api.cba.am/exchangerates.asmx
2. [S2] The Horeca LLC, homepage (services, projects, brand links, contacts): https://www.thehoreca.com
3. [S3] Mahlkönig, authorised dealer page "The Horeca LLC": https://www.mahlkoenig.com/pages/the-horeca-llc
4. [S4] Spyur.am listing "DR HORECA" (search snippet; page blocked by Cloudflare): https://www.spyur.am/am/companies/the-horeca/36014
5. [S5] Spyur.am business directory, coffee machines/equipment category (Arahet Development, Art Global; search snippets): https://www.spyur.am/en/business_directory/bd/41632 ; https://www.spyur.am/en/companies/art-global/36585
6. [S6] Alta-Soft EAEU tariff database (import duty by HS code): https://www.alta.ru/tnved/code/8419812000/ ; /8419818000/ ; /8418690008/ ; /8516500000/ ; /8509400000/ ; /8422190000/ ; /8418501900/ ; /8421210009/ ; /8516710000/ ; /4823699000/ ; /3923501000/ ; /0901110001/ ; /0901210001/ ; /2106909808/ ; /1905909000/ ; /8471300000/
7. [S7] Kontur, CN FEA 8419 81 200 0 (0% duty): https://kontur.ru/markirovka/tnved/xvi/8419/81/200/0 ; IFCG: https://www.ifcg.ru/kb/tnved/8419812000/
8. [S8] PwC Worldwide Tax Summaries, Armenia: Other taxes (VAT 20%, EAEU imports; last reviewed 30 Jun 2026): https://taxsummaries.pwc.com/armenia/corporate/other-taxes
9. [S9] Coffee Machine Depot, La Marzocco Linea PB AV 2-group: https://coffeemachinedepot.com/products/la-marzocco-linea-pb-av-2-group-commercial-espresso-machine-custom-painted-from-factory ; Espresso Parts: https://www.espressoparts.com/products/la-marzocco-linea-pb-2-group-av-with-scales-espresso-machine
10. [S10] Linea PB UK, AU and CA dealer listings (search results): https://www.coffeeparts.com.au/lamarzocco-linea-pb-av-2gr ; https://cafeliegeois.ca/products/la-marzocco-linea-pb-av-abr
11. [S11] Victoria Arduino Eagle One: https://majestycoffee.com/products/victoria-arduino-eagle-one ; https://blackrabbitservice.com/products/victoria-arduino-eagle-one ; https://www.coffeemachinedepot.com/collections/2-group-heads?page=4
12. [S12] Nuova Simonelli Aurelia Wave: https://www.voltagerestaurantsupply.com/products/nuova-simonelli-aurelia-wave-vol ; https://blackrabbitservice.com/collections/all/products/nuova-simonelli-aurelia-wave-volumetric-espresso-machine
13. [S13] Kofemarket (Kyiv), 2-group machines incl. NS Appia Life/Compact (search snippet): http://kofemarket.com.ua/category/2gr-coffeemachine
14. [S14] Eversys: https://visionsespresso.com/eversys/?page=2 ; https://procoffeegear.com/products/eversys-cameo ; https://procoffeegear.com/products/eversys-enigma-e4m ; https://majestycoffee.com/products/eversys-enigma-classic-espresso-machine
15. [S15] Franke A-series: https://majestycoffee.com/pages/franke-a600-vs-a800 ; https://majestycoffee.com/products/franke-a800-fresh-brew-superautomatic-coffee-machine ; https://www.caterkwik.co.uk/shop/shop-by-brand/franke-coffee-systems/
16. [S16] Mahlkönig E80 Supreme, US: https://majestycoffee.com/products/mahlkonig-e80-supreme-on-demand-espresso-grinder ; https://coffeemachinedepot.com/products/mahlkonig-e80-supreme-commercial-espresso-coffee-grinder ; https://blackrabbitservice.com/collections/all/products/mahlkonig-e80-supreme-espresso-grinder
17. [S17] Mahlkönig, Russian retail: https://entero.ru/item/117425 (EK43) ; https://entero.ru/item/317538 (E65S) ; https://coffeestate.ru/catalog/kofemolki/mahlkonig/ ; https://restoran-service.ru/catalog/kofemolki_dozatory/mahlkonig_germaniya/
18. [S18] Merrychef eikon e2s: https://www.webstaurantstore.com/merrychef-eikon-e2s-classic-high-speed-accelerated-cooking-countertop-oven-208-240v/574E2SSCH.html ; https://www.h2products.co.uk/?p=186320
19. [S19] TurboChef: https://www.webstaurantstore.com/turbochef-sota-single-mag-high-speed-accelerated-cooking-countertop-oven-with-touch-controls-208-240v/532SOTAMAGT.html ; https://www.catering-appliance.com/turbo-chef/high-speed-ovens
20. [S20] Hoshizaki: https://www.katom.com/440-KM520MAJB300SF.html ; https://www.katom.com/index.php/440-KMD355MAJB500212.html ; https://www.cityfoodequipment.com/collections/ice-machines-with-bins ; https://www.wasserstrom.com/restaurant-supplies-equipment/ice-machines-with-bins
21. [S21] Vitamix The Quiet One: https://www.vitamix.com/us/en_us/commercial/products/the-quiet-one ; Blendtec Stealth 885 (AU): https://commercialequipmentonline.com.au/products/blendtec-stealth-885
22. [S22] Bunn ICB: https://www.katom.com/021-542000101.html ; https://www.katom.com/index.php/021-532000100.html ; https://voltagerestaurantsupply.com/collections/bunn
23. [S23] Consumer blog on Dutch Bros espresso machines (weak source): https://cookwithrome.com/?p=87965
24. [S24] CBA Board Decision 27-N of 09.02.2026 on maximum fees for cashless operations, and Appendix 1 (MCC list): https://www.cba.am/hy/Board-decisions/9505/ ; https://www.cba.am/file_manager/Decision-Appendix/2026/Appendix-1-27N.pdf
25. [S25] ArmInfo via Finport.am, "Central Bank sets maximum commission fee limits…" (11 Feb 2026): https://finport.am/full_news.php?id=55549&lang=3
26. [S26] Fast Bank, POS terminals tariffs (updated 27.04.2026): https://www.fastbank.am/en/individual/more/pos
27. [S27] Ameriabank CJSC tariffs for corporate clients (effective 3 Apr 2026), section 7 POS: https://ameriabank.am/Portals/0/files/Business/green/Corporate_tariffs_03.04.26_eng.pdf
28. [S28] Ameriabank Internet Acquiring Terms and Tariffs, ed. 9 (effective 27 Apr 2026): https://ameriabank.am/Portals/0/files/Business/pos/green/Internet_Acquiring_Terms_and_Conditions_ed9_eng.pdf
29. [S29] Evocabank payment card tariffs (updated 09/10/2026): https://www.evoca.am/en/tariffs-for-commissions/cards-tariffs/tariffs-payment-cards
30. [S30] Apple Pay launch in Armenia: https://armenpress.am/en/article/1073251 ; https://appleosophy.com/2022/01/18/apple-pay-debuts-in-armenia-launches-in-six-banks/ ; https://www.nfcw.com/?p=75651
31. [S31] Idram unified QR / merchant network: https://www.fintech.am/idram-qr/?lang=en ; https://www.fintech.am/idram/?lang=en
32. [S32] iravaban.net, "From 2027 new regulations for e-HDM receipts" (26 Aug 2026): https://iravaban.net/569382.html ; [S32b] ARKA, "Use of electronic HDMs will be expanded: draft" (20 May 2026): https://arka.am/am/news/business/kendlaynvi-elektronayin-hdm-neri-kirarume-nakhagitc/ ; [S32c] https://packagist.org/packages/tobelyan/e-hdm ; https://wordpress.org/plugins/virtual-hdm-for-taxservice-am/
33. [S33] HDM device prices (search snippets): https://realhashvapah.am/blog/nor-serndi-hdm-sarq/ ; https://qterminal.am/ ; https://www.list.am/en/category/223?q=%D5%B0%D5%A4%D5%B4 ; 2019 regulated price: https://www.aravot.am/2019/02/06/1016409/
34. [S34] Poster POS pricing: https://joinposter.com/en/pricing
35. [S35] iiko tariffs (Russian dealer): https://iiko-sa.ru/services/iiko/iiko-tarify/
36. [S36] Yerevan City online supermarket, coffee category (also milk items on the same page): https://yerevan-city.am/shop/products/201
37. [S37] Caffeine specialty roastery (Dilijan), product catalogue: https://caffeine.am/ (products.json)
38. [S38] AfroLab Roastery: https://www.afrolab.am/ ; https://www.afrolab.am/menu
39. [S39] Yerevan roaster guides: https://coffeehow.co/specialty-coffee-yerevan-fein/ ; https://wanderlog.com/list/geoCategory/1861466/best-coffee-roasters-in-yerevan ; https://royalarmenia.coffee/en/product-type/roasted-coffee-beans/
40. [S40] SAS supermarket online catalogue: milk https://www.sas.am/en/catalog/moloko/ ; Alpro https://www.sas.am/catalog/brand_alpro/ ; butter https://www.sas.am/en/catalog/slivochnoe_maslo/ ; cream https://www.sas.am/en/catalog/slivki_kokteyl/ ; Armenian cheese https://www.sas.am/en/catalog/armyanskiy_syr/ ; eggs https://www.sas.am/en/catalog/molochnye_produkty/ ; gata https://www.sas.am/en/catalog/gata/ ; croissant https://www.sas.am/en/catalog/croissant/ ; lavash https://www.sas.am/en/catalog/lavashhh/ ; sugar https://www.sas.am/en/catalog/sakhar/ ; ham https://www.sas.am/en/catalog/vetchina/ ; hot chocolate https://www.sas.am/en/catalog/goryachiy_shokolad_kappuchino/ ; cocoa https://www.sas.am/en/catalog/kakao/ ; ice https://www.sas.am/en/catalog/led/ ; tropical fruit https://www.sas.am/en/catalog/ekzotika/
41. [S41] Monin in Yerevan: https://thehouse.am/am/brand/monin/page/3 ; https://thehouse.am/am/product/maple-spice-syrup-monin ; https://www.sas.am/catalog/kompot/163800/ ; https://noyantunonline.am/hy/shop/%D1%81%D0%B8%D1%80%D0%BE%D0%BF-monin-caramel-0-7%D0%BB/ ; Alpha Food Service: https://www.yell.am/-ALPHA-FOOD-SERVICE-CJSC-2889 ; https://staff.am/company/alpha-food-service-llc
42. [S42] Barinoff syrup, Russia: https://www.barista-ltd.ru/magazin/syrup-barinoff-raspberry-1000ml.html ; https://foodcorn.ru/siropy/siropy-barinoff
43. [S43] Oval Pack (Ovalplast), Yerevan, wholesale catalogue: https://ovalpack.am/tkhtya-bazhakner ; https://ovalpack.am/tkhte-bazhak-erkshert-400-hat ; https://ovalpack.am/bazhaki-kaparichner ; https://ovalpack.am/bazhaki-tapantsik-kaparichner ; https://ovalpack.am/bazhakner ; https://ovalpack.am/tkhtya-brnakner
44. [S44] Retail cup cross-checks: https://complex.am/catalog/odnorazovaya_posuda/stakany/bumazhnye_stakany/ ; https://www.officepro.am/hy/product/tea-coffee/disposable-items/disposable-items
45. [S45] Russian frozen croissant wholesale: https://gfc-russia.ru/catalog/konditerskie-izdeliya-vypechka-morozhenoe/vypechka-sloenaya/criterii-kruassany ; https://rusbakery.ru/catalog/kruassany/kruassan_frantsuzskiy_na_slivochnom_masle_65gr/ ; https://productcenter.ru/products/catalog-kruassany-753
46. [S46] Yerevan menu prices (search snippets; Tripadvisor and Yandex pages partly blocked): https://www.tripadvisor.com/Restaurant_Review-g293932-d34315833-Reviews-FEIN_by_Coffee_House-Yerevan.html ; https://www.tripadvisor.com/Restaurant_Review-g293932-d28283562-Reviews-Coffee_House_Cafe-Yerevan.html ; https://www.tripadvisor.com/Restaurant_Review-g293932-d33393017-Reviews-Jeffrey_s_Coffee_Yerevan-Yerevan.html ; https://yandex.com/maps/org/surf_coffee_x_tumanyan/235371465522/ ; https://yandex.com/maps/org/the_coffee/102752569728/ ; https://yandex.com/maps/org/coffee_house/178826944404/ ; https://restonews.am/blog/2026/02/01/menu-10-establishments/ ; https://www.spottedbylocals.com/yerevan/the-green-bean-cafe/ ; https://www.armenia-spirit.com/guides/yerevan-cafe-culture-guide/
47. [S47] Coffee House Company (57 branches; menu without prices): https://coffeehouse.am ; https://coffeehouse.am/mer-tesakanin
48. [S48] State procurement coffee price (undated, outlier, not used): https://www.ilur.am/8500-%D5%A4%D6%80%D5%A1%D5%B4-%D5%B4%D5%A5%D5%AF-%D5%BF%D5%B8%D6%82%D6%83-%D5%AF%D5%A1%D5%AF%D5%A1%D5%B8%D5%B5%D5%AB-4600-%D5%A4%D6%80%D5%A1%D5%B4%D5%9D-1-%D5%AF%D5%A3-%D5%BD%D5%B8%D6%82%D6%80%D5%B3/
49. [S49] buy.am, Yerevan City storefront (Royal Armenia Ultra; plant milks): https://buy.am/en/products/yerevan-city/ground-arabica-50-and-robusta-50-coffee-royal-armenia-ultra-100g/1043890-2900000027510
50. [S50] CEIC, Armenia foreign exchange rate (USD/AMD 387.29, Sep 2024; search snippet): https://www.dr.ceicdata.com/en/armenia/foreign-exchange-rate
