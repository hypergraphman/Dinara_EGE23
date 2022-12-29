def f(start, end):
    if start == 25:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 1, end) + f(start * 2, end)


print(f(2, 14) * f(14, 29))
