"""Erza Scarlet (Fairy Tail) - chibi redraw (see tools/chibi.py for the style guide).
Matched to refs/redraw/erza (Heart Kreuz full body + face close-up), checklist in refs/redraw/erza/NOTES.md:
sharp narrow dark eyes with heavy lashes, brows angled down, stern flat mouth, pointed chin; long straight scarlet hair
with a heavy lock over the far side of the face and a lock in front of the shoulder; silver Heart Kreuz armour with high
collar, gold cross, round grooved pauldrons, black elbow bands, faulds + brown belt; navy pleated skirt; black heeled
knee boots; broadsword with a pale blue blade held low and forward."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(40, 12, 24),                                   # outline
    h=(206, 30, 46), H=(124, 10, 32),                 # scarlet hair / shade (also the stern mouth line)
    s=(252, 220, 192), S=(224, 160, 132),             # skin
    e=(255, 255, 255), k=(30, 14, 20), b=(92, 38, 40),  # eye white, lash/pupil, very dark brown iris
    a=(220, 224, 234), A=(140, 146, 166),             # silver armour
    g=(240, 184, 40),                                 # gold cross
    u=(40, 62, 160), U=(22, 32, 96),                  # navy skirt
    n=(36, 34, 44), d=(128, 76, 40),                  # black boots / elbow bands, brown belt
    B=(196, 222, 246), G=(110, 140, 176),             # pale blue blade, blue-grey guard
)
sp = Sprite('erza', W=50, H=52, palette=PAL)
L = sp.layer

# ---------------- long straight hair down the back (past the waist) ----------------
back_hair = L()
back_hair.poly('h', [(12, 5), (18, 12), (18, 26), (16, 36), (13, 40), (9, 39), (8, 32), (8, 18), (9, 10)])
back_hair.poly('H', [(8, 20), (10, 20), (10, 38), (9, 38), (8, 32)])
back_hair.v('H', 13, 30, 38)
back_hair.poly('h', [(27, 10), (33, 10), (34, 22), (33, 31), (30, 33), (29, 24)]).v('H', 31, 22, 31)   # hair falling behind the near shoulder

# ---------------- back arm: pauldron, black elbow band, gauntlet ----------------
back_arm = L()
back_arm.rect('n', 11, 25, 15, 28)
back_arm.poly('A', [(10, 28), (15, 28), (15, 34), (10, 34)]).v('a', 14, 29, 33).h('a', 11, 14, 29)

# ---------------- legs: bare knees, black heeled knee boots, wide stance ----------------
leg_b = L()
leg_b.poly('s', [(15, 38), (21, 38), (19, 43), (14, 43)]).poly('S', [(15, 38), (17, 38), (16, 43), (14, 43)])
leg_b.poly('n', [(13, 42), (19, 42), (18, 47), (13, 47)])
leg_b.poly('n', [(9, 47), (18, 47), (18, 49), (9, 49)]).rect('n', 15, 49, 18, 50).rect('n', 9, 49, 11, 50)  # sole + heel
leg_b.v('A', 17, 43, 46)
leg_f = L()
leg_f.poly('s', [(24, 38), (30, 38), (31, 43), (26, 43)]).v('S', 26, 39, 43)
leg_f.poly('n', [(26, 42), (32, 42), (32, 47), (27, 47)])
leg_f.poly('n', [(26, 47), (35, 47), (36, 49), (26, 49)]).rect('n', 26, 49, 29, 50).rect('n', 33, 49, 36, 50)
leg_f.v('A', 31, 43, 46)

# ---------------- navy pleated skirt (flared, to mid-thigh) ----------------
skirt = L()
skirt.poly('u', [(17, 29), (28, 29), (33, 39), (12, 39)])
skirt.poly('U', [(17, 29), (19, 29), (17, 39), (12, 39)])
skirt.v('U', 22, 34, 39).v('U', 27, 34, 39).v('U', 31, 36, 39)

# ---------------- torso: breastplate with high collar, gold cross, brown belt, short faulds ----------------
torso = L()
torso.rect('s', 21, 18, 24, 21).v('S', 21, 18, 21)                                  # neck
torso.poly('a', [(17, 21), (28, 21), (29, 25), (27, 29), (18, 29), (17, 25)])
torso.poly('A', [(17, 21), (20, 21), (20, 29), (18, 29), (17, 25)])                 # back side shade
torso.h('A', 21, 27, 27)                                                            # plate line
torso.v('g', 24, 22, 28).h('g', 22, 26, 24).px('H', (25, 22))                       # gold cross, long bar, red heart mark
torso.h('d', 18, 28, 29)                                                            # brown belt
torso.poly('a', [(18, 30), (29, 30), (30, 33), (17, 33)])                           # faulds over the skirt
torso.v('A', 18, 30, 33).v('A', 19, 30, 33).v('d', 21, 30, 32).v('d', 26, 30, 32)
collar = L().rect('a', 20, 18, 25, 21).v('A', 20, 18, 21).v('A', 21, 18, 21)        # high neck guard

# ---------------- back pauldron (round, grooved) ----------------
pauld_b = L().poly('a', [(11, 21), (13, 19), (18, 19), (20, 21), (20, 26), (10, 26)]).h('A', 11, 19, 22).h('A', 10, 20, 25).h('A', 10, 20, 26).v('A', 11, 21, 26)

# ---------------- head ----------------
head = L()
head.ell('h', 10, 0, 33, 18)
head.poly('s', [(16, 7), (30, 7), (31, 11), (31, 13), (29, 16), (26, 19), (24, 20), (22, 19), (18, 16), (16, 12)])  # slim face, pointed chin
# heavy bangs parted near the middle; the far-side lock sweeps down the side of the face to the jaw
head.poly('h', [(13, 2), (23, 2), (23, 6), (20, 8), (19, 13), (18, 18), (16, 20), (14, 18)])
head.poly('h', [(21, 2), (29, 3), (28, 6), (24, 7)])
head.poly('h', [(26, 2), (32, 4), (33, 9), (32, 14), (30, 7)])
head.v('H', 16, 12, 19).v('H', 14, 9, 17).px('H', (22, 3), (22, 4), (21, 5), (27, 4), (26, 5), (31, 7), (31, 8))
# stern brows angled down toward the middle
head.px('k', (19, 8), (20, 8), (21, 9)).px('k', (24, 9), (25, 9), (26, 8), (27, 8), (28, 8))
# sharp eyes: heavy lash line with an outer flick, very dark iris, 2 rows tall
head.h('k', 20, 22, 11).px('e', (21, 12), (21, 13)).px('b', (22, 12), (22, 13))
head.h('k', 24, 28, 11).px('k', (29, 10))
head.px('e', (24, 12), (24, 13), (27, 12), (27, 13)).px('b', (25, 12), (25, 13), (26, 13)).px('k', (26, 12))
head.px('S', (30, 14), (30, 15))                                                    # nose
head.h('H', 25, 26, 17)                                                             # flat stern mouth
head.px('S', (22, 18), (23, 19))

# ---------------- sword: broadsword held low at the side, pale blue blade pointing down ----------------
sword = L().poly('B', [(37, 35), (41, 35), (41, 47), (39, 50), (37, 47)]).v('e', 39, 36, 47)
grip = L().rect('G', 36, 25, 39, 29)                                                 # grip + pommel above the fist
guard = L().rect('G', 34, 33, 44, 35)                                                # crossguard

# ---------------- front arm: black elbow band, steel gauntlet, fist on the grip; round pauldron ----------------
front = L()
front.rect('n', 27, 25, 31, 28)
front.poly('A', [(28, 28), (32, 27), (37, 29), (37, 33), (30, 32)]).h('a', 30, 35, 29)
fist = L().rect('A', 35, 28, 40, 33).h('a', 36, 39, 29).v('a', 39, 29, 31)
pauld_f = L().poly('a', [(25, 21), (27, 19), (32, 19), (34, 21), (35, 26), (25, 26)]).h('A', 26, 34, 22).h('A', 25, 35, 25).h('A', 25, 35, 26)

for lay in (back_hair, back_arm, leg_b, leg_f, skirt, torso, collar, pauld_b, head, sword, grip, front, guard, fist, pauld_f):
    sp.add(lay)
sp.save()
