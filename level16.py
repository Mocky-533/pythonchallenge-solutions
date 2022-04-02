from PIL import Image

img = Image.open("assets/mozart.gif")
for pos_y in range(img.size[1]):
    pixels = [img.getpixel((pos_x, pos_y)) for pos_x in range(img.size[0])]
    flag = pixels.index(195)
    pixels = pixels[flag:] + pixels[:flag]
    for pos_x in range(img.size[0]):
        img.putpixel((pos_x,pos_y), pixels[pos_x])
img.show()


# print(pixels)