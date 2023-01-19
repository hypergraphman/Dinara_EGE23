def add_fib(n):
    fib = (1, 2, 3, 5, 8, 13, 21)
    i = 0
    while fib[i] < n:
        i += 1
    return n + fib[i]


opp = (lambda x: x + 1, lambda x: x + 4, add_fib)


def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return sum(map(lambda x: f(x(start), end), opp))


print(f(1, 17))