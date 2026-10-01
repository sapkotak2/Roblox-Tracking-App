from PIL import Image
def snap(im, palette):
    """nearest-colour snap every opaque pixel to a fixed palette (list of (r,g,b))."""
    out = im.copy(); px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if a == 0: continue
            best = min(palette, key=lambda p: (p[0]-r)**2 + (p[1]-g)**2 + (p[2]-b)**2)
            px[x, y] = best + (255,)
    return out
