"""Big Mom (Charlotte Linlin) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(26, 12, 26),                                   # outline
    s=(246, 196, 160), S=(214, 146, 116),             # skin / shade
    h=(246, 112, 168), H=(186, 56, 112),              # curly pink hair / curl lines
    p=(252, 186, 206), P=(226, 130, 166),             # pastel pink dress / shade
    w=(255, 255, 255), C=(184, 192, 214),             # white (dots, collar, hat, teeth) / shade
    k=(66, 50, 78), K=(40, 30, 52),                   # black cape / shade, shoes
    r=(214, 30, 52),                                  # red lips
)
sp = Sprite('bigmom', W=50, H=52, palette=PAL)

# ---------------- cape (behind everything) ----------------
cape = sp.layer().poly('k', [(8, 20), (42, 20), (47, 28), (47, 45), (2, 45), (2, 28)])
cape.poly('K', [(2, 45), (2, 28), (8, 21), (10, 45)]).poly('K', [(42, 30), (47, 45), (44, 45)])

# ---------------- hair falling behind the shoulders ----------------
hair_b = sp.layer()
for b in ((3, 12, 15, 24), (4, 18, 14, 28), (35, 12, 47, 24), (37, 18, 46, 27)):
    hair_b.ell('h', *b)
hair_b.line('H', [(6, 21), (9, 25)]).line('H', [(43, 20), (41, 24)])

# ---------------- legs + shoes ----------------
legs = sp.layer().rect('s', 15, 38, 21, 47).rect('s', 28, 38, 34, 47).v('S', 15, 38, 47).v('S', 16, 38, 47).v('S', 28, 38, 47)
shoes = sp.layer().poly('k', [(14, 47), (22, 47), (22, 50), (13, 50)]).poly('k', [(27, 47), (35, 47), (38, 49), (38, 50), (27, 50)])
shoes.h('K', 13, 22, 50).h('K', 27, 38, 50)

# ---------------- back arm ----------------
arm_b = sp.layer().ell('s', 7, 22, 16, 32).poly('s', [(8, 28), (14, 29), (13, 36), (7, 36)]).ell('s', 6, 33, 13, 39)
arm_b.v('S', 8, 25, 37).v('S', 7, 34, 37)

# ---------------- polka-dot dress ----------------
dress = sp.layer().poly('p', [(14, 23), (36, 23), (40, 30), (41, 35), (39, 40), (11, 40), (9, 35), (10, 30)])
dress.poly('P', [(9, 35), (10, 30), (14, 24), (15, 40), (11, 40)]).h('P', 11, 39, 40)
for x, y in ((20, 30), (28, 30), (35, 31), (12, 33), (24, 33), (32, 34), (17, 36), (28, 37), (36, 37)):
    dress.px('w', (x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1))

# ---------------- white collar ----------------
collar = sp.layer().ell('w', 8, 19, 42, 28).h('C', 10, 40, 27).h('C', 9, 41, 26).h('w', 13, 16, 26).h('w', 20, 23, 26).h('w', 27, 30, 26).h('w', 34, 37, 26)

# ---------------- head: huge curly hair, wide grin, bicorne hat ----------------
head = sp.layer()
head.ell('h', 6, 3, 44, 22)
for b in ((3, 6, 13, 16), (37, 6, 47, 16), (8, 2, 18, 10), (32, 2, 42, 10)):
    head.ell('h', *b)                                                # curls around the face
head.ell('s', 16, 6, 38, 24)                                         # big round face
head.poly('h', [(14, 5), (38, 5), (38, 10), (33, 8), (29, 10), (25, 7), (21, 10), (17, 8), (14, 11)])  # curly bangs
head.line('H', [(6, 10), (9, 13)]).line('H', [(5, 17), (9, 18)]).line('H', [(41, 10), (44, 13)]).line('H', [(41, 17), (45, 17)])
head.line('H', [(19, 6), (21, 8)]).line('H', [(29, 6), (31, 8)])
head.h('S', 17, 37, 11).px('S', (16, 12), (37, 12))                  # shade under the bangs
head.h('o', 21, 23, 12).h('o', 29, 32, 12)                           # brows
head.rect('w', 21, 13, 23, 15).v('o', 23, 13, 15).rect('w', 29, 13, 32, 15).v('o', 31, 13, 15)  # eyes (near one bigger)
head.px('S', (36, 15), (36, 16))                                     # nose
head.poly('r', [(23, 17), (36, 17), (36, 19), (34, 21), (25, 21), (23, 19)]).px('r', (22, 16), (37, 16))  # grin
head.h('w', 24, 35, 18).h('w', 25, 34, 19)                           # teeth
head.h('S', 19, 33, 23).v('S', 17, 17, 21)                            # chin / cheek shade
hat = sp.layer().poly('w', [(7, 8), (11, 4), (17, 1), (22, 0), (30, 0), (35, 1), (41, 4), (45, 8), (38, 7), (26, 6), (14, 7)])
hat.poly('C', [(7, 8), (14, 7), (26, 6), (38, 7), (45, 8), (38, 6), (26, 5), (14, 6)]).rect('k', 25, 2, 26, 3)

# ---------------- front arm: big bare arm, fist on the hip ----------------
arm = sp.layer().ell('s', 34, 22, 43, 31).poly('s', [(36, 27), (43, 27), (44, 34), (38, 35)]).ell('s', 37, 32, 45, 38)
arm.v('S', 36, 28, 34).h('S', 38, 44, 37)

for L in (cape, hair_b, legs, shoes, arm_b, dress, collar, head, hat, arm):
    sp.add(L)
sp.save()
