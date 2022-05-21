import numpy as np
import math, cv2

def resolve(n: int):
    for i in range(2, int(math.sqrt(n))+1):
        if not n % i:
            yield i, n//i


with open("assets/yankeedoodle.csv", "r") as f:
    # data = [float(x.strip()) for x in f.read().split(",")]
    data = [x.strip() for x in f.read().split(",")]
content = np.array([data])
n = len(content[0])
# print(n)
# height, width = list(resolve(n))[0]
# content.resize((width, height))
# cv2.imshow("img", content)
# cv2.waitKey()
info = []
for i in range(0, n-2, 3):
    n = chr(int(str(content[0][i])[5] + str(content[0][i+1])[5] + str(content[0][i+2])[6]))
    info.append(n)
print("".join(info))