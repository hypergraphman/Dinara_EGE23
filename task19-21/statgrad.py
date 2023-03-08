a = []
for x1 in range(1, 80):
    for x2 in range(1, 80):
        if 2 * min(x1, x2) + max(x1, x2) >= 80:
            a.append((x1 + x2, x1, x2))
print(min(a))