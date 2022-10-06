def check(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


num = int(input())

matrix = []
snake_row, snake_col = 0, 0
for _ in range(num):
    matrix.append(list(input()))

burrows_positions = []
for row in range(num):
    for col in range(num):
        if matrix[row][col] == 'S':
            snake_row, snake_col = row, col
        elif matrix[row][col] == 'B':
            burrows_positions.append([row, col])

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c),
}
food_quantity = 0
game_over = False
out_of_teritory = False
while True:
    command = input()
    for key, value in directions.items():
        if key == command:
            matrix[snake_row][snake_col] = '.'
            next_row, next_col = value(snake_row, snake_col)

            if check(next_row, next_col, num):
                if matrix[next_row][next_col] == '*':
                    food_quantity += 1
                    matrix[next_row][next_col] = 'S'
                    snake_row, snake_col = next_row, next_col
                    if food_quantity >= 10:
                        game_over = True
                        break

                elif matrix[next_row][next_col] == 'B':
                    matrix[next_row][next_col] = '.'
                    if next_row == burrows_positions[0][0] and next_col == burrows_positions[0][1]:

                        next_row, next_col = burrows_positions[1][0], burrows_positions[1][1]
                        snake_row, snake_col = next_row, next_col
                        matrix[snake_row][snake_col] = 'S'

                    else:
                        next_row, next_col = burrows_positions[1][0], burrows_positions[1][1]
                        snake_row, snake_col = next_row, next_col
                        matrix[next_row][next_col] = 'S'

                else:
                    matrix[next_row][next_col] = 'S'
                    snake_row, snake_col = next_row, next_col

            else:
                out_of_teritory = True
                break

    if game_over:
        break

    if out_of_teritory:
        break


if out_of_teritory:
    print('Game over!')

if game_over:
    print('You won! You fed the snake.')

print(f'Food eaten: {food_quantity}')

for el in matrix:
    print(f'{"".join(el)}')