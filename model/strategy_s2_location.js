export const meta = {
  name: 'drivethru-strategy-location',
  description: 'Weighted location scoring, adversarial challenge, revision',
  phases: [{ title: 'Analyze' }, { title: 'Challenge' }, { title: 'Resolve' }],
}

const R = '/home/user/Drive-thru/research'
const FILES = {
  A1: `${R}/A1-macro-consumer.md`, A2: `${R}/A2-coffee-market.md`, A3: `${R}/A3-qsr-fuel-convenience.md`, A4: `${R}/A4-food-preferences.md`,
  A5: `${R}/A5-drivethru-cultural-fit.md`, A9: `${R}/A9-gapfill.md`, B1: `${R}/B1-m4-traffic.md`, B2: `${R}/B2-m4-corridor-map.md`,
  B3: `${R}/B3-tourism-seasonality.md`, B4: `${R}/B4-alt-corridors.md`, B5: `${R}/B5-land-real-estate.md`, B9: `${R}/B9-gapfill.md`,
  C1: `${R}/C1-construction-costs.md`, C2: `${R}/C2-equipment-supply.md`, C3: `${R}/C3-labor.md`, C4: `${R}/C4-tax.md`,
  C5: `${R}/C5-regulations.md`, C6: `${R}/C6-benchmarks.md`, C9: `${R}/C9-gapfill.md`,
}
const files = keys => keys.map(k => FILES[k]).join('\n')
const OUT = '/home/user/Drive-thru/strategy'

const CONTEXT = `You are part of a senior consulting team (strategy, foodservice, real estate, finance) preparing an investor-grade feasibility study and investment recommendation for a drive-thru coffee & food business in Armenia. The founder's idea: a premium American-style (Starbucks/Dutch Bros/Dunkin'-inspired) drive-thru chain, first site on the M4 Yerevan–Sevan highway. The team must critically test this, not validate it. Today is 2026-10-10. FX: CBA 361.93 AMD/USD (9 Oct 2026).
Evidence lives in research files (markdown with status tags VERIFIED/REPORTED/ESTIMATE/ASSUMPTION and a fact-check log in section 7 — when the fact-check corrected something, use the corrected value). Read the files you are given in full (use the Read tool; they are long — read all of it). Do NOT invent facts: every number you use must come from the files (cite file id + the original source number/URL as given there) or be explicitly labelled ESTIMATE (show formula) or ASSUMPTION (give basis). Web search is unavailable in this session; do not try to search.
Already decided context from the design team: a parametric prototype exists (171 m² tuff-clad building with glazed café + 12 seats + 2 accessible restrooms, hypar oak-soffit roof, dual order lanes merging to a single pickup lane with 2 windows, 13-car stack, 25 parking stalls incl. 2 EV + long-vehicle bay, terrace 62 m², on a 3,256 m² roadside plot with decel/accel lanes; right-in/right-out). Working brand name BARI (Բարի, "good/kind"; tagline Բարի ճանապարհ "bon voyage"), affordable-premium positioning, deep teal + apricot identity. These can be challenged if evidence says so.\nFILE-WRITE FALLBACK: if you are asked to write a file, ALSO return its complete content in the schema's markdown (or python_source) field — some agents are blocked from writing files, and the coordinator will save it.`

const LOC_SCHEMA = { type: 'object', properties: {
  criteria: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, weight: { type: 'number' }, definition: { type: 'string' } }, required: ['name', 'weight', 'definition'] } },
  sites: { type: 'array', items: { type: 'object', properties: {
    id: { type: 'string' }, name: { type: 'string' }, corridor: { type: 'string' }, lat: { type: 'number' }, lon: { type: 'number' },
    description: { type: 'string' }, aadt_base: { type: 'number' }, aadt_range: { type: 'string' }, directions_served: { type: 'string' },
    accessible_share_base: { type: 'number' }, seasonality_profile: { type: 'string' }, competition: { type: 'string' }, land_cost_note: { type: 'string' },
    access_note: { type: 'string' }, scores: { type: 'object' }, weighted_score: { type: 'number' }, evidence: { type: 'string' } },
    required: ['id', 'name', 'corridor', 'lat', 'lon', 'description', 'aadt_base', 'directions_served', 'accessible_share_base', 'scores', 'weighted_score', 'evidence'] } },
  top3: { type: 'array', items: { type: 'string' } }, recommended: { type: 'string' }, reasoning: { type: 'string' },
  verification_plan: { type: 'array', items: { type: 'string' } }, markdown: { type: 'string' },
}, required: ['criteria', 'sites', 'top3', 'recommended', 'reasoning', 'verification_plan'] }

const locP = () => agent(`${CONTEXT}\n\nTASK: Location feasibility analyst. Build a weighted location-scoring model (8–10 criteria, weights summing to 1.0: traffic volume, year-round demand stability, visibility, legal & safe access incl. both-direction service, land availability & cost, competition, proximity to population/commuters, tourism demand, infrastructure/utilities, future development/expansion fit). Score 8–12 concrete candidate sites (0–10 per criterion) drawn from the research: M4 sites (Yerevan-edge gateway/interchange incl. near the existing Coffee House drive-thru at Ptghni, Abovyan–Charentsavan, Hrazdan/Tsaghkadzor junction, Sevan town/peninsula junction) AND the strongest non-M4 candidates (M5 airport/Ejmiatsin, M1 Ashtarak, M2 Artashat, Yerevan arterials/suburbs). Give each site approximate coordinates (from the files; mark estimates), base AADT and range, directions served and an accessible share of two-way traffic (one carriageway ≈ 0.5 × light-vehicle share; interchange/both-direction sites higher), land cost notes, access notes. Identify the top 3 and recommend the optimal first site, explaining why (and why NOT the founder's preferred mid-highway M4 location if applicable). Include a site-verification plan. Read fully:\n${files(['B1', 'B2', 'B3', 'B4', 'B5', 'A2', 'A3', 'C5', 'C1'])}\nAlso write a markdown version (with the scoring table) to ${OUT}/location-study.md. Return the schema.`, { label: 'location', phase: 'Analyze', schema: LOC_SCHEMA })

const CH_SCHEMA = { type: 'object', properties: { verdict: { type: 'string' }, problems: { type: 'array', items: { type: 'object', properties: { issue: { type: 'string' }, severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['issue', 'severity', 'fix'] } } }, required: ['verdict', 'problems'] }
phase('Analyze')
const loc = await locP()
phase('Challenge')
const ch = await agent(`${CONTEXT}\n\nADVERSARIAL REVIEW of the location study. Read ${OUT}/location-study.md and these research files:\n${files(['B1', 'B2', 'B4', 'B5', 'C5', 'A2'])}\nLocation agent's output: ${JSON.stringify(loc)}\nAttack the weights, scores and the recommendation: is any score unsupported, is traffic double-counted, is both-direction access real (interchange geometry), is land actually available, is the incumbent Coffee House drive-thru properly accounted for, would a different site win under reasonable weight changes (do a sensitivity check of the top 3 to ±30% weight changes)? Return the schema.`, { label: 'challenge:location', phase: 'Challenge', schema: CH_SCHEMA })
phase('Resolve')
const rev = await agent(`${CONTEXT}\n\nYou wrote the location study (output: ${JSON.stringify(loc)}). An adversarial reviewer raised: ${JSON.stringify(ch)}.\nRevise ${OUT}/location-study.md: fix every critical/major issue the evidence supports (re-score, re-weight, run the ±30% weight sensitivity on the top 3 and report it), add a 'Challenge & response' section answering each point. Re-read research files as needed: ${files(['B1','B2','B4','B5','C5','A2'])}. Return the revised schema.`, { label: 'location:revise', phase: 'Resolve', schema: LOC_SCHEMA })
return { location: rev, first: loc, challenge: ch }
