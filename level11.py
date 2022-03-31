import cv2
import numpy as np
img = cv2.imread("assets/cave.jpg")
x, y, _ = img.shape
img1, img2 = np.zeros((x//2,y//2,3), np.uint8), np.zeros((x//2,y//2,3), np.uint8)
for i in range(x):
    for j in range(y):
        if (i+j)%2 == 1:
            img1[i//2][j//2] = img[i][j]
        else:
            img2[i//2][j//2] = img[i][j]
cv2.imshow("odd", img1)
cv2.imshow("even", img2)
cv2.waitKey(0)