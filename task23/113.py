def f(start, end, cmds):
    if start > end or len(cmds) > 7:
        return 0
    if start == end:
        print(cmds)
        return 1
    return f(start + 1, end, cmds + '1') + f(start + 5, end, cmds + '2') + f(start * 3, end, cmds + '3')


print(f(1, 227, ''))