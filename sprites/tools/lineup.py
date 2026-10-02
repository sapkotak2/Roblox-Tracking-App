"""Render labelled lineups (rows of N) of out/<dir>/*.png at a given scale, with roster anchors at the start of each row."""
import os, sys, glob
from PIL import Image, ImageDraw
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def lineup(names, src, out, per=8, scale=4, anchors=('luffy',)):
    bg = (213, 225, 237)
    anc = [(a, Image.open(f'{R}/refs/game/{a}_native.png')) for a in anchors]
    rows = [names[i:i + per] for i in range(0, len(names), per)]
    tiles_rows = [anc + [(n, Image.open(f'{R}/out/{src}/{n}.png')) for n in r] for r in rows]
    RH = max(t.height for tr in tiles_rows for _, t in tr) + 12
    W = max(sum(t.width + 8 for _, t in tr) for tr in tiles_rows) + 8
    sh = Image.new('RGBA', (W, RH * len(rows)), bg + (255,))
    for r, tr in enumerate(tiles_rows):
        x = 4
        for _, t in tr: sh.alpha_composite(t, (x, (r + 1) * RH - t.height - 2)); x += t.width + 8
    sh = sh.resize((sh.width * scale, sh.height * scale), Image.NEAREST); d = ImageDraw.Draw(sh)
    for r, tr in enumerate(tiles_rows):
        x = 4
        for n, t in tr: d.text((x * scale, r * RH * scale + 2), n, fill=(0, 0, 0)); x += t.width + 8
    sh.save(out)
if __name__ == '__main__':
    names = sys.argv[3].split(',') if len(sys.argv) > 3 else sorted(os.path.basename(f)[:-4] for f in glob.glob(f'{R}/out/{sys.argv[1]}/*.png'))
    lineup(names, sys.argv[1], sys.argv[2])
