"""Vegeta head v13: same skull/face size as the game's Luffy (25 wide, face x11-24), 3/4 view facing right,
plus ~6 rows of upright spikes (user's pixel references). Authored as spans per row; '.' = empty.
o outline  h hair  H hair light  s skin  S skin shade  w eye white"""
import os
from PIL import Image
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W, H = 26, 28
g = [['.'] * W for _ in range(H)]
def sp(y, *spans):
    for c, a, b in spans:
        for x in range(a, b + 1): g[y][x] = c
# ---- hair: three upright spikes (each leans slightly back), back spikes, widow's peak
sp(0, ('o',4,4))
sp(1, ('o',3,3),('h',4,4),('o',5,5))
sp(2, ('o',3,3),('h',4,5),('o',6,6),                      ('o',15,15))
sp(3, ('o',3,3),('h',4,6),('o',7,7),          ('o',14,14),('h',15,15),('o',16,16))
sp(4, ('o',3,3),('h',4,7),('o',8,8),          ('o',13,13),('h',14,16),('o',17,17))
sp(5, ('o',3,3),('h',4,8),('o',9,9),          ('o',12,12),('h',13,17),('o',18,18))
sp(6, ('o',3,3),('h',4,9),('o',10,11),('h',12,18),('o',19,19),                    ('o',23,23))
sp(7, ('o',2,2),('h',3,19),('o',20,20),                               ('o',22,22),('h',23,23),('o',24,24))
sp(8, ('o',1,1),('h',2,20),('o',21,21),('h',22,23),('o',24,24))
sp(9, ('o',0,0),('h',1,24),('o',25,25))
sp(10,('o',1,1),('h',2,24),('o',25,25))
sp(11,('o',2,2),('h',3,24),('o',25,25))
sp(12,('o',2,2),('h',3,24),('o',25,25))
sp(13,('o',1,1),('h',2,24),('o',25,25))
# ---- face: forehead either side of the V peak, temple lock on the right
sp(14,('o',0,0),('h',1,11),('o',12,12),('s',13,15),('o',16,16),('h',17,24),('o',25,25))
sp(15,('o',1,1),('h',2,10),('o',11,11),('s',12,17),('o',18,18),('h',19,19),('o',20,20),('s',21,22),('o',23,23),('h',24,24),('o',25,25))
sp(16,('o',2,2),('h',3,9),('o',10,10),('s',11,18),('o',19,19),('s',20,23),('o',24,24),('h',24,24),('o',25,25))
# angry V brows meeting at the nose bridge
sp(17,('o',2,2),('h',3,8),('o',9,9),('s',10,12),('o',13,15),('s',16,21),('o',22,23),('s',24,24),('o',25,25))
sp(18,('o',1,1),('h',2,7),('o',8,8),('s',9,15),('o',16,19),('o',20,21),('s',22,24),('o',25,25))
# big glaring eye (white + pupil at the front) under the brow; ear on the left
sp(19,('o',0,0),('h',1,5),('o',6,6),('s',7,8),('o',9,9),('s',10,15),('w',16,17),('o',18,18),('s',19,23),('o',24,24))
sp(20,('o',1,1),('h',2,5),('o',6,6),('s',7,7),('S',8,8),('s',9,15),('w',16,17),('o',18,18),('s',19,23),('S',24,24),('o',25,25))
sp(21,('o',2,2),('h',3,5),('o',6,6),('s',7,7),('S',8,8),('s',9,15),('S',16,18),('s',19,24),('o',25,25))
sp(22,('o',2,2),('h',3,5),('o',6,6),('s',7,8),('o',9,9),('s',10,19),('S',20,20),('s',21,23),('o',24,24))
sp(23,('o',3,3),('h',4,5),('o',6,7),('s',8,23),('o',24,24))
# frown, square chin
sp(24,('o',4,5),('h',5,5),('o',6,7),('S',8,9),('s',10,17),('o',18,21),('s',22,22),('o',23,23))
sp(25,('o',7,8),('S',9,10),('s',11,20),('S',21,22),('o',23,23))
sp(26,('o',9,10),('S',11,13),('s',14,19),('S',20,21),('o',22,22))
sp(27,('o',11,21))
# hair light strands along each spike's front edge (the visible 'curves')
for x, y in ((5,2),(6,3),(7,4),(8,5),(9,6),(10,7),(11,8),(16,3),(17,4),(18,5),(19,6),(20,7),(21,8),(23,7),(24,9),
             (2,9),(3,10),(4,11),(2,13),(3,14),(3,18),(4,19)):
    if g[y][x] == 'h': g[y][x] = 'H'
PAL = """o 1d1c21
h 2c2a36
H 4e4c66
s f2c6a5
S d79f7b
w f9f5ec"""
open(f'{R}/chars/vegeta_head.txt', 'w').write("# Vegeta head v13 (tools/build_vegeta_head8.py)\n# palette\n" + PAL + "\n# grid\n" + '\n'.join(''.join(r) for r in g) + '\n')
