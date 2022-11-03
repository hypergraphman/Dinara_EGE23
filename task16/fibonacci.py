def fib(x):
    if 1 <= x <= 2:
        return 1
    return fib(x - 1) + fib(x - 2)


n = int(input())
# print(fib(n))

prev, cur = 1, 1
for i in range(3, n + 1):
    prev, cur = cur, prev + cur
print(cur)