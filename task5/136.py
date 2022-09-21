def f(n):
    s1 = f'{n:b}'
    s2 = s1 + str(sum(map(int, s1)) % 2)
    s3 = s2 + str(sum(map(int, s2)) % 2)
    return int(s3, 2)


all_num = set(range(16, 32 + 1))
find_num = set()
for i in range(32):
    x = f(i)
    if x in all_num:
        find_num.add(x)

print(len(all_num - find_num))
