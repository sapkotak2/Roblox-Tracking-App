"""Merge compression-noise shades: greedy clustering by frequency (colours within `tol` collapse onto the most
common one). usage: python3 clean_palette.py in.png out.png [tol]"""
import sys
from collections import Counter
from PIL import Image
def clean(src, dst, tol=34):
    im = Image.open(src).convert('RGBA'); px = im.load(); w, h = im.size
    cnt = Counter(px[x, y][:3] for y in range(h) for x in range(w) if px[x, y][3])
    reps = []
    for c, _ in cnt.most_common():
        if not any(sum(abs(a - b) for a, b in zip(c, r)) < tol for r in reps): reps.append(c)
    near = lambda c: min(reps, key=lambda r: sum((a - b) ** 2 for a, b in zip(c, r)))
    for y in range(h):
        for x in range(w):
            if px[x, y][3]: px[x, y] = near(px[x, y][:3]) + (255,)
    im.save(dst); print(f'{src}: {len(cnt)} -> {len(reps)} colours'); return im
if __name__ == '__main__':
    clean(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 34)
