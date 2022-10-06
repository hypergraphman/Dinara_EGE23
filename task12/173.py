def alg(n):
    d1 = '03175'
    d2 = '2'
    d3 = '46'
    r = ''
    for d in n:
        if d in d1:
            r += d1[(d1.find(d) + 1) % len(d1)]
        elif d in d2:
            r += d2
        elif d in d3:
            r += d3[(d3.find(d) + 1) % len(d3)]
    return r


num = '32006'
for _ in range(13):
    num = alg(num)
print(num)
