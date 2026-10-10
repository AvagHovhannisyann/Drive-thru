"""
Page frame for the investor report: <title>, fonts, theme tokens (light/dark), components CSS,
navigation, tooltip script and the three.js viewer bootstrap.
"""

CSS = r"""
/* Layout concept: an editorial dossier — a fixed chapter rail on wide screens, one 72ch reading column
   with full-bleed figures; brand teal ink, apricot used only for emphasis and the critical path. */
:root {
  --bg: #fbfaf8; --surface: #ffffff; --surface-2: #f2efea; --ink: #11282b; --ink-2: #3e5357; --ink-3: #6b7b7e;
  --line: #e2ded6; --brand: #0f3b40; --accent: #d4701f; --accent-soft: #fbe6d3; --tuff: #c98b6b;
  --ok: #1d7a46; --warn: #a86400; --bad: #b42318;
  --s1: #2a78d6; --s2: #eb6834; --s3: #1baf7a; --pos: #2a78d6; --neg: #e34948;
  --seq-1: #e4eef9; --seq-2: #b7d2f1; --seq-3: #7eaee5; --seq-4: #3f86d6; --seq-5: #1f5aa6;
  --heat-1: #e9f3ea; --heat-2: #f4f0d4; --heat-3: #f8dcb4; --heat-4: #f3b994; --heat-5: #e98f84;
  --grid: #ebe8e2; --font-display: "Unbounded", "Noto Sans Armenian", system-ui, sans-serif;
  --font-body: "Manrope", "Noto Sans Armenian", system-ui, sans-serif; --font-hy: "Noto Sans Armenian", "Manrope", sans-serif;
  --measure: 72ch; --radius: 10px;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #0b1c1e; --surface: #102629; --surface-2: #15302f; --ink: #eef3f1; --ink-2: #c3d0cd; --ink-3: #8fa3a0;
  --line: #24403f; --brand: #8fd0c8; --accent: #f29a52; --accent-soft: #3a2a1c; --tuff: #d9a183;
  --ok: #5fc58c; --warn: #f0b85a; --bad: #f2867c;
  --s1: #3987e5; --s2: #d95926; --s3: #199e70; --pos: #3987e5; --neg: #e66767;
  --seq-1: #16314a; --seq-2: #1d4a77; --seq-3: #2b67a8; --seq-4: #4d8fd6; --seq-5: #8dbbef;
  --heat-1: #173326; --heat-2: #34371c; --heat-3: #4a3a1d; --heat-4: #5a2e22; --heat-5: #6b2a2a;
  --grid: #1f3a3c; color-scheme: dark; } }
:root[data-theme="dark"] {
  --bg: #0b1c1e; --surface: #102629; --surface-2: #15302f; --ink: #eef3f1; --ink-2: #c3d0cd; --ink-3: #8fa3a0;
  --line: #24403f; --brand: #8fd0c8; --accent: #f29a52; --accent-soft: #3a2a1c; --tuff: #d9a183;
  --ok: #5fc58c; --warn: #f0b85a; --bad: #f2867c;
  --s1: #3987e5; --s2: #d95926; --s3: #199e70; --pos: #3987e5; --neg: #e66767;
  --seq-1: #16314a; --seq-2: #1d4a77; --seq-3: #2b67a8; --seq-4: #4d8fd6; --seq-5: #8dbbef;
  --heat-1: #173326; --heat-2: #34371c; --heat-3: #4a3a1d; --heat-4: #5a2e22; --heat-5: #6b2a2a;
  --grid: #1f3a3c; color-scheme: dark; }
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } * { animation: none !important; transition: none !important; } }
body { background: var(--bg); color: var(--ink); font-family: var(--font-body); font-size: 16.5px; line-height: 1.62; margin: 0; }
.wrap { display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 48px; max-width: 1320px; margin: 0 auto; padding-inline: 24px; }
@media (max-width: 1000px) { .wrap { grid-template-columns: minmax(0, 1fr); gap: 0; padding-inline: 16px; } nav.rail { display: none; } }
nav.rail { position: sticky; top: env(safe-area-inset-top, 0px); align-self: start; padding-block: 28px; max-height: 100vh; overflow-y: auto; }
nav.rail .brandline { display: flex; gap: 10px; align-items: center; margin-bottom: 18px; color: var(--brand); font-family: var(--font-display); font-weight: 800; letter-spacing: .06em; }
nav.rail ol { list-style: none; padding: 0; margin: 0; counter-reset: ch; }
nav.rail li a { display: grid; grid-template-columns: 26px 1fr; gap: 6px; padding: 5px 8px; border-radius: 6px; color: var(--ink-2); text-decoration: none; font-size: 13.5px; line-height: 1.35; }
nav.rail li a:hover, nav.rail li a:focus-visible { background: var(--surface-2); color: var(--ink); outline: none; }
nav.rail li a span.n { color: var(--ink-3); font-variant-numeric: tabular-nums; }
main { min-width: 0; padding-block: 28px 80px; }
.hero { position: relative; border-radius: 16px; overflow: hidden; background: var(--brand); color: #fff; margin-bottom: 40px; }
.hero img { display: block; width: 100%; height: auto; aspect-ratio: 16/9; object-fit: cover; }
.hero .over { position: absolute; inset: auto 0 0 0; padding: 28px clamp(16px, 4vw, 40px); background: linear-gradient(transparent, rgba(5,20,22,.82)); }
.hero h1 { font-family: var(--font-display); font-weight: 800; font-size: clamp(28px, 4.4vw, 56px); line-height: 1.05; margin: 0 0 10px; letter-spacing: .01em; text-wrap: balance; }
.hero p { margin: 0; max-width: 60ch; font-size: clamp(14px, 1.6vw, 18px); color: #e9f0ee; }
.eyebrow { text-transform: uppercase; letter-spacing: .14em; font-size: 12px; font-weight: 700; color: var(--accent); }
.hero .eyebrow { color: #f6b27a; }
section.ch { padding-block: 36px; border-top: 1px solid var(--line); }
section.ch > h2 { font-family: var(--font-display); font-weight: 700; font-size: clamp(22px, 2.6vw, 32px); line-height: 1.15; margin: 6px 0 18px; text-wrap: balance; letter-spacing: .005em; }
h3 { font-size: 19px; margin: 28px 0 8px; text-wrap: balance; }
h4 { font-size: 15px; margin: 18px 0 6px; text-transform: uppercase; letter-spacing: .08em; color: var(--ink-2); }
p, ul, ol { max-width: var(--measure); }
li { margin-block: 3px; }
a { color: var(--brand); }
.hy { font-family: var(--font-hy); }
.lede { font-size: 19px; color: var(--ink-2); max-width: 62ch; }
.grid2 { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; }
.grid3 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.grid4 { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; }
@media (max-width: 760px) { .grid2, .grid3, .grid4 { grid-template-columns: minmax(0, 1fr); } }
.kpi { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: 14px 16px; }
.kpi .v { font-family: var(--font-display); font-weight: 700; font-size: 24px; font-variant-numeric: tabular-nums; line-height: 1.15; }
.kpi .l { color: var(--ink-3); font-size: 13px; }
.verdict { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 18px; align-items: start; background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 20px; margin-block: 18px; }
.verdict .badge { font-family: var(--font-display); font-weight: 800; font-size: 15px; letter-spacing: .06em; padding: 10px 14px; border-radius: 8px; background: var(--accent-soft); color: var(--accent); white-space: nowrap; }
@media (max-width: 600px) { .verdict { grid-template-columns: minmax(0, 1fr); } }
.callout { border-left: 3px solid var(--accent); background: var(--surface); padding: 12px 16px; border-radius: 0 8px 8px 0; max-width: var(--measure); }
.tscroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: 14px; font-variant-numeric: tabular-nums; }
th, td { text-align: left; padding: 7px 10px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { color: var(--ink-2); font-weight: 700; font-size: 12.5px; text-transform: uppercase; letter-spacing: .05em; background: var(--surface-2); }
td.num, th.num { text-align: right; }
.tag { display: inline-block; font-size: 10.5px; font-weight: 800; letter-spacing: .06em; padding: 2px 6px; border-radius: 4px; vertical-align: 1px; white-space: nowrap; }
.tag.VERIFIED { background: color-mix(in srgb, var(--ok) 16%, transparent); color: var(--ok); }
.tag.REPORTED { background: color-mix(in srgb, var(--s1) 16%, transparent); color: var(--s1); }
.tag.ESTIMATE { background: color-mix(in srgb, var(--warn) 16%, transparent); color: var(--warn); }
.tag.ASSUMPTION { background: color-mix(in srgb, var(--ink-3) 20%, transparent); color: var(--ink-2); }
figure { margin: 22px 0; }
figure.img img { width: 100%; height: auto; border-radius: 12px; display: block; background: var(--surface-2); }
figure.img figcaption, .viz figcaption { color: var(--ink-3); font-size: 13.5px; margin-top: 8px; }
.gallery { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }
@media (max-width: 760px) { .gallery { grid-template-columns: minmax(0, 1fr); } }
.sheet { background: #fbfaf7; border-radius: 10px; padding: 6px; border: 1px solid var(--line); }
/* charts */
.viz { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 16px 16px 10px; }
.viz figcaption { margin: 0 0 6px; display: flex; flex-direction: column; gap: 2px; }
.viz .viz-title { color: var(--ink); font-weight: 700; font-size: 15px; }
.viz .viz-sub { color: var(--ink-3); font-size: 13px; }
.viz-svg { overflow-x: auto; }
.viz svg { width: 100%; height: auto; display: block; min-width: 520px; font-family: var(--font-body); }
.viz .grid { stroke: var(--grid); stroke-width: 1; }
.viz .axis { stroke: var(--ink-3); stroke-width: 1; }
.viz .tick { fill: var(--ink-3); font-size: 11.5px; }
.viz .cat { fill: var(--ink-2); font-size: 12.5px; }
.viz .val { fill: var(--ink); font-size: 12px; font-weight: 700; }
.viz .hit { fill: transparent; }
.viz .mark:hover path, .viz .mark:focus path, .viz .mark:hover rect:not(.hit), .viz .mark:focus rect:not(.hit) { filter: brightness(1.12); }
.viz .mark:focus { outline: none; }
.viz .line { fill: none; stroke-width: 2; stroke-linejoin: round; stroke-linecap: round; }
.viz .area { opacity: .1; }
.viz .dot { stroke: var(--surface); stroke-width: 2; }
.viz .ref { stroke: var(--ink-3); stroke-width: 1; stroke-dasharray: 4 4; }
.viz .whisker { stroke: var(--ink-2); stroke-width: 1.2; }
.viz .xhair { stroke: var(--ink-3); stroke-width: 1; opacity: 0; }
.viz .col:hover .xhair, .viz .col:focus .xhair { opacity: .7; }
.viz .cell { font-size: 11px; fill: var(--ink); font-variant-numeric: tabular-nums; }
.viz .cell-dark { fill: #fff; }
.viz .risk-dot { fill: var(--brand); stroke: var(--surface); stroke-width: 2; }
.viz .risk-id { fill: var(--surface); font-size: 10px; font-weight: 800; }
.legend { display: flex; flex-wrap: wrap; gap: 14px; margin: 4px 0 8px; font-size: 13px; color: var(--ink-2); }
.legend .lg { display: inline-flex; align-items: center; gap: 6px; }
.key-rect { width: 12px; height: 12px; border-radius: 3px; background: var(--k); display: inline-block; }
.key-line { width: 16px; height: 2px; background: var(--k); display: inline-block; border-radius: 2px; }
.viz-note { color: var(--ink-3); font-size: 12.5px; margin: 6px 0 0; }
details.viz-table { margin-top: 6px; font-size: 13px; }
details.viz-table summary { cursor: pointer; color: var(--ink-3); }
#tip { position: fixed; pointer-events: none; z-index: 50; background: var(--ink); color: var(--bg); font-size: 12.5px; padding: 6px 9px; border-radius: 6px; max-width: 320px; opacity: 0; transition: opacity .08s; font-variant-numeric: tabular-nums; }
/* map */
.corridor-map { width: 100%; height: auto; display: block; border-radius: 12px; }
.m-bg { fill: var(--surface-2); } .m-water { fill: color-mix(in srgb, var(--s1) 30%, var(--surface)); stroke: none; }
.m-road-m4 { fill: none; stroke: var(--accent); stroke-width: 3.2; stroke-linecap: round; }
.m-road-m { fill: none; stroke: var(--ink-2); stroke-width: 1.6; } .m-road-h { fill: none; stroke: var(--ink-3); stroke-width: 1; }
.m-poi-fuel { fill: var(--warn); } .m-poi-food { fill: var(--s1); } .m-poi-jct { fill: var(--ink); }
.m-city { fill: var(--ink); } .m-town { fill: var(--ink-2); }
.m-label { font: 12px var(--font-body); fill: var(--ink-2); } .m-label-city { font: 700 15px var(--font-body); fill: var(--ink); }
.m-comp path { fill: var(--bad); } .m-label-comp { font: 700 11.5px var(--font-body); fill: var(--bad); }
.m-site circle { fill: var(--surface); stroke: var(--brand); stroke-width: 2.5; } .m-site-top circle { fill: var(--brand); stroke: var(--surface); stroke-width: 2.5; }
.m-site-num { font: 800 11px var(--font-body); text-anchor: middle; fill: var(--brand); } .m-site-top .m-site-num { fill: var(--surface); }
.m-label-site { font: 700 12.5px var(--font-body); fill: var(--ink); paint-order: stroke; stroke: var(--surface-2); stroke-width: 3px; }
.m-scale line { stroke: var(--ink); stroke-width: 2; } .m-scale text, .m-credit { font: 10.5px var(--font-body); fill: var(--ink-3); }
/* 3D */
.viewer { position: relative; border-radius: 14px; overflow: hidden; background: var(--surface-2); aspect-ratio: 16/9; max-width: 100%; }
.viewer canvas { width: 100% !important; height: 100% !important; display: block; }
.viewer .hint { position: absolute; left: 12px; bottom: 10px; font-size: 12px; color: var(--ink-2); background: color-mix(in srgb, var(--surface) 80%, transparent); padding: 4px 8px; border-radius: 6px; }
.viewer .views { position: absolute; right: 10px; top: 10px; display: flex; gap: 6px; flex-wrap: wrap; }
.viewer button { font: 600 12px var(--font-body); border: 1px solid var(--line); background: var(--surface); color: var(--ink); padding: 5px 9px; border-radius: 6px; cursor: pointer; }
.viewer button:focus-visible { outline: 2px solid var(--accent); }
.swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; }
.sw { border: 1px solid var(--line); border-radius: 10px; overflow: hidden; background: var(--surface); }
.sw .c { height: 74px; } .sw .t { padding: 8px 10px; font-size: 12.5px; } .sw .t b { display: block; font-size: 13.5px; }
.typespec { background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 18px; }
.pill { display: inline-block; padding: 2px 9px; border-radius: 999px; background: var(--surface-2); font-size: 12.5px; color: var(--ink-2); margin: 2px 4px 2px 0; }
.foot { color: var(--ink-3); font-size: 13px; padding-block: 30px; border-top: 1px solid var(--line); }
.toc-mobile { display: none; } @media (max-width: 1000px) { .toc-mobile { display: block; margin-bottom: 24px; } }
"""

JS = r"""
(function(){
  const tip = document.getElementById('tip');
  function show(e, el){ tip.textContent = el.getAttribute('data-tip'); tip.style.opacity = 1; move(e, el); }
  function move(e, el){ let x, y; if (e && e.clientX !== undefined && e.type !== 'focusin') { x = e.clientX; y = e.clientY; }
    else { const r = el.getBoundingClientRect(); x = r.left + r.width/2; y = r.top; }
    const w = tip.offsetWidth, h = tip.offsetHeight; let L = x + 14, T = y - h - 10;
    if (L + w > window.innerWidth - 8) L = x - w - 14; if (T < 8) T = y + 16; tip.style.left = L + 'px'; tip.style.top = T + 'px'; }
  document.addEventListener('pointerover', e => { const el = e.target.closest('[data-tip]'); if (el) show(e, el); });
  document.addEventListener('pointermove', e => { const el = e.target.closest('[data-tip]'); if (el) move(e, el); else tip.style.opacity = 0; });
  document.addEventListener('pointerout', e => { if (!e.relatedTarget || !e.relatedTarget.closest || !e.relatedTarget.closest('[data-tip]')) tip.style.opacity = 0; });
  document.addEventListener('focusin', e => { const el = e.target.closest && e.target.closest('[data-tip]'); if (el) show(e, el); });
  document.addEventListener('focusout', () => { tip.style.opacity = 0; });
})();
"""

VIEWER_JS = r"""
(function(){
  const box = document.getElementById('viewer3d'); if (!box || !window.THREE) return;
  const W = () => box.clientWidth, H = () => box.clientHeight;
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); renderer.setSize(W(), H());
  renderer.outputEncoding = THREE.sRGBEncoding; renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  box.prepend(renderer.domElement);
  const scene = new THREE.Scene(); scene.background = new THREE.Color(0xcfdde4); scene.fog = new THREE.Fog(0xcfdde4, 260, 700);
  const cam = new THREE.PerspectiveCamera(35, W()/H(), 0.5, 2000);
  const ctl = new THREE.OrbitControls(cam, renderer.domElement); ctl.enableDamping = true; ctl.maxPolarAngle = Math.PI*0.495; ctl.minDistance = 8; ctl.maxDistance = 320;
  scene.add(new THREE.HemisphereLight(0xffffff, 0x8a7a66, 0.75));
  const sun = new THREE.DirectionalLight(0xfff1dc, 0.95); sun.position.set(60, 90, 50); sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048); Object.assign(sun.shadow.camera, { left: -80, right: 80, top: 80, bottom: -80, near: 1, far: 300 }); scene.add(sun);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(2000, 2000), new THREE.MeshLambertMaterial({ color: 0x8c8a5c }));
  ground.rotation.x = -Math.PI/2; ground.position.y = -0.08; ground.receiveShadow = true; scene.add(ground);
  // glTF is Y-up; Blender X(east) -> X, Blender Y(north) -> -Z
  const V = { aerial: [[112,62,64],[37,0,-19]], hero: [[66.5,1.8,-3.2],[36,4.4,-25.5]], drive: [[52,1.6,-37],[32,2.2,-33.6]], plan: [[37,190,-21],[37,0,-20.9]] };
  function go(k){ const [p,t] = V[k]; cam.position.set(...p); ctl.target.set(...t); ctl.update(); }
  go('aerial');
  box.querySelectorAll('button[data-view]').forEach(b => b.addEventListener('click', () => go(b.dataset.view)));
  new THREE.GLTFLoader().load(box.dataset.src, g => {
    g.scene.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; if (o.material && o.material.transparent) o.material.depthWrite = false; } });
    scene.add(g.scene); box.querySelector('.hint').textContent = 'Drag to orbit · scroll or pinch to zoom · right-drag to pan';
  }, undefined, () => { box.querySelector('.hint').textContent = 'The 3D model could not be loaded in this viewer.'; });
  const ro = new ResizeObserver(() => { cam.aspect = W()/H(); cam.updateProjectionMatrix(); renderer.setSize(W(), H()); }); ro.observe(box);
  (function loop(){ requestAnimationFrame(loop); ctl.update(); renderer.render(scene, cam); })();
})();
"""


def page(title, description_meta, nav_items, body_html, brand_name, include_viewer=True):
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@600;700;800&family=Manrope:wght@400;500;600;700;800'
             '&family=Noto+Sans+Armenian:wght@400;600;700;800&display=swap">')
    nav = "".join(f'<li><a href="#{a}"><span class="n">{i + 1:02d}</span><span>{t}</span></a></li>' for i, (a, t) in enumerate(nav_items))
    scripts = ""
    if include_viewer:
        scripts = ('<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>'
                   '<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>'
                   '<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>'
                   f'<script>{VIEWER_JS}</script>')
    return (f'<title>{title}</title><meta name="description" content="{description_meta}">{fonts}<style>{CSS}</style>'
            f'<div class="wrap"><nav class="rail" aria-label="Chapters"><div class="brandline">{brand_name}</div><ol>{nav}</ol></nav>'
            f'<main>{body_html}</main></div><div id="tip" role="tooltip"></div><script>{JS}</script>{scripts}')
