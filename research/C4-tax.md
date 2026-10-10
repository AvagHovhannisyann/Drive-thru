# C4 — Tax Regime and Legal Structure for a Café / Drive-Thru in Armenia (2026)

*Prepared 2026-10-10. Analyst workstream C4. Currency: AMD; USD at the CBA official rate of 9 Oct 2026, **USD 1 = AMD 361.93** (VERIFIED in A1-macro-consumer.md, source [1] there).*

**Status tags.**
- **VERIFIED**: a primary or official text I opened myself, mainly the consolidated Tax Code and the amending laws on arlis.am, plus SRC, e-register and WIPO pages.
- **REPORTED**: a credible secondary source or an official *draft*.
- **ESTIMATE**: my own calculation; the formula and inputs are shown.
- **ASSUMPTION**: analyst judgement; the basis is stated.

**How this was researched.**
- The shared web-search budget (200 calls per turn, across all agents) was already used up when this workstream started. **No search-engine queries were run for C4.**
- Every fact comes from primary sources opened directly:
  - the official consolidated **Tax Code of the RA** on arlis.am. That text includes amendments up to **Law HO-440-N of 27 Aug 2026**, the latest amendment referenced in it [1];
  - the amending laws themselves [2]–[11];
  - the Law on State Duty [13], the Law on Funded Pensions [14], SRC pages [15][16], e-register.am [17], e-draft.am [18][19] and WIPO [20];
  - sibling research files C1, C2, A1 and B1.
- Items I could not open are listed in Section 5 with a verification route.

**This is not legal advice.** Several conclusions rest on my reading of Armenian statutory text. The most important ones are listed in Section 5 and should be confirmed by a written SRC clarification under Tax Code Art. 306, or by an Armenian tax adviser, before the model is finalised.

---

## 1. Executive summary

1. **Catering has its own turnover-tax path with no revenue cap. This is the single most important tax fact for this project** (VERIFIED, Tax Code Art. 254(6)–(7), 258) [1].
   - A resident LLC in public catering can stay on turnover tax (TT) at **any revenue level**. It must file a "catering" TT declaration; the declaration overrides the AMD 115M ceiling and the related-party restrictions.
   - **TT replaces both VAT and the 18% profit tax** (Art. 253).
   - 2026 catering formula: **TT = 12% × catering receipts − 9% × documented operating expenses, never less than 3.5% of receipts.** Unused deductions carry forward.
   - At typical café cost structures this means an **effective rate of about 4.5–6.5% of gross receipts** (ESTIMATE, §3.11). That is 5.2% / 6.25% at AMD 150M / 300M with AMD 6M land rent, and 4.5% / 5.9% with the model-wide AMD 18M rent. At the C6 base of AMD 140M it is 4.3–5.1%. The VAT regime instead takes 16.67% of every VAT-inclusive sale before input credits, plus profit tax.
     - *Fact-check correction: the original "5–6.5%" assumed AMD 6M a year of land rent, which contradicts C6/B4 (AMD 15.6–21.6M). Higher documented rent lowers TT. See §3.11.*
2. **The 2024–2025 reform doubled the headline catering rate and only reached the M4 corridor on 1 Jan 2026** (VERIFIED) [2][3].
   - Law HO-285-N (12 Jun 2024) replaced the old **flat 6%** catering TT with the 12% / 9% / 3.5% formula. It applied in Yerevan from 1 Jan 2025 and **outside Yerevan (Kotayk, Gegharkunik) from 1 Jan 2026**.
   - HO-72-N (26 Mar 2025) widened the deductible expenses to include administrative and selling costs from 2025.
   - **The SRC's own guidance page still shows the old 6% rate** (last updated 6 Oct 2022) [15]. Any secondary source quoting 6% is out of date. *Fact-check: source unreachable on 10 Oct 2026; treat as unverified.* (The page body loads dynamically and could not be retrieved. No 2026 figure depends on it: the 12% rate is confirmed from Art. 258 itself, and ARKA (6 Jun 2024) [23] confirms the pre-reform 6%.)
   - *Fact-check note: part of the M-4 corridor (Nor Nork / Avan) lies inside Yerevan's administrative boundary. A site there has been on the new formula since 1 Jan 2025 and cannot use micro-entrepreneurship (§3.6).*
3. **Expenses that do not count against TT** (VERIFIED, Art. 258(6) as amended): capex, depreciation, costs incurred on fixed assets (repairs and maintenance), business trips and representation.
   - TT therefore gives **no relief for the heavy capex** of a drive-thru, and a TT payer **cannot recover the 20% VAT** on construction and equipment.
   - That VAT is about 1/6 of the VAT-inclusive capex: **≈ AMD 36M for the mid-range unit** (ESTIMATE, using C1/C2 capex).
4. **Recommended regime for a single unit depends on both capex and revenue. In the study's base case (mid-range capex, AMD 100–150M receipts) the VAT regime is better on 5-year NPV.** Catering TT wins clearly only with lean capex, or with receipts above about AMD 200M at mid capex (ESTIMATE, §3.11(a)).
   - *Fact-check correction: the original text recommended "catering TT for AMD 150–300M receipts; the exception is a high-capex flagship". That contradicted this file's own breakeven table: the mid-capex 5-year breakeven was ≈186M even on the original timing. It also ignored the study's base revenue of AMD 100–150M (C6-benchmarks.md: base 140M = 150 tx × AMD 2,600 × 360 days).*
   - Steady-state annual cash saving of TT versus the VAT regime (ESTIMATE): about **AMD 6.9–7.4M at 140M, AMD 7.7M at 150M and AMD 20.4–21.5M at 300M** of receipts. Each range runs from AMD 6M to AMD 18M of land rent.
   - The VAT regime recovers the capex VAT once, during construction: ≈AMD 36M for a mid-range unit. **With that refund at t=0, the 5-year NPV breakeven at 14% is ≈AMD 200–203M of receipts for mid-range capex, ≈107M for lean and ≈364–375M for flagship.** The 10-year breakevens are ≈145M, ≈60M and ≈257–262M. At the model-wide AMD 18M rent, the mid 5-year breakeven rises to ≈216M (ESTIMATE, §3.11).
   - At mid capex and G = AMD 100–140M, **TT minus VAT 5-year NPV is −15 to −19M** with the refund at t=0, or −11 to −14M if the refund is 12 months late. The 10-year NPV is roughly break-even (−9 to +3M), and that assumes TT survives for 10 years (item 5, §4.2).
   - *Fact-check correction (downgraded): the original breakevens (≈186M mid, ≈86M lean, ≈344M flagship; ≈132M, ≈53M, ≈242M over 10 years) discounted the capex-VAT refund by a full year (t=1) without saying so. §3.11 keeps them as a "refund delayed 12 months" scenario for a new company flagged as "risky" under Art. 74(5).*
   - The decision is sticky. Moving from VAT to TT **claws back 20% of the net book value** of assets on which VAT was recovered (Art. 73(14), VERIFIED). You therefore **cannot harvest the capex VAT and then switch**.
5. **Multi-unit chain: stay on catering TT.** The catering path has no cap and lifts the related-party ban. At an illustrative 5 units × AMD 300M, TT saves about **AMD 98M a year** against roughly AMD 180M of capex VAT forgone, so payback is under 2 years (ESTIMATE).
   - **Policy risk: the Government has said it intends to abolish turnover tax.** In June 2024 PM Pashinyan said "the turnover tax should be completely abandoned in Armenia… step by step", in favour of a unified tax system. The Ministry of Finance called TT an "extraordinary favourable treatment" (REPORTED, ARKA, 6 Jun 2024 [23]). No 2027 amendment to Arts 253–265 has been enacted yet; the consolidated notes show only the HO-83-N and HO-385-N exclusions.
   - **Treat TT surviving more than 2–3 years as a key risk.** If TT ends early, the capex VAT forgone at the start cannot be recovered, except possibly gradually under Art. 73(4)(2) (unverified). At G ≤ AMD 200M, TT takes about 3–7 years to repay that VAT.
   - *Fact-check correction: the original treated TT only as a "policy-dependent concession", did not cite the stated abolition policy, and used 10-year NPVs that assume TT survives 10 years.*
   - **Trap:** once the catering declaration is filed, **all non-catering income is taxed at 20% of turnover** (Art. 258 row 7, VERIFIED). This covers retail bags of beans, merchandise, rent and similar.
   - Put any retail, roastery, wholesale or franchising activity in a **separate VAT-registered entity**.
6. **Profit tax and payout rules** (VERIFIED) [1]:
   - Profit tax **18%**, paid by 20 April. Quarterly advances are the lower of 20% of last year's tax and 2% of last quarter's revenue; there are none in the year of registration.
   - Tax losses carry forward **5 years**.
   - **Dividend withholding is 5%** for resident and non-resident individuals and for non-resident companies. **Dividends received by resident companies are deductible**, so they are effectively untaxed (Art. 123(2)(1)).
7. **Tax depreciation, minimum straight-line lives** (VERIFIED, Art. 121):
   - **buildings and structures** (including linear utility infrastructure) **20 years**;
   - **production equipment 5 years**; production lines and robotics 3; **computers and communications 1**; **other fixed assets 8**.
   - Vehicles have no row of their own, so they fall under "other", 8 years. This is my reading; confirm with SRC.
   - Assets **up to AMD 50,000 are expensed immediately**.
8. **Property tax is now at 100% of cadastral value** (the phase-in was 75% in 2025) (VERIFIED, Art. 229, 233(7)).
   - Rates: **public-purpose (service) buildings 0.3% a year**; unimproved settlement land 1%; industrial land 0.25%; energy, transport and utility land 0.5%. Companies pay half-yearly (1 June, 1 December).
   - For a mid-range site this is about **AMD 0.9–1.8M a year if the company owns the plot, or AMD 0.3–0.45M (building only) if the land is leased** (ESTIMATE, §3.8). Cadastral values were not obtained.
   - *Fact-check correction: the original "AMD 0.4–0.9M" did not match §3.8's own table (≈0.4–0.65M). That table also valued the land at AMD 2,000–8,000/m², far below B4's market evidence for Kotayk suburban plots ($66–150/m² ≈ AMD 24,000–54,000/m²).*
9. **Local and road levies are small but site-specific.**
   - Abovyan community (Kotayk) 2025 draft rates [18] (REPORTED): catering permit **AMD 18,000 a quarter** for 100–200 m²; **operating after 24:00, AMD 100,000 a year**; outdoor advertising **AMD 1,500 per m² per month**; waste fee **AMD 50 per m²**.
   - Advertising boards on the **interstate M-4 outside settlement limits** pay state **road tax of AMD 10,000 per m² per year** instead (VERIFIED, Art. 190).
10. **Fiscal compliance is strict and getting stricter** (VERIFIED, Art. 380–381, 416; HO-309-N; Government Decision 125-N; HO-376-N).
    - A registered cash register (HDM) is mandatory for cash and card sales. Fines: **AMD 500,000** for having no registered HDM at the point of sale; **AMD 200,000 plus 0.5% of the prior quarter's HDM turnover (cap AMD 10M)** for each rule breach.
    - **e-HDM becomes mandatory from 2027** in sectors the Government will define.
    - **Coffee and tea have been under Data Matrix product marking since 1 Mar 2025, and dairy since 1 Jan 2026.**
    - The late-payment penalty rose to **0.075% a day** from 2025.
    - I could **not** verify that a receipt lottery or cashback scheme operates in 2026.
11. **No investment incentive applies to a café.**
    - The VAT deferral for imported equipment under Government-approved programmes was **repealed in Dec 2021** (HO-383-N).
    - The profit-tax reduction for approved business programmes was **repealed in May 2024** (HO-145-N). Both repeals VERIFIED.
    - Free-economic-zone benefits apply only to operators inside a zone, and I found **no Kotayk or Gegharkunik regional tax relief** in the Tax Code.
    - Customs duty is 0% on commercial coffee machines and 10% on refrigeration; import VAT is 20%. These are recoverable only by a VAT payer (REPORTED) [21][22].
12. **Set-up is cheap and fast** (VERIFIED) [13][17][20].
    - LLC registration is **free and immediate** online for RA citizens using the standard charter, or **2 business days** with a custom charter. A trade name containing "Armenia" or "Hay" costs **AMD 600,000 a year**.
    - National trademark duties: about **AMD 120,000 for one class and AMD 150,000 for three classes**; renewal AMD 120,000.
    - Madrid filing: **CHF 653 basic fee** (CHF 903 in colour), plus CHF 100 per standard designation or the country's individual fee, plus an AMD 30,000 handling fee at the Armenian office.

---

## 2. Key data table

| # | Metric | Value | Period / effective | Status | Source |
|---|---|---|---|---|---|
| 1 | VAT standard rate | 20%; VAT inside a VAT-inclusive price = 16.67%. A VAT payer issuing only an HDM receipt is deemed to include VAT at 16.67% | 2026 | VERIFIED | [1] Art. 63 |
| 2 | VAT registration threshold | AMD 115M turnover (prior or current year). If exceeded mid-year, VAT is due **only on the excess**. Voluntary registration is allowed | 2026 | VERIFIED | [1] Art. 59, 254(2) |
| 3 | VAT return and payment | Monthly; return due by the 20th of the following month | 2026 | VERIFIED | [1] Art. 69, 75 |
| 4 | VAT on catering / food | No exemption or reduced rate for catering or food (Art. 64 checked) | 2026 | VERIFIED | [1] Art. 64 |
| 5 | Excess input VAT | Credited to the taxpayer's unified tax account, from which it can be refunded. Credited automatically by the payment deadline if the taxpayer is not "risky" under Government criteria; otherwise only after an inspection or desk review | 2026 | VERIFIED | [1] Art. 74 |
| 6 | Input-VAT block on passenger cars | No recovery on light passenger cars bought or leased after 1 Aug 2025, unless the car is rented out | from 1 Aug 2025 | VERIFIED | [1] Art. 72(1)(11)–(12) |
| 7 | Corporate profit tax | 18% (individual entrepreneur on the general regime: 23%) | 2026 | VERIFIED | [1] Art. 125 |
| 8 | Profit-tax advances | Each quarter: min(20% of prior-year profit tax; 2% of prior-quarter revenue), due the 20th of the quarter's last month. None in the year of registration | 2026 | VERIFIED | [1] Art. 135 |
| 9 | Profit-tax return and payment | By 20 April of the following year | 2026 | VERIFIED | [1] Art. 134, 136 |
| 10 | Loss carry-forward | 5 years, oldest losses used first; no carry-back | 2026 | VERIFIED | [1] Art. 123(1)(4) |
| 11 | Tax depreciation, minimum lives (straight line, monthly pro-rata) | Buildings and structures (incl. utility lines) 20 y; hotels and education buildings 10 y; production equipment 5 y; production lines and robotics 3 y; computers and telecoms 1 y; other fixed assets 8 y | 2026 | VERIFIED | [1] Art. 121(1)(3) |
| 12 | Low-value asset write-off | Assets ≤ AMD 50,000 expensed in the year of purchase | 2026 | VERIFIED | [1] Art. 121(2)(1) |
| 13 | Turnover tax: catering | **12% of receipts − 9% of documented direct, admin and selling expenses; floor 3.5% of receipts;** unused deduction carried forward | Yerevan from 1 Jan 2025; **rest of Armenia from 1 Jan 2026** | VERIFIED | [1] Art. 258; [2] Art. 12, 16(6); [3] |
| 14 | TT on non-catering income of a "catering-declared" payer | 20% of turnover | 2025+ | VERIFIED | [1] Art. 258 row 7, (8) |
| 15 | Other TT rates | Trade 10% (− 9.5% of costs, floor 1%); production 7% (− 5%, floor 3%); rent, interest, royalties 10%; other 10% (− 6%, floor 4.5%) | 2025+ | VERIFIED | [1] Art. 258 |
| 16 | Old catering TT (superseded) | Flat 6% of turnover, no expense credit | to 31 Dec 2024 in Yerevan; to 31 Dec 2025 outside | VERIFIED | [2] Art. 16(6); [15] |
| 17 | TT eligibility | Prior-year turnover ≤ AMD 115M; related parties excluded. **Catering declaration lifts both limits.** Banks and similar bodies excluded | 2026 | VERIFIED | [1] Art. 254 |
| 18 | TT timing | Declaration by 20 Feb, or within 20 days of state registration. Within 20 days of exceeding AMD 115M, file the catering declaration to remain on TT. Quarterly returns and payment by the 20th of the following month | 2026 | VERIFIED | [1] Art. 254, 255, 259, 261, 262 |
| 19 | Moving from VAT to a special regime | VAT previously recovered on fixed assets is reversed: **20% × net book value** (applies to assets bought after 1 Jul 2024) | 2025+ | VERIFIED | [1] Art. 73(14); [2] Art. 4, 16(4) |
| 20 | Moving from TT to the general regime | Unused TT expense deductions × 10 (catering) become deductible against gross income. Fixed-asset VAT appears recoverable gradually at 16.67% × each period's tax depreciation | 2025+ | VERIFIED (first) / ESTIMATE (second: my reading) | [1] Art. 264(4), 73(4)(2) |
| 21 | Micro-entrepreneurship | Turnover ≤ AMD 24M. Exempt from all state taxes except import taxes, PIT withholding, excise, environmental and road tax. **Catering is excluded only inside Yerevan** | 2025+ | VERIFIED | [1] Art. 266–269 |
| 22 | Dividend tax | 5% for resident and non-resident individuals; 5% WHT for non-resident companies; resident companies may deduct dividends received (0%). Bank dividends 15% from 1 Feb 2027 (not relevant) | 2026 | VERIFIED | [1] Art. 150(8), 125(4)(3.1), 123(2)(1); [8] |
| 23 | WHT on other payments to non-residents | Passive income (royalties, interest) 10%; other Armenian-source income 20% (before any treaty relief) | 2026 | VERIFIED | [1] Art. 125(4) |
| 24 | Personal income tax on wages | 20% flat | from 2023 | VERIFIED | [1] Art. 150(1) |
| 25 | Funded-pension social payment (employee, withheld) | 5% of salary ≤ AMD 500,000 a month; 10% − AMD 25,000 above that; base capped at 15 × minimum wage | 2026 | VERIFIED | [14] Art. 6 |
| 26 | Rent paid to individuals | 10% PIT withheld by the tenant company (+10% on the landlord's annual rent above AMD 60M) | 2026 | VERIFIED | [1] Art. 150(7) |
| 27 | Property tax rates (annual) | Public-purpose buildings 0.3%; production buildings 0.25%; unimproved land: settlement 1% (residential 0.6%), industrial 0.25%, energy, transport and utility 0.5%; agricultural land 15% of notional net income | 2026 | VERIFIED | [1] Art. 229 |
| 28 | Property tax base and phase-in | Market-approximated cadastral value, revalued every 3 years; **100% of value from 2026** (25%, 30%, 35%, 50%, 75% in 2021–25); companies pay half-yearly by 1 Jun and 1 Dec | 2026 | VERIFIED | [1] Art. 228, 233(7), 236 |
| 29 | Road tax on roadside advertising | Interstate roads AMD 10,000 per m² per year; republican and regional roads AMD 7,500; empty boards 25%; outside settlement transit sections | 2026 | VERIFIED | [1] Art. 186–190, 195 |
| 30 | Abovyan local duties (2025 draft) | Catering permit per quarter, inside main buildings: ≤26 m² 5,000; 26–50 m² 8,000; 50–100 m² 12,000; **100–200 m² 18,000**; 200–500 m² 25,000; >500 m² 50,000 (temporary structures 1,000–25,000). **Night operation after 24:00: AMD 100,000 a year (catering).** Alcohol sales: 6,500–45,500 per quarter by area. Outdoor ads: 1,500 per m² per month. Summer or winter terrace on public land: 10,000 per m² per season | 2025 | REPORTED (official draft; adoption not checked) | [18] |
| 31 | Abovyan waste fee (2025 draft) | Trade and catering buildings: AMD 50 per m² of total area (the period is not stated in the annex; likely monthly) | 2025 | REPORTED | [19] |
| 32 | HDM fines | No registered HDM at the point of payment: AMD 500,000. Each rule breach: AMD 200,000 + 0.5% of prior-quarter HDM turnover (≤ AMD 10M). Tampering through integrated software: AMD 5M + a turnover share | 2026 | VERIFIED | [1] Art. 416 |
| 33 | e-HDM | Government to set sectors where e-HDM is mandatory; **AMD 500,000 fine** for trading without it where required | from 1 Jan 2027 | VERIFIED | [6] Art. 8, 12 |
| 34 | Product marking (Data Matrix) | Coffee (HS 0901) and tea from 1 Mar 2025; dairy (0401–0406), ice cream (2105) and some drinks from 1 Jan 2026. Retailers must scan marks at the HDM | 2025–26 | VERIFIED | [11]; [1] Art. 381(3.1) |
| 35 | Late-payment penalty | 0.075% a day (≈27% a year) | from 1 Jan 2025 | VERIFIED | [10]; [1] Art. 401 |
| 36 | Environmental tax on imported plastic packaging and tableware | 2% (HS 3923, 3924) | 2026 | VERIFIED | [1] Art. 171 |
| 37 | Customs duty (EAEU CET) | Commercial coffee machines (8419 81 200 0) 0%; other refrigeration and ice makers (8418 69 000 8) 10%; display counters 10%; dishwashers 0% (more in C2). EAEU-origin goods are duty-free | 2026 | REPORTED | [21]; C2 §2 |
| 38 | Import VAT | 20% at customs, or self-assessed for EAEU imports; recoverable only by VAT payers | 2026 | VERIFIED | [1] Art. 59(5)–(6), 63, 77 |
| 39 | Investment incentives | VAT deferral on imported equipment for investment programmes: **repealed** (HO-383-N, Dec 2021). Profit-tax reduction for Government-approved business programmes: **repealed** (HO-145-N, May 2024; existing projects grandfathered) | 2022 / 2024 | VERIFIED | [8][9] |
| 40 | LLC registration | **Free**; immediate with the standard charter, otherwise 2 business days; online for RA citizens via YesEm; ≤49 participants; name reservable for 6 months | Oct 2026 | VERIFIED | [17] |
| 41 | "Armenia" or "Hay" in a trade name | AMD 600,000 a year | Oct 2026 | VERIFIED | [17] |
| 42 | National trademark state duty | Base duty AMD 1,000. Filing 30×, examination 40× (+15× per extra class), registration 50×, renewal 120× (+10× per extra class). **1 class AMD 120k; 3 classes AMD 150k** (ESTIMATE from the coefficients) | 2026 | VERIFIED | [13] Art. 8, 18(4) |
| 43 | Madrid Protocol | WIPO basic fee CHF 653 (B/W) or 903 (colour); complementary fee CHF 100 per designation, or the individual fee where a party has one; supplementary CHF 100 per class beyond 3. Armenian office handling fee AMD 30,000; Armenia's individual fee when designated AMD 100,000 (+10,000 per class) | WIPO schedule in force 1 Feb 2023; State Duty law 2026 | VERIFIED | [20]; [13] Art. 18(4)(իբ)–(իգ) |
| 44 | Effective TT rate, illustrative café | 5.2% of receipts (AMD 150M case) and 6.25% (AMD 300M case) at AMD 6M land rent; **4.5% and 5.9% at the model-wide AMD 18M rent**. If wages (and rent) are *not* deductible: 7.4–8.3% (computed at 6M rent). *Fact-check correction: rent basis aligned with C6/B4.* | 2026 rules | ESTIMATE | §3.11 |
| 45 | Capex VAT forgone under TT | ≈ AMD 36M per mid-range unit (20% × ≈180M ex-VAT); ≈18M lean; ≈74M flagship | 2026 | ESTIMATE | C1, C2 capex × 20% |
| 46 | Stamp duty (military insurance fund), employee | AMD 1,000 a month for gross ≤ AMD 1,000,000; AMD 15,000 above. *Fact-check correction: replaces the unverified "AMD 1,500–15,000 by band".* | from Dec 2025 | REPORTED | [24]; C3 |
| 47 | Universal health insurance (UHI) | Employee premium withheld: AMD 0 (gross ≤ 200k), 4,800 (200–500k), 10,800 (> 500k) a month. **Draft employer levy AMD 4,400 a month per employee earning ≤ AMD 200k**, from the Dec-2026 payroll if adopted | from Dec 2025 (draft: Dec 2026) | REPORTED (levy: draft) | [24]; C3 |
| 48 | Turnover-tax policy outlook | Government's stated aim (June 2024) to abandon TT "step by step" for a unified tax system. No amendment to Arts 253–265 enacted for 2027 | 2024 statement; Oct 2026 status | REPORTED | [23]; [1] |

---

## 3. Detailed findings and analysis

### 3.1 Sources and legal status

- **Primary text.** The arlis.am "official incorporation" of the Tax Code (Law HO-165-N of 4 Oct 2016) [1], retrieved 2026-10-10. It references amendments up to **HO-440-N of 27 Aug 2026**.
  - Where arlis shows an article with a note that a later law takes effect from 2027, I read that amending law ([4][6][7]) to separate 2026 law from 2027 law.
  - Empty numbered points such as "8)" or "1.1." in the consolidated text are 2027 insertions that are not yet in force.
- **2027 changes already enacted.** None of these changes the catering TT economics:
  - HO-83-N: e-commerce platforms excluded from TT and micro, from 1 Jan 2027.
  - HO-385-N: bank dividends taxed at 15%, and bank shareholders barred from TT and micro, from 1 Feb 2027.
  - HO-309-N: e-HDM regime from 1 Jan 2027.
  - HO-391-N: realtor and property-manager rules from 1 Jun 2027.
- **Source conflict.** The SRC's explanatory page "About turnover tax" [15] still lists catering TT at **6%**, trade at 5% and production at 3.5%. It was last updated on 6 Oct 2022 and is overtaken by HO-285-N. *Fact-check: source unreachable on 10 Oct 2026; treat as unverified.*
  - **I trust the arlis consolidated text and the amending law** because they are the legal acts themselves. The SRC page is only guidance.
  - Online articles or bank guides citing "6% turnover tax for restaurants" should be treated as obsolete for 2026.

### 3.2 Legal form and set-up

| Option | Liability | Tax on profits | Distribution to owner | Fit for this project |
|---|---|---|---|---|
| **LLC (ՍՊԸ)** | Limited | TT (replaces VAT + profit tax) or VAT + 18% profit tax | 5% dividend tax (0% to a resident HoldCo) | **Recommended.** Allows outside investors (≤49 participants), share pledges and a later chain structure |
| CJSC (ՓԲԸ) | Limited | Same as LLC | Same | For a larger investor base or share classes; more governance overhead |
| Individual entrepreneur (ԱՁ) | **Unlimited** | TT plus a flat AMD 5,000/month final profit tax (Art. 125(3)); or 23% profit tax on the general regime | No dividend tax | Cheapest for an owner-operator. Unsuitable for an investor-funded, capex-heavy site |
| Micro-entrepreneur | Either form | Exempt (≤ AMD 24M turnover) | — | Irrelevant: a drive-thru would pass AMD 24M within 1–2 months |

**Registration** (VERIFIED [17]):
- An LLC is registered free of charge through e-register.am. It is "immediate" with the system's standard bylaws, or takes 2 business days with custom bylaws.
- The online flow is for RA citizens with YesEm e-ID. Foreign founders file through the State Register (in person or by power of attorney). Timing for that route was not verified.
- A beneficial-ownership declaration is part of the e-register service set.
- The **State Duty Law contains no current fee line for registering a commercial company**. Art. 16 points 1–1.5 and 1.7–1.9 were repealed by HO-41-N of 19 Jan 2021 [13], which is consistent with "free" on e-register.
- Later charter amendments cost 10 × base duty (**AMD 10,000**); participant changes cost 20× (**AMD 20,000**) [13] Art. 16(1.12).
- **Tax registration** is automatic on state registration. The **TT declaration must be filed within 20 days of registration** (Art. 254(1)(2)). Missing it makes the company a VAT payer for the rest of the year (Art. 59(1)(2)).

**Group structure for investors and a chain** (ESTIMATE, based on VERIFIED rules):
- A resident **HoldCo LLC** owns the OpCo LLC(s).
- OpCo-to-HoldCo dividends are deductible for the HoldCo (Art. 123(2)(1)) and carry no withholding, because Art. 132 withholds only for non-residents. HoldCo-to-individual dividends pay 5%.
- A foreign HoldCo would also suffer 5% WHT (Art. 125(4)(3.1)). Treaty relief was not researched.
- **Do not route brand royalties or management fees to a foreign related party without advice.** They attract 10% (royalties) or 20% (services and other income) WHT, and transfer-pricing documentation if the thresholds are met.

### 3.3 VAT (general regime)

- **Rate and registration** (VERIFIED, Art. 63, 59):
  - Rate 20%. B2C receipts carry VAT at 16.67% of the price.
  - Registration is compulsory above AMD 115M turnover. When the threshold is crossed mid-year, VAT applies to the part above it (Art. 59(1)(5)). Voluntary registration is possible (Art. 59(1)(4)).
- **No catering relief.** Art. 64 has no exemption for food or restaurant services (VERIFIED by reading the full article).
- **Input VAT recovery** (VERIFIED, Art. 71–74):
  - VAT on purchases and imports used in taxable supplies is creditable. Capex VAT is credited in the period of purchase.
  - Any excess becomes a refundable amount: credited to the unified account automatically if the company is not flagged as risky, otherwise after a desk or field audit (Art. 74(4)–(5)).
  - Blocked: VAT on cars bought after 1 Aug 2025 (Art. 72(1)(11)) and VAT on inputs attributable to special-regime activity.
- **Practical leakage under the VAT regime** (ASSUMPTION): many Armenian dairy farms, bakeries and small contractors are themselves on turnover tax, so their invoices carry no recoverable VAT. I assume 85% of food COGS comes from VAT payers.
- **Reporting** (VERIFIED, Art. 69, 75): monthly VAT return by the 20th of the following month.

### 3.4 Profit tax, depreciation and losses

- **Rate** (VERIFIED, Art. 125): 18% for resident companies. Individual entrepreneurs on the general regime pay 23% (Art. 125(3.1)).
- **Advances** (VERIFIED, Art. 135): quarterly, the lower of 20% of last year's tax and 2% of last quarter's revenue.
  - None are due in the year of registration, or by companies that were not VAT payers the previous year (Art. 135(5)).
  - A TT company pays none (Art. 263(2)).
- **Depreciation** (VERIFIED, Art. 121):

| Asset group (Art. 121(1)(3)) | Min. life | Drive-thru examples |
|---|---|---|
| Buildings, structures, linear utility infrastructure (power, water, sewer, gas lines) | 20 y | Building shell, canopy, lanes and paving (as "structures"), site utilities |
| Hotels, sanatoria, education buildings | 10 y | n/a |
| Production equipment | 5 y | Espresso machines, ovens, refrigeration, dishwashers |
| Production lines, robotics | 3 y | Possibly automated beverage systems (classification risk) |
| Computers and communication equipment | 1 y | POS terminals, KDS screens, headsets, routers |
| Other fixed assets | 8 y | Furniture, signage, vehicles (my reading, since vehicles have no own row) |

- Further depreciation rules (VERIFIED):
  - A company may choose **longer** lives, never shorter.
  - Items **≤ AMD 50,000 are expensed** (Art. 121(2)(1)).
  - Capital improvements on leased property are depreciated over the group minimum life, or the lessor's remaining period (Art. 121(3)(2)).
  - Land is not depreciable.
- **Losses** (VERIFIED, Art. 123(1)(4)): carried forward **5 years**, oldest first, with no carry-back. A capex-heavy unit that is loss-making in years 1–2 under the VAT regime should use its losses by year 7 at the latest.
- **Food-waste limits** (VERIFIED, Art. 122(3)):
  - Documented "quality losses" (expired goods) are deductible only up to **1% of gross income**, or **2% for marked dairy and ice cream** (HS 0401–0406, 2105).
  - Under the VAT regime, input VAT on non-deductible losses must be reversed (Art. 73(6)).
  - **Model waste above 1–2% as non-deductible.**

### 3.5 Turnover tax: the catering path in detail

**Statutory mechanics** (VERIFIED, Art. 253–265 as of Oct 2026):

1. **What TT replaces** (Art. 253(2)): for a resident commercial company, TT replaces **both VAT and profit tax**. For budget accounting, 40% of TT is treated as profit tax and 60% as VAT.
   - The company still withholds PIT and pension contributions, and pays property, land, local, environmental and road taxes and import VAT (Art. 263).
2. **Who can use it.**
   - The **general path** (Art. 254(1)–(3)) requires resident commercial companies whose prior-year turnover was ≤ AMD 115M. Related parties, joint-activity parties, banks and similar bodies are excluded.
   - The **catering path** (Art. 254(6)–(7)) is available to resident companies "engaged in public catering" that **do not** meet those conditions. They file the catering declaration and note which condition they fail. It works "regardless of the restrictions of this chapter", except the banking/financial and legal/accounting exclusions.
   - A catering TT payer whose turnover passes AMD 115M during the year stays on TT if it files the catering declaration **within 20 days** (Art. 254(7)).
   - "Public catering" means alienation of culinary products, **including with delivery**, or the organisation of their consumption, plus directly related goods and services (Art. 254(8)).
3. **Rates and formula** (Art. 258, as replaced by HO-285-N and amended by HO-72-N):
   - **Catering receipts:** `TT = 12% × Rc − 9% × E`, floored at `3.5% × Rc`.
     - *E* = expenses incurred **in the quarter**: direct production and service costs (materials, **staff wages**), **administrative** costs (management wages, accounting, IT, training, communications) and **selling** costs (packaging, storage, transport, **advertising and marketing**).
     - E must be documented by tax invoices, HDM receipts showing the buyer's TIN, settlement documents, or the "other documents" allowed by Art. 55(12)–(13). Those cover payroll, taxes and bank fees, and contracts with individuals.
     - Excluded from E: purchase or construction of fixed or intangible assets, **capital and current costs on fixed assets**, depreciation, business trips, representation, and gratuitously received items (Art. 258(6)(2)).
     - **Unused deductions carry forward without limit** (Art. 258(7)).
   - **Non-catering income** of a catering-declared payer: **20%** of turnover, with no deduction (Art. 258 row 7, (8)).
4. **Filing and payment:** quarterly return and payment by the 20th of the month after the quarter (Art. 259, 261, 262). Admin and selling costs must be tracked separately for each activity, or allocated by revenue weights (Art. 260(3)).
5. **Effective dates** (HO-285-N Art. 16; HO-72-N Art. 9):
   - The new formula applies from 1 Jan 2025 in Yerevan and **from 1 Jan 2026 elsewhere**.
   - Admin and selling costs became deductible for expenses from 1 Jan 2025.
   - Before that, catering TT was a flat 6%.

**Effective-rate ladder.** Rate = max(12% − 9% × e, 3.5%), where e = documented E ÷ catering receipts (ESTIMATE):

| e (E ÷ receipts) | 50% | 60% | 70% | 80% | 90% | ≥94.4% |
|---|---|---|---|---|---|---|
| Effective TT | 7.5% | 6.6% | 5.7% | 4.8% | 3.9% | 3.5% (floor) |

**Interpretation risks to confirm with SRC** (ASSUMPTION):
- **(a) Wages and land rent.** My reading is that wages are deductible: Art. 258(6)(1) points to Art. 121(7) "direct costs", which explicitly include the pay of staff in service processes, and to Art. 55(12) documents, which cover payroll. Land rent paid to an individual should also be deductible via Art. 55(13).
  - If SRC disagrees, the effective rate rises to about **7.4% (A) or 7.7% (B)** without wages, and about **8.2–8.3%** without wages, rent and utilities.
  - The TT regime still beats the VAT regime on recurring cash, but by a smaller margin: about AMD 3.3M a year in Case A and AMD 15.3M in Case B (ESTIMATE).
  - *Fact-check note: 3.3 / 15.3 is the worst case (no wages, rent or utilities). With only wages disallowed, the margin is ≈4.5 / 17.1. All of these use AMD 6M rent. At mid capex, a 3.3M-a-year margin takes about 11 years to repay the ≈36M of capex VAT forgone.*
- **(b) Fixed-asset costs.** Utilities and cleaning are deductible, but maintenance contracts on equipment fall under the "costs on fixed assets" exclusion.
- **(c) Retail-type products.** Bottled water and packaged snacks sold through the window are probably "catering" if they are part of the catering service. Bags of coffee beans, mugs and gift cards are probably not, and would be taxed at 20%.

**Who TT does not suit:**
- Businesses with large B2B or corporate catering sales: buyers cannot reclaim VAT, but that does not matter for B2C.
- Businesses with large non-catering revenue (the 20% row).
- Businesses whose capex VAT (one-off) outweighs the recurring saving (§3.11).

**Regime switching** (VERIFIED, Art. 59, 254, 255, 73(14), 264):
- Status is chosen per **tax year**. To leave the VAT regime, the TT declaration is filed by 20 Feb of the next year.
- **VAT → TT:** previously recovered VAT on assets held at the switch date is reversed in the last VAT return, equal to 20% of net book value for fixed assets and 20% of cost for inventory.
  - With 20-year building lives, roughly 95% of building VAT is clawed back after one year. **"Recover capex VAT in the construction year, then switch to TT" therefore yields only a timing benefit** of about one year's use of AMD 36M, worth about AMD 5M at 14% (ESTIMATE). It also carries audit risk.
  - *Fact-check note: the 5M figure leaves out the VAT that is kept for good after one year of depreciation: ≈5% of building VAT, ≈20% of equipment VAT and 100% of IT VAT, about AMD 3M more. That makes ≈AMD 8M in total, and only if the company runs a full year on the VAT regime.*
- **TT → VAT:**
  - Unused TT expense deductions × 10 become a profit-tax deduction in the switch period (Art. 264(4)).
  - Fixed assets' tax basis continues with notional TT-period depreciation (Art. 264(2)).
  - Unrecovered VAT on those assets appears recoverable **gradually** at 16.67% × each period's tax depreciation once they serve VAT-able supplies (Art. 73(4)(2)(a), my reading).
  - This gives TT-first an **option value**: some capex VAT can still come back if the business later moves to VAT.

### 3.6 Micro-entrepreneurship

- Applies to resident companies and individual entrepreneurs with prior-year turnover ≤ AMD 24M (≈ USD 66k).
- **Catering is excluded only inside Yerevan's administrative boundaries** (Art. 267(5)(2), as amended by HO-285-N). An M4 site in Kotayk could technically qualify. *Fact-check note: the Nor Nork / Avan stretch of the M-4 is inside Yerevan, so a site there is excluded.*
- It is exempt from all state taxes except import taxes, **PIT and pension withholding on wages**, excise, environmental and road tax (Art. 269) (VERIFIED).
- The status ends the moment turnover passes AMD 24M (Art. 268(1)(2)). The company must then elect TT within 20 days or become a VAT payer.
- **Implication:** useful only for a seasonal pop-up or test kiosk. A drive-thru at AMD 100–300M a year (≈ AMD 0.3–0.8M a day) would breach the cap within the first 1–3 months (ESTIMATE).

### 3.7 Payroll taxes (for the opex model)

- **PIT:** 20% flat on gross wages (Art. 150(1)), withheld by the employer.
- **Funded-pension social payment** (VERIFIED, Funded Pensions law Art. 6) [14]:
  - **5%** of salary up to AMD 500,000 a month; **10% − AMD 25,000** above that; the base is capped at 15 × the minimum monthly wage.
  - At the AMD 75,000 minimum wage (REPORTED in A1), the cap is AMD 1,125,000 (ESTIMATE).
  - Withheld from the employee for persons covered by the mandatory scheme (born from 1974 onward, per Art. 5; not re-read in detail).
- **Employer-side contributions:** none in force in 2026, so employer cost ≈ gross wage (REPORTED; C3-labor.md §3.4).
  - **A draft universal-health-insurance (UHI) amendment would add an employer levy of AMD 4,400 a month for each employee earning ≤ AMD 200k gross**, from the Dec-2026 payroll if adopted. This is about AMD 53k per such employee a year (REPORTED, draft e-draft 10624; C3).
  - Model it as an employer-side cost from Dec 2026 or 2027.
- **Stamp duty (military insurance fund):** **AMD 1,000 a month** for gross pay up to AMD 1,000,000, and AMD 15,000 above that, from Dec 2025 (REPORTED, PwC Tax Summaries reviewed 30 Jun 2026 [24]; C3).
- **UHI premium (employee, withheld), from the Dec-2025 payroll:** AMD 0 for gross ≤ AMD 200k; **AMD 4,800 a month for AMD 200–500k**; AMD 10,800 above AMD 500k (REPORTED [24]; C3).
- **Model:** net pay = gross × 0.75 − AMD 1,000 − UHI premium (0 / 4,800 / 10,800 by band), for wages up to AMD 500k a month. The 0.75 factor is 1 − 20% PIT − 5% pension (ESTIMATE).
- *Fact-check correction: the original text set employer cost at gross with no employer-side levy and gave stamp duty as "roughly AMD 1,500–15,000 by wage band" (not verified). It left out health insurance and used net pay = gross × 0.75 − stamp duty. That was out of date and contradicted C3-labor.md.*

### 3.8 Property, land, local and road levies

**Property tax** (VERIFIED, Art. 224–238):
- The base is cadastral value approximated to market value, reassessed every 3 years.
- The 2021–2025 phase-in is complete, so **2026 and later = 100%** (Art. 233(7)).
- The tax goes to the community budget. Companies pay half the annual amount by 1 June and 1 December (Art. 229(2), 236).
- A drive-thru building is most likely a "public-purpose building" (Art. 227(2)(5): buildings serving the population), taxed at **0.3%**. This is my classification; confirm with the community or Cadastre.
- Unimproved land is 1% for settlement and public-construction land, 0.5% for transport and utility land and 0.25% for industrial land.
- **Open question:** the Tax Code lists land rates only for land "without improvements". How land under a building is taxed (included in the building's cadastral value, or at the land rate) needs a Cadastre answer. **Conservative model:** 0.3% × building cadastral value + 1% × land cadastral value.

Mid-range site (140 m² building, 2,500 m² plot, per C1). The cadastral values are ASSUMPTIONS:

| Item | Value | Rate | Annual tax |
|---|---|---|---|
| Building cadastral value (assume 70–100% of AMD 150M ex-VAT cost) | AMD 105–150M | 0.3% | AMD 315–450k |
| Land cadastral value, **if the company owns the plot**. Re-based on B4 asking prices for Kotayk suburban plots ($66–150 per m² ≈ AMD 24,000–54,000 per m²) × 2,500 m², since cadastral value approximates market value | AMD 60–136M | 1% | AMD 0.6–1.36M |
| **Total, land owned** | | | **≈ AMD 0.9–1.8M** (ESTIMATE) |
| **Total, land leased** (land tax falls on the landlord, though it may be passed through in rent) | | | **≈ AMD 0.3–0.45M** (ESTIMATE) |

*Fact-check correction: the original land row assumed AMD 2,000–8,000 per m² (AMD 5–20M, tax 50–200k), for a total of ≈AMD 0.4–0.65M. That conflicts with B4-alt-corridors.md, where Abovyan, Ptghni and Arinj ask $66–150 per m². Asking prices may overstate cadastral value, so get a Cadastre extract for the actual plot (gap 5).*

*Fact-check note on local duties (below): the Abovyan annex applies coefficients of 0.5–3.0 to villages in the enlarged community, e.g. Arinj ×3.0 on some lines and Ptghni / Verin Ptghni ×0.5–0.75. A site outside Abovyan town may pay different rates.*

**Local duties and fees** (REPORTED: Abovyan community, Kotayk, draft 2025 decisions on e-draft.am [18][19]; adoption and 2026 rates not checked):
- Local duty rates are set annually by each community council within the ranges of the Law on Local Duties and Fees. That law was not opened.
- Abovyan is the first larger community on the M4 out of Yerevan. Other M4 communities (Nor Hachn, Charentsavan, Hrazdan, Sevan) set their own rates.

| Levy | Abovyan 2025 draft rate | Mid-range drive-thru (ESTIMATE) |
|---|---|---|
| Catering permit (per outlet, quarterly, inside a main building) | 100–200 m²: AMD 18,000 a quarter | AMD 72,000 a year |
| Operating after 24:00 (catering, annual) | AMD 100,000 a year | AMD 100,000 if open 24/7 |
| Alcohol sale permit (if beer or wine is sold) | AMD 20,500 a quarter (100–200 m²) | AMD 82,000 a year (excluded in base case) |
| Outdoor advertising inside settlement limits | AMD 1,500 per m² per month (other ads) | 24 m² pylon (2 faces × 12 m²) ≈ AMD 432,000 a year |
| Seasonal terrace on community land | AMD 10,000 per m² per season | n/a for drive-thru |
| Waste collection fee (trade or catering building) | AMD 50 per m² (period not stated in annex; likely monthly) | 140 m² → AMD 84,000 a year if monthly |
| Building permit duty (public building ≤ 200 m²) | AMD 15,000 (Abovyan town) | One-off |

**Road tax on roadside advertising** (VERIFIED, Art. 186(1)(3), 187(4), 190, 195):
- Boards **on or within the right-of-way or protection zone of interstate roads (the M-4 is interstate; B1) outside settlement transit sections** pay state road tax of **AMD 10,000 per m² per year**. Republican and regional roads pay AMD 7,500; empty boards pay 25%.
- The tax is paid quarterly from the date of the road authority's technical-compliance act. The local duty does not apply there.
- A 24 m² pylon therefore costs about **AMD 240,000 a year** (ESTIMATE).
- Whether an on-premise **name sign** counts as "advertising" under the Law on Advertising is not verified; signboards are often treated separately.

### 3.9 Fiscal cash registers, e-HDM, product marking, receipt lottery

- **HDM is mandatory** for all cash and card settlements in retail and consumer services (Art. 380(1)). It must be registered with SRC at the outlet address and positioned where payment happens (Art. 381(1)–(2)). A receipt must be given to every customer (Art. 381(3), as amended by HO-309-N).
- **Fines** (Art. 416): **AMD 500,000** for having no registered, compliant HDM at the payment place. Each rule breach costs **AMD 200,000 + 0.5% of the prior quarter's HDM turnover, capped at AMD 10M**. Tampering via integrated POS software costs AMD 5M plus a turnover share. Wrong product or service codes earn a warning first, then AMD 50,000.
- **Drive-thru implication.** Payment usually happens at a pay window or by app pre-order. Every payment point (window, kiosk, app) needs its own registered HDM or a lawful **e-HDM** for online orders (Art. 380.1(1)).
- **e-HDM:**
  - Currently optional for web and app orders.
  - From **1 Jan 2027** (HO-309-N) the Government will define sectors where it is mandatory. Trading without it where required is fined **AMD 500,000**, and e-receipts become the legal transport and settlement document.
  - C2 found new-generation physical HDMs at AMD 60–125k each (REPORTED).
- **Data Matrix product marking** (Government Decision 125-N of 6 Feb 2025 [11]):
  - Coffee (HS 0901), tea and coffee extracts (2101) have been under marking **since 1 Mar 2025**; dairy (0401–0406), ice cream (2105) and some beverages since **1 Jan 2026**.
  - Buying marked inputs is automatic. **Retail resale** of marked packs (beans, bottled milk drinks) requires scanning at the HDM (Art. 381(3.1)), so the POS must support it.
- **Receipt lottery / cashback: not verified.**
  - I found **no receipt-lottery provision in the current Tax Code**.
  - Art. 18.1 (added by HO-376-N, in force Nov 2024) lets the Government set up "tax-administration support programmes" with public-control mechanisms. That is the legal basis such a scheme would use [10].
  - Whether one runs in 2026 is unknown. It would not change the business's tax, only customers' incentive to ask for receipts.

### 3.10 Customs duties and investment incentives

- **Customs duty** (REPORTED: EAEU CET via alta.ru [21]; full table in C2 §3). I re-checked two codes:

| HS code | Item | Rate |
|---|---|---|
| 8419 81 200 0 | Commercial coffee machines | **0%** |
| 8418 69 000 8 | Other refrigerating equipment | **10%** |

  - Imports from EAEU members (e.g., Russia) are duty-free; import VAT is self-assessed on an import tax declaration (Art. 77).
  - **Import VAT of 20% is a pure cost for a TT payer.** It must be paid at import and cannot be recovered (Art. 59(5), 72(1)(1)). Landed cost ≈ 1.30 × foreign price for 0%-duty items and ≈1.43 × for 10%-duty items (C2's ESTIMATE).
- **Environmental tax** of 2% on imported plastic packaging (3923) and tableware (3924) (Art. 171) applies if the company imports lids or cups itself.
- **Investment incentives** (VERIFIED):
  - Tax Code Art. 79 (VAT payment deferral on imports by Government-selected investment programmes) was **repealed by HO-383-N** (10 Dec 2021, in force 10 days after publication on 22 Dec 2021); approved projects were grandfathered [8].
  - Art. 127(1)–(2) (profit-tax reduction for Government-approved business programmes) and the related accelerated depreciation were **repealed by HO-145-N** (11 Apr 2024, in force 4 May 2024); existing approvals were grandfathered [9].
  - **Free economic zones:** exemptions (profit tax, property tax, VAT on supplies inside the zone) apply only to registered FEZ operators for activity inside a zone (Art. 64(2)(23), 126(7), 230). A roadside café is not a realistic FEZ project (ASSUMPTION).
  - **Kotayk and Gegharkunik:** searching the full Tax Code text for "border settlement" (սահմանամերձ) finds only mortgage-interest refunds and inspection rules. **There is no regional business-tax relief.**
  - Agricultural profit-tax exemption to 31 Dec 2026 (Art. 126(1)) is irrelevant.
  - **Customs-duty exemptions for "investment projects"** under EAEU or Government decisions (e.g., technological equipment not produced in the EAEU) were **not verified**. Catering is unlikely to qualify (ASSUMPTION; see Section 5).

### 3.11 Numeric regime comparison and recommendation

**Method** (ESTIMATE; calculation script reproduced in the gaps section):
- Menu prices are the same under both regimes; G = gross receipts paid by customers.
- Under the VAT regime the company keeps G/1.2, recovers input VAT, and pays 18% profit tax with Art. 121 depreciation and 5-year losses.
- Under TT it keeps G, pays supplier VAT as a cost, and pays catering TT on documented expenses as in §3.5.
- **Capex-VAT timing.** Under the VAT regime, capex VAT is credited during construction and refunded within 1–3 months if the company is not "risky" (§3.3, Art. 74). **The base NPV therefore books the refund at t=0.** Delays of 12 and 24 months (t=1, t=2) are run as risky-taxpayer scenarios under Art. 74(5).
  - *Fact-check correction: the original NPV table discounted the refund by a full year (t=1) without saying so, which moved results toward TT by about AMD 2–9M of NPV.*
- For G between the two cases, the NPV runs use payroll = 24 + 0.08 × G (straight line between Case A and Case B) and marketing at 4% of G. This rebuild reproduces the original t=1 table to within ±1 per cell; the flagship breakevens differ by 3–13M between rebuilds.

Cost inputs (all ASSUMPTION, aligned with C1/C2):

| Input | Value |
|---|---|
| Food COGS (ex-VAT) | 29% of G (≈35% of net-of-VAT sales, C2); 85% bought from VAT payers |
| Utilities (VAT-able) | 4% of G |
| Marketing and services (VAT-able) | 4% (Case A) / 3% (Case B) |
| Repairs (VAT-able; not TT-deductible) | 1.5% of G |
| Other admin | 2% of G, half VAT-able |
| Card acquiring (no VAT) | 1.4% of G |
| Land lease from an individual (no VAT) | **Model-wide assumption: AMD 18M a year** (C6 base AMD 1.5M a month; B4 placeholder AMD 1.3–1.8M a month = 15.6–21.6M a year). The original runs used AMD 6M; the tables below show both. The tenant withholds 10% PIT on rent paid to an individual (Art. 150(7)), so agree the rent gross. *Fact-check correction: 6M contradicted C6/B4. It understated rent by AMD 12M a year, which overstated the §3.11 cash lines by ≈AMD 10–11M a year after tax.* |
| Payroll (gross) | AMD 36M (Case A) / 48M (Case B) |
| Local duties and property tax | AMD 1M a year (land leased; ≈AMD 1.4–2.5M if the plot is owned, §3.8) |
| Capex (mid-range) | AMD 180M ex-VAT: 150M building and site, 27M equipment, 3M IT; **VAT 36M** |
| Tax depreciation | 15.9M in year 1, 12.9M from year 2 |
| Ramp-up | Year 1 75%, year 2 90%, years 3–5 100% |
| Discount rate | 14% (AMD) |

**Steady-state year (AMD million).** The rent 6 columns are the original runs. The rent 18 columns use the model-wide rent assumption (fact-check rebuild).

| | Case A: G = 150 (≈ USD 0.41M), rent 6 | Case A, rent 18 | Case B: G = 300 (≈ USD 0.83M), rent 6 | Case B, rent 18 |
|---|---|---|---|---|
| **VAT regime:** net VAT paid | 14.5 (9.7% of G) | 14.5 | 29.5 (9.8%) | 29.5 |
| VAT regime: profit tax | 1.1 | 0.0 (tax loss) | 10.7 | 8.5 |
| VAT regime: post-tax operating cash | 18.0 | 7.2 | 61.6 | 51.8 |
| **TT regime:** documented expenses ÷ G | 75% | 83% | 64% | 68% |
| TT paid | **7.9 (5.2% of G)** | **6.8 (4.5%)** | **18.7 (6.25%)** | **17.7 (5.9%)** |
| TT regime: post-tax operating cash | 25.7 | 14.8 | 83.1 | 72.2 |
| **Annual cash advantage of TT** | **+7.7** | **+7.7** | **+21.5** | **+20.4** |
| Economic tax burden at fixed menu prices: VAT regime | output VAT 25.0 + profit tax 1.1 = 17.4% of G | 25.0 + 0 = 16.7% | 50.0 + 10.7 = 20.2% | 50.0 + 8.5 = 19.5% |
| Economic tax burden: TT regime (incl. unrecoverable supplier VAT) | 7.9 + 10.5 = 12.3% of G | 6.8 + 10.5 = 11.5% | 18.7 + 20.5 = 13.1% | 17.7 + 20.5 = 12.7% |
| Capex VAT recoverable only under VAT | 36.0 | 36.0 | 36.0 | 36.0 |
| Years for TT savings to repay the forgone capex VAT (undiscounted) | 4.7 | 4.7 | 1.7 | 1.8 |

*Fact-check correction: against the model-wide rent, the post-tax cash lines at AMD 6M rent are overstated by about AMD 10–11M a year (AMD 12M of rent, less its tax effect). The TT advantage hardly changes at G = 150, because VAT-regime profit tax falls to zero, and falls from 21.5 to 20.4 at G = 300.*

**At the study's base revenue (C6: G = 140, payroll 35.2):** TT advantage is AMD 6.9M a year at rent 6 and 7.4M at rent 18, so repaying 36M of capex VAT takes 5.2 / 4.9 years. At G = 100 it is 5.3 / 6.1M (6.8 / 5.9 years) (ESTIMATE).

**5- and 10-year view: NPV at 14% of TT minus VAT, AMD million, by capex scenario (undiscounted in brackets).** Capex-VAT refund at **t=0**; land rent AMD 6M, as in the original runs (ESTIMATE, fact-check rebuild):

| Capex (ex-VAT, incl. equipment and IT) | Horizon | G = 100 | G = 140 | G = 150 | G = 200 | G = 250 | G = 300 | NPV-breakeven G, refund at t=0 (base) | Breakeven, refund 12 months late (t=1; original table) |
|---|---|---|---|---|---|---|---|---|---|
| Lean ≈ 91 (C1 lean 76.6 + equipment) | 5 y | −1 (+7) | +5 (+17) | +8 (+21) | +21 (+41) | +35 (+61) | +48 (+81) | ≈ 107 | ≈ 86 |
| | 10 y | +9 (+34) | +21 (+60) | +25 (+68) | +46 (+109) | +67 (+151) | +88 (+192) | ≈ 60 | ≈ 53 |
| Mid ≈ 180 | 5 y | −19 (−10) | −15 (−5) | −14 (−3) | −1 (+17) | +13 (+37) | +26 (+57) | **≈ 200–203** | ≈ 186 |
| | 10 y | −9 (+16) | −2 (+32) | +2 (+41) | +22 (+82) | +44 (+124) | +65 (+165) | ≈ 145 | ≈ 132 |
| Flagship ≈ 370 (C1 flagship 313.6 + equipment) | 5 y | −56 (−48) | −53 (−43) | −52 (−42) | −46 (−33) | −33 (−13) | −20 (+7) | **≈ 364–375** | ≈ 331–344 |
| | 10 y | −47 (−22) | −42 (−11) | −40 (−9) | −26 (+25) | −5 (+66) | +16 (+108) | ≈ 257–262 | ≈ 237–242 |

Positive values mean TT is better. The undiscounted figures do not depend on refund timing. Where a breakeven is given as a range, it spans the independent rebuilds (the original analysis, the fact-checker's and this revision's). The flagship results are the most sensitive to how capex is split between building and equipment.

*Fact-check correction (downgraded): the original table showed only G = 150–300 with the refund discounted a full year (t=1), without saying so. Its cells were: mid 5 y −9 / +4 / +17 / +30, breakeven ≈186; lean ≈86; flagship ≈344; 10 y ≈132 / ≈53 / ≈242. Those figures now appear only as the "refund 12 months late" column.*

**Breakeven sensitivity (receipts G at which 5-year / 10-year NPV of TT minus VAT = 0, AMD million; ESTIMATE):**

| Scenario | Lean | Mid | Flagship |
|---|---|---|---|
| Base: refund at t=0, rent 6M | 107 / 60 | 200–203 / 145 | 364–375 / 257–262 |
| Refund 12 months late (t=1): new company classed as "risky", Art. 74(5) | 86 / 53 | 186 / 132 | 331–344 / 237–242 |
| Refund 24 months late (t=2): refund only after a field audit | 73 / 46 | 171 / 105 | ≈ 311 / 222 |
| Model-wide rent AMD 18M, refund at t=0 | 95 / 60 | 216 / 129 | ≈ 389 / 275 |

**These NPVs assume TT lasts for the whole horizon.** The Government has stated that it intends to abolish TT (§4.2, [23]). If TT ends after 2–3 years, the capex VAT forgone at the start is not repaid at G ≤ AMD 200M, where undiscounted payback is about 3–7 years. Some of it might be recovered gradually under Art. 73(4)(2), but that is unverified. **Use the 5-year columns, not the 10-year ones, for the regime decision.**

**Chain illustration** (5 units × AMD 300M = AMD 1.5bn; HQ payroll 60M and services 20M added) (ESTIMATE):
- VAT regime: net VAT + profit tax = AMD 185M a year (12.3% of G).
- Catering TT: AMD 86M a year (5.75% of G; e ≈ 69%).
- **TT advantage ≈ AMD 98M a year**, against AMD 180M of capex VAT forgone across 5 units, so payback is under 2 years.

**Recommendations.**

**(a) Single unit: choose the regime on capex and revenue together.**
- *Fact-check correction: the original recommendation was "default: catering TT from day one for AMD 150–300M; VAT only if capex is flagship-level (≥ AMD 300M) and receipts are below ~250–340M". It contradicted the breakeven table above and ignored the study's base revenue (C6-benchmarks.md: AMD 100–150M, base 140M). On this file's own inputs, mid capex at G = 100–140M gives a TT-minus-VAT 5-year NPV of −11 to −14M with the refund 12 months late, and −15 to −19M with the refund at t=0.*

| Capex (ex-VAT) | Steady-state receipts | Regime with better 5-year NPV (refund at t=0) | Margin and comment |
|---|---|---|---|
| Lean ≈ AMD 91M | above ≈ AMD 110M | Catering TT | +5 to +8M at 140–150M; near neutral at 100M |
| **Mid ≈ AMD 180M** | **below ≈ AMD 200M** (≈216M at AMD 18M rent). This includes the C6 base of 100–150M | **VAT regime** | VAT ahead by ≈AMD 14–19M at 100–150M. The 10-year result is roughly break-even (−9 to +2) and holds only if TT survives 10 years |
| Mid ≈ AMD 180M | above ≈ AMD 200–215M | Catering TT | +13M at 250M; +26M at 300M |
| Flagship ≈ AMD 370M | below ≈ AMD 365–390M | VAT regime | |

- **Before choosing VAT at mid capex, price these factors explicitly. They can tip the result either way:**
  - *Against VAT:* refund risk for a new, pre-revenue company classed as "risky" under Art. 74(5). A 12- or 24-month delay lowers the mid 5-year breakeven to ≈186M or ≈171M. There is also monthly VAT compliance cost, and the one-way switching cost under Art. 73(14).
  - *Against TT:* the Government's stated aim to abolish TT (§4.2). There is also the risk that SRC disallows wages, which would raise TT to ≈7.4–8.3% of receipts (§3.5), and the 20% rate on any non-catering income.
  - *For TT:* the option value of a later move from TT to VAT, with gradual capex-VAT recovery under Art. 73(4)(2) (unverified).
  - "16.67% VAT inside every menu price" is **not** an extra argument for TT. The NPVs already assume the same menu prices under both regimes.
- **Deadlines under either choice:**
  - If TT: file the TT declaration within 20 days of LLC registration.
  - File the **catering** declaration within 20 days of passing AMD 115M. Diarise it: missing it turns the company into a VAT payer on the excess for the rest of the year.
  - If VAT: register before the first capex invoices, so that construction VAT is creditable.
- Treat **"VAT during construction, TT afterwards" as worth only about AMD 5M of timing**, plus ≈AMD 3M of VAT kept for good if the company runs a full year on VAT (§3.5). It is not a real arbitrage.

**(b) Multi-unit chain.**
- **Stay on catering TT** in each operating company. It is uncapped, available to related parties, and does not charge 18% profit tax.
- Keep **non-catering revenue** (retail beans, merchandise, franchise fees, sub-leases, EV charging) **out of the TT company**: under the catering declaration it is taxed at 20% of turnover.
- Put roastery, commissary and brand/IP activities in a separate VAT-registered company. Its VAT is an unrecoverable cost to the TT outlets, so price intercompany supplies at arm's length.
- Use a resident HoldCo for dividends: 0% upstream, 5% to individuals.
- Review annually, because the regime choice is made each year by 20 February. The catering TT is a **policy-dependent concession**: the 2025 reform already doubled the headline rate.
  - *Fact-check correction: it is more than policy-dependent. The Government's stated policy (PM, June 2024) is to abandon TT entirely, "step by step", for a unified tax system (REPORTED [23]). Test the chain case under "TT abolished after year 2–3". The chain's under-2-year payback holds only if TT survives at least 2 years.*

### 3.12 What the 5-year model must include, and how

Notation: quarterly periods q, years y. Gc = catering receipts (customer-paid); Gn = non-catering receipts. All AMD.

**A. Regime switch.** Model `REGIME ∈ {TT_CATERING, VAT_GENERAL}` as a scenario input. Do not switch mid-horizon unless the Art. 73(14) clawback is modelled.

**B. Turnover tax (TT_CATERING).**
```
E_q   = COGS_gross_q + Payroll_gross_q + Utilities_gross_q + Marketing_gross_q
        + Admin_gross_q + CardFees_q + Rent_q          # documented; EXCLUDES capex, depreciation,
                                                       # repairs/maintenance of fixed assets, trips, representation
D_q   = 0.09 × E_q + U_(q-1)                           # deduction available (AMD), U = unused carry-forward
A_q   = MIN(D_q, (0.12 − 0.035) × Gc_q)                # deduction actually used (floor 3.5%)
U_q   = D_q − A_q
TT_q  = 0.12 × Gc_q − A_q + 0.20 × Gn_q                # paid by the 20th of the month after the quarter
ProfitTax = 0 ; VAT = 0
Capex and imports booked GROSS of VAT (incl. 20% import VAT; duty 0–10% per C2)
```

**C. General regime (VAT_GENERAL).**
```
OutputVAT_m = (Gc_m + Gn_m) / 6
InputVAT_m  = 0.20 × (VAT-able opex ex-VAT_m + capex ex-VAT_m + imports customs value incl. duty_m)
NetVAT_m    = OutputVAT_m − InputVAT_m       # if < 0: refund/offset (assume 1–3 month lag; Art. 74)
Revenue_net = (Gc + Gn) / 1.2
TaxDep_y    = Σ asset_cost_exVAT / life      # 20y buildings/structures, 5y equipment, 1y IT, 8y other; monthly pro-rata
PBT_tax_y   = Revenue_net − opex_exVAT − payroll − rent − local taxes − TaxDep − interest
              − non-deductible waste above 1% (2% marked dairy) of gross income
ProfitTax_y = 0.18 × MAX(0, PBT_tax_y − LossCF_(y−1)), LossCF expires after 5 years
Advances    = from year 2: each quarter MIN(20% × ProfitTax_(y−1), 2% × Revenue_prior quarter);
              balance by 20 April
```

**D. Both regimes.**
- `DividendTax = 5% × dividends to individuals or non-resident companies`; 0% to a resident HoldCo.
- `PayrollWithholding = 20% PIT + 5% pension (≤ AMD 500k a month) + stamp duty AMD 1,000 + UHI premium (0 / 4,800 / 10,800 by gross band)`. These are withheld from gross pay, and the cost line = gross payroll.
  - If the draft UHI amendment is adopted, add `EmployerUHI = AMD 4,400 × employees with gross ≤ AMD 200k × months` from Dec 2026 or 2027 (REPORTED, draft; C3).
  - *Fact-check correction: stamp duty and UHI updated to match C3-labor.md.*
- `RentWithholding = 10% × rent paid to individual landlords`. Withheld from the landlord's rent, so it is not an extra cost if rent is agreed gross.
- `PropertyTax_y = 0.3% × CV_building + 1% × CV_land`, paid ½ by 1 June and ½ by 1 December. CV = cadastral value; assume 70–100% of build cost until a Cadastre figure is obtained. CV_land = 0 if the land is leased. If the company owns the plot, use market evidence (B4: ≈AMD 24,000–54,000 per m² in the Kotayk suburbs). *Fact-check correction: the original land value of AMD 2,000–8,000 per m² was far below market.*
- `LocalDuties_y ≈ 4 × catering permit (by m²) + night permit (if open past 24:00) + 12 × waste fee × m² + advertising` (local duty per m² per month, or road tax of AMD 10,000 per m² per year outside settlements).
- One-offs: LLC registration 0; trademark ≈ AMD 120–150k nationally; Madrid ≈ CHF 653 + designations; HDM/e-HDM units ≈ AMD 60–125k each (C2).
- Contingency for penalties: 0 in the base case, but run a stress test (late payment = 0.075% a day).

**E. FX.** The tax lines are in AMD. Convert to USD at the model's FX path (base 362; A1 recommends 345–390 sensitivity). There is no FX element in the tax rates themselves.

---

## 4. Implications for the drive-thru concept (critical)

1. **Tax favours a lean format.** Because TT ignores capex and denies capex VAT, every AMD of building or equipment costs a full 1.2 AMD (VAT-inclusive) and earns no TT deduction. The lean or mid-range build (C1) becomes relatively more attractive. **A flagship build pushes the optimal regime toward VAT,** which makes menu pricing harder because 16.67% of every price goes to VAT. *Fact-check correction: so does a mid-range build at the study's base revenue of AMD 100–150M, where VAT leads on 5-year NPV by ≈AMD 14–19M (§3.11(a)). TT is clearly better only with lean capex or receipts above ≈AMD 200M.*
2. **TT is a large but political advantage.**
   - About 4.5–6.5% of receipts against about 10% net VAT plus profit tax. For a single unit this is **≈AMD 7–22M a year** at G = 140–300M, comparable to 1–2 extra staff salaries or the whole annual marketing budget.
   - Policy risk is real: the Government doubled the catering headline rate in 2025, added a 3.5% floor and removed catering from micro in Yerevan.
   - **The Government has also said it intends to abolish TT altogether.** In June 2024 PM Pashinyan said "the turnover tax should be completely abandoned in Armenia… step by step… unified tax system", and the Ministry of Finance called TT an "extraordinary favourable treatment" (REPORTED, ARKA [23]). No amendment to Arts 253–265 has been enacted for 2027, but **treat TT surviving more than 2–3 years as a key risk, not a base case.**
   - A further tightening (e.g., a cap for catering TT, or forcing large chains into VAT) or outright abolition would hit a multi-unit plan hardest. **The model must include a "forced VAT from year 3" downside scenario.** In that scenario the capex VAT forgone at the start is lost, apart from a possible gradual recovery under Art. 73(4)(2) (unverified). For that reason the 10-year breakevens in §3.11 should carry little weight. Severity: High.
   - *Fact-check correction: the original omitted the stated abolition policy and used 10-year NPVs that assume TT survives for 10 years.*
3. **Interpretation risk on deductible expenses.** If SRC treated wages or rent as non-deductible, TT would rise by 1.5–2.5 points of revenue. **Obtain a written SRC clarification (Art. 306) before final investment approval.**
4. **The non-catering 20% trap.** A Starbucks-style retail wall (beans, mugs, tumblers) inside the TT company would pay 20% of turnover with no deduction, which wipes out the retail margin. **Either drop retail or run it through a VAT-registered sister company with its own HDM.**
5. **Compliance, not rate, is the main operational tax risk.**
   - Each HDM violation costs at least AMD 200,000 + 0.5% of quarterly HDM turnover. At AMD 75M a quarter, that is ≈ AMD 575,000 per incident.
   - A missing HDM at a payment point costs AMD 500,000.
   - Multi-window drive-thrus, mobile pre-order and delivery platforms all need correctly registered HDM or e-HDM endpoints, and product-mark scanning for marked retail goods.
   - **Budget for an iiko/R-Keeper-type POS with certified SRC HDM integration** (C2 gap).
6. **Missing a deadline is expensive.** Not filing the TT or catering declaration within its 20-day window makes the company a VAT payer for the rest of the year, at a 16.67% hit on receipts, with no way back until 1 January. A **compliance calendar** is a must (Art. 59, 254, 255).
7. **Local cost is small; site status is not.** Local duties come to ≈AMD 0.5–0.7M a year. With property tax the total is ≈AMD 0.8–1.1M a year if the land is leased (<1% of receipts). If the company owns the plot it is **≈AMD 1.4–2.5M (≈1–2% of AMD 140M receipts)** (ESTIMATE, §3.8). However:
   - *Fact-check correction: the original "below AMD 1.5M a year (<1% of receipts)" relied on a land cadastral value far below B4's market evidence. It does not hold if the plot is owned.*
   - roadside advertising outside a settlement needs road-authority technical conditions plus road tax;
   - 24-hour operation needs the community's night permit;
   - the community's rules on catering outlets apply.

   Confirm these with the specific community **before** signing land.
8. **No subsidies to count on.** There is no investment-programme VAT deferral, no profit-tax holiday and no regional tax relief. **The investment case must not assume tax incentives.** Grants or concessional credit, if any, belong to a separate financing workstream.
9. **Investor exit and distributions are tax-light.** There is 5% on dividends, and dividends from a resident subsidiary to a resident holding are untaxed. Gains on selling LLC shares were not researched; check them before structuring the exit.

---

## 5. Data gaps and how to verify them

| # | Gap or uncertainty | Why it matters | How to verify |
|---|---|---|---|
| 1 | Are **staff wages, land rent from individuals, utilities and equipment service contracts** deductible against catering TT (Art. 258(6) read with 121(7), 55(12)–(13))? | ±1.5–2.5 points of revenue in TT | Written request for an **official clarification** to SRC (Art. 306; src.am → "Official clarifications"); or a Big-4 Yerevan tax opinion (KPMG, PwC, EY, Deloitte, Grant Thornton Amyot) |
| 2 | Classification of retail goods (bagged beans, bottled drinks, merchandise, gift cards) as catering (12%/9%) or "other" (20%) | Retail strategy | Same SRC request, with a product list |
| 3 | Whether a TT → VAT switch lets capex VAT be recovered gradually (Art. 73(4)(2)) | Option value of starting on TT | SRC clarification; tax adviser |
| 4 | Land under a building: taxed at land rate, within the building's cadastral value, or both | Property-tax line | Cadastre Committee (cadastre.am) cadastral-value certificate for the candidate plot; the community finance department |
| 5 | Cadastral values of candidate plots and the building | Property tax | Cadastre extract (ԱՍԿ) for the specific plot; Law on cadastral valuation approximated to market value |
| 6 | **2026 local duty and fee decisions** of the actual community (Abovyan, Nor Hachn, Charentsavan, Hrazdan, Sevan), including night-operation, catering-permit, advertising and waste rates | Opex; 24-hour feasibility | Community websites or council decisions on arlis.am ("local acts"), or e-draft.am drafts for 2026; community finance office |
| 7 | Text and ranges of the **Law on Local Duties and Fees** | Caps on what communities can charge | arlis.am (search the Law by name); not opened here |
| 8 | Whether a pylon or name sign on own land in the M-4 protection zone counts as "advertising" for road tax, and what the road authority's permit cost and lead time are | Signage plan and cost | Roads Department SNCO (Ministry of Territorial Administration and Infrastructure); Law on Advertising (definitions of "signboard") |
| 9 | Receipt lottery / cashback programme in 2026 under Art. 18.1 | Marketing and compliance only | src.am news; Government decisions referencing Art. 18.1 |
| 10 | Sectors and dates in the **e-HDM mandate** from 1 Jan 2027 (Government decision under HO-309-N) | POS architecture | e-draft.am (Ministry of Finance / SRC drafts); arlis.am after adoption |
| 11 | Stamp duty is now resolved as REPORTED: AMD 1,000 / 15,000 a month (PwC [24], C3). Still open: whether the **draft employer UHI levy** (AMD 4,400 per employee ≤ AMD 200k, from Dec 2026) is adopted, and the 2027 UHI rule for earners above AMD 200k | Payroll cost (employer side) | e-draft.am project 10624; arlis.am after adoption; C3-labor.md |
| 12 | Customs duty exemptions for investment projects (EEC lists of technological equipment) | Up to 10% of refrigeration cost | SRC Customs Department; Ministry of Economy investment-incentive desk |
| 13 | Customs classification of speed ovens and automated beverage systems (0% vs 10% duty; 5-year vs 3-year depreciation) | Capex and depreciation | Preliminary classification decision from SRC customs (EAEU Customs Code procedure) |
| 14 | Trademark examination timeline and the IP office's current practice (aipa.am was unreachable from this session) | Brand launch timing | Intellectual Property Office (aipa.am) or a local IP attorney; typical timelines not verified |
| 15 | Registration route and time for **foreign founders** (offline State Register) | Investor onboarding | State Register Agency (e-register.am legal support +374 10 201448) |
| 16 | Treaty WHT rates if the investor or HoldCo is foreign | Distribution planning | Armenia's tax treaties on arlis.am / Ministry of Finance; the investor's residence |
| 17 | Capital-gains treatment of selling LLC shares (resident and non-resident sellers) | Exit modelling | Tax Code Art. 125(4)(4) (non-residents: 18% on gains on shares) indicates taxation; confirm resident-individual treatment |
| 18 | Abovyan 2025 rates are a **draft**; adoption and any 2026 changes not checked | Local duties | Abovyan council decision on arlis.am or abovyan.am |
| 19 | **Future of turnover tax.** Timing of the stated plan to abolish TT (June 2024) and any draft that would amend Arts 253–265 | Regime choice; 10-year NPVs | e-draft.am (Ministry of Finance drafts); Government tax-policy programme; Big-4 tax alerts |
| 20 | **VAT refund speed for a new, pre-revenue company** (is it "risky" under Art. 74(5)? how long does a desk or field review take?) | Capex-VAT timing (t=0 vs t=1–2 moves the mid breakeven between ≈171M and ≈203M) | SRC risk criteria (Government decision under Art. 74); tax adviser experience |

**Reproducibility.** The regime-comparison script (Python, assumptions as in §3.11) was kept in the analyst scratchpad. The formulas in §3.12 are sufficient to rebuild it in the model workbook.

---

## 6. Sources (all accessed 2026-10-10)

1. Tax Code of the Republic of Armenia (HO-165-N, 4 Oct 2016), official incorporation on ARLIS, including amendments up to HO-440-N of 27 Aug 2026. https://www.arlis.am/hy/acts/143894/latest. Articles used: 4, 55, 59, 63, 64, 69, 72–75, 79, 102–136, 150, 166, 171, 186–195, 224–238, 253–272, 380–381, 401, 416.
2. Law HO-285-N "On amendments to the Tax Code" (adopted 12 Jun 2024, published 28 Jun 2024; in force 1 Jan 2025; catering outside Yerevan from 1 Jan 2026). https://www.arlis.am/hy/acts/201067
3. Law HO-72-N (adopted 26 Mar 2025, published 7 Apr 2025): administrative and selling costs deductible for TT from 2025. https://www.arlis.am/hy/acts/205201
4. Law HO-83-N (adopted 4 Mar 2026; in force 1 Jan 2027): e-commerce platforms. https://www.arlis.am/hy/acts/223255
5. Law HO-234-N (adopted 6 May 2026; in force 1 Jul 2026 / 1 Jan 2027). https://www.arlis.am/hy/acts/226008
6. Law HO-309-N (adopted 3 Jul 2026): e-HDM provisions, from 1 Jan 2027. https://www.arlis.am/hy/acts/228152
7. Law HO-385-N (adopted 3 Jul 2026; in force 1 Feb 2027): bank dividends 15%. https://www.arlis.am/hy/acts/228632
8. Law HO-383-N (adopted 10 Dec 2021, published 22 Dec 2021): repeal of Tax Code Art. 79 (VAT deferral on investment-programme imports). https://www.arlis.am/hy/acts/158700
9. Law HO-145-N (adopted 11 Apr 2024, published 3 May 2024): repeal of Art. 127(1)–(2) business-programme profit-tax reduction. https://www.arlis.am/hy/acts/192452
10. Law HO-376-N (adopted 24 Oct 2024, published 8 Nov 2024): Art. 18.1 tax-administration support programmes; late penalty 0.075% a day from 2025. https://www.arlis.am/hy/acts/199379
11. Government Decision 125-N of 6 Feb 2025: goods subject to Data Matrix marking and timelines (coffee and tea from 1 Mar 2025; dairy etc. from 1 Jan 2026). https://www.arlis.am/hy/acts/207406/latest. See also Government Decision 1715-L of 31 Oct 2024 (marking pilot): https://www.arlis.am/hy/acts/199013
12. Law HO-391-N (adopted 13 Nov 2025; in force 1 Jun 2027): realtor rules (checked; not relevant). https://www.arlis.am/hy/acts/217643
13. Law of the RA "On State Duty" (27 Dec 1997, consolidated): Art. 8 (base duty AMD 1,000), Art. 16 (state registration), Art. 18(4) (trademarks, Madrid). https://www.arlis.am/hy/acts/142614/latest
14. Law of the RA "On Funded Pensions" (consolidated): Art. 6 social payment rates. https://www.arlis.am/hy/acts/141948/latest
15. State Revenue Committee: "About turnover tax" guidance (legal-entity section, menu item 185; last updated 6 Oct 2022, **outdated rates**). https://www.src.am/am/legal
16. State Revenue Committee: Tax legislation → Tax Code page (links to the ARLIS consolidated text). https://www.src.am/am/getMenusContents/222
17. Ministry of Justice e-register platform: "Registration of a Limited Liability Company" service page (fee: free; process: immediate / 2 business days; "Armenia" name fee AMD 600,000 a year). https://www.e-register.am/en/services/d0fd5a23-a8bf-4103-bedd-ef6a6db9cdda
18. e-draft.am: Draft decision of Abovyan community council "Types and rates of local duties in Abovyan community for 2025" (posted Nov 2024), with rate annex (xls). https://www.e-draft.am/en/projects/7998/about
19. e-draft.am: Draft decision of Abovyan community council "Types, rates and privileges of local payments for 2025" (incl. waste-fee annex, docx). https://www.e-draft.am/en/projects/7999/about
20. WIPO: Madrid System schedule of fees (in force 1 Feb 2023). https://www.wipo.int/madrid/en/fees/sched.html
21. Alta-Soft EAEU tariff database: HS 8419 81 200 0 (0%) and 8418 69 000 8 (10%). https://www.alta.ru/tnved/code/8419812000/ ; https://www.alta.ru/tnved/code/8418690008/ (the VAT shown there, 22%, is Russia's, not Armenia's)
22. Sibling workstreams (this repository):
    - C2-equipment-supply.md: CET table, landed-cost factors, HDM prices.
    - C1-construction-costs.md: capex scenarios (lean 91.9 / mid 183.2 / flagship 376.3 AMD M incl. VAT, excl. land and equipment), building and plot sizes.
    - A1-macro-consumer.md: CBA FX 361.93; minimum wage AMD 75,000 (REPORTED).
    - B1-m4-traffic.md: the M-4 is an interstate road.
    - C3-labor.md (§3.4 and the key data table): stamp duty, UHI premiums and the draft employer UHI levy (added at fact-check).
    - C6-benchmarks.md: base unit revenue AMD 100–150M (base 140M) and base rent AMD 1.5M a month (added at fact-check).
    - B4-alt-corridors.md: Kotayk suburban land asking prices of $66–150 per m², and a ground-lease placeholder of AMD 1.3–1.8M a month (added at fact-check).
23. ARKA News Agency, "Armenia to abandon turnover tax and switch to unified tax system", 6 Jun 2024 (PM Pashinyan; the Ministry of Finance calls TT an "extraordinary favourable treatment"). REPORTED. https://arka.am/en/news/economy/armenia_to_abandon_turnover_tax_and_switch_to_unified_tax_system (added at fact-check)
24. PwC Worldwide Tax Summaries, "Armenia – Individual – Other taxes" (last reviewed 30 Jun 2026): stamp duty and UHI from Dec 2025. REPORTED; opened via C3-labor.md [S6]. https://taxsummaries.pwc.com/armenia/individual/other-taxes (added at fact-check)

---

## 7. Fact-check log

*Adversarial fact-check, 10 Oct 2026. Statutory claims were re-opened on arlis.am (consolidated Tax Code, acts/143894/latest, amended to HO-440-N of 27.08.26) and in the amending laws; the decision-layer figures were rebuilt from §3.11's inputs. Cross-checked against C1, C2, C3, C6, B4 and A1. The results below are applied in the text above. Corrected passages carry "Fact-check correction" notes; caveats on confirmed items carry "Fact-check note".*

| # | Claim | Result | Correction / evidence |
|---|---|---|---|
| 1 | Catering TT 2026 = 12% × receipts − 9% × documented direct, admin and selling expenses; floor 3.5%; unused deductions carried forward without limit (exec 1, row 13, §3.5) | Confirmed | Art. 258(1) row 6 (12); 258(4) (−9% of 258(6) expenses, 3.5% floor); 258(7) carry-forward; 258(6)(2) exclusions as stated. Ladder rechecked: 7.5 / 6.6 / 5.7 / 4.8 / 3.9%; floor binds at e = 94.4% |
| 2 | Catering declaration keeps a catering company on TT at any revenue, overriding the AMD 115M cap and the related-party exclusions; 20-day filing window (exec 1, row 17, §3.5) | Confirmed | Art. 254(6) "regardless of the restrictions of this chapter", except 254(3)(3) and (3.1); 254(7) 20 days; 254(8) includes delivery; 254(2) 115M |
| 3 | New formula outside Yerevan from 1 Jan 2026 (HO-285-N); admin and selling costs deductible from 1 Jan 2025 (HO-72-N) (exec 2, row 13, §3.5) | Confirmed | HO-285-N Art. 16(6)(1); HO-72-N Art. 9(4). Caveat added: the Nor Nork / Avan part of the M-4 is inside Yerevan (new formula since 2025; no micro-entrepreneurship) |
| 4 | Catering-declared payer pays 20% of turnover, with no deduction, on all non-catering income (exec 5, row 14, §3.5, §4.4) | Confirmed | Art. 258(1) row 7; 258(8): only rows 6 and 7 apply, so rent and other income that would get 10% elsewhere gets 20% |
| 5 | VAT 20% (16.67% inside a price); AMD 115M threshold with VAT only on the excess; no catering exemption (rows 1–4, §3.3) | Confirmed | Art. 63(1), 63(2)(4); 59(1)(5), 59(2)(2) |
| 6 | Profit tax 18% (IE 23%); advances = min(20% of prior-year tax, 2% of prior-quarter revenue), none in the registration year; 5-year losses; dividends 5%, intercompany dividends deductible (exec 6, rows 7–10, 22–23) | Confirmed | Art. 125(1), (3.1), (4)(3.1), (4)(2), (4)(5), (4)(4); 135(1), (5); 123(1)(4), (2)(1); 150(8), (1), (7) |
| 7 | Minimum depreciation lives 20 / 10 / 5 / 3 / 1 / 8 years; assets ≤ AMD 50,000 expensed (exec 7, rows 11–12, §3.4) | Confirmed | Art. 121(1)(3) rows 1–6; 121(2)(1); 121(1)(4) allows longer lives |
| 8 | VAT → TT claws back 20% × NBV of fixed assets with recovered VAT (bought after 1 Jul 2024); TT → VAT makes unused catering deductions × 10 deductible (exec 4, rows 19–20, §3.5) | Confirmed | HO-285-N Art. 4(2) (Art. 73(14)), Art. 16(4); Art. 264(4). Note added: the "AMD 5M timing benefit" leaves out ≈AMD 3M of VAT kept for good after one year of depreciation |
| 9 | Steady state: Case A net VAT 14.5, profit tax 1.1, TT 7.9 (5.2%), advantage +7.7; Case B 29.5 / 10.7 / 18.7 (6.25%) / +21.5; payback 4.7 / 1.7 years (§3.11, exec 4) | Confirmed | Rebuilt exactly from the stated inputs: A: E/G 75.1%, TT 7.86, advantage 7.72. B: E/G 63.9%, TT 18.74, advantage 21.46. The chain figure (≈98M saved) reproduces to within ~AMD 2M |
| 10 | 5-year NPV breakeven at 14% ≈186M (mid), ≈86M (lean), ≈344M (flagship); 10-year ≈132M / 53M / 242M (exec 4, §3.11 NPV table) | **Downgraded** | Reproducible only if the AMD 36M capex-VAT refund is discounted a full year (t=1), which was not disclosed. With the refund at construction (t=0): 5-year **≈107 lean / ≈200–203 mid / ≈364–375 flagship**; 10-year ≈60 / 145 / 257–262. NPV table rebuilt at t=0 with G = 100 and 140 columns added. The original figures are kept as a "refund 12 months late" scenario (Art. 74(5)), and a 24-month scenario (mid ≈171M) is added |
| 11 | Recommendation: catering TT by default for AMD 150–300M receipts; VAT only for flagship capex with receipts below ~250–340M (exec 4, §3.11(a)) | **Corrected** | It contradicted the file's own breakeven table and missed the study's base revenue (C6: AMD 100–150M, base 140M). At mid capex and G = 100–140M, TT minus VAT 5-year NPV is −14 / −12 / −11 (refund at t=1) or −19 / −17 / −15 (t=0). The 10-year result is about break-even. Recommendation rewritten as a capex × revenue matrix: **at mid capex below ≈AMD 200M of receipts, the VAT regime is NPV-better over 5 years** unless refund risk, compliance cost, wage deductibility and the TT→VAT option are priced explicitly |
| 12 | TT is a durable, policy-dependent concession; the downside is "forced VAT from year 3" (exec 5, §3.11(b), §4.2) | **Corrected** | Added the Government's stated policy to abolish TT entirely (PM Pashinyan; MinFin "extraordinary favourable treatment"; ARKA, 6 Jun 2024 [23]; REPORTED). No 2027 amendment to Arts 253–265 is enacted. TT persistence beyond 2–3 years is now flagged as a key risk, and the 10-year NPVs are marked as low-weight. New gap #19 and key-data row 48 |
| 13 | If wages are not deductible, TT ≈7.4% (A) / 7.7% (B), or ≈8.2–8.3% also without rent and utilities; TT still ahead by ≈3.3M / 15.3M (§3.5, §4.3, row 44) | Confirmed | Recomputed: 11.10 (7.4%) / 23.06 (7.69%); 12.29 (8.2%) / 24.90 (8.3%). The 3.3 / 15.3 figures are the worst case; with only wages disallowed, ≈4.5 / 17.1. Note added: at mid capex a 3.3M margin takes about 11 years to repay the capex VAT |
| 14 | Property tax 0.3% (public-purpose buildings) / 1% (settlement land) at 100% of cadastral value from 2026; mid site ≈AMD 0.4–0.65M (§3.8), shown as 0.4–0.9M in the exec summary; local plus property tax < AMD 1.5M (§4.7) | **Corrected** | Rates, phase-in and payment dates confirmed (Art. 229, 233(7), 236). The exec-summary figure did not match the table, and the land value of AMD 2,000–8,000/m² conflicted with B4 ($66–150/m² ≈ AMD 24,000–54,000/m²). Re-based: **≈AMD 0.9–1.8M a year if the plot is owned**, ≈0.3–0.45M if the land is leased. Local plus property tax ≈AMD 1.4–2.5M if owned (≈1–2% of receipts) or ≈0.8–1.1M if leased. Exec 8, §3.8, §3.12 D and §4.7 updated |
| 15 | Payroll: employer cost ≈ gross; stamp duty "roughly AMD 1,500–15,000 by band"; net = gross × 0.75 − stamp duty (§3.7, §3.12 D, gap 11) | **Corrected** | PIT 20% and pension 5% / 10% − 25,000 (cap 1,125,000) confirmed. Stamp duty is AMD 1,000 up to a gross of AMD 1M and 15,000 above, from Dec 2025. A UHI premium of 0 / 4,800 / 10,800 applies from Dec-2025 payroll, and a draft employer UHI levy of AMD 4,400 per employee ≤ 200k would apply from Dec 2026 (PwC [24], C3; REPORTED). Net = gross × 0.75 − 1,000 − UHI. Rows 46–47 added |
| 16 | Land lease from an individual = AMD 6M a year in the regime model (§3.11 inputs) | **Corrected** | Contradicts C6 (AMD 1.5M a month = 18M a year) and B4 (15.6–21.6M a year). Rerun at 18M: TT advantage 7.7 (A, unchanged because VAT-regime profit tax falls to 0) and 20.4 (B, from 21.5). TT 4.5% / 5.9% of G. Cash lines were overstated by ≈AMD 10–11M a year. The steady-state table now shows both rents; a rent-18M breakeven row was added (mid 5-year ≈216M). The 10% PIT withholding on rent is noted |
| 17 | Road tax AMD 10,000 per m² a year on interstate roads outside settlements; Abovyan 2025 draft local duties (catering permit 18,000 a quarter, night operation 100,000 a year, ads 1,500 per m² a month) (exec 9, rows 29–30, §3.8) | Confirmed | Art. 190(1)(1), (1)(2), (2); Abovyan annex rows 12(2), 13(1)(d), 15(4). Arithmetic 240k / 432k / 72k correct; the REPORTED (draft) tag is appropriate. Caveat added: village coefficients of 0.5–3.0 (e.g., Arinj ×3.0; Ptghni ×0.5–0.75) |
| 18 | HDM fines, e-HDM from 1 Jan 2027, Data Matrix (coffee and tea from 1 Mar 2025, dairy from 1 Jan 2026), late penalty 0.075% a day (exec 10, rows 32–35, §3.9) | Confirmed | Art. 416(1), (2), (4); HO-309-N Arts 8, 12, 13; Gov. Decision 125-N points 1–2; HO-376-N Art. 3 |
| 19 | Set-up and IP: free LLC registration (immediate or 2 business days); "Armenia" or "Hay" in a name AMD 600k a year; trademark ≈120k / 150k; Madrid CHF 653 / 903 + AMD 30k handling; Armenia's individual fee 100k + 10k per class (exec 12, rows 40–43) | Confirmed | e-register.am service page; State Duty law Art. 8, 18(4); WIPO schedule 2.1.1, 2.1.2, 2.2, 2.3 |
| 20 | No incentives: Art. 79 repealed (HO-383-N), Art. 127(1)–(2) repealed (HO-145-N); micro catering exclusion only inside Yerevan; customs duty 0% on coffee machines, 10% on refrigeration (exec 11, rows 21, 37, 39, §3.6, §3.10) | Confirmed | HO-383-N Art. 4; HO-145-N Art. 1, 3(2); Art. 267(3), (5)(2); alta.ru (REPORTED tag appropriate) |
| 21 | SRC "About turnover tax" page still shows the old 6% catering rate (last updated 6 Oct 2022) (exec 2, §3.1, source [15]) | Unverifiable | The page body loads dynamically and could not be retrieved. Marked "*Fact-check: source unreachable on 10 Oct 2026; treat as unverified.*" in exec 2 and §3.1. No 2026 figure depends on it: 12% is confirmed from Art. 258, and the pre-reform 6% is confirmed by ARKA [23] |

**Net effect for the investor.** The statutory content stands, and every VERIFIED rate re-opened on arlis.am matched. The decision layer has changed:
- At the study's base case (mid-range capex, AMD 100–150M receipts), the VAT regime is better on 5-year NPV by about AMD 14–19M. Catering TT is better only with lean capex or receipts above about AMD 200M.
- The value of TT now carries an explicit abolition risk.
- Payroll, property-tax and rent inputs are aligned with C3, B4 and C6.
