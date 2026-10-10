export const meta = {
  name: 'drivethru-factcheck',
  description: 'Adversarially fact-check decision-critical numbers in research files and log corrections in-file',
  phases: [{ title: 'Check' }, { title: 'Apply' }],
}
// args: ["B1-m4-traffic", "C4-tax", ...]  (file stems under research/)
const R = '/home/user/Drive-thru/research'
const files = Array.isArray(args) ? args : JSON.parse(args)
const CTX = `You are an adversarial fact-checker for an investor-grade feasibility study of a drive-thru coffee & bakery business in Armenia (today 2026-10-10; FX CBA 361.93 AMD/USD on 9 Oct 2026). Research files use status tags VERIFIED (primary source opened), REPORTED (credible secondary), ESTIMATE (own calc, formula shown), ASSUMPTION (judgement). An investor will make a real money decision from these numbers. Your job is to catch errors, not to approve.`
const FC = { type: 'object', properties: {
  checks: { type: 'array', items: { type: 'object', properties: {
    claim: { type: 'string' }, location: { type: 'string' }, result: { type: 'string', enum: ['confirmed', 'corrected', 'downgraded', 'unverifiable', 'wrong'] },
    correction: { type: 'string' }, evidence: { type: 'string' } }, required: ['claim', 'result', 'evidence'] } },
  overall: { type: 'string' } }, required: ['checks', 'overall'] }
const APPLY = { type: 'object', properties: { file_written: { type: 'boolean' }, applied: { type: 'number' }, summary: { type: 'string' } }, required: ['file_written', 'applied', 'summary'] }

const out = await pipeline(
  files,
  f => agent(`${CTX}\n\nFACT-CHECK ${R}/${f}.md. Read it fully. Pick the 12–18 numbers and claims that most affect the investment decision (traffic volumes, prices, costs, wages, tax rates/rules, legal requirements, capture/benchmark figures, competitor facts) plus every ESTIMATE whose arithmetic you can recompute.\nFor each: re-open the cited source URL (WebFetch, or curl via Bash if WebFetch fails) and confirm the number, unit, date and status tag; recompute ESTIMATE arithmetic; flag VERIFIED tags where the source is actually secondary (downgrade to REPORTED), stale data presented as current, currency/unit confusion (AMD vs USD, monthly vs annual, gross vs net of VAT, one-way vs two-way traffic), and internal contradictions with sibling files in ${R}/ if you notice them. You may use at most 5 WebSearch calls in total — prefer fetching the cited URLs. If a source is unreachable, mark 'unverifiable' (do not guess). Return the schema.`, { label: `fc:${f}`, phase: 'Check', schema: FC })
    .then(fc => ({ f, fc })),
  ({ f, fc }) => agent(`${CTX}\n\nAPPLY the fact-check results to ${R}/${f}.md:\n${JSON.stringify(fc)}\nFor each 'corrected', 'downgraded' or 'wrong' item: edit the text where the claim appears (fix the number/status and add an inline note "*Fact-check correction: …*"); if an executive-summary bullet or key-data-table row depends on it, fix that too, and propagate any recomputed figure. For 'unverifiable' items add "*Fact-check: source unreachable on 10 Oct 2026; treat as unverified.*" only where the status was VERIFIED. Then append a final section "## 7. Fact-check log" (after the sources) with a table: # | claim | result | correction / evidence. Use the Edit tool for targeted edits (the files are long; do not rewrite the whole file). Return the schema.`, { label: `apply:${f}`, phase: 'Apply', schema: APPLY })
    .then(a => ({ f, overall: fc.overall, n: fc.checks.length, corrected: fc.checks.filter(c => c.result !== 'confirmed').map(c => `${c.result}: ${c.claim} → ${c.correction || ''}`.slice(0, 300)), applied: a })),
)
return out
