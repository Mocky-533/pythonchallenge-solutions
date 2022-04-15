# section 1
import base64
with open("assets/txt_for_19.txt", "r") as f:
    content = f.read()
audio = base64.b64decode(content)
with open("assets/indian.wav", 'wb') as f:
    f.write(audio)


# section 2
import wave

with wave.open('assets/indian.wav', 'rb') as sound:
    with wave.open('assets/results.wav', 'wb') as output:
        output.setparams(sound.getparams())
        for i in range(sound.getnframes()):
            frame = sound.readframes(1)
            output.writeframes(frame[::-1])


