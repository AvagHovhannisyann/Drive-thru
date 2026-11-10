#!/usr/bin/env node
/* Render a web page to a numbered PNG sequence, one frame per film frame, deterministically.

     node tools/film/html_frames.cjs PAGE.html OUT_DIR --duration 6 [--fps 24] [--size 1920x1200]
          [--scale 1] [--name ui] [--start 0] [--transparent]

   The page is never played in real time. For every frame the tool sets the time and takes a
   screenshot, so a slow machine gives the same pictures as a fast one. A page takes part by
   defining   window.seek = (t) => { ...draw the state at t seconds... }   (may return a Promise).
   CSS animations and Web Animations are also moved to t, so plain CSS pages work without seek().
   Uses the Chromium that is already installed with Playwright.
*/
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

const args = process.argv.slice(2);
const flag = (name, fallback) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : fallback; };
const [page_, outDir] = args;
if (!page_ || !outDir) { console.error('usage: html_frames.cjs PAGE.html OUT_DIR --duration S [--fps 24] [--size WxH]'); process.exit(2); }
const fps = Number(flag('--fps', 24));
const duration = Number(flag('--duration', 5));
const start = Number(flag('--start', 0));
const [width, height] = flag('--size', '1920x1200').split('x').map(Number);
const scale = Number(flag('--scale', 1));
const name = flag('--name', 'ui');
const transparent = args.includes('--transparent');

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: scale });
  const page = await context.newPage();
  page.on('pageerror', (e) => { console.error('page error:', e.message); process.exitCode = 1; });
  const url = /^https?:|^file:/.test(page_) ? page_ : 'file://' + path.resolve(page_);
  await page.goto(url, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const frames = Math.round(duration * fps);
  for (let i = 0; i < frames; i++) {
    const t = start + i / fps;
    await page.evaluate(async (time) => {
      for (const a of document.getAnimations()) { a.pause(); a.currentTime = time * 1000; }
      if (typeof window.seek === 'function') await window.seek(time);
      await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
    }, t);
    const file = path.join(outDir, `${name}_${String(i + 1).padStart(4, '0')}.png`);
    await page.screenshot({ path: file, omitBackground: transparent, type: 'png' });
    if ((i + 1) % 48 === 0 || i + 1 === frames) console.log(`  ${i + 1}/${frames} frames`);
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
