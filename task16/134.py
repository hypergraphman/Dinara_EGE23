from functools import cache


@cache
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1) + 1


for i in range(400, 3400, 400):
    f(i)

print(f(3303)/f(3300))

a = [0] * 3400
for i in range(1, 3400):
    if i == 1:
        a[i] = 1
    if i > 1:
        a[i] = i * a[i - 1] + 1

print(a[3303]/a[3300])

p = 1
p3303 = None
p3300 = None
for i in range(2, 3400):
    p = i * p + 1
    if i == 3303:
        p3303 = p
    if i == 3300:
        p3300 = p
print(p3303 / p3300)
