"""Yuta Okkotsu (Jujutsu Kaisen) - chibi redraw (see tools/chibi.py for the style guide).
Messy near-black hair, tired eyes with dark circles, WHITE Jujutsu High uniform (long high-collared jacket, white
trousers), katana held in front."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(26, 24, 38),                                    # outline
    h=(50, 48, 64), H=(24, 22, 34), j=(112, 116, 146),  # hair base / strands / shine
    s=(246, 214, 186), S=(208, 164, 140),              # skin / shade
    e=(250, 250, 255), k=(52, 50, 84), u=(170, 128, 140), m=(160, 96, 90),  # eye white, iris, dark circles, mouth
    w=(242, 244, 250), W=(176, 184, 206),              # white uniform / shade
    b=(40, 40, 54), B=(84, 86, 106),                   # shoes + buttons / shoe shine
    g=(214, 222, 236), G=(138, 146, 166),              # katana blade / blade shade
    t=(198, 160, 70),                                  # guard
)
sp = Sprite('okkotsu', W=46, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- jacket tail behind the legs ----------------
tail = sp.layer()
tail.poly('w', [(12, 30), (20, 30), (19, 38), (14, 42), (7, 43), (9, 36)])
tail.poly('W', [(7, 43), (9, 36), (12, 31), (14, 33), (12, 42)])
seg(tail, 'W', (16, 34), (16, 41))

# ---------------- back arm (sleeve + hand, behind the body) ----------------
back_arm = sp.layer()
back_arm.poly('W', [(10, 21), (15, 21), (14, 30), (10, 31), (8, 26)])
back_arm.ell('s', 7, 29, 12, 34).px('S', (8, 33), (9, 33), (10, 33))

# ---------------- legs (white trousers, dark shoes) ----------------
leg_b = sp.layer()
leg_b.poly('w', [(14, 33), (20, 33), (17, 40), (14, 46), (8, 46), (11, 40)])
seg(leg_b, 'W', (14, 34), (10, 45)); seg(leg_b, 'W', (15, 34), (11, 41))
leg_b.poly('b', [(7, 45), (15, 45), (15, 50), (4, 50), (4, 47)]).h('B', 9, 13, 46)
leg_f = sp.layer()
leg_f.poly('w', [(21, 33), (27, 33), (30, 40), (31, 46), (25, 46), (24, 40)])
seg(leg_f, 'W', (22, 34), (24, 39)); leg_f.v('W', 25, 40, 45)
leg_f.poly('b', [(24, 45), (32, 45), (33, 47), (36, 48), (36, 50), (24, 50)]).h('B', 26, 31, 46)

# ---------------- torso: closed white jacket, dark buttons on the front edge ----------------
torso = sp.layer()
torso.poly('w', [(12, 21), (27, 21), (26, 27), (26, 35), (14, 35), (13, 27)])
torso.poly('W', [(12, 21), (15, 21), (16, 35), (14, 35), (13, 27)])            # back side in shade
torso.v('W', 23, 22, 35)                                                         # front edge of the jacket
torso.px('b', (24, 24), (24, 28), (24, 32))                                      # buttons
skirt = sp.layer()  # front flap of the long jacket over the front thigh
skirt.poly('w', [(22, 33), (27, 33), (30, 40), (25, 41), (23, 38)])
seg(skirt, 'W', (24, 34), (26, 40))

# ---------------- head ----------------
head = sp.layer()
head.rect('S', 18, 18, 22, 22)                                                   # neck
head.ell('h', 8, 1, 31, 19)
head.ell('h', 11, 0, 28, 10)                                                     # rounder, softer top
for pts in ([(10, 4), (8, 2), (13, 2)], [(23, 1), (27, 1), (27, 4)],
            [(9, 7), (6, 8), (9, 11)], [(8, 11), (5, 14), (9, 15)], [(9, 15), (8, 19), (13, 18)]):
    head.poly('h', pts)                                                          # droopy, messy outline
head.poly('s', [(15, 8), (29, 7), (31, 11), (31, 16), (27, 20), (20, 21), (16, 18), (14, 13)])  # face
for pts in ([(14, 6), (20, 6), (18, 11)], [(19, 6), (24, 6), (22, 11)], [(23, 6), (29, 6), (27, 10)],
            [(27, 6), (32, 7), (31, 11)], [(12, 6), (16, 6), (15, 13)]):
    head.poly('h', pts)                                                          # fringe falling down + sideburn
seg(head, 'H', (11, 4), (13, 9)); seg(head, 'H', (18, 2), (18, 7)); seg(head, 'H', (10, 12), (12, 17))
seg(head, 'H', (24, 3), (23, 7)); seg(head, 'H', (7, 9), (9, 12))
head.px('j', (15, 4), (16, 3), (21, 3))
head.rect('s', 16, 12, 17, 14).px('S', (16, 13), (16, 14))                       # ear
head.h('S', 17, 30, 11)                                                          # shade under the fringe
# soft, slightly sad brows; round tired eyes with dark circles under them
head.px('o', (19, 11), (20, 11), (25, 11), (26, 11), (27, 11))
head.h('o', 19, 21, 12).px('e', (19, 13)).px('k', (20, 13), (21, 13))
head.h('o', 24, 28, 12).px('e', (24, 13), (25, 13), (28, 13)).px('k', (26, 13), (27, 13)).px('e', (28, 13))
head.px('k', (26, 14), (27, 14)).px('e', (24, 14), (25, 14), (28, 14)).px('k', (20, 14), (21, 14)).px('e', (19, 14))
head.h('u', 19, 21, 15).h('u', 24, 28, 15)                                       # dark circles
head.px('S', (31, 15), (31, 16))                                                 # nose
head.h('m', 26, 27, 18)                                                          # small mouth
head.v('S', 17, 16, 18).h('S', 18, 20, 19)                                       # jaw shade (back side)

# ---------------- high collar ----------------
collar = sp.layer()
collar.poly('w', [(15, 17), (18, 19), (22, 20), (26, 18), (27, 22), (22, 24), (15, 23)])
collar.poly('W', [(15, 17), (18, 19), (18, 23), (15, 23)])
collar.px('b', (24, 21))

# ---------------- katana (held in front, blade angled forward-up) ----------------
katana = sp.layer()
katana.poly('g', [(30, 27), (41, 15), (44, 13), (43, 17), (33, 30)])
seg(katana, 'G', (33, 28), (42, 17)); seg(katana, 'G', (32, 28), (41, 17))
katana.poly('b', [(26, 32), (30, 28), (32, 30), (28, 34)])                       # black grip
katana.poly('t', [(29, 26), (31, 25), (34, 29), (33, 31)])                       # guard

# ---------------- front arm: both hands on the grip in front of the body ----------------
front = sp.layer()
front.poly('w', [(24, 21), (29, 21), (31, 25), (30, 30), (26, 31), (26, 26)])
seg(front, 'W', (25, 22), (27, 30))
front.ell('s', 27, 27, 32, 32).px('S', (28, 31), (29, 31))

for L in (tail, back_arm, leg_b, leg_f, torso, skirt, head, collar, katana, front):
    sp.add(L)
sp.save()
