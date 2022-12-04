
number = input().split()
new_values = []
for n in number:
    n = int(n)
    if n < 0:
        new_values.append(n * -1)
    elif n > 0:
        new_values.append(n * -1)
    else:
        new_values.append(0)
print(new_values)
