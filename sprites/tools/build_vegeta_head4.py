"""Vegeta head v9: hair + skin silhouettes taken directly from the official profile art
(refs/vegeta/profile_head_ref.png) by colour masks, downscaled with coverage thresholds so spike tips survive.
Eye/brow/mouth hand-placed at the positions they sit in the art. Writes chars/vegeta_head.png"""
import os
from PIL import Image, ImageFilter
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
O=(29,28,33); HAIR=(44,42,54); HL=(74,72,96); SK=(242,198,165); SH=(215,159,123); DK=(174,120,98); WH=(249,245,236)
ref = Image.open(f'{R}/refs/vegeta/profile_head_ref.png').convert('RGB')
w, h = ref.size; px = ref.load()
hair = Image.new('L', (w, h), 0); skin = Image.new('L', (w, h), 0); hp = hair.load(); sp = skin.load()
for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]
        if r + g + b < 200 and y < 132: hp[x, y] = 255           # below y=132 on the left is the suit collar
        elif r > 200 and 150 < g < 235 and b < 200 and r - b > 35: sp[x, y] = 255
skin = skin.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(3))   # close the halftone dots
# everything inside the head outline that isn't hair is face (lines, eye) -> treat as skin
TW = 30; TH = round(h * TW / w)
def cover(m, thr):
    s = m.resize((TW, TH), Image.BOX); return [[s.getpixel((x, y)) >= thr * 255 for x in range(TW)] for y in range(TH)]
H_ = cover(hair, 0.30); S_ = cover(skin, 0.40)
G = [[None] * TW for _ in range(TH)]
for y in range(TH):
    for x in range(TW):
        if S_[y][x]: G[y][x] = SK
        elif H_[y][x]: G[y][x] = HAIR
# fill face holes (eye/brow lines were black in the art and got classed as hair inside the face)
sx = lambda X: round(X * TW / w); sy = lambda Y: round(Y * TH / h)
im = Image.new('RGBA', (TW, TH + 3), (0, 0, 0, 0)); p = im.load()
for y in range(TH):
    for x in range(TW):
        if G[y][x]: p[x, y] = G[y][x] + (255,)
from PIL import ImageDraw
d = ImageDraw.Draw(im)
# re-skin the face interior region (front of the head, right of the ear) where art line-work was misread as hair
face_poly = [(sx(118), sy(70)), (sx(150), sy(80)), (sx(160), sy(100)), (sx(165), sy(118)), (sx(158), sy(140)),
             (sx(150), sy(160)), (sx(128), sy(160)), (sx(112), sy(140)), (sx(115), sy(95))]
d.polygon(face_poly, fill=SK)
d.rectangle([sx(108), sy(150), sx(132), TH + 2], fill=SH)                      # neck
d.ellipse([sx(92), sy(92), sx(117), sy(138)], fill=O); d.ellipse([sx(96), sy(96), sx(115), sy(134)], fill=SK)   # ear
d.line([(sx(104), sy(104)), (sx(104), sy(128))], fill=SH)
# angry brow (art: from ~(122,92) down to (152,110)), thick
d.line([(sx(120), sy(90)), (sx(152), sy(108))], fill=O, width=2)
# narrow eye under it, pupil at the front
ex, ey = sx(138), sy(110)
d.line([(ex - 2, ey), (ex, ey)], fill=WH); d.point((ex + 1, ey), fill=O); d.point((ex + 1, ey + 1), fill=O)
d.line([(ex - 2, ey + 1), (ex, ey + 1)], fill=WH); d.line([(ex - 2, ey + 2), (ex + 1, ey + 2)], fill=SH)
# frown + cheek line
d.line([(sx(142), sy(142)), (sx(158), sy(140))], fill=O)
d.line([(sx(128), sy(128)), (sx(138), sy(134))], fill=SH)
d.line([(sx(118), sy(156)), (sx(146), sy(158))], fill=SH)                      # under-jaw shade
# hair highlight strands along the spikes (art spikes point up-left)
for a, b in (((sx(45), sy(30)), (sx(80), sy(70))), ((sx(95), sy(30)), (sx(110), sy(70))), ((sx(30), sy(95)), (sx(70), sy(100)))):
    d.line([a, b], fill=HL)
# outline: transparent pixels touching the sprite, and hair pixels touching skin
src = im.copy(); s = src.load(); p = im.load()
for y in range(im.height):
    for x in range(im.width):
        nb = [(x+dx, y+dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)) if 0 <= x+dx < im.width and 0 <= y+dy < im.height]
        if s[x, y][3] == 0 and any(s[n][3] for n in nb): p[x, y] = O + (255,)
        elif s[x, y][:3] in (HAIR, HL) and any(s[n][3] and s[n][:3] in (SK, SH) for n in nb): p[x, y] = O + (255,)
im = im.crop(im.getbbox())
im.save(f'{R}/chars/vegeta_head.png'); print(im.size)
