import cv2
import numpy as np

img = cv2.imread("assets/wire.png")
img1 = np.zeros((300, 300, 3), np.uint8)
img1.fill(200)
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
count, i, pos_x, pos_y = 200, 0, -1, 0
dis = count//2
while dis > 0:
    for dir in dirs:
        dis = count//2
        for _ in range(dis):
            pos_x = pos_x + dir[0]
            pos_y = pos_y + dir[1]
            img1[pos_x, pos_y] = img[0, i]
            i += 1
        count -= 1
cv2.imshow("result", img1)
cv2.waitKey(0)