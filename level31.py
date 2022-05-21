from PIL import Image
from math import sqrt

# def resolve(n: int):
#     for i in range(2, int(sqrt(n))+1):
#         if not n % i:
#             yield i, n//i

def mandelbrot(size: tuple):
    left, top, width, height = 0.34, 0.57, 0.036, 0.027
    iteration = 128
    xstep, ystep = width/size[0], height/size[1]
    for y in range(size[1]-1, -1, -1):
        for x in range(size[0]):
            c, z = complex(left+x*xstep, top+y*ystep), complex(0, 0)
            for count in range(iteration):
                z = z**2 + c
                if abs(z) > 2:
                    break
            yield count

img = Image.open("assets/mandelbrot.gif")
# print(img.size)
# newimg = img.copy()
# newimg.putdata(list(mandelbrot(img.size)))
# newimg.show()
diff = [(a - b) for a, b in zip(img.getdata(), list(mandelbrot(img.size))) if a != b]
# print(list(resolve(len(diff))))

result = Image.new("1", (23, 73))
result.putdata([(i > 0) and 1 or 0 for i in diff])
result.show()