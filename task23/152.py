def f(start, end, s):
    if start > end:
        return 0
    if start == end and (17 in s or 23 in s):
        return 1
    elif start == end:
        return 0
    return f(start + 1, end, s | {start}) + f(start +2, end, s | {start})


print(f(11, 29, set()))