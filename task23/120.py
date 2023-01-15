def f(start, end, cmds):
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 1, end, cmds + '1') + f(start + 5, end, cmds + '2') + f(start * 3, end, cmds + '3')


i = 3
while f(1, i, '') != 175:
    i += 1
print(i)
