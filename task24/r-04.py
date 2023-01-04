s = open('k7-0.txt').readline()
count = 0
for i in range(2, len(s)):
    if s[i - 2] in 'BCD' and s[i - 1] in 'BDE' and s[i] in 'BCE' and s[i - 2] != s[i - 1] and s[i - 1] != s[i]:
        count += 1
print(count)






