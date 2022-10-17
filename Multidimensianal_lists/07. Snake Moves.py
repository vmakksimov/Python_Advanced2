rows, cols = [int(x) for x in input().split()]
command = input()
matrix = []
for el in range(rows):
    matrix.append([0 for x in range(cols)])

index_word = 0

for row in range(rows):
    for col in range(cols):
        matrix[row][col] = command[index_word]
        index_word += 1
        if index_word == len(command):
            index_word = 0

for rowe in range(rows):
    if rowe % 2 != 0:
        matrix[rowe].reverse()
    print(f'{"".join(matrix[rowe])}')

