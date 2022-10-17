n = int(input())

matrix = []

for el in range(n):
    matrix.append(input().split())

max_result = 0
right_path = ''
path_follow = []
directions = {
    'right': lambda r, c: (r, c +1),
    'left': lambda r, c: (r, c -1),
    'down': lambda r, c: (r+1, c),
    'up': lambda r, c: (r-1, c),

}
def is_inside(r, c, n):
    return 0 <= r < n and 0 <= c < n
max_eggs = -999999999999
bunny_row, bunny_col = 0, 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'B':
            bunny_row, bunny_col = row, col

for direction, step in directions.items():
    eggs = 0
    current_row, current_col = bunny_row, bunny_col
    path = []

    while True:
        current_row, current_col = step(current_row, current_col)
        if not is_inside(current_row, current_col, n):
            break

        if matrix[current_row][current_col] == 'X':
            break

        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])
    if eggs > max_eggs:
        max_eggs = eggs
        right_path = direction
        path_follow = path

print(right_path)
for i in path_follow:
    print(i)
print(max_eggs)

