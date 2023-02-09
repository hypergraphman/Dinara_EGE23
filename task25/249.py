from re import fullmatch



for n in range(161, 10 ** 8 + 1, 161):
    if fullmatch(r'12\d*4\d65', str(n)):
        print(n, n // 161)


        
