def f(start, end, s):
    if start in s or not (-40 <= start <= 40):
        return 0
    if start == end:
        return 1
    return f(start + 2, end, s | {start}) + f(start - 3, end, s | {start})


print(f(1, 30, set()))