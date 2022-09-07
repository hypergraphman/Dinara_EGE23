def f(n):
    d = list(map(int, str(n)))
    # digits = []
    # while n > 0:
    #     digits.append(n % 10)
    #     n //= 10
    # d0 = n // 1 % 10
    # d1 = n // 10 % 10
    # d2 = n // 100 % 10
    # d3 = n // 1000 % 10
    # sums = sorted([d0 + d1, d1 + d2, d2 + d3])
    sums = sorted([d[0] + d[1], d[1] + d[2], d[2] + d[3]])
    return str(sums[1]) + str(sums[2])


for i in range(1000, 10000):
    if f(i) == '511':
        print(i)