"""Armin Arlert (Attack on Titan) - chibi redraw (see tools/chibi.py for the style guide).
Matched to refs/redraw/armin (official colour artwork in the Survey Corps uniform, S1 anime face, official chibi),
checklist in refs/redraw/armin/NOTES.md: very big round sky-blue eyes with lots of white, worried brows, small open
mouth, round boyish face; golden blond bob (dome + straight fringe to the brows, sides to the chin covering the ears);
short tan Survey Corps jacket with the Wings of Freedom badge, white shirt, brown chest/thigh straps and belt, dark
brown hip panel, white trousers, dark brown knee boots; grey ODM boxes on the hips, handle + long blade in his hand."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(44, 28, 22),                                    # outline
    h=(246, 204, 76), H=(196, 140, 44),                # golden blond / shade
    s=(255, 222, 194), S=(232, 166, 130),              # skin
    e=(255, 255, 255), k=(40, 30, 40), b=(84, 156, 226), m=(150, 60, 56),  # eye white, lash/pupil, sky blue, mouth
    j=(204, 140, 72), J=(142, 88, 44),                 # tan jacket / shade
    w=(244, 242, 236), W=(182, 178, 176),              # white shirt + trousers / shade
    n=(84, 50, 34),                                    # dark brown leather: straps, belt, hip panel, boots
    g=(168, 174, 186), G=(104, 110, 124),              # ODM steel
)
sp = Sprite('armin', W=50, H=52, palette=PAL)
L = sp.layer

# ---------------- back arm (sleeve + fist, slightly back) ----------------
back_arm = L()
back_arm.poly('j', [(13, 22), (18, 22), (17, 30), (12, 30)]).v('J', 13, 23, 30).v('J', 14, 23, 30)
back_arm.rect('s', 12, 30, 16, 33).h('S', 13, 15, 32)

# ---------------- back ODM box (pokes out behind the hip, angled back) ----------------
odm_b = L().poly('g', [(10, 30), (17, 31), (17, 36), (9, 34)]).poly('G', [(9, 33), (17, 34), (17, 36), (9, 34)]).v('G', 10, 31, 33)

# ---------------- legs: white trousers with brown thigh straps, dark brown knee boots ----------------
leg_b = L()
leg_b.poly('w', [(16, 33), (22, 33), (21, 44), (15, 44)]).v('W', 16, 34, 44).v('W', 17, 34, 44)
leg_b.h('n', 16, 21, 37).h('n', 16, 21, 40)                                           # thigh straps
leg_b.poly('n', [(14, 43), (21, 43), (20, 47), (14, 47)])
leg_b.poly('n', [(11, 47), (20, 47), (20, 50), (10, 50)])
leg_b.v('J', 19, 44, 47)
leg_f = L()
leg_f.poly('w', [(23, 33), (29, 33), (31, 44), (25, 44)]).poly('W', [(23, 33), (25, 33), (27, 44), (25, 44)])
leg_f.h('n', 23, 30, 37).h('n', 24, 30, 40)
leg_f.poly('n', [(25, 43), (31, 43), (31, 47), (26, 47)])
leg_f.poly('n', [(26, 47), (35, 47), (36, 50), (26, 50)])
leg_f.v('J', 30, 44, 47)

# ---------------- torso: white shirt, short tan jacket, chest strap, belt, dark hip panel ----------------
torso = L()
torso.rect('s', 20, 17, 24, 22).v('S', 20, 17, 22)                                    # neck
torso.poly('w', [(18, 21), (27, 21), (28, 33), (17, 33)])                            # shirt
torso.v('W', 18, 27, 33).v('W', 19, 27, 33)
torso.poly('n', [(17, 29), (28, 29), (28, 32), (17, 32)])                            # belt + dark hip panel
torso.h('J', 17, 28, 29)
torso.poly('j', [(16, 21), (22, 21), (22, 28), (16, 28)])                            # jacket, back half
torso.poly('j', [(25, 21), (29, 21), (29, 28), (25, 28)])                            # jacket, front half
torso.v('J', 17, 22, 28).v('J', 18, 22, 28)
torso.h('n', 22, 25, 25)                                                              # chest strap in the opening
torso.px('b', (20, 23), (21, 23)).px('e', (20, 24), (21, 24))                         # Wings of Freedom badge
torso.h('w', 20, 21, 21).px('w', (25, 21))                                            # shirt collar points

# ---------------- head: golden bob ----------------
head = L()
head.ell('h', 10, 0, 33, 18)
head.poly('h', [(10, 8), (18, 8), (18, 20), (10, 20)])                               # bob falls to the chin at the back
head.poly('s', [(16, 7), (30, 7), (31, 11), (31, 14), (29, 17), (26, 19), (21, 19), (18, 17), (16, 13)])  # round boyish face
# straight-cut fringe down to the brows, uneven tips; near-side hair covers the ear down to the jaw
head.poly('h', [(13, 2), (32, 3), (32, 7), (29, 8), (27, 7), (24, 8), (21, 7), (18, 8), (15, 8)])
head.poly('h', [(30, 6), (33, 7), (33, 16), (31, 17), (31, 10)])
head.poly('h', [(11, 6), (19, 8), (19, 21), (11, 21)])                               # far side of the bob over the ear
head.v('H', 14, 9, 20).v('H', 16, 12, 20).h('H', 11, 18, 20)
head.px('H', (21, 4), (21, 5), (21, 6), (26, 4), (26, 5), (26, 6), (31, 5), (31, 6))
head.px('e', (23, 1), (24, 1))                                                       # shine
# worried brows (inner ends raised), very big round sky-blue eyes, small open mouth
head.px('H', (19, 9), (20, 9), (21, 8)).px('H', (24, 8), (25, 9), (26, 9), (27, 9))
head.h('k', 19, 22, 10).px('e', (19, 11), (19, 12), (19, 13), (22, 11), (22, 12), (22, 13))
head.px('b', (20, 11), (21, 11), (20, 12), (20, 13), (21, 13)).px('k', (21, 12))
head.h('k', 24, 28, 10)
head.px('e', (24, 11), (24, 12), (24, 13), (28, 11), (28, 12), (28, 13), (25, 14), (26, 14), (27, 14))
head.px('b', (25, 11), (26, 11), (27, 11), (25, 12), (27, 12), (25, 13), (26, 13), (27, 13)).px('k', (26, 12))
head.px('S', (30, 15))
head.px('m', (26, 17), (27, 17))
head.px('S', (21, 17), (22, 18))

# ---------------- front ODM box ----------------
odm_f = L().rect('g', 26, 31, 34, 36).h('G', 26, 34, 35).h('G', 26, 34, 36).v('G', 27, 32, 34)

# ---------------- front arm: elbow bent, ODM handle + long blade held forward ----------------
front = L()
front.poly('j', [(26, 21), (31, 21), (32, 27), (27, 28)]).v('J', 27, 22, 27)            # upper arm
front.poly('j', [(28, 25), (35, 25), (35, 29), (29, 29)]).h('J', 29, 35, 29)            # forearm
blade = L().poly('g', [(38, 25), (48, 25), (49, 26), (48, 28), (38, 28)]).h('e', 38, 47, 26)
grip = L().rect('G', 35, 23, 38, 31)                                                  # ODM handle with trigger
hand = L().rect('s', 34, 24, 38, 29).h('S', 34, 38, 28).h('S', 34, 38, 29)

for lay in (back_arm, odm_b, leg_b, leg_f, torso, head, odm_f, blade, grip, front, hand):
    sp.add(lay)
sp.save()
