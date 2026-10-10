"""Overhaul (Kai Chisaki, My Hero Academia) - chibi redraw (see tools/chibi.py for the style guide).
Checklist: refs/redraw/overhaul/NOTES.md (red/gold plague beak mask, purple fur collar, cropped dark-green bomber,
dark shirt + grey tie, brown belt, black trousers, white sneakers, white gloves, open hand reaching forward)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(24, 16, 24),                                   # outline
    h=(92, 56, 74), H=(54, 30, 46),                   # very dark brown hair with a purple tint
    s=(242, 202, 168), S=(204, 152, 124),             # skin
    e=(244, 242, 232), n=(230, 186, 66),              # eye white; gold (iris, mask trim, rivets, buckle)
    m=(164, 46, 46), M=(104, 26, 32),                 # dark red plague mask
    f=(140, 92, 204), F=(90, 54, 146),                # purple fur collar
    g=(62, 98, 62), G=(38, 64, 42),                   # dark green bomber jacket
    t=(50, 50, 60), T=(30, 30, 40),                   # dark shirt / black trousers
    b=(118, 74, 42),                                  # brown belt
    w=(248, 248, 248), W=(178, 186, 200),             # white gloves, white sneakers
)
sp = Sprite('overhaul', W=46, H=52, palette=PAL)

# ---------------- back arm (hangs at his side, glove at the hip) ----------------
back_arm = sp.layer().poly('g', [(8, 21), (13, 21), (12, 30), (7, 30)]).v('G', 8, 22, 30).v('G', 9, 26, 30)
back_arm.h('G', 7, 12, 29).h('T', 7, 12, 30)                                   # ribbed cuff
back_hand = sp.layer().ell('w', 6, 30, 11, 36).v('W', 6, 32, 35).px('W', (7, 35), (8, 35)).px('o', (10, 33))

# ---------------- legs: slim black trousers, clear gap, white sneakers ----------------
leg_b = sp.layer().poly('t', [(12, 33), (18, 33), (17, 46), (12, 46)]).v('T', 12, 35, 46).v('T', 13, 35, 46)
leg_f = sp.layer().poly('t', [(21, 33), (27, 33), (29, 46), (23, 46)]).v('T', 23, 37, 46)
shoe_b = sp.layer().poly('w', [(11, 46), (17, 46), (18, 50), (8, 50)]).h('W', 8, 18, 50).px('W', (13, 47), (14, 47))
shoe_f = sp.layer().poly('w', [(22, 46), (29, 46), (32, 50), (22, 50)]).h('W', 22, 32, 50).px('W', (26, 47), (27, 47))

# ---------------- torso: dark shirt + grey tie, cropped green bomber with ribbed hem, brown belt ----------------
torso = sp.layer()
torso.poly('g', [(10, 20), (29, 20), (30, 25), (28, 30), (29, 33), (10, 33), (11, 30), (9, 25)])
torso.poly('t', [(17, 20), (23, 20), (23, 29), (17, 29)])                       # shirt in the opening
torso.v('W', 20, 21, 28).v('W', 21, 22, 27)                                      # grey tie
torso.poly('G', [(10, 21), (13, 21), (13, 33), (11, 33), (11, 30), (10, 26)])   # back side of the jacket in shade
torso.v('G', 16, 21, 28).v('G', 24, 21, 28)                                      # jacket front edges
torso.h('G', 10, 29, 29).h('G', 10, 29, 30).px('g', (12, 30), (15, 30), (18, 30), (21, 30), (25, 30), (28, 30))  # ribbed hem
torso.h('b', 10, 29, 31).h('b', 10, 29, 32).px('n', (19, 31), (20, 31), (19, 32), (20, 32))  # brown belt + gold buckle

# ---------------- big purple fur collar: one flat shape with a few big tufts ----------------
collar = sp.layer()
collar.ell('f', 4, 13, 17, 25).ell('f', 21, 15, 33, 25).rect('f', 10, 16, 28, 23)        # puffy ring round the shoulders
collar.poly('f', [(5, 19), (1, 21), (5, 23)]).poly('f', [(31, 18), (35, 20), (32, 22)])   # side tufts
for y, (x0, x1) in ((23, (4, 15)), (24, (5, 15)), (23, (24, 33)), (24, (23, 32))):
    collar.h('F', x0, x1, y)                                                               # flat shade band underneath
collar.poly('t', [(16, 21), (24, 21), (22, 25), (18, 25)]).v('W', 20, 22, 25)              # shirt + tie at the opening
# ---------------- head ----------------
head = sp.layer()
head.ell('h', 9, 1, 29, 17)
for pts in ([(10, 4), (9, -1), (15, 2)], [(15, 2), (17, -1), (20, 2)], [(20, 1), (24, -1), (25, 3)],
            [(24, 2), (30, 1), (28, 6)], [(9, 7), (5, 7), (9, 11)], [(9, 11), (6, 14), (11, 14)]):
    head.poly('h', pts)                                                          # short messy spikes
head.poly('s', [(15, 6), (28, 6), (29, 10), (29, 16), (26, 19), (17, 19), (14, 15)])   # face
head.poly('h', [(14, 4), (29, 4), (29, 6), (27, 5), (26, 6), (24, 5), (22, 5), (21, 6), (19, 5), (16, 6), (15, 9)])  # loose fringe
head.poly('H', [(9, 7), (13, 5), (14, 13), (10, 13)])                            # back of the head in shade
head.px('H', (14, 1), (15, 2), (19, 2), (20, 3), (24, 3), (25, 4))               # strand lines
head.px('s', (14, 10), (14, 11), (14, 12)).px('S', (15, 11), (15, 12))          # ear (clearly visible)
# cold half-lidded eyes: heavy lid line, gold iris, low thin brows
head.h('o', 17, 18, 6).px('o', (19, 7)).h('o', 24, 26, 6).px('o', (23, 7))     # short low brows angled to the nose
head.h('o', 17, 19, 8).h('o', 23, 26, 8)                                         # heavy flat upper lids
head.px('e', (17, 9), (18, 9), (17, 10), (18, 10)).px('n', (19, 9), (19, 10)).px('o', (19, 9))      # far eye
head.px('e', (23, 9), (24, 9), (23, 10), (24, 10)).px('n', (25, 9), (26, 9), (25, 10), (26, 10)).px('o', (25, 9))  # near eye
head.h('S', 17, 19, 11).h('S', 23, 26, 11)                                       # tired under-eye line
# red plague-doctor mask with gold rim: covers nose/mouth/chin, beak sticks far out forward and curves down
head.poly('m', [(18, 12), (27, 12), (29, 14), (29, 19), (26, 21), (19, 21), (18, 17)])   # cup over nose/mouth/chin
head.poly('m', [(27, 13), (32, 15), (38, 20), (38, 22), (33, 21), (28, 20)])             # long beak
head.h('n', 18, 27, 12).px('n', (28, 13), (29, 13), (30, 14), (31, 14), (32, 15), (33, 16), (34, 17), (35, 18), (36, 19), (37, 20))
head.px('n', (38, 21), (37, 21)).px('n', (21, 15), (25, 15), (21, 18))           # gold beak tip, rivets
head.h('M', 29, 36, 21).px('M', (28, 20), (29, 20)).v('M', 19, 13, 20).h('M', 20, 25, 20)   # underside / back-edge shade
head.h('o', 15, 18, 14)                                                          # strap to the ear

# ---------------- front arm: reaching toward the enemy, white glove open with spread fingers ----------------
front = sp.layer()
front.poly('g', [(25, 20), (30, 20), (33, 26), (29, 29), (26, 25)]).v('G', 26, 22, 26)          # upper arm (under the collar)
front.poly('g', [(29, 25), (37, 24), (38, 29), (30, 30)]).h('G', 31, 37, 29)                    # forearm reaching forward
front.v('G', 36, 24, 29).v('T', 37, 24, 29)                                                      # ribbed cuff
hand = sp.layer()
dy = 4
hand.poly('w', [(38, 20 + dy), (41, 19 + dy), (42, 24 + dy), (39, 27 + dy)])                     # palm
for f in ([(40, 19), (42, 15), (43, 16), (42, 20)], [(41, 20), (44, 17), (45, 18), (42, 21)],
          [(41, 22), (45, 21), (45, 22), (42, 23)], [(40, 24), (44, 25), (43, 26), (40, 26)]):
    hand.poly('w', [(x, y + dy) for x, y in f])                                                 # spread fingers
hand.poly('w', [(38, 20 + dy), (38, 16 + dy), (39, 16 + dy), (40, 20 + dy)])                     # thumb up
hand.px('W', (39, 25 + dy), (40, 25 + dy), (39, 26 + dy), (38, 24 + dy))

for L in (back_arm, back_hand, leg_b, leg_f, shoe_b, shoe_f, torso, front, collar, head, hand):
    sp.add(L)
sp.save()
