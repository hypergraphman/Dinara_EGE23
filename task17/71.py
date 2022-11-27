k = 0
mn = None
for i in range(125888, 1031 - 1, -1):
    if int(i**0.5)**2 == i and i % 10 != 5:
        k += 1
        if i % 100 == 36:
            mn = i
print(k, mn)