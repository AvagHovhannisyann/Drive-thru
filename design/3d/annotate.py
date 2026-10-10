"""
Draws numbered leader labels on a rendered cutaway using the projected anchors written by render_views.py.
  python3 design/3d/annotate.py design/renders/cutaway_day.png
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = Path(__file__).resolve().parents[2] / "assets/fonts/ttf"


def annotate(png, out=None):
    png = Path(png)
    pts = json.loads(png.with_name(png.stem + "_labels.json").read_text())
    im = Image.open(png).convert("RGB")
    W, H = im.size
    d = ImageDraw.Draw(im, "RGBA")
    s = W / 1920
    f_tag = ImageFont.truetype(str(FONT_DIR / "Manrope-800.ttf"), int(22 * s))
    f_lab = ImageFont.truetype(str(FONT_DIR / "Manrope-700.ttf"), int(21 * s))
    teal, apricot = (15, 59, 64), (238, 138, 59)
    # place labels in a column on the side nearest to each anchor, avoiding overlaps
    left = sorted([p for p in pts if p["x"] < 0.5], key=lambda p: p["y"])
    right = sorted([p for p in pts if p["x"] >= 0.5], key=lambda p: p["y"])
    for side, group in (("L", left), ("R", right)):
        n = len(group)
        for i, p in enumerate(group):
            ax, ay = p["x"] * W, p["y"] * H
            ly = H * (0.12 + 0.76 * (i + 0.5) / max(n, 1))
            text = p["name"]
            tw = d.textlength(text, font=f_lab)
            pad = 12 * s
            bw = tw + 2 * pad + 44 * s
            bx = 30 * s if side == "L" else W - 30 * s - bw
            bh = 40 * s
            # leader
            ex = bx + bw if side == "L" else bx
            d.line([(ex, ly), (ax, ay)], fill=(255, 255, 255, 230), width=max(2, int(3 * s)))
            d.line([(ex, ly), (ax, ay)], fill=teal + (255,), width=max(1, int(1.6 * s)))
            d.ellipse([ax - 7 * s, ay - 7 * s, ax + 7 * s, ay + 7 * s], fill=apricot + (255,), outline=(255, 255, 255), width=max(1, int(2 * s)))
            d.rounded_rectangle([bx, ly - bh / 2, bx + bw, ly + bh / 2], radius=8 * s, fill=(255, 255, 255, 238), outline=teal + (255,), width=max(1, int(1.5 * s)))
            d.rounded_rectangle([bx + 6 * s, ly - bh / 2 + 6 * s, bx + 6 * s + 34 * s, ly + bh / 2 - 6 * s], radius=6 * s, fill=teal + (255,))
            d.text((bx + 23 * s, ly), p["id"], font=f_tag, fill=(255, 255, 255), anchor="mm")
            d.text((bx + 50 * s, ly), text, font=f_lab, fill=teal, anchor="lm")
    out = out or png.with_name(png.stem + "_annotated.png")
    im.save(out)
    return out


if __name__ == "__main__":
    print(annotate(sys.argv[1]))
