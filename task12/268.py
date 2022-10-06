for x in range(100):
    for y in range(100):
        for z in range(100):
            f1 = 2 * y + z
            f2 = y + z
            f3 = x + 2 * y + z
            if f1 == 59 and f2 == 40 and f3 == 66:
                print(x, y, z)