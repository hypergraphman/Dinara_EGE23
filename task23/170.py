from math import gcd

funcs = [lambda x, y: (x + 3, y),
         lambda x, y: (x * 4, y),
         lambda x, y: (x, y + 5),
         lambda x, y: (x, y * 2)]
st = [(2, 3)]
for _ in range(5):
    nxt = []
    for pair in st:
        for func in funcs:
            nxt.append(func(*pair))
    st = nxt
ans = set()
for pair in st:
    if gcd(*pair) == 1:
        ans.add(pair)
print(ans)
print(len(ans))
ans_2 = set()
for p1, p2 in ans:
    if (p2, p1) not in ans_2 and (p1, p2) not in ans_2:
        ans_2.add((p1, p2))
print(len(ans_2))