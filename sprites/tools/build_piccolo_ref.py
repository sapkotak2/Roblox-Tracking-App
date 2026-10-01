"""Piccolo - drawn on the user's reference sprite layout (sticker, ~19 x 46 grid, facing left; mirrored to face
right). Fill-only authoring, 1px dark outline added automatically. Writes out/piccolo.png"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from fillgrid import Grid, render
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PAL = {'g': (124,214,60), 'G': (70,160,44), 'd': (34,96,30), 'r': (236,86,118), 'R': (250,170,190), 'w': (250,250,250),
       'k': (16,16,20), 'P': (126,60,168), 'p': (88,40,124), 'b': (96,196,236), 'B': (60,140,200), 'n': (166,112,62), 'N': (112,72,36)}
g = Grid(20, 44)
# antenna curls (top-left)
g.px([(4,0),(5,0),(3,1),(6,1),(3,2),(5,2),(4,3),(8,1),(8,2),(9,0)], 'g')
# head dome (face on the left = front in the reference) - bigger, egg-shaped
DOME = {2:(7,11),3:(5,13),4:(4,14),5:(3,15),6:(3,16),7:(3,16),8:(3,16),9:(3,16),10:(3,15),11:(3,15),12:(4,14),13:(5,13),14:(6,12)}
for y, (a, b) in DOME.items(): g.sp(y, 'g', a, b)
for y, (a, b) in {4:(0,0),5:(0,1),6:(0,2),7:(1,2),8:(2,2)}.items(): g.sp(y, 'g', a, b)         # front ear (triangle)
for y, (a, b) in {3:(19,19),4:(18,19),5:(17,19),6:(17,18),7:(17,17)}.items(): g.sp(y, 'g', a, b)  # back ear
g.px([(1,6),(18,5)], 'G')
for y, (a, b) in DOME.items():                                 # back-of-head shading
    g.sp(y, 'G', max(a, b - 4), b)
    if y >= 5: g.sp(y, 'd', b, b)
g.px([(7,3),(8,4),(10,3),(11,4)], 'G')                         # forehead ridges
# angry face: heavy brow sloping down to the nose (left), glaring eye, frown
g.px([(3,8),(4,8),(5,8),(6,8),(7,7),(8,7),(9,7)], 'k')
g.px([(4,7),(5,7),(6,7),(7,6),(8,6)], 'd')
g.px([(5,9),(6,9),(5,10),(6,10)], 'w'); g.px([(4,9),(4,10),(7,9)], 'k')
g.px([(5,11),(6,11),(8,10),(9,11),(10,12)], 'G')
g.px([(5,12),(6,12),(7,12),(4,13),(8,13)], 'k')
# neck + purple gi
g.sp(14, 'g', 6, 11); g.sp(15, 'G', 7, 10)
g.sp(15, 'P', 3, 6); g.sp(15, 'P', 11, 15)
g.sp(16, 'P', 2, 16); g.px([(8,16),(9,16)], 'G')
# crossed arms: outer upper arms carry the pink markings, forearms cross in front, hands at the ends
g.sp(17, 'r', 1, 2); g.sp(17, 'g', 3, 14); g.sp(17, 'r', 15, 16); g.px([(17,17)], 'R')
g.sp(18, 'r', 1, 2); g.sp(18, 'g', 3, 15); g.px([(14,18),(15,18)], 'G'); g.sp(18, 'R', 16, 17)
g.sp(19, 'R', 1, 2); g.sp(19, 'G', 3, 14); g.sp(19, 'r', 15, 16)
g.sp(20, 'r', 1, 2); g.sp(20, 'g', 3, 15); g.sp(20, 'r', 16, 16); g.px([(17,20)], 'R')
g.sp(21, 'g', 2, 14); g.px([(2,21),(3,21)], 'G')
g.sp(22, 'P', 3, 15); g.px([(14,22),(15,22)], 'p')
g.sp(23, 'P', 3, 15); g.sp(23, 'b', 5, 12); g.sp(24, 'P', 3, 15); g.sp(24, 'B', 5, 12)
# baggy pants tapering to the ankles, brown shoes
g.sp(25, 'P', 3, 15)
for y in range(26, 31): g.sp(y, 'P', 2, 16)
for y in range(31, 37): g.sp(y, 'P', 2, 8); g.sp(y, 'P', 10, 16)
for y in range(37, 40): g.sp(y, 'P', 3, 7); g.sp(y, 'P', 11, 15)
for y in range(22, 40):                                        # pants/gi shading on the back side
    idx = [x for x in range(20) if g.g[y][x] == 'P']
    if idx: g.px([(idx[-1], y), (idx[-1] - 1, y)], 'p')
g.px([(5,28),(5,29),(6,30),(12,29),(12,30),(13,31),(9,27),(9,28)], 'p')   # folds
g.sp(40, 'n', 2, 7); g.sp(40, 'n', 11, 16)
for y in (41, 42): g.sp(y, 'n', 0, 7); g.sp(y, 'n', 11, 18)
g.sp(43, 'N', 0, 7); g.sp(43, 'N', 11, 18)
im = render(g, PAL)
im.save(f'{R}/chars/piccolo_ref_layout.png')
im = im.transpose(Image.FLIP_LEFT_RIGHT); im.save(f'{R}/out/piccolo.png')
b = Image.new('RGBA', im.size, (255,255,255,255)); b.alpha_composite(Image.open(f'{R}/chars/piccolo_ref_layout.png'))
b.resize((im.width*20, im.height*20), Image.NEAREST).save(f'{R}/out/piccolo_20x.png')
print(im.size)
