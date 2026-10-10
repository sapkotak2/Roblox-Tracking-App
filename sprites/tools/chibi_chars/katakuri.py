"""Charlotte Katakuri - chibi redraw (see tools/chibi.py for the style guide).
Checked against refs/redraw/katakuri/NOTES.md (official anime concept art / infobox)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(30, 16, 24),                                   # outline
    s=(226, 164, 118), S=(176, 112, 76),              # tan skin / shade
    h=(158, 40, 84), H=(98, 20, 52),                  # short spiky magenta-maroon hair / strands
    c=(244, 236, 214), C=(196, 184, 160),             # cream fur / shade; studs, skull buckle, eye whites
    k=(38, 34, 42),                                   # black scarf stripes, belt, boots, trident
    v=(72, 70, 84), V=(48, 46, 58),                   # black leather vest + trousers / shade
    p=(238, 96, 146), P=(170, 44, 96),                # pink tattoos, knee pad / dark pink, iris
    g=(92, 60, 44),                                   # brown gloves
    b=(112, 44, 48),                                  # maroon trident shaft
    M=(178, 182, 196),                                # steel: spikes, prongs, strap
)
sp = Sprite('katakuri', W=50, H=52, palette=PAL)

# ---------------- Mogura: long maroon shaft, steel trident head pointing DOWN beside him ----------------
tri = sp.layer()
tri.rect('b', 4, 2, 6, 38)                                          # shaft
tri.rect('M', 3, 37, 7, 39)                                         # collar
tri.rect('k', 4, 40, 6, 50)                                         # middle prong
tri.poly('k', [(3, 40), (0, 43), (0, 50), (2, 50), (2, 44), (4, 42)])    # curved outer prongs
tri.poly('k', [(7, 40), (10, 43), (10, 50), (8, 50), (8, 44), (6, 42)])
tri.v('M', 5, 41, 49).v('M', 1, 45, 49).v('M', 9, 45, 49)

# ---------------- back arm: bare, gloved hand on the shaft ----------------
arm_b = sp.layer()
arm_b.ell('s', 8, 21, 17, 30)                                       # shoulder
arm_b.poly('s', [(9, 26), (16, 27), (11, 34), (6, 33)])             # forearm down to the shaft
arm_b.poly('S', [(8, 23), (11, 22), (9, 32), (7, 33)])
arm_b.ell('g', 2, 31, 9, 37)                                        # brown glove gripping the shaft

# ---------------- legs: black trousers, thigh strap, pink knee pad, spiked boots ----------------
legs = sp.layer().poly('v', [(15, 34), (36, 34), (37, 46), (29, 46), (27, 38), (24, 38), (22, 46), (14, 46)])
legs.poly('V', [(14, 46), (15, 36), (18, 36), (18, 46)]).poly('V', [(27, 38), (28, 38), (30, 46), (29, 46)])
legs.line('M', [(28, 39), (36, 37)]).line('M', [(28, 40), (37, 38)]).px('c', (30, 39), (34, 38))  # studded thigh strap
pad = sp.layer().rect('p', 30, 43, 36, 46).v('c', 33, 43, 46).h('P', 30, 36, 46).put('M', (37, 44), (38, 44))
boots = sp.layer().poly('k', [(13, 46), (22, 46), (22, 50), (11, 50)]).poly('k', [(29, 46), (37, 46), (40, 48), (40, 50), (29, 50)])
boots.h('M', 13, 22, 47).h('M', 29, 37, 47).put('M', (12, 47), (23, 47), (28, 47), (38, 47))  # spiked boot bands

# ---------------- torso: bare chest, pink stripe tattoo, open black vest, skull belt ----------------
torso = sp.layer()
torso.poly('s', [(13, 21), (37, 21), (37, 27), (34, 33), (16, 33), (13, 27)])
torso.v('S', 22, 25, 32).h('S', 17, 21, 28).h('S', 17, 21, 31)     # abs / pec lines
for x in (25, 29, 33):
    torso.v('p', x, 22, 33).v('p', x + 1, 22, 33)                                       # pink stripe tattoo
vest = sp.layer()
vest.poly('v', [(11, 20), (17, 22), (18, 33), (14, 33), (12, 27)])
vest.poly('v', [(35, 22), (38, 20), (39, 27), (38, 33), (36, 33)])
vest.poly('V', [(11, 20), (13, 21), (14, 33), (14, 33), (12, 27)])
vest.px('c', (15, 31), (16, 31), (37, 31))                                    # white studs
belt = sp.layer().rect('k', 15, 33, 36, 34).rect('c', 23, 32, 26, 35).px('k', (24, 33), (25, 33))   # skull buckle

# ---------------- head: short spiky hair, stern half-lidded eyes over the scarf ----------------
head = sp.layer()
head.ell('h', 14, 0, 34, 14)
for pts in ([(15, 3), (13, -1), (19, 1)], [(19, 1), (21, -2), (24, 0)], [(24, 0), (27, -2), (29, 1)],
            [(29, 1), (33, -1), (34, 3)], [(14, 7), (11, 6), (14, 10)]):
    head.poly('h', pts)                                              # small crew-cut spikes
head.poly('s', [(19, 3), (35, 2), (37, 5), (37, 14), (19, 14)])     # face (mouth hidden by the scarf)
head.poly('h', [(18, 1), (36, 0), (37, 3), (34, 3), (32, 4), (29, 3), (26, 4), (23, 3), (20, 5), (19, 7)])  # spiky hairline
head.line('H', [(17, 2), (21, 4)]).line('H', [(24, 1), (27, 3)]).line('H', [(15, 8), (17, 5)])
head.ell('s', 15, 6, 19, 11).v('S', 16, 7, 10)                       # ear
head.px('o', (22, 5), (23, 5), (24, 5), (25, 6), (26, 6)).px('o', (28, 6), (29, 5), (30, 5), (31, 5), (32, 5), (33, 5))  # brows dipping in
head.v('S', 27, 4, 7)                                                # frown crease
head.rect('c', 22, 7, 25, 8).v('P', 24, 7, 8).rect('c', 29, 7, 32, 8).v('P', 31, 7, 8).h('o', 22, 25, 6).h('o', 29, 32, 6)   # narrow half-lidded eyes, pink-red iris
head.px('S', (36, 8), (36, 9)).v('S', 20, 7, 13)  # bags, nose, cheek shade
# fur scarf: cream with thick black bands, jagged furry edge, spread over both shoulders
scarf = sp.layer()
scarf.ell('c', 14, 10, 38, 19).ell('c', 10, 14, 42, 24)
for x in (11, 17, 23, 29, 35):
    scarf.poly('c', [(x, 22), (x + 3, 27), (x + 6, 22)])            # jagged fur tufts along the bottom
for pts in ([(11, 15), (7, 17), (10, 20)], [(41, 15), (45, 17), (41, 20)], [(15, 13), (12, 9), (19, 12)], [(34, 12), (38, 8), (38, 14)]):
    scarf.poly('c', pts)                                             # side / top tufts
for y in (15, 16, 20, 21):
    scarf.h('k', 0, 49, y)                                           # thick black fur bands
scarf.v('C', 10, 13, 25).v('C', 11, 13, 25).v('C', 12, 13, 25).px('C', (8, 17), (9, 17), (9, 16))   # back side in shade
for y in (15, 16, 20, 21):
    scarf.h('k', 0, 12, y)

# ---------------- front arm: hand on the hip, pink shoulder tattoo, spiked band, glove ----------------
arm = sp.layer()
arm.ell('s', 34, 20, 44, 30)                                         # deltoid
arm.poly('s', [(39, 26), (44, 27), (45, 31), (41, 32)])              # upper arm out to the elbow
arm.poly('s', [(41, 29), (45, 31), (39, 34), (36, 31)])              # forearm back to the hip
arm.rect('p', 37, 23, 44, 26).h('P', 38, 43, 25).px('P', (40, 24), (41, 24))           # pink tattoo
arm.v('S', 37, 27, 29).px('S', (42, 30), (43, 31))
arm.line('V', [(38, 31), (42, 29)], width=2).put('M', (43, 28), (37, 33))            # spiked band
glove = sp.layer().ell('g', 32, 30, 38, 35)

for L in (tri, arm_b, legs, pad, boots, torso, vest, belt, head, scarf, arm, glove):
    sp.add(L)
sp.save()
