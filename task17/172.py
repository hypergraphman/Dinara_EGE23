data = tuple(map(int, open('17-4.txt').readlines()))
mx = 0
sums = 0
for n in data:
    if n % (2 ** 4) == 9 and n % 25 == 6:
        mx = max(mx, n)
        sums += n
print(mx, sums)
    