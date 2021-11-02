n = int(input())
unique = set()
for el in range(n):
    elements = input().split()
    for x in elements:
        unique.add(x)

[print(result) for result in unique]