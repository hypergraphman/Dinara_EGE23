a = 49 ** 7 + 7 ** 21 - 7
b = ''
while a > 0:
    b = str(a % 7) + b
    a //= 7
print(b)