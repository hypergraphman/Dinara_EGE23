def alg(line):
    while '111' in line or '222' in line:
        if '111' in line:
            line = line.replace('111', '22', 1)
        else:
            line = line.replace('222', '11', 1)
    return line


a = []
for i in range(204):
    r = '1' * i + '2' + '1' * (204 - (i + 1))
    a.append(r)

t = []
for line in a:
    t.append(alg(line))

print(max(t, key=lambda x: len(x)))
