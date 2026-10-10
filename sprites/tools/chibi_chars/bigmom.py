"""Big Mom (Charlotte Linlin) - chibi redraw (see tools/chibi.py for the style guide).
Checked against refs/redraw/bigmom/NOTES.md (official anime concept art / infobox)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(44, 16, 32),                                   # outline
    s=(242, 198, 158), S=(204, 148, 112),             # skin / shade
    h=(250, 156, 196), H=(214, 92, 148),              # feathery pink hair / strands
    d=(250, 168, 184), D=(222, 122, 148),             # pink dress / shade
    r=(212, 34, 64), R=(124, 18, 42),                 # red polka dots + lips / mouth inside, heels
    w=(255, 255, 255), C=(186, 194, 216),             # white (teeth, skull, plume, cape, hem) / shade
    m=(222, 64, 136), M=(156, 32, 92),                # magenta captain hat / shade
    g=(242, 192, 62),                                 # gold hat trim, neckline frill, cape lining
    u=(150, 88, 176),                                 # purple eyeshadow
)
sp = Sprite('bigmom', W=50, H=52, palette=PAL)

# ---------------- white cape behind her ----------------
cape = sp.layer().poly('w', [(8, 24), (42, 24), (46, 34), (46, 45), (4, 45), (4, 34)])
cape.poly('C', [(4, 45), (4, 34), (8, 25), (10, 45)]).poly('C', [(42, 30), (46, 45), (43, 45)]).h('C', 4, 46, 45)
cape.v('g', 46, 35, 44).v('g', 4, 35, 44)                                           # yellow lining at the edges

# ---------------- feathery pink hair flaring out sideways ----------------
hair = sp.layer()
hair.ell('h', 6, 6, 44, 28)
for pts in ([(8, 9), (2, 12), (7, 15)], [(6, 14), (1, 19), (7, 20)], [(6, 19), (2, 26), (9, 24)], [(9, 23), (6, 30), (13, 26)],
            [(42, 9), (47, 11), (43, 15)], [(44, 14), (47, 20), (43, 20)], [(43, 19), (47, 26), (41, 24)], [(40, 23), (43, 30), (37, 26)]):
    hair.poly('h', pts)                                                             # feather tufts
for pts in ([(4, 13), (9, 15)], [(3, 20), (9, 20)], [(5, 25), (10, 23)], [(45, 13), (41, 15)], [(45, 20), (41, 20)], [(44, 25), (40, 23)]):
    hair.line('H', pts)

# ---------------- legs + dark red heels ----------------
legs = sp.layer().rect('s', 17, 42, 20, 47).rect('s', 29, 42, 32, 47).v('S', 17, 42, 47).v('S', 29, 42, 47)
heels = sp.layer().poly('R', [(15, 47), (21, 47), (21, 50), (15, 50)]).poly('R', [(28, 47), (34, 47), (36, 50), (28, 50)])

# ---------------- back arm ----------------
arm_b = sp.layer().ell('s', 6, 27, 14, 35).poly('s', [(7, 31), (13, 32), (11, 40), (6, 39)]).ell('s', 5, 37, 11, 42)
arm_b.v('S', 7, 30, 40)

# ---------------- pink dress with big red polka dots, gold frill neckline, white frilly hem ----------------
dress = sp.layer().poly('d', [(12, 27), (38, 27), (41, 31), (44, 37), (45, 43), (5, 43), (6, 37), (9, 31)])
dress.poly('D', [(5, 43), (6, 37), (9, 31), (12, 28), (14, 43)])
for x, y in ((14, 29), (24, 30), (33, 29), (9, 35), (19, 35), (28, 35), (37, 34), (13, 39), (23, 39), (32, 39)):
    dress.ell('r', x, y, x + 4, y + 4)
dress.h('g', 11, 39, 27).px('g', (12, 28), (16, 28), (20, 28), (24, 28), (28, 28), (32, 28), (36, 28))   # scalloped gold frill
dress.h('w', 5, 45, 43).px('w', (8, 42), (12, 42), (16, 42), (20, 42), (24, 42), (28, 42), (32, 42), (36, 42), (40, 42))  # frilly hem

# ---------------- head: big round face, long hooked nose, huge red grin ----------------
head = sp.layer()
head.ell('s', 14, 6, 38, 28)
head.poly('s', [(34, 12), (38, 12), (44, 16), (44, 18), (36, 19)])                    # long hooked nose
head.poly('h', [(14, 8), (38, 8), (38, 12), (34, 10), (30, 11), (26, 10), (22, 11), (18, 10), (15, 13)])  # fringe under the hat
head.h('u', 19, 21, 12).h('u', 27, 30, 12)                                           # purple eyeshadow
head.h('w', 19, 21, 13).px('o', (21, 13)).h('w', 27, 30, 13).px('o', (29, 13))      # small eyes
head.h('o', 19, 21, 11).h('o', 27, 30, 11)                                           # thin brows
head.h('S', 37, 43, 18).v('S', 16, 14, 24)              # nose underside, cheek shade
head.poly('r', [(18, 19), (34, 19), (37, 18), (36, 23), (31, 26), (23, 26), (19, 23)])   # big red lips
head.poly('R', [(20, 20), (35, 20), (34, 23), (30, 25), (24, 25), (21, 23)])         # open mouth
head.h('w', 21, 34, 20).h('w', 24, 30, 24)                                           # rows of teeth
head.h('S', 20, 32, 27)                                                              # double chin
hat = sp.layer()
hat.ell('w', 2, 2, 9, 8).ell('w', 5, 0, 12, 6).ell('w', 4, 5, 13, 11)                 # fluffy white feather plume at the back
hat.px('C', (3, 6), (4, 7), (5, 8), (6, 9), (7, 10), (8, 10))
hat.poly('m', [(9, 9), (12, 4), (18, 1), (25, 0), (32, 1), (38, 4), (42, 9), (36, 8), (25, 7), (14, 8)])   # captain bicorne
hat.line('g', [(10, 8), (13, 4), (18, 2), (25, 1), (32, 2), (37, 4), (41, 8)])       # gold trim
hat.poly('M', [(9, 9), (14, 8), (25, 7), (36, 8), (42, 9), (36, 9), (25, 8), (14, 9)])
hat.ell('w', 22, 2, 28, 7).px('o', (24, 4), (26, 4)).px('M', (25, 6), (23, 6), (27, 6))   # skull
hat.put('w', (22, 2), (21, 1), (28, 2), (29, 1))                                     # horns

# ---------------- front arm with heart tattoo ----------------
arm = sp.layer().ell('s', 36, 27, 45, 36).poly('s', [(38, 32), (45, 32), (46, 39), (40, 40)]).ell('s', 39, 37, 46, 43)
arm.v('S', 38, 33, 39).h('S', 40, 45, 42)
arm.px('r', (41, 29), (43, 29), (41, 30), (42, 30), (43, 30), (42, 31))              # heart tattoo

for L in (cape, hair, legs, heels, arm_b, dress, head, hat, arm):
    sp.add(L)
sp.save()
