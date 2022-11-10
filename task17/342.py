data = tuple(map(int, open('17-342.txt').readlines()))
c = 0
mn = 10 ** 10
mx = 0
mn_sum = 10 ** 10
for el in data:
    if el % 37 == 0:
        mn = min(mn, el)
    if el % 73 == 0:
        mx = max(mx, el)
if mx < mn:
    mx, mn = mn, mx
for i in range(1, len(data)):
    x1, x2 = data[i - 1], data[i]
    if (mn < x1 < mx and not (mn < x2 < mx) or
       mn < x2 < mx and not (mn < x1 < mx)):
        c += 1
        mn_sum = min(mn_sum, x1 + x2)
print(c, mn_sum)

