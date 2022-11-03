for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        dxa = x % a != 0
        dx6 = x % 6 == 0
        dx9 = x % 9 != 0
        if not (dxa <= (dx6 <= dx9)):
            is_a = False
            break
    if is_a:
        print(a)


lst = []
for a in range(1, 1000):
    if all([(x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0)) for x in range(1, 1000)]):
        lst.append(a)
print(*lst)