def f(n):
    d = list(map(int, str(n)))
    sums = sorted([d[0] + 6, d[1] + 9, d[2] + 4], reverse=True)
    return ''.join(map(str, sums))


for i in range(100, 1000):
    if f(i) == '11108':
        print(i)
        break
