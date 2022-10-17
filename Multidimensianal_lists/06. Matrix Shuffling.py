rows, cols = [int(x) for x in input().split()]

matrix = []

for el in range(rows):
    matrix.append([x for x in input().split()])

command = input()

while not command == 'END':
    commands = command.split()
    act = commands[0]
    numbers_left = commands[1:]
    if act == 'swap' and len(numbers_left) == 4:
        numbers = [int(x) for x in numbers_left]
        crlf = numbers[0]
        ccf = numbers[1]
        crcs = numbers[2]
        cccs = numbers[3]
        if 0 <= crlf < rows and 0 <= ccf < cols and 0 <= crcs < rows and 0 <= cccs < cols:
            previous_value = matrix[crlf][ccf]
            value_to_change = matrix[crcs][cccs]
            matrix[crlf][ccf] = value_to_change
            matrix[crcs][cccs] = previous_value
            for k in matrix:
                print(" ".join(k))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')

    command = input()