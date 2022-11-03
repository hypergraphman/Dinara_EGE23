def fac(x):
    if x <= 1:
        return 1
    return x * fac(x - 1)


n = int(input())

# print(fac(n))

res = 1
for x in range(1, n + 1):
    res *= x
print(res)