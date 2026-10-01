"""Recover native pixels from an upscaled pixel-art image (any non-integer scale, lossy OK).
1) find colour-edge positions along x and y, 2) fit pixel size + phase that best explains the edges,
3) sample the median colour at each cell centre, 4) flood-remove the white/near-white background from the border.
usage: python3 recover_grid.py in.png out.png"""
import sys
import numpy as np
from PIL import Image

def edges(a, axis):
    d = np.abs(np.diff(a.astype(int), axis=axis)).sum(axis=2) > 60
    return d.sum(axis=0 if axis == 1 else 1)          # edge counts per x (axis=1) or per y (axis=0)

def fit(counts, lo=3.0, hi=60.0):
    pos = np.nonzero(counts > counts.max() * 0.08)[0].astype(float)
    w = counts[counts > counts.max() * 0.08].astype(float)
    best = None
    for s in np.arange(lo, hi, 0.01):
        ph = (pos + 0.5) % s                           # edge sits between pixel i and i+1
        ang = 2 * np.pi * ph / s
        c, sn = (w * np.cos(ang)).sum(), (w * np.sin(ang)).sum()
        r = np.hypot(c, sn) / w.sum()                  # alignment of edges to a period-s grid
        score = r - 0.002 * s / hi                      # tiny bias toward... nothing big; keeps smallest consistent period
        if best is None or score > best[0] + 1e-4: best = (score, s, (np.arctan2(sn, c) % (2*np.pi)) * s / (2*np.pi))
    return best

def recover(path, out, bg_tol=40):
    im = Image.open(path).convert('RGB'); a = np.asarray(im)
    sx = fit(edges(a, 1)); sy = fit(edges(a, 0))
    # prefer one common pixel size (square pixels)
    s = (sx[1] + sy[1]) / 2 if abs(sx[1] - sy[1]) < 0.6 else min(sx[1], sy[1])
    ox, oy = sx[2] % s, sy[2] % s                      # grid lines (pixel boundaries)
    H, W = a.shape[:2]
    cols = int((W - ox) / s); rows = int((H - oy) / s)
    nat = np.zeros((rows, cols, 3), np.uint8)
    for r in range(rows):
        for c in range(cols):
            x0, y0 = ox + c * s, oy + r * s
            xa, xb = int(x0 + s * 0.3), int(x0 + s * 0.7) + 1
            ya, yb = int(y0 + s * 0.3), int(y0 + s * 0.7) + 1
            blk = a[ya:yb, xa:xb].reshape(-1, 3)
            nat[r, c] = np.median(blk, axis=0)
    # background removal: flood from the border over near-white cells
    near = (np.abs(nat.astype(int) - 255).sum(axis=2) < bg_tol)
    bg = np.zeros_like(near); stack = [(r, c) for r in range(rows) for c in (0, cols - 1)] + [(r, c) for c in range(cols) for r in (0, rows - 1)]
    while stack:
        r, c = stack.pop()
        if not (0 <= r < rows and 0 <= c < cols) or bg[r, c] or not near[r, c]: continue
        bg[r, c] = True; stack += [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    rgba = np.dstack([nat, np.where(bg, 0, 255).astype(np.uint8)])
    img = Image.fromarray(rgba, 'RGBA'); img = img.crop(img.getbbox()); img.save(out)
    print(f'{path}: pixel={s:.2f}px  native={img.size}')
    return img

if __name__ == '__main__':
    recover(sys.argv[1], sys.argv[2])
