"""Vegeta head (23 wide) on the face geometry of the game's Shanks head; hair redrawn as Vegeta's flame."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
TOP = [  # five big flame spikes leaning up/back, forehead opens at the front
"..........o............",
".........oh.......o....",
"...o.....ohh.....oh....",
"...oo...ohhh....ohh....",
"....oh..ohhHo..ohhh..o.",
"....ohh.ohhHh.ohhHh.oh.",
".o..ohhhohhHhoohhHhohh.",
".oo.ohhHhhhHhhhhhHhhho.",
"..oohhhHhhhhHhhhhHhhho.",
"...ohhhhHhhhHhhhhhhho..",
"oo.ohhhhHhhhhhhhhhhho..",
".oohhhhhhhhhhhhhhhhho..",
"..ohhhhhhhhhhhhhhhhho..",
".ohhhhhhhhhhhhhhhhhso..",
"ohhhhhhhhhhhhhhhhhsso..",
".ohhhhhhhhhhhhhhhhssso.",
]
# left 12 px: Shanks' rows 8-21 (back of head, ear, jaw) | right 11 px: Vegeta's forehead, peak, brow, eye
FACE = [
(".ohhhhhhhhhh", "hhhhhsssso."),
("oohhhhhhHhhh", "hhhhssssso."),   # high forehead
(".ohhhhhhhhhh", "hhhsssssso."),
("..ohhhhhhhhh", "hhssssssso."),   # hairline slants back to the temple point (widow's peak)
("...ohhhhhhhh", "hhsooossso."),   # heavy brow
("....ohhoSsoh", "ossowoooso."),   # ear | narrow angry eye, pupil at the front
("....ohoSStsh", "ossSwoSssso"),   # nose
("....ohoSttso", "osssSsssso."),
(".....ooSSsso", "sssssssso.."),
("......osssss", "ssssssmmo.."),   # scowl
(".......ossss", "sssssSSo..."),
("........oSSS", "SSSSSSo...."),   # jaw
("..........oS", "Sooooo....."),
("..........oS", "So........."),   # neck
]
rows = TOP + [a + b for a, b in FACE]
for i, r in enumerate(rows): assert len(r) == 23, (i, len(r), r)
PAL = """o 1d1c21
h 2c2a36
H 4a4860
s f2c6a5
S d79f7b
t ae7862
w f9f5ec
m 8a4040"""
open(os.path.join(HERE, '..', 'chars', 'vegeta_head.txt'), 'w').write("# palette\n" + PAL + "\n# grid\n" + '\n'.join(rows) + '\n')
