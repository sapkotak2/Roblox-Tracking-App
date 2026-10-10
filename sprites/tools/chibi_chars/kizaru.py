"""Admiral Kizaru (Borsalino) - chibi redraw (see tools/chibi.py for the style guide).
Checked against refs/redraw/kizaru/NOTES.md (official anime art)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(34, 24, 20),                                   # outline
    s=(226, 168, 118), S=(176, 116, 76),              # tan skin / shade
    h=(44, 34, 32),                                   # short dark hair, sideburns, goatee
    y=(214, 160, 44), Y=(158, 106, 26), w=(250, 228, 120),   # gold suit / shade / pale-yellow stripes + glow
    k=(38, 86, 80), v=(186, 140, 222),                # dark teal shirt, lavender tie
    c=(250, 250, 248), C=(178, 188, 208), n=(86, 90, 116),   # coat white / shade / dark lining
    p=(246, 230, 136), P=(196, 164, 64),              # pale-gold fringed epaulettes, cuffs, coat buttons
    a=(236, 132, 56), m=(110, 40, 32),                # orange sunglass lenses; mouth / eyes behind the lenses
)
sp = Sprite('kizaru', W=44, H=52, palette=PAL)

# ---------------- coat back: dark lining seen inside the open coat ----------------
coat_b = sp.layer().poly('n', [(9, 20), (31, 20), (34, 28), (34, 44), (6, 44), (6, 28)])
collar = sp.layer()                                                    # tall upturned collar beside the neck
collar.poly('c', [(7, 9), (9, 9), (12, 13), (18, 18), (18, 22), (8, 21)]).poly('c', [(36, 9), (31, 14), (24, 18), (24, 22), (34, 21)])
collar.poly('C', [(7, 9), (9, 9), (11, 13), (11, 21), (8, 21)]).poly('C', [(36, 9), (35, 21), (33, 21), (33, 13)])

# ---------------- legs: long pinstriped trousers, white shoes ----------------
legs = sp.layer().poly('y', [(14, 32), (27, 32), (27, 47), (22, 47), (21, 37), (19, 37), (19, 47), (14, 47)])
for x in (16, 24, 26):
    legs.v('w', x, 33, 47)
legs.rect('Y', 14, 33, 15, 47).rect('Y', 22, 38, 22, 47).v('y', 15, 33, 47)
shoes = sp.layer().poly('c', [(13, 47), (19, 47), (19, 50), (12, 50)]).poly('c', [(22, 47), (27, 47), (30, 49), (30, 50), (22, 50)])
shoes.h('C', 12, 19, 50).h('C', 22, 30, 50)

# ---------------- torso: double-breasted gold suit, teal shirt, lavender tie ----------------
torso = sp.layer().poly('y', [(14, 21), (27, 21), (27, 26), (26, 33), (15, 33), (14, 26)])
for x in (16, 24, 26):
    torso.v('w', x, 21, 33)
torso.rect('Y', 14, 21, 15, 33)
torso.poly('k', [(18, 21), (23, 21), (21, 26), (20, 26)]).v('v', 20, 22, 26).v('v', 21, 22, 25)
torso.px('m', (18, 28), (23, 28), (18, 31), (23, 31))                  # buttons
neck = sp.layer().rect('s', 19, 15, 24, 22).v('S', 19, 15, 22).h('S', 19, 24, 18)

# ---------------- coat fronts draped over the shoulders ----------------
coat_l = sp.layer().poly('c', [(8, 20), (14, 20), (15, 24), (13, 44), (5, 44), (6, 28)])
coat_l.poly('C', [(5, 44), (6, 28), (8, 22), (9, 44)]).rect('p', 5, 31, 8, 33).h('P', 5, 8, 33)      # empty sleeve cuff
coat_r = sp.layer().poly('c', [(26, 20), (32, 20), (35, 28), (35, 44), (28, 44), (28, 29)])
coat_r.v('n', 28, 29, 44).rect('p', 33, 32, 35, 34).h('P', 33, 35, 34).px('P', (30, 36), (30, 40))
# fringed epaulettes: plate + hanging fringe
ep_l = sp.layer().poly('p', [(8, 17), (15, 17), (16, 18), (16, 23), (7, 23), (7, 18)]).h('P', 7, 16, 20)
ep_r = sp.layer().poly('p', [(25, 17), (32, 17), (33, 18), (33, 23), (24, 23), (24, 18)]).h('P', 24, 33, 20)
for x in (8, 10, 12, 14):
    ep_l.v('P', x, 21, 23)
for x in (25, 27, 29, 31):
    ep_r.v('P', x, 21, 23)

# ---------------- head: long face, short dark hair, orange shades, lazy grin, goatee ----------------
head = sp.layer()
head.ell('h', 10, 0, 29, 15)
head.poly('s', [(15, 3), (28, 3), (31, 6), (32, 10), (33, 12), (32, 14), (30, 17), (26, 19), (21, 19), (18, 17), (16, 13)])
head.poly('h', [(11, 2), (19, 0), (28, 1), (31, 4), (28, 4), (22, 3), (17, 4), (15, 7), (14, 10)])    # close-cropped hairline
head.ell('s', 12, 7, 15, 11).v('S', 13, 8, 10)                                                      # ear
head.poly('h', [(15, 5), (17, 5), (18, 14), (20, 17), (19, 17), (16, 12)])                          # long sideburn
head.h('S', 21, 27, 6)                                                                               # forehead crease
head.rect('a', 19, 8, 22, 10).rect('a', 25, 8, 29, 10).h('o', 23, 24, 8).px('o', (18, 8), (17, 8))  # orange shades
head.px('m', (21, 9), (28, 9)).px('c', (29, 8))                                                      # sleepy eyes, glint
head.px('S', (32, 11), (32, 12)).h('S', 20, 22, 11)                                                  # long nose, cheek
head.h('h', 26, 30, 14)                                                                              # moustache
head.h('c', 26, 29, 15).h('m', 27, 29, 16).px('m', (25, 15))                                          # lazy open grin
head.rect('h', 27, 17, 29, 18)                                                                       # goatee
head.px('S', (19, 16), (20, 17))                                                                     # jaw shade

# ---------------- front arm out of the coat: index finger up with a small light glow ----------------
arm = sp.layer()
arm.poly('y', [(23, 27), (27, 32), (37, 27), (35, 22)])
arm.line('w', [(26, 29), (34, 25)]).line('Y', [(24, 29), (27, 31)]).line('Y', [(27, 31), (35, 27)])
arm.poly('k', [(34, 22), (36, 21), (38, 26), (36, 27)])                                              # teal shirt cuff
arm.ell('s', 36, 20, 40, 24).px('S', (36, 23), (37, 24), (38, 24))
arm.rect('s', 38, 16, 40, 21)                                                                        # raised index finger
glow = sp.layer().ell('w', 37, 11, 41, 15).px('c', (39, 13), (38, 13), (40, 13), (39, 12), (39, 14))

for L in (coat_b, collar, legs, shoes, torso, neck, coat_l, coat_r, ep_l, ep_r, head, arm):
    sp.add(L)
sp.add(glow, outline='P')
sp.save()
