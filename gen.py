#!/usr/bin/env python3
"""Draw the nurz news-image entry: a simplified broadsheet front page.

One day, one page: Monday 23 November 2026. Four big stories in large
panels, a small ticker at the bottom. Navy + gold + white.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
NAVY = (13, 27, 62)
NAVY2 = (24, 48, 96)
GOLD = (198, 148, 42)
GOLD_LT = (232, 190, 90)
WHITE = (255, 255, 255)
INK = (18, 24, 38)
GREY = (74, 82, 100)
PAPER = (250, 248, 242)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=5)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
              outline=NAVY, width=3)
    d.line([cx - r, cy, cx + r, cy], fill=NAVY, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          200, 340, fill=NAVY, width=3)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          20, 160, fill=NAVY, width=3)
    # gold flame above the globe
    fx, fy = cx + r * 0.55, cy - r - 8
    d.polygon([(fx, fy - 22), (fx + 14, fy + 6), (fx + 4, fy + 2),
               (fx, fy + 12), (fx - 4, fy + 2), (fx - 14, fy + 6)],
              fill=GOLD)


def draw_drone_building(d, x, y, s):
    # broken apartment block
    bx, by, bw, bh = x, y + s * 0.35, s * 0.62, s * 0.65
    d.polygon([(bx, by + bh), (bx, by + 18), (bx + bw * 0.3, by),
               (bx + bw * 0.45, by + 22), (bx + bw * 0.7, by + 6),
               (bx + bw, by + 26), (bx + bw, by + bh)], fill=NAVY)
    for wy in range(3):
        for wx in range(3):
            d.rectangle([bx + 10 + wx * 22, by + 34 + wy * 26,
                         bx + 22 + wx * 22, by + 48 + wy * 26],
                        fill=GOLD_LT)
    # drone top-right
    dx, dy = x + s * 0.62, y + s * 0.08
    d.ellipse([dx - 12, dy - 8, dx + 12, dy + 8], fill=INK)
    for sx in (-1, 1):
        for sy in (-1, 1):
            rx, ry = dx + sx * 24, dy + sy * 14
            d.line([dx, dy, rx, ry], fill=INK, width=3)
            d.ellipse([rx - 10, ry - 3, rx + 10, ry + 3], fill=INK)
    d.line([dx, dy + 8, dx, dy + 26], fill=INK, width=3)
    d.polygon([(dx - 5, dy + 26), (dx + 5, dy + 26), (dx, dy + 38)],
              fill=GOLD)


def draw_ship(d, x, y, s):
    # sea waves
    for i in range(3):
        yy = y + s * 0.78 + i * 12
        d.arc([x, yy - 10, x + s, yy + 10], 0, 180, fill=NAVY2, width=4)
    # hull
    hx, hy = x + s * 0.1, y + s * 0.52
    d.polygon([(hx, hy), (hx + s * 0.8, hy), (hx + s * 0.68, hy + s * 0.2),
               (hx + s * 0.12, hy + s * 0.2)], fill=NAVY)
    d.rectangle([hx + s * 0.3, hy - s * 0.22, hx + s * 0.42, hy],
                fill=NAVY)
    d.line([hx + s * 0.36, hy - s * 0.34, hx + s * 0.36, hy - s * 0.22],
           fill=NAVY, width=4)
    d.polygon([(hx + s * 0.36, hy - s * 0.34), (hx + s * 0.52, hy - s * 0.28),
               (hx + s * 0.36, hy - s * 0.22)], fill=GOLD)
    # explosion starburst above the ship
    ex, ey = x + s * 0.62, y + s * 0.18
    for k in range(8):
        import math
        a = math.pi * k / 4
        d.line([ex, ey, ex + int(26 * math.cos(a)),
                ey + int(26 * math.sin(a))], fill=GOLD, width=5)
    d.ellipse([ex - 10, ey - 10, ex + 10, ey + 10], fill=GOLD)


def draw_ball(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE,
              outline=NAVY, width=5)
    # centre pentagon
    import math
    pts = []
    for k in range(5):
        a = -math.pi / 2 + 2 * math.pi * k / 5
        pts.append((cx + int(r * 0.42 * math.cos(a)),
                    cy + int(r * 0.42 * math.sin(a))))
    d.polygon(pts, fill=NAVY)
    for (px, py) in pts:
        d.line([px, py, cx + int((px - cx) * 2.1),
                cy + int((py - cy) * 2.1)], fill=NAVY, width=3)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer frame
    d.rectangle([0, 0, W - 1, H - 1], outline=NAVY, width=6)

    # ---- masthead ----
    d.rectangle([0, 0, W, 168], fill=NAVY)
    f_title = font(SERIF_B, 74)
    d.text((W // 2, 30), "THE WORLD IN ONE DAY", font=f_title,
           fill=WHITE, anchor="ma")
    d.line([60, 118, W - 60, 118], fill=GOLD, width=4)
    f_date = font(SANS_B, 40)
    d.text((W // 2, 130), "MONDAY  ·  23 NOVEMBER 2026", font=f_date,
           fill=GOLD_LT, anchor="ma")

    # ---- four story panels ----
    panels = [
        ("CLIMATE  ·  ANTALYA", "COP31 TALKS",
         "COLLAPSE",
         "EU rejects deal with no fossil fuel phase-out.",
         "globe"),
        ("UKRAINE  ·  KYIV", "DRONE HITS",
         "KYIV HOMES",
         "At least 14 missing as residents search rubble.",
         "drone"),
        ("LIBYA  ·  BENGHAZI", "WARSHIP HIT",
         "AT SEA BASE",
         "Suspected Ukrainian sea drone strikes Russian warship.",
         "ship"),
        ("SPORT", "LIVERPOOL",
         "BEAT UNITED",
         "Ten-man United lose on Pochettino debut. Alcaraz wins first ATP Finals.",
         "ball"),
    ]
    px0, py0, gap = 24, 188, 16
    pw, ph = (W - 2 * px0 - gap) // 2, 304
    f_kick = font(SANS_B, 24)
    f_head = font(SERIF_B, 52)
    f_cap = font(SANS, 26)
    for i, (kick, h1, h2, cap, icon) in enumerate(panels):
        x = px0 + (i % 2) * (pw + gap)
        y = py0 + (i // 2) * (ph + gap)
        d.rectangle([x, y, x + pw, y + ph], fill=WHITE, outline=NAVY,
                    width=3)
        d.rectangle([x, y, x + pw, y + 10], fill=GOLD)
        d.text((x + 22, y + 26), kick, font=f_kick, fill=GOLD)
        # icon top-right
        ix, iy = x + pw - 132, y + 22
        if icon == "globe":
            draw_globe(d, ix + 52, iy + 56, 42)
        elif icon == "drone":
            draw_drone_building(d, ix, iy - 6, 110)
        elif icon == "ship":
            draw_ship(d, ix - 6, iy - 4, 116)
        else:
            draw_ball(d, ix + 52, iy + 52, 44)
        # headline
        d.text((x + 22, y + 108), h1, font=f_head, fill=INK)
        d.text((x + 22, y + 168), h2, font=f_head, fill=INK)
        # caption, wrapped
        lines = wrap(d, cap, f_cap, pw - 44)
        cy = y + 236
        for ln in lines[:2]:
            d.text((x + 22, cy), ln, font=f_cap, fill=GREY)
            cy += 32

    # ---- ticker ----
    ty = 828
    d.rectangle([0, ty, W, H], fill=NAVY)
    d.line([0, ty, W, ty], fill=GOLD, width=4)
    f_tick_t = font(SANS_B, 26)
    d.text((24, ty + 12), "ALSO TODAY", font=f_tick_t, fill=GOLD_LT)
    f_tick = font(SANS, 27)
    items = [
        "US–IRAN: Houthis claim Saudi refinery & radar strike",
        "INDONESIA FACTORY FIRE: 7 dead, 50 missing",
        "GOLD $3,603/OZ  ·  MEXICO CAPTURES 'EL CHAPO ISIDRO'",
        "FIFA: ENGLAND TO HOST WOMEN'S WORLD CUP 2035",
    ]
    cy = ty + 48
    for it in items:
        d.polygon([(24, cy + 8), (24, cy + 22), (38, cy + 15)], fill=GOLD)
        d.text((48, cy), it, font=f_tick, fill=WHITE)
        cy += 34

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
