import os, sys
from pix import sheet
from chars import ALL
out = os.path.join(os.path.dirname(__file__), '..', 'out'); os.makedirs(out, exist_ok=True)
items = []
for name, fn in ALL:
    im = fn().image(); im.save(f'{out}/{name.lower()}.png'); items.append((name, im))
sheet(items, f'{out}/sheet_light.png', scale=7, cols=4)
sheet(items, f'{out}/sheet_dark.png', scale=7, cols=4, bg=(10, 14, 26))
print('built', len(items))
