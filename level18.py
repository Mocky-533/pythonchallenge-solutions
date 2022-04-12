import gzip, difflib
file1, file2 = [], []
with gzip.open('assets/deltas.gz', 'rb') as f:
    content = f.readline().decode()
    while content:
        file1.append(content[:53]+'\n')
        file2.append(content[56:])
        content = f.readline().decode()
diff = difflib.Differ().compare(file1, file2)
l1, l2, common = [], [], []
for line in diff:
    if line[0] == '-':
        l1.append(line[2:-1])
    elif line[0] == '+':
        l2.append(line[2:-1])
    else:
        common.append(line[2:-1])
print(f"l1: {l1}")
print(f"l2: {l2}")
print(f"common: {common}")
with open('assets/lvl18_1.png', 'wb') as f1:
    for line in l1:
        f1.write(bytes([int(o, 16) for o in line.strip().split(" ") if o]))
with open('assets/lvl18_2.png', 'wb') as f2:
    for line in l2:
        f2.write(bytes([int(o, 16) for o in line.strip().split(" ") if o]))
with open('assets/lvl18_3.png', 'wb') as f3:
    for line in common:
        f3.write(bytes([int(o, 16) for o in line.strip().split(" ") if o]))

