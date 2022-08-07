# import requests
from PIL import Image
from math import sqrt
# import numpy as np
# with open("assets/beer2.png", 'wb') as f:
#     f.write(requests.get(url="http://www.pythonchallenge.com/pc/rock/beer2.png", auth=("kohsamui", "thailand")).content)
"""
If you are blinded by the light,
remove its power, with its might.
Then from the ashes, fair and square,
another truth at you will glare.
"""

img = Image.open("assets/beer2.png")
values = list(img.getdata())
while True:
    max_value = max(values)
    values = [i for i in values if i != max_value]
    if len(values) == 0:
        break
    root = sqrt(len(values))
    if root == int(root):
        output = Image.new("L", (int(root), int(root)))
        max_value = max(values)
        l = [255 if j == max_value else 0 for j in values]
        output.putdata(l)
        output.save(f"assets/33/{int(root)}.png")
