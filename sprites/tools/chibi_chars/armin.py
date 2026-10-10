"""Armin Arlert (Attack on Titan) - chibi redraw (see tools/chibi.py for the style guide).
Blond bob, big blue eyes, Survey Corps tan jacket, white trousers with leather straps, dark brown boots,
grey ODM gear boxes on the hips with a blade handle."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(42, 26, 22),                                    # outline
    h=(250, 218, 112), H=(198, 150, 58), l=(255, 246, 196),  # hair base / shade / shine
    s=(252, 216, 184), S=(226, 158, 124),              # skin
    e=(255, 255, 255), k=(44, 30, 34), b=(56, 140, 224), m=(168, 70, 64),  # eye white, lash, blue iris, mouth
    j=(190, 136, 82), J=(126, 82, 48),                 # jacket tan
    w=(240, 238, 230), W=(178, 174, 170),              # white shirt / trousers
    n=(86, 52, 36), N=(126, 82, 48),                   # straps and boots (highlight = jacket shade)
    g=(160, 166, 178), G=(100, 104, 118),              # ODM gear steel
)
sp = Sprite('armin', W=48, H=52, palette=PAL)
L = sp.layer

# ---------------- back arm (sleeve + hand, hangs behind the body) ----------------
back_arm = L()
back_arm.poly('j', [(13, 22), (18, 22), (17, 30), (12, 30)]).v('J', 13, 23, 30).v('J', 14, 23, 30)
back_arm.rect('s', 12, 30, 16, 33).px('S', (13, 32), (14, 32))

# ---------------- back ODM box (pokes out behind the hip) ----------------
odm_b = L()
odm_b.rect('g', 10, 31, 17, 36).h('G', 10, 17, 35)

# ---------------- legs: white trousers with a thigh strap, dark knee boots ----------------
leg_b = L()
leg_b.poly('w', [(16, 33), (22, 33), (21, 44), (15, 44)]).v('W', 16, 34, 44).v('W', 17, 34, 44)
leg_b.h('n', 16, 21, 40)                                                           # thigh strap
leg_b.poly('n', [(14, 44), (21, 44), (20, 47), (14, 47)])
leg_b.poly('n', [(11, 47), (20, 47), (20, 50), (10, 50)])
leg_b.v('N', 19, 45, 47).h('N', 12, 14, 48)
leg_f = L()
leg_f.poly('w', [(23, 33), (29, 33), (31, 44), (25, 44)]).poly('W', [(23, 33), (25, 33), (27, 44), (25, 44)])
leg_f.h('n', 24, 30, 40)
leg_f.poly('n', [(25, 44), (31, 44), (31, 47), (26, 47)])
leg_f.poly('n', [(26, 47), (35, 47), (36, 50), (26, 50)])
leg_f.v('N', 30, 45, 47).h('N', 32, 34, 48)

# ---------------- torso: short tan jacket over a white shirt, chest strap, belt ----------------
torso = L()
torso.rect('s', 20, 17, 24, 22).v('S', 20, 17, 22).v('S', 21, 19, 22)              # neck
torso.poly('w', [(18, 21), (27, 21), (28, 34), (17, 34)])                          # shirt / hips
torso.v('W', 18, 30, 34).v('W', 19, 30, 34)
torso.h('n', 17, 28, 30)                                                            # belt
torso.poly('j', [(16, 21), (22, 21), (22, 28), (16, 28)])                          # jacket, back half
torso.poly('j', [(25, 21), (29, 21), (29, 28), (25, 28)])                          # jacket, front half
torso.v('J', 17, 22, 28).v('J', 18, 22, 28)
torso.h('n', 22, 25, 25)                                                            # chest strap in the opening

# ---------------- head: bob cut ----------------
head = L()
head.ell('h', 10, 0, 33, 18)
head.poly('h', [(11, 7), (17, 8), (18, 19), (11, 19)])                            # bob falls to the jaw at the back
head.poly('s', [(16, 7), (30, 7), (31, 11), (31, 13), (29, 16), (25, 19), (21, 19), (18, 16), (16, 12)])  # face
# blunt bangs with a side part, cut above the eyes
for pts in ([(14, 2), (22, 2), (21, 8), (17, 9)], [(20, 2), (28, 3), (27, 8), (22, 8)],
            [(26, 2), (32, 3), (33, 9), (32, 16), (30, 15), (30, 8), (28, 7)]):
    head.poly('h', pts)
head.poly('h', [(12, 6), (19, 8), (19, 19), (12, 19)])                            # side of the bob over the ear
head.v('H', 15, 10, 19).v('H', 17, 13, 19).h('H', 12, 18, 18).h('H', 12, 18, 19)
head.px('H', (22, 3), (22, 4), (21, 5), (21, 6), (28, 4), (27, 5), (27, 6), (31, 8), (31, 9), (31, 10))
head.px('l', (23, 1), (24, 1), (17, 3), (18, 3))
# brows, big eyes, nose, mouth
head.h('k', 20, 21, 9).h('k', 25, 28, 9)
head.h('k', 19, 22, 11).px('e', (20, 12), (20, 13), (20, 14)).px('b', (21, 12), (21, 13), (21, 14))
head.h('k', 24, 28, 11)
head.px('e', (24, 12), (24, 13), (24, 14), (27, 12), (27, 13), (27, 14))
head.px('b', (25, 12), (26, 12), (25, 13), (26, 13), (25, 14), (26, 14)).px('k', (26, 12))
head.px('S', (30, 14))
head.h('m', 26, 27, 17)
head.px('S', (21, 17), (22, 18))

# ---------------- front ODM box ----------------
odm_f = L()
odm_f.rect('g', 26, 31, 34, 36).h('G', 26, 34, 35).v('G', 27, 32, 35)

# ---------------- front arm: elbow bent, blade handle held forward ----------------
front = L()
front.poly('j', [(26, 21), (31, 21), (32, 27), (27, 28)]).v('J', 27, 22, 27)        # upper arm
front.poly('j', [(28, 25), (35, 25), (35, 29), (29, 29)]).h('J', 29, 35, 29)        # forearm
blade = L().poly('g', [(38, 25), (46, 25), (47, 26), (46, 28), (38, 28)]).h('e', 38, 46, 26)
grip = L().rect('G', 35, 23, 38, 30)                                                # ODM blade handle
hand = L().rect('s', 34, 24, 38, 29).h('S', 34, 38, 28).h('S', 34, 38, 29)

for lay in (back_arm, odm_b, leg_b, leg_f, torso, head, odm_f, blade, grip, front, hand):
    sp.add(lay)
sp.save()
