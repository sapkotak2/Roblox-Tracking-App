"""Yuta Okkotsu (Jujutsu Kaisen 0) - chibi redraw (see tools/chibi.py for the style guide; checklist in
refs/redraw/okkotsu/NOTES.md, built from the JJK0 character sheet).
Smooth dark teal-black parted hair with locks over the forehead, big round empty eyes with heavy dark circles,
white hip-length Jujutsu High jacket (tall collar, gold buttons, off-centre closure), BLACK slim trousers, white
sneakers, sword bag slung on the back with a strap across the chest, katana drawn in the front hand."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(20, 24, 32),                                    # outline
    h=(36, 54, 62), H=(16, 26, 32),                    # hair (dark teal-black) / strands
    s=(248, 220, 194), S=(210, 170, 148), m=(170, 108, 100),  # skin / shade / mouth
    e=(252, 252, 255), k=(26, 30, 40), u=(150, 118, 132),     # eye white / pupil / dark circles
    w=(244, 246, 252), W=(180, 190, 210), g=(222, 178, 64),  # white jacket + sneakers / shade / gold buttons
    b=(46, 46, 56), B=(24, 24, 32),                    # black trousers / shade (+ sword bag shade)
    c=(40, 46, 76), G=(128, 134, 152),                 # sword bag (navy) / strap + blade shade
    t=(220, 228, 240),                                 # katana blade
)
sp = Sprite('okkotsu', W=46, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- sword bag on the back: top sticks out above the back shoulder ----------------
bag = sp.layer()
bag.poly('c', [(3, 21), (9, 18), (17, 34), (11, 37)])
seg(bag, 'B', (5, 22), (12, 36)); seg(bag, 'B', (5, 23), (12, 35))
bag.poly('B', [(3, 21), (9, 18), (10, 21), (5, 24)])                                # tied end of the bag

# ---------------- back arm (sleeve + hand) ----------------
back_arm = sp.layer()
back_arm.poly('W', [(10, 21), (15, 21), (15, 29), (10, 30), (8, 26)])
back_arm.ell('s', 8, 28, 13, 33).h('S', 9, 12, 32)

# ---------------- legs: black slim trousers, white sneakers ----------------
leg_b = sp.layer()
leg_b.poly('b', [(14, 33), (20, 33), (17, 40), (14, 46), (9, 46), (11, 40)])
seg(leg_b, 'B', (14, 34), (10, 45)); seg(leg_b, 'B', (15, 34), (12, 40))
leg_b.poly('w', [(8, 45), (15, 45), (15, 50), (4, 50), (5, 47)]).h('W', 4, 15, 50).h('W', 9, 14, 46)
leg_f = sp.layer()
leg_f.poly('b', [(21, 33), (27, 33), (29, 40), (30, 46), (25, 46), (24, 40)])
seg(leg_f, 'B', (22, 34), (24, 39)); leg_f.v('B', 25, 40, 45)
leg_f.poly('w', [(24, 45), (31, 45), (33, 47), (35, 48), (35, 50), (24, 50)]).h('W', 24, 35, 50).h('W', 26, 30, 46)

# ---------------- torso: white hip-length jacket, off-centre closure, strap across the chest ----------------
torso = sp.layer()
torso.poly('w', [(12, 21), (27, 21), (27, 28), (27, 35), (13, 35), (12, 28)])
torso.poly('W', [(12, 21), (15, 21), (15, 35), (13, 35), (12, 28)])                 # back side in shade
torso.h('W', 14, 26, 34)                                                            # hem
seg(torso, 'W', (22, 22), (24, 33))                                                 # diagonal closure
torso.px('g', (24, 26))                                                             # gold button
seg(torso, 'G', (14, 22), (26, 31)); seg(torso, 'G', (14, 23), (26, 32))            # sword-bag strap
torso.px('w', (20, 35), (21, 35))

# ---------------- head ----------------
head = sp.layer()
head.rect('s', 18, 17, 22, 21).v('S', 18, 17, 20)                                   # neck
head.ell('h', 9, 1, 30, 18)                                                         # smooth, rounded hair
head.poly('h', [(9, 8), (15, 8), (15, 17), (11, 18), (9, 15)])
head.poly('s', [(15, 8), (29, 7), (31, 11), (31, 16), (27, 20), (21, 21), (17, 18), (15, 13)])  # soft oval face
for pts in ([(14, 5), (21, 5), (19, 9)], [(19, 5), (24, 5), (22, 10)], [(23, 5), (31, 6), (29, 9)],
            [(28, 5), (32, 7), (31, 9)], [(12, 6), (16, 6), (16, 12)]):
    head.poly('h', pts)                                                             # locks hanging down over the forehead
head.poly('h', [(16, 1), (19, -1), (22, 1)])
seg(head, 'H', (17, 1), (16, 5)); seg(head, 'H', (21, 5), (22, 9)); seg(head, 'H', (11, 9), (12, 15))
seg(head, 'H', (26, 4), (27, 7))
head.rect('s', 15, 12, 16, 14).px('S', (15, 13))                                    # ear tip under the hair
head.h('S', 17, 30, 10)                                                             # shade under the fringe
# thin brows; big round eyes: lid line, 2 rows of white round a small pupil, heavy dark circles below
head.px('o', (19, 10), (20, 10), (25, 10), (26, 10), (27, 10))
head.h('o', 20, 21, 12).h('o', 25, 27, 12).px('o', (19, 13), (24, 13), (28, 13))   # rounded upper lids
head.px('e', (21, 13), (19, 14), (21, 14)).px('k', (20, 13), (20, 14))
head.px('e', (25, 13), (27, 13), (24, 14), (25, 14), (27, 14), (28, 14)).px('k', (26, 13), (26, 14))
head.h('u', 19, 21, 15).h('u', 25, 28, 15)                                          # dark circles
head.px('S', (31, 15), (31, 16))                                                    # nose
head.h('m', 25, 26, 17)                                                             # small flat mouth
head.v('S', 17, 16, 18).h('S', 18, 20, 19)                                          # jaw shade

# ---------------- tall stiff collar with a gold button ----------------
collar = sp.layer()
collar.poly('w', [(15, 17), (18, 19), (22, 20), (26, 18), (27, 23), (22, 24), (15, 23)])
collar.poly('W', [(15, 17), (18, 19), (18, 23), (15, 23)])
collar.px('g', (25, 20))

# ---------------- katana (drawn, held in front, blade forward-up) ----------------
katana = sp.layer()
katana.poly('t', [(30, 27), (41, 15), (44, 13), (43, 17), (33, 30)])
seg(katana, 'G', (33, 28), (42, 17))
katana.poly('b', [(26, 32), (30, 28), (32, 30), (28, 34)])                          # dark grip
katana.poly('g', [(29, 26), (31, 25), (34, 29), (33, 31)])                          # small guard

# ---------------- front arm: loose white sleeve, hand on the grip ----------------
front = sp.layer()
front.poly('w', [(24, 21), (29, 21), (31, 25), (30, 30), (26, 31), (26, 26)])
seg(front, 'W', (25, 22), (27, 30))
front.ell('s', 27, 27, 32, 32).h('S', 28, 31, 31)

for L in (bag, back_arm, leg_b, leg_f, torso, head, collar, katana, front):
    sp.add(L)
sp.save()
