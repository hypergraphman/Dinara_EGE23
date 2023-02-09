from functools import lru_cache

@lru_cache
def f(n):
    deliteli = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            deliteli.add(d)
            deliteli.add(n // d)
    return sorted(deliteli)


a = []
n = 121332131
while len(a) != 5:
    if len(f(n)) > 2 and f(n)[1] > 999 and len(f(f(n)[1])) == 2:
        a.append((n, f(n)[1]))
    n -= 2
print(*a, sep='\n')