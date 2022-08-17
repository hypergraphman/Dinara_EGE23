def greeter(x):
    print('Имя?')
    name = input()
    print('Привет', name)
    return len(name) * x


print(greeter(4))
#....

print(greeter(5))