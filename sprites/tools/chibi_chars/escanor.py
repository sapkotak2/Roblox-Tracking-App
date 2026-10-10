"""Escanor 'The One' (Seven Deadly Sins) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(42, 22, 14),                                   # outline
    h=(252, 242, 212), H=(180, 134, 64),              # ivory-blond hair (shade also = mustache)
    s=(240, 182, 126), S=(198, 128, 84),              # skin
    e=(255, 252, 244), k=(40, 22, 16), m=(140, 52, 40),   # eye white, dark, mouth
    g=(84, 132, 66), G=(52, 88, 44),                  # green trousers
    y=(252, 196, 58), Y=(222, 118, 28),               # Rhitta: gold / orange
    b=(146, 86, 46),                                  # belt, boots, axe handle
)
sp = Sprite('escanor', W=48, H=52, palette=PAL)

# ---------------- Rhitta's handle: from behind his back, over the near shoulder ----------------
handle = sp.layer().poly('b', [(30, 26), (36, 1), (39, 1), (33, 26)])

# ---------------- back arm: huge, hanging at the side, fist clenched ----------------
arm_b = sp.layer()
arm_b.poly('s', [(3, 20), (10, 20), (10, 31), (7, 35), (2, 34), (1, 26)])
arm_b.ell('s', 0, 31, 8, 38)
arm_b.v('S', 2, 23, 32).v('S', 3, 26, 31).h('S', 1, 7, 37)

# ---------------- legs: green trousers, brown boots ----------------
leg_b = sp.layer()
leg_b.poly('g', [(9, 33), (19, 33), (17, 40), (15, 46), (7, 46), (8, 39)]).v('G', 9, 37, 45).v('G', 10, 39, 45)
leg_b.poly('b', [(7, 45), (15, 45), (16, 48), (17, 50), (4, 50), (6, 47)])
leg_f = sp.layer()
leg_f.poly('g', [(20, 33), (29, 33), (32, 39), (32, 46), (24, 46), (23, 40)]).v('G', 24, 40, 45).v('G', 25, 42, 45)
leg_f.poly('b', [(24, 45), (32, 45), (33, 48), (36, 49), (36, 50), (24, 50)])

# ---------------- torso: massive V, shirtless ----------------
torso = sp.layer()
torso.poly('s', [(7, 19), (32, 19), (36, 23), (34, 27), (30, 34), (10, 34), (6, 27), (4, 23)])
torso.poly('S', [(5, 22), (8, 21), (10, 28), (11, 34), (10, 34), (6, 27)])         # back side in shade
torso.h('S', 12, 18, 27).h('S', 23, 31, 27).px('S', (19, 26), (22, 26), (32, 26))  # pec lines
torso.v('S', 20, 22, 26).h('S', 16, 19, 30).h('S', 22, 27, 30)                    # centre + ab line
torso.v('S', 11, 21, 25).px('S', (12, 26))                                        # deltoid line
torso.rect('b', 9, 32, 30, 34)                                                    # belt
torso.rect('s', 16, 15, 25, 20).v('S', 16, 15, 20).h('S', 16, 24, 17)             # thick neck

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 9, 1, 30, 14).ell('h', 24, 1, 32, 9)
# hair swept up and back: broad locks pointing up-left
for t1, t2, b1, b2 in (((3, 3), (4, 1), (10, 10), (15, 3)), ((12, 0), (14, -1), (14, 4), (22, 2)),
                       ((21, 0), (23, -1), (20, 3), (29, 4)), ((3, 10), (3, 12), (10, 8), (11, 14))):
    head.poly('h', [t1, t2, b2, b1])
head.poly('s', [(16, 8), (29, 8), (31, 11), (30, 15), (27, 18), (18, 18), (15, 14)])   # face, strong jaw
head.h('H', 7, 13, 6).h('H', 4, 9, 11).h('H', 15, 21, 3).h('H', 22, 27, 5)          # strands swept back
head.v('S', 16, 10, 14).h('S', 18, 20, 17)                                         # face shade (back side)
# confident narrow eyes, heavy brow
head.h('k', 18, 21, 9).h('k', 24, 28, 9).px('k', (21, 10), (24, 10))               # heavy brows angled in
head.h('o', 19, 21, 10).px('e', (19, 11), (19, 12)).rect('k', 20, 11, 21, 12)
head.h('o', 25, 28, 10).px('e', (25, 11), (26, 11), (25, 12), (26, 12)).rect('k', 27, 11, 28, 12)
head.px('e', (21, 11), (28, 11))                                                  # catch-lights
head.px('S', (30, 12), (30, 13))                                                  # nose
head.h('H', 24, 29, 14).px('H', (23, 15), (30, 15))                               # thin mustache
head.h('m', 25, 28, 16)                                                           # smirk

# ---------------- front arm: elbow out, hand on the handle at the shoulder ----------------
arm_f = sp.layer()
arm_f.poly('s', [(29, 19), (35, 19), (41, 25), (38, 29), (31, 24)]).v('S', 31, 21, 23).h('S', 33, 37, 25)
fore_f = sp.layer().poly('s', [(37, 29), (41, 25), (37, 18), (33, 18), (34, 22)]).v('S', 35, 21, 24)
hand = sp.layer().ell('s', 31, 15, 37, 21).h('S', 32, 35, 21).v('S', 31, 18, 20)

# ---------------- Rhitta's head: sun-disc blade above the shoulder ----------------
axe = sp.layer()
axe.poly('y', [(37, 2), (42, 0), (47, 3), (47, 14), (44, 18), (36, 13)])             # big crescent blade
axe.ell('Y', 38, 5, 45, 13).ell('y', 40, 7, 43, 11)                                # sun ring
axe.v('e', 46, 4, 13)                                                             # sharp edge shine

for L in (handle, arm_b, leg_b, leg_f, torso, head, arm_f, fore_f, axe, hand):
    sp.add(L)
sp.save()
