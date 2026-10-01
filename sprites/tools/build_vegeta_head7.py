"""Vegeta head v12: curved hair. Each spike is a 'blade' whose two edges are quadratic beziers bowing back,
rendered at 8x and downsampled (coverage) so curves survive; curved strand + separation lines drawn at 1x.
Face as in v11 (angry profile)."""
import os
from PIL import Image, ImageDraw
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W, H = 31, 32; SS = 8
O=(29,28,33); HAIR=(44,42,54); HL=(78,76,102); SK=(242,198,165); SH=(215,159,123); DK=(174,120,98); WH=(249,245,236)

def bez(p0, c, p1, n=24):
    return [((1-t)**2*p0[0] + 2*(1-t)*t*c[0] + t*t*p1[0], (1-t)**2*p0[1] + 2*(1-t)*t*c[1] + t*t*p1[1])
            for t in (i/n for i in range(n+1))]

# blade = (base_a, base_b, tip, bow): edges base_a->tip and tip->base_b bow by `bow` (perpendicular push, + = back/left)
BLADES = [
    ((6,12), (13,10), (3,0),   (-1.5, 2.5)),   # tallest, at the back
    ((10,10),(18,10), (12,1),  (-1.5, 2.0)),
    ((15,11),(23,12), (20,4),  (-1.2, 1.6)),
    ((20,13),(27,15), (25,8),  (-1.0, 1.2)),   # small front spike
    ((7,9),  (7,17),  (0,13),  (0.0, -2.0)),   # back spikes curving down
    ((7,15), (9,21),  (0,23),  (0.0, -2.0)),
    ((9,20), (13,25), (4,29),  (1.0, -1.5)),
]
def blade_poly(a, b, tip, bow):
    ma = ((a[0]+tip[0])/2 + bow[0], (a[1]+tip[1])/2 - bow[1]*0.3)
    mb = ((b[0]+tip[0])/2 + bow[0]*0.6, (b[1]+tip[1])/2 + bow[1]*0.2)
    # bow the front edge outward (convex) and the back edge inward (concave) -> flame curve
    ca = (ma[0] - 1.2, ma[1]); cb = (mb[0] + 1.2, mb[1] - 0.5)
    return bez(a, ca, tip) + bez(tip, cb, b)[1:]

big = Image.new('L', (W*SS, H*SS), 0); bd = ImageDraw.Draw(big)
S = lambda pts: [((x+0.5)*SS, (y+0.5)*SS) for x, y in pts]
# core hair mass (rounded skull + front edge curving down to the temple point)
core = bez((5,9),(14,4),(24,9)) + bez((24,9),(29,12),(26,15))[1:] + bez((26,15),(24,17),(22,17))[1:] \
     + bez((22,17),(20,13),(16,16))[1:] + bez((16,16),(13,21),(13,25))[1:] + bez((13,25),(6,22),(5,9))[1:]
bd.polygon(S(core), fill=255)
for bl in BLADES: bd.polygon(S(blade_poly(*bl)), fill=255)
hairmask = big.resize((W, H), Image.BOX)

im = Image.new('RGBA', (W, H), (0,0,0,0)); d = ImageDraw.Draw(im)
FACE = [(19,13),(24,11),(27,14),(28,18),(27,19),(29,22),(27,23),(27,26),(25,29),(21,30),(16,27),(14,22),(15,16)]
d.polygon(FACE, fill=SK); d.rectangle([16,27,21,31], fill=SH)
p = im.load()
for y in range(H):
    for x in range(W):
        if hairmask.getpixel((x, y)) >= 64: p[x, y] = HAIR + (255,)
def curve(p0, c, p1, col):
    last = None
    for (x, y) in bez(p0, c, p1, 40):
        q = (round(x), round(y))
        if q != last and 0 <= q[0] < W and 0 <= q[1] < H and p[q][3] and p[q][:3] in (HAIR, HL, O): p[q] = col + (255,)
        last = q
# curved separation lines between blades (dark) and light strands along each blade's spine
curve((9,11),(6,6),(4,2), O); curve((14,10),(12,6),(12,3), O); curve((19,11),(18,8),(20,6), O)
curve((8,15),(4,13),(2,13), O); curve((9,19),(5,20),(2,22), O); curve((11,23),(8,25),(6,27), O)
curve((7,10),(5,5),(4,3), HL); curve((12,9),(11,5),(12,3), HL); curve((17,10),(18,7),(20,6), HL)
curve((22,12),(23,10),(24,9), HL); curve((6,12),(3,12),(2,13), HL); curve((7,17),(4,19),(2,21), HL)
curve((10,22),(7,24),(6,26), HL)
# ear, face features (angry profile)
d.ellipse([13,17,18,24], fill=O); d.ellipse([14,18,17,23], fill=SK); d.line([(15,19),(15,22)], fill=SH); d.point((16,20), fill=DK)
d.line([(19,28),(24,29)], fill=SH); d.line([(21,23),(24,24)], fill=SH); d.point((27,21), fill=SH)
d.line([(20,17),(27,19)], fill=O, width=2)
d.line([(23,20),(25,20)], fill=WH); d.line([(26,20),(26,21)], fill=O); d.line([(23,21),(25,21)], fill=SH)
d.line([(25,25),(27,25)], fill=O); d.point((24,26), fill=SH)
# outline pass
src = im.copy(); s = src.load(); p = im.load()
for y in range(H):
    for x in range(W):
        nb = [(x+dx, y+dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)) if 0 <= x+dx < W and 0 <= y+dy < H]
        if s[x,y][3] == 0:
            if any(s[n][3] for n in nb): p[x,y] = O + (255,)
        elif s[x,y][:3] in (HAIR, HL) and any(s[n][3] and s[n][:3] in (SK, SH) for n in nb):
            p[x,y] = O + (255,)
im.save(f'{R}/chars/vegeta_head.png'); print(im.size)
