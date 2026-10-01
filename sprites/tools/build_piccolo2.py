"""Piccolo v3 - redrawn at full roster size (~24x51), facing right, arms crossed. Fill-only + auto outline."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from fillgrid import Grid, render
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PAL = {'l': (170,234,96), 'g': (118,200,58), 'G': (72,152,42), 'd': (40,98,32), 'r': (232,90,120), 'R': (176,52,84),
       'w': (250,250,250), 'k': (16,16,20), 'P': (128,62,172), 'L': (162,98,206), 'p': (86,38,122),
       'b': (96,196,236), 'B': (58,138,198), 'n': (168,112,62), 'N': (112,72,36)}
g = Grid(22, 49)
# antennae curling forward
g.px([(11,2),(11,1),(12,0),(13,0),(14,1), (15,2),(16,1),(17,0),(18,0),(19,1)], 'g')
# dome
DOME = {3:(8,14),4:(6,15),5:(5,16),6:(4,17),7:(4,17),8:(3,18),9:(3,18),10:(3,18),11:(3,18),12:(3,18),
        13:(4,18),14:(4,18),15:(5,17),16:(6,17),17:(7,16),18:(9,15)}
for y, (a, b) in DOME.items():
    g.sp(y, 'g', a, b)
    g.sp(y, 'G', a, a + (3 if y > 5 else 1))
    if y > 6: g.sp(y, 'd', a, a)
g.px([(11,4),(12,4),(13,5),(12,5),(14,6)], 'l')                 # dome highlight
g.px([(8,5),(9,6),(9,7),(14,4)], 'G')                            # forehead ridges
# ears: big back ear pointing up-back, small far ear on the right
for y, (a, b) in {3:(0,0),4:(0,1),5:(0,2),6:(1,3),7:(1,3),8:(2,3),9:(2,3)}.items(): g.sp(y, 'g', a, b)
g.px([(1,5),(2,6),(2,7)], 'G')
for y, (a, b) in {6:(20,20),7:(19,20),8:(19,19)}.items(): g.sp(y, 'g', a, b)
# angry face
g.sp(9, 'd', 10, 18)                                             # brow ridge
g.px([(11,10),(12,10),(13,10),(14,11),(15,11),(16,11)], 'k')    # brow sloping down toward the nose
g.px([(17,10),(18,10)], 'k')                                     # far brow
g.px([(13,12),(14,12),(13,13),(14,13)], 'w'); g.px([(15,12),(15,13),(12,12)], 'k')   # glaring eye
g.px([(12,14),(13,14),(14,14),(17,13)], 'G')                    # lower lid, far cheek
g.px([(10,14),(11,15),(12,16)], 'G')                            # cheekbone
g.px([(14,16),(15,16),(16,16),(13,17),(17,17)], 'k')            # frown
g.px([(10,17),(11,17),(12,18)], 'G')
# neck
g.sp(19, 'G', 9, 13)
# gi + crossed arms (upper arms down the sides, two forearms crossing, outlined so they read)
g.sp(20, 'P', 4, 17); g.sp(20, 'g', 9, 12); g.sp(20, 'g', 2, 3); g.sp(20, 'g', 18, 19)
for y in (21, 22, 23):
    g.sp(y, 'g', 1, 3); g.sp(y, 'P', 4, 17); g.sp(y, 'g', 18, 20)
g.px([(10,21),(11,21)], 'G'); g.px([(14,21),(15,22),(16,22)], 'L')
g.px([(1,22),(2,22),(19,22),(20,22),(1,23),(20,23)], 'r')
g.sp(24, 'g', 1, 3); g.sp(24, 'k', 4, 17); g.sp(24, 'g', 18, 20)
g.sp(25, 'g', 1, 19); g.px([(14,25),(15,25),(16,25)], 'r'); g.px([(1,25),(2,25)], 'l')
g.sp(26, 'g', 1, 19); g.px([(14,26),(15,26),(16,26)], 'R'); g.px([(1,26),(2,26),(3,26)], 'G')
g.sp(27, 'k', 3, 18); g.px([(1,27),(2,27)], 'G'); g.px([(19,27),(20,27)], 'g')
g.sp(28, 'g', 2, 20); g.px([(5,28),(6,28),(7,28)], 'r'); g.px([(19,28),(20,28)], 'l')
g.sp(29, 'g', 2, 20); g.px([(5,29),(6,29),(7,29)], 'R'); g.px([(18,29),(19,29),(20,29)], 'G')
g.sp(30, 'k', 4, 17); g.sp(30, 'g', 2, 3); g.sp(30, 'G', 18, 19)
g.sp(31, 'P', 4, 17); g.px([(4,31),(5,31)], 'p')
g.sp(32, 'b', 4, 17); g.sp(33, 'B', 4, 17)
# baggy pants
g.sp(34, 'P', 3, 18)
for y in range(35, 38): g.sp(y, 'P', 2, 19)
for y in range(38, 43): g.sp(y, 'P', 2, 9); g.sp(y, 'P', 12, 19)
for y in range(43, 45): g.sp(y, 'P', 3, 8); g.sp(y, 'P', 13, 18)
for y in range(34, 45):
    idx = [x for x in range(22) if g.g[y][x] == 'P']
    if idx: g.px([(idx[0], y), (idx[0] + 1, y)], 'p')
g.px([(14,35),(15,36),(16,37),(7,35),(7,36),(6,37),(10,35),(16,40),(16,41)], 'p')
g.px([(13,35),(17,39),(17,40)], 'L')
# shoes
g.sp(45, 'n', 2, 8); g.sp(45, 'n', 12, 19)
for y in (46, 47): g.sp(y, 'n', 1, 9); g.sp(y, 'n', 12, 20)
g.sp(48, 'N', 1, 9); g.sp(48, 'N', 12, 20)
im = render(g, PAL)
im.save(f'{R}/out/piccolo.png')
b = Image.new('RGBA', im.size, (255,255,255,255)); b.alpha_composite(im)
b.resize((im.width*16, im.height*16), Image.NEAREST).save(f'{R}/out/piccolo_20x.png')
print(im.size)
