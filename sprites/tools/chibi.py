"""Chibi sprite framework: draw a character from scratch at the game's native size.

STYLE GUIDE (match the cast, e.g. Luffy / Krillin / Gon, and the reference redraw tools/chibi_chars/baki.py)
- Canvas: native pixels, character exactly 51 rows tall (feet on the last row), facing RIGHT, idle fighting stance.
- Proportions (Luffy): head (hair included) ~19 rows tall and ~22-27 wide; body ~32 rows; torso/legs core ~18-22 wide.
  Big characters (Big Mom, Katakuri, Escanor) may be wider and bulkier but stay 51 tall; slim ones (Makima, Asuna) narrower.
- Face 3/4 toward the right: far eye smaller on the left, near eye bigger on the right, nose 1-2 px at the right edge.
  Eyes are 2-4 px of white + 1 px pupil/iris (iris colour matters: Makima yellow ringed, Rengoku gold/red...).
- Every body part on its own Layer, outlined, stacked back to front (back arm/leg first, front arm last), so limbs that
  cross the body stay readable. Outline colour: a very dark tint (not pure black unless the character is mostly black).
- THE OWNER'S TARGET LOOK (reference sprites he showed: One Piece Luffy / Fujitora / Shanks, Naruto, Tanjiro chibis):
  details are EASY TO SEE. Not complex shading, no different colours close together, everything neat.
  * TWO tones per material: a base and ONE shade. A single extra highlight only where it really helps (hair shine,
    metal blade). No deep-shade + highlight + base + shade stacks, no gradients, no dithering.
  * Big flat areas of colour. Shade = a clear shape (under the hair on the face, the back side of a coat, a fold line),
    never scattered pixels. No single stray pixels anywhere.
  * Neighbouring materials must contrast strongly (skin vs cloth vs hair), so the outfit reads at a glance.
  * Hair: one big silhouette in the base colour + 2-5 dark strand lines + optional 1-2 shine pixels.
  * Faces simple: each eye = white + 1-2 dark/iris pixels, one dark brow line, mouth 1-3 px, nose 1 px or none.
  * Clothes: show only the iconic pieces (checkered haori, Marine coat with gold epaulettes, headband...), drawn as
    clean blocks; patterns simplified to a few big shapes.
  * Muscles (if any) as 2-4 shade lines, not a pile of tones.
  * Total roughly 10-18 colours. Light from the front-right; the back side gets the shade tone.
- WHAT THE OWNER CALLED UGLY (old Kenpachi, Guts, Okkotsu, Hitsugaya sprites) - never do this:
  * Too compact / squat: body crushed under the head, stubby legs, no neck, no waist. Good sprites are ~2.3 heads tall:
    head ~19-20 rows, then a visible neck, a torso that narrows to a waist, and legs ~13-15 rows long with a clear gap
    between them and readable feet. Arms clearly separate from the torso where the pose allows.
  * Detailed/noisy pixels: speckled armour, shredded coat edges, dithered hair. If a texture needs more than 2 tones
    or scattered pixels to show, simplify it into big flat shapes.
  * Unreadable face: the face must be an open skin area with nothing crossing it (no hair strands or noise over the
    eyes); eyes clearly placed, brow a clean line. You must be able to tell the face at 1x from across the room.
  * Mis-proportioned: head, torso, legs and props must look like one character at one scale (no giant hair blob on a
    tiny body, no sword bigger than the character).
- Signature features must read at 1x: hair silhouette, iconic outfit colours, weapons/props (Asta's sword, Erza's sword,
  Rengoku's flaming sword...), but props must not make the sprite huge (keep total width <= ~48).
- No text, no emoji.

USAGE (see tools/chibi_chars/baki.py):
    from chibi import Sprite
    sp = Sprite('baki', W=38, H=52, palette=dict(o=(40,10,10), s=(222,148,96), ...))
    arm = sp.layer().poly('s', [...]).ell('s', x0, y0, x1, y1).h('S', x0, x1, y).v('S', x, y0, y1).px('T', (x, y), ...)
    sp.add(arm)            # in back-to-front order
    sp.save()              # -> out/redraw/<name>.png (native, cropped) + out/redraw/<name>_cmp.png (8x vs old + cast)
Palette keys are single characters. px/h/v only recolour pixels that are already filled on that layer
(so details never leak outside a shape); poly/ell/rect fill.
"""
import os
from PIL import Image, ImageDraw
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OUT = f'{R}/out/redraw'


class Layer:
    def __init__(self, sp):
        self.sp = sp
        self.im = Image.new('RGBA', (sp.W, sp.H), (0, 0, 0, 0)); self.d = ImageDraw.Draw(self.im)
    def poly(self, k, pts): self.d.polygon(pts, fill=self.sp.C(k)); return self
    def ell(self, k, *b): self.d.ellipse(b, fill=self.sp.C(k)); return self
    def rect(self, k, *b): self.d.rectangle(b, fill=self.sp.C(k)); return self
    def line(self, k, pts, width=1): self.d.line(pts, fill=self.sp.C(k), width=width); return self
    def px(self, k, *pts):
        for x, y in pts:
            if 0 <= x < self.sp.W and 0 <= y < self.sp.H and self.im.getpixel((x, y))[3]:
                self.im.putpixel((x, y), self.sp.C(k))
        return self
    def put(self, k, *pts):
        """like px but also paints transparent pixels (for thin details sticking out: strands, sparks, blade tips)"""
        for x, y in pts:
            if 0 <= x < self.sp.W and 0 <= y < self.sp.H:
                self.im.putpixel((x, y), self.sp.C(k))
        return self
    def h(self, k, x0, x1, y): return self.px(k, *[(x, y) for x in range(x0, x1 + 1)])
    def v(self, k, x, y0, y1): return self.px(k, *[(x, y) for y in range(y0, y1 + 1)])
    def outlined(self, outline='o', skip=()):
        W, H = self.sp.W, self.sp.H
        src = self.im.copy(); out = self.im.copy(); c = self.sp.C(outline)
        for y in range(H):
            for x in range(W):
                if src.getpixel((x, y))[3] == 0: continue
                for dx, dy, side in ((1, 0, 'right'), (-1, 0, 'left'), (0, 1, 'bottom'), (0, -1, 'top')):
                    if side in skip: continue
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < W and 0 <= ny < H) or src.getpixel((nx, ny))[3] == 0:
                        out.putpixel((x, y), c); break
        return out


class Sprite:
    def __init__(self, name, W, H, palette):
        self.name, self.W, self.H, self.P = name, W, H, palette
        self.layers = []
    def C(self, k): return tuple(self.P[k]) + (255,)
    def layer(self): return Layer(self)
    def add(self, layer, outline='o', skip=(), outlined=True):
        self.layers.append((layer, outline, skip, outlined)); return layer
    def render(self):
        im = Image.new('RGBA', (self.W, self.H), (0, 0, 0, 0))
        for L, o, skip, ol in self.layers:
            im.alpha_composite(L.outlined(o, skip) if ol else L.im)
        return im.crop(im.getbbox())
    def save(self):
        os.makedirs(OUT, exist_ok=True)
        out = self.render()
        out.save(f'{OUT}/{self.name}.png')
        sheet(self.name)
        n = len(out.getcolors(4096) or [])
        print(f'{self.name}: {out.size[0]}x{out.size[1]}, {n} colours' + ('  (WARNING: should be 51 tall)' if out.size[1] != 51 else ''))
        return out


def sheet(name, scale=8):
    """8x comparison: old sprite (if any), NEW, Luffy, the reference Baki redraw, Krillin, Gon."""
    items = []
    old = f'{R}/final/native/{name}.png'
    if os.path.exists(old): items.append(('old ' + name, old))
    items.append(('NEW ' + name, f'{OUT}/{name}.png'))
    items += [('luffy', f'{R}/refs/game/luffy_native.png'), ('krillin', f'{R}/final/native/krillin.png'), ('gon', f'{R}/final/native/gon.png')]
    if name != 'baki' and os.path.exists(f'{OUT}/baki.png'): items.insert(2, ('baki (ref)', f'{OUT}/baki.png'))
    ims = [(n, Image.open(p).convert('RGBA')) for n, p in items]
    Hh = max(i.height for _, i in ims) * scale
    # official reference art (refs/redraw/<name>/, from tools/fetch_wiki_refs.py or picked by hand), same height
    refs = []
    rdir = f'{R}/refs/redraw/{name}'
    if os.path.isdir(rdir):
        pick = [l.strip() for l in open(f'{rdir}/USE.txt')] if os.path.exists(f'{rdir}/USE.txt') else sorted(f for f in os.listdir(rdir) if f.endswith('.png'))[:3]
        for f in pick:
            if f and os.path.exists(f'{rdir}/{f}'):
                im = Image.open(f'{rdir}/{f}').convert('RGBA'); im.thumbnail((int(Hh * 1.1), Hh)); refs.append(('ref ' + f[:18], im))
    sh = Image.new('RGBA', (sum(i.width * scale + 24 for _, i in ims) + sum(i.width + 24 for _, i in refs) + 24, Hh + 40), (214, 222, 234, 255))
    x = 24
    for n, i in ims:
        b = i.resize((i.width * scale, i.height * scale), Image.NEAREST)
        sh.alpha_composite(b, (x, 20 + Hh - b.height)); ImageDraw.Draw(sh).text((x, 4), n, fill=(0, 0, 0, 255))
        x += b.width + 24
    for n, i in refs:
        sh.alpha_composite(i, (x, 20 + Hh - i.height)); ImageDraw.Draw(sh).text((x, 4), n, fill=(160, 0, 0, 255))
        x += i.width + 24
    sh.save(f'{OUT}/{name}_cmp.png')


def lineup(names, path, scale=6, cols=10):
    """all redraws side by side at the same baseline, for a final consistency check"""
    ims = [(n, Image.open(f'{OUT}/{n}.png').convert('RGBA')) for n in names if os.path.exists(f'{OUT}/{n}.png')]
    cw = max(i.width for _, i in ims) * scale + 20; ch = max(i.height for _, i in ims) * scale + 30
    rows = (len(ims) + cols - 1) // cols
    sh = Image.new('RGBA', (cw * min(cols, len(ims)) + 20, ch * rows + 20), (214, 222, 234, 255))
    for k, (n, i) in enumerate(ims):
        b = i.resize((i.width * scale, i.height * scale), Image.NEAREST)
        x = 20 + (k % cols) * cw; y = 10 + (k // cols) * ch
        sh.alpha_composite(b, (x, y + ch - 20 - b.height)); ImageDraw.Draw(sh).text((x, y), n, fill=(0, 0, 0, 255))
    sh.save(path)
