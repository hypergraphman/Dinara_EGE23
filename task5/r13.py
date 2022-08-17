def f(n):
    step1 = f'{n:b}'
    step2a = step1 + str(sum(map(int, step1)) % 2)
    step2b = step2a + str(sum(map(int, step2a)) % 2)
    return int(step2b, 2)


search = 1
while f(search) <= 77:
    search += 1
print(search)