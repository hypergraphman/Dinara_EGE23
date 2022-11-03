def f(n):
    res = 1
    for x in range(1, n + 1):
        res *= x
    return res
print(f(2023) / f(2020))