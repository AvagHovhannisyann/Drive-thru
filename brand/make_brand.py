"""
Brand identity generator.

Writes brand/out/: logo suite (SVG), packaging artwork, signage & menu-board textures (PNG) for the
Blender scenes, uniforms flats, roadside sign, app screen, and brand.json (single source of truth for
name, colours, fonts and texture paths used by design/3d/*.py, design/drawings and the report).

Run:  python3 brand/make_brand.py        (needs Playwright/Chromium for PNG rasterisation)
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "brand/out"
OUT.mkdir(parents=True, exist_ok=True)
CFG = json.loads((ROOT / "brand/brand_config.json").read_text())

NAME = CFG["name_latin"]
NAME_HY = CFG["name_armenian"]
NAME_RU = CFG.get("name_russian", "")
TAG_EN = CFG["tagline_en"]
TAG_HY = CFG["tagline_hy"]
C = CFG["colors"]
FD = CFG["fonts"]["display"]
FB = CFG["fonts"]["body"]
FA = CFG["fonts"]["armenian"]
FONT_D = f"'{FD}', '{FA}', sans-serif"
FONT_B = f"'{FB}', '{FA}', sans-serif"
FONT_A = f"'{FA}', sans-serif"
MENU = CFG["menu"]

# ======================================================================================
# Symbol: an arch (Armenian tuff portal / the building's frame) holding a rising sun over two road bands
# ======================================================================================
ARCH = "M0,120 V50 A50,50 0 0 1 100,50 V120 Z"


def symbol(fill_arch, fill_sun, x=0, y=0, s=1.0, extra=""):
    """Nested portal arch (archivolt of Armenian tuff architecture) with the sun rising at its threshold."""
    inner = "M17,120 V52 A33,33 0 0 1 83,52 V120"
    return (f'<g transform="translate({x},{y}) scale({s})" {extra}>'
            f'<path d="{ARCH}" fill="{fill_arch}"/>'
            f'<path d="{inner}" fill="none" stroke="{fill_sun}" stroke-width="8"/>'
            f'<path d="M27,120 A23,23 0 0 1 73,120 Z" fill="{fill_sun}"/>'
            f'</g>')


def svg(w, h, body, bg=None, defs=""):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<defs>{defs}</defs>{b}{body}</svg>')


def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size, fill, family=None, weight=800, anchor="start", ls=0, extra="", tl=None):
    family = family or FONT_D
    s = esc(s)
    if tl:  # lock the rendered width so the lock-up is identical whatever font the viewer resolves
        return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
                f'text-anchor="{anchor}" textLength="{tl:.1f}" lengthAdjust="spacingAndGlyphs" {extra}>{s}</text>')
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" {extra}>{s}</text>')


FONT_FILES = {"display": "/root/.fonts/Unbounded-800.ttf", "armenian": "/root/.fonts/NotoSansArmenian-800.ttf"}


def measure(s, kind, size, ls=0.0):
    """Advance width in px of string s set in the brand font (fontTools), plus letter-spacing between glyphs."""
    try:
        from fontTools.ttLib import TTFont
        t = TTFont(FONT_FILES[kind]); cmap = t.getBestCmap(); hm = t["hmtx"]; upm = t["head"].unitsPerEm
        w = sum(hm[cmap[ord(c)]][0] for c in s) / upm * size
    except Exception:
        w = len(s) * size * (0.66 if kind == "display" else 0.48)
    return w + ls * (len(s) - 1)


def fmt_price(v):
    """1400 -> '1 400'; '1100/1400' -> '1 100 / 1 400'."""
    parts = str(v).split("/")
    return " / ".join(f"{int(x):,}".replace(",", " ") for x in parts)


def write(name, content):
    p = OUT / name
    p.write_text(content)
    return p


# ---- logo suite -------------------------------------------------------------------------
def logos():
    files = {}
    files["symbol"] = write("logo_symbol.svg", svg(100, 120, symbol(C["accent"], C["light"])))
    files["symbol_dark"] = write("logo_symbol_on_dark.svg", svg(140, 160, symbol(C["accent"], C["primary"], 20, 20), bg=C["primary"]))
    wH = measure(NAME, "display", 92, 4)
    files["horizontal"] = write("logo_horizontal.svg", svg(int(140 + wH + 24), 160,
        symbol(C["accent"], C["light"], 10, 20) + text(140, 116, NAME, 92, C["primary"], tl=wH)))
    files["horizontal_rev"] = write("logo_horizontal_reverse.svg", svg(int(160 + wH + 40), 200,
        symbol(C["accent"], C["primary"], 30, 40) + text(160, 136, NAME, 92, C["light"], tl=wH), bg=C["primary"]))
    wS, wSa = measure(NAME, "display", 64, 4), measure(NAME_HY, "armenian", 44, 6)
    W = int(max(wS, wSa) + 70)
    files["stacked"] = write("logo_stacked.svg", svg(W, 400,
        symbol(C["accent"], C["light"], W / 2 - 50, 36) + text(W / 2, 262, NAME, 64, C["primary"], anchor="middle", tl=wS)
        + text(W / 2, 330, NAME_HY, 44, C["primary"], family=FONT_A, anchor="middle", weight=700, tl=wSa)))
    wA, wL = measure(NAME_HY, "armenian", 92, 6), measure(NAME, "display", 84, 4)
    xr = 150 + wA + 30
    files["bilingual"] = write("logo_bilingual.svg", svg(int(xr + 32 + wL + 30), 200,
        symbol(C["accent"], C["light"], 20, 30) + text(150, 132, NAME_HY, 92, C["primary"], family=FONT_A, weight=800, tl=wA)
        + f'<rect x="{xr:.0f}" y="58" width="3" height="84" fill="{C["accent"]}"/>'
        + text(xr + 32, 129, NAME, 84, C["primary"], tl=wL)))
    wW = measure(NAME, "display", 100, 5)
    files["wordmark"] = write("wordmark.svg", svg(int(wW + 30), 140, text(10, 112, NAME, 100, C["primary"], tl=wW)))
    return files


# ---- PNG rasterisation via Chromium ---------------------------------------------------------
JOBS = []


def png(name, w, h, inner_svg, transparent=False):
    p = write(name.replace(".png", ".svg"), inner_svg)
    JOBS.append((str(p), str(OUT / name), w, h, transparent))
    return OUT / name


def rasterise():
    script = ROOT / "brand/_raster.js"
    script.write_text("""
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  for (const [src, out, w, h, transparent] of jobs) {
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    const html = path.join(path.dirname(src), '_wrap.html');
    fs.writeFileSync(html, `<html><head><style>html,body{margin:0;background:${transparent ? 'transparent' : '#fff'}}</style></head><body><img src="${path.basename(src)}" width="${w}" height="${h}"></body></html>`);
    await page.goto('file://' + html); await page.waitForTimeout(300);
    await page.screenshot({ path: out, omitBackground: !!transparent });
    await page.close();
  }
  await browser.close();
})();
""")
    jf = OUT / "_jobs.json"
    jf.write_text(json.dumps(JOBS))
    env_node = "/tmp/claude-0/-home-user-Drive-thru/29307adb-6a27-5feb-96a7-e9f259e01769/scratchpad/node_modules"
    subprocess.run(["node", str(script), str(jf)], check=True, env={"NODE_PATH": env_node, "PATH": "/opt/node22/bin:/usr/bin:/bin",
                                                                     "HOME": "/root", "PLAYWRIGHT_BROWSERS_PATH": "/opt/pw-browsers"})
    (OUT / "_wrap.html").unlink(missing_ok=True)
    jf.unlink()
    script.unlink()


# ---- packaging artwork -----------------------------------------------------------------------
def pattern_defs(color, bg):
    # repeating mini-arch pattern (brand texture)
    return (f'<pattern id="arches" patternUnits="userSpaceOnUse" width="56" height="64">'
            f'<rect width="56" height="64" fill="{bg}"/>'
            f'<path d="M8,60 V30 A20,20 0 0 1 48,30 V60" fill="none" stroke="{color}" stroke-width="3"/></pattern>')


def packaging():
    P, A, L, T = C["primary"], C["accent"], C["light"], C["tuff"]
    # hot cup wrap: 2048 x 650 (u = around, v = height). Two logo faces opposite each other.
    W_, H_ = 2048, 650
    body = f'<rect width="{W_}" height="{H_}" fill="{L}"/>'
    body += f'<rect y="{H_ - 120}" width="{W_}" height="120" fill="{P}"/>'
    body += f'<rect y="0" width="{W_}" height="34" fill="{P}"/>'
    for cx in (512, 1536):
        body += symbol(A, L, cx - 95, 150, 1.9)
        body += text(cx, 470, NAME, 82, P, anchor="middle", ls=6)
    for cx in (0, 1024, 2048):
        body += text(cx - 10, 330, TAG_HY, 34, P, family=FONT_A, anchor="middle", weight=600) if cx == 1024 else ""
    body += text(1024, 400, TAG_EN.upper(), 26, A, anchor="middle", ls=6, weight=700)
    body += text(1024, H_ - 50, f"{NAME} · {NAME_HY} · DRIVE-THRU", 30, L, anchor="middle", ls=8, weight=700)
    png("cup_wrap.png", W_, H_, svg(W_, H_, body))
    # sleeve
    W_, H_ = 2048, 420
    body = f'<rect width="{W_}" height="{H_}" fill="{A}"/>'
    for i, cx in enumerate(range(128, W_, 256)):
        body += symbol(P, A, cx - 45, 120, 0.9) if i % 2 == 0 else text(cx, 245, NAME_HY, 54, P, family=FONT_A, anchor="middle", weight=800)
    png("sleeve.png", W_, H_, svg(W_, H_, body))
    # iced cup print (transparent background)
    W_, H_ = 2048, 650
    body = ""
    for cx in (512, 1536):
        body += symbol(A, "#ffffff", cx - 70, 230, 1.4)
        body += text(cx, 470, NAME, 74, "#ffffff", anchor="middle", ls=6)
    png("iced_wrap.png", W_, H_, svg(W_, H_, body), transparent=True)
    # bag front (portrait 900 x 1450)
    W_, H_ = 900, 1450
    body = f'<rect width="{W_}" height="{H_}" fill="#a8774a"/>'
    body += f'<rect y="0" width="{W_}" height="150" fill="{P}"/>'
    body += symbol(A, "#a8774a", 300, 420, 3.0)
    body += text(450, 920, NAME, 118, P, anchor="middle", ls=8)
    body += text(450, 1010, NAME_HY, 74, P, family=FONT_A, anchor="middle", weight=700, ls=8)
    body += text(450, 1250, TAG_EN, 40, P, family=FONT_B, anchor="middle", weight=600)
    body += text(450, 1310, TAG_HY, 40, P, family=FONT_A, anchor="middle", weight=600)
    png("bag_front.png", W_, H_, svg(W_, H_, body))
    # pastry box top (square)
    W_ = 1200
    body = f'<rect width="{W_}" height="{W_}" fill="url(#arches)"/>'
    body += f'<rect x="250" y="400" width="700" height="400" rx="200" fill="{L}"/>'
    body += symbol(A, L, 290, 470, 2.2) + text(540, 680, NAME, 92, P, ls=4)
    png("box_top.png", W_, W_, svg(W_, W_, body, defs=pattern_defs(T, L)))
    # retail beans bag
    W_, H_ = 700, 1400
    body = f'<rect width="{W_}" height="{H_}" fill="{P}"/>'
    body += symbol(A, P, 230, 230, 2.4)
    body += text(350, 700, NAME, 96, L, anchor="middle", ls=6)
    body += text(350, 800, "ROAD BLEND", 54, A, anchor="middle", ls=8)
    body += text(350, 870, "Espresso · 1 kg", 40, L, family=FONT_B, anchor="middle", weight=600)
    body += text(350, 940, "Roasted in Armenia", 34, L, family=FONT_B, anchor="middle", weight=500)
    png("beans_front.png", W_, H_, svg(W_, H_, body))


# ---- signage & screens -----------------------------------------------------------------------
def menu_board(w, h, compact=False):
    """Armenian leads (Law on Language Art. 4 / Law on Advertising Art. 5): Armenian names larger and first, English below."""
    P, A, L = C["primary"], C["accent"], C["light"]
    body = f'<rect width="{w}" height="{h}" fill="{P}"/>'
    wA = measure(NAME_HY, "armenian", 70, 4)
    wL = measure(NAME, "display", 40, 3)
    body += symbol(A, P, 60, 50, 0.9) + text(170, 132, NAME_HY, 70, L, family=FONT_A, tl=wA)
    body += text(170 + wA + 24, 132, NAME, 40, A, tl=wL)
    body += text(w - 60, 112, "Պատվեր", 44, A, family=FONT_A, anchor="end", weight=800)
    body += text(w - 60, 146, "Order here", 24, "#c9d6d3", family=FONT_B, anchor="end", weight=600)
    cols = MENU["sections"][: (2 if compact else 3)]
    cw = (w - 120) / len(cols)
    for i, sec in enumerate(cols):
        x = 60 + i * cw
        body += text(x, 240, sec["title_hy"], 36, A, family=FONT_A, weight=800)
        body += text(x, 276, sec["title_en"].upper(), 22, "#c9d6d3", ls=3, weight=700)
        for j, it in enumerate(sec["items"][: (4 if compact else 6)]):
            y = 350 + j * 78
            body += text(x, y, it["hy"], 34, L, family=FONT_A, weight=700)
            body += text(x, y + 30, it["en"], 22, "#c9d6d3", family=FONT_B, weight=500)
            body += text(x + cw - 40, y, fmt_price(it["price"]), 36, A, family=FONT_B, anchor="end", weight=800)
    body += f'<rect y="{h - 80}" width="{w}" height="80" fill="{A}"/>'
    body += text(w / 2, h - 28, "Քարտ · Apple Pay · Google Pay · Idram   |   Գները՝ ՀՀ դրամով · Prices in AMD", 30, P, family=FONT_A, anchor="middle", weight=700)
    return svg(w, h, body)


def signage():
    P, A, L = C["primary"], C["accent"], C["light"]
    tex = {}
    tex["logo_tower"] = png("tex_logo_tower.png", 1024, 1024, svg(1024, 1024, f'<rect width="1024" height="1024" fill="{P}"/>' + symbol(A, P, 262, 200, 5.0)))
    tex["logo_badge"] = png("tex_logo_badge.png", 1024, 1024, svg(1024, 1024, f'<rect width="1024" height="1024" fill="{A}"/>' + symbol(P, A, 312, 170, 4.0)
                                                                      + text(512, 900, NAME, 104, P, anchor="middle", ls=8)))
    # pylon face: 1.9 x 4.8 m -> 760 x 1920
    w, h = 760, 1920
    body = f'<rect width="{w}" height="{h}" fill="{P}"/>' + symbol(A, P, 180, 140, 4.0)
    body += text(w / 2, 790, NAME_HY, 132, L, family=FONT_A, anchor="middle", weight=800, ls=8)
    body += text(w / 2, 900, NAME, 96, A, anchor="middle", ls=6)
    body += f'<rect x="80" y="960" width="{w - 160}" height="4" fill="{A}"/>'
    for i, (en, hy) in enumerate([("DRIVE-THRU", "ԴՐԱՅՎ-ԹՐՈՒ"), ("COFFEE · BAKERY", "ՍՈՒՐՃ · ԹԽՎԱԾՔ"), ("WC · EV · TERRACE", "ԶՈՒԳԱՐԱՆ · ԼԻՑՔԱՎՈՐՈՒՄ")]):
        body += text(w / 2, 1060 + i * 150, en, 60, A, anchor="middle", ls=4)
        body += text(w / 2, 1110 + i * 150, hy, 36, L, family=FONT_A, anchor="middle", weight=600)
    body += f'<rect y="{h - 230}" width="{w}" height="230" fill="{A}"/>'
    body += text(w / 2, h - 135, "07:00 – 23:00", 78, P, family=FONT_B, anchor="middle", weight=800)
    body += text(w / 2, h - 65, "every day · ամեն օր", 44, P, family=FONT_A, anchor="middle", weight=700)
    tex["pylon_face"] = png("tex_pylon_face.png", w, h, svg(w, h, body))
    # fascia wordmark (bronze-halo letters): transparent PNG 2400 x 140
    tex["wordmark_fascia"] = png("tex_wordmark_fascia.png", 2400, 140,
                                  svg(2400, 140, text(1200, 112, f"{NAME}   ·   {NAME_HY}", 110, L, anchor="middle", ls=16)), transparent=True)
    tex["wordmark_vertical"] = png("tex_wordmark_vertical.png", 240, 1440,
                                    svg(240, 1440, text(0, 0, NAME, 170, L, ls=20, extra='transform="translate(170,60) rotate(90)"')), transparent=True)
    for wid, en, hy in (("W1", "PAY & CONFIRM", "ՎՃԱՐՈՒՄ"), ("W2", "PICK UP · CHAMPAD BATS!", "ՃԱՄՓԱԴ ԲԱՑ")):
        tex[f"window_{wid}"] = png(f"tex_window_{wid}.png", 1600, 90, svg(1600, 90, f'<rect width="1600" height="90" fill="{P}"/>'
                                    + text(40, 62, f"{wid}", 50, A) + text(150, 62, hy, 46, L, family=FONT_A, weight=800) + text(1560, 60, en, 30, "#c9d6d3", anchor="end", ls=3)))
    tex["menu_board"] = png("tex_menu_board.png", 1920, 1100, menu_board(1920, 1100))
    tex["menu_interior"] = png("tex_menu_interior.png", 1920, 1080, menu_board(1920, 1080, compact=True))
    # preview board (promo)
    w, h = 1100, 1000
    body = f'<rect width="{w}" height="{h}" fill="{A}"/>' + symbol(P, A, 80, 90, 1.3)
    body += text(80, 430, CFG["promo"]["hy"], 66, P, family=FONT_A, weight=800)
    body += text(80, 530, CFG["promo"]["en"] + " " + CFG["promo"]["en2"], 50, P, ls=1)
    body += f'<rect x="80" y="720" width="{w - 160}" height="160" rx="80" fill="{P}"/>'
    body += text(w / 2, 825, CFG["promo"]["price"], 76, L, family=FONT_B, anchor="middle", weight=800)
    tex["preview_board"] = png("tex_preview_board.png", w, h, svg(w, h, body))
    return tex


def roadside_and_app():
    P, A, L = C["primary"], C["accent"], C["light"]
    # advance directional sign (where permitted) 3:1
    w, h = 1800, 600
    body = f'<rect width="{w}" height="{h}" fill="{P}"/>' + symbol(A, P, 70, 90, 3.4)
    body += text(470, 220, NAME_HY, 130, L, family=FONT_A, weight=800, ls=6) + text(470, 330, NAME, 92, A, ls=6)
    body += text(470, 455, "Սուրճ · Թխվածք · WC", 60, A, family=FONT_A, weight=800)
    body += text(470, 525, "Drive-thru coffee · bakery · WC", 38, "#c9d6d3", family=FONT_B, weight=700)
    body += f'<g transform="translate(1500,300)"><circle r="190" fill="{A}"/><text y="-10" text-anchor="middle" font-family="{FONT_B}" font-size="150" font-weight="800" fill="{P}">2</text><text y="90" text-anchor="middle" font-family="{FONT_B}" font-size="64" font-weight="800" fill="{P}">km →</text></g>'
    png("roadside_sign.png", w, h, svg(w, h, body))
    # billboard 3:1 (Yerevan city edge, where outdoor ads permitted)
    body = f'<rect width="{w}" height="{h}" fill="{A}"/>'
    body += text(90, 200, "Ճամփադ բաց։", 104, P, family=FONT_A, weight=800)
    body += text(90, 320, "Սուրճը՝ 3 րոպեում", 84, P, family=FONT_A, weight=800)
    body += text(90, 450, CFG["campaign"]["en"] + " " + CFG["campaign"]["en2"], 54, P, ls=1)
    body += symbol(P, A, 1430, 70, 2.5) + text(1555, 510, NAME, 70, P, anchor="middle", ls=4)
    png("billboard.png", w, h, svg(w, h, body))
    # app screen (390 x 844)
    w, h = 390, 844
    body = f'<rect width="{w}" height="{h}" fill="{L}"/><rect width="{w}" height="300" fill="{P}"/>'
    body += symbol(A, P, 24, 48, 0.42) + text(80, 92, NAME, 30, L, ls=2)
    body += text(24, 170, "Barev, Ani!", 30, L, family=FONT_B, weight=800)
    body += text(24, 206, "Your usual is 2 min away.", 18, "#c9d6d3", family=FONT_B, weight=500)
    body += f'<rect x="24" y="232" width="342" height="46" rx="23" fill="{A}"/>' + text(195, 262, "Order ahead · skip the line", 17, P, family=FONT_B, anchor="middle", weight=800)
    body += f'<rect x="24" y="320" width="342" height="120" rx="18" fill="#ffffff"/>' + text(44, 356, "Road kilometres", 16, P, family=FONT_B, weight=800)
    body += text(44, 400, "70 / 100 km", 26, P, family=FONT_B, weight=800) + text(346, 400, "Free cup at 100 km", 14, A, family=FONT_B, anchor="end", weight=800)
    for i in range(10):
        body += f'<circle cx="{54 + i * 31}" cy="424" r="10" fill="{A if i < 7 else "#e7dfd3"}"/>'
    for i, it in enumerate(MENU["sections"][0]["items"][:4]):
        y = 470 + i * 84
        body += f'<rect x="24" y="{y}" width="342" height="72" rx="14" fill="#ffffff"/>'
        body += text(44, y + 32, it["hy"], 17, P, family=FONT_A, weight=800) + text(44, y + 56, it["en"], 13, "#6b6b6b", family=FONT_B, weight=500)
        body += text(346, y + 44, fmt_price(it["price"]) + " ֏", 17, P, family=FONT_B, anchor="end", weight=800)
    body += f'<rect x="0" y="{h - 70}" width="{w}" height="70" fill="#ffffff"/>'
    png("app_screen.png", w * 2, h * 2, svg(w, h, body).replace(f'width="{w}" height="{h}"', f'width="{w * 2}" height="{h * 2}"', 1))


def uniforms():
    P, A, L = C["primary"], C["accent"], C["light"]
    # flat technical drawings (apron, tee, cap) on one sheet
    body = f'<rect width="1500" height="700" fill="{L}"/>'
    # apron
    body += (f'<g transform="translate(80,80)"><path d="M90,0 H250 L250,70 Q330,90 340,160 L340,520 Q170,560 0,520 L0,160 Q10,90 90,70 Z" fill="{P}"/>'
             f'<path d="M90,0 Q60,-60 120,-80 M250,0 Q280,-60 220,-80" stroke="{A}" stroke-width="10" fill="none"/>'
             f'<rect x="60" y="330" width="220" height="120" rx="10" fill="none" stroke="{A}" stroke-width="5"/>'
             f'{symbol(A, P, 145, 150, 0.5)}<text x="170" y="270" text-anchor="middle" font-family="{FONT_D}" font-size="34" font-weight="800" fill="{L}">{NAME}</text>'
             f'<text x="170" y="620" text-anchor="middle" font-family="{FONT_B}" font-size="26" font-weight="700" fill="{P}">Crew apron — waxed cotton</text></g>')
    # tee
    body += (f'<g transform="translate(560,80)"><path d="M100,0 Q170,40 240,0 L340,40 L400,140 L330,170 L300,130 L300,520 L40,520 L40,130 L10,170 L-60,140 L0,40 Z" fill="{A}"/>'
             f'{symbol(P, A, 150, 120, 0.42)}<text x="170" y="290" text-anchor="middle" font-family="{FONT_D}" font-size="30" font-weight="800" fill="{P}">{NAME}</text>'
             f'<text x="170" y="330" text-anchor="middle" font-family="{FONT_A}" font-size="22" font-weight="700" fill="{P}">{NAME_HY}</text>'
             f'<text x="170" y="620" text-anchor="middle" font-family="{FONT_B}" font-size="26" font-weight="700" fill="{P}">Crew tee — apricot</text></g>')
    # cap + runner vest
    body += (f'<g transform="translate(1080,180)"><path d="M0,120 Q10,0 150,0 Q290,0 300,120 Z" fill="{P}"/><path d="M200,120 Q330,120 380,150 L210,150 Z" fill="{P}"/>'
             f'{symbol(A, P, 125, 30, 0.45)}'
             f'<text x="160" y="250" text-anchor="middle" font-family="{FONT_B}" font-size="26" font-weight="700" fill="{P}">Cap — basalt ink</text>'
             f'<rect x="40" y="300" width="250" height="160" rx="24" fill="{A}"/><text x="165" y="395" text-anchor="middle" font-family="{FONT_D}" font-size="34" font-weight="800" fill="{P}">RUNNER</text>'
             f'<text x="165" y="520" text-anchor="middle" font-family="{FONT_B}" font-size="26" font-weight="700" fill="{P}">Hi-vis runner vest (lane staff)</text></g>')
    png("uniforms.png", 1500, 700, svg(1500, 700, body))


def main():
    logos()
    packaging()
    tex = signage()
    roadside_and_app()
    uniforms()
    rasterise()
    brand = {k: CFG[k] for k in ("name_latin", "name_armenian", "name_russian", "tagline_en", "tagline_hy", "colors", "fonts")}
    brand["textures"] = {k: str(v) for k, v in tex.items()}
    (OUT / "brand.json").write_text(json.dumps(brand, indent=1, ensure_ascii=False))
    print("brand assets ->", OUT)


if __name__ == "__main__":
    main()
