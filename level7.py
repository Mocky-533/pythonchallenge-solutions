import cv2

img = cv2.imread("assets/oxygen.png")
offset1, offset2, offset3 = 7, 8, 9
x, y, z, m = 0, 0, 0, int(img.shape[0] / 2 + 1)
l1, l2, l3 = [], [], []
while x <= img.shape[1]:
    px1 = img[m, x]
    if px1[0] == px1[1] == px1[2]:
        l1.append(px1[0])
    x += offset1
while y <= img.shape[1]:
    px2 = img[m, y]
    if px2[0] == px2[1] == px2[2]:
        l2.append(px2[0])
    y += offset2
while z <= img.shape[1]:
    px3 = img[m, z]
    if px3[0] == px3[1] == px3[2]:
        l3.append(px3[0])
    z += offset3
print(f"offset = 7: {l1}")
print(f"offset = 8: {l2}")
print(f"offset = 9: {l3}")

s1 = [chr(i) for i in l1]
s2 = [chr(i) for i in l2]
s3 = [chr(i) for i in l3]
print(f"offset = 7: {''.join(s1)}")
print(f"offset = 8: {''.join(s2)}")
print(f"offset = 9: {''.join(s3)}")

ascii = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join([chr(i) for i in ascii]))