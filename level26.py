import hashlib

standard = "bbb8b499a0eef99b52c7f13f4e78c24b"
with open("assets/maze/mybroken.zip", "rb") as f:
    original = f.read()
# print(len(original))
flag = 0
for i in range(len(original)):
    for j in range(256):
        data = original[:i] + bytes([j]) + original[i+1:]
        if hashlib.md5(data).hexdigest() == standard:
            flag = 1
            break
    if flag:
        break
print(flag)
with open("assets/maze/new.zip", 'wb') as new_file:
    new_file.write(data)