from functools import lru_cache


@lru_cache
def f(start, end, lst):
    if start > end:
        return 0
    if start == end:
        for p1, p2, p3 in zip(lst, lst[1:], lst[2:]):
            if (p1 + p2 + p3) % 11 == 0:
                return 1
        return 0
    return (f(start + 2, end, tuple(list(lst) + [start + 2])) +
            f(start * 3, end, tuple(list(lst) + [start * 3])) +
            f(start * 4, end, tuple(list(lst) + [start * 4])))


print(f(1, 600, (1,)))