def f(n):
    step1 = f'{n:b}'
    if sum(map(int, step1)) % 2 == 0:
        step2 = f'{int(step1[1:], 2):b}'
    else:
        step2 = '1' + step1 + '00'
    if sum(map(int, step2)) % 2 == 0:
        step3 = step2[1:]
    else:
        step3 = '1' + step2 + '00'

    return int(step3, 2)


for i in range(1, 100):
    print(i, f(i))
