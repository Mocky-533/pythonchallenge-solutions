from PIL import Image
import bz2, keyword

img = Image.open('assets/zigzag.gif')
width, height = img.size
palette = img.getpalette()[::3]
trans = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))
raw = img.tobytes()
img_b = bytes.translate(raw, trans)
raw, img_b = raw[1:], img_b[:-1]
diff_raw, diff_b, pos = [], [], []
for i in range(len(raw)):
    if raw[i] != img_b[i]:
        diff_raw.append(raw[i])
        diff_b.append(img_b[i])
        pos.append(i)
newimg = Image.new("1", img.size, 1)
for v in pos:
    newimg.putpixel((v%width, v//width), 0)
# newimg.show()
clue1, clue2 = bytes(diff_raw), bytes(diff_b)
clue1 = bz2.BZ2Decompressor().decompress(clue1)
words = set(clue1.decode().split(' '))
# print(clue1)
for ele in words:
    if not keyword.iskeyword(ele):
        print(ele)
