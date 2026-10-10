"""Asta (Black Clover) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(22, 18, 22),                                   # outline
    a=(232, 232, 224), A=(164, 166, 168),             # ash-white hair
    s=(248, 206, 166), S=(214, 150, 112),             # skin
    e=(255, 255, 250), g=(40, 168, 76), k=(30, 26, 32), m=(130, 44, 40),   # eye white, green iris, dark, mouth
    b=(52, 50, 62), B=(32, 30, 40),                   # black cape
    d=(112, 114, 128), D=(80, 82, 96),                # dark grey outfit (d also = sword edge)
    r=(170, 72, 44), R=(112, 44, 30),                 # red-brown boots / belt
    y=(236, 190, 60),                                 # gold Black Bulls emblem
)
sp = Sprite('asta', W=48, H=52, palette=PAL)


# ---------------- cape, back part (hangs behind, to the left) ----------------
cape_b = sp.layer()
cape_b.poly('b', [(10, 19), (19, 19), (17, 34), (5, 35), (6, 26)])
cape_b.poly('B', [(9, 21), (11, 21), (8, 35), (5, 35), (6, 27)])
cape_b.poly('B', [(5, 35), (8, 32), (10, 35), (12, 32), (14, 35)])            # ragged hem as two clean notches
cape_b.rect('y', 9, 26, 10, 27)                                                # gold emblem

# ---------------- legs ----------------
leg_b = sp.layer()   # back leg angled back
leg_b.poly('d', [(12, 33), (19, 33), (16, 39), (13, 44), (7, 44), (10, 38)])
leg_b.poly('D', [(8, 43), (11, 37), (13, 35), (13, 37), (11, 43)])
leg_b.poly('r', [(7, 42), (13, 42), (13, 47), (15, 50), (4, 50), (6, 47)]).v('R', 8, 43, 48).h('R', 4, 15, 50)
leg_f = sp.layer()   # front leg bent forward
leg_f.poly('d', [(21, 33), (27, 33), (31, 38), (31, 44), (25, 44), (24, 39)]).v('D', 25, 39, 43).v('D', 26, 41, 43)
leg_f.poly('r', [(25, 42), (31, 42), (32, 47), (35, 48), (35, 50), (25, 50)]).v('R', 26, 43, 48).h('R', 25, 35, 50)

# ---------------- torso: dark grey top, belt ----------------
torso = sp.layer()
torso.poly('d', [(13, 21), (26, 21), (27, 25), (25, 33), (14, 33), (12, 25)])
torso.poly('D', [(13, 22), (16, 22), (16, 33), (14, 33), (13, 26)])
torso.h('R', 13, 26, 30).h('r', 13, 26, 31).rect('y', 20, 30, 21, 31)           # belt + buckle
torso.rect('s', 17, 18, 21, 22).h('S', 17, 21, 19).v('S', 17, 18, 22)             # neck
torso.v('D', 22, 24, 30)                                                          # fold line

# ---------------- hood bunched around the neck ----------------
hood = sp.layer()
hood.poly('b', [(10, 19), (16, 19), (18, 22), (25, 22), (27, 21), (26, 24), (17, 25), (11, 23)])
hood.h('B', 12, 24, 24).px('B', (11, 22), (12, 23))

# ---------------- head ----------------
head = sp.layer()
head.ell('a', 9, 3, 30, 19)
# sharp spikes up and back (blunt 2-px tips so each spike keeps its colour)
for t1, t2, b1, b2 in (((3, 1), (5, 0), (9, 8), (15, 5)), ((11, 1), (13, 1), (13, 5), (20, 4)),
                       ((20, 0), (22, 0), (18, 4), (26, 4)), ((29, 1), (30, 2), (24, 5), (30, 8)),
                       ((35, 5), (35, 7), (28, 6), (30, 11)), ((1, 7), (1, 9), (11, 5), (10, 12)),
                       ((3, 15), (4, 17), (10, 12), (12, 18))):
    head.poly('a', [t1, t2, b2, b1])
head.poly('s', [(14, 10), (29, 10), (30, 13), (29, 16), (26, 19), (17, 19), (14, 16)])   # face
head.poly('a', [(12, 9), (15, 9), (14, 17), (12, 15)])                            # side lock
# black headband just above the brows, knot tails fluttering behind
head.poly('b', [(10, 8), (31, 8), (31, 9), (10, 9)])
head.poly('b', [(11, 8), (2, 9), (3, 12), (11, 10)])
head.v('A', 11, 4, 7).v('A', 18, 3, 6).v('A', 25, 3, 6).h('A', 6, 11, 15)
head.v('S', 15, 10, 15)                                                           # face shade under the hair
# eyes: determined, green
head.h('k', 16, 18, 11).h('k', 25, 28, 11)                                       # angled brows
head.px('k', (20, 12), (23, 12))
head.h('o', 18, 20, 12).px('e', (18, 13), (18, 14)).rect('g', 19, 13, 20, 14).px('k', (20, 13))
head.h('o', 24, 27, 12).px('e', (23, 13), (24, 13), (27, 13), (23, 14), (24, 14), (27, 14))
head.rect('g', 25, 13, 26, 14).px('k', (26, 13))
head.px('S', (28, 15))                                                            # nose
head.h('m', 23, 26, 17).px('e', (24, 17), (25, 17))                               # shouting grin

# ---------------- demon-slayer greatsword: black, rough, held low and forward ----------------
sword = sp.layer()
sword.poly('b', [(30, 32), (34, 28), (38, 32), (39, 31), (40, 34), (46, 40), (45, 44), (43, 43), (41, 46), (38, 44)])
sword.line('A', [(35, 30), (37, 32)]).line('A', [(40, 35), (44, 39)])               # rough light edge (notched)
sword.line('B', [(33, 33), (39, 39)])                                             # crack
sword.poly('k', [(29, 31), (33, 27), (35, 29), (31, 33)])                         # dark guard band

# ---------------- front arm: grey sleeve, bare forearm, fist on the hilt ----------------
arm_f = sp.layer()
arm_f.poly('d', [(23, 21), (28, 21), (31, 26), (27, 28), (24, 25)]).v('D', 24, 22, 25).px('D', (25, 26), (26, 27))
arm_f.poly('s', [(27, 26), (30, 25), (31, 28), (28, 29)])
fist = sp.layer().ell('s', 28, 26, 33, 31).px('S', (29, 30), (30, 31), (28, 29)).px('S', (31, 31))

for L in (cape_b, leg_b, leg_f, torso, hood, head, sword, arm_f, fist):
    sp.add(L)
sp.save()
