for i in range(2, 11):
    res = ''
    n = 432
    while n > 0:
        res = str(n % i) + res
        n //= i
    print(res, i)