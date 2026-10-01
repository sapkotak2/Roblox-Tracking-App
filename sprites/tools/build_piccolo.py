"""Piccolo (no cape/turban, arms crossed) - head on the Luffy/Vegeta head frame, Luffy-width body.
g green  G green shade  d dark green  r pink arm stripe  w white  k dark line
P purple  p purple shade  b blue sash  B blue shade  n brown shoe  N brown shade"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from fillgrid import Grid, render
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PAL = {'g': (120,206,70), 'G': (78,160,48), 'd': (44,108,34), 'r': (236,96,120), 'w': (249,245,236), 'k': (29,28,33),
       'P': (122,62,170), 'p': (86,40,128), 'b': (70,150,220), 'B': (44,104,170), 'n': (168,112,60), 'N': (118,76,40)}
# ---------------- head (25 x 25): bald dome, antennae, long pointed ear, heavy angry brow
h = Grid(27, 25)
DOME = {3:(10,16),4:(8,18),5:(7,20),6:(6,21),7:(5,22),8:(5,23),9:(4,23),10:(4,23),11:(4,24),12:(4,24),13:(5,25),
        14:(5,25),15:(5,24),16:(6,24),17:(6,23),18:(7,23),19:(7,22),20:(8,22),21:(9,21),22:(11,20),23:(13,18)}
for y, (a, b) in DOME.items(): h.sp(y, 'g', a, b)
h.px([(15,2),(14,1),(15,0),(16,0)], 'g')                 # antenna 1 curling forward
h.px([(19,3),(20,2),(21,1),(22,1)], 'g')                 # antenna 2
for y, (a, b) in {6:(0,0),7:(0,1),8:(1,2),9:(1,3),10:(2,4),11:(3,5),12:(3,5),13:(4,5)}.items(): h.sp(y, 'g', a, b)  # pointed ear
h.px([(2,9),(3,10),(4,11),(4,12)], 'G')                  # ear inner
for y, (a, b) in DOME.items(): h.sp(y, 'G', a, a + 2 if y > 8 else a)   # back-of-head shade
h.px([(12,6),(13,7),(14,6),(16,7),(17,8)], 'G')          # forehead ridges
h.px([(14,11),(15,11),(16,12),(17,12),(18,12),(19,13),(20,13)], 'k')    # heavy brow, sloping down to the nose
h.px([(22,12),(23,12),(21,13)], 'k')                     # far brow -> angry V
h.px([(14,10),(15,10),(16,11),(17,11),(18,11)], 'd')     # brow ridge shadow above
h.px([(17,14),(18,14),(17,15),(18,15)], 'w'); h.px([(19,14),(19,15),(16,14)], 'k')   # glaring eye
h.px([(16,16),(17,16),(18,16),(22,15),(21,17)], 'G')     # lower lid, nose, cheek ridge
h.px([(13,17),(14,18),(15,19)], 'G')                     # cheek line
h.px([(18,19),(19,19),(20,19),(17,20),(21,20)], 'k')     # frown
h.px([(12,21),(13,22),(14,22),(19,21)], 'G')             # jaw shade
head = render(h, PAL, edge_pairs=())
# ---------------- body (20 wide): purple gi, crossed green arms with pink stripes, blue sash, baggy pants, brown shoes
b = Grid(20, 24)
b.rows(0, {0:[('g',8,11)], 1:[('P',1,17),('g',8,10)], 2:[('P',0,18),('g',9,9)], 3:[('P',0,18)],
           4:[('g',0,16),('G',0,0),('r',3,5),('r',10,11)], 5:[('g',0,17),('G',0,1),('r',3,5),('r',10,11),('G',14,17)],
           6:[('g',0,2),('P',3,16),('g',17,18)],
           7:[('g',1,18),('r',6,7),('r',12,14),('G',1,2)], 8:[('g',1,17),('r',6,7),('r',12,14),('G',1,3)],
           9:[('P',2,16)], 10:[('b',2,16)], 11:[('B',2,16)],
           12:[('P',1,17)], 13:[('P',0,18)], 14:[('P',0,8),('P',10,18)], 15:[('P',0,8),('P',10,18)],
           16:[('P',0,8),('P',10,18)], 17:[('P',1,8),('P',10,17)], 18:[('P',1,7),('P',11,17)], 19:[('P',2,6),('P',11,16)],
           20:[('n',1,7),('n',10,16)], 21:[('n',0,7),('n',10,17)], 22:[('N',0,7),('N',10,18)]})
for y in range(12, 20): b.sp(y, 'p', b.g[y].index('P'), b.g[y].index('P') + 1)   # pants shade on the back edge
b.px([(9,3),(9,2)], 'p'); b.px([(4,9),(13,9)], 'p'); b.px([(8,13),(9,13)], 'p')
body = render(b, PAL)
# ---------------- compose
out = Image.new('RGBA', (29, 52), (0,0,0,0))
out.alpha_composite(head, (0, 0))
out.alpha_composite(body, (5, 26))
out = out.crop(out.getbbox()); out.save(f'{R}/out/piccolo.png'); print('piccolo', out.size)
