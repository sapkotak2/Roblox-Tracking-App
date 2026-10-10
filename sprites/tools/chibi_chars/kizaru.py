"""Admiral Kizaru (Borsalino) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(34, 24, 18),                                   # outline
    s=(238, 182, 132), S=(196, 130, 88),              # skin / shade
    h=(70, 56, 48), H=(30, 22, 20),                   # hair (also shoes) / strands
    y=(248, 210, 64), Y=(204, 150, 32),               # yellow suit / shade
    w=(255, 250, 222),                                # suit stripes, glow core
    c=(250, 250, 246), C=(176, 188, 206),             # Marine coat / shade
    g=(236, 160, 40), G=(170, 98, 22),                # gold epaulettes, amber lenses
    k=(42, 46, 74),                                   # dark shirt
    m=(150, 72, 62),                                  # mouth
)
sp = Sprite('kizaru', W=44, H=52, palette=PAL)

# ---------------- coat, back half (hangs behind the body) ----------------
coat_b = sp.layer().poly('c', [(10, 19), (30, 19), (33, 28), (33, 32), (7, 32), (7, 28)])

# ---------------- legs (long striped trousers) ----------------
legs = sp.layer().poly('y', [(14, 32), (26, 32), (27, 47), (22, 47), (20, 37), (18, 47), (13, 47)])
for x in (16, 23, 26):
    legs.v('w', x, 33, 47)
legs.poly('Y', [(13, 47), (14, 34), (15, 34), (15, 47)])
legs.poly('Y', [(20, 37), (21, 37), (22, 47), (21, 47)])
shoes = sp.layer().poly('h', [(12, 47), (18, 47), (18, 50), (11, 50)]).poly('h', [(21, 47), (27, 47), (29, 49), (29, 50), (21, 50)])
shoes.h('H', 11, 18, 50).h('H', 21, 29, 50)

# ---------------- torso: striped jacket, dark shirt V ----------------
torso = sp.layer().poly('y', [(13, 21), (27, 21), (27, 26), (26, 33), (14, 33), (13, 26)])
for x in (17, 23, 26):
    torso.v('w', x, 20, 33)
torso.poly('k', [(18, 21), (22, 21), (20, 26)])
torso.poly('Y', [(13, 26), (13, 21), (15, 21), (15, 33), (14, 33)])
neck = sp.layer().rect('s', 18, 15, 22, 22).v('S', 18, 15, 22).h('S', 18, 22, 19)

# ---------------- coat fronts draped over the shoulders + epaulettes ----------------
coat_l = sp.layer().poly('c', [(8, 19), (15, 19), (16, 23), (14, 40), (6, 40), (7, 27)])
coat_l.poly('C', [(6, 40), (7, 27), (9, 22), (10, 40)])
coat_r = sp.layer().poly('c', [(25, 19), (31, 19), (34, 28), (34, 40), (28, 40), (26, 30)])
coat_r.v('C', 28, 31, 40).v('C', 27, 29, 31)
ep_l = sp.layer().poly('g', [(9, 17), (15, 17), (16, 18), (16, 21), (8, 21), (8, 18)]).h('G', 8, 16, 21)
ep_r = sp.layer().poly('g', [(25, 17), (31, 17), (32, 18), (32, 21), (24, 21), (24, 18)]).h('G', 24, 32, 21)

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 7, 0, 28, 16)
head.poly('s', [(15, 5), (28, 4), (31, 7), (32, 12), (30, 15), (26, 18), (19, 18), (16, 15), (15, 11)])
head.poly('h', [(9, 2), (18, 0), (27, 1), (31, 4), (31, 6), (23, 5), (17, 6), (15, 8), (14, 11)])  # slicked-back hairline
head.ell('s', 11, 8, 15, 13).v('S', 12, 9, 12)                                                     # ear
head.rect('h', 16, 7, 17, 14).px('h', (18, 13), (18, 14))                                         # sideburn
for pts in ([(12, 3), (24, 2)], [(9, 6), (16, 4)], [(8, 12), (9, 7)]):
    head.line('H', pts)                                                                            # combed-back strands
head.h('S', 18, 29, 6).px('S', (17, 15), (18, 16), (19, 17))          # shade under hairline, jaw
head.h('H', 19, 21, 8).h('H', 24, 29, 8)                                                           # brows
head.rect('g', 19, 9, 21, 11).rect('g', 24, 9, 28, 11)                                             # round amber shades
head.h('G', 19, 21, 11).h('G', 24, 28, 11).px('o', (22, 10), (23, 10), (18, 10)).px('w', (27, 9))
head.px('S', (31, 12), (31, 13)).h('m', 25, 28, 16)                                               # nose, pursed mouth

# ---------------- front arm: comes out of the coat opening, index finger up with a small light glow ----------------
arm = sp.layer()
arm.poly('y', [(23, 27), (27, 32), (36, 26), (33, 21)])                 # sleeve, from inside the coat up to the front
arm.line('Y', [(24, 29), (27, 31)]).line('Y', [(27, 31), (34, 26)])
arm.ell('s', 34, 20, 38, 24).px('S', (34, 23), (35, 24), (36, 24))     # hand
arm.rect('s', 36, 16, 38, 21)                                           # raised index finger
glow = sp.layer().ell('y', 35, 11, 39, 15).px('w', (37, 13), (36, 13), (38, 13), (37, 12), (37, 14))

for L in (coat_b, legs, shoes, torso, neck, coat_l, coat_r, ep_l, ep_r, head, arm):
    sp.add(L)
sp.add(glow, outline='g')
sp.save()
