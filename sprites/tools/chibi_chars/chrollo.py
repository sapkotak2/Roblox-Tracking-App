"""Chrollo Lucilfer (Hunter x Hunter) - chibi redraw (see tools/chibi.py for the style guide).
Checklist: refs/redraw/chrollo/NOTES.md (slicked-back black hair with spiky nape, purple ornate forehead cross, teal ball
earrings, calm round grey eyes, long purple-black coat with white fur collar + cuffs, gold buttons, crimson lining,
bare chest, X leg wraps, book)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(18, 12, 26),                                   # outline
    h=(40, 38, 58), H=(20, 18, 32),                   # blue-black hair, also trousers / boots
    s=(248, 224, 206), S=(208, 174, 158),             # pale skin
    e=(250, 250, 246), i=(104, 104, 118),             # eye white, grey iris
    c=(76, 50, 104), C=(44, 28, 64),                  # purple-black coat
    r=(156, 30, 64),                                  # crimson lining
    f=(248, 248, 252), F=(176, 180, 206),             # white fur; grey (fur shade, leg wraps)
    n=(232, 192, 64),                                 # gold buttons
    x=(40, 182, 160),                                 # teal earrings
    p=(150, 84, 172),                                 # purple forehead cross
    b=(156, 62, 42), B=(100, 36, 30),                 # red-brown book
)
sp = Sprite('chrollo', W=46, H=52, palette=PAL)

# ---------------- long coat, back part: flaps + crimson lining (behind the legs) ----------------
coat_back = sp.layer().poly('r', [(12, 30), (28, 30), (30, 45), (9, 45)])
coat_back.poly('C', [(10, 28), (15, 30), (14, 45), (6, 45), (8, 34)])                    # back flap in shade
coat_back.poly('c', [(26, 28), (31, 31), (34, 45), (27, 45), (26, 36)])                 # front flap
coat_back.v('C', 27, 37, 45).v('C', 14, 31, 45)

# ---------------- back arm: coat sleeve, white fur cuff, hand ----------------
back_arm = sp.layer().poly('c', [(7, 21), (12, 21), (11, 31), (6, 31)]).poly('C', [(7, 22), (9, 22), (8, 31), (6, 31)])
back_cuff = sp.layer().poly('f', [(5, 30), (12, 30), (12, 33), (5, 33)]).h('F', 5, 12, 33)
back_hand = sp.layer().ell('s', 6, 33, 10, 37).px('S', (7, 36), (8, 36))

# ---------------- legs: black trousers, grey criss-cross wraps, black boots with a gold mark ----------------
def leg(pts, x0):
    L = sp.layer().poly('h', pts)
    for y in range(39, 46):
        L.h('F', x0 - 1, x0 + 6, y)
    for k in range(6):                                   # one big X strap per shin
        L.px('H', (x0 + k, 39 + k), (x0 + 5 - k, 39 + k))
    return L
leg_b = leg([(13, 34), (19, 34), (18, 46), (13, 46)], 13).v('H', 13, 35, 38)
leg_f = leg([(21, 34), (27, 34), (28, 46), (23, 46)], 23).v('H', 22, 35, 38)
boot_b = sp.layer().poly('H', [(12, 46), (18, 46), (19, 50), (9, 50)]).px('n', (11, 48), (12, 48))
boot_f = sp.layer().poly('H', [(22, 46), (28, 46), (31, 50), (22, 50)]).px('n', (28, 48), (29, 48))

# ---------------- torso: open coat over the bare chest, gold buttons ----------------
torso = sp.layer()
torso.poly('c', [(10, 20), (29, 20), (30, 25), (28, 31), (28, 35), (11, 35), (11, 31), (9, 25)])
torso.poly('s', [(16, 20), (23, 20), (22, 33), (17, 33)])                               # bare chest
torso.h('S', 17, 19, 25).h('S', 20, 22, 25).v('S', 19, 27, 32).h('S', 18, 21, 29)      # pecs + abs, a few lines
torso.h('F', 16, 23, 33).h('F', 16, 23, 34)                                              # grey belt
torso.poly('C', [(10, 21), (13, 21), (13, 35), (11, 35), (11, 31), (10, 26)])           # back side in shade
torso.v('C', 15, 22, 35).v('C', 24, 22, 35)                                              # coat front edges
torso.px('n', (14, 24), (14, 28), (25, 24), (25, 28))                                    # gold buttons

# ---------------- big spiky white fur collar (flat block, a few big points) ----------------
collar = sp.layer()
collar.poly('f', [(8, 21), (7, 15), (11, 18), (12, 13), (15, 17), (18, 18), (16, 23), (14, 25), (9, 24)])
collar.poly('f', [(31, 21), (32, 15), (28, 18), (27, 13), (24, 17), (21, 18), (23, 23), (25, 25), (30, 24)])
collar.poly('F', [(8, 21), (12, 21), (14, 24), (9, 24)]).poly('F', [(25, 22), (30, 22), (30, 24), (25, 24)])
neck = sp.layer().rect('s', 16, 16, 23, 21).v('S', 16, 16, 21).h('S', 17, 22, 17)

# ---------------- head: hair slicked back, spiky nape, big open forehead with the purple cross ----------------
head = sp.layer()
head.ell('h', 8, 0, 28, 15)
for pts in ([(9, 7), (4, 9), (5, 11), (10, 12)], [(9, 11), (5, 15), (7, 16), (12, 15)], [(11, 13), (10, 18), (12, 18), (14, 15)]):
    head.poly('h', pts)                                                                  # spiky ends at the nape
head.poly('s', [(15, 4), (26, 2), (29, 6), (30, 12), (29, 16), (26, 19), (18, 19), (15, 15)])   # face, high forehead
head.poly('h', [(12, 3), (18, 0), (26, 0), (29, 3), (29, 4), (26, 2), (20, 2), (16, 4), (15, 9), (13, 12)])  # combed-back hairline
head.poly('H', [(8, 6), (12, 3), (14, 12), (10, 13)])                                    # back of the head in shade
head.px('H', (16, 2), (17, 2), (18, 1), (21, 1), (22, 1), (23, 1))                       # combed lines
head.px('s', (14, 11), (14, 12), (13, 12), (14, 13)).px('S', (15, 12), (15, 13))        # ear
head.v('p', 22, 3, 7).h('p', 20, 24, 5)                                                  # purple cross on the forehead
head.h('o', 17, 19, 7).h('o', 24, 27, 7)                                                 # thin straight brows
head.h('o', 17, 19, 9).h('o', 23, 27, 9)                                                 # upper lids
head.px('e', (17, 10), (17, 11)).px('i', (18, 10), (19, 10), (18, 11), (19, 11)).px('o', (19, 10))   # far eye: calm, round
head.px('e', (23, 10), (23, 11), (27, 10)).px('i', (24, 10), (25, 10), (26, 10), (24, 11), (25, 11), (26, 11))
head.px('o', (25, 10)).px('e', (27, 11))                                                 # near eye
head.px('S', (29, 13), (28, 14)).h('S', 24, 26, 16)                                      # nose, calm small mouth
head.px('S', (16, 17), (17, 18))                                                         # jaw shade
earring = sp.layer().ell('x', 12, 13, 15, 16).px('f', (13, 14))                          # teal ball earring

# ---------------- front arm holding the open book (Bandit's Secret) ----------------
front = sp.layer()
front.poly('c', [(26, 20), (31, 21), (33, 28), (28, 30), (27, 25)]).v('C', 28, 26, 29).v('C', 27, 22, 25)
front.poly('c', [(29, 26), (33, 24), (35, 28), (31, 30)])
cuff = sp.layer().poly('f', [(32, 23), (36, 22), (37, 28), (33, 29)]).px('F', (33, 28), (34, 28), (35, 28))
book = sp.layer().poly('b', [(34, 20), (43, 18), (43, 25), (34, 27)])                   # red-brown cover
book.poly('f', [(35, 20), (42, 18), (42, 23), (35, 25)]).v('F', 38, 19, 24).px('F', (39, 19), (39, 23))   # open pages, fold
book.h('B', 35, 42, 26).px('B', (43, 25), (42, 25))
hand = sp.layer().ell('s', 6, 33, 10, 37).px('S', (7, 36), (8, 36))

# ---------------- legs: black trousers, grey criss-cross wraps, black boots with a gold mark ----------------
def leg(pts, x0):
    L = sp.layer().poly('h', pts)
    for y in range(39, 46):
        L.h('F', x0 - 1, x0 + 6, y)
    for k in range(6):                                   # one big X strap per shin
        L.px('H', (x0 + k, 39 + k), (x0 + 5 - k, 39 + k))
    return L
leg_b = leg([(13, 34), (19, 34), (18, 46), (13, 46)], 13).v('H', 13, 35, 38)
leg_f = leg([(21, 34), (27, 34), (28, 46), (23, 46)], 23).v('H', 22, 35, 38)
boot_b = sp.layer().poly('H', [(12, 46), (18, 46), (19, 50), (9, 50)]).px('n', (11, 48), (12, 48))
boot_f = sp.layer().poly('H', [(22, 46), (28, 46), (31, 50), (22, 50)]).px('n', (28, 48), (29, 48))

# ---------------- torso: open coat over the bare chest, gold buttons ----------------
torso = sp.layer()
torso.poly('c', [(10, 20), (29, 20), (30, 25), (28, 31), (28, 35), (11, 35), (11, 31), (9, 25)])
torso.poly('s', [(16, 20), (23, 20), (22, 33), (17, 33)])                               # bare chest
torso.h('S', 17, 19, 25).h('S', 20, 22, 25).v('S', 19, 27, 32).h('S', 18, 21, 29)      # pecs + abs, a few lines
torso.h('F', 16, 23, 33).h('F', 16, 23, 34)                                              # grey belt
torso.poly('C', [(10, 21), (13, 21), (13, 35), (11, 35), (11, 31), (10, 26)])           # back side in shade
torso.v('C', 15, 22, 35).v('C', 24, 22, 35)                                              # coat front edges
torso.px('n', (14, 24), (14, 28), (25, 24), (25, 28))                                    # gold buttons

# ---------------- big spiky white fur collar (flat block, a few big points) ----------------
collar = sp.layer()
collar.poly('f', [(8, 21), (7, 15), (11, 18), (12, 13), (15, 17), (18, 18), (16, 23), (14, 25), (9, 24)])
collar.poly('f', [(31, 21), (32, 15), (28, 18), (27, 13), (24, 17), (21, 18), (23, 23), (25, 25), (30, 24)])
collar.poly('F', [(8, 21), (12, 21), (14, 24), (9, 24)]).poly('F', [(25, 22), (30, 22), (30, 24), (25, 24)])
neck = sp.layer().rect('s', 16, 16, 23, 21).v('S', 16, 16, 21).h('S', 17, 22, 17)

# ---------------- head: hair slicked back, spiky nape, big open forehead with the purple cross ----------------
head = sp.layer()
head.ell('h', 8, 0, 28, 15)
for pts in ([(9, 7), (4, 9), (5, 11), (10, 12)], [(9, 11), (5, 15), (7, 16), (12, 15)], [(11, 13), (10, 18), (12, 18), (14, 15)]):
    head.poly('h', pts)                                                                  # spiky ends at the nape
head.poly('s', [(15, 4), (26, 2), (29, 6), (30, 12), (29, 16), (26, 19), (18, 19), (15, 15)])   # face, high forehead
head.poly('h', [(12, 3), (18, 0), (26, 0), (29, 3), (29, 4), (26, 2), (20, 2), (16, 4), (15, 9), (13, 12)])  # combed-back hairline
head.poly('H', [(8, 6), (12, 3), (14, 12), (10, 13)])                                    # back of the head in shade
head.px('H', (16, 2), (17, 2), (18, 1), (21, 1), (22, 1), (23, 1))                       # combed lines
head.px('s', (14, 11), (14, 12), (13, 12), (14, 13)).px('S', (15, 12), (15, 13))        # ear
head.v('p', 22, 3, 7).h('p', 20, 24, 5)                                                  # purple cross on the forehead
head.h('o', 17, 19, 7).h('o', 24, 27, 7)                                                 # thin straight brows
head.h('o', 17, 19, 9).h('o', 23, 27, 9)                                                 # upper lids
head.px('e', (17, 10), (17, 11)).px('i', (18, 10), (19, 10), (18, 11), (19, 11)).px('o', (19, 10))   # far eye: calm, round
head.px('e', (23, 10), (23, 11), (27, 10)).px('i', (24, 10), (25, 10), (26, 10), (24, 11), (25, 11), (26, 11))
head.px('o', (25, 10)).px('e', (27, 11))                                                 # near eye
head.px('S', (29, 13), (28, 14)).h('S', 24, 26, 16)                                      # nose, calm small mouth
head.px('S', (16, 17), (17, 18))                                                         # jaw shade
earring = sp.layer().ell('x', 12, 13, 15, 16).px('f', (13, 14))                          # teal ball earring

# ---------------- front arm holding the open book (Bandit's Secret) ----------------
front = sp.layer()
front.poly('c', [(26, 20), (31, 21), (33, 28), (28, 30), (27, 25)]).v('C', 28, 26, 29).v('C', 27, 22, 25)
front.poly('c', [(29, 26), (33, 24), (35, 28), (31, 30)])
cuff = sp.layer().poly('f', [(32, 23), (36, 22), (37, 28), (33, 29)]).px('F', (33, 28), (34, 28), (35, 28))
book = sp.layer().poly('b', [(34, 22), (42, 20), (43, 25), (36, 27)])                   # cover seen from below/side
book.poly('f', [(34, 21), (38, 19), (42, 19), (42, 21), (38, 22), (35, 23)]).v('F', 38, 19, 21)   # open pages on top
book.h('B', 36, 42, 25).px('B', (37, 26), (36, 26))
hand = sp.layer().ell('s', 34, 24, 38, 28).px('S', (35, 27), (36, 27))

for L in (coat_back, back_arm, back_cuff, back_hand, leg_b, leg_f, boot_b, boot_f, torso, neck, collar, head, earring,
          front, cuff, book, hand):
    sp.add(L)
sp.save()
