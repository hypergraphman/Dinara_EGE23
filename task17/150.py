data = tuple(map(int, open('17-1.txt').readlines()))
# print(data)
c = 0
mn = 10 ** 10
for i in range(1, len(data)):
    x1, x2 = data[i - 1], data[i]
    if x1 % 7 == 0 and x2 % 17 or x2 % 7 == 0 and x1 % 17:
        c += 1
        if x1 + x2 < mn:
            mn = x1 + x2
print(c, mn)