from itertools import product

print('x y w z')
for x, y, w, z in product([0, 1], repeat=4):
    F = (w and y) or ((x <= w) == (y <= z))
    if not F:
        print(x, y, w, z)
