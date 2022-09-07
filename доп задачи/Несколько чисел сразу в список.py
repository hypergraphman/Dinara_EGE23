a = [1, 2, 3]
print(a)
a += [6, 7, 8, 9]
print(a)
print(''.join(map(str, a)))
res = ''
for el in a:
    res += str(el)
print(res)