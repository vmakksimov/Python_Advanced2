list_of_numbers = [int(el) for el in input().split(', ')]
max_number = max(list_of_numbers)
group = 10

while len(list_of_numbers) > 0:
    nums_group = []
    for num in list_of_numbers:
        if num in range(group - 10, group + 1):
            nums_group.append(num)
    for number in nums_group:
        if number in list_of_numbers:
            list_of_numbers.remove(number)
    print(f'Group of {group}\'s: {nums_group}')
    group += 10


