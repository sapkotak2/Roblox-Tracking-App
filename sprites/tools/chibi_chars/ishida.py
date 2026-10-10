"""Uryu Ishida (Bleach) - chibi redraw (see tools/chibi.py for the style guide).
Black hair with a long fringe and parted bangs, rectangular glasses, WHITE Quincy outfit with blue trim and a small
blue cross, glowing light-blue spirit bow in the front hand."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(22, 26, 46),                                    # outline (dark navy)
    h=(46, 50, 74), H=(22, 24, 40), j=(118, 130, 172),  # hair base / strands / shine
    s=(246, 216, 190), S=(208, 168, 146),              # skin / shade
    e=(250, 250, 255), k=(38, 60, 120), m=(164, 100, 96), f=(96, 104, 134),  # eye white, iris, mouth, glasses frame
    w=(244, 246, 252), W=(178, 188, 212),              # white outfit / shade
    n=(46, 96, 206),                                   # blue trim + cross
    c=(130, 214, 255), C=(226, 250, 255), q=(40, 120, 214),  # spirit bow: glow / core / glowing outline
)
sp = Sprite('ishida', W=46, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- long coat tail behind the legs, blue hem ----------------
tail = sp.layer()
tail.poly('w', [(12, 30), (20, 30), (19, 39), (14, 43), (7, 44), (9, 36)])
tail.poly('W', [(7, 44), (9, 36), (12, 31), (14, 33), (12, 43)])
seg(tail, 'n', (8, 43), (14, 42)); seg(tail, 'n', (8, 42), (14, 41)); tail.px('n', (15, 41), (16, 40))

# ---------------- back arm (hangs behind the body) ----------------
back_arm = sp.layer()
back_arm.poly('W', [(10, 21), (15, 21), (14, 30), (10, 31), (8, 26)])
back_arm.h('n', 9, 14, 30)
back_arm.ell('s', 7, 30, 12, 35).px('S', (8, 34), (9, 34), (10, 34))

# ---------------- legs (white trousers, white shoes with blue soles) ----------------
leg_b = sp.layer()
leg_b.poly('w', [(14, 33), (20, 33), (17, 40), (14, 46), (8, 46), (11, 40)])
seg(leg_b, 'W', (14, 34), (10, 45)); seg(leg_b, 'W', (15, 34), (11, 41))
leg_b.poly('W', [(7, 45), (15, 45), (15, 50), (4, 50), (4, 47)]).h('n', 5, 14, 49)
leg_f = sp.layer()
leg_f.poly('w', [(21, 33), (27, 33), (30, 40), (31, 46), (25, 46), (24, 40)])
seg(leg_f, 'W', (22, 34), (24, 39)); leg_f.v('W', 25, 40, 45)
leg_f.poly('w', [(24, 45), (32, 45), (33, 47), (36, 48), (36, 50), (24, 50)]).h('W', 25, 35, 48).h('n', 25, 35, 49)

# ---------------- torso: white top, blue trim down the front edge, small blue cross ----------------
torso = sp.layer()
torso.poly('w', [(12, 21), (27, 21), (26, 27), (26, 35), (14, 35), (13, 27)])
torso.poly('W', [(12, 21), (15, 21), (16, 35), (14, 35), (13, 27)])
torso.v('n', 21, 22, 34)                                                        # front trim
torso.h('n', 14, 25, 33)                                                        # belt trim
torso.v('n', 24, 24, 28).h('n', 23, 25, 25)                                     # Quincy cross
skirt = sp.layer()
skirt.poly('w', [(21, 33), (27, 33), (30, 40), (25, 41), (22, 38)])
seg(skirt, 'n', (23, 34), (25, 39)); skirt.h('n', 25, 29, 40)

# ---------------- head ----------------
head = sp.layer()
head.rect('S', 18, 18, 22, 22)                                                  # neck
head.ell('h', 8, 1, 31, 19)
head.ell('h', 11, 0, 29, 12)                                                    # smooth rounded top
head.poly('h', [(9, 8), (15, 8), (15, 20), (12, 21), (8, 19), (7, 13)])        # straight hair falling at the back
head.poly('s', [(15, 8), (29, 7), (31, 11), (31, 16), (27, 20), (20, 21), (16, 18), (14, 13)])  # face
# parted bangs: part at x 21, one side sweeps left, the other right; long lock down the far cheek
head.poly('h', [(13, 5), (22, 5), (20, 8), (17, 11), (16, 9)])
head.poly('h', [(21, 5), (32, 6), (32, 10), (28, 9), (24, 8)])
head.poly('h', [(13, 7), (17, 7), (17, 19), (15, 21), (14, 14)])               # long lock on the far side
seg(head, 'H', (12, 6), (13, 10)); seg(head, 'H', (10, 12), (11, 19)); seg(head, 'H', (16, 9), (16, 18)); seg(head, 'H', (21, 4), (21, 6))
seg(head, 'H', (13, 13), (13, 19)); seg(head, 'H', (25, 4), (29, 6))
head.px('j', (17, 3), (18, 3), (24, 3))
head.h('S', 18, 30, 10).px('S', (18, 11), (22, 9), (23, 9))                     # shade under the bangs
# calm brows, eyes inside rectangular glasses
head.h('o', 19, 21, 11).h('o', 25, 28, 11)
head.h('f', 18, 22, 12).h('f', 18, 22, 15).v('f', 18, 12, 15).v('f', 22, 12, 15)   # far lens frame
head.h('f', 24, 30, 12).h('f', 24, 30, 15).v('f', 24, 12, 15).v('f', 30, 12, 15)   # near lens frame
head.px('f', (23, 13))                                                          # bridge
head.px('e', (19, 13), (19, 14)).px('k', (20, 13), (20, 14), (21, 13), (21, 14))
head.px('e', (25, 13), (25, 14), (26, 13), (26, 14), (29, 13), (29, 14)).px('k', (27, 13), (27, 14), (28, 13), (28, 14))
head.px('S', (31, 16))                                                          # nose
head.h('m', 26, 27, 18)                                                         # small mouth
head.h('S', 18, 20, 19)                                                         # jaw shade

# ---------------- high collar with blue trim ----------------
collar = sp.layer()
collar.poly('w', [(15, 17), (18, 19), (22, 20), (26, 18), (27, 22), (22, 24), (15, 23)])
collar.poly('W', [(15, 17), (18, 19), (18, 23), (15, 23)])
collar.h('n', 17, 25, 22)

# ---------------- front arm: reaching forward, holding the bow ----------------
front = sp.layer()
front.poly('w', [(24, 21), (29, 21), (34, 23), (34, 28), (28, 28), (26, 26)])
seg(front, 'W', (25, 23), (33, 27))
front.v('n', 33, 23, 28)                                                        # cuff
front.ell('s', 34, 22, 39, 28).px('S', (35, 28), (36, 28))

# ---------------- spirit bow: glowing arc + string ----------------
bow = sp.layer()
bow.d.arc((20, 11, 41, 41), -72, 72, fill=sp.C('c'), width=4)
bow.d.arc((21, 12, 40, 40), -66, 66, fill=sp.C('C'), width=1)
string = sp.layer()
string.line('C', [(33, 13), (33, 39)])

for L in (tail, back_arm, leg_b, leg_f, torso, skirt, head, collar):
    sp.add(L)
sp.add(string, outlined=False)
sp.add(bow, outline='q')
sp.add(front)
sp.save()
