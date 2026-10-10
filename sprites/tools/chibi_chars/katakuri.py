"""Charlotte Katakuri - chibi redraw (see tools/chibi.py for the style guide).
Checked against refs/redraw/katakuri/NOTES.md (official anime concept art / infobox): tall, lean, long-legged."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(30, 16, 24),                                   # outline
    s=(226, 164, 118), S=(176, 112, 76),              # tan skin / shade
    h=(158, 40, 84), H=(98, 20, 52),                  # short spiky magenta-maroon hair / strands
    c=(246, 240, 224),                                # white fur, studs, skull buckle, eye whites
    k=(34, 30, 38),                                   # black zebra stripes, belt, boots, trident prongs
    v=(72, 70, 84), V=(48, 46, 58),                   # black leather vest + trousers / shade
    p=(238, 96, 146), P=(170, 44, 96),                # pink tattoos, knee pad / dark pink, iris
    g=(92, 60, 44),                                   # brown gloves
    b=(120, 46, 50),                                  # maroon trident shaft
    M=(178, 182, 196),                                # steel: collar, spikes, strap
)
sp = Sprite('katakuri', W=40, H=52, palette=PAL)

# ---------------- Mogura: slim vertical shaft, trident head pointing DOWN beside him (drawn pixel by pixel) ----------------
tri = sp.layer()
tri.rect('o', 3, 0, 5, 39).rect('b', 4, 1, 4, 38)                  # shaft
tri.rect('o', 1, 38, 7, 41).rect('M', 2, 39, 6, 40)                 # steel collar
tri.rect('k', 4, 42, 4, 50)                                         # middle prong
tri.put('k', (3, 42), (2, 43), (1, 44), (1, 45), (1, 46), (1, 47), (1, 48), (1, 49), (1, 50))   # outer prongs, curving out
tri.put('k', (5, 42), (6, 43), (7, 44), (7, 45), (7, 46), (7, 47), (7, 48), (7, 49), (7, 50))

# ---------------- back arm: lean, gloved hand on the shaft ----------------
arm_b = sp.layer()
arm_b.ell('s', 9, 15, 15, 22)
arm_b.poly('s', [(10, 19), (14, 20), (11, 29), (8, 28)]).v('S', 9, 18, 28)
glove_b = sp.layer().ell('g', 5, 27, 10, 32)

# ---------------- long legs: black trousers, studded strap, pink knee pad, spiked boots ----------------
legs = sp.layer().poly('v', [(16, 30), (29, 30), (30, 47), (25, 47), (23, 36), (22, 36), (20, 47), (15, 47)])
legs.poly('V', [(15, 47), (16, 32), (18, 32), (17, 47)]).v('V', 23, 37, 47)
legs.line('M', [(24, 36), (30, 34)]).line('M', [(24, 37), (30, 35)]).px('c', (26, 36), (29, 35))   # studded thigh strap
pad = sp.layer().rect('p', 24, 40, 29, 43).v('c', 26, 40, 43).v('c', 27, 40, 43).h('P', 24, 29, 43).put('M', (31, 41))
boots = sp.layer().poly('k', [(15, 46), (20, 46), (20, 50), (13, 50)]).poly('k', [(25, 46), (30, 46), (33, 49), (33, 50), (25, 50)])
boots.h('M', 15, 20, 47).h('M', 25, 30, 47).put('M', (13, 47), (32, 47))     # spiked boot bands

# ---------------- lean V torso: bare chest, pink stripe tattoo, short studded black vest, skull belt ----------------
torso = sp.layer()
torso.poly('s', [(12, 15), (32, 15), (31, 20), (28, 29), (17, 29), (14, 20)])
torso.h('S', 17, 21, 20).v('S', 20, 21, 28).h('S', 17, 20, 23).h('S', 18, 20, 26)       # pec / abs lines
torso.v('p', 22, 18, 29).v('p', 23, 18, 29).v('p', 25, 18, 29).v('p', 26, 18, 29)       # pink stripe tattoo
vest = sp.layer()
vest.poly('v', [(12, 15), (17, 16), (18, 26), (15, 26), (13, 20)])
vest.poly('v', [(27, 16), (32, 15), (31, 20), (29, 26), (27, 26)])
vest.v('V', 13, 16, 21).v('V', 14, 18, 26)
vest.px('c', (16, 25), (28, 25))                                     # white studs
belt = sp.layer().rect('k', 16, 29, 29, 30).rect('c', 20, 28, 23, 31).px('k', (21, 29), (22, 29))   # skull buckle

# ---------------- head: short spiky magenta hair, heavy brows, narrow eyes ----------------
head = sp.layer()
head.ell('h', 13, 0, 31, 12)
for pts in ([(14, 3), (12, -1), (17, 1)], [(17, 1), (19, -2), (22, 0)], [(22, 0), (25, -2), (27, 1)], [(27, 1), (31, -1), (31, 3)], [(14, 5), (11, 5), (14, 8)]):
    head.poly('h', pts)                                              # crew-cut spikes
head.poly('s', [(17, 3), (30, 2), (32, 5), (32, 12), (17, 12)])     # face
head.poly('h', [(16, 1), (31, 0), (32, 3), (29, 3), (27, 4), (24, 3), (21, 4), (18, 3), (17, 6)])  # spiky hairline
head.line('H', [(15, 1), (18, 2)]).line('H', [(22, 0), (24, 2)])
head.ell('s', 14, 5, 17, 9).v('S', 15, 6, 8)                        # ear
head.px('o', (18, 5), (19, 5), (20, 5), (21, 6)).px('o', (24, 6), (25, 5), (26, 5), (27, 5), (28, 5))   # heavy brows dipping in
head.h('o', 18, 21, 6).h('o', 25, 28, 6)                             # heavy lids
head.rect('c', 18, 7, 21, 8).v('P', 20, 7, 8).rect('c', 25, 7, 28, 8).v('P', 27, 7, 8)   # narrow eyes, pink-red iris
head.v('S', 23, 4, 6).px('S', (31, 8), (31, 9)).v('S', 17, 7, 11)    # frown crease, nose, cheek shade
# thin zebra fur scarf wrapping the neck and up over the mouth
scarf = sp.layer().poly('c', [(11, 9), (33, 9), (36, 12), (35, 16), (10, 17), (8, 13)])
for x in range(8, 37):
    up = ((x + 1) // 6) % 2 == 0
    scarf.px('k', (x, 11 if up else 12), (x, 13 if up else 14), (x, 14 if up else 15))   # two bold wavy zebra stripes

# ---------------- front arm: hand on the hip, pink shoulder tattoo, spiked band ----------------
arm = sp.layer()
arm.ell('s', 29, 14, 36, 21)                                         # deltoid
arm.poly('s', [(32, 18), (36, 18), (38, 25), (35, 26)])              # upper arm out to the elbow
arm.poly('s', [(35, 23), (38, 25), (33, 30), (31, 28)])              # forearm back to the hip
arm.rect('p', 31, 16, 36, 19).h('P', 32, 35, 18).px('P', (33, 17))   # pink tattoo
arm.v('S', 32, 20, 24)
arm.line('V', [(32, 27), (36, 25)], width=2).put('M', (37, 24), (31, 29))   # spiked band
glove = sp.layer().ell('g', 28, 27, 32, 31)

for L in (tri, arm_b, legs, pad, boots, torso, vest, belt, head, scarf, arm, glove):
    sp.add(L)
sp.layers[0] = (tri, 'o', (), False)                                 # trident is hand-drawn, no auto outline
sp.add(glove_b)
sp.save()
