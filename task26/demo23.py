with open('26demo23.txt') as f:
    n = int(f.readline())
    a = sorted(map(int, f.readlines()))[::-1]

k = [a[0]]
for box in a:
    if k[-1] - box >= 3:
        k.append(box)
print(len(k), k[-1])