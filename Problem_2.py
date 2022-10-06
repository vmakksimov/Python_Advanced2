import math

def check(nums, r, c):
    if 0 <= r < nums and 0 <= c < nums:
        return True
    return False


num = int(input())
matrix = []
for _ in range(num):
    matrix.append(input().split())
player_row, player_col = 0, 0
wall_row, wall_col = 0, 0
for row in range(num):
    for col in range(num):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col
        elif matrix[row][col] == 'X':
            wall_row, wall_col = row, col



direction = {
    'right': lambda r, c: (r, c +1),
    'left': lambda r, c: (r, c -1),
    'down': lambda r, c: (r+1, c),
    'up': lambda r, c: (r-1, c),
}

result = 0
current_row, current_col = player_row, player_col
position = []
game_over = False
while True:
    command = input()
    for key, value in direction.items():
        if command == key:
            next_row, next_col = value(current_row, current_col)
            is_valid = check(num, next_row, next_col)
            if is_valid:
                if matrix[next_row][next_col] == 'X':
                    result = math.floor(result - (result * 0.5))
                    game_over = True
                    break

                result += int(matrix[next_row][next_col])
                current_row, current_col = next_row, next_col
                position.append([current_row, current_col])

                if result >= 100:
                    game_over = True
                    break
            else:
                result = math.floor(result - (result * 0.5))
                game_over = True
                break

    if game_over:
        break

if result >= 100:
    print(f"You won! You've collected {math.floor(result)} coins.")
else:
    print(f"Game over! You've collected {math.floor(result)} coins.")
print('Your path:')
for path in position:
    print(path)