"""Sung Jinwoo (Solo Leveling) - chibi redraw (see tools/chibi.py for the style guide; checklist in
refs/redraw/jinwoo/NOTES.md, built from the Season 2 character visual).
Short black hair with a swept fringe and tapered sides, narrow calm eyes glowing blue-violet, long open navy hooded
coat with pushed-up sleeves, white T-shirt, dark slim trousers, white sneakers, jagged red dagger with a gold guard
held low."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(14, 14, 28),                                    # outline
    h=(42, 44, 66), H=(18, 18, 32),                    # hair (blue-black) / strands
    s=(246, 212, 184), S=(206, 160, 134), m=(168, 104, 96),  # skin / shade / mouth
    e=(250, 250, 255), v=(126, 120, 255),              # eye white / glowing blue-violet iris
    n=(52, 58, 110), N=(30, 34, 70),                   # navy coat / shade
    w=(244, 246, 252), W=(178, 186, 208),              # white T-shirt + sneakers / shade
    p=(46, 36, 40), P=(24, 18, 22),                    # dark trousers / shade
    r=(176, 30, 44), R=(84, 16, 26), g=(226, 184, 72),  # dagger blade / dark edge / gold guard
)
sp = Sprite('jinwoo', W=44, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- long coat, back half, flaring behind to the calves ----------------
coat_back = sp.layer()
coat_back.poly('n', [(11, 21), (19, 21), (19, 36), (16, 46), (6, 47), (2, 45), (8, 33)])
coat_back.poly('N', [(2, 45), (8, 33), (11, 22), (13, 23), (11, 34), (7, 46)])     # inside of the coat in shade
seg(coat_back, 'N', (16, 30), (13, 45))

# ---------------- hood bunched behind the neck ----------------
hood = sp.layer()
hood.ell('n', 9, 15, 19, 24).poly('N', [(10, 18), (14, 16), (13, 23), (10, 22)])

# ---------------- legs: dark slim trousers, white sneakers ----------------
leg_b = sp.layer()
leg_b.poly('p', [(14, 33), (20, 33), (17, 40), (14, 46), (9, 46), (11, 40)])
seg(leg_b, 'P', (14, 34), (10, 45)); seg(leg_b, 'P', (15, 34), (12, 40))
leg_b.poly('w', [(8, 45), (15, 45), (15, 50), (4, 50), (5, 47)]).h('W', 4, 15, 50).h('W', 9, 14, 46)
leg_f = sp.layer()
leg_f.poly('p', [(21, 33), (27, 33), (29, 40), (30, 46), (25, 46), (24, 40)])
seg(leg_f, 'P', (22, 34), (24, 39)); leg_f.v('P', 25, 40, 45)
leg_f.poly('w', [(24, 45), (31, 45), (33, 47), (35, 48), (35, 50), (24, 50)]).h('W', 24, 35, 50).h('W', 26, 30, 46)

# ---------------- torso: white T-shirt ----------------
torso = sp.layer()
torso.poly('w', [(14, 21), (25, 21), (25, 28), (25, 34), (15, 34), (14, 28)])
torso.poly('W', [(14, 21), (17, 21), (17, 34), (15, 34)])                          # back side in shade
torso.h('W', 18, 24, 33)
torso.poly('s', [(18, 21), (22, 21), (20, 23)])                                    # neckline

# ---------------- coat, front parts: back-side lapel and the long near-side panel ----------------
coat_front = sp.layer()
coat_front.poly('n', [(12, 21), (17, 21), (17, 31), (15, 37), (12, 37)])
coat_front.v('N', 13, 22, 36)
coat_front.poly('n', [(23, 21), (27, 21), (28, 30), (30, 41), (26, 42), (24, 33)])
seg(coat_front, 'N', (24, 23), (26, 41))

# ---------------- head ----------------
head = sp.layer()
head.rect('s', 18, 17, 22, 22).v('S', 18, 17, 21)                                  # long neck
head.ell('h', 9, 1, 30, 16)                                                        # hair cap
head.poly('h', [(9, 7), (15, 7), (15, 16), (12, 17), (9, 14)])                    # short tapered back
for pts in ([(14, 2), (15, -1), (19, 1)], [(21, 1), (25, -1), (25, 2)], [(27, 3), (31, 3), (29, 5)]):
    head.poly('h', pts)                                                            # a few messy flicks on top
head.poly('s', [(15, 8), (29, 7), (31, 11), (31, 16), (28, 20), (25, 21), (20, 20), (17, 17), (15, 13)])  # face
head.rect('h', 13, 4, 30, 7)
for pts in ([(13, 6), (20, 6), (19, 10)], [(18, 6), (25, 6), (24, 11)], [(23, 6), (30, 6), (29, 10)],
            [(28, 5), (32, 6), (32, 9)]):
    head.poly('h', pts)                                                            # fringe swept down to the right
seg(head, 'H', (12, 4), (14, 9)); seg(head, 'H', (19, 2), (18, 6)); seg(head, 'H', (24, 6), (23, 10))
seg(head, 'H', (28, 6), (27, 8)); seg(head, 'H', (11, 10), (13, 15))
head.rect('s', 14, 11, 16, 14).px('S', (14, 12), (14, 13))                        # ear (sides are short)
head.h('S', 17, 30, 10).px('S', (18, 11), (25, 11))                                # shade under the fringe
# straight, low brows (calm); narrow eyes: heavy lid line + one row of white with a glowing iris
head.h('o', 18, 20, 11).h('o', 25, 28, 11)
head.h('o', 19, 21, 12).px('e', (19, 13)).px('v', (20, 13), (21, 13))
head.h('o', 24, 28, 12).px('e', (24, 13), (25, 13)).px('v', (26, 13), (27, 13)).px('e', (28, 13))
head.h('S', 19, 21, 14).h('S', 24, 28, 14)                                         # lower lid shade
head.px('S', (31, 15), (31, 16))                                                   # nose
head.h('m', 25, 27, 18)                                                            # neutral mouth
head.v('S', 17, 15, 17).h('S', 18, 21, 19)                                         # jaw shade (back side)

# ---------------- dagger held low, blade down: jagged red blade, gold guard ----------------
dagger = sp.layer()
dagger.poly('r', [(29, 36), (33, 36), (35, 40), (34, 43), (36, 45), (33, 48), (32, 44), (30, 41)])
seg(dagger, 'R', (30, 37), (33, 47))
dagger.rect('g', 28, 34, 34, 36)                                                   # guard

# ---------------- front arm: sleeve pushed to the elbow, bare forearm, hand on the grip ----------------
front = sp.layer()
front.poly('n', [(24, 21), (29, 21), (31, 28), (27, 29), (25, 25)])
seg(front, 'N', (25, 23), (27, 28))
front.poly('s', [(27, 28), (31, 27), (33, 32), (29, 33)]).px('S', (28, 29), (29, 31))
front.ell('s', 28, 30, 33, 35).h('S', 29, 32, 34)

for L in (coat_back, hood, leg_b, leg_f, torso, coat_front, head, dagger, front):
    sp.add(L)
sp.save()
