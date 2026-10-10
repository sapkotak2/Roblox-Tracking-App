"""Izuku Midoriya / Deku (My Hero Academia) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(16, 26, 24),                                   # outline
    h=(44, 122, 74), H=(20, 60, 40),                   # dark green hair
    s=(252, 214, 176), S=(222, 158, 120),             # skin (shade also = freckles)
    e=(255, 255, 250), g=(36, 150, 84), k=(24, 30, 28), m=(112, 40, 40),   # eye white, green iris, dark, mouth
    c=(52, 136, 140), C=(30, 90, 100),                # hero suit
    w=(244, 244, 238), W=(184, 190, 192),             # gloves / belt / soles
    r=(226, 44, 44), R=(150, 22, 30),                 # red shoes
    l=(150, 255, 110),                                # green lightning
)
sp = Sprite('deku', W=42, H=52, palette=PAL)


def lock(L, t1, t2, b1, b2, k='h'):
    """hair clump with a blunt 2-px tip"""
    L.poly(k, [t1, t2, b2, b1])
    return L


# ---------------- back arm (upper arm behind the torso) ----------------
arm_b = sp.layer()
arm_b.poly('c', [(11, 21), (15, 21), (13, 28), (8, 28), (8, 25)]).v('C', 9, 25, 27).v('C', 10, 23, 27)
arm_b.rect('w', 6, 26, 11, 31).h('W', 6, 11, 31).v('W', 6, 27, 30).h('k', 7, 9, 29)              # gloved fist at the hip

# ---------------- legs: slim, clear gap, red shoes ----------------
leg_b = sp.layer()
leg_b.poly('c', [(14, 32), (20, 32), (18, 40), (16, 46), (10, 46), (12, 39)]).v('C', 12, 40, 45).v('C', 13, 38, 45)
leg_b.h('k', 11, 18, 39).h('k', 11, 18, 40)                                       # black kneepad
leg_f = sp.layer()
leg_f.poly('c', [(21, 32), (26, 32), (29, 39), (30, 46), (24, 46), (23, 39)]).v('C', 24, 40, 45).v('C', 25, 41, 45)
leg_f.h('k', 23, 29, 38).h('k', 23, 29, 39)
shoe_b = sp.layer().poly('r', [(9, 45), (16, 45), (18, 48), (18, 50), (7, 50), (8, 47)])
shoe_b.v('R', 9, 46, 48).h('w', 7, 18, 49).h('W', 7, 18, 50).h('k', 12, 15, 46)  # sole + strap line
shoe_f = sp.layer().poly('r', [(24, 45), (30, 45), (33, 48), (33, 50), (23, 50), (23, 47)])
shoe_f.v('R', 24, 46, 48).h('w', 23, 33, 49).h('W', 23, 33, 50).h('k', 26, 29, 46)

# ---------------- torso: suit narrowing to the waist, black straps, belt ----------------
torso = sp.layer()
torso.poly('c', [(13, 21), (26, 21), (27, 25), (25, 33), (14, 33), (12, 25)])
torso.poly('C', [(13, 22), (16, 22), (16, 33), (14, 33), (13, 26)])
torso.h('W', 13, 26, 30).h('w', 13, 26, 31).rect('k', 19, 30, 20, 31)            # belt + buckle
torso.rect('s', 17, 18, 21, 22).h('S', 17, 21, 19).v('S', 17, 18, 22)             # neck
torso.h('C', 16, 22, 22)                                                          # collar
torso.rect('k', 16, 22, 17, 29).rect('k', 22, 22, 23, 29)                         # black suit straps

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 8, 2, 31, 19)
# messy bushy clumps all around
for t1, t2, b1, b2 in (((10, 0), (12, 0), (8, 6), (16, 3)), ((17, 0), (19, -1), (14, 4), (23, 3)),
                       ((25, 0), (27, 1), (21, 3), (30, 6)), ((33, 4), (33, 6), (27, 4), (30, 11)),
                       ((4, 3), (4, 5), (12, 4), (10, 10)), ((3, 10), (3, 12), (9, 8), (9, 15)),
                       ((5, 18), (7, 19), (9, 13), (13, 18))):
    lock(head, t1, t2, b1, b2)
head.poly('s', [(14, 9), (29, 9), (30, 12), (29, 16), (26, 19), (17, 19), (14, 16)])   # face
for pts in ([(12, 6), (19, 6), (15, 11)], [(18, 6), (24, 6), (21, 10)], [(23, 6), (31, 7), (28, 11)],
            [(12, 7), (15, 7), (14, 15)]):
    head.poly('h', pts)                                                           # fringe clumps
for pts in ([(14, 3), (16, 3), (16, 8)], [(21, 3), (23, 3), (22, 7)], [(28, 4), (30, 5), (27, 8)],
            [(9, 6), (12, 6), (13, 10)], [(8, 11), (9, 9), (12, 12)], [(9, 15), (10, 13), (12, 17)]):
    head.poly('H', pts)                                                       # dark gaps between the curly clumps
head.px('g', (16, 4), (17, 4))                                           # shine
head.v('S', 15, 11, 15).px('S', (16, 10), (17, 10), (22, 10), (23, 10), (27, 10))                                        # face shade under the fringe
# big round green eyes, brows, freckles
head.h('k', 18, 20, 11).h('k', 23, 26, 11)                                       # brows
head.h('o', 18, 20, 12).px('e', (18, 13), (18, 14)).rect('g', 19, 13, 20, 14).px('k', (20, 13))
head.h('o', 23, 27, 12).px('e', (23, 13), (24, 13), (27, 13), (23, 14), (24, 14), (27, 14))
head.rect('g', 25, 13, 26, 14).px('k', (26, 13))
head.px('S', (18, 16), (23, 16), (26, 16))                                        # freckles
head.px('S', (28, 14))                                                            # nose
head.h('m', 23, 25, 17)                                         # determined grin

# ---------------- front arm: punching forward, white glove ----------------
arm_f = sp.layer()
arm_f.poly('c', [(24, 21), (29, 21), (34, 23), (34, 27), (28, 27), (25, 26)]).h('C', 25, 33, 26)
arm_f.rect('k', 29, 22, 30, 26)                                                   # black elbow band
arm_f.rect('w', 33, 21, 38, 27).h('W', 33, 38, 27).v('W', 33, 22, 26).px('W', (37, 24), (36, 24))
sparks = sp.layer()       # two small outlined lightning bolts around the charged fist
for bolt in ([(39, 15), (40, 16), (39, 17), (40, 18), (41, 19)], [(36, 29), (37, 30), (36, 31), (37, 32)]):
    cs = set(bolt)
    sparks.put('o', *[(x + dx, y + dy) for x, y in bolt for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) not in cs])
    sparks.put('l', *bolt)

for L in (leg_b, leg_f, shoe_b, shoe_f, torso, arm_b, head, arm_f):
    sp.add(L)
sp.add(sparks, outlined=False)
sp.save()
