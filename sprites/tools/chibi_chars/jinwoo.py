"""Sung Jinwoo (Solo Leveling) - chibi redraw (see tools/chibi.py for the style guide).
Short messy black hair, glowing violet eyes, long black high-collared coat over dark clothes, black boots,
one black dagger held low in the front hand."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(12, 10, 20),                                    # outline
    h=(46, 44, 62), H=(22, 20, 32), j=(104, 108, 142),  # hair base / strands / shine
    s=(244, 206, 176), S=(206, 156, 128),              # skin / shade
    e=(250, 248, 255), v=(150, 70, 240), V=(214, 170, 255), m=(150, 82, 76),  # eye white, violet iris, glow, mouth
    c=(74, 76, 100), C=(48, 50, 68),                   # coat / coat shade
    i=(96, 100, 126),                                 # inner shirt (grey, so the coat opening reads)
    p=(40, 40, 56), P=(24, 24, 36), B=(74, 76, 100),   # trousers / trouser shade + boots / boot shine
    d=(30, 28, 40), D=(150, 152, 176),                 # dagger blade / edge
)
sp = Sprite('jinwoo', W=44, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- coat tail flaring behind the legs ----------------
tail = sp.layer()
tail.poly('c', [(12, 30), (20, 30), (19, 38), (13, 43), (6, 44), (9, 36)])
tail.poly('C', [(6, 44), (9, 36), (12, 31), (14, 33), (11, 43)])
seg(tail, 'C', (16, 34), (15, 41))

# ---------------- back arm (hangs behind the body, fist by the hip) ----------------
back_arm = sp.layer()
back_arm.poly('C', [(10, 21), (15, 21), (14, 30), (10, 31), (8, 26)])
back_arm.ell('s', 7, 29, 12, 34).px('S', (8, 33), (9, 33), (10, 33))

# ---------------- legs ----------------
leg_b = sp.layer()  # back leg, steps back-left
leg_b.poly('p', [(14, 33), (20, 33), (17, 40), (14, 46), (8, 46), (11, 40)])
seg(leg_b, 'P', (14, 34), (10, 45)); seg(leg_b, 'P', (15, 34), (11, 41))
leg_b.poly('P', [(7, 45), (15, 45), (15, 50), (4, 50), (4, 47)]).h('B', 9, 13, 46)
leg_f = sp.layer()  # front leg, knee bent forward
leg_f.poly('p', [(21, 33), (27, 33), (30, 40), (31, 46), (25, 46), (24, 40)])
seg(leg_f, 'P', (22, 34), (24, 39)); leg_f.v('P', 25, 40, 45)
leg_f.poly('P', [(24, 45), (32, 45), (33, 47), (36, 48), (36, 50), (24, 50)]).h('B', 26, 31, 46)

# ---------------- torso: coat body with an open front showing the grey shirt, belt ----------------
torso = sp.layer()
torso.poly('c', [(12, 21), (27, 21), (26, 27), (26, 34), (14, 34), (13, 27)])
torso.poly('i', [(20, 21), (23, 21), (23, 32), (20, 32)])                       # shirt in the opening
torso.poly('C', [(12, 21), (15, 21), (16, 34), (14, 34), (13, 27)])             # back side in shade
torso.v('C', 19, 22, 33).v('C', 25, 24, 33)                                     # coat edges / fold
torso.h('P', 14, 26, 33).h('P', 14, 26, 34).px('v', (21, 33), (22, 33))         # belt + small violet buckle
coat_skirt = sp.layer()  # short front flap over the front thigh
coat_skirt.poly('c', [(24, 33), (28, 33), (30, 39), (26, 40)])
seg(coat_skirt, 'C', (25, 34), (27, 39))

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 8, 1, 31, 19)
for pts in ([(10, 6), (5, 3), (13, 3)], [(13, 3), (12, -1), (18, 2)], [(18, 2), (23, -1), (24, 3)],
            [(23, 3), (30, 0), (29, 5)], [(28, 5), (34, 5), (30, 9)], [(9, 9), (4, 10), (9, 13)],
            [(9, 13), (5, 17), (12, 17)]):
    head.poly('h', pts)
head.poly('s', [(15, 8), (29, 7), (31, 11), (31, 16), (27, 20), (20, 21), (16, 18), (14, 13)])  # face
for pts in ([(14, 6), (21, 6), (17, 10)], [(20, 6), (26, 6), (23, 9)], [(25, 6), (32, 7), (29, 10)],
            [(12, 6), (16, 6), (15, 12)]):
    head.poly('h', pts)                                                       # fringe spikes + sideburn
seg(head, 'H', (11, 4), (13, 9)); seg(head, 'H', (18, 2), (17, 6)); seg(head, 'H', (10, 12), (12, 16))
seg(head, 'H', (25, 3), (24, 6))
head.px('j', (15, 3), (16, 3), (21, 2))
head.rect('s', 16, 12, 17, 14).px('S', (16, 14), (16, 13))                    # ear
head.h('S', 17, 29, 10)                                                       # shade under the fringe
# sharp angled brows (inner ends low), narrow eyes: far eye small, near eye big, violet iris + glow pixel
head.px('o', (18, 10), (19, 10), (20, 11), (21, 11), (24, 11), (25, 11), (26, 10), (27, 10), (28, 10))
head.h('o', 19, 21, 12).px('e', (19, 13)).px('v', (20, 13), (20, 14), (21, 14)).px('V', (21, 13))
head.h('o', 24, 28, 12).px('e', (24, 13), (25, 13), (28, 13)).px('v', (26, 13), (26, 14), (27, 14)).px('V', (27, 13))
head.px('S', (31, 14), (31, 15))                                              # nose
head.h('m', 26, 28, 17)                                                       # flat mouth
head.v('S', 17, 16, 18).h('S', 18, 20, 19)                                    # jaw shade (back side)

# ---------------- high collar (in front of the neck) ----------------
collar = sp.layer()
collar.poly('c', [(15, 17), (18, 19), (22, 20), (26, 18), (27, 22), (22, 24), (15, 23)])
collar.poly('C', [(15, 17), (18, 19), (18, 23), (15, 23)])
collar.h('v', 21, 25, 22)                                                     # small violet accent on the collar

# ---------------- front arm: hangs low and forward, black dagger pointing forward-down ----------------
front = sp.layer()
front.poly('c', [(24, 21), (29, 21), (32, 26), (33, 31), (29, 32), (27, 26)])
seg(front, 'C', (26, 22), (29, 31))
front.ell('s', 29, 29, 34, 34).px('S', (30, 33), (31, 33))
dagger = sp.layer()
dagger.poly('d', [(34, 31), (36, 31), (42, 38), (42, 40), (40, 40), (34, 34)])
seg(dagger, 'D', (35, 32), (40, 38))
dagger.rect('d', 31, 30, 33, 34)                                              # grip through the fist
dagger.rect('B', 33, 30, 34, 35)                                              # small guard
dagger.px('v', (32, 31))

for L in (tail, back_arm, leg_b, leg_f, torso, coat_skirt, head, collar, front, dagger):
    sp.add(L)
sp.save()
