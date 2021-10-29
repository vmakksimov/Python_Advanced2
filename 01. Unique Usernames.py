n = int(input())

names = set()

for el in range(n):
    names.add(input())

[print(k) for k in names]