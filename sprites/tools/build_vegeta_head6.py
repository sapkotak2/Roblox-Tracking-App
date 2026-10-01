"""Vegeta head v11 (30x32): polygons following the official profile art - tall narrow top spikes with deep notches,
three long back spikes, front hair edge running down to a temple point, long face with pointed chin."""
import os
from PIL import Image, ImageDraw
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W, H = 31, 32
O=(29,28,33); HAIR=(44,42,54); HL=(74,72,96); SK=(242,198,165); SH=(215,159,123); DK=(174,120,98); WH=(249,245,236)
im = Image.new('RGBA', (W, H), (0,0,0,0)); d = ImageDraw.Draw(im)
FACE = [(19,13),(24,11),(27,14),(28,18),(27,19),(29,22),(27,23),(27,26),(25,29),(21,30),(16,27),(14,22),(15,16)]
HAIRP = [(3,0),(10,7),(12,2),(16,8),(19,5),(22,10),(24,8),(26,11),(27,13),     # flame tilted back: highest at the back
         (22,17),(19,14),(16,17),(14,24),(12,27),                                # temple point, hairline, behind ear
         (8,25),(4,29),(6,22),(0,22),(5,16),(0,14),(4,9)]                         # back spikes pointing down/back
d.polygon(FACE, fill=SK)
d.rectangle([16,27,21,31], fill=SH)
d.polygon(HAIRP, fill=HAIR)
for a, b in (((4,3),(9,9)), ((12,5),(14,9)), ((19,8),(20,11)), ((2,15),(7,14)), ((2,21),(7,20)), ((6,26),(9,23))):
    d.line([a, b], fill=HL)
d.ellipse([13,17,18,24], fill=O); d.ellipse([14,18,17,23], fill=SK); d.line([(15,19),(15,22)], fill=SH); d.point((16,20), fill=DK)
d.line([(19,28),(24,29)], fill=SH); d.line([(21,23),(24,24)], fill=SH); d.point((27,21), fill=SH)
d.line([(20,17),(27,19)], fill=O, width=2)                       # long angry brow, down to the nose
d.line([(23,20),(25,20)], fill=WH); d.line([(26,20),(26,21)], fill=O)
d.line([(23,21),(25,21)], fill=SH)
d.line([(25,25),(27,25)], fill=O)                                # frown
d.point((24,26), fill=SH)
src = im.copy(); s = src.load(); p = im.load()
for y in range(H):
    for x in range(W):
        nb = [(x+dx, y+dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)) if 0 <= x+dx < W and 0 <= y+dy < H]
        if s[x,y][3] == 0:
            if any(s[n][3] for n in nb): p[x,y] = O + (255,)
        elif s[x,y][:3] in (HAIR, HL) and any(s[n][3] and s[n][:3] in (SK, SH) for n in nb):
            p[x,y] = O + (255,)
im.save(f'{R}/chars/vegeta_head.png'); print(im.size)
