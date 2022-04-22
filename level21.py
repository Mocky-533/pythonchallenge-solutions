import zlib, bz2
# from collections import Counter
with open('assets/21/package.pack', 'rb') as f:
    data = f.read()
logs = []
while True:
    if data[:2].hex() == '789c':
        data = zlib.decompress(data)
        logs.append("*")
    elif data[:2].hex() == "425a":
        data = bz2.decompress(data)
        logs.append("@")
    elif data[-2:].hex() == "9c78":
        data = zlib.decompress(data[::-1])
        logs.append("#")
    elif data[-2:].hex() == "5a42":
        data = bz2.decompress(data[::-1])
        logs.append("+")
    else:
        break
# count = Counter(logs)
lines = "".join(logs).split("#")
for line in lines:
    print(line)
