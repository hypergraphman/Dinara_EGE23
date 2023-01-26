from functools import lru_cache


@lru_cache
def divs(n):
    s = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            s.add(d)
            s.add(n // d)
    return s


# print(divs(100), len(divs(100)))
a = list(map(int, open('17_adv.txt').readlines()))
# print(a)
mx = -10**10
divs_key = None
for el in a:
    if len(divs(el)) > mx:
        mx = len(divs(el))
        divs_key = divs(el)

ans = []
for i in range(1, len(a)):
    p1, p2 = a[i - 1], a[i]
    if len(divs(p1) & divs_key) >= 3 and len(divs(p2) & divs_key) >= 3:
        ans.append(len(divs(p1) & divs(p2)))
print(len(ans), max(ans))