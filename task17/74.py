count = 0
mn = 10**10
ans = None
for n in range(5903, 174203 + 1):
    t = str(n)
    if len(t) == len(set(t)) and [d > '4' for d in t].count(True) == 3:
        count += 1
        if mn > abs(30000 - n):
            mn = abs(30000 - n)
            ans = n
print(count, ans)