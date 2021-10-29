number_of_names = int(input())
all_names = set()
for names in range(number_of_names):
    name = input()
    all_names.add(name)

[print(x) for x in all_names]

