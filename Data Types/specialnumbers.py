number = int(input())

for num in range(1, number + 1):
    total = 0
    num_as_string = str(num)
    for i in num_as_string:

        total += int(i)
    if total == 5 or total == 7 or total == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
