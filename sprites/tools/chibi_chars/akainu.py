"""Admiral Akainu (Sakazuki) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(40, 14, 14),                                   # outline
    s=(232, 168, 124), S=(184, 116, 82),              # skin / shade
    k=(46, 54, 86), K=(24, 28, 50),                   # Marine cap + dark shirt / shade, shoes
    r=(198, 38, 42), R=(128, 18, 28),                 # red suit / shade
    p=(252, 150, 192), P=(206, 86, 140),              # rose
    c=(250, 250, 246), C=(176, 188, 206),             # Marine coat / shade
    g=(240, 178, 44), G=(172, 108, 24),               # gold epaulettes
    e=(250, 246, 236),                                # eye white
    f=(255, 124, 30), F=(255, 228, 96),               # magma orange / yellow core
)
sp = Sprite('akainu', W=46, H=52, palette=PAL)

# ---------------- coat, back half ----------------
coat_b = sp.layer().poly('c', [(8, 19), (33, 19), (36, 28), (36, 32), (5, 32), (6, 28)])

# ---------------- legs ----------------
legs = sp.layer().poly('r', [(12, 32), (29, 32), (30, 47), (23, 47), (22, 37), (19, 37), (18, 47), (11, 47)])
legs.poly('R', [(11, 47), (12, 34), (14, 34), (14, 47)]).poly('R', [(22, 37), (23, 37), (24, 47), (23, 47)])
shoes = sp.layer().poly('K', [(10, 47), (18, 47), (18, 50), (9, 50)]).poly('K', [(22, 47), (30, 47), (32, 49), (32, 50), (22, 50)])

# ---------------- torso: red suit, dark shirt, pink rose ----------------
torso = sp.layer().poly('r', [(10, 21), (31, 21), (31, 26), (29, 33), (12, 33), (10, 26)])
torso.poly('k', [(18, 21), (23, 21), (21, 27), (20, 27)])
torso.line('R', [(17, 21), (20, 28)]).line('R', [(24, 21), (21, 28)])
torso.poly('R', [(10, 26), (10, 21), (13, 21), (14, 33), (12, 33)])
neck = sp.layer().rect('s', 17, 15, 24, 22).v('S', 17, 15, 22).h('S', 17, 24, 20)
rose = sp.layer().ell('p', 24, 21, 28, 25).px('P', (24, 24), (25, 25), (24, 23), (25, 24), (26, 25)).px('e', (26, 22))

# ---------------- coat fronts + epaulettes ----------------
coat_l = sp.layer().poly('c', [(6, 19), (13, 19), (14, 23), (12, 40), (4, 40), (5, 27)])
coat_l.poly('C', [(4, 40), (5, 27), (7, 22), (8, 40)])
coat_r = sp.layer().poly('c', [(28, 19), (35, 19), (37, 28), (37, 40), (31, 40), (29, 30)])
coat_r.v('C', 31, 31, 40).v('C', 30, 29, 31)
ep_l = sp.layer().ell('g', 5, 17, 14, 21).h('G', 5, 14, 21)
ep_r = sp.layer().ell('g', 27, 17, 36, 21).h('G', 27, 36, 21)

# ---------------- head: Marine cap with back flap, square grim face ----------------
head = sp.layer()
head.poly('s', [(13, 7), (30, 7), (31, 10), (31, 15), (29, 17), (26, 19), (17, 19), (14, 16), (13, 12)])
head.poly('k', [(9, 6), (10, 2), (14, 0), (26, 0), (29, 2), (30, 6)])          # cap crown
head.poly('k', [(9, 5), (15, 6), (15, 14), (9, 15)])                            # back flap over the nape
head.poly('K', [(14, 6), (31, 6), (33, 8), (14, 8)])                            # visor
head.h('K', 10, 29, 5).poly('K', [(9, 6), (11, 6), (11, 15), (9, 15)])         # band + flap shade
head.rect('c', 20, 2, 22, 3).px('g', (21, 2))                                   # emblem
head.ell('s', 13, 9, 16, 13).v('S', 14, 10, 12)                                 # ear
head.h('S', 16, 30, 9)                                                          # shade under the visor
head.h('K', 17, 20, 10).px('K', (21, 11), (20, 11)).h('K', 24, 28, 10).px('K', (23, 11), (24, 11))  # heavy brows
head.h('e', 18, 20, 12).px('o', (20, 12)).h('e', 24, 27, 12).px('o', (26, 12))  # narrow eyes
head.px('S', (30, 13), (30, 14)).h('R', 23, 27, 16).h('S', 24, 26, 17)                # nose, hard mouth
head.v('S', 16, 14, 17).px('S', (17, 18))                             # jaw shade

# ---------------- front arm with the magma fist ----------------
arm = sp.layer().poly('r', [(25, 26), (27, 32), (37, 32), (37, 26)]).h('R', 27, 37, 32).h('R', 26, 37, 31)
magma = sp.layer()
magma.poly('f', [(36, 24), (42, 24), (43, 25), (43, 32), (42, 33), (36, 33), (35, 32), (35, 25)])   # fist
magma.poly('f', [(35, 25), (36, 18), (38, 21), (40, 14), (43, 21), (43, 25)])                    # magma flaring up
magma.poly('R', [(35, 30), (38, 33), (35, 33)]).h('R', 36, 42, 33).v('R', 42, 28, 32)            # cooling crust
magma.ell('F', 36, 25, 40, 30).px('F', (40, 19), (40, 20), (39, 21), (41, 21))                  # yellow core

for L in (coat_b, legs, shoes, torso, neck, rose, coat_l, coat_r, ep_l, ep_r, head, arm):
    sp.add(L)
sp.add(magma, outline='R')
sp.save()
