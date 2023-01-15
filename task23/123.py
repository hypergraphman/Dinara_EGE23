def f(start, end, cmds):
    if start > end or len(cmds) > 5:
        return 0
    if start == end:
        return 1
    return f(start + 1, end, cmds + '1') + f(start * 2, end, cmds + '2') + f(start + start % 4, end, cmds + '3')


k = 0
for i in range(1, 80 + 1):
    if f(i, 80, ''):
        k += 1
print(k)
