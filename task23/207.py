def f(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    return f(start - 1, end) + f(start // 2, end)


print(f(30, 12) * f(12, 1))