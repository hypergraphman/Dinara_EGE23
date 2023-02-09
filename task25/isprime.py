def f(n):
    deliteli = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            deliteli.add(d)
            deliteli.add(n // d)
    return sorted(deliteli)

print(f(100))