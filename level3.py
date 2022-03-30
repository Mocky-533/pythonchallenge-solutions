import re
with open("assets/txt_for_3.txt", "r") as f:
    line = f.read()
reg=re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
url = reg.findall(line)
for u in url:
    print(u[4], end='')