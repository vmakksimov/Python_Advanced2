n = int(input())

matrix = []
new_matrix = []
for el in range(n):
    matrix.append([int(x) for x in input().split(', ')])
for row in range(n):
    new_matrix.append([int(k) for k in matrix[row] if k % 2 == 0])
print(new_matrix)