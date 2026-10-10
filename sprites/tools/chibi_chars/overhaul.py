"""Overhaul (Kai Chisaki, My Hero Academia) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(24, 20, 28),                                   # outline
    h=(80, 52, 38), H=(46, 30, 24),                   # dark brown hair
    s=(242, 200, 164), S=(204, 152, 122),             # skin
    e=(252, 248, 236), y=(236, 180, 36),              # eye white, golden iris
    m=(42, 40, 50), M=(118, 118, 134),                # black plague mask / shoes (+ one shine), also trouser shade
    f=(232, 212, 166), F=(186, 156, 108),             # tan fur collar
    g=(44, 108, 94), G=(26, 68, 62),                  # teal-green jacket
    p=(136, 78, 170), P=(90, 46, 120),                # purple shirt
    w=(246, 246, 246), W=(176, 184, 200),             # white gloves
    t=(66, 64, 84),                                   # dark trousers
)
sp = Sprite('overhaul', W=42, H=52, palette=PAL)

# ---------------- back arm (hangs behind, a little away from the body) ----------------
back_arm = sp.layer().poly('g', [(7, 21), (12, 21), (11, 31), (6, 31)]).v('G', 7, 22, 31).v('G', 8, 26, 31)
back_hand = sp.layer().ell('w', 5, 30, 10, 35).px('W', (6, 34), (7, 34), (8, 34), (6, 33))

# ---------------- legs: two clear legs with a gap, readable shoes ----------------
leg_b = sp.layer().poly('t', [(12, 35), (18, 35), (17, 47), (11, 47)]).v('m', 12, 37, 46).v('m', 13, 37, 46)
leg_f = sp.layer().poly('t', [(21, 35), (27, 35), (29, 47), (23, 47)]).v('m', 23, 39, 46).px('m', (22, 37), (22, 38))
shoe_b = sp.layer().poly('m', [(10, 46), (17, 46), (18, 50), (8, 50)])
shoe_f = sp.layer().poly('m', [(22, 46), (29, 46), (32, 50), (22, 50)]).px('M', (29, 47), (30, 48))

# ---------------- jacket: shoulders, narrowing to the waist, open over the purple shirt ----------------
torso = sp.layer()
torso.poly('g', [(10, 20), (29, 20), (30, 25), (28, 31), (29, 37), (10, 37), (11, 31), (9, 25)])
torso.poly('p', [(18, 20), (22, 20), (22, 33), (18, 33)])                        # shirt in the opening
torso.v('P', 18, 21, 33)
torso.poly('G', [(10, 21), (13, 21), (13, 37), (11, 37), (11, 31), (10, 26)])   # back side of the jacket in shade
torso.v('G', 17, 21, 37).v('G', 23, 21, 37)                                      # jacket front edges
torso.h('m', 18, 22, 34).h('t', 18, 22, 35)                                      # belt + trousers in the opening
torso.h('G', 13, 28, 36)

# ---------------- big tan fur collar: one flat block, shaded underneath ----------------
collar = sp.layer()
collar.poly('f', [(8, 19), (14, 16), (26, 16), (32, 19), (32, 23), (26, 26), (22, 23), (18, 23), (14, 26), (7, 23)])
collar.poly('F', [(7, 22), (14, 25), (15, 23), (16, 22), (18, 22), (18, 23), (22, 23), (22, 22), (24, 22), (26, 25), (32, 22), (32, 23), (26, 26), (22, 23), (18, 23), (14, 26), (7, 23)])

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 9, 0, 30, 18).poly('h', [(21, 1), (31, 0), (30, 4), (25, 4)]).poly('h', [(10, 4), (12, 0), (16, 2)])
head.poly('h', [(11, 3), (6, 8), (7, 11), (6, 14), (12, 16)])                       # hair swept back at the nape
head.poly('s', [(14, 6), (29, 6), (30, 10), (30, 16), (27, 19), (17, 19), (14, 15)])  # face
head.poly('h', [(13, 4), (30, 4), (30, 6), (26, 6), (24, 8), (21, 6), (17, 7), (14, 9)])  # fringe, above the brows
head.poly('H', [(8, 9), (13, 6), (13, 14), (9, 13)])                                 # back of the head in shade
head.px('H', (17, 2), (18, 3), (19, 3), (20, 4), (26, 2), (27, 3), (28, 4), (24, 6), (24, 7))                # two strand lines + part
head.px('s', (14, 11), (14, 12)).px('S', (15, 12), (14, 13))                        # ear
head.h('o', 17, 19, 8).h('o', 23, 26, 8)                                            # brows
head.px('e', (17, 10), (18, 10), (19, 10), (17, 11), (18, 11)).px('y', (19, 10), (19, 11))      # far eye
head.px('e', (23, 10), (24, 10), (25, 10), (23, 11), (24, 11)).px('y', (25, 10), (25, 11), (26, 10), (26, 11))  # near eye
head.px('o', (26, 11)).h('S', 17, 19, 9).h('S', 23, 26, 9)
# plague-doctor beak mask over the lower face, beak pointing forward
head.poly('m', [(16, 13), (26, 13), (30, 14), (37, 18), (37, 19), (29, 20), (26, 21), (18, 21), (16, 17)])
head.h('o', 14, 16, 13)                                                             # strap to the ear
head.px('M', (28, 15), (29, 15), (30, 16), (31, 16), (32, 17)).v('o', 21, 15, 20)         # beak shine, centre seam

# ---------------- front arm: forearm forward, white glove raised, palm toward the enemy ----------------
front = sp.layer()
front.poly('g', [(26, 20), (31, 21), (33, 29), (28, 30), (27, 25)]).v('G', 28, 26, 29).v('G', 27, 22, 25)
front.poly('g', [(29, 26), (35, 24), (36, 28), (31, 30)]).h('G', 31, 35, 29)
hand = sp.layer().rect('w', 34, 19, 39, 28).poly('w', [(32, 22), (34, 21), (34, 25), (32, 25)])
hand.px('o', (34, 19), (39, 19), (39, 28)).v('W', 34, 24, 28).h('W', 35, 38, 28).px('W', (33, 24))
hand.v('W', 36, 20, 22).v('W', 38, 20, 22)                                           # finger gaps

for L in (back_arm, back_hand, leg_b, leg_f, shoe_b, shoe_f, torso, collar, head, front, hand):
    sp.add(L)
sp.save()
