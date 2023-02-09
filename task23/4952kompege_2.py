from functools import lru_cache


@lru_cache
def f(p0, end, p1, p2, flag):
    if (p0 + p1 + p2) % 11 == 0:
        flag = True
    if p0 > end:
        return 0
    if p0 == end and flag:
        return 1
    return (f(p0 + 2, end, p0, p1, flag) +
            f(p0 * 3, end, p0, p1, flag) +
            f(p0 * 4, end, p0, p1, flag))


print(f(1, 600, 0, 0, False))