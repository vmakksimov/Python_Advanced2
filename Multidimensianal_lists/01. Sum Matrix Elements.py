rows, columns = [int(x) for x in input().split(', ')]
result = 0
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
    result += sum(matrix[row])

print(result)
print(matrix)


