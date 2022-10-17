n = int(input())

matrix = []

for el in range(n):
    matrix.append([int(x) for x in input().split()])

commands = input()

def check(coord, nums):
    for el in coord:
        if not 0 <= int(el) < n:
            print('Invalid coordinates')
            return False
    return True



while not commands == 'END':
    command = commands.split()
    act = command[0]
    coordinates = command[1:-1]
    value = int(command[-1])
    check_is_valid = check(coordinates, matrix)
    if check_is_valid:
        row_to_change = int(coordinates[0])
        col_to_change = int(coordinates[1])
        if act == 'Add':
            matrix[row_to_change][col_to_change] += value
        elif act == 'Subtract':
            matrix[row_to_change][col_to_change] -= value

    commands = input()

for final in matrix:
    print(*final)