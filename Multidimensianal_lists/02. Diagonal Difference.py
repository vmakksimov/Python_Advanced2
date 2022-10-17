n = int(input())

left_matrix = []
left_result = 0
right_result = 0
for i in range(n):
    left_matrix.append([int(x) for x in input().split()])
col = n
for row in range(n):
    left_result += left_matrix[row][row]
    right_result += left_matrix[row][col -1]
    col -= 1

print(abs(left_result - right_result))





