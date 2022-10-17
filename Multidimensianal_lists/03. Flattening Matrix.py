n = int(input())

matrix = []
new_matrix = []
for el in range(n):
    matrix.append([int(x) for x in input().split(', ')])
for i in range(n):
    for j in matrix[i]:
        new_matrix.append(j)
print(new_matrix)