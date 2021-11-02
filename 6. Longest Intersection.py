n = int(input())

all_together = {}
max_int = -999999
for el in range(n):
    first_number = set([])
    second_number = set([])
    first_start, second_start= input().split('-')
    new_one = str(first_start)
    k = first_start.split(',')
    l = second_start.split(',')
    first_start_number_one = int(k[0])
    first_start_number_two = int(k[1])
    second_start_number_one = int(l[0])
    second_start_number_two = int(l[1])
    for f in range(first_start_number_one, first_start_number_two + 1):
        first_number.add(f)
    for s in range(second_start_number_one, second_start_number_two + 1):
        second_number.add(s)

    longest_interaction = list(first_number.intersection(second_number))
    if len(longest_interaction) > max_int:
        max_int = len(longest_interaction)
        all_together['name'] = longest_interaction

for key, value in all_together.items():
    print(f'Longest intersection is {value} with length {max_int}')

