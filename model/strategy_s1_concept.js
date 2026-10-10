export const meta = {
  name: 'drivethru-strategy-concept',
  description: 'Concept & positioning: three lens analysts, adversarial challenge',
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
Already decided context from the design team: a parametric prototype exists (171 m² tuff-clad building with glazed café + 12 seats + 2 accessible restrooms, hypar oak-soffit roof, dual order lanes merging to a single pickup lane with 2 windows, 13-car stack, 25 parking stalls incl. 2 EV + long-vehicle bay, terrace 62 m², on a 3,256 m² roadside plot with decel/accel lanes; right-in/right-out). Working brand name CHAMPA (ՃԱՄՓԱ / ЧАМПА, Armenian vernacular for "road"; send-off blessing "Ճամփադ բաց!" = "May your road be open"; trademark screening found no conflict, BARI was dropped due to a registered class-43 mark), affordable-premium positioning, deep teal + apricot identity. These can be challenged if evidence says so.\nFILE-WRITE FALLBACK: if you are asked to write a file, ALSO return its complete content in the schema's markdown (or python_source) field — some agents are blocked from writing files, and the coordinator will save it.`

const CONCEPT_SCHEMA = { type: 'object', properties: {
  lens: { type: 'string' },
  scores: { type: 'array', items: { type: 'object', properties: { concept: { type: 'string' }, score: { type: 'number' }, rationale: { type: 'string' } }, required: ['concept', 'score', 'rationale'] } },
  recommended_concept: { type: 'string' }, positioning_tier: { type: 'string' }, key_arguments: { type: 'array', items: { type: 'string' } },
  menu_architecture: { type: 'string' }, pricing_notes: { type: 'string' }, markdown: { type: 'string' }, risks: { type: 'array', items: { type: 'string' } },
}, required: ['lens', 'scores', 'recommended_concept', 'positioning_tier', 'key_arguments', 'menu_architecture', 'pricing_notes', 'risks'] }

const CONCEPTS = `Evaluate exactly these four concepts on a 0–10 scale: (1) Specialty coffee & beverages only; (2) Coffee + breakfast & bakery (hand-held, mostly bake-off/assembled); (3) Broad fast-food & beverage menu (burgers/shawarma/hot meals + coffee); (4) Hybrid roadside convenience (coffee + bakery + grab-and-go + restrooms + EV/fuel-station partnership). Also decide positioning tier: premium / affordable premium / mass-market, with price points in AMD for core drinks and the resulting average transaction value (ATV) per order — justify ATV from menu mix (items per order, attach rate), not from US benchmarks.`

const lenses = [
  { id: 'economics', keys: ['C1', 'C2', 'C3', 'C4', 'C6', 'A2', 'A4'], prompt: 'Lens: unit economics & capital efficiency (COGS, labour intensity, throughput, capex, margins, break-even).' },
  { id: 'customer', keys: ['A1', 'A2', 'A3', 'A4', 'A5', 'B3'], prompt: 'Lens: Armenian customer & market fit (purchasing power, habits, segments, willingness to pay, drive-thru culture, seasonality).' },
  { id: 'competition', keys: ['A2', 'A3', 'A5', 'B2', 'B4', 'C5', 'C6'], prompt: 'Lens: competitive strategy, defensibility and scalability (incumbents incl. Coffee House drive-thru, fuel stations, Starbucks entry risk, regulation, multi-unit roll-out).' },
]
const conceptP = lenses.map(l => () => agent(`${CONTEXT}\n\nTASK: ${l.prompt}\n${CONCEPTS}\nRead fully:\n${files(l.keys)}\nReturn the schema. Be decisive and quantitative.`, { label: `concept:${l.id}`, phase: 'Analyze', schema: CONCEPT_SCHEMA }))

const CH_SCHEMA = { type: 'object', properties: { verdict: { type: 'string' }, problems: { type: 'array', items: { type: 'object', properties: { issue: { type: 'string' }, severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['issue', 'severity', 'fix'] } } }, required: ['verdict', 'problems'] }
phase('Analyze')
const [cE, cC, cK] = await parallel(conceptP)
phase('Challenge')
const ch = await agent(`${CONTEXT}\n\nADVERSARIAL REVIEW of the concept choice. Three lens analysts scored the four concepts:\n${JSON.stringify([cE, cC, cK])}\nRead these research files:\n${files(['A2', 'A3', 'A4', 'A5', 'C2', 'C6'])}\nAttack the emerging recommendation: is the price point realistic vs Coffee House (~1,000 AMD) and purchasing power, does food add margin or only complexity, does the hybrid convenience format dilute the brand or win on restrooms/EV, is "American-style" a selling point in Armenia, what concept would a disciplined investor choose for unit 1? Return the schema.`, { label: 'challenge:concept', phase: 'Challenge', schema: CH_SCHEMA })
return { lenses: [cE, cC, cK], challenge: ch }
