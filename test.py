def f(n):
    d = list(map(int, str(n)))
    sums = sorted([d[0] + 1, d[1] + 9, d[2] + 6], reverse=True)
    return ''.join(map(str, sums))


print(f(835))