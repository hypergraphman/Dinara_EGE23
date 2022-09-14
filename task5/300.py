def f(n):
    step1 = f'{n:b}'
    step2 = step1[1:]
    if step2.count('1') % 2 == 0:
        step3 = '10' + step2
    else:
        step3 = '1' + step2 + '0'
    return int(step3,2)


mx = 0
for i in range(1, 451):
    if f(i) < 450 and f(i) > mx:
            mx = f(i)
print(mx)
