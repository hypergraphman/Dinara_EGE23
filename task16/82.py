def f(n):
    if n <= 5:
        return n
    if n % 4 == 0:
        return n + f(n / 2 - 1)
    if n % 4:
        return n + f(n + 2)


mx = 0
for n in range(1, 1000):
    try:
        f(n)
        mx = max(mx, n)
    except:
        pass
print(mx)