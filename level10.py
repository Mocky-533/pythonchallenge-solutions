a = ['1']
c1, c2 = '1', ''
for _ in range(30):
    count, i, j = 0, 0, 0
    while i < len(c1):
        while j < len(c1):
            if c1[i] == c1[j]:
                count += 1
                j += 1
            else:
                break
        c2 += str(count) + c1[i]
        i = j
        count = 0
    a.append(c2)
    c1 = c2
    c2 = ''
print(len(a[30]))