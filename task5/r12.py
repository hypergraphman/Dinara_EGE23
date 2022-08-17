from itertools import permutations


def f(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    all_ = []
    for x1, x2 in list(permutations([d1, d2, d3], 2)):
        if 10 <= x1 * 10 + x2 <= 99:
            all_.append(x1 * 10 + x2)
    return max(all_) - min(all_)


search = 100
while f(search) != 40:
    search += 1
print(search)