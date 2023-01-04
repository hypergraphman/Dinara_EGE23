s = open('k7-0.txt').readline()
max_len = 0
cur_len = 0
for i in range(len(s)):
    if s[i] in 'ABC':
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0

print(max_len)