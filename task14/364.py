lst = []
for x in range(55):
    a = int('Z', 36) * 55 ** 3 + x * 55 ** 2 + int('Y', 36) * 55 + int('X', 36)
    b = 2 * 55 ** 3 + int('X', 36) * 55 ** 2 + x * 55 + int('Y', 36)
    if (a - b) % 29 == 0:
        print(x)
        lst.append(a - b)
print(max(lst) - min(lst))
