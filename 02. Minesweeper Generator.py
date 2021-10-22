def check(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

num = int(input())

test = num * [0]
matrix = []

for _ in range(num):
    matrix.append(list(test))

positions = int(input())

bombs_move = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c),
    'diagonall_down_right': lambda r, c: (r + 1, c + 1),
    'diagonall_down_left': lambda r,c: (r +1, c -1),
    'diagonall_up_lef': lambda r, c: (r -1, c -1),
    'diagonall_up_right': lambda r, c: (r -1, c+ 1),
}

def move(mat, com):
    com = com[1:-1]
    row, col = int(com.split(", ")[0]), int(com.split(", ")[1])
    mat[row][col] = '*'
    return mat


for position in range(positions):
    command = input()
    move(matrix, command)

for row in range(num):
    for col in range(num):

        current_row, current_col = row, col
        if matrix[current_row][current_col] == '*':
            continue

        for key, value in bombs_move.items():
            next_row, next_col = value(row, col)
            if check(next_row, next_col, num):
                if matrix[next_row][next_col] == '*':
                    matrix[current_row][current_col] += 1

for el in matrix:
    print(f'{" ".join(map(str,el))}')
