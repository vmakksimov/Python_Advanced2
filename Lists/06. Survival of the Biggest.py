
numbers = input().split(' ')
number = []


for num in numbers:
    num = int(num)
    number.append(num)


remover = int(input())
for i in range(remover):
    number.remove(min(number))
print(*number, sep=', ')