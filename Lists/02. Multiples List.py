factor = int(input())
count = int(input())
new_numbers = []
for i in range(1, count + 1):
    new_numbers.append(i * factor)
print(new_numbers)