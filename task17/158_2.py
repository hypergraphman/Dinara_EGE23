data = tuple(map(int, open('17-1.txt').readlines()))

cur_len = 1
mx_len = 1
k = 1
for i in range(1, len(data)):
    if data[i - 1] > data[i]:
        cur_len += 1
        if cur_len > mx_len:
            k = 1
            mx_len = cur_len
        elif cur_len == mx_len:
            k += 1
    else:
        cur_len = 1

print(mx_len, k)
