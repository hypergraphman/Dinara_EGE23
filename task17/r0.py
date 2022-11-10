c = 0
mx = 0
for i in range(1035, 7737 + 1, 5):
    if i % 11 and i % 17 and i % 19 and i % 23:
        c += 1
        mx = max(mx, i)
print(c, mx)
