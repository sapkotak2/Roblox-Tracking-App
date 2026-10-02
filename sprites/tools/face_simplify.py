"""Simplify the head: merge near-identical shades (within `tol`) onto the most common one, so a face reads as a
few flat colours. Outlines/near-black and pure whites (eye highlights) are never merged away."""
from PIL import Image
def simplify_head(im, rows=19, tol=70):
    im = im.convert('RGBA'); p = im.load(); cnt = {}
    for y in range(min(rows, im.height)):
        for x in range(im.width):
            c = p[x, y]
            if c[3]: cnt[c[:3]] = cnt.get(c[:3], 0) + 1
    protected = lambda c: max(c) < 50 or min(c) > 235
    reps = []
    for c, _ in sorted(cnt.items(), key=lambda kv: -kv[1]):
        if protected(c): continue
        if not any(sum(abs(a - b) for a, b in zip(c, r)) < tol for r in reps): reps.append(c)
    def near(c):
        if protected(c): return c
        best = min(reps, key=lambda r: sum(abs(a - b) for a, b in zip(c, r)))
        return best if sum(abs(a - b) for a, b in zip(c, best)) < tol else c
    for y in range(min(rows, im.height)):
        for x in range(im.width):
            c = p[x, y]
            if c[3]: p[x, y] = near(c[:3]) + (255,)
    return im
