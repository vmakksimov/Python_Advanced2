num = int(input())

matrix = []
result = 0
for row in range(num):
    matrix.append([int(x) for x in input().split()])
    result += matrix[row][row]
print(result)
