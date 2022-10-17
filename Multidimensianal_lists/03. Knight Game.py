n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

removed_counter = 0

while True:
    max_hits = 0
    position = []
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                attacks = 0
                rows = [-2, -2, 2, 2, 1, 1, -1, -1]
                cols = [-1, 1, -1, 1, -2, 2, -2, 2]
                for index in range(len(rows)):
                    potential_row = row + rows[index]
                    potential_col = col + cols[index]
                    if 0 <= potential_row < n and 0 <= potential_col < n:
                        potential_position = matrix[row + rows[index]][col + cols[index]]
                        if potential_position == 'K':
                            attacks += 1
                    if max_hits < attacks:
                        max_hits = attacks
                        position = [row, col]

    if position:
        matrix[position[0]][position[1]] = '0'
        removed_counter += 1
    else:
        break

print(removed_counter)