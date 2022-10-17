rows, cols = [int(x) for x in input().split()]

matrix = []

for el in range(rows):
    matrix.append([int(x) for x in input().split()])

max_num = -999999
total = 0
first_position = None
second_position = None
third_position = None
for row in range(rows-2):
    for col in range(cols-2):
        first_roll_num = matrix[row][col]
        secont_roll_sum = matrix[row][col +1]
        third_roll_sum = matrix[row][col+2]
        bottom_first_sum = matrix[row+1][col]
        bottom_second_sum = matrix[row+1][col+1]
        bottom_third_sum = matrix[row+1][col+2]
        last_first_sum = matrix[row+2][col]
        last_second_sum = matrix[row+2][col+1]
        last_third_sum = matrix[row+2][col+2]
        total += first_roll_num + secont_roll_sum + third_roll_sum + bottom_first_sum + bottom_second_sum + bottom_third_sum + last_first_sum + last_second_sum + last_third_sum
        if total > max_num:
            max_num = total
            first_position = first_roll_num, secont_roll_sum, third_roll_sum
            second_position = bottom_first_sum, bottom_second_sum, bottom_third_sum
            third_position = last_first_sum, last_second_sum, last_third_sum

        total = 0

print(f'Sum = {max_num}')
print(*first_position)
print(*second_position)
print(*third_position)

