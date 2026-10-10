"""Baki Hanma (Baki) - reference redraw for the chibi framework (see tools/chibi.py for the style guide).
Shirtless and very muscular (V-taper), shaggy dark reddish-brown hair, scowling red-brown eyes, gritted teeth, maroon shorts with a white waistband, white wrist and ankle
wraps, bare feet, fists-up fighting stance facing right."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(44, 14, 10),                                    # outline
    h=(100, 46, 36), H=(62, 26, 20),                   # dark reddish-brown hair / strand lines
    s=(230, 160, 110), S=(182, 104, 64),               # skin / shade
    e=(252, 248, 240), k=(190, 52, 40), m=(110, 34, 28),  # eye white, red-brown iris, mouth
    r=(152, 24, 36), R=(98, 12, 22),                   # maroon shorts / shade
    w=(244, 244, 236), W=(176, 184, 176),              # wraps + waistband / shade
)
sp = Sprite('baki', W=42, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- back arm, upper part (behind the torso, elbow down-left) ----------------
back_upper = sp.layer()
back_upper.poly('S', [(7, 21), (13, 21), (13, 29), (9, 31), (6, 27)])

# ---------------- legs: bare, long, with a gap, ankle wraps and bare feet ----------------
leg_b = sp.layer()  # back leg, steps back-left
leg_b.poly('s', [(13, 36), (20, 36), (17, 42), (15, 46), (9, 46), (11, 41)])
seg(leg_b, 'S', (13, 37), (10, 45)); seg(leg_b, 'S', (14, 37), (11, 42))
leg_b.h('w', 9, 15, 44).h('W', 9, 15, 45)
leg_b.poly('s', [(8, 46), (15, 46), (15, 50), (4, 50), (5, 48)]).h('S', 4, 15, 50)
leg_f = sp.layer()  # front leg, knee forward
leg_f.poly('s', [(21, 36), (28, 36), (31, 41), (31, 46), (25, 46), (24, 41)])
seg(leg_f, 'S', (22, 37), (24, 41)); leg_f.v('S', 25, 42, 45)
leg_f.h('w', 25, 31, 44).h('W', 25, 31, 45)
leg_f.poly('s', [(25, 46), (31, 46), (33, 48), (36, 49), (36, 50), (25, 50)]).h('S', 25, 36, 50)

# ---------------- shorts: compact, white waistband ----------------
shorts = sp.layer()
shorts.poly('r', [(13, 31), (27, 31), (28, 36), (28, 38), (21, 38), (20, 36), (19, 38), (12, 38), (12, 35)])
shorts.h('w', 13, 27, 32).h('W', 13, 27, 33)
shorts.v('R', 13, 34, 38).v('R', 14, 34, 38).v('R', 20, 35, 37).h('R', 22, 27, 37)

# ---------------- torso: V-taper, wide delts, narrow waist ----------------
torso = sp.layer()
torso.poly('s', [(14, 19), (25, 19), (31, 22), (29, 27), (26, 32), (15, 32), (12, 27), (9, 22)])
torso.ell('s', 7, 19, 14, 27).ell('s', 25, 19, 33, 27)                       # deltoids
torso.poly('S', [(8, 21), (11, 20), (12, 27), (15, 32), (13, 32), (10, 27)])  # back side in shade
torso.h('S', 14, 18, 26).h('S', 20, 27, 26)                                   # under the pecs
torso.v('S', 19, 22, 32)                                                      # centre line
torso.h('S', 16, 18, 29).h('S', 20, 24, 29)                                   # one ab line
torso.rect('s', 16, 16, 23, 20).v('S', 16, 16, 19)                            # thick neck

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 6, 1, 32, 20)
for pts in ([(8, 8), (3, 7), (11, 3)], [(13, 2), (16, -1), (20, 1)], [(22, 1), (27, 0), (28, 4)],
            [(28, 4), (34, 6), (31, 9)], [(7, 11), (3, 14), (8, 17)], [(8, 16), (6, 21), (12, 19)]):
    head.poly('h', pts)                                                       # shaggy, voluminous, messy tips
head.poly('s', [(15, 8), (29, 7), (31, 11), (31, 17), (29, 20), (19, 21), (16, 18), (14, 13)])  # square jaw
for pts in ([(13, 6), (20, 6), (18, 11)], [(19, 6), (25, 6), (22, 11)], [(24, 6), (31, 6), (29, 10)],
            [(29, 6), (33, 8), (31, 11)], [(12, 6), (16, 6), (16, 14)]):
    head.poly('h', pts)                                                       # clumps of bangs over the forehead
seg(head, 'H', (8, 5), (12, 9)); seg(head, 'H', (20, 2), (18, 6)); seg(head, 'H', (6, 13), (10, 16))
seg(head, 'H', (27, 2), (26, 5)); seg(head, 'H', (21, 7), (22, 10))
head.rect('s', 16, 13, 17, 15).px('S', (16, 14), (16, 15))                    # ear
head.h('S', 17, 30, 10)                                                       # shadow under the bangs
# thick scowling brows angled down to the nose; glaring eyes with red-brown irises, small whites
head.px('o', (18, 10), (19, 10), (20, 10), (20, 11), (21, 11), (24, 11), (25, 11), (25, 10), (26, 10), (27, 10), (28, 10))
head.h('o', 19, 21, 12).px('e', (19, 13)).px('k', (20, 13), (21, 13), (20, 14), (21, 14)).px('S', (19, 14))
head.h('o', 24, 28, 12).px('e', (24, 13), (28, 13)).px('k', (25, 13), (26, 13), (27, 13), (26, 14), (27, 14))
head.px('S', (24, 14), (25, 14), (28, 14))
head.px('S', (31, 15), (31, 16), (30, 17))                                    # nose
head.px('m', (24, 18), (27, 18)).px('e', (25, 18), (26, 18))                  # gritted teeth
head.px('S', (29, 15), (28, 16))                                              # small cheek scar
head.v('S', 17, 16, 18).h('S', 18, 21, 19)                                    # jaw shade (back side)

# ---------------- back arm, forearm rising across the body + fist guarding the chin ----------------
back_fore = sp.layer()
back_fore.poly('s', [(7, 27), (12, 25), (18, 24), (19, 27), (12, 31), (8, 31)]).h('S', 9, 12, 30)
back_fore.rect('w', 16, 23, 19, 24).rect('W', 16, 25, 19, 26)                 # wrist wrap
back_fore.ell('s', 16, 17, 23, 24).h('S', 17, 22, 23).px('S', (18, 20), (20, 20))

# ---------------- front arm: elbow down, forearm up, fist raised forward ----------------
front = sp.layer()
front.poly('s', [(28, 21), (33, 21), (36, 29), (32, 31), (30, 26)]).v('S', 29, 23, 25).px('S', (30, 26), (31, 27))
front.poly('s', [(33, 22), (38, 22), (38, 25), (36, 31), (32, 31), (32, 27)]).v('S', 33, 25, 30)
front.rect('w', 32, 21, 38, 21).rect('W', 32, 22, 38, 22)                     # wrist wrap
front.ell('s', 32, 14, 39, 21).h('S', 33, 38, 20).px('S', (34, 17), (36, 17))

for L in (back_upper, leg_b, leg_f, torso, shorts, head, back_fore, front):
    sp.add(L)
sp.save()
