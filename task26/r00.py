with open('26.txt') as f:
    v, n = map(int, f.readline().split())
    a = sorted(map(int, f.readlines()))
    # a = [int(x) for x in f.readlines()]
    # a.sort()

k = 0
while v - a[k] >= 0:
    v -= a[k]
    k += 1
print(k)

v += a[k - 1]
print(v)
print(*a)
while v - a[k] >= 0:
    k += 1
print(a[k - 1])