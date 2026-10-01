"""Build option pages: one row per character, up to 3 candidate images each (nearest-neighbour upscaled to fit)."""
import os, sys, json
from PIL import Image, ImageDraw
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def tile(path, H=260, W=330):
    im = Image.open(path).convert('RGB')
    s = min(H / im.height, W / im.width)
    if s >= 1: s = max(1, int(s)); im = im.resize((im.width * s, im.height * s), Image.NEAREST)
    else: im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)
    return im
def page(rows, out, title):
    RH, CW, LW = 300, 350, 130
    sheet = Image.new('RGB', (LW + 3 * CW, 40 + RH * len(rows)), (232, 236, 242)); d = ImageDraw.Draw(sheet)
    d.text((10, 12), title, fill=(0, 0, 0))
    for r, (name, opts) in enumerate(rows):
        y = 40 + r * RH
        d.line([(0, y), (sheet.width, y)], fill=(170, 170, 180)); d.text((10, y + 10), name.upper(), fill=(0, 0, 0))
        for i, (key, fn) in enumerate(opts):
            t = tile(f'{R}/refs/candidates/{key}/{fn}')
            x = LW + i * CW
            d.text((x + 4, y + 8), f'{i + 1}', fill=(200, 0, 0)); sheet.paste(t, (x + 16, y + 26))
    sheet.save(out)
if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    names = list(spec); per = 6
    for p in range(0, len(names), per):
        rows = [(n, [tuple(o) for o in spec[n]]) for n in names[p:p + per]]
        out = f'{R}/out/{sys.argv[2]}_{p // per + 1}.png'; page(rows, out, f'{sys.argv[2]} - page {p // per + 1}'); print(out)
