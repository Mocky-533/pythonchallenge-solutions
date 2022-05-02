from PIL import Image
import requests, wave

# Section 1.
# file downloading
i = 1
while True:
    url = f"http://www.pythonchallenge.com/pc/hex/lake{i}.wav"
    r = requests.get(url, auth=requests.auth.HTTPBasicAuth('butter', 'fly'))
    if r.status_code != 200:
        break # break when url is invalid
    with open(f"assets/25/lake{i}.wav", 'wb') as f:
        f.write(r.content)
    i += 1

# Section 2
# wav files to image
j = 0
img = Image.new('RGB', (300, 300), 0)
waves = [wave.open(f"assets/25/lake{i}.wav", 'rb') for i in range(1, 26)]
for audio in waves:
    tmp = Image.frombytes("RGB", (60, 60), bytes(audio.readframes(10800)))
    img.paste(tmp, [j%5*60, j//5*60])
    j += 1
img.show()