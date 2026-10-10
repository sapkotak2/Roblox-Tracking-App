"""Charlotte Katakuri - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(30, 14, 22),                                   # outline
    s=(232, 168, 128), S=(184, 112, 80),              # skin / shade
    h=(136, 30, 60), H=(78, 14, 36),                  # maroon hair / strands
    c=(246, 232, 200), C=(204, 180, 140),             # fur scarf / shade
    v=(110, 68, 42), V=(66, 40, 26),                  # leather vest + boots / shade
    d=(74, 52, 88), D=(44, 30, 56),                   # trousers / shade
    m=(62, 58, 72), M=(140, 136, 150),                # black trident, wristbands / steel shine
    e=(250, 246, 236),                                # eye white
)
sp = Sprite('katakuri', W=50, H=52, palette=PAL)

# ---------------- Mogura (black spiked trident) held upright on the back side ----------------
tri = sp.layer()
tri.rect('m', 4, 10, 6, 50)                                         # shaft
tri.rect('m', 0, 9, 10, 11)                                         # crossbar
tri.rect('m', 0, 3, 2, 10).rect('m', 8, 3, 10, 10).rect('m', 4, 0, 6, 10)   # three prongs
tri.ell('m', 2, 12, 8, 18)                                          # spiked knob
tri.put('m', (1, 15), (9, 15), (1, 2), (9, 2))
tri.v('M', 5, 1, 10).v('M', 5, 19, 48).v('M', 1, 4, 9).v('M', 9, 4, 9).px('M', (4, 14), (4, 15))

# ---------------- back arm (holds the trident) ----------------
arm_b = sp.layer()
arm_b.ell('s', 8, 20, 17, 29)                                       # shoulder
arm_b.poly('s', [(9, 25), (16, 26), (13, 31), (8, 31)])             # forearm down to the shaft
arm_b.poly('S', [(8, 22), (11, 21), (10, 31), (8, 31)])
arm_b.rect('m', 7, 29, 13, 31).h('M', 8, 12, 29)                    # spiked band
arm_b.put('M', (6, 30), (14, 30))
arm_b.ell('s', 4, 31, 11, 37).h('S', 5, 10, 36)                     # fist around the shaft

# ---------------- legs ----------------
legs = sp.layer().poly('d', [(15, 34), (36, 34), (37, 46), (29, 46), (27, 39), (24, 39), (22, 46), (14, 46)])
legs.poly('D', [(14, 46), (15, 36), (18, 36), (18, 46)]).poly('D', [(27, 39), (28, 39), (30, 46), (29, 46)])
boots = sp.layer().poly('v', [(13, 45), (22, 45), (22, 50), (11, 50)]).poly('v', [(29, 45), (37, 45), (40, 48), (40, 50), (29, 50)])
boots.h('V', 11, 22, 50).h('V', 29, 40, 50).v('V', 13, 46, 49)

# ---------------- torso: bare muscular chest, open leather vest ----------------
torso = sp.layer()
torso.poly('s', [(12, 21), (38, 21), (37, 28), (34, 35), (16, 35), (13, 28)])
torso.v('S', 25, 25, 34).h('S', 21, 29, 28).h('S', 21, 29, 31)      # abs
torso.h('S', 18, 23, 25).h('S', 27, 33, 25)                         # pec line
vest = sp.layer()
vest.poly('v', [(11, 20), (19, 22), (20, 35), (15, 35), (12, 28)])
vest.poly('v', [(32, 22), (38, 20), (39, 28), (36, 35), (32, 35)])
vest.poly('V', [(11, 20), (15, 21), (16, 35), (15, 35), (12, 28)]).v('V', 32, 23, 35)
vest.h('V', 15, 36, 35)

# ---------------- head: spiky maroon hair, fur scarf over the mouth ----------------
head = sp.layer()
head.ell('h', 12, 1, 34, 18)
for pts in ([(14, 5), (10, -1), (20, 2)], [(19, 3), (23, -2), (27, 2)], [(26, 2), (32, -1), (33, 5)],
            [(31, 3), (39, 2), (36, 7)], [(14, 6), (7, 6), (13, 11)], [(13, 10), (7, 15), (15, 15)]):
    head.poly('h', pts)
head.poly('s', [(19, 7), (36, 6), (37, 8), (37, 15), (19, 15)])     # face (mouth hidden by the scarf)
head.poly('h', [(18, 4), (37, 4), (37, 6), (19, 7), (18, 9)])       # swept-back hairline
for pts in ([(14, 3), (21, 5)], [(13, 8), (17, 10)], [(25, 1), (28, 4)], [(31, 2), (34, 4)]):
    head.line('H', pts)                                              # strand lines
head.h('S', 20, 36, 7)                                               # shade under the hairline
head.ell('s', 16, 8, 20, 12).v('S', 17, 9, 11)                       # ear
head.h('o', 22, 25, 8).h('o', 29, 33, 8).px('o', (26, 9), (28, 9))   # stern brows
head.rect('e', 22, 10, 24, 11).v('h', 24, 10, 11).rect('e', 29, 10, 32, 11).v('h', 31, 10, 11)  # eyes, maroon iris
head.px('S', (36, 11), (36, 12)).v('S', 20, 12, 14)                  # nose bridge, cheek shade
scarf = sp.layer()
scarf.ell('c', 15, 13, 40, 25)
scarf.poly('C', [(15, 19), (22, 24), (17, 24)]).line('C', [(18, 16), (36, 16)]).line('C', [(20, 20), (38, 20)])
scarf.poly('C', [(16, 15), (19, 15), (18, 22), (15, 20)])

# ---------------- front arm: big bare arm, spiked band, fist ----------------
arm = sp.layer()
arm.ell('s', 34, 20, 44, 30)                                         # deltoid
arm.poly('s', [(36, 26), (43, 26), (45, 35), (39, 36)])              # forearm
arm.v('S', 37, 27, 35).h('S', 36, 41, 29)
arm.rect('m', 38, 31, 45, 33).h('M', 39, 44, 31)
arm.put('M', (37, 32), (46, 32))
arm.ell('s', 38, 34, 46, 40).h('S', 38, 45, 39).px('S', (41, 36), (41, 37))

for L in (tri, arm_b, legs, boots, torso, vest, head, scarf, arm):
    sp.add(L)
sp.save()
