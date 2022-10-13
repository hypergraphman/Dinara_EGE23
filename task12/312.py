import itertools as it


def alg(line):
    while '>1' in line or '>2' in line or '>0' in line:
        if '>1' in line:
            line = line.replace('>1', '22>', 1)
        if '>2' in line:
            line = line.replace('>2', '00>', 1)
        if '>0' in line:
            line = line.replace('>0', '11>', 1)
        line = line.replace('>', '1', 1)
    return line


n = 41
is_finish = False
while not is_finish:
    for s in it.product('012', repeat=3):
        line = '>'
        line += ''.join(s)
        line += '0' * (n - s.count('0')) + '1' * (n - s.count('1')) + '2' * (n - s.count('2'))
        r = alg(line)
        if sum(map(int, r)) % 100 == 77:
            print(line)
            print(r)
            print(n)
            is_finish = True
    n += 1