from collections import Counter

with open("assets/txt_for_2.txt", "r") as f:
    string = f.read()
count = Counter(string)
print(count)