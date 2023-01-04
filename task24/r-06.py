s = open('k8-0.txt').readline()
max_len = 1
cur_len = 1
simvols = []
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            simvols = [s[i]]
        elif cur_len == max_len:
            simvols.append(s[i])
    else:
        cur_len = 1
print(simvols, max_len)
