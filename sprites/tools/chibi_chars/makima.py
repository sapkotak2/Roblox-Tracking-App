"""Makima (Chainsaw Man) - chibi redraw (see tools/chibi.py for the style guide).
Checklist: refs/redraw/makima/NOTES.md (coral hair with blunt bangs + long straight side locks + thin low braid,
golden ringed half-lidded eyes, faint smile, cream shirt, thin black tie, high-waisted charcoal trousers, brown shoes,
hands clasped behind her back)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(42, 20, 26),                                   # outline
    h=(228, 114, 94), H=(168, 62, 58), l=(248, 164, 138),  # coral hair (+ shine)
    s=(252, 228, 212), S=(220, 180, 162),             # skin
    e=(252, 250, 244), y=(248, 200, 64), Y=(214, 118, 40),  # eye white, golden iris, orange ring
    w=(242, 236, 206), W=(194, 186, 150),             # cream shirt
    t=(54, 58, 62), T=(32, 34, 40),                   # charcoal trousers / black tie
    b=(132, 74, 42), B=(84, 44, 26),                  # brown shoes
)
sp = Sprite('makima', W=40, H=52, palette=PAL)

# ---------------- thin low braid hanging down her back ----------------
braid = sp.layer().poly('h', [(11, 15), (14, 15), (12, 26), (10, 36), (7, 36), (9, 24)])
for y in range(17, 33, 3):                                                    # braid segments
    cx = round(12.5 - (y - 15) * 4 / 19)
    braid.px('H', (cx - 1, y), (cx, y + 1))
braid.h('T', 7, 10, 35).h('T', 7, 10, 36)                                     # hair tie
braid.poly('h', [(7, 37), (10, 37), (11, 39), (8, 41), (6, 39)])               # small flared tip

# ---------------- hands clasped behind her back (peek out at the small of the back) ----------------

# ---------------- legs: long, high-waisted charcoal trousers, brown shoes ----------------
leg_b = sp.layer().poly('t', [(14, 32), (20, 32), (18, 47), (13, 47)]).v('T', 14, 34, 46).v('T', 15, 39, 46)
leg_f = sp.layer().poly('t', [(20, 32), (26, 32), (27, 47), (22, 47)]).v('T', 22, 36, 46)
shoe_b = sp.layer().poly('b', [(12, 46), (18, 46), (19, 50), (10, 50)]).h('B', 10, 19, 50).px('B', (12, 47))
shoe_f = sp.layer().poly('b', [(21, 46), (27, 46), (30, 50), (21, 50)]).h('B', 21, 30, 50).px('l', (27, 47), (28, 48))

# ---------------- torso: neck, cream shirt to a slim waist, black tie, very high waistband ----------------
torso = sp.layer()
torso.rect('s', 17, 16, 23, 21).v('S', 17, 16, 21).h('S', 18, 22, 17)                    # neck
torso.poly('w', [(13, 20), (17, 20), (20, 23), (23, 20), (26, 20), (27, 23), (25, 30), (15, 30), (13, 23)])
torso.poly('W', [(13, 21), (16, 21), (16, 30), (15, 30), (14, 24)])                       # back side in shade
torso.poly('w', [(16, 20), (20, 22), (18, 24), (15, 21)]).poly('w', [(24, 20), (20, 22), (22, 24), (25, 21)])  # collar
torso.px('W', (17, 22), (18, 23), (23, 22), (22, 23))
torso.poly('T', [(20, 22), (21, 22), (21, 29), (20, 30)])                       # thin black tie
torso.poly('t', [(14, 29), (26, 29), (26, 34), (14, 34)]).h('T', 14, 26, 29)             # high waistband
torso.v('T', 15, 30, 34)

# ---------------- front arm: straight down, angled back toward the hidden hands ----------------
front = sp.layer().poly('w', [(23, 20), (27, 21), (28, 28), (25, 32), (22, 32), (24, 27)]).v('W', 24, 23, 27).h('W', 22, 25, 31)  # arm bending back

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 9, 0, 29, 17)
head.poly('s', [(14, 6), (28, 6), (29, 10), (28, 14), (24, 18), (19, 18), (15, 15)])      # slim face, pointed chin
head.poly('h', [(12, 3), (29, 3), (30, 8), (27, 8), (26, 7), (23, 8), (20, 7), (17, 8), (14, 7)])   # blunt bangs
head.poly('h', [(12, 6), (16, 6), (16, 15), (15, 22), (12, 22)])                          # far side lock (to the chest)
head.poly('h', [(28, 7), (31, 7), (31, 24), (28, 24), (28, 16)])                          # near side lock (to the chest)
head.poly('H', [(9, 7), (12, 4), (13, 16), (10, 15)])                                     # back of the head in shade
head.v('H', 14, 10, 21).v('H', 29, 12, 23).px('H', (20, 6), (21, 6), (26, 6))           # strand lines
head.px('l', (18, 1), (19, 1), (20, 1), (21, 2))                                          # shine
# calm half-lidded RINGED eyes: lash line, golden iris with orange ring and dark centre
head.h('o', 17, 19, 9).h('o', 23, 26, 9)
head.px('e', (17, 10), (17, 11)).px('y', (18, 10), (19, 10)).px('Y', (18, 11), (19, 11)).px('o', (19, 10))
head.px('e', (23, 10), (23, 11)).px('Y', (24, 10), (26, 10), (24, 11), (25, 11), (26, 11)).px('o', (25, 10))
head.px('y', (24, 10), (26, 10))
head.px('S', (27, 13)).h('S', 23, 24, 15)                                                 # nose, faint closed smile

for L in (braid, leg_b, leg_f, shoe_b, shoe_f, torso, front, head):
    sp.add(L)
sp.save()
