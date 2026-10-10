"""Admiral Akainu (Sakazuki) - chibi redraw (see tools/chibi.py for the style guide).
Checked against refs/redraw/akainu/NOTES.md (pre-timeskip official art)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(36, 14, 14),                                   # outline
    s=(204, 140, 98), S=(150, 94, 62),                # dark tan skin / shade + face lines
    h=(28, 22, 24),                                   # black hair, brows, pupils, shoes
    c=(250, 250, 246), C=(178, 188, 206), n=(70, 80, 118),   # white (cap, coat, eyes) / shade / navy cap stripes + coat lining
    t=(40, 150, 150),                                 # teal cap patch
    r=(150, 28, 38), R=(96, 14, 24),                  # maroon suit / shade, magma crust
    f=(222, 54, 44), O=(250, 150, 48),                # red Hawaiian shirt / orange flowers + magma
    p=(248, 170, 200), P=(176, 92, 168),              # pink rose / rose shade + purple tattoo
    g=(240, 186, 56), G=(176, 116, 28),               # gold buttons, fringed epaulettes
    F=(255, 232, 100),                                # magma hot core
)
sp = Sprite('akainu', W=46, H=52, palette=PAL)

# ---------------- coat back: dark lining inside ----------------
coat_b = sp.layer().poly('n', [(8, 19), (33, 19), (36, 28), (36, 42), (5, 42), (6, 28)])

# ---------------- legs ----------------
legs = sp.layer().poly('r', [(12, 32), (29, 32), (30, 47), (23, 47), (22, 37), (19, 37), (18, 47), (11, 47)])
legs.poly('R', [(11, 47), (12, 34), (14, 34), (14, 47)]).poly('R', [(22, 37), (23, 37), (24, 47), (23, 47)])
shoes = sp.layer().poly('h', [(10, 47), (18, 47), (18, 50), (9, 50)]).poly('h', [(22, 47), (30, 47), (32, 49), (32, 50), (22, 50)])

# ---------------- torso: maroon double-breasted suit, open red flower shirt ----------------
torso = sp.layer().poly('r', [(10, 20), (31, 20), (31, 26), (29, 33), (12, 33), (10, 26)])
torso.poly('R', [(10, 26), (10, 20), (13, 20), (14, 33), (12, 33)])
torso.poly('f', [(14, 20), (27, 20), (24, 25), (21, 28), (20, 28), (17, 25)])   # open red flower shirt
torso.poly('s', [(18, 20), (23, 20), (21, 26), (20, 26)])                       # bare chest in the V
torso.px('O', (15, 21), (16, 22), (25, 21), (26, 21), (24, 23), (17, 24))      # orange flowers
torso.px('g', (16, 28), (25, 28), (16, 31), (25, 31))                           # gold buttons
neck = sp.layer().rect('s', 18, 15, 23, 21).v('S', 18, 15, 21).h('S', 18, 23, 18)
neck.px('P', (22, 19), (23, 19), (22, 20), (23, 21))                            # purple tattoo
rose = sp.layer().ell('p', 23, 22, 28, 27).px('P', (23, 25), (24, 26), (25, 24), (26, 25)).px('c', (26, 23))

# ---------------- coat fronts + fringed gold epaulettes ----------------
coat_l = sp.layer().poly('c', [(6, 19), (13, 19), (14, 23), (12, 41), (4, 41), (5, 27)])
coat_l.poly('C', [(4, 41), (5, 27), (7, 22), (8, 41)]).rect('f', 4, 31, 7, 33)                      # red sleeve cuff
coat_r = sp.layer().poly('c', [(28, 19), (35, 19), (37, 28), (37, 41), (30, 41), (29, 30)])
coat_r.v('n', 30, 30, 41).px('g', (32, 34), (32, 38))
ep_l = sp.layer().poly('g', [(6, 17), (13, 17), (14, 18), (14, 23), (5, 23), (5, 18)]).h('G', 5, 14, 20)
ep_r = sp.layer().poly('g', [(28, 17), (35, 17), (36, 18), (36, 23), (27, 23), (27, 18)]).h('G', 27, 36, 20)
for x in (6, 8, 10, 12):
    ep_l.v('G', x, 21, 23)
for x in (28, 30, 32, 34):
    ep_r.v('G', x, 21, 23)

# ---------------- head: white Marine cap, long hard face, heavy frown ----------------
head = sp.layer()
head.poly('s', [(14, 7), (31, 7), (32, 10), (33, 12), (32, 15), (31, 17), (28, 19), (18, 19), (15, 16), (14, 12)])
head.poly('h', [(10, 6), (16, 6), (16, 12), (11, 13)])                          # short black hair at the side
head.ell('s', 12, 8, 15, 12).v('S', 13, 9, 11)                                  # ear
head.poly('c', [(10, 6), (10, 2), (14, 0), (27, 0), (30, 2), (31, 6)])          # cap crown
head.poly('c', [(15, 5), (32, 5), (34, 7), (15, 7)])                            # visor
head.h('C', 15, 34, 7).poly('C', [(10, 2), (12, 1), (13, 6), (10, 6)])          # visor underside, back of the cap
head.v('n', 18, 0, 3).v('n', 20, 0, 3)                                          # navy stripes over the crown
head.rect('t', 22, 2, 28, 4)                                                    # teal patch
head.h('S', 16, 31, 8).h('S', 19, 21, 12).h('S', 25, 27, 12)                    # shadow under the brim, deep-set eyes
head.px('h', (18, 9), (19, 9), (20, 10), (21, 10)).px('h', (24, 10), (25, 9), (26, 9), (27, 9), (28, 9))  # brows pulled down
head.v('S', 22, 9, 11).v('S', 23, 9, 10)                                        # crease between the brows
head.h('c', 19, 20, 11).px('h', (20, 11)).h('c', 25, 27, 11).px('h', (26, 11))  # small hard eyes
head.px('S', (32, 12), (32, 13)).line('S', [(30, 14), (30, 16)])               # nose, deep cheek line
head.h('R', 23, 28, 16).px('R', (22, 17), (29, 17))                             # hard downturned mouth
head.v('S', 16, 13, 16).px('S', (17, 17))                                       # jaw shade

# ---------------- front arm with the magma fist ----------------
arm = sp.layer().poly('r', [(25, 26), (27, 32), (37, 32), (37, 26)]).h('R', 27, 37, 32).h('R', 26, 37, 31)
magma = sp.layer()
magma.ell('O', 34, 23, 43, 33).ell('O', 36, 19, 41, 25).ell('O', 39, 21, 44, 27)   # lumpy molten fist
magma.rect('O', 35, 32, 37, 37).rect('O', 40, 32, 42, 35)                          # drips
magma.poly('R', [(34, 28), (38, 33), (34, 33)]).h('R', 38, 42, 33).v('R', 43, 25, 29)  # cooling crust
magma.ell('F', 36, 25, 40, 29).px('F', (38, 21), (39, 22), (41, 23), (36, 35))         # yellow hot spots

for L in (coat_b, legs, shoes, torso):
    sp.add(L)
sp.add(neck, skip=('bottom',))
for L in (coat_l, coat_r, ep_l, ep_r, rose, head, arm):
    sp.add(L)
sp.add(magma, outline='R')
sp.save()
