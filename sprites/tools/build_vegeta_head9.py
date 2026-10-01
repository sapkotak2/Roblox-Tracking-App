"""Vegeta head v14: skull + face area taken pixel-for-pixel from the game's Luffy head (refs/game/luffy_native.png,
rows 0-20), shifted down 6 rows; Vegeta hair spikes added on top, widow's peak, angry V brows, glaring eye, frown.
o outline  h hair  H hair light  s skin  S skin shade  w eye white"""
import os
from PIL import Image
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
OFF = 6; W, H = 26, 21 + OFF
lu = Image.open(f'{R}/refs/game/luffy_native.png'); lp = lu.load()
def cls(c):
    r, gg, b, a = c
    if a == 0: return '.'
    if (r > 200 and gg > 150 and b > 110 and r - b > 40) or (r > 230 and gg > 230) or (r > 150 and gg > 100 and r - b > 50): return 's'
    return 'h'
g = [['.'] * W for _ in range(H)]
for y in range(21):
    for x in range(W):
        g[y + OFF][x] = cls(lp[x, y])
def sp(y, c, a, b):
    for x in range(a, b + 1): g[y][x] = c
# --- remove Luffy-specific bits: bangs over the forehead -> Vegeta's high forehead with a V peak
for y in range(10 + OFF, 14 + OFF):
    for x in range(13, 25):
        if g[y][x] == 'h': g[y][x] = 's'
sp(10 + OFF, 'h', 12, 25); sp(10 + OFF, 's', 13, 16); sp(10 + OFF, 's', 21, 23)    # hairline row
sp(9 + OFF, 'h', 12, 24)
for (x, y) in ((17, 10), (18, 10), (19, 10), (20, 10), (18, 11), (19, 11), (19, 12)):   # widow's peak V
    g[y + OFF][x] = 'h'
for y in range(10 + OFF, 17 + OFF): g[y][24] = 'h'; g[y][25] = 'h' if y < 14 + OFF else g[y][25]  # front temple lock
# --- clean face interior (Luffy's eye/grin/scar become plain skin; Vegeta features drawn below)
for y in range(13 + OFF, 21 + OFF):
    for x in range(11, 24):
        if g[y][x] == 'h' and not (y == 20 + OFF and x >= 16): g[y][x] = 's'
for x in range(16, 24): g[20 + OFF][x] = '.' if x > 21 else g[20 + OFF][x]
# --- spikes on top (rows 0-6) rising from Luffy's crown: back spike tallest, leaning slightly back
SPK = {0: [(4, 4)], 1: [(3, 5)], 2: [(3, 6), (14, 14)], 3: [(3, 7), (13, 15)], 4: [(3, 8), (12, 16), (21, 21)],
       5: [(3, 9), (11, 17), (20, 22)], 6: [(3, 10), (10, 18), (19, 23)], 7: [(2, 23)], 8: [(2, 24)]}
for y, spans in SPK.items():
    for a, b in spans: sp(y, 'h', a, b)
# back spikes jutting out behind the head
for (x, y) in ((0, 11), (1, 11), (0, 12), (0, 17), (1, 17), (1, 18), (0, 18), (2, 23), (3, 23)):
    g[y][x] = 'h'
# ear (Luffy's ear position) keep skin; add inner shade
for (x, y) in ((8, 15 + OFF), (8, 16 + OFF)): g[y][x] = 'S'
# --- Vegeta face: angry V brows meeting at the nose bridge, glaring eye, frown
for (x, y) in ((15, 12), (16, 12), (17, 13), (18, 13), (19, 13), (20, 14),     # near brow, sloping down to the nose
               (22, 12), (23, 12), (21, 13)):                                  # far brow, sloping down the other way
    g[y + OFF][x] = 'o'
for (x, y) in ((18, 14), (19, 14), (18, 15), (19, 15)): g[y + OFF][x] = 'w'     # eye white
for (x, y) in ((20, 15), (17, 14)): g[y + OFF][x] = 'o'                          # pupil at the front, eye corner
for (x, y) in ((17, 16), (18, 16), (19, 16), (22, 15), (16, 17)): g[y + OFF][x] = 'S'   # lower lid, cheek, nose shade
for (x, y) in ((18, 18), (19, 18), (20, 18), (21, 18), (17, 19)): g[y + OFF][x] = 'o'   # frown
for (x, y) in ((18, 19), (19, 19), (12, 19), (13, 20)): g[y + OFF][x] = 'S'
# --- hair light strands along spike front edges (the curves), then outline pass
for (x, y) in ((5, 1), (6, 2), (7, 3), (8, 4), (9, 5), (10, 6), (15, 3), (16, 4), (17, 5), (18, 6), (22, 5), (23, 6),
               (3, 9), (4, 10), (5, 11), (2, 13), (3, 14), (2, 18), (3, 19)):
    if g[y][x] == 'h': g[y][x] = 'H'
solid = {(x, y) for y in range(H) for x in range(W) if g[y][x] != '.'}
out = [r[:] for r in g]
for (x, y) in solid:
    if g[y][x] in 'hH':
        if any((x + dx, y + dy) not in solid or g[y + dy][x + dx] in 'sS' for dx, dy in ((1,0),(-1,0),(0,1),(0,-1))
               if 0 <= x + dx < W and 0 <= y + dy < H) or x in (0, W - 1) or y == 0:
            out[y][x] = 'o'
for y in range(H):
    for x in range(W):
        if g[y][x] == '.' and any(0 <= x+dx < W and 0 <= y+dy < H and g[y+dy][x+dx] in 'sS' for dx, dy in ((1,0),(-1,0),(0,1),(0,-1))):
            out[y][x] = 'o'
PAL = """o 1d1c21
h 2c2a36
H 4e4c66
s f2c6a5
S d79f7b
w f9f5ec"""
open(f'{R}/chars/vegeta_head.txt', 'w').write("# Vegeta head v14 (tools/build_vegeta_head9.py)\n# palette\n" + PAL + "\n# grid\n" + '\n'.join(''.join(r) for r in out) + '\n')
