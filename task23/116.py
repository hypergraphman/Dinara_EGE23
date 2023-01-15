def f(start, end, cmds):
    if start > end:
        return 0
    if len(cmds) == 4:
        a.add(start)
        return 1
    return f(start + 1, end, cmds + '1') + f(start + 5, end, cmds + '2') + f(start * 3, end, cmds + '3')


a = set()
print(f(1, 250, ''))
print(len(a))