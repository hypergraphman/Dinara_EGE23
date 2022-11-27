from functools import reduce

n = 1234
print(reduce(lambda x, y: x * y, map(int, str(n))))
