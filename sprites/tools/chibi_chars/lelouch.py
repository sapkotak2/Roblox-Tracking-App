"""Lelouch vi Britannia as Zero, helmet off (Code Geass) - chibi redraw (see tools/chibi.py for the style guide).
Black hair with bangs, purple eyes with the left (far) eye glowing red with Geass, dark purple suit with a high
collar and gold trim, black cape with red lining flowing behind, arm thrust forward."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(18, 12, 26),                                    # outline
    h=(46, 42, 64), H=(22, 18, 34), j=(116, 112, 150),  # hair base / strands / shine
    s=(248, 218, 194), S=(210, 168, 150),              # skin / shade
    e=(252, 250, 255), p=(130, 70, 200), r=(220, 34, 50), m=(160, 96, 96),  # eye white, purple iris, red (Geass + lining), mouth
    d=(84, 56, 126), D=(52, 34, 82),                   # purple suit / shade
    g=(236, 194, 78),                                  # gold trim
    c=(42, 38, 54), C=(24, 22, 32),                    # black cape / shade (also boots)
    R=(140, 18, 36),                                   # red lining shade
)
sp = Sprite('lelouch', W=46, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- cape flowing behind: black outside, red lining showing on the flared edge ----------------
cape = sp.layer()
cape.poly('c', [(12, 19), (22, 19), (22, 32), (19, 45), (8, 47), (1, 46), (4, 36), (8, 26)])
cape.poly('r', [(1, 46), (4, 36), (8, 26), (11, 21), (12, 26), (9, 36), (8, 45)])     # lining on the flared edge
cape.poly('R', [(1, 46), (4, 36), (8, 26), (9, 25), (6, 36), (4, 45)])
seg(cape, 'C', (15, 24), (13, 44)); seg(cape, 'C', (19, 30), (17, 44))              # two folds

# ---------------- legs (dark purple trousers, black boots) ----------------
leg_b = sp.layer()
leg_b.poly('D', [(14, 33), (20, 33), (18, 40), (15, 46), (9, 46), (12, 40)])
leg_b.poly('C', [(8, 44), (16, 44), (16, 50), (5, 50), (5, 47)]).h('c', 10, 14, 45)
leg_f = sp.layer()
leg_f.poly('d', [(21, 33), (26, 33), (29, 40), (30, 46), (24, 46), (23, 40)])
seg(leg_f, 'D', (22, 34), (24, 39)); leg_f.v('D', 24, 40, 45)
leg_f.poly('C', [(23, 44), (31, 44), (32, 47), (35, 48), (35, 50), (23, 50)]).h('c', 25, 30, 45)

# ---------------- torso: slim purple tunic, gold trim down the front and at the waist ----------------
torso = sp.layer()
torso.poly('d', [(13, 21), (26, 21), (25, 27), (25, 35), (15, 35), (14, 27)])
torso.poly('D', [(13, 21), (16, 21), (17, 35), (15, 35), (14, 27)])                 # back side in shade
torso.v('g', 22, 22, 35).h('g', 15, 24, 32)                                         # gold trim
torso.v('D', 23, 24, 31)
skirt = sp.layer()  # tunic flap over the front thigh
skirt.poly('d', [(21, 33), (26, 33), (29, 39), (24, 40), (22, 37)])
seg(skirt, 'g', (22, 34), (24, 39)); skirt.h('g', 24, 28, 39)

# ---------------- head ----------------
head = sp.layer()
head.rect('S', 18, 18, 22, 22)                                                      # neck
head.ell('h', 9, 1, 31, 19)
head.ell('h', 12, 0, 29, 12)
head.poly('h', [(9, 8), (15, 8), (15, 20), (12, 21), (8, 18), (7, 12)])            # hair at the back, to the nape
head.poly('s', [(15, 8), (29, 7), (31, 11), (31, 16), (27, 20), (20, 21), (16, 18), (14, 13)])  # face
# swooping bangs ending in sharp points
for pts in ([(14, 5), (21, 5), (18, 11)], [(19, 5), (25, 5), (22, 10)], [(23, 5), (30, 5), (27, 10)],
            [(28, 5), (32, 7), (31, 11)], [(13, 6), (17, 6), (16, 19)]):
    head.poly('h', pts)
seg(head, 'H', (12, 4), (13, 10)); seg(head, 'H', (10, 11), (12, 18)); seg(head, 'H', (19, 2), (17, 8))
seg(head, 'H', (25, 3), (23, 7))
head.px('j', (20, 2), (21, 2), (15, 3))
head.h('S', 18, 30, 10).px('S', (19, 11), (23, 11), (24, 11))                       # shade under the bangs
# brows; far (left) eye glows red with Geass, near eye purple
head.h('o', 19, 21, 11).h('o', 25, 28, 11)
head.h('o', 19, 21, 12).px('e', (19, 13)).px('r', (20, 13), (21, 13), (20, 14), (21, 14)).px('e', (19, 14))
head.h('o', 24, 28, 12).px('e', (24, 13), (25, 13), (28, 13), (24, 14), (25, 14), (28, 14))
head.px('p', (26, 13), (27, 13), (26, 14), (27, 14))
head.px('S', (31, 15), (31, 16))                                                    # nose
head.h('m', 26, 27, 18)                                                             # mouth
head.h('S', 18, 20, 19)                                                             # jaw shade

# ---------------- high Zero collar with gold edge ----------------
collar = sp.layer()
collar.poly('d', [(14, 15), (18, 18), (22, 20), (26, 18), (28, 22), (22, 24), (14, 23)])
collar.poly('D', [(14, 15), (18, 18), (18, 23), (14, 23)])
collar.h('g', 15, 27, 22).px('g', (26, 19), (27, 20), (27, 21))

# ---------------- back arm: a sliver of the cape-covered shoulder ----------------
# (the back arm is hidden by the cape)

# ---------------- front arm: thrust forward, open hand giving a command ----------------
front = sp.layer()
front.poly('d', [(24, 21), (29, 21), (35, 23), (35, 27), (29, 27), (26, 26)])
seg(front, 'D', (25, 24), (34, 26)); seg(front, 'D', (26, 25), (29, 26))
front.v('g', 33, 23, 27)                                                            # gold cuff
front.poly('s', [(34, 20), (38, 19), (40, 20), (40, 27), (35, 28)])                 # open palm thrust forward
front.h('S', 35, 39, 27).px('S', (38, 22), (38, 23), (38, 25))                      # finger lines

for L in (cape, leg_b, leg_f, torso, skirt, head, collar, front):
    sp.add(L)
sp.save()
