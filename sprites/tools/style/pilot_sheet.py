"""Pilot comparison sheet: out/style/pilot_sheet.png

Row 1 (6x, nearest): clean templates Luffy, Tanjiro, Shanks, Robin | NEW Okkotsu | rejected redraw | old game sprite.
Row 2: the style sheet's own roster row (Goku ... Shanks) at the SAME sprite-pixel scale (6 screen px per
sprite pixel). The roster row has 1.695 sheet px per sprite pixel, so it is resized by 6/1.695 (bicubic,
nothing re-drawn), followed by the 4x row (Tanjiro, Zoro, Robin, Luffy, Shanks; 3.39 px per sprite pixel)
also brought to 6x.
usage: python3 tools/style/pilot_sheet.py
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

Z = 6
BG = (213, 225, 237, 255)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
SHEET = 'refs/game/style_sheet.webp'
ITEMS = [
    ('out/style/luffy_clean.png', 'Luffy (clean)', None),
    ('out/style/tanjiro_clean.png', 'Tanjiro (clean)', None),
    ('out/style/shanks_clean.png', 'Shanks (clean)', None),
    ('out/style/robin_clean.png', 'Robin (clean)', None),
    ('out/style/okkotsu.png', 'NEW Okkotsu', (40, 120, 60)),
    ('out/redraw/okkotsu.png', 'rejected redraw', (190, 40, 40)),
    ('final/native/okkotsu.png', 'old game sprite', (120, 120, 120)),
]
ROSTER = (0, 1855, 812, 1975)      # sheet crop: roster row incl. name labels
ROW4X = (10, 1022, 812, 1262)      # sheet crop: the 4x row


def main():
    f = ImageFont.truetype(FONT, 16); fb = ImageFont.truetype(FONT, 20)
    sprites = [(Image.open(p).convert('RGBA'), lab, col) for p, lab, col in ITEMS]
    gap = 10 * Z
    H1 = max(s.height for s, _, _ in sprites) * Z
    W1 = sum(s.width * Z for s, _, _ in sprites) + gap * (len(sprites) + 1)
    sheet = Image.open(SHEET).convert('RGB')
    r1 = sheet.crop(ROSTER); r1 = r1.resize((round(r1.width * Z / 1.695), round(r1.height * Z / 1.695)), Image.BICUBIC)
    r2 = sheet.crop(ROW4X); r2 = r2.resize((round(r2.width * Z / 3.39), round(r2.height * Z / 3.39)), Image.BICUBIC)
    W = max(W1, r1.width, r2.width) + 40
    H = 50 + H1 + 50 + 60 + r1.height + 60 + r2.height + 20
    c = Image.new('RGBA', (W, H), BG); d = ImageDraw.Draw(c)
    d.text((20, 12), 'Okkotsu pilot, 6x. Top: clean templates + NEW + rejected/old. Below: the style sheet itself at the same sprite-pixel scale.', fill=(20, 20, 30), font=fb)
    x = gap; base = 50 + H1
    for s, lab, col in sprites:
        c.alpha_composite(s.resize((s.width * Z, s.height * Z), Image.NEAREST), (x, base - s.height * Z))
        d.text((x, base + 10), lab, fill=col or (30, 30, 40), font=fb if col else f)
        x += s.width * Z + gap
    d.line([(10, base + 2), (W - 10, base + 2)], fill=(150, 160, 180), width=2)
    y = base + 50
    d.text((20, y), 'style sheet roster row (game sprites), resized to 6 px per sprite pixel', fill=(20, 20, 30), font=fb)
    c.paste(r1, (20, y + 30)); y += 30 + r1.height + 20
    d.text((20, y), "style sheet 4x row, resized to 6 px per sprite pixel", fill=(20, 20, 30), font=fb)
    c.paste(r2, (20, y + 30))
    c.convert('RGB').save('out/style/pilot_sheet.png')
    print('out/style/pilot_sheet.png', c.size)


if __name__ == '__main__':
    main()
