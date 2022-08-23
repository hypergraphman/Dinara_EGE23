def f(n):
    a = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)


n = int(input())
divs = f(n)
print(divs)
if len(divs) == 2:
    print('Это простое число')
