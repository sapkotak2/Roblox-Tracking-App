"""Load/render a text-grid sprite: '# palette' lines 'k rrggbb', then '# grid' rows ('.' = transparent)."""
import sys
from PIL import Image
def load(path):
    pal, rows, mode = {}, [], None
    for line in open(path):
        line = line.rstrip('\n')
        if line.startswith('# palette'): mode = 'p'; continue
        if line.startswith('# grid'): mode = 'g'; continue
        if line.startswith('#') or not line.strip(): continue
        if mode == 'p':
            k, v = line.split()[:2]; pal[k] = tuple(int(v[i:i+2], 16) for i in (0, 2, 4))
        elif mode == 'g': rows.append(line)
    w = max(len(r) for r in rows)
    bad = [i for i, r in enumerate(rows) if len(r) != w]
    if bad: print('warning: ragged rows', bad, file=sys.stderr)
    im = Image.new('RGBA', (w, len(rows)), (0, 0, 0, 0))
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch != '.': im.putpixel((x, y), pal[ch] + (255,))
    return im
