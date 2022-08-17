from itertools import permutations


def f(n):
    all_ = list(filter(lambda y: 10 <= y < 100, list(map(lambda x: x[0] * 10 + x[1], permutations(map(int, str(n)), 2)))))
    return max(all_) - min(all_)


search = 100
while f(search) != 40:
    search += 1
print(search)