for x in range(0, 50):
    for y in range(0, 50):
        for z in range(0, 50):
            if (0 * x + 0 * y + 0 * z == 0 and
                    2 * x + 3 * y + 6 * z == 186 and
                    0 * x + 1 * y + 1 * z == 26):
                print(x, y, z, x + y + z)
