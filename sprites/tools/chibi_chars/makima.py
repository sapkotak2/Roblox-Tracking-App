"""Makima (Chainsaw Man) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(36, 18, 24),                                   # outline
    h=(214, 80, 66), H=(150, 44, 42), l=(240, 140, 118),  # coral-red hair (+ shine)
    s=(250, 220, 198), S=(216, 170, 150),             # skin
    e=(252, 250, 244), y=(242, 200, 56),              # eye white, yellow ringed iris
    w=(246, 246, 242), W=(184, 192, 208),             # white shirt
    t=(52, 50, 64), T=(30, 28, 40),                   # black tie / trousers / shoes
)
sp = Sprite('makima', W=40, H=52, palette=PAL)

# ---------------- braid down her back (behind everything) ----------------
braid = sp.layer().poly('h', [(8, 15), (13, 15), (10, 26), (8, 34), (3, 34), (5, 25), (7, 19)])
for y in range(18, 33, 3):                                                   # braid segments: short diagonal lines
    cx = round(10 - (y - 15) * 4.5 / 19)
    braid.px('H', (cx - 2, y), (cx - 1, y), (cx, y + 1), (cx + 1, y + 1))
braid.px('H', (7, 20), (6, 23), (6, 24), (5, 27), (5, 28), (4, 31), (4, 32))      # back edge in shade
braid.h('T', 3, 8, 33).h('T', 3, 8, 34)                                      # hair tie
braid.poly('h', [(3, 35), (8, 35), (8, 38), (5, 41), (2, 38)]).px('H', (5, 37), (5, 38))   # tuft at the end

# ---------------- back arm (sleeve hanging, angled away from the body) ----------------
back_arm = sp.layer().poly('w', [(11, 21), (16, 21), (13, 32), (8, 31)]).poly('W', [(11, 22), (13, 22), (10, 32), (8, 31)])
back_hand = sp.layer().ell('s', 7, 30, 11, 34).px('S', (8, 33), (9, 33))

# ---------------- legs: slim, clear gap ----------------
leg_b = sp.layer().poly('t', [(14, 32), (20, 32), (18, 47), (13, 47)]).v('T', 14, 34, 46).v('T', 15, 40, 46)
leg_f = sp.layer().poly('t', [(20, 32), (26, 32), (27, 47), (22, 47)]).v('T', 22, 37, 46)
shoe_b = sp.layer().poly('T', [(12, 46), (18, 46), (19, 50), (10, 50)])
shoe_f = sp.layer().poly('T', [(21, 46), (27, 46), (30, 50), (21, 50)]).px('t', (26, 47), (27, 48), (28, 48))

# ---------------- torso: neck, white shirt narrowing to the waist, collar + black tie ----------------
torso = sp.layer()
torso.rect('s', 17, 16, 23, 21).v('S', 17, 16, 21).h('S', 18, 22, 17)                    # neck
torso.poly('w', [(13, 20), (17, 20), (20, 23), (23, 20), (26, 20), (27, 24), (25, 30), (26, 34), (14, 34), (15, 30), (13, 24)])
torso.poly('W', [(13, 21), (16, 21), (16, 34), (14, 34), (15, 30), (14, 25)])             # back side in shade
torso.poly('w', [(16, 20), (20, 22), (18, 24), (15, 21)]).poly('w', [(24, 20), (20, 22), (22, 24), (25, 21)])  # collar points
torso.px('W', (17, 22), (18, 23), (23, 22), (22, 23))
torso.poly('t', [(19, 22), (21, 22), (22, 29), (20, 31), (18, 29)]).v('T', 19, 23, 29)    # tie
torso.h('t', 14, 25, 33).h('T', 14, 25, 34)                                              # trouser waistband
torso.px('W', (23, 27), (24, 28), (24, 29))                                              # one fold line

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 8, 0, 30, 17)
head.poly('h', [(9, 8), (8, 17), (12, 18)])                                              # hair falling behind the neck
head.poly('s', [(14, 6), (28, 6), (29, 10), (29, 15), (26, 18), (18, 18), (14, 15)])     # face
# fringe: parted bangs, ending above the eyes; long side locks framing the face
head.poly('h', [(13, 3), (30, 3), (30, 8), (27, 6), (24, 9), (22, 6), (19, 9), (16, 6), (14, 9)])
head.poly('h', [(12, 6), (16, 6), (16, 18), (13, 19)])                                    # far side lock
head.poly('h', [(28, 6), (31, 6), (31, 17), (29, 18)])                                    # near side lock
head.poly('H', [(8, 7), (12, 5), (13, 18), (9, 17)])                                      # back of the head in shade
head.px('H', (22, 6), (21, 5), (16, 6), (15, 5), (27, 6), (26, 5), (13, 10), (13, 11))  # strands
head.px('l', (19, 2), (20, 2), (21, 2), (22, 3))                                          # shine
head.h('o', 17, 19, 9).h('o', 23, 26, 9)                                                  # calm half-lidded lids
head.px('e', (17, 10), (18, 10), (17, 11)).px('y', (19, 10), (18, 11), (19, 11)).px('o', (19, 10))   # far eye
head.px('e', (23, 10), (23, 11)).px('y', (24, 10), (26, 10), (24, 11), (25, 11), (26, 11)).px('o', (25, 10))  # near eye
head.px('S', (27, 13)).h('S', 24, 25, 16)                                                 # nose, small mouth

# ---------------- front arm: relaxed at her side ----------------
front = sp.layer().poly('w', [(24, 20), (28, 21), (32, 31), (28, 32), (26, 26)]).v('W', 27, 26, 30).v('W', 26, 22, 25)
front_hand = sp.layer().ell('s', 28, 30, 32, 34).px('S', (29, 33), (30, 33))

for L in (braid, back_arm, back_hand, leg_b, leg_f, shoe_b, shoe_f, torso, head, front, front_hand):
    sp.add(L)
sp.save()
