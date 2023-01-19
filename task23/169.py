def f(start, end, a):
    if len(a) > 9:
        return 0
    if start == end and 1 < len(a) <= 9:
        return 1
    return f(start + 3, end, a + [start + 3]) + f(start - 1, end, a + [start - 1])


print(f(1, 1, [1]))