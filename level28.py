import cv2
import numpy as np

img = cv2.imread("assets/bell.png")
height, width, _ = img.shape
b, g, r = cv2.split(img)
g1 = np.reshape(g, (1, -1))[0].astype(np.int8)
g2= g1[0::2] - g1[1::2]
l = []
for i in g2:
    if i != 42 and i != -42:
        l.append(i)
# print("".join(l))
print("".join(chr(abs(j)) for j in l))