"""Grow a pixel sprite to a target size by duplicating the rows/columns that are most similar to their neighbour
(flat areas), never the same line twice in a row and avoiding protected bands (e.g. the face)."""
from PIL import Image
def _rows(im): return [[im.getpixel((x, y)) for x in range(im.width)] for y in range(im.height)]
def _diff(a, b): return sum(1 for p, q in zip(a, b) if p != q)
def grow_rows(im, n, protect=()):
    rows = _rows(im); used = set()
    for _ in range(n):
        best = None
        for y in range(1, len(rows)):
            if any(a <= y <= b for a, b in protect) or y in used or y - 1 in used or y + 1 in used: continue
            d = _diff(rows[y], rows[y - 1])
            if best is None or d < best[0]: best = (d, y)
        if best is None: break
        y = best[1]; rows.insert(y, list(rows[y]))
        used = {u + 1 if u >= y else u for u in used} | {y, y + 1}
        protect = tuple((a + 1 if a >= y else a, b + 1 if b >= y else b) for a, b in protect)
    out = Image.new('RGBA', (im.width, len(rows)))
    for y, r in enumerate(rows):
        for x, c in enumerate(r): out.putpixel((x, y), c)
    return out
def grow(im, target_h, target_w=None, protect_rows=(), protect_cols=()):
    im = grow_rows(im, target_h - im.height, protect_rows)
    if target_w:
        im = grow_rows(im.transpose(Image.TRANSPOSE), target_w - im.width, protect_cols).transpose(Image.TRANSPOSE)
    return im
