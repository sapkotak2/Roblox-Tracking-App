"""Recover native pixels from an upscaled (lossy) sheet crop: find the grid phase, sample block centres."""
from PIL import Image
def recover(crop, scale, bg, bg_tol=40):
    w, h = crop.size; px = crop.convert('RGB').load()
    best = None
    for ox in range(scale):
        for oy in range(scale):
            err = 0
            for by in range(oy, h - scale, scale * 3):
                for bx in range(ox, w - scale, scale * 3):
                    c = px[bx + scale // 2, by + scale // 2]
                    for dx, dy in ((1, 1), (scale - 2, scale - 2), (1, scale - 2)):
                        d = px[bx + dx, by + dy]; err += sum(abs(a - b) for a, b in zip(c, d))
            if best is None or err < best[0]: best = (err, ox, oy)
    _, ox, oy = best
    nw, nh = (w - ox) // scale, (h - oy) // scale
    out = Image.new('RGBA', (nw, nh), (0, 0, 0, 0)); o = out.load()
    for y in range(nh):
        for x in range(nw):
            # median of the inner 2x2 to resist compression noise
            cs = [px[ox + x*scale + scale//2 + a, oy + y*scale + scale//2 + b] for a in (-1, 0) for b in (-1, 0)]
            c = tuple(sorted(v[i] for v in cs)[1] for i in range(3))
            if sum(abs(a - b) for a, b in zip(c, bg)) > bg_tol: o[x, y] = c + (255,)
    bb = out.getbbox()
    return out.crop(bb), (ox, oy)
