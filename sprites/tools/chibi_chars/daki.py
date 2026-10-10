"""Daki (Demon Slayer) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(30, 12, 26),                                   # outline
    h=(50, 40, 60), H=(26, 20, 34), l=(112, 100, 136),  # black hair (+ shine)
    s=(252, 226, 216), S=(216, 176, 172),             # pale skin
    e=(252, 250, 244), g=(160, 214, 80),              # eye white, yellow-green iris
    r=(144, 28, 50), R=(78, 14, 32),                  # dark red / black outfit
    p=(242, 128, 178), P=(166, 74, 150),              # pink obi sashes, purple pattern / flower marks
    y=(244, 196, 72),                                 # gold hairpins
)
sp = Sprite('daki', W=48, H=52, palette=PAL)
X = 6   # shift the whole character right to leave room for the sash behind her

def P(pts):
    return [(x + X, y) for x, y in pts]

def ribbon(ctrl, w0, w1, n=24):
    """smooth sash polygon along a quadratic-bezier chain of control points, width w0 -> w1"""
    import math
    c = []
    for i in range(0, len(ctrl) - 2, 2):
        (ax, ay), (bx, by), (cx, cy) = ctrl[i], ctrl[i + 1], ctrl[i + 2]
        for k in range(n + 1):
            t = k / n
            c.append(((1 - t) ** 2 * ax + 2 * (1 - t) * t * bx + t * t * cx, (1 - t) ** 2 * ay + 2 * (1 - t) * t * by + t * t * cy))
    L, R = [], []
    for i, (x, y) in enumerate(c):
        x0, y0 = c[max(i - 1, 0)]; x1, y1 = c[min(i + 1, len(c) - 1)]
        dx, dy = x1 - x0, y1 - y0; d = math.hypot(dx, dy) or 1
        hw = (w0 + (w1 - w0) * i / (len(c) - 1)) / 2
        L.append((x - dy / d * hw, y + dx / d * hw)); R.append((x + dy / d * hw, y - dx / d * hw))
    return L + R[::-1], c

# ---------------- obi sash behind her: big loop from the waist up over the back shoulder ----------------
sash_b = sp.layer()
poly, c = ribbon([(15 + X, 31), (-2 + X, 34), (-2 + X, 20), (-2 + X, 10), (7 + X, 9)], 5, 4)
sash_b.poly('p', poly)
sash_b.line('P', [(13 + X, 33), (5 + X, 33), (0 + X, 29), (-3 + X, 21)], width=1)   # shaded lower/outer edge
sash_b.px('P', (X - 1, 14), (X - 2, 15), (X - 1, 16), (X - 2, 24), (X - 1, 25), (X - 2, 26), (X + 5, 31), (X + 6, 32), (X + 4, 32))

# ---------------- long hair falling down her back ----------------
back_hair = sp.layer().poly('h', P([(9, 10), (15, 12), (14, 30), (11, 34), (8, 30), (7, 20)]))
back_hair.poly('H', P([(9, 12), (11, 12), (10, 31), (8, 29), (8, 20)])).v('H', 13, 18 , 28)

# ---------------- back arm ----------------
back_arm = sp.layer().poly('s', P([(13, 21), (17, 21), (14, 32), (11, 31)])).v('S', 12, 25, 31).v('S', 13, 22, 25)
back_arm.ell('s', *P([(10, 30)]) [0], *P([(14, 34)])[0]).px('S', (X + 11, 33), (X + 12, 33))

# ---------------- legs: long, bare thighs, dark stockings, high geta ----------------
leg_b = sp.layer().poly('s', P([(15, 33), (20, 33), (18, 46), (14, 46)])).v('S', 15, 35, 38)
leg_b.poly('R', P([(14, 39), (19, 39), (18, 46), (14, 46)])).v('H', X + 15, 40, 46)
leg_f = sp.layer().poly('s', P([(20, 33), (25, 33), (26, 46), (22, 46)])).v('S', X + 21, 35, 38)
leg_f.poly('R', P([(21, 39), (26, 39), (26, 46), (22, 46)])).v('H', X + 22, 40, 46)
geta_b = sp.layer().poly('r', P([(12, 46), (19, 46), (19, 48), (12, 48)])).rect('R', *P([(13, 49)])[0], *P([(14, 50)])[0])
geta_b.rect('R', *P([(17, 49)])[0], *P([(18, 50)])[0])
geta_f = sp.layer().poly('r', P([(21, 46), (28, 46), (28, 48), (21, 48)])).rect('R', *P([(22, 49)])[0], *P([(23, 50)])[0])
geta_f.rect('R', *P([(26, 49)])[0], *P([(27, 50)])[0])

# ---------------- torso: chest wrap, bare midriff, short dark skirt ----------------
torso = sp.layer()
torso.rect('s', *P([(17, 16)])[0], *P([(22, 21)])[0]).v('S', X + 17, 16, 21).h('S', X + 18, X + 21, 17)   # neck
torso.poly('s', P([(14, 20), (25, 20), (26, 24), (24, 30), (25, 34), (15, 34), (16, 30), (14, 24)]))
torso.poly('S', P([(14, 21), (16, 21), (16, 26), (17, 30), (16, 30), (15, 25)]))
torso.poly('r', P([(14, 22), (26, 22), (26, 26), (14, 26)])).h('R', X + 14, X + 26, 26).v('R', X + 14, 22, 26)  # chest wrap
torso.poly('r', P([(15, 31), (25, 31), (27, 37), (13, 37)]))                         # short skirt
torso.poly('R', P([(13, 37), (17, 31), (19, 31), (16, 37)])).h('R', X + 13, X + 27, 37)
torso.h('p', X + 15, X + 25, 30).h('P', X + 15, X + 25, 31)                        # sash tied at the waist
torso.px('S', (X + 20, 28), (X + 20, 29))                                          # navel line

# ---------------- hair tied up high: two big loops on top (behind the head), gold tie + pins ----------------
loops = sp.layer()
loops.poly('h', P([(17, 7), (11, 0), (6, 0), (4, 4), (9, 9)])).poly('h', P([(17, 7), (24, 0), (30, 0), (31, 4), (25, 9)]))
loops.poly('H', P([(5, 3), (9, 2), (13, 7), (9, 8)])).poly('H', P([(26, 6), (30, 3), (30, 4), (25, 8)]))
loops.px('l', (X + 25, 2), (X + 26, 2), (X + 27, 2))
tie = sp.layer().rect('y', *P([(15, 2)])[0], *P([(19, 6)])[0])

# ---------------- head ----------------
head = sp.layer()
head.ell('h', *P([(9, 5)])[0], *P([(29, 21)])[0])
head.poly('s', P([(14, 9), (28, 9), (29, 12), (28, 16), (25, 19), (17, 19), (14, 15)]))   # face
head.poly('h', P([(13, 7), (29, 7), (29, 10), (26, 9), (22, 10), (19, 9), (15, 11)]))     # fringe
head.poly('h', P([(12, 9), (16, 9), (15, 21), (12, 21)]))                          # far side lock
head.poly('H', P([(9, 11), (12, 9), (13, 19), (10, 18)]))                          # back of the head in shade
head.px('H', (X + 22, 9), (X + 23, 8), (X + 18, 8), (X + 19, 9))                   # fringe strand lines
head.px('l', (X + 24, 7), (X + 25, 7), (X + 26, 8))                                 # shine
head.px('s', (X + 15, 13), (X + 15, 14)).px('S', (X + 16, 14))                     # ear
head.h('o', X + 17, X + 19, 11).h('o', X + 23, X + 26, 11)                         # lash lines
head.px('e', (X + 17, 12), (X + 18, 12)).px('g', (X + 19, 12), (X + 18, 13), (X + 19, 13)).px('o', (X + 19, 12))
head.px('e', (X + 23, 12), (X + 23, 13)).px('g', (X + 24, 12), (X + 26, 12), (X + 24, 13), (X + 25, 13), (X + 26, 13))
head.px('o', (X + 25, 12))
head.px('P', (X + 26, 15), (X + 25, 16), (X + 27, 16), (X + 26, 17))               # flower mark on the cheek
head.px('r', (X + 22, 17), (X + 23, 17))                                           # red lips

# ---------------- front arm: hand on the hip, elbow out ----------------
front = sp.layer()
front.poly('s', P([(24, 20), (28, 21), (31, 27), (28, 28), (26, 24)])).v('S', X + 27, 25, 27)
front.poly('s', P([(28, 25), (31, 27), (28, 32), (25, 31)])).px('S', (X + 26, 31), (X + 27, 31))

# ---------------- front sash: sweeping down and out in front of her ----------------
sash_f = sp.layer()
poly, c = ribbon([(25 + X, 34), (34 + X, 33), (36 + X, 39), (37 + X, 44), (34 + X, 48)], 5, 4)
sash_f.poly('p', poly)
sash_f.line('P', [(27 + X, 36), (33 + X, 36), (35 + X, 40), (35 + X, 44)], width=1)
sash_f.px('P', (X + 36, 37), (X + 35, 38), (X + 37, 38), (X + 34, 45), (X + 35, 44), (X + 35, 46))

for L in (sash_b, loops, tie, back_hair, back_arm, leg_b, leg_f, geta_b, geta_f, torso, head, front, sash_f):
    sp.add(L)
sp.layers.remove((tie, 'o', (), True)); sp.layers.insert(sp.layers.index((head, 'o', (), True)) + 1, (tie, 'o', (), True))
sp.save()
