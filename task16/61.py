def f(n):
    if n <= 15:
        return n * n + 3 * n + 9
    if n % 3:
        return f(n - 2) + n + 2
    return f(n - 1) + n - 2


def check(n):
    while n > 0:
        d = n % 10
        if d % 2:
            return False
        n //= 10
    return True


def check2(n):
    for d in str(n):
        if d in '13579':
            return False
    return True


k = 0
for i in range(1, 1000 + 1):
    # if check(f(i)):
    if all(map(lambda x: x in '02468', str(f(i)))):
        k += 1
print(k)
