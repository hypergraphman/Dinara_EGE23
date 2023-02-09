for i in range(2023, 10**10, 2023):
    s = str(i)
    if s[0] == '1' and s[2:6] == '2139' and s[-1] == '4':
        print(s, i // 2023)


from re import fullmatch
for i in range(2023, 10**10, 2023):
    if fullmatch(r'1\d2139\d*4', str(i)):
        print(i, i // 2023)