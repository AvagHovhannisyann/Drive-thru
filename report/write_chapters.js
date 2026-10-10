export const meta = {
  name: 'drivethru-write-chapters',
  description: 'Write report chapter fragments from evidence files, adversarially check every number, revise',
  phases: [{ title: 'Write' }, { title: 'Check' }, { title: 'Revise' }],
}
// args: [{ id, eyebrow, title, files: [abs paths], brief, figs: [ids] }]
const ROOT = '/home/user/Drive-thru'
const STYLE = `${ROOT}/report/STYLE.md`
const COMMON = `You are a senior writer on an investor-grade feasibility study: "CHAMPA (ՃԱՄՓԱ): a drive-thru coffee & bakery chain for Armenia". Today is 2026-10-10; FX 361.93 AMD/USD (CBA, 9 Oct 2026). The reader is the founder deciding whether to invest his own money; he asked for critical, data-driven analysis that separates verified data from estimates, never validation for its own sake.
Read the style guide ${STYLE} first and follow it exactly (HTML fragment, allowed classes, status tags, citations, AMD-first money format, no filler).
Integrity: every number, company fact, regulation or quote must come from the files you are given (cite as <sup>[FILEID §section #row]</sup> e.g. [B1 §2 #13], or [STRATEGY:concept], [MODEL] for model/results_summary.json). If a research file's fact-check log (section 7) corrected something, use the corrected value. Never upgrade a status tag. If a fact you need is missing, say so and point to the verification step. Web search is unavailable; do not search.
The model numbers in ${ROOT}/model/results_summary.json are the single source of truth for any financial figure (capex, revenue, EBITDA, payback, break-even); do not recompute them differently.
FILE-WRITE FALLBACK: also return the complete fragment in the schema's html field.`
const SCHEMA = { type: 'object', properties: { file_written: { type: 'boolean' }, html: { type: 'string' }, open_questions: { type: 'array', items: { type: 'string' } } }, required: ['file_written', 'html'] }
const CHECK = { type: 'object', properties: { problems: { type: 'array', items: { type: 'object', properties: { quote: { type: 'string' }, issue: { type: 'string' }, severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, fix: { type: 'string' } }, required: ['quote', 'issue', 'severity', 'fix'] } }, verdict: { type: 'string' } }, required: ['problems', 'verdict'] }

const chapters = Array.isArray(args) ? args : JSON.parse(args)
const results = await pipeline(
  chapters,
  c => agent(`${COMMON}\n\nWRITE CHAPTER "${c.id}" → file ${ROOT}/report/fragments/${c.id}.html\nOpening: <section class="ch" id="${c.id}"><div class="eyebrow">${c.eyebrow}</div><h2>${c.title}</h2>\nBrief:\n${c.brief}\nFigure placeholders you must place (each on its own line where it fits the argument): ${c.figs.map(f => `<!--FIG:${f}-->`).join(' ')}\nRead fully (use Read; long files: read all parts):\n${c.files.join('\n')}\nLength: as long as the brief needs and no longer (typically 900–1,800 words of prose plus tables). Write the file with the Write tool, then return the schema.`, { label: `write:${c.id}`, phase: 'Write', schema: SCHEMA }).then(w => ({ c, w })),
  ({ c, w }) => agent(`${COMMON}\n\nADVERSARIAL CHECK of chapter "${c.id}" at ${ROOT}/report/fragments/${c.id}.html (if missing, use: ${JSON.stringify(w.html).slice(0, 80000)}).\nOpen the cited source files (${c.files.join(', ')}) and verify EVERY number, status tag, company fact and regulatory claim against them. Flag: numbers not in the files, wrong status tags (esp. upgraded ones), arithmetic errors, AMD/USD conversion errors (361.93), claims that contradict a fact-check correction, promotional or one-sided framing, missing disconfirming evidence the files contain, style-guide violations (filler, em-dash asides, wrong classes), missing figure placeholders (${c.figs.join(', ')}). Quote the exact offending text. Default to flagging when uncertain. Return the schema.`, { label: `check:${c.id}`, phase: 'Check', schema: CHECK })
    .then(ch => ({ c, w, ch })),
  ({ c, w, ch }) => agent(`${COMMON}\n\nREVISE chapter "${c.id}" at ${ROOT}/report/fragments/${c.id}.html (if missing, start from: ${JSON.stringify(w.html).slice(0, 80000)}). A checker found: ${JSON.stringify(ch)}\nFix every critical and major problem and every minor one that is clearly right, re-reading the source files (${c.files.join(', ')}) where needed. Keep all figure placeholders. Write the file, then return the schema with the full final html.`, { label: `revise:${c.id}`, phase: 'Revise', schema: SCHEMA })
    .then(r => ({ id: c.id, file_written: r.file_written, html: r.html, problems: ch.problems.length, open_questions: r.open_questions || [] })),
)
return results.map(r => r ? { id: r.id, file_written: r.file_written, problems: r.problems, open_questions: r.open_questions, html: r.file_written ? '' : r.html } : null)
