data = tuple(map(int, open('17-2.txt').readlines()))
c = 0
mx_index = 0
mn_data = min(data)
for i, el in enumerate(data, start=1):
    if el == mn_data:
        c += 1
        mx_index = max(mx_index, i)
print(c, mx_index)