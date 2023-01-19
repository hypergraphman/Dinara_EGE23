def f(start, end, com):
    if len(com) > 10:
        return 0
    if start == end and len(com) == 10:
        return 1
    return f(start + 4, end, com + '1') + f(start + 7, end, com + '2') + f(start // 2, end, com + '3')


print(f(1, 1, ''))