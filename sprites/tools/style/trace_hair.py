"""Trace a hair silhouette from official art onto a sprite's head (the style sheet's "hair redrawn after the
official head" technique), reusable for any character.

1. mask   : isolate the hair in the reference by colour (a predicate on RGB), inside a head box, keep the
            connected parts that touch the main hair blob, close the thin line-art gaps.
2. align  : map reference pixels to sprite (template) pixels from facial landmarks: the two eye centres
            fix x scale/offset (inter-eye distance) and the scale above the eye line; the eye-to-chin distance
            fixes a separate (chibi-short) scale below the eye line, so the face block lines up.
3. vote   : every sprite pixel takes the fraction of hair pixels in its reference footprint; >= THRESH -> hair.

usage (debug): python3 tools/style/trace_hair.py   -> out/style/hitsugaya_hair_trace.png (ref mask | sprite mask)
"""
import numpy as np
from PIL import Image


def ref_mask(path, pred, box, mirror=False, close=2):
    im = np.asarray(Image.open(path).convert('RGB')).astype(int)
    if mirror:
        im = im[:, ::-1]
    m = pred(im)
    x0, y0, x1, y1 = box
    keep = np.zeros_like(m); keep[y0:y1, x0:x1] = True
    m &= keep
    for _ in range(close):                                  # bridge the dark line art inside the hair
        g = m.copy()
        g[1:] |= m[:-1]; g[:-1] |= m[1:]; g[:, 1:] |= m[:, :-1]; g[:, :-1] |= m[:, 1:]
        m = g
    for _ in range(close):
        g = m.copy()
        g[1:] &= m[:-1]; g[:-1] &= m[1:]; g[:, 1:] &= m[:, :-1]; g[:, :-1] &= m[:, 1:]
        m = g
    return largest(m)


def largest(m):
    """keep the biggest 4-connected component (drops eye whites, highlights, background specks)"""
    lab = np.zeros(m.shape, np.int32); best, best_n, n = 0, 0, 0
    ys, xs = np.nonzero(m)
    for y0, x0 in zip(ys, xs):
        if lab[y0, x0]:
            continue
        n += 1; st = [(y0, x0)]; lab[y0, x0] = n; cnt = 0
        while st:
            y, x = st.pop(); cnt += 1
            for yy, xx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if 0 <= yy < m.shape[0] and 0 <= xx < m.shape[1] and m[yy, xx] and not lab[yy, xx]:
                    lab[yy, xx] = n; st.append((yy, xx))
        if cnt > best_n:
            best, best_n = n, cnt
    return lab == best


def white_hair(im, lo=168, sat=42):
    mx, mn = im.max(-1), im.min(-1)
    return (mn >= lo) & (mx - mn <= sat)


class Mapping:
    """reference pixel -> sprite (template) pixel. anchor_ref (eye midpoint in the ref) lands on anchor_spr;
    sx = horizontal scale, s_up = vertical scale above the eye line (sets the hair height), s_dn = below it
    (eye-to-chin, chibi-short)."""
    def __init__(self, anchor_ref, anchor_spr, sx, s_up, s_dn):
        self.ar, self.asp, self.sx, self.s_up, self.s_dn = anchor_ref, anchor_spr, sx, s_up, s_dn

    @classmethod
    def from_landmarks(cls, ref_eyes, ref_chin, spr_eyes, spr_chin):
        (rlx, rly), (rrx, rry) = ref_eyes; (slx, sly), (srx, sry) = spr_eyes
        sx = (srx - slx) / (rrx - rlx); rey, sey = (rly + rry) / 2, (sly + sry) / 2
        return cls(((rlx + rrx) / 2, rey), ((slx + srx) / 2, sey), sx, sx, (spr_chin[1] - sey) / (ref_chin[1] - rey))

    def back(self, x, y):                                    # sprite coords -> ref coords
        rx = self.ar[0] + (x - self.asp[0]) / self.sx
        ry = self.ar[1] + (y - self.asp[1]) / (self.s_up if y < self.asp[1] else self.s_dn)
        return rx, ry

    def fwd(self, rx, ry):                                   # ref coords -> sprite coords
        x = self.asp[0] + (rx - self.ar[0]) * self.sx
        y = self.asp[1] + (ry - self.ar[1]) * (self.s_up if ry < self.ar[1] else self.s_dn)
        return x, y

    def footprints(self, spr_box, shape):
        H, W = shape
        for j, y in enumerate(range(spr_box[1], spr_box[3])):
            for i, x in enumerate(range(spr_box[0], spr_box[2])):
                ax, ay = self.back(x, y); bx, by = self.back(x + 1, y + 1)
                xa, xb = int(max(0, min(ax, bx))), int(min(W, max(ax, bx)))
                ya, yb = int(max(0, min(ay, by))), int(min(H, max(ay, by)))
                yield j, i, (slice(ya, yb), slice(xa, xb)) if xb > xa and yb > ya else None


def to_sprite(mask, mapping, spr_box, thresh=0.45, tip=None):
    """vote: sprite pixel is hair when >= thresh of its reference footprint is hair. With tip=t (hysteresis),
    pixels with >= t that are connected to the mass are added too, so thin spikes keep their 1-px tips."""
    frac = np.zeros((spr_box[3] - spr_box[1], spr_box[2] - spr_box[0]))
    for j, i, fp in mapping.footprints(spr_box, mask.shape):
        if fp:
            frac[j, i] = mask[fp].mean()
    out = frac >= thresh
    if tip is not None:
        weak = frac >= tip
        while True:
            g = out.copy()
            g[1:] |= out[:-1]; g[:-1] |= out[1:]; g[:, 1:] |= out[:, :-1]; g[:, :-1] |= out[:, 1:]
            g &= weak
            if (g == out).all():
                break
            out = g
    return out, frac


def target(path, mapping, spr_box, mirror=False, ncolors=8):
    """the WHOLE reference head downsampled to sprite pixels (median colour per footprint), quantised:
    the pixelated ground truth to rebuild the hair against"""
    im = np.asarray(Image.open(path).convert('RGB'))
    if mirror:
        im = im[:, ::-1]
    out = np.zeros((spr_box[3] - spr_box[1], spr_box[2] - spr_box[0], 3), np.uint8)
    for j, i, fp in mapping.footprints(spr_box, im.shape[:2]):
        if fp:
            out[j, i] = np.median(im[fp].reshape(-1, 3), 0)
    q = Image.fromarray(out).quantize(ncolors, method=Image.Quantize.MEDIANCUT).convert('RGB')
    return np.asarray(q)


def polar_profile(mask, centre, step=1.0):
    """outer radius of the mask along rays from centre, for angles 0..360 (deg, image coords: 90 = down)"""
    H, W = mask.shape; cx, cy = centre
    angs = np.arange(0, 360, step); rad = np.zeros(len(angs))
    for k, a in enumerate(angs):
        dx, dy = np.cos(np.radians(a)), np.sin(np.radians(a))
        r = 0
        for t in range(1, int(np.hypot(H, W))):
            x, y = int(cx + dx * t), int(cy + dy * t)
            if not (0 <= x < W and 0 <= y < H):
                break
            if mask[y, x]:
                r = t
        rad[k] = r
    return angs, rad


def find_tips(mask, centre, min_prom=18, window=12, arc=(180, 360)):
    """spike tips (local maxima of the outline radius, with prominence) and the valleys between them,
    restricted to an angle arc (default: the upper half). Returns tips [(x, y, prom)], valleys [(x, y, depth)]"""
    angs, rad = polar_profile(mask, centre)
    n = len(angs); cx, cy = centre
    tips, valleys = [], []
    for k in range(n):
        a = angs[k]
        if not (arc[0] <= a <= arc[1]) or rad[k] == 0:
            continue
        seg = [rad[(k + d) % n] for d in range(-window, window + 1)]
        if rad[k] == max(seg) and (not tips or a - tips[-1][3] > window):
            left = min(rad[(k - d) % n] for d in range(1, 3 * window)); right = min(rad[(k + d) % n] for d in range(1, 3 * window))
            prom = rad[k] - max(left, right)
            if prom >= min_prom:
                tips.append((cx + np.cos(np.radians(a)) * rad[k], cy + np.sin(np.radians(a)) * rad[k], prom, a))
    for t0, t1 in zip(tips, tips[1:]):
        ks = [k for k in range(n) if t0[3] < angs[k] < t1[3]]
        if ks:
            k = min(ks, key=lambda k: rad[k]); a = angs[k]
            depth = min(np.hypot(t0[0] - cx, t0[1] - cy), np.hypot(t1[0] - cx, t1[1] - cy)) - rad[k]
            valleys.append((cx + np.cos(np.radians(a)) * rad[k], cy + np.sin(np.radians(a)) * rad[k], depth))
    return [t[:3] for t in tips], valleys


def sharpen(spr, spr_box, mapping, tips, valleys, centre, tip_w=3, min_len=2.0, ext=1.5):
    """re-cut the ref's spike tips and the notches between them into the downsampled mask (the vote rounds
    them off): each tip becomes a tapered spike ending in 1 px, each valley a V notch"""
    def tri_fill(m, a, b, c, value):
        (x0, y0), (x1, y1), (x2, y2) = a, b, c
        d = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
        if abs(d) < 1e-9:
            return
        for y in range(int(np.floor(min(y0, y1, y2))), int(np.ceil(max(y0, y1, y2))) + 1):
            for x in range(int(np.floor(min(x0, x1, x2))), int(np.ceil(max(x0, x1, x2))) + 1):
                px, py = x + 0.5, y + 0.5
                l1 = ((y1 - y2) * (px - x2) + (x2 - x1) * (py - y2)) / d
                l2 = ((y2 - y0) * (px - x2) + (x0 - x2) * (py - y2)) / d
                if min(l1, l2, 1 - l1 - l2) >= -0.05:
                    j, i = y - spr_box[1], x - spr_box[0]
                    if 0 <= j < m.shape[0] and 0 <= i < m.shape[1]:
                        m[j, i] = value
    cx, cy = mapping.fwd(*centre)
    out = spr.copy()
    for vx, vy, depth in valleys:                         # notches first
        x, y = mapping.fwd(vx, vy); d = np.array([x - cx, y - cy]); d /= np.linalg.norm(d)
        n = np.array([-d[1], d[0]]); L = max(1.5, depth * mapping.sx)
        o = np.array([x, y]) + d * L
        tri_fill(out, (x, y), tuple(o + n * L * 0.8), tuple(o - n * L * 0.8), False)
    for tx, ty, prom in tips:                             # then spikes
        x, y = mapping.fwd(tx, ty); d = np.array([x - cx, y - cy]); d /= np.linalg.norm(d)
        n = np.array([-d[1], d[0]]); L = max(min_len, prom * mapping.sx)
        apex = np.array([x, y]) + d * ext                     # poke past the rounded-off outline
        b = apex - d * (L + 1.5)
        tri_fill(out, tuple(apex), tuple(b + n * tip_w / 2), tuple(b - n * tip_w / 2), True)
    return out


if __name__ == '__main__':
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    import hitsugaya as h
    m = ref_mask(h.REF, white_hair, h.REF_HEAD_BOX, mirror=h.REF_MIRROR)
    spr, frac = to_sprite(m, h.MAPPING, h.SPR_BOX, h.TRACE_THRESH)
    a = Image.fromarray((m * 255).astype(np.uint8)).convert('RGB')
    b = Image.fromarray((spr * 255).astype(np.uint8)).convert('RGB')
    b = b.resize((b.width * 12, b.height * 12), Image.NEAREST)
    a = a.resize((round(a.width * b.height / a.height), b.height))
    c = Image.new('RGB', (a.width + b.width + 20, b.height), (90, 90, 90)); c.paste(a, (0, 0)); c.paste(b, (a.width + 20, 0))
    c.save('out/style/hitsugaya_hair_trace.png')
