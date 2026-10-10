"""Asuna (Sword Art Online) - chibi redraw (see tools/chibi.py for the style guide).
Long chestnut hair with a side braid, Knights of the Blood white uniform with red trim and cross, red skirt,
white thigh-high boots, slim rapier thrust forward."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(52, 20, 22),                                    # outline
    h=(220, 114, 48), H=(144, 60, 30), l=(255, 182, 116),  # hair base / shade / shine
    s=(252, 216, 184), S=(228, 160, 128),              # skin
    e=(255, 255, 255), k=(56, 26, 24), z=(176, 132, 46), m=(160, 56, 56),  # eye white, lash, hazel iris, mouth
    w=(242, 242, 246), W=(176, 178, 198),              # white uniform / cool shade
    r=(214, 32, 44), R=(132, 14, 28),                  # red trim / skirt
)
sp = Sprite('asuna', W=50, H=52, palette=PAL)
L = sp.layer

# ---------------- long hair down the back ----------------
back_hair = L()
back_hair.poly('h', [(12, 5), (18, 12), (18, 24), (16, 33), (12, 38), (7, 37), (6, 30), (6, 18), (8, 10)])
back_hair.poly('H', [(7, 18), (9, 18), (9, 36), (8, 36), (7, 32)])
back_hair.v('H', 14, 22, 34).v('H', 12, 26, 33)

# ---------------- back arm (hanging behind, white sleeve, red cuff) ----------------
back_arm = L()
back_arm.poly('w', [(12, 23), (17, 23), (17, 31), (12, 31)]).v('W', 13, 24, 31).v('W', 14, 24, 31)
back_arm.h('r', 12, 17, 31).h('R', 12, 17, 32)
back_arm.rect('s', 12, 32, 16, 35)
back_arm.px('S', (13, 34), (14, 34))

# ---------------- legs: white thigh-high boots with red tops ----------------
leg_b = L()
leg_b.poly('s', [(16, 36), (22, 36), (21, 39), (16, 39)])
leg_b.poly('w', [(15, 39), (21, 39), (19, 47), (15, 47)]).h('r', 15, 21, 39).h('r', 15, 21, 40)
leg_b.poly('w', [(11, 47), (19, 47), (19, 50), (11, 50)])
leg_b.v('W', 16, 41, 47).v('W', 17, 41, 47).h('W', 12, 18, 49).h('r', 12, 18, 50)
leg_f = L()
leg_f.poly('s', [(23, 36), (28, 36), (29, 39), (24, 39)])
leg_f.poly('w', [(24, 39), (29, 39), (30, 47), (26, 47)]).h('r', 24, 29, 39).h('r', 24, 29, 40)
leg_f.poly('w', [(26, 47), (34, 47), (35, 50), (26, 50)])
leg_f.v('W', 25, 41, 47).v('W', 26, 43, 47).h('W', 27, 34, 49).h('r', 27, 34, 50)

# ---------------- skirt: red with a white hem ----------------
skirt = L()
skirt.poly('r', [(17, 30), (28, 30), (32, 37), (13, 37)])
skirt.poly('R', [(17, 30), (19, 30), (17, 37), (13, 37)])
skirt.v('R', 22, 33, 36).v('R', 27, 33, 36)
skirt.h('w', 14, 31, 36)

# ---------------- torso: white top, red collar, red cross ----------------
torso = L()
torso.rect('s', 20, 17, 24, 22).v('S', 20, 17, 22).v('S', 21, 19, 22)              # neck
torso.poly('w', [(17, 21), (28, 21), (29, 25), (27, 31), (18, 31), (17, 25)])
torso.poly('W', [(17, 21), (20, 21), (20, 31), (18, 31), (17, 25)])                 # back side shade
torso.h('r', 18, 27, 21).h('r', 21, 24, 22)                                         # red collar
torso.v('r', 23, 24, 28).h('r', 22, 24, 25)                                         # red cross
torso.h('R', 18, 27, 30)                                                            # belt

# ---------------- head ----------------
head = L()
head.ell('h', 10, 0, 33, 18)
head.poly('s', [(16, 7), (30, 7), (31, 11), (31, 13), (29, 16), (25, 19), (21, 19), (18, 16), (16, 12)])  # face
# side-swept bangs, cut above the eyes, one lock at the front of the face
for pts in ([(14, 2), (22, 2), (19, 9), (17, 10)], [(19, 2), (28, 3), (24, 8), (21, 7)],
            [(25, 2), (32, 3), (33, 10), (31, 15), (30, 9), (27, 7)]):
    head.poly('h', pts)
head.poly('h', [(11, 5), (18, 8), (18, 22), (15, 24), (12, 18)])                  # side lock over the ear
head.v('H', 16, 9, 11)
head.px('H', (21, 3), (21, 4), (20, 5), (20, 6), (26, 3), (25, 4), (25, 5), (24, 6), (30, 5), (31, 6), (31, 7))
# braided side lock: slanted segment lines down the lock beside the face
for y in (12, 15, 18, 21):
    head.px('H', (13, y + 1), (14, y), (15, y), (16, y - 1))
head.px('l', (22, 1), (23, 1), (28, 2), (29, 2))
# brows, eyes, nose, mouth
head.h('k', 20, 21, 9).h('k', 25, 28, 9)
head.h('k', 19, 22, 11).px('e', (20, 12), (20, 13), (20, 14)).px('z', (21, 12), (21, 13), (21, 14))
head.h('k', 24, 28, 11).px('k', (29, 10))
head.px('e', (24, 12), (24, 13), (24, 14), (27, 12), (27, 13), (27, 14))
head.px('z', (25, 12), (25, 13), (26, 13), (25, 14), (26, 14)).px('k', (26, 12))
head.px('S', (30, 14))
head.h('m', 26, 27, 16)
head.px('S', (21, 17), (22, 18))

# ---------------- rapier (thin, thrust forward) ----------------
rapier = L()
rapier.poly('W', [(37, 22), (48, 22), (49, 23), (48, 24), (37, 24)])
rapier.h('e', 38, 47, 23)

# ---------------- front arm: straight out at shoulder height ----------------
front = L()
front.poly('w', [(25, 21), (32, 21), (33, 26), (26, 27), (25, 25)]).h('W', 26, 32, 26).h('W', 26, 32, 25)
front.rect('r', 32, 21, 34, 26)                                                    # red cuff
fist = L().rect('s', 34, 21, 38, 26).h('S', 34, 38, 25).h('S', 34, 38, 26)
guard = L().rect('W', 37, 20, 39, 27).v('e', 38, 21, 26)                           # cup guard

for lay in (back_hair, back_arm, leg_b, leg_f, skirt, torso, head, rapier, front, fist, guard):
    sp.add(lay)
sp.save()
