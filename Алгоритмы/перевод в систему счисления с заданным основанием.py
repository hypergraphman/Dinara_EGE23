def n_to_p(n, p):
    res = ''
    while n > 0:
        d = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n % p]
        res = d + res
        n //= p
    return res


# DK
print(n_to_p(345, 25))