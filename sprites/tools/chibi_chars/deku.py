"""Izuku Midoriya / Deku (My Hero Academia) - chibi redraw (see tools/chibi.py for the style guide).
Matched to refs/redraw/deku (04 2nd costume full body + face crop), checklist in refs/redraw/deku/NOTES.md."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(16, 24, 24),                                   # outline (also pupils, brows)
    h=(32, 92, 62), H=(16, 40, 30),                  # dark green hair / near-black shade
    s=(252, 214, 176), S=(214, 150, 112),             # skin (shade also = freckles)
    e=(255, 255, 250), g=(40, 130, 84), m=(132, 44, 44),   # eye white / boot soles, green iris ring, mouth
    c=(40, 132, 116), C=(24, 88, 80),                 # teal-green suit
    K=(40, 44, 50),                                   # black costume parts (side panels, knee + shin guards)
    w=(240, 230, 200), W=(194, 182, 150),             # cream shoulder pads + gloves
    u=(74, 104, 196),                                 # blue glove stripe
    r=(214, 42, 42), R=(144, 24, 30),                 # red belt + boots
    x=(150, 156, 166),                                # grey respirator
)
sp = Sprite('deku', W=42, H=52, palette=PAL)

# ---------------- back arm: teal sleeve, cream gloved fist at the hip ----------------
arm_b = sp.layer()
arm_b.poly('c', [(11, 21), (15, 21), (13, 28), (8, 28), (8, 25)]).v('C', 9, 25, 27).v('C', 10, 23, 27)
arm_b.poly('K', [(8, 25), (12, 25), (12, 28), (8, 28)])                            # black forearm guard
glove_b = sp.layer().rect('w', 6, 26, 11, 31).h('W', 6, 11, 31).v('W', 6, 27, 30).h('u', 7, 11, 26)

# ---------------- legs: teal thighs, black knee + shin guards, big red high-top boots ----------------
leg_b = sp.layer()
leg_b.poly('c', [(14, 32), (20, 32), (18, 39), (16, 45), (10, 45), (12, 38)]).v('C', 13, 34, 38)
leg_b.poly('K', [(11, 37), (18, 37), (17, 45), (10, 45)]).h('o', 11, 17, 40)       # knee pad + shin guard
leg_f = sp.layer()
leg_f.poly('c', [(21, 32), (26, 32), (29, 37), (30, 45), (24, 45), (23, 38)]).v('C', 24, 35, 37)
leg_f.poly('K', [(23, 36), (29, 36), (30, 45), (24, 45)]).h('o', 24, 29, 39)
boot_b = sp.layer().poly('r', [(9, 43), (17, 43), (17, 47), (19, 48), (19, 50), (7, 50), (8, 46)])
boot_b.v('R', 9, 44, 48).h('R', 10, 16, 44).h('e', 8, 18, 49).px('w', (13, 46), (14, 47))   # cuff, sole, laces
boot_f = sp.layer().poly('r', [(23, 43), (30, 43), (31, 46), (34, 48), (34, 50), (23, 50)])
boot_f.v('R', 24, 44, 48).h('R', 24, 29, 44).h('e', 24, 33, 49).px('w', (28, 46), (29, 47))

# ---------------- torso: teal suit, black side panels, red belt with pouches ----------------
torso = sp.layer()
torso.poly('c', [(13, 21), (26, 21), (27, 25), (25, 33), (14, 33), (12, 25)])
torso.poly('K', [(12, 23), (15, 22), (16, 33), (14, 33), (12, 26)])               # black side panel
torso.v('C', 20, 23, 29).px('C', (19, 29), (21, 29))                              # centre seam
torso.h('r', 13, 26, 30).h('R', 13, 26, 31).rect('r', 23, 30, 26, 34).h('R', 23, 26, 34)   # belt + pouch
torso.rect('s', 17, 17, 21, 20)
# grey respirator worn around the neck
mask = sp.layer().poly('x', [(15, 18), (24, 18), (25, 21), (20, 24), (14, 21)]).v('o', 20, 19, 22).px('o', (17, 20), (23, 20))
pad_b = sp.layer().poly('w', [(11, 21), (16, 20), (16, 24), (11, 25)]).h('W', 11, 15, 24)   # cream shoulder pads

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 7, 1, 32, 19)
# messy curly mop: clumps poking out everywhere
for t1, t2, b1, b2 in (((10, 0), (12, 0), (8, 5), (16, 2)), ((18, 0), (20, 0), (15, 2), (23, 2)),
                       ((26, 0), (28, 1), (23, 2), (31, 5)), ((34, 5), (34, 7), (30, 3), (32, 11)),
                       ((4, 4), (4, 6), (10, 3), (8, 10)), ((3, 11), (3, 13), (8, 8), (8, 16)),
                       ((5, 18), (6, 19), (9, 14), (12, 19)), ((33, 12), (33, 14), (31, 10), (31, 16))):
    head.poly('h', [t1, t2, b2, b1])
head.poly('s', [(14, 9), (29, 9), (30, 12), (29, 16), (26, 19), (17, 19), (14, 16)])   # face
for pts in ([(12, 6), (19, 6), (16, 10)], [(18, 6), (25, 6), (21, 10)], [(24, 6), (31, 7), (28, 10)],
            [(12, 7), (15, 7), (14, 15)]):
    head.poly('h', pts)                                                           # fringe clumps
for pts in ([(14, 3), (16, 3), (16, 8)], [(21, 2), (23, 2), (22, 7)], [(28, 4), (30, 5), (27, 8)],
            [(9, 6), (12, 6), (13, 10)], [(8, 11), (9, 9), (12, 12)], [(9, 15), (10, 13), (12, 17)]):
    head.poly('H', pts)                                                           # black shadows between clumps
head.v('S', 15, 11, 15).px('S', (16, 10), (17, 10), (22, 10), (23, 10))                                                           # face shade (back side)
# HUGE round eyes: big outlined whites, small pupil with a green ring
head.h('o', 17, 19, 11).v('o', 16, 12, 13).v('o', 20, 12, 13)
head.rect('e', 17, 12, 19, 14).px('g', (18, 12), (19, 12)).px('o', (18, 13))
head.h('o', 23, 26, 11).v('o', 22, 12, 13).v('o', 27, 12, 13)
head.rect('e', 23, 12, 26, 14).px('g', (24, 12), (25, 12), (24, 13)).px('o', (25, 13))
head.px('S', (16, 15), (18, 16), (27, 15), (28, 16))                              # freckles
head.px('S', (29, 13))                                                            # nose
head.px('m', (22, 16), (26, 16)).h('e', 23, 25, 16).h('m', 23, 25, 17)           # big open grin, upper teeth

# ---------------- front arm: punching forward, cream glove with a blue stripe ----------------
arm_f = sp.layer()
arm_f.poly('c', [(24, 21), (29, 21), (34, 23), (34, 27), (28, 27), (25, 26)]).h('C', 25, 33, 26)
arm_f.poly('K', [(29, 22), (34, 23), (34, 27), (29, 27)])                         # black forearm guard
pad_f = sp.layer().poly('w', [(23, 20), (28, 20), (29, 24), (24, 25)]).h('W', 24, 28, 24)
glove_f = sp.layer().rect('w', 33, 21, 38, 27).h('W', 33, 38, 27).v('u', 33, 22, 26).px('W', (36, 24), (37, 24))

for L in (arm_b, glove_b, leg_b, leg_f, boot_b, boot_f, torso, pad_b, head, mask, arm_f, pad_f, glove_f):
    sp.add(L)
sp.save()
