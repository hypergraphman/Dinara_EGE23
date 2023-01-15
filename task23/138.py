def f(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    return f(start - 1, end) + (f(2 ** (len(f'{start:b}') - 1), end) if bin(start).count('1') > 1 else 0)


print(f(17, 1))