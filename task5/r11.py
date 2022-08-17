def f(n):
    step1 = f'{n:b}'
    step2 = step1[1:]
    step3 = int(step2, 2)
    return n - step3


res = set()
for i in range(500, 5000 + 1):
    res.add(f(i))
print(len(res))
