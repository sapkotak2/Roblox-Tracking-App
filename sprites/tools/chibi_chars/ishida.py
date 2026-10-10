"""Uryu Ishida (Bleach) - chibi redraw (see tools/chibi.py for the style guide; checklist in
refs/redraw/ishida/NOTES.md, built from the Brave Souls Hueco Mundo art and the anime close-up).
Sleek blue-black hair with parted bangs and long side locks to the chin, thin silver rectangular glasses, sharp
blue eyes, white Quincy outfit with a short white cape over the shoulders, blue belt and a small blue cross,
Ginrei Kojaku spirit bow (cyan ring round the hand with long pointed limbs)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(22, 26, 50),                                    # outline (dark navy)
    h=(42, 46, 88), H=(20, 22, 48),                    # hair (blue-black) / strands
    s=(248, 224, 202), S=(212, 176, 156), m=(170, 112, 108),  # skin / shade / mouth
    e=(252, 252, 255), k=(52, 96, 200),                # eye white / blue iris
    f=(150, 162, 194),                                 # thin silver glasses frame
    w=(244, 246, 252), W=(180, 190, 214),              # white outfit / shade
    n=(40, 112, 176), g=(214, 176, 80),                # blue belt, trim and cross / gold cape cord
    c=(120, 220, 255), C=(232, 252, 255), q=(30, 140, 220),  # spirit bow: glow / core / glowing outline
)
sp = Sprite('ishida', W=46, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- legs: white trousers, white shoes ----------------
leg_b = sp.layer()
leg_b.poly('w', [(14, 33), (20, 33), (17, 40), (14, 46), (9, 46), (11, 40)])
seg(leg_b, 'W', (14, 34), (10, 45)); seg(leg_b, 'W', (15, 34), (12, 40))
leg_b.poly('W', [(8, 45), (15, 45), (15, 50), (4, 50), (5, 47)]).h('n', 4, 15, 50)
leg_f = sp.layer()
leg_f.poly('w', [(21, 33), (27, 33), (29, 40), (30, 46), (25, 46), (24, 40)])
seg(leg_f, 'W', (22, 34), (24, 39)); leg_f.v('W', 25, 40, 45)
leg_f.poly('w', [(24, 45), (31, 45), (33, 47), (35, 48), (35, 50), (24, 50)]).h('W', 26, 30, 46).h('n', 24, 35, 50)

# ---------------- torso: white tunic with a short skirt, blue belt ----------------
torso = sp.layer()
torso.poly('w', [(13, 21), (26, 21), (26, 30), (28, 37), (12, 37), (13, 30)])
torso.poly('W', [(13, 21), (16, 21), (16, 37), (12, 37), (13, 30)])                # back side in shade
torso.h('n', 13, 26, 31).h('n', 13, 26, 32)                                         # blue belt
seg(torso, 'W', (21, 33), (21, 36)); seg(torso, 'W', (25, 33), (26, 36))            # skirt pleats

# ---------------- head ----------------
head = sp.layer()
head.rect('s', 18, 17, 22, 21).v('S', 18, 17, 20)                                   # neck
head.ell('h', 9, 0, 30, 16)                                                         # sleek rounded top
head.poly('h', [(9, 7), (16, 7), (17, 20), (14, 21), (10, 19), (8, 13)])           # straight hair falling to the chin
head.poly('s', [(17, 8), (29, 7), (31, 11), (31, 15), (28, 19), (25, 21), (21, 20), (18, 17), (16, 13)])  # narrow face, pointed chin
head.poly('h', [(13, 4), (21, 4), (20, 7), (18, 10), (17, 8)])                      # bangs, parted at x 21
head.poly('h', [(21, 4), (31, 5), (32, 11), (29, 9), (25, 8)])
head.poly('h', [(15, 7), (18, 7), (18, 19), (17, 21)])                              # long lock down the far cheek
seg(head, 'H', (12, 5), (14, 12)); seg(head, 'H', (17, 9), (18, 18)); seg(head, 'H', (21, 3), (21, 5))
seg(head, 'H', (11, 13), (12, 19)); seg(head, 'H', (26, 4), (30, 7))
head.h('S', 19, 31, 10).px('S', (19, 11))                                           # shade under the bangs
# serious brows angled down to the nose; sharp eyes with blue irises
head.px('o', (20, 10), (21, 11), (25, 11), (26, 10), (27, 10), (28, 10))
head.h('o', 20, 22, 12).px('e', (20, 13)).px('k', (21, 13), (22, 13))
head.h('o', 24, 28, 12).px('e', (24, 13), (25, 13)).px('k', (26, 13), (27, 13)).px('e', (28, 13))
# thin silver rectangular glasses: top bar, bottom bar, bridge, arm to the ear
head.h('f', 19, 22, 14).h('f', 24, 29, 14).px('f', (23, 13), (29, 13))
head.px('S', (31, 15))                                                              # nose
head.h('m', 25, 26, 17)                                                             # small serious mouth
head.h('S', 19, 21, 18)                                                             # jaw shade

# ---------------- short white cape over the shoulders, high collar ----------------
cape = sp.layer()
cape.poly('w', [(12, 19), (25, 19), (29, 22), (28, 26), (21, 28), (16, 33), (9, 33), (8, 26)])
cape.poly('W', [(12, 19), (14, 19), (14, 27), (16, 33), (9, 33), (8, 26)])         # back side in shade
seg(cape, 'W', (16, 23), (13, 32)); cape.h('W', 18, 27, 26)
cape.v('n', 20, 21, 24).h('n', 19, 21, 22)                                         # small blue Quincy cross
seg(cape, 'g', (17, 22), (22, 25)); seg(cape, 'g', (22, 25), (26, 23))            # gold cord holding the cape
collar = sp.layer()
collar.poly('w', [(16, 16), (19, 18), (23, 19), (26, 17), (27, 21), (22, 22), (16, 21)])
collar.poly('W', [(16, 16), (19, 18), (19, 21), (16, 21)])

# ---------------- Ginrei Kojaku: cyan ring round the front hand + long pointed limbs ----------------
bow = sp.layer()
bow.poly('c', [(35, 21), (38, 21), (38, 9), (37, 7)])                               # upper limb
bow.poly('c', [(35, 29), (38, 29), (38, 41), (37, 43)])                             # lower limb
bow.ell('c', 31, 20, 42, 30)
bow.d.ellipse((34, 23, 39, 27), fill=(0, 0, 0, 0))                                   # hollow ring
bow.v('C', 37, 10, 20).v('C', 37, 30, 40)
bow.px('C', (33, 22), (32, 24), (32, 25), (33, 27), (40, 22), (41, 24), (41, 25), (40, 27))

# ---------------- front arm: reaching forward into the ring ----------------
front = sp.layer()
front.poly('w', [(24, 21), (29, 21), (34, 23), (34, 27), (28, 28), (26, 26)])
seg(front, 'W', (25, 23), (33, 27))
front.v('n', 33, 23, 27)                                                            # blue cuff
front.ell('s', 33, 22, 38, 27).h('S', 34, 37, 27)

for L in (leg_b, leg_f, torso, head, cape, collar):
    sp.add(L)
sp.add(bow, outline='q')
sp.add(front)
sp.save()
