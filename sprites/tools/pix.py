"""Tiny pixel-art toolkit: canvas, shapes, auto-outline, auto-shade, sheet renderer."""
from PIL import Image, ImageDraw
W, H = 48, 72
OY = 4  # logical y=0 is head top; spikes may go to y=-4
OUT = (22, 16, 34)

def hx(s):
    s = s.lstrip('#'); return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))

def shade(c, f=0.78):
    return tuple(max(0, int(v * f)) for v in c)

def light(c, f=1.18):
    return tuple(min(255, int(v * f)) for v in c)

class Canvas:
    def __init__(self):
        self.g = {}
        self.shadeable = {}

    def px(self, x, y, c, sh=True):
        y += OY
        if 0 <= x < W and 0 <= y < H:
            self.g[(x, y)] = c
            if sh: self.shadeable[(x, y)] = True

    def rect(self, x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.px(x, y, c)

    def ellipse(self, x0, y0, x1, y1, c):
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        rx, ry = (x1 - x0 + 1) / 2, (y1 - y0 + 1) / 2
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0:
                    self.px(x, y, c)

    def poly(self, pts, c):
        im = Image.new('1', (W, H), 0)
        ImageDraw.Draw(im).polygon([(a, b + OY) for a, b in pts], fill=1)
        for y in range(H):
            for x in range(W):
                if im.getpixel((x, y)): self.px(x, y - OY, c)

    def line(self, x0, y0, x1, y1, c, t=1):
        im = Image.new('1', (W, H), 0)
        ImageDraw.Draw(im).line([(x0, y0 + OY), (x1, y1 + OY)], fill=1, width=t)
        for y in range(H):
            for x in range(W):
                if im.getpixel((x, y)): self.px(x, y - OY, c)

    def clear(self, x, y):
        self.g.pop((x, y + OY), None)

    def finish(self, shade_f=0.8):
        """auto-shade (pixels sitting on the lower/left edge) then 1px outline."""
        occupied = set(self.g)
        res = dict(self.g)
        for (x, y), c in self.g.items():
            if not self.shadeable.get((x, y)): continue
            below = (x, y + 1) not in occupied
            left = (x - 1, y) not in occupied
            if below or left:
                res[(x, y)] = shade(c, shade_f)
        for (x, y) in occupied:
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                n = (x + dx, y + dy)
                if n not in occupied and 0 <= n[0] < W and 0 <= n[1] < H:
                    res[n] = OUT
        self.g = res
        return self

    def image(self):
        im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        for (x, y), c in self.g.items():
            im.putpixel((x, y), tuple(c) + (255,))
        return im

def sheet(items, path, scale=6, bg=(206, 220, 236), cols=None, label_h=10):
    cols = cols or len(items)
    rows = (len(items) + cols - 1) // cols
    cw, ch = W * scale, H * scale + label_h
    out = Image.new('RGBA', (cw * cols, ch * rows), bg + (255,))
    d = ImageDraw.Draw(out)
    for i, (name, im) in enumerate(items):
        x, y = (i % cols) * cw, (i // cols) * ch
        out.alpha_composite(im.resize((W * scale, H * scale), Image.NEAREST), (x, y))
        d.text((x + 4, y + H * scale - 4), name, fill=(20, 20, 40, 255))
    out.save(path)
