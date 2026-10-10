"""Daki (Demon Slayer), awakened form - chibi redraw (see tools/chibi.py for the style guide).
Checklist: refs/redraw/daki/NOTES.md (silver-white hair swept up with green-tipped ends + red fan kanzashi, sharp green
eyes with red flicks, pink flower marks, smirk, red ball earrings, black V halter, pink/orange obi, crimson bottom,
black thigh-highs with white bands, tall black geta, pink sashes with orange stripes + dark flower motifs)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(36, 14, 32),                                   # outline
    h=(230, 232, 244), H=(160, 164, 192),             # silver-white hair (also eye whites, white bands)
    g=(176, 226, 84),                                 # lime green hair tips / green eyes
    s=(248, 228, 218), S=(206, 180, 182),             # pale skin
    r=(196, 32, 84), R=(116, 18, 54),                 # crimson (bottom, stocking pattern, lips, eyeliner, fans, earrings)
    k=(40, 30, 42),                                   # black outfit / geta / flower motifs
    p=(242, 116, 184), P=(186, 70, 142),              # pink sash + flower marks
    y=(246, 172, 60),                                 # orange stripes / gold
)
sp = Sprite('daki', W=52, H=52, palette=PAL)


def ribbon(ctrl, w0, w1, n=24):
    """smooth sash polygon along a quadratic-bezier chain of control points (width w0 -> w1); returns poly, centre, normals"""
    c = []
    for i in range(0, len(ctrl) - 2, 2):
        (ax, ay), (bx, by), (cx, cy) = ctrl[i], ctrl[i + 1], ctrl[i + 2]
        for k in range(n + 1):
            t = k / n
            c.append(((1 - t) ** 2 * ax + 2 * (1 - t) * t * bx + t * t * cx, (1 - t) ** 2 * ay + 2 * (1 - t) * t * by + t * t * cy))
    L, R, N = [], [], []
    for i, (x, y) in enumerate(c):
        x0, y0 = c[max(i - 1, 0)]; x1, y1 = c[min(i + 1, len(c) - 1)]
        dx, dy = x1 - x0, y1 - y0; d = math.hypot(dx, dy) or 1
        hw = (w0 + (w1 - w0) * i / (len(c) - 1)) / 2
        nx, ny = -dy / d, dx / d
        L.append((x + nx * hw, y + ny * hw)); R.append((x - nx * hw, y - ny * hw)); N.append((nx, ny))
    return L + R[::-1], c, N


def sash(ctrl, w0, w1, stripes, motifs, shade_side=1):
    """pink sash: shade along one edge, orange stripe bands across it, dark four-petal motifs"""
    lay = sp.layer()
    poly, c, N = ribbon(ctrl, w0, w1)
    lay.poly('p', poly)
    for (x, y), (nx, ny) in zip(c, N):                                       # shaded edge
        lay.px('P', (round(x - shade_side * nx * (w0 / 2 - 1)), round(y - shade_side * ny * (w0 / 2 - 1))))
    for f in stripes:                                                        # orange bands across the sash
        i = int(f * (len(c) - 1)); (x, y), (nx, ny) = c[i], N[i]
        tx, ty = ny, -nx
        for a in range(-4, 5):
            for b in (0, 1):
                lay.px('y', (round(x + nx * a / 1.3 + tx * b), round(y + ny * a / 1.3 + ty * b)))
    for f in motifs:                                                         # four-petal flower motif
        i = int(f * (len(c) - 1)); x, y = round(c[i][0]), round(c[i][1])
        lay.px('k', (x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1))
    return lay


# ---------------- sash behind her: from the obi out to the left and up over her shoulder ----------------
sash_b = sash([(16, 29), (2, 33), (2, 20), (2, 8), (11, 5)], 6, 5, stripes=(0.22, 0.62), motifs=(0.42, 0.85), shade_side=-1)

# ---------------- very long white hair behind her, ending in green wavy strands ----------------
back_hair = sp.layer()
back_hair.poly('h', [(12, 8), (17, 14), (16, 32), (12, 35), (8, 33), (9, 20)])
back_hair.poly('h', [(29, 9), (33, 14), (34, 30), (30, 33), (28, 20)])
back_hair.v('H', 11, 14, 32).v('H', 13, 22, 33).v('H', 32, 16, 30)
tips = sp.layer()
for pts in ([(8, 30), (12, 31), (10, 35), (11, 39), (9, 43), (7, 42), (8, 38), (6, 34)],
            [(12, 32), (16, 32), (14, 36), (16, 40), (14, 43), (12, 40), (12, 36)],
            [(29, 29), (34, 29), (36, 33), (35, 37), (37, 41), (34, 41), (32, 37), (32, 33)]):
    tips.poly('g', pts)

# ---------------- back arm: hanging, clawed hand ----------------
back_arm = sp.layer().poly('s', [(15, 20), (19, 21), (14, 31), (11, 30)]).v('S', 13, 25, 29).px('S', (12, 29), (12, 30))
back_hand = sp.layer().ell('s', 9, 29, 14, 34).px('r', (9, 33), (11, 34), (13, 34)).px('S', (10, 32), (11, 32))

# ---------------- legs: pale thighs, white band, black stockings with a crimson vine, tall black geta ----------------
def leg(pts, top, cx):
    L = sp.layer().poly('s', pts)
    L.h('h', 0, 51, top).h('H', 0, 51, top + 1)                              # white band at the top of the stocking
    for y in range(top + 2, 47):
        L.h('k', 0, 51, y)
    L.h('h', 0, 51, 46)                                                      # white ankle tie
    L.v('r', cx, top + 3, 44).px('r', (cx - 1, top + 5), (cx + 1, top + 8), (cx - 1, top + 11))   # crimson floral vine
    return L
leg_b = leg([(15, 32), (21, 32), (18, 46), (12, 46)], 36, 16).px('S', (15, 33), (15, 34), (16, 35))
leg_f = leg([(21, 32), (27, 32), (30, 46), (24, 46)], 36, 26).px('S', (22, 33), (22, 34))
geta_b = sp.layer().rect('k', 10, 47, 18, 50).h('h', 11, 17, 47)
geta_f = sp.layer().rect('k', 23, 47, 31, 50).h('h', 24, 30, 47)

# ---------------- torso: black V halter, pink/orange obi, black front strip, crimson bottom ----------------
torso = sp.layer()
torso.rect('s', 18, 16, 23, 21).v('S', 18, 16, 21).h('S', 19, 22, 17)                     # neck
torso.poly('s', [(15, 20), (26, 20), (27, 24), (25, 28), (26, 33), (15, 33), (16, 28), (14, 24)])
torso.poly('k', [(15, 20), (18, 20), (19, 26), (15, 26)]).poly('k', [(23, 20), (26, 20), (27, 24), (26, 26), (22, 26)])  # halter bands, deep V
torso.px('S', (20, 25), (21, 25))
torso.h('p', 15, 26, 27).h('p', 15, 26, 28).h('p', 15, 26, 29)                            # obi band
torso.px('y', (17, 29), (18, 28), (19, 27), (18, 29), (19, 28), (20, 27), (24, 29), (25, 28), (26, 27), (25, 29), (26, 28))
torso.px('P', (15, 29), (16, 29))
torso.poly('r', [(15, 30), (26, 30), (26, 32), (22, 34), (19, 34), (15, 32)]).h('R', 15, 26, 30)   # crimson bottom
torso.v('k', 20, 26, 35).v('k', 21, 26, 35)                                                # black strip down the front
torso.px('R', (16, 31), (24, 31), (25, 32))

# ---------------- head: silver hair swept up off the forehead, sharp green eyes, flower marks ----------------
head = sp.layer()
head.ell('h', 11, 3, 31, 19)
head.ell('h', 14, 1, 30, 9)                                                               # high swept-up top
head.poly('s', [(16, 7), (29, 6), (30, 10), (29, 15), (26, 18), (19, 18), (16, 15)])      # face, open forehead
head.poly('h', [(15, 5), (22, 4), (29, 5), (30, 7), (25, 6), (19, 7), (16, 10)])          # swept-back hairline
head.poly('h', [(13, 8), (17, 8), (17, 17), (14, 20)])                                     # far side lock
head.poly('H', [(11, 9), (14, 5), (15, 17), (12, 17)])                                     # back of the head in shade
head.px('H', (17, 2), (18, 2), (19, 3), (22, 1), (23, 2), (24, 3), (27, 2), (28, 3))       # swept strand lines
head.px('s', (16, 11), (16, 12)).px('S', (17, 12))                                         # ear
# thin high arched brows
head.px('o', (18, 8), (19, 7), (20, 7)).px('o', (23, 7), (24, 7), (25, 6), (26, 6), (27, 7))
# sharp eyes tilted up, red eyeliner flicks at the outer corners, yellow-green irises with slit pupils
head.h('o', 18, 20, 9).px('r', (18, 9))
head.px('h', (18, 10), (18, 11), (18, 12)).px('g', (19, 10), (20, 10), (19, 11), (20, 11), (19, 12), (20, 12)).px('o', (20, 10), (20, 11))
head.h('o', 23, 26, 9).px('r', (27, 8), (27, 9))
head.px('h', (23, 10), (23, 11), (23, 12)).px('g', (24, 10), (26, 10), (24, 11), (26, 11), (24, 12), (25, 12), (26, 12)).px('o', (25, 10), (25, 11))
head.px('P', (27, 13), (26, 14), (28, 14), (27, 15)).px('r', (27, 14))                     # pink flower mark on the cheek
head.px('S', (28, 13)).px('r', (23, 16), (24, 16)).px('S', (25, 15))                       # nose, pink smirk
ornaments = sp.layer()                                                                     # red fan kanzashi on top
for x0, y0 in ((13, 2), (21, 0), (28, 2)):
    ornaments.poly('r', [(x0 - 3, y0), (x0 + 3, y0), (x0 + 1, y0 + 4), (x0 - 1, y0 + 4)]).px('y', (x0, y0 + 3)).h('R', x0 - 2, x0 + 2, y0 + 1)
earring = sp.layer().ell('r', 14, 13, 17, 16)

# ---------------- front arm: hand on the hip, elbow out ----------------
front = sp.layer()
front.poly('s', [(25, 20), (29, 21), (32, 27), (29, 28), (27, 24)]).v('S', 28, 25, 27)
front.poly('s', [(29, 25), (32, 27), (28, 32), (25, 31)]).px('S', (26, 31), (27, 31)).px('r', (25, 31))
ribbon_tie = sp.layer().poly('r', [(26, 30), (29, 31), (28, 37), (26, 37)]).v('R', 26, 32, 37)   # red ribbon tied at the hip

# ---------------- front sash: from the obi out to the right and down ----------------
sash_f = sash([(26, 29), (40, 27), (42, 37), (43, 44), (38, 47)], 6, 5, stripes=(0.3, 0.72), motifs=(0.15, 0.52, 0.88))

for L in (sash_b, sash_f, back_hair, tips, back_arm, back_hand, leg_b, leg_f, geta_b, geta_f, torso, head, ornaments, earring,
          ribbon_tie, front):
    sp.add(L)
sp.save()
