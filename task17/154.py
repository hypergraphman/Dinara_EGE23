from math import inf

data = tuple(map(int, open('17-1.txt').readlines()))
print(data)
local_max = []
for i in range(1, len(data) - 1):
    if data[i - 1] < data[i] > data[i + 1]:
        local_max.append(i)
mn = inf
for i in range(1, len(local_max)):
    mn = min(local_max[i] - local_max[i - 1], mn)
print(len(local_max), mn)
