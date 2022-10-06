for x in range(100):
    for y in range(100):
        for z in range(100):
            f1 = x + y + z
            f2 = x + 2 * z
            f3 = x + z
            if f1 == 51 and f2 == 29 and f3 == 23:
                print(x, y, z)
