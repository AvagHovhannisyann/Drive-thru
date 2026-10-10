"""
Inline-SVG chart helpers for the investor report.

Colours come from CSS custom properties (theme-aware): --s1/--s2/--s3 categorical (validated order),
--seq-1..--seq-5 sequential, --pos/--neg diverging, --grid, --ink, --ink-2, --ink-3, --surface.
Every chart ships: a legend for >=2 series, sparing direct labels, per-mark tooltips ([data-tip],
handled by the page script) and a table view in <details>.
Mark specs: bars <= 24px with 4px rounded data ends, 2px lines, >= 8px markers with 2px surface ring,
1px solid recessive gridlines.
"""
from __future__ import annotations

import html
import math

FONT = "var(--font-body)"


def esc(s):
    return html.escape(str(s), quote=True)


def nice_ticks(vmin, vmax, n=5):
    if vmax == vmin:
        vmax = vmin + 1
    span = vmax - vmin
    raw = span / n
    mag = 10 ** math.floor(math.log10(raw))
    step = min((1, 2, 2.5, 5, 10), key=lambda m: abs(m * mag - raw)) * mag
    lo = math.floor(vmin / step) * step
    hi = math.ceil(vmax / step) * step
    ticks = []
    v = lo
    while v <= hi + step * 0.001:
        ticks.append(round(v, 10))
        v += step
    return ticks


def compact(v, unit=""):
    a = abs(v)
    if a >= 1e9:
        s = f"{v / 1e9:.1f}B"
    elif a >= 1e6:
        s = f"{v / 1e6:.0f}M" if a >= 1e8 else f"{v / 1e6:.1f}M"
    elif a >= 1e3:
        s = f"{v / 1e3:.0f}K" if a >= 1e4 else f"{v / 1e3:.1f}K"
    else:
        s = f"{v:,.0f}" if abs(v) >= 10 or v == int(v) else f"{v:.2f}"
    return s.replace(".0M", "M").replace(".0K", "K") + unit


def table(headers, rows):
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<details class="viz-table"><summary>Show data table</summary><div class="tscroll"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div></details>'


def legend(items, kind="rect"):
    out = []
    for name, var in items:
        key = (f'<span class="key key-{kind}" style="--k: var({var})"></span>')
        out.append(f'<span class="lg">{key}{esc(name)}</span>')
    return f'<div class="legend">{"".join(out)}</div>'


def figure(svg, title, sub="", legend_html="", table_html="", note=""):
    t = f'<figcaption><span class="viz-title">{esc(title)}</span>' + (f'<span class="viz-sub">{esc(sub)}</span>' if sub else "") + "</figcaption>"
    n = f'<p class="viz-note">{note}</p>' if note else ""
    return f'<figure class="viz">{t}{legend_html}<div class="viz-svg">{svg}</div>{n}{table_html}</figure>'


def rbar_h(x0, y, w, h, r=4):
    """Horizontal bar: square at baseline (left), rounded data end (right)."""
    if w <= 0:
        return ""
    r = min(r, w, h / 2)
    return (f"M{x0:.1f},{y:.1f} H{x0 + w - r:.1f} Q{x0 + w:.1f},{y:.1f} {x0 + w:.1f},{y + r:.1f} V{y + h - r:.1f} "
            f"Q{x0 + w:.1f},{y + h:.1f} {x0 + w - r:.1f},{y + h:.1f} H{x0:.1f} Z")


def rbar_v(x, y0, w, h, r=4):
    """Vertical bar from baseline y0 upward (h>0) or downward (h<0) with rounded data end."""
    if abs(h) < 0.01:
        return ""
    r = min(r, abs(h), w / 2)
    if h > 0:
        top = y0 - h
        return (f"M{x:.1f},{y0:.1f} V{top + r:.1f} Q{x:.1f},{top:.1f} {x + r:.1f},{top:.1f} H{x + w - r:.1f} "
                f"Q{x + w:.1f},{top:.1f} {x + w:.1f},{top + r:.1f} V{y0:.1f} Z")
    bot = y0 - h
    return (f"M{x:.1f},{y0:.1f} V{bot - r:.1f} Q{x:.1f},{bot:.1f} {x + r:.1f},{bot:.1f} H{x + w - r:.1f} "
            f"Q{x + w:.1f},{bot:.1f} {x + w:.1f},{bot - r:.1f} V{y0:.1f} Z")


# ======================================================================================
def bar_h(rows, title, sub="", fmt=lambda v: f"{v:,.0f}", var="--s1", highlight=None, highlight_var="--s2", width=760,
          label_w=230, xmax=None, ranges=None, note="", unit_header="Value"):
    """rows: [(label, value)]; ranges: optional [(lo, hi)] drawn as a hairline whisker."""
    bh, gap = 20, 14
    top, bottom = 12, 30
    H = top + len(rows) * (bh + gap) + bottom
    plot_w = width - label_w - 70
    vmax = xmax or max(max(v for _, v in rows), max((r[1] for r in ranges), default=0) if ranges else 0) * 1.05
    ticks = nice_ticks(0, vmax, 5)
    vmax = ticks[-1]
    sx = lambda v: label_w + v / vmax * plot_w
    g = []
    for t in ticks:
        g.append(f'<line class="grid" x1="{sx(t):.1f}" x2="{sx(t):.1f}" y1="{top - 4}" y2="{H - bottom + 2}"/>'
                 f'<text class="tick" x="{sx(t):.1f}" y="{H - bottom + 18}" text-anchor="middle">{esc(compact(t))}</text>')
    for i, (lab, v) in enumerate(rows):
        y = top + i * (bh + gap)
        col = highlight_var if (highlight and lab in highlight) else var
        g.append(f'<text class="cat" x="{label_w - 10}" y="{y + bh * 0.72:.1f}" text-anchor="end">{esc(lab)}</text>')
        tip = f"{lab}: {fmt(v)}" + (f" (range {fmt(ranges[i][0])}–{fmt(ranges[i][1])})" if ranges else "")
        g.append(f'<g class="mark" tabindex="0" data-tip="{esc(tip)}"><rect class="hit" x="{label_w}" y="{y - gap / 2}" width="{plot_w + 60}" height="{bh + gap}"/>'
                 f'<path d="{rbar_h(label_w, y, sx(v) - label_w, bh)}" style="fill: var({col})"/></g>')
        if ranges:
            lo, hi = ranges[i]
            g.append(f'<line class="whisker" x1="{sx(lo):.1f}" x2="{sx(hi):.1f}" y1="{y + bh / 2:.1f}" y2="{y + bh / 2:.1f}"/>'
                     f'<line class="whisker" x1="{sx(lo):.1f}" x2="{sx(lo):.1f}" y1="{y + 5:.1f}" y2="{y + bh - 5:.1f}"/>'
                     f'<line class="whisker" x1="{sx(hi):.1f}" x2="{sx(hi):.1f}" y1="{y + 5:.1f}" y2="{y + bh - 5:.1f}"/>')
        lx = sx(max(v, ranges[i][1]) if ranges else v) + 6
        g.append(f'<text class="val" x="{lx:.1f}" y="{y + bh * 0.72:.1f}">{esc(fmt(v))}</text>')
    g.append(f'<line class="axis" x1="{label_w}" x2="{label_w}" y1="{top - 4}" y2="{H - bottom + 2}"/>')
    svg = f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="{esc(title)}">{"".join(g)}</svg>'
    tbl = table(["Item", unit_header] + (["Low", "High"] if ranges else []),
                [[l, fmt(v)] + ([fmt(ranges[i][0]), fmt(ranges[i][1])] if ranges else []) for i, (l, v) in enumerate(rows)])
    return figure(svg, title, sub, "", tbl, note)


def grouped_bars(cats, series, title, sub="", fmt=lambda v: f"{v:,.0f}", width=760, height=300, note="", zero_line=True):
    """series: [(name, var, [values per cat])]. Supports negatives."""
    left, right, top, bottom = 64, 16, 16, 34
    pw, ph = width - left - right, height - top - bottom
    allv = [v for _, _, vs in series for v in vs] + [0]
    ticks = nice_ticks(min(allv), max(allv), 5)
    lo, hi = ticks[0], ticks[-1]
    sy = lambda v: top + (hi - v) / (hi - lo) * ph
    g = []
    for t in ticks:
        g.append(f'<line class="grid" x1="{left}" x2="{width - right}" y1="{sy(t):.1f}" y2="{sy(t):.1f}"/>'
                 f'<text class="tick" x="{left - 8}" y="{sy(t) + 4:.1f}" text-anchor="end">{esc(compact(t))}</text>')
    band = pw / len(cats)
    n = len(series)
    bw = min(24, (band * 0.7 - (n - 1) * 2) / n)
    for i, c in enumerate(cats):
        cx = left + band * i + band / 2
        x0 = cx - (n * bw + (n - 1) * 2) / 2
        tip = f"{c}: " + " · ".join(f"{nm} {fmt(vs[i])}" for nm, _, vs in series)
        g.append(f'<g class="mark" tabindex="0" data-tip="{esc(tip)}"><rect class="hit" x="{left + band * i:.1f}" y="{top}" width="{band:.1f}" height="{ph}"/>')
        for j, (nm, var, vs) in enumerate(series):
            v = vs[i]
            g.append(f'<path d="{rbar_v(x0 + j * (bw + 2), sy(0), bw, sy(0) - sy(v))}" style="fill: var({var})"/>')
        g.append("</g>")
        g.append(f'<text class="tick" x="{cx:.1f}" y="{height - 12}" text-anchor="middle">{esc(c)}</text>')
    if zero_line and lo < 0:
        g.append(f'<line class="axis" x1="{left}" x2="{width - right}" y1="{sy(0):.1f}" y2="{sy(0):.1f}"/>')
    svg = f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">{"".join(g)}</svg>'
    lg = legend([(nm, var) for nm, var, _ in series]) if n > 1 else ""
    tbl = table([""] + [nm for nm, _, _ in series], [[c] + [fmt(vs[i]) for _, _, vs in series] for i, c in enumerate(cats)])
    return figure(svg, title, sub, lg, tbl, note)


def lines(xs, series, title, sub="", fmt=lambda v: f"{v:,.0f}", width=760, height=280, note="", y0=None, ref_line=None,
          x_every=1, end_labels=True, area_first=False):
    """series: [(name, var, [values])]."""
    left, right, top, bottom = 64, 168 if end_labels else 16, 16, 34
    pw, ph = width - left - right, height - top - bottom
    allv = [v for _, _, vs in series for v in vs] + ([y0] if y0 is not None else []) + ([ref_line[0]] if ref_line else [])
    ticks = nice_ticks(min(allv), max(allv), 5)
    lo, hi = ticks[0], ticks[-1]
    sx = lambda i: left + (i / (len(xs) - 1)) * pw
    sy = lambda v: top + (hi - v) / (hi - lo) * ph
    g = []
    for t in ticks:
        g.append(f'<line class="grid" x1="{left}" x2="{left + pw}" y1="{sy(t):.1f}" y2="{sy(t):.1f}"/>'
                 f'<text class="tick" x="{left - 8}" y="{sy(t) + 4:.1f}" text-anchor="end">{esc(compact(t))}</text>')
    for i, x in enumerate(xs):
        if i % x_every == 0:
            g.append(f'<text class="tick" x="{sx(i):.1f}" y="{height - 12}" text-anchor="middle">{esc(x)}</text>')
    if ref_line:
        v, lab = ref_line
        g.append(f'<line class="ref" x1="{left}" x2="{left + pw}" y1="{sy(v):.1f}" y2="{sy(v):.1f}"/>'
                 f'<text class="tick" x="{left + 4}" y="{sy(v) - 6:.1f}">{esc(lab)}</text>')
    for k, (nm, var, vs) in enumerate(series):
        pts = " ".join(f"{sx(i):.1f},{sy(v):.1f}" for i, v in enumerate(vs))
        if area_first and k == 0:
            g.append(f'<polygon class="area" style="fill: var({var})" points="{sx(0):.1f},{sy(max(lo, 0)):.1f} {pts} {sx(len(vs) - 1):.1f},{sy(max(lo, 0)):.1f}"/>')
        g.append(f'<polyline class="line" style="stroke: var({var})" points="{pts}"/>')
        g.append(f'<circle class="dot" cx="{sx(len(vs) - 1):.1f}" cy="{sy(vs[-1]):.1f}" r="4.5" style="fill: var({var})"/>')
        if end_labels:
            g.append(f'<text class="val" x="{sx(len(vs) - 1) + 10:.1f}" y="{sy(vs[-1]) + 4:.1f}">{esc(nm)} {esc(fmt(vs[-1]))}</text>')
    # crosshair columns
    colw = pw / max(1, len(xs) - 1)
    for i, x in enumerate(xs):
        tip = f"{x}: " + " · ".join(f"{nm} {fmt(vs[i])}" for nm, _, vs in series)
        g.append(f'<g class="col" tabindex="0" data-tip="{esc(tip)}"><rect class="hit" x="{sx(i) - colw / 2:.1f}" y="{top}" width="{colw:.1f}" height="{ph}"/>'
                 f'<line class="xhair" x1="{sx(i):.1f}" x2="{sx(i):.1f}" y1="{top}" y2="{top + ph}"/></g>')
    svg = f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">{"".join(g)}</svg>'
    lg = legend([(nm, var) for nm, var, _ in series], kind="line") if len(series) > 1 else ""
    tbl = table([""] + [nm for nm, _, _ in series], [[x] + [fmt(vs[i]) for _, _, vs in series] for i, x in enumerate(xs)])
    return figure(svg, title, sub, lg, tbl, note)


def stacked_bars(cats, parts, title, sub="", fmt=lambda v: f"{v:,.0f}", width=760, height=300, note="", total_fmt=None):
    """parts: [(name, var, [values per cat])] stacked bottom->top."""
    left, right, top, bottom = 64, 16, 22, 34
    pw, ph = width - left - right, height - top - bottom
    totals = [sum(p[2][i] for p in parts) for i in range(len(cats))]
    ticks = nice_ticks(0, max(totals), 5)
    hi = ticks[-1]
    sy = lambda v: top + (hi - v) / hi * ph
    g = []
    for t in ticks:
        g.append(f'<line class="grid" x1="{left}" x2="{width - right}" y1="{sy(t):.1f}" y2="{sy(t):.1f}"/>'
                 f'<text class="tick" x="{left - 8}" y="{sy(t) + 4:.1f}" text-anchor="end">{esc(compact(t))}</text>')
    band = pw / len(cats)
    bw = min(64, band * 0.5)
    for i, c in enumerate(cats):
        x = left + band * i + (band - bw) / 2
        acc = 0
        tip = f"{c}: total {fmt(totals[i])} · " + " · ".join(f"{nm} {fmt(vs[i])}" for nm, _, vs in parts)
        g.append(f'<g class="mark" tabindex="0" data-tip="{esc(tip)}"><rect class="hit" x="{left + band * i:.1f}" y="{top}" width="{band:.1f}" height="{ph}"/>')
        for k, (nm, var, vs) in enumerate(parts):
            v = vs[i]
            if v <= 0:
                continue
            y1, y2 = sy(acc), sy(acc + v)
            last = k == len(parts) - 1 or all(p[2][i] <= 0 for p in parts[k + 1:])
            hgt = y1 - y2 - (0 if k == 0 else 2)
            if last:
                g.append(f'<path d="{rbar_v(x, y1 - (0 if k == 0 else 2), bw, hgt)}" style="fill: var({var})"/>')
            else:
                g.append(f'<rect x="{x:.1f}" y="{y2:.1f}" width="{bw:.1f}" height="{max(0, hgt):.1f}" style="fill: var({var})"/>')
            acc += v
        g.append("</g>")
        g.append(f'<text class="val" x="{x + bw / 2:.1f}" y="{sy(totals[i]) - 7:.1f}" text-anchor="middle">{esc((total_fmt or fmt)(totals[i]))}</text>')
        g.append(f'<text class="tick" x="{x + bw / 2:.1f}" y="{height - 12}" text-anchor="middle">{esc(c)}</text>')
    svg = f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">{"".join(g)}</svg>'
    lg = legend([(nm, var) for nm, var, _ in parts])
    tbl = table([""] + [nm for nm, _, _ in parts] + ["Total"], [[c] + [fmt(vs[i]) for _, _, vs in parts] + [fmt(totals[i])] for i, c in enumerate(cats)])
    return figure(svg, title, sub, lg, tbl, note)


def heatmap(row_labels, col_labels, matrix, title, sub="", fmt=lambda v: f"{v:,.0f}", width=760, steps=None, note="",
            row_title="", col_title="", highlight=None):
    """Sequential single-hue heatmap; steps: thresholds ascending -> --seq-1..--seq-5 (light->dark)."""
    left, top = 92, 46
    cw = (width - left - 10) / len(col_labels)
    ch = 28
    H = top + ch * len(row_labels) + 12
    flat = [v for r in matrix for v in r]
    steps = steps or [sorted(flat)[int(len(flat) * q)] for q in (0.2, 0.4, 0.6, 0.8)]
    def cls(v):
        for k, t in enumerate(steps):
            if v <= t:
                return k + 1
        return 5
    g = [f'<text class="tick" x="{left + (width - left) / 2:.1f}" y="14" text-anchor="middle">{esc(col_title)}</text>']
    for j, c in enumerate(col_labels):
        g.append(f'<text class="tick" x="{left + cw * j + cw / 2:.1f}" y="{top - 10}" text-anchor="middle">{esc(c)}</text>')
    for i, r in enumerate(row_labels):
        y = top + ch * i
        g.append(f'<text class="tick" x="{left - 10}" y="{y + ch * 0.65:.1f}" text-anchor="end">{esc(r)}</text>')
        for j, c in enumerate(col_labels):
            v = matrix[i][j]
            k = cls(v)
            hl = ' stroke="var(--ink)" stroke-width="2"' if highlight and (i, j) in highlight else ""
            g.append(f'<g class="mark" tabindex="0" data-tip="{esc(f"{row_title} {r}, {col_title} {c}: {fmt(v)}")}">'
                     f'<rect x="{left + cw * j + 1:.1f}" y="{y + 1:.1f}" width="{cw - 2:.1f}" height="{ch - 2}" rx="3" style="fill: var(--seq-{k})"{hl}/>'
                     f'<text class="cell {"cell-dark" if k >= 4 else ""}" x="{left + cw * j + cw / 2:.1f}" y="{y + ch * 0.66:.1f}" text-anchor="middle">{esc(fmt(v))}</text></g>')
    g.append(f'<text class="tick" x="12" y="{top + ch * len(row_labels) / 2:.1f}" transform="rotate(-90 12 {top + ch * len(row_labels) / 2:.1f})" text-anchor="middle">{esc(row_title)}</text>')
    svg = f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="{esc(title)}">{"".join(g)}</svg>'
    tbl = table([row_title + " \\ " + col_title] + list(col_labels), [[r] + [fmt(v) for v in matrix[i]] for i, r in enumerate(row_labels)])
    return figure(svg, title, sub, "", tbl, note)


def tornado(rows, base, title, sub="", fmt=lambda v: f"{v:,.0f}", width=760, note=""):
    """rows: [(label, low_value, high_value)] relative to base value; diverging --neg / --pos."""
    label_w, bh, gap = 200, 18, 12
    top, bottom = 10, 34
    H = top + len(rows) * (bh + gap) + bottom
    pw = width - label_w - 20
    span = max(max(abs(l - base), abs(h - base)) for _, l, h in rows) * 1.15
    sx = lambda v: label_w + pw / 2 + (v - base) / span * (pw / 2)
    g = []
    for t in nice_ticks(base - span, base + span, 6):
        if base - span <= t <= base + span:
            g.append(f'<line class="grid" x1="{sx(t):.1f}" x2="{sx(t):.1f}" y1="{top - 4}" y2="{H - bottom + 2}"/>'
                     f'<text class="tick" x="{sx(t):.1f}" y="{H - bottom + 18}" text-anchor="middle">{esc(compact(t))}</text>')
    for i, (lab, lo, hi) in enumerate(rows):
        y = top + i * (bh + gap)
        g.append(f'<text class="cat" x="{label_w - 10}" y="{y + bh * 0.72:.1f}" text-anchor="end">{esc(lab)}</text>')
        tip = f"{lab}: low case {fmt(lo)} · high case {fmt(hi)} (base {fmt(base)})"
        g.append(f'<g class="mark" tabindex="0" data-tip="{esc(tip)}"><rect class="hit" x="{label_w}" y="{y - gap / 2}" width="{pw}" height="{bh + gap}"/>')
        for v, var in ((lo, "--neg"), (hi, "--pos")):
            x0, x1 = sorted((sx(base), sx(v)))
            if x1 - x0 > 0.5:
                if v < base:
                    d = f"M{x1:.1f},{y} H{x0 + 4:.1f} Q{x0:.1f},{y} {x0:.1f},{y + 4} V{y + bh - 4} Q{x0:.1f},{y + bh} {x0 + 4:.1f},{y + bh} H{x1:.1f} Z"
                else:
                    d = rbar_h(x0, y, x1 - x0, bh)
                g.append(f'<path d="{d}" style="fill: var({var})"/>')
        g.append("</g>")
    g.append(f'<line class="axis" x1="{sx(base):.1f}" x2="{sx(base):.1f}" y1="{top - 4}" y2="{H - bottom + 2}"/>')
    svg = f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="{esc(title)}">{"".join(g)}</svg>'
    lg = legend([("Downside case", "--neg"), ("Upside case", "--pos")])
    tbl = table(["Driver", "Low case", "High case", "Swing"], [[l, fmt(lo), fmt(hi), fmt(abs(hi - lo))] for l, lo, hi in rows])
    return figure(svg, title, sub, lg, tbl, note)


def gantt(tasks, title, sub="", width=900, months=24, note=""):
    label_w, bh, gap = 290, 14, 8
    top, bottom = 26, 16
    H = top + len(tasks) * (bh + gap) + bottom
    pw = width - label_w - 14
    sx = lambda m: label_w + m / months * pw
    g = []
    for m in range(0, months + 1, 3):
        g.append(f'<line class="grid" x1="{sx(m):.1f}" x2="{sx(m):.1f}" y1="{top - 6}" y2="{H - bottom}"/>'
                 f'<text class="tick" x="{sx(m):.1f}" y="{top - 10}" text-anchor="middle">M{m}</text>')
    for i, t in enumerate(tasks):
        y = top + i * (bh + gap)
        var = "--s2" if t.get("critical") else "--s1"
        g.append(f'<text class="cat" x="{label_w - 10}" y="{y + bh * 0.8:.1f}" text-anchor="end">{esc(t["task"][:46])}</text>')
        x0, x1 = sx(t["start_month"]), sx(min(months, t["start_month"] + t["duration_months"]))
        tip = f'{t["task"]}: month {t["start_month"]:g} → {t["start_month"] + t["duration_months"]:g}' + (" · critical path" if t.get("critical") else "") + (f' · {t.get("owner")}' if t.get("owner") else "")
        g.append(f'<g class="mark" tabindex="0" data-tip="{esc(tip)}"><rect x="{x0:.1f}" y="{y}" width="{max(3, x1 - x0):.1f}" height="{bh}" rx="4" style="fill: var({var})"/></g>')
    svg = f'<svg viewBox="0 0 {width} {H}" role="img" aria-label="{esc(title)}">{"".join(g)}</svg>'
    lg = legend([("Critical path", "--s2"), ("Other workstreams", "--s1")])
    tbl = table(["Task", "Start (month)", "Duration (months)", "Critical"], [[t["task"], t["start_month"], t["duration_months"], "yes" if t.get("critical") else ""] for t in tasks])
    return figure(svg, title, sub, lg, tbl, note)


def risk_matrix(risks, title, sub="", width=760, note=""):
    """risks: [(id, name, likelihood 1-5, impact 1-5)]."""
    left, top, cell = 70, 20, 92
    H = top + cell * 5 + 50
    g = []
    for li in range(1, 6):
        for im in range(1, 6):
            sev = li * im
            k = 1 if sev <= 4 else 2 if sev <= 8 else 3 if sev <= 12 else 4 if sev <= 16 else 5
            x = left + (im - 1) * cell
            y = top + (5 - li) * cell
            g.append(f'<rect x="{x + 1}" y="{y + 1}" width="{cell - 2}" height="{cell - 2}" rx="4" style="fill: var(--heat-{k})"/>')
    buckets = {}
    for rid, name, li, im in risks:
        buckets.setdefault((li, im), []).append((rid, name))
    for (li, im), items in buckets.items():
        x = left + (im - 1) * cell
        y = top + (5 - li) * cell
        for n, (rid, name) in enumerate(items[:6]):
            cx = x + 20 + (n % 3) * 26
            cy = y + 24 + (n // 3) * 30
            g.append(f'<g class="mark" tabindex="0" data-tip="{esc(f"{rid} {name} · likelihood {li}/5 · impact {im}/5")}">'
                     f'<circle cx="{cx}" cy="{cy}" r="11" class="risk-dot"/><text class="risk-id" x="{cx}" y="{cy + 4}" text-anchor="middle">{esc(rid)}</text></g>')
    for i in range(1, 6):
        g.append(f'<text class="tick" x="{left + (i - 0.5) * cell:.1f}" y="{top + 5 * cell + 18}" text-anchor="middle">{i}</text>')
        g.append(f'<text class="tick" x="{left - 12}" y="{top + (5 - i + 0.55) * cell:.1f}" text-anchor="end">{i}</text>')
    g.append(f'<text class="tick" x="{left + 2.5 * cell:.1f}" y="{top + 5 * cell + 40}" text-anchor="middle">Impact →</text>')
    g.append(f'<text class="tick" x="16" y="{top + 2.5 * cell:.1f}" transform="rotate(-90 16 {top + 2.5 * cell:.1f})" text-anchor="middle">Likelihood →</text>')
    svg = f'<svg viewBox="0 0 {left + 5 * cell + 10} {H}" role="img" aria-label="{esc(title)}" style="max-width:{left + 5 * cell + 10}px">{"".join(g)}</svg>'
    tbl = table(["ID", "Risk", "Likelihood", "Impact", "Score"], [[r[0], r[1], r[2], r[3], r[2] * r[3]] for r in risks])
    return figure(svg, title, sub, "", tbl, note)
