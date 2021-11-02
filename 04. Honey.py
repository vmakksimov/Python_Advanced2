from collections import deque
working_bees = deque([int(x) for x in input().split()])
nectar = [int(i) for i in input().split()]
symbols = deque(input().split())
matrix = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
result = 0
while working_bees and nectar:
    working_bee = working_bees[0]
    current_nectar = nectar[-1]
    current_arithmetics = symbols[0]

    if working_bee <= current_nectar:
        working_bee = working_bees.popleft()
        current_nectar = nectar.pop()
        current_arithmetics = symbols.popleft()
        if current_nectar > 0:
            result += abs(matrix[current_arithmetics](working_bee, current_nectar))
    elif current_nectar < working_bee:
        nectar.pop()
        continue


print(f'Total honey made: {result}')
if working_bees or nectar:
    if working_bees:
        working_bees = [str(i) for i in working_bees]
        print(f'Bees left: {", ".join(working_bees)}')
    else:
        nectar = [str(i) for i in nectar]
        print(f'Nectar left: {", ".join(nectar)}')





