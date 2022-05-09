import numpy as np
import math, cv2

# def resolve(n: int):
#     factors = []
#     for i in range(2, int(math.sqrt(n))):
#         if n % i == 0:
#             factors.append([i, int(n/i)])
#     return factors


with open("assets/yankeedoodle.csv", "r") as f:
    data = [x.strip() for x in f.read().split(",")]
content = np.array([data])
n = len(content[0])
# print(n)
# height, width = resolve(n)[0]
# content.resize((width, height))
# cv2.imshow("img", content)
# cv2.waitKey()
info = []
for i in range(0, n-2, 3):
    n = chr(int(str(content[0][i])[5] + str(content[0][i+1])[5] + str(content[0][i+2])[6]))
    info.append(n)
print("".join(info))