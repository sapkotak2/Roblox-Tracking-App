"""Vegeta head v8 (30x31): hair = polygon traced by eye from the official profile art (spikes swept up/back,
front lock pointing down over the brow); face hand-placed; auto outline. Writes chars/vegeta_head.png"""
import os
from PIL import Image, ImageDraw
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W, H = 30, 31
O=(29,28,33); HAIR=(44,42,54); HL=(74,72,96); SK=(242,198,165); SH=(215,159,123); DK=(174,120,98); WH=(249,245,236)
im = Image.new('RGBA', (W, H), (0,0,0,0)); d = ImageDraw.Draw(im)
# face / skull skin (profile facing right)
d.polygon([(17,13),(23,12),(26,15),(27,18),(27,19),(29,22),(27,23),(27,26),(26,28),(23,29),(18,28),(15,24),(15,17)], fill=SK)
d.rectangle([17,27,21,30], fill=SH)                       # neck
# hair: big swept-back flame
HAIRPTS = [(3,0),(10,6),(11,0),(17,6),(21,1),(23,8),(26,12),(27,16),     # three tall spikes, leaning back
           (24,19),(23,15),(21,14),(18,16),(15,17),(14,24),(11,23),          # front lock -> hairline -> behind ear
           (3,24),(8,19),(0,15),(7,12),(1,6),(6,7)]                          # two big back spikes
d.polygon(HAIRPTS, fill=HAIR)
# highlight strands along the spikes
for a, b in (((5,2),(10,8)), ((12,3),(15,8)), ((20,4),(21,9)), ((4,9),(9,12)), ((5,19),(10,19))):
    d.line([a, b], fill=HL)

# ear (drawn over the hair so it reads)
d.ellipse([14,17,19,24], fill=O); d.ellipse([15,18,19,23], fill=SK); d.line([(16,19),(16,22)], fill=SH); d.point((17,20), fill=DK); d.point((17,21), fill=SH)
# face shading: jaw underside + cheekbone + nose side
d.line([(19,28),(25,28)], fill=SH); d.line([(21,23),(24,24)], fill=SH); d.point((27,21), fill=SH)
# angry brow: thick, pressing down toward the nose
d.line([(20,17),(26,19)], fill=O, width=2); d.line([(21,19),(22,19)], fill=O)
d.point((26,18), fill=O)
d.line([(25,16),(25,17)], fill=SH)                         # furrow above the brow knot
# narrow eye under the brow: white, pupil at the front
d.line([(22,20),(24,20)], fill=WH); d.point((23,21), fill=WH); d.point((24,21), fill=WH)
d.line([(25,20),(25,21)], fill=O); d.point((26,20), fill=O)  # pupil at the front
d.line([(22,22),(25,22)], fill=SH)                         # lower lid
# frown
d.line([(25,25),(27,25)], fill=O); d.point((24,26), fill=SH)
# outline pass
px = im.load(); out = im.copy(); po = out.load()
for y in range(H):
    for x in range(W):
        if px[x,y][3]: continue
        if any(0<=x+dx<W and 0<=y+dy<H and px[x+dx,y+dy][3] for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))):
            po[x,y] = O + (255,)
# hair edge pixels get the outline too (hair meets skin along the hairline)
for y in range(H):
    for x in range(W):
        if px[x,y][:3] == HAIR and any(0<=x+dx<W and 0<=y+dy<H and px[x+dx,y+dy][:3] in (SK,SH) for dx,dy in ((1,0),(-1,0),(0,1),(0,-1))):
            po[x,y] = O + (255,)
out.save(f'{R}/chars/vegeta_head.png')
