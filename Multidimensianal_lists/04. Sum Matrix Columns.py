row, col = [int(x) for x in input().split(', ')]

matrix = []
for i in range(row):
    matrix.append([int(x) for x in input().split()])

for cols in range(col):
    result = 0
    for rows in range(row):
        result += (matrix[rows][cols])
    print(result)
