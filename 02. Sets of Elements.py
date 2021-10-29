numbers = input().split()
first = int(numbers[0])
second = int(numbers[1])
set_one = set()
for x in range(first):
    set_one.add(int(input()))
set_second = set()
for k in range(second):
    set_second.add(int(input()))
result = set_one.intersection(set_second)

for el in result:
    print(el)




