rows, cols = [int(x) for x in input().split()]

matrix = []

for j in range(rows):
    matrix.append(input().split())

counter = 0
for row in range(rows-1):
    for col in range(cols-1):
        current_chr = matrix[row][col]
        next_current_chr = matrix[row][col+1]
        bottom_chr = matrix[row+1][col]
        bottom_right_chr = matrix[row+1][col +1]
        if current_chr == next_current_chr and bottom_chr == bottom_right_chr and current_chr == bottom_chr and next_current_chr == bottom_right_chr:
            counter += 1
print(counter)
