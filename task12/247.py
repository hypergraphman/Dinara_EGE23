def alg(line: str):
    while '111' in line:
        line = line.replace('111', '22', 1)
        line = line.replace('222', '11', 1)
    return line


for i in range(51, 60):
    print(i, alg('1' * i))
