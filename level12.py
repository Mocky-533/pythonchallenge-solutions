with open("assets/evil2.gfx", "rb") as f:
    text = f.read()
for i in range(5):
    with open(f'assets/{i}.jpg', 'wb') as f:
        f.write(text[i::5])