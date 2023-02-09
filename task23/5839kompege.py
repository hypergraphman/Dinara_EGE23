from functools import lru_cache


@lru_cache
def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 3, end) + f(start + 2, end) + (0 if start % 2 else f(start * 5 // 2, end))


print(f(1, 40))
