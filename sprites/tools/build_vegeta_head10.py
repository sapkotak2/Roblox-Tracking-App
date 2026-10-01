"""Vegeta head v15 - hand-authored fills (outline added automatically), sized to the game's Luffy head:
face ~13 px wide x 10 rows on the lower right, ear at x7-9, plus upright spikes (+6 rows), back spikes,
V widow's peak, angry V brows, glaring eye, frown.  h hair  H hair light  s skin  S shade  w white  k dark line"""
import os
from PIL import Image
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FW, FH = 25, 24
g = [['.'] * FW for _ in range(FH)]
def sp(y, *spans):
    for c, a, b in spans:
        for x in range(a, b + 1): g[y][x] = c
# spikes: back (tallest) - middle - front, each leaning slightly back
sp(0, ('h',3,3),                         ('h',13,13))
sp(1, ('h',3,4),             ('h',12,13))
sp(2, ('h',3,5),             ('h',11,14),             ('h',21,21))
sp(3, ('h',3,6),             ('h',10,15),             ('h',20,21))
sp(4, ('h',3,7),             ('h',9,16),              ('h',19,22))
sp(5, ('h',3,8),             ('h',9,17),              ('h',18,22))
sp(6, ('h',3,22))
sp(7, ('h',2,22))
sp(8, ('h',1,23))
sp(9, ('h',0,23))                      # back spike 1 tip
sp(10,('h',1,23))
sp(11,('h',2,23))
sp(12,('h',1,23))
# forehead with V widow's peak (peak x17-19), temple lock on the far side (x22-23)
sp(13,('h',0,11), ('s',12,16), ('h',17,19), ('s',20,21), ('h',22,23))
sp(14,('h',1,10), ('s',11,17), ('h',18,18), ('s',19,22), ('h',23,23))
sp(15,('h',2,10), ('s',11,23))
sp(16,('h',1,9),  ('s',10,23))
sp(17,('h',0,6),  ('s',7,24))           # back spike 2 tip, ear starts, nose bridge
sp(18,('h',1,6),  ('s',7,24))
sp(19,('h',2,6),  ('s',7,23))
sp(20,('h',2,6),  ('s',7,23))
sp(21,('h',1,6),  ('s',9,22))           # back spike 3
sp(22,('h',3,7),  ('s',11,21))
sp(23,('h',5,7),  ('s',13,19))
# ---- features
for x, y in ((12,15),(13,15),(14,15),(15,16),(16,16),(17,16),        # near brow sloping down to the nose
             (21,15),(22,15),(20,16),(19,16)):                       # far brow sloping down the other way -> V
    g[y][x] = 'k'
for x, y in ((14,17),(15,17),(14,18),(15,18)): g[y][x] = 'w'         # eye white
for x, y in ((16,17),(16,18),(13,17)): g[y][x] = 'k'                 # pupil at the front + outer corner
for x, y in ((14,19),(15,19),(16,19),(21,17),(22,18)): g[y][x] = 'S' # lower lid, nose side
for x, y in ((17,21),(18,21),(19,21),(16,22),(20,22)): g[y][x] = 'k' # frown
for x, y in ((8,18),(8,19),(9,20),(12,22),(13,23),(14,23)): g[y][x] = 'S'   # ear inner, jaw shade
g[17][10] = 'k'; g[18][10] = 'k'; g[19][10] = 'k'; g[20][9] = 'k'    # ear outline (front edge)
# ---- re-layout: tall spikes (10 rows, deep notches) on top of a shorter hair base
def spans_for(y):
    out = []
    # back spike: tip (3,0), back edge vertical, front edge slopes to the notch at (9,9)
    out.append((3, 3 + round(y * 0.62)))
    # middle spike: tip (13,0); back edge from notch (9,9), front edge to notch (18,9)
    if y >= 0: out.append((13 - round(y * 0.45), 13 + round(y * 0.55)))
    # front spike: tip (21,3); back edge from notch (18,9), front edge to (23,10)
    if y >= 3: out.append((21 - round((y - 3) * 0.5), 21 + round((y - 3) * 0.34)))
    return out
top = [['.'] * FW for _ in range(10)]
for y in range(10):
    for a, b in spans_for(y):
        for x in range(a, b + 1): top[y][x] = 'h'
keep = [6, 8, 9, 11, 12] + list(range(13, FH))
g = top + [g[r] for r in keep]
FH = len(g)
# hair light strands along the spike edges
for x, y in ((4,1),(4,2),(5,3),(6,4),(6,5),(7,6),(8,7),(13,1),(14,2),(14,3),(15,4),(16,5),(16,6),(17,7),(21,4),(22,5),(22,6),(2,12),(3,13),(1,19),(2,20),(2,23)):
    if g[y][x] == 'h': g[y][x] = 'H'
P = {'h': (44,42,54), 'H': (78,76,102), 's': (242,198,165), 'S': (215,159,123), 'w': (249,245,236), 'k': (29,28,33)}
O = (29,28,33)
im = Image.new('RGBA', (FW + 2, FH + 1), (0,0,0,0)); p = im.load()
for y in range(FH):
    for x in range(FW):
        if g[y][x] != '.': p[x+1, y] = P[g[y][x]] + (255,)
src = im.copy(); s = src.load()
for y in range(im.height):
    for x in range(im.width):
        nb = [(x+dx, y+dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)) if 0 <= x+dx < im.width and 0 <= y+dy < im.height]
        if s[x,y][3] == 0:
            if any(s[n][3] for n in nb): p[x,y] = O + (255,)
        elif s[x,y][:3] in (P['h'], P['H']) and any(s[n][3] and s[n][:3] in (P['s'], P['S']) for n in nb):
            p[x,y] = O + (255,)
# top spike tips: put the outline pixel on the tip itself so spikes stay sharp
im.save(f'{R}/chars/vegeta_head.png'); print(im.size)
