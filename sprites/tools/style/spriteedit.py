"""Tiny sprite-edit toolkit used by the per-character scripts (tools/style/<name>.py).

A template (out/style/<name>_clean.png) is loaded as a grid of RGBA pixels. Edits are applied as:
  recolour(img, mapping, box)   -> swap exact template colours inside a box (keeps every pixel's position)
  patch(img, x, y, rows, keys)  -> ASCII patch: '?' keeps the template pixel, '.' clears it, any other
                                   character is a palette key
The palette keys are per character; '#' is always the template's own outline colour.
"""
import numpy as np
from PIL import Image

OUTLINE = (26, 21, 33)


def load(path):
    return np.asarray(Image.open(path).convert('RGBA')).copy()


def save(img, path):
    Image.fromarray(img, 'RGBA').save(path)


def hexrgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def recolour(img, mapping, box=None):
    """mapping {(r,g,b): (r,g,b) or None}; box (x0,y0,x1,y1) exclusive end"""
    h, w = img.shape[:2]
    x0, y0, x1, y1 = box or (0, 0, w, h)
    sub = img[y0:y1, x0:x1]
    src = sub.copy()
    for a, b in mapping.items():
        m = (src[..., 3] > 0) & np.all(src[..., :3] == np.array(a, np.uint8), -1)
        if b is None:
            sub[m] = 0
        else:
            sub[m, :3] = b; sub[m, 3] = 255
    return img


def patch(img, x, y, rows, keys):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch == '?':
                continue
            yy, xx = y + j, x + i
            if not (0 <= yy < img.shape[0] and 0 <= xx < img.shape[1]):
                continue
            if ch == '.':
                img[yy, xx] = 0
            else:
                img[yy, xx, :3] = keys[ch]; img[yy, xx, 3] = 255
    return img


def patch_under(img, x, y, rows, keys):
    """like patch, but only paints where the sprite is still transparent (for things behind the body)"""
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            yy, xx = y + j, x + i
            if ch in '?.' or not (0 <= yy < img.shape[0] and 0 <= xx < img.shape[1]) or img[yy, xx, 3]:
                continue
            img[yy, xx, :3] = keys[ch]; img[yy, xx, 3] = 255
    return img


def pad(img, left=0, top=0, right=0, bottom=0):
    h, w = img.shape[:2]
    out = np.zeros((h + top + bottom, w + left + right, 4), np.uint8)
    out[top:top + h, left:left + w] = img
    return out


def crop_to_content(img, margin=0):
    ys, xs = np.nonzero(img[..., 3])
    return img[max(0, ys.min() - margin):ys.max() + 1 + margin, max(0, xs.min() - margin):xs.max() + 1 + margin]


def dump(img, keys=None):
    """ASCII dump with a key per colour (for planning edits)"""
    from collections import Counter
    cols = Counter(tuple(int(v) for v in img[y, x, :3]) for y in range(img.shape[0])
                   for x in range(img.shape[1]) if img[y, x, 3]).most_common()
    inv = {v: k for k, v in (keys or {}).items()}
    sym = iter('abcdefghijklmnopqrstuvwxyz0123456789@$%&*+=')
    m = {}
    for c, _ in cols:
        m[c] = inv.get(c) or next(sym)
    lines = ['   ' + ''.join(str(i % 10) for i in range(img.shape[1]))]
    for y in range(img.shape[0]):
        lines.append(f'{y:2d} ' + ''.join(m[tuple(int(v) for v in img[y, x, :3])] if img[y, x, 3] else '.'
                                          for x in range(img.shape[1])))
    return '\n'.join(lines), m


def zoom(imgs, path, z=8, gap=2, bg=(213, 225, 237, 255)):
    """side by side, bottom aligned, gap in sprite pixels"""
    H = max(a.shape[0] for a in imgs)
    W = sum(a.shape[1] + gap for a in imgs) - gap
    c = Image.new('RGBA', (W * z, H * z), bg)
    x = 0
    for a in imgs:
        im = Image.fromarray(a, 'RGBA')
        c.alpha_composite(im.resize((im.width * z, im.height * z), Image.NEAREST), (x * z, (H - a.shape[0]) * z))
        x += a.shape[1] + gap
    c.save(path)
