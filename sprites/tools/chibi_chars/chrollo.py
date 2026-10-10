"""Chrollo Lucilfer (Hunter x Hunter) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(16, 14, 24),                                   # outline
    h=(46, 46, 62), H=(26, 26, 36), l=(110, 112, 140),  # black slicked-back hair (+ shine)
    s=(246, 214, 190), S=(208, 166, 142),             # pale skin
    e=(252, 250, 244),                                # eye white
    c=(56, 50, 76), C=(34, 30, 48),                   # black long coat (purple-black)
    f=(246, 246, 250), F=(184, 188, 206),             # white fur trim
    d=(92, 92, 112),                                  # dark top
    b=(162, 56, 42), B=(104, 32, 28),                 # red-brown book
    x=(90, 160, 230),                                 # blue earring
)
sp = Sprite('chrollo', W=42, H=52, palette=PAL)

# ---------------- long coat tails (behind the legs, open in the middle) ----------------
tail_b = sp.layer().poly('C', [(10, 28), (15, 32), (14, 44), (5, 44), (8, 33)])
tail_f = sp.layer().poly('c', [(26, 28), (31, 31), (35, 44), (27, 44), (26, 34)]).poly('C', [(26, 34), (29, 36), (29, 44), (27, 44)])

# ---------------- back arm (coat sleeve hanging behind) ----------------
back_arm = sp.layer().poly('c', [(7, 21), (12, 21), (11, 31), (6, 31)]).poly('C', [(7, 22), (9, 22), (8, 31), (6, 31)])
back_cuff = sp.layer().rect('f', 5, 30, 11, 32).h('F', 5, 11, 32)
back_hand = sp.layer().ell('s', 6, 32, 10, 36).px('S', (7, 35), (8, 35))

# ---------------- legs ----------------
leg_b = sp.layer().poly('c', [(13, 34), (19, 34), (18, 47), (12, 47)]).v('C', 13, 36, 46).v('C', 14, 36, 46)
leg_f = sp.layer().poly('c', [(21, 34), (27, 34), (29, 47), (23, 47)]).v('C', 23, 38, 46)
shoe_b = sp.layer().poly('H', [(11, 46), (18, 46), (19, 50), (9, 50)])
shoe_f = sp.layer().poly('H', [(22, 46), (29, 46), (32, 50), (22, 50)]).px('l', (29, 47), (30, 48))

# ---------------- torso: dark top + open coat front, narrowing to the waist ----------------
torso = sp.layer()
torso.poly('c', [(10, 20), (29, 20), (30, 25), (28, 31), (28, 36), (11, 36), (11, 31), (9, 25)])
torso.poly('d', [(17, 20), (23, 20), (23, 36), (17, 36)])
torso.poly('C', [(10, 21), (13, 21), (13, 36), (11, 36), (11, 31), (10, 26)])          # back side in shade
torso.h('C', 17, 23, 34)                                                                # waistband shadow

# ---------------- white fur collar, running down the lapels: flat blocks ----------------
collar = sp.layer()
collar.poly('f', [(7, 19), (14, 16), (25, 16), (32, 19), (32, 23), (25, 24), (24, 30), (22, 30), (21, 22),
                  (19, 22), (18, 30), (16, 30), (15, 24), (7, 23)])
collar.poly('F', [(7, 22), (15, 23), (16, 25), (7, 23)]).h('F', 25, 32, 23).v('F', 16, 23, 30).v('F', 22, 23, 30)
collar.poly('s', [(17, 17), (23, 17), (22, 21), (18, 21)]).v('S', 17, 17, 21).h('S', 18, 21, 18)   # neck

# ---------------- head: hair slicked back, open forehead with the cross ----------------
head = sp.layer()
head.ell('h', 8, 0, 29, 17)
head.poly('h', [(10, 2), (3, 7), (7, 9), (2, 13), (9, 15), (12, 17)])                  # swept-back points
head.poly('s', [(14, 5), (22, 3), (28, 4), (30, 8), (30, 15), (27, 19), (17, 19), (14, 15)])  # face + forehead
head.poly('h', [(13, 3), (19, 0), (27, 0), (30, 3), (29, 4), (25, 2), (19, 4), (16, 7), (14, 10)])  # hairline combed back
head.poly('H', [(8, 6), (13, 4), (13, 14), (9, 15)])                                     # back of head in shade
head.px('H', (17, 2), (18, 2), (19, 2), (20, 1), (22, 2), (23, 2), (24, 1), (25, 1))       # combed-back strand lines
head.px('l', (11, 2), (12, 2), (13, 1))                                                  # shine
head.px('s', (14, 11), (14, 12)).px('S', (15, 12), (14, 13))                              # ear
head.px('x', (14, 14)).put('x', (14, 14))                                                # earring
head.v('o', 22, 4, 7).h('o', 21, 23, 5)                                                  # cross mark (forehead centre)
head.h('o', 17, 19, 8).h('o', 23, 26, 8)                                                 # brows
head.px('e', (17, 10), (18, 10), (19, 10), (17, 11), (18, 11)).px('o', (19, 10), (19, 11))      # far eye
head.px('e', (23, 10), (24, 10), (25, 10), (26, 10), (23, 11), (24, 11)).px('o', (25, 10), (25, 11), (26, 11))  # near eye
head.px('S', (29, 13), (28, 14)).h('S', 25, 27, 16)                                      # nose, calm mouth
head.v('S', 15, 14, 16).px('S', (16, 17), (17, 18))                                       # jaw shade

# ---------------- front arm holding the book (Bandit's Secret) ----------------
front = sp.layer()
front.poly('c', [(26, 20), (31, 21), (33, 29), (28, 30), (27, 25)]).v('C', 28, 26, 29).v('C', 27, 22, 25)
front.poly('c', [(29, 26), (33, 24), (34, 28), (31, 30)])
cuff = sp.layer().poly('f', [(32, 23), (35, 22), (36, 28), (33, 29)]).px('F', (33, 28), (34, 28), (35, 27))
book = sp.layer().rect('b', 34, 18, 40, 27).v('B', 34, 18, 27).v('f', 40, 19, 26).h('B', 35, 39, 27)
book.h('B', 36, 38, 20).h('B', 36, 38, 25)                                               # cover emblem bars
hand = sp.layer().ell('s', 34, 23, 38, 27).px('S', (35, 26), (36, 26))

for L in (tail_b, tail_f, back_arm, back_cuff, back_hand, leg_b, leg_f, shoe_b, shoe_f, torso, collar, head,
          front, cuff, book, hand):
    sp.add(L)
sp.save()
