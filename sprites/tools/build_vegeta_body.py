"""Vegeta armour body, 20 px wide (Luffy-width), rows 30-55 of the sprite. Writes chars/vegeta_body.txt"""
import os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
BODY = [
".oooooooSSSoooooooo.",
"oggGoaaaaaaaaaaoggGo",   # gold shoulder pads, white chest plate
"ogggoaaaaaAaaaaogggo",
"oGGGobaaaaAaaaabGGGo",
".oGobbaaaaAaaaabboo.",
".obooooooooooooooo..",   # crossed forearm (outlined)
".obobbbbbbbbbbbaaao.",   # glove fist on the right
"oaaoBBBBBBBBBBBaaAo.",   # back glove peeks out on the left
"oaAAooooooooooooaoo.",
".oAoaaaaaaAaaaaaao..",
"..oaaaaaaaAaaaaaAo..",
"..oAAAAAAAAAAAAAAo..",
"..oggGbbbbbbbbGggo..",   # gold hip flaps
"..oGGobbbbbbbbbGGo..",
"...oobbbbbbobbbbo...",
"...obbbbBoobbbbBo...",
"...obbbbBo.obbbbBo..",
"...obbbbBo.obbbbBo..",
"..oaaaaaAo.oaaaaaAo.",   # tall white boots
"..oaaaaaAo.oaaaaaAo.",
"..oaaaaaAo.oaaaaaAo.",
".oaaaaaaAo.oaaaaaaAo",
".oaaaaaaAo.oaaaaaaAo",
"oggaaaaAo..oaaaaaggo",   # gold toe caps
"ogggAAAAo..oAAAAgggo",
"oooooooo...ooooooooo",
]
for i, r in enumerate(BODY): assert len(r) == 20, (i, len(r))
PAL = """o 1d1c21
s f2c6a5
S d79f7b
b 3c58c0
B 263c8c
a f2f2f6
A bcc2d4
g e8bc48
G a8822c"""
open(f'{R}/chars/vegeta_body.txt', 'w').write("# palette\n" + PAL + "\n# grid\n" + '\n'.join(BODY) + '\n')
