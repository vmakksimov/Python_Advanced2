n = int(input())

matrix = []

for el in range(n):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = 0
primary = []
secondary_diagonal = 0
secondary = []
col = n -1
for row in range(n):
    primary_diagonal += matrix[row][row]
    primary.append(matrix[row][row])
    secondary_diagonal += matrix[row][col]
    secondary.append(matrix[row][col])
    col -= 1

print(f'Primary diagonal: {", ".join(map(str, primary))}. Sum: {primary_diagonal}')
print(f'Secondary diagonal: {", ".join(map(str, secondary))}. Sum: {secondary_diagonal}')

