"""Lelouch Lamperouge / vi Britannia (Code Geass) - chibi redraw (see tools/chibi.py for the style guide; checklist
in refs/redraw/lelouch/NOTES.md, built from the infobox and anime stills).
Black hair with pointed bangs falling between the eyes and locks framing the face, large clear purple eyes (the left
one, far side, lit red by Geass), black Ashford Academy uniform with a tall collar, gold trim lines, gold collar
marks and buttons, arm thrust forward in the Geass command pose."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(14, 12, 20),                                    # outline
    h=(44, 38, 50), H=(18, 14, 24),                    # hair (brown-black) / strands
    s=(250, 224, 202), S=(214, 174, 154), m=(172, 108, 104),  # skin / shade / mouth
    e=(252, 250, 255), p=(150, 78, 222), r=(226, 36, 56),     # eye white / purple iris / Geass red
    j=(50, 54, 62), J=(28, 30, 36),                    # black uniform / shade
    g=(232, 192, 84),                                  # gold trim
)
sp = Sprite('lelouch', W=46, H=52, palette=PAL)


def seg(L, k, p0, p1):
    """recolour a straight line of already-filled pixels"""
    (x0, y0), (x1, y1) = p0, p1
    n = max(abs(x1 - x0), abs(y1 - y0))
    L.px(k, *[(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)])
    return L


# ---------------- back arm (sleeve + hand, hanging behind) ----------------
back_arm = sp.layer()
back_arm.poly('J', [(10, 21), (15, 21), (15, 29), (11, 31), (8, 26)])
back_arm.h('g', 9, 13, 30)
back_arm.ell('s', 8, 30, 13, 35).h('S', 9, 12, 34)

# ---------------- legs: black trousers, dark shoes ----------------
leg_b = sp.layer()
leg_b.poly('J', [(14, 34), (20, 34), (17, 40), (14, 46), (9, 46), (11, 40)])
leg_b.poly('J', [(8, 45), (15, 45), (15, 50), (4, 50), (5, 47)]).h('j', 9, 13, 46)
leg_f = sp.layer()
leg_f.poly('j', [(21, 34), (27, 34), (29, 40), (30, 46), (25, 46), (24, 40)])
seg(leg_f, 'J', (22, 35), (24, 39)); leg_f.v('J', 25, 40, 45)
leg_f.poly('J', [(24, 45), (31, 45), (33, 47), (35, 48), (35, 50), (24, 50)]).h('j', 26, 30, 46)

# ---------------- torso: slim black jacket to the hips, off-centre gold line, gold hem, buttons ----------------
torso = sp.layer()
torso.poly('j', [(13, 21), (26, 21), (26, 28), (27, 36), (13, 36), (13, 28)])
torso.poly('J', [(13, 21), (16, 21), (16, 36), (13, 36)])                           # back side in shade
torso.v('g', 19, 22, 27).v('g', 24, 22, 27).h('g', 14, 19, 27).h('g', 24, 26, 27)  # gold lines down from the collar, then outward
torso.h('g', 14, 26, 35)                                                            # gold hem
torso.px('g', (16, 30), (25, 30))                                                   # gold buttons
torso.v('J', 21, 28, 34)

# ---------------- head ----------------
head = sp.layer()
head.rect('s', 18, 17, 22, 21).v('S', 18, 17, 20)                                   # neck
head.ell('h', 9, 0, 30, 16)
head.poly('h', [(9, 7), (16, 7), (16, 19), (13, 18), (10, 20), (9, 16), (6, 17), (8, 12)])  # pointed locks at the nape
head.poly('s', [(16, 8), (29, 7), (31, 11), (31, 15), (28, 19), (25, 21), (21, 20), (18, 17), (16, 13)])  # narrow face, pointed chin
# pointed bangs: long tips, one falling between the eyes; a lock framing the far cheek
for pts in ([(14, 4), (21, 4), (18, 11)], [(19, 4), (25, 4), (23, 12)], [(24, 4), (31, 5), (28, 10)],
            [(28, 5), (33, 7), (31, 11)], [(14, 6), (18, 6), (17, 18)]):
    head.poly('h', pts)
seg(head, 'H', (12, 4), (14, 10)); seg(head, 'H', (18, 2), (17, 7)); seg(head, 'H', (22, 5), (23, 10))
seg(head, 'H', (11, 12), (12, 18)); seg(head, 'H', (27, 4), (28, 7))
head.h('S', 18, 30, 10).px('S', (19, 11), (20, 11), (25, 11))                       # shade under the bangs
# thin straight brows; large half-lidded eyes: far eye Geass red, near eye clear purple
head.px('o', (20, 10), (21, 10), (26, 10), (27, 10), (28, 10))
head.h('o', 19, 21, 12).px('e', (19, 13)).px('r', (20, 13), (21, 13), (20, 14), (21, 14)).px('e', (19, 14))
head.h('o', 24, 28, 12).px('e', (24, 13), (24, 14), (28, 13), (28, 14))
head.px('p', (25, 13), (26, 13), (27, 13), (25, 14), (26, 14), (27, 14))
head.px('S', (31, 15))                                                              # nose
head.h('m', 25, 26, 18).px('m', (27, 17))                                           # small smug smile
head.h('S', 19, 21, 18)                                                             # jaw shade

# ---------------- tall collar, gold edge and gold collar marks ----------------
collar = sp.layer()
collar.poly('j', [(15, 16), (18, 18), (22, 19), (26, 17), (27, 22), (22, 23), (15, 22)])
collar.poly('J', [(15, 16), (18, 18), (18, 22), (15, 22)])
collar.h('g', 16, 26, 22).px('g', (25, 19), (25, 20), (24, 20), (17, 19))

# ---------------- front arm: thrust forward, open palm (Geass command) ----------------
front = sp.layer()
front.poly('j', [(24, 21), (29, 21), (35, 23), (35, 27), (29, 27), (26, 26)])
seg(front, 'J', (25, 24), (34, 26))
front.v('g', 34, 23, 27)                                                            # gold cuff
front.poly('s', [(35, 20), (39, 19), (41, 20), (41, 27), (36, 28)])                 # open palm
front.h('S', 36, 40, 27).px('S', (39, 22), (39, 23), (39, 25))                      # finger lines

for L in (back_arm, leg_b, leg_f, torso, head, collar, front):
    sp.add(L)
sp.save()
