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


def to_sprite(mask, ref_eyes, ref_chin, spr_eyes, spr_chin, spr_box, thresh=0.45):
    """returns {(x, y): fraction} for sprite pixels in spr_box=(x0, y0, x1, y1) (template coords)"""
    (rlx, rly), (rrx, rry) = ref_eyes
    (slx, sly), (srx, sry) = spr_eyes
    sx = (srx - slx) / (rrx - rlx)
    rey, sey = (rly + rry) / 2, (sly + sry) / 2
    s_dn = (spr_chin[1] - sey) / (ref_chin[1] - rey)
    rcx, scx = (rlx + rrx) / 2, (slx + srx) / 2

    def back(x, y):                                          # sprite pixel edge -> ref coords
        rx = rcx + (x - scx) / sx
        ry = rey + (y - sey) / (sx if y < sey else s_dn)
        return rx, ry
    out = np.zeros((spr_box[3] - spr_box[1], spr_box[2] - spr_box[0]), bool)
    frac = np.zeros(out.shape)
    H, W = mask.shape
    for j, y in enumerate(range(spr_box[1], spr_box[3])):
        for i, x in enumerate(range(spr_box[0], spr_box[2])):
            ax, ay = back(x, y); bx, by = back(x + 1, y + 1)
            xa, xb = int(max(0, min(ax, bx))), int(min(W, max(ax, bx)))
            ya, yb = int(max(0, min(ay, by))), int(min(H, max(ay, by)))
            if xb > xa and yb > ya:
                frac[j, i] = mask[ya:yb, xa:xb].mean()
    out = frac >= thresh
    return out, frac


if __name__ == '__main__':
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    import hitsugaya as h
    m = ref_mask(h.REF, white_hair, h.REF_HEAD_BOX, mirror=h.REF_MIRROR)
    spr, frac = to_sprite(m, h.REF_EYES, h.REF_CHIN, h.SPR_EYES, h.SPR_CHIN, h.SPR_BOX, h.TRACE_THRESH)
    a = Image.fromarray((m * 255).astype(np.uint8)).convert('RGB')
    b = Image.fromarray((spr * 255).astype(np.uint8)).convert('RGB')
    b = b.resize((b.width * 12, b.height * 12), Image.NEAREST)
    a = a.resize((round(a.width * b.height / a.height), b.height))
    c = Image.new('RGB', (a.width + b.width + 20, b.height), (90, 90, 90)); c.paste(a, (0, 0)); c.paste(b, (a.width + 20, 0))
    c.save('out/style/hitsugaya_hair_trace.png')
