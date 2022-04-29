from PIL import Image, ImageSequence, ImageStat

pic = Image.open("assets/white.gif")
newpic = Image.new("1", (1000, 100))
frames = ImageSequence.Iterator(pic)
coords = []
for frame in frames:
    # stat = ImageStat.Stat(frame)
    # print(stat.extrema)
    for n_y in range(97, frame.size[1]):
        pixels = [frame.getpixel((n_x, n_y)) for n_x in range(frame.size[0])]
        try:
            pos_x = pixels.index(8)
            pos_y = n_y
            coords.append([pos_x, pos_y])
            break
        except ValueError:
            try:
                pos_x = pixels.index((8, 8, 8))
                pos_y = n_y
                coords.append([pos_x, pos_y])
            except ValueError:
                pass
print(coords)
px = py = 0
for coord in coords:
    x = coord[0] - 100
    y = coord[1] - 100
    if x == y == 0:
        x += 100
    px += x
    py += y
    newpic.putpixel((px, py), 1)
newpic.show()