"""Erza Scarlet (Fairy Tail) - chibi redraw (see tools/chibi.py for the style guide).
Long scarlet hair down the back, Heart Kreuz armour (flat silver + blue cross), blue skirt, black boots, sword ready."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(44, 14, 26),                                   # outline
    h=(214, 36, 48), H=(140, 16, 36), l=(255, 120, 110),  # hair base / shade / shine
    s=(252, 214, 180), S=(226, 156, 124),             # skin
    e=(255, 255, 255), k=(52, 22, 26), b=(150, 72, 34), m=(150, 46, 56),  # eye white, lash/pupil, iris, mouth
    a=(214, 220, 232), A=(132, 140, 162),             # silver armour
    c=(44, 100, 210), C=(22, 54, 136),                # blue cross / skirt
    n=(52, 50, 64), N=(96, 98, 120),                  # boots
    g=(244, 186, 52),                                 # gold hilt
)
sp = Sprite('erza', W=48, H=52, palette=PAL)
L = sp.layer

# ---------------- long hair down the back ----------------
back_hair = L()
back_hair.poly('h', [(12, 5), (17, 12), (17, 24), (15, 32), (11, 37), (7, 36), (6, 30), (6, 18), (8, 10)])
back_hair.poly('H', [(7, 18), (9, 18), (9, 35), (8, 36), (7, 32)])               # back side in shade
back_hair.v('H', 13, 22, 33).px('H', (12, 34))                                     # strand line

# ---------------- back arm (beside the body, gauntlet) ----------------
back_arm = L()
back_arm.poly('s', [(12, 24), (16, 24), (16, 29), (12, 29)]).v('S', 13, 25, 29)
back_arm.poly('A', [(11, 29), (16, 29), (16, 35), (11, 35)]).v('a', 15, 30, 34).h('a', 12, 15, 30)   # gauntlet: steel, lit edge

# ---------------- legs (bare thighs, black boots), clear gap between ----------------
leg_b = L()
leg_b.poly('s', [(16, 36), (22, 36), (20, 42), (15, 42)]).v('S', 16, 37, 42)
leg_b.poly('n', [(14, 42), (20, 42), (19, 47), (14, 47)])
leg_b.poly('n', [(10, 47), (19, 47), (19, 50), (10, 50)])
leg_b.v('N', 18, 43, 48).h('N', 11, 13, 48)
leg_f = L()
leg_f.poly('s', [(23, 36), (28, 36), (30, 42), (25, 42)]).v('S', 25, 38, 42).v('S', 24, 37, 38)
leg_f.poly('n', [(25, 42), (30, 42), (31, 47), (26, 47)])
leg_f.poly('n', [(26, 47), (34, 47), (35, 50), (26, 50)])
leg_f.v('N', 30, 43, 47).h('N', 31, 33, 48)

# ---------------- skirt ----------------
skirt = L()
skirt.poly('c', [(17, 30), (28, 30), (32, 37), (13, 37)])
skirt.poly('C', [(17, 30), (19, 30), (17, 37), (13, 37)])                         # back side shade
skirt.v('C', 22, 33, 37).v('C', 27, 33, 37)                                        # pleat lines

# ---------------- torso: breastplate ----------------
torso = L()
torso.rect('s', 20, 17, 24, 22).v('S', 20, 17, 22).v('S', 21, 19, 22)             # neck
torso.poly('a', [(17, 21), (28, 21), (29, 25), (27, 31), (18, 31), (17, 25)])
torso.poly('A', [(17, 21), (20, 21), (20, 31), (18, 31), (17, 25)])                # back side shade
torso.h('A', 21, 28, 27)                                                           # under-bust line
torso.v('c', 25, 22, 26).h('c', 23, 27, 24)                                        # blue cross

# ---------------- back pauldron ----------------
pauld_b = L().ell('a', 11, 20, 19, 26).poly('A', [(11, 23), (19, 24), (18, 26), (12, 26)])

# ---------------- head ----------------
head = L()
head.ell('h', 10, 0, 33, 18)
head.poly('s', [(16, 7), (30, 7), (31, 11), (31, 13), (29, 16), (25, 19), (21, 19), (18, 16), (16, 12)])  # face
# straight parted bangs, cut above the eyes
for pts in ([(14, 2), (22, 2), (20, 8), (17, 10)], [(20, 2), (27, 2), (25, 8), (22, 7)],
            [(25, 2), (32, 3), (32, 8), (29, 9), (27, 7)]):
    head.poly('h', pts)
head.poly('h', [(11, 5), (18, 8), (18, 20), (15, 23), (12, 18)])                  # side lock over the ear
head.v('H', 14, 10, 21).v('H', 16, 13, 20)
head.px('H', (20, 6), (21, 5), (26, 5), (25, 6), (13, 4), (12, 5))
head.px('l', (22, 1), (23, 1), (26, 2), (27, 2))
# brows, eyes (far small, near big), nose, mouth
head.h('k', 20, 21, 9).h('k', 25, 28, 9)
head.h('k', 19, 22, 11).px('e', (20, 12), (20, 13), (20, 14)).px('b', (21, 12), (21, 13), (21, 14))
head.h('k', 24, 28, 11).px('k', (29, 10))
head.px('e', (24, 12), (24, 13), (24, 14), (27, 12), (27, 13), (27, 14))
head.px('b', (25, 12), (25, 13), (26, 13), (25, 14), (26, 14)).px('k', (26, 12))
head.px('S', (30, 14), (30, 15))
head.h('m', 26, 27, 16)
head.px('S', (21, 17), (22, 18))

# ---------------- sword (vertical guard stance, held at the waist) ----------------
sword = L()
sword.poly('a', [(35, 25), (39, 25), (39, 7), (37, 4), (35, 7)])                   # blade
sword.v('A', 36, 7, 24).v('e', 38, 7, 24)
sword.rect('g', 32, 25, 41, 26)                                                     # crossguard
sword.rect('g', 35, 27, 39, 35)                                                     # grip / pommel

# ---------------- front pauldron + front arm (fist on the grip) ----------------
front = L()
front.poly('s', [(28, 24), (32, 24), (32, 30), (28, 30)]).v('S', 28, 25, 30)
front.rect('A', 28, 29, 35, 33).h('a', 29, 35, 30)                                 # gauntlet forearm
front.ell('a', 26, 20, 34, 26).poly('A', [(26, 23), (34, 24), (33, 26), (27, 26)])  # front pauldron
fist = L().rect('A', 34, 27, 39, 32).h('a', 35, 38, 28).v('a', 38, 28, 30)        # gauntlet fist on the grip

for lay in (back_hair, back_arm, leg_b, leg_f, skirt, torso, pauld_b, head, sword, front):
    sp.add(lay)
sp.add(fist)
sp.save()
