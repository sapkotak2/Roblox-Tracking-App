"""Step 1 of the style method: recover the game's real sprites as crisp, few-colour pixel art.

Finding: the style sheet webp was downscaled by 0.8475 from the original. Its "4x" row therefore has a sprite
pixel every 3.39 sheet px (measured from the edge periodicity of the whole row, x and y agree to 0.001), and
the "2x" roster row has one every 1.695 px. The refs/game/*_native.png files were cut out of the sheet as if
the scale were an exact integer, so they are a 0.85x RESAMPLE of the real art (51 rows instead of ~60): that,
plus the webp, is why they are blurry and have hundreds of colours.

Method:
 1. Lock the true pixel grid of the 4x row (period PERIOD, edge phase measured by grid_phase()).
 2. Sample every grid cell at its centre (median of the sheet pixels whose centres lie within 0.75 px of the
    cell centre); this avoids the blurred cell borders.
 3. Alpha: opaque where the cell centre differs from the panel background (213,225,237); the ground line row
    (y 1244) is excluded; only components connected to the main body are kept.
 4. Palette: greedy clustering by frequency (redmean distance, tolerance TOL) + 3 median refinements, so each
    material ends up as base / shade (/ highlight) like the original art.
 5. Edge fix: border pixels that are lighter blends of outline and background are snapped to the darkest
    palette colour (the outline) or dropped; single-pixel specks with no same-coloured neighbour and close to
    the neighbour majority are merged into it.

usage: python3 tools/style/clean_templates.py [names...]
  -> out/style/{name}_clean.png (true grid) and out/style/{name}_clean_check.png (native vs clean at 10x)
"""
import sys, os
from collections import Counter
import numpy as np
from PIL import Image

SHEET = 'refs/game/style_sheet.webp'
BG = np.array([213, 225, 237], float)
PERIOD = 3.39                      # sprite pixel size in the sheet's 4x row
ROW = (1010, 1246)                 # y range of the 4x row (ground line at 1244 falls between cell centres)
# x ranges of each sprite in the 4x row (Tanjiro, Zoro, Robin, Luffy, Shanks v5)
XR = {'tanjiro': (18, 200), 'zoro': (196, 380), 'robin': (396, 506), 'luffy': (508, 641), 'shanks': (641, 812)}
TOL = {'default': 11}
MINCOUNT = 6        # colours used by fewer cells are compression strays...
ACCENT = 28         # ...unless they differ from every other colour by this deltaE
NAMES = ['luffy', 'tanjiro', 'shanks', 'robin', 'zoro']


def lab(c):
    """sRGB (0-255) -> CIELAB"""
    c = np.asarray(c, float) / 255
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    xyz = c @ np.array([[0.4124, 0.2126, 0.0193], [0.3576, 0.7152, 0.1192], [0.1805, 0.0722, 0.9505]])
    xyz = xyz / [0.9505, 1.0, 1.089]
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def dist(a, b):
    """CIE76 delta-E"""
    return np.sqrt(((lab(a) - lab(b)) ** 2).sum(-1))


def grid_phase(sheet, x0, x1, y0, y1, p=PERIOD):
    """absolute sheet coordinate of one pixel-cell edge, per axis"""
    r = sheet[y0:y1, x0:x1]
    out = []
    for axis, o in ((1, x0), (0, y0)):
        sig = np.abs(np.diff(r, axis=axis)).sum((0, 2) if axis == 1 else (1, 2))
        n = np.arange(len(sig))
        z = (sig * np.exp(2j * np.pi * n / p)).sum()
        out.append((o + 0.5 + (-np.angle(z) / (2 * np.pi)) * p) % p)
    return out  # ex, ey


def sample(sheet, ex, ey, x0, x1, y0, y1, p=PERIOD):
    """grid of cell-centre colours covering [x0,x1)x[y0,y1)"""
    kx0 = int(np.ceil((x0 - ex) / p)); kx1 = int((x1 - ex) / p)
    ky0 = int(np.ceil((y0 - ey) / p)); ky1 = int((y1 - ey) / p)
    H, W = ky1 - ky0, kx1 - kx0
    out = np.zeros((H, W, 3))
    for j in range(H):
        cy = ey + (ky0 + j + 0.5) * p
        ys = [y for y in range(int(cy) - 2, int(cy) + 3) if abs(y + 0.5 - cy) <= 0.75]
        for i in range(W):
            cx = ex + (kx0 + i + 0.5) * p
            xs = [x for x in range(int(cx) - 2, int(cx) + 3) if abs(x + 0.5 - cx) <= 0.75]
            out[j, i] = np.median(sheet[np.ix_(ys, xs)].reshape(-1, 3), 0)
    return out


def components(mask):
    h, w = mask.shape
    lab = np.zeros((h, w), int); n = 0
    for y in range(h):
        for x in range(w):
            if mask[y, x] and not lab[y, x]:
                n += 1; st = [(y, x)]; lab[y, x] = n
                while st:
                    cy, cx = st.pop()
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            yy, xx = cy + dy, cx + dx
                            if 0 <= yy < h and 0 <= xx < w and mask[yy, xx] and not lab[yy, xx]:
                                lab[yy, xx] = n; st.append((yy, xx))
    return lab, n


def quantise(rgb, alpha, tol):
    pts = rgb[alpha].round().astype(int)
    cnt = Counter(map(tuple, pts))
    reps = []
    for c, _ in cnt.most_common():
        if not reps or dist(np.array(reps), c).min() >= tol:
            reps.append(c)
    reps = np.array(reps, float)
    for _ in range(3):
        lab = np.argmin(dist(pts[:, None, :], reps[None]), axis=1)
        reps = np.array([np.median(pts[lab == i], 0) if (lab == i).any() else reps[i] for i in range(len(reps))])
    # fold rare colours (compression strays) into their nearest colour, unless they are a distinct accent
    # (deltaE > ACCENT from everything else, e.g. an eye or a button) which the artist placed on purpose
    keep_accent = set()
    while True:
        lab_ = np.argmin(dist(pts[:, None, :], reps[None]), axis=1)
        cnt = np.bincount(lab_, minlength=len(reps))
        rare = [i for i in np.argsort(cnt) if cnt[i] < MINCOUNT and i not in keep_accent]
        if not rare:
            break
        i = rare[0]
        dd = dist(reps, reps[i]); dd[i] = 1e9
        if dd.min() > ACCENT and cnt[i] > 0:
            keep_accent.add(i); continue
        reps = np.delete(reps, i, 0)
        keep_accent = {k - (k > i) for k in keep_accent}
    lab_ = np.argmin(dist(pts[:, None, :], reps[None]), axis=1)
    reps = reps[[i for i in range(len(reps)) if (lab_ == i).any()]]
    idx = np.argmin(dist(rgb[..., None, :], reps[None, None]), axis=-1)
    return reps[idx].round().astype(np.uint8), reps.round().astype(np.uint8)


def nbrs(a, alpha, y, x):
    h, w = alpha.shape
    return [tuple(a[yy, xx]) for yy in range(max(0, y - 1), min(h, y + 2))
            for xx in range(max(0, x - 1), min(w, x + 2)) if (yy, xx) != (y, x) and alpha[yy, xx]]


def fix_edges(q, alpha, raw, pal):
    q = q.copy(); alpha = alpha.copy(); h, w = alpha.shape
    lum = pal.astype(float) @ [0.3, 0.59, 0.11]
    outline = tuple(int(v) for v in pal[np.argmin(lum)])
    o = np.array(outline, float); d = BG - o
    for y in range(h):
        for x in range(w):
            if not alpha[y, x]:
                continue
            edge = any(not (0 <= y + dy < h and 0 <= x + dx < w) or not alpha[y + dy, x + dx]
                       for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)))
            if not edge:
                continue
            c = raw[y, x]
            t = np.clip(((c - o) @ d) / (d @ d), 0, 1)       # blend of outline and background?
            if t > 0.2 and dist(c, o + t * d) < 8:
                if t > 0.65:
                    alpha[y, x] = False
                else:
                    q[y, x] = outline
    for y in range(h):                                     # isolated specks
        for x in range(w):
            if not alpha[y, x]:
                continue
            nb = nbrs(q, alpha, y, x); c = tuple(q[y, x])
            if len(nb) < 6 or c in nb:
                continue
            maj, n = Counter(nb).most_common(1)[0]
            if n >= 5 and dist(np.array(maj), np.array(c)) < 20:
                q[y, x] = maj
    return q, alpha


def clean(name, sheet, tol=None):
    x0, x1 = XR[name]; y0, y1 = ROW
    ex, ey = grid_phase(sheet, 20, 800, 1040, 1236)
    raw = sample(sheet, ex, ey, x0, x1, y0, y1)
    alpha = dist(raw, BG) > 6
    lab, n = components(alpha)
    if n:
        sizes = np.bincount(lab.ravel())[1:]
        alpha = np.isin(lab, [i + 1 for i in range(n) if sizes[i] >= 25])
    q, pal = quantise(raw, alpha, tol or TOL.get(name, TOL['default']))
    q, alpha = fix_edges(q, alpha, raw, pal)
    ys, xs = np.nonzero(alpha)
    out = np.zeros(alpha.shape + (4,), np.uint8)
    out[..., :3] = q; out[..., 3] = alpha * 255; out[~alpha] = 0
    return out[ys.min():ys.max() + 1, xs.min():xs.max() + 1], pal


def checksheet(ims, path, z=10, gap=20):
    W = sum(a.shape[1] * z + gap for a in ims); H = max(a.shape[0] for a in ims) * z
    c = Image.new('RGBA', (W, H), (213, 225, 237, 255)); x = 0
    for a in ims:
        im = Image.fromarray(np.asarray(a, np.uint8), 'RGBA')
        c.alpha_composite(im.resize((im.width * z, im.height * z), Image.NEAREST), (x, H - im.height * z))
        x += im.width * z + gap
    c.save(path)


if __name__ == '__main__':
    sheet = np.asarray(Image.open(SHEET).convert('RGB'), float)
    for n in sys.argv[1:] or NAMES:
        out, pal = clean(n, sheet)
        Image.fromarray(out, 'RGBA').save(f'out/style/{n}_clean.png')
        nat = np.asarray(Image.open(f'refs/game/{n}_native.png').convert('RGBA'))
        print(f'{n}: {out.shape[1]}x{out.shape[0]}, {len(np.unique(out[out[..., 3] > 0][:, :3], axis=0))} colours')
        checksheet([nat, out], f'out/style/{n}_clean_check.png')
