rows, cols = [int(x) for x in input().split(', ')]

matrix = []
max_sum = -999999
for el in range(rows):
    matrix.append([int(i) for i in input().split(', ')])

current_sum = 0
position = None
for row in range(rows-1, 0, -1):
    for col in range(cols-1, 0, -1):
        current_sum = matrix[row][col] + matrix[row][col -1] + matrix[row -1][col] + matrix[row -1][col -1]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)
row, col = position
print(matrix[row -1][col -1], matrix[row -1][col])
print(matrix[row][col -1], matrix[row][col])
print(max_sum)
