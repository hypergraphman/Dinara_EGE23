def f(n):
    if n == 0:
        return 0
    if n % 2:
        return 1 + f(n - 1)
    return f(n // 2)


for i in range(1, 100):
    print(i, f(i), f'{i:b}')