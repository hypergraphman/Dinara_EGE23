def negative(n):
    s1 = f'{n:b}'
    s2 = s1.rjust(8, '0')
    res = ''
    for d in s2:
        if d == '0':
            res += '1'
        else:
            res += '0'
    return res


def negative_2(n):
    return f'{255 - n:b}'.rjust(8, '0')


for i in range(200, 250):
    print(i, negative(i), negative_2(i))
