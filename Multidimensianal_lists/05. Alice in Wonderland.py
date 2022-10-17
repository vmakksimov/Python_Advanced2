n = int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split())

alice_row, alice_col = 0, 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'A':
            alice_row, alice_col = row, col

direction = {
    'right': lambda r, c: (r, c +1),
    'left': lambda r, c: (r, c -1),
    'down': lambda r, c: (r+1, c),
    'up': lambda r, c: (r-1, c),
}

matrix[alice_row][alice_col] = '*'
current_row, current_col = alice_row, alice_col
bags_of_tea_collected = 0
needed_bags = 10
is_failed = False
while True:
    command = input()
    for key, value in direction.items():
        if key == command:

            current_row, current_col = value(current_row, current_col)
            if not 0 <= int(current_row) < n:
                print("Alice didn't make it to the tea party.")
                is_failed = True
                break

            if not 0 <= int(current_col) < n:
                print("Alice didn't make it to the tea party.")
                is_failed = True
                break

            current_value = matrix[current_row][current_col]
            matrix[current_row][current_col] = '*'
            if current_value == 'R':
                print("Alice didn't make it to the tea party.")
                is_failed = True
                break

            if current_value != '.' and current_value != '*':
                current_number = int(current_value)
                bags_of_tea_collected += current_number
                if bags_of_tea_collected >= needed_bags:
                    print("She did it! She went to the party.")
                    is_failed = True
                    break

        if is_failed:
            break
    if is_failed:
        break

for v in matrix:
    print(*v)