def is_valid(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False

def direction(mat, r, c, counter, presents):
    r_up, c_up = r - 1, c
    r_down, c_down = r + 1, c
    r_left, c_left = r, c - 1
    r_right, c_right = r, c + 1
    if mat[r_up][c_up] == 'V':
        counter -= 1
        presents -= 1
        mat[r_up][c_up] = '-'
        if presents == 0:
            return mat, counter, presents
    elif mat[r_up][c_up] == 'X':
        mat[r_up][c_up] = '-'
        presents -= 1
        if presents == 0:
            return mat, counter, presents
    if mat[r_down][c_down] == 'V':
        counter -= 1
        presents -= 1
        mat[r_down][c_down] = '-'
        if presents == 0:
            return mat, counter, presents
    elif mat[r_down][c_down] == 'X':
        mat[r_down][c_down] = '-'
        presents -= 1
        if presents == 0:
            return mat, counter, presents
    if mat[r_left][c_left] == 'V':
        counter -= 1
        presents -= 1
        mat[r_left][c_left] = '-'
        if presents == 0:
            return mat, counter, presents
    elif mat[r_left][c_left] == 'X':
        mat[r_left][c_left] = '-'
        presents -= 1
        if presents == 0:
            return mat, counter, presents
    if mat[r_right][c_right] == 'V':
        counter -= 1
        presents -= 1
        mat[r_right][c_right] = '-'
        if presents == 0:
            return mat, counter, presents
    elif mat[r_right][c_right] == 'X':
        mat[r_right][c_right] = '-'
        presents -= 1
        if presents == 0:
            return mat, counter, presents

    return mat, counter, presents


def next_moves(act, r, c, step):
    if act == 'up':
        return r - step, c
    elif act == 'down':
        return r + step, c
    elif act == 'left':
        return r, c - step
    elif act == 'right':
        return r, c + step


presents = int(input())
current_present = presents
size = int(input())
matrix = []
for _ in range(size):
    matrix.append(input().split())


santa_row, santa_col = 0, 0
nice_kids_counter = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'S':
            santa_row, santa_col = row, col
        elif matrix[row][col] == 'V':
            nice_kids_counter += 1


total_presents = nice_kids_counter

while True:
    command = input()
    if command == 'Christmas morning':
        break
    if current_present == 0:
        break
    else:
        next_row, next_col = santa_row, santa_col
        next_row, next_col = next_moves(command, next_row, next_col, 1)
        if is_valid(next_row, next_col):
            if matrix[next_row][next_col] == 'V':
                matrix[santa_row][santa_col] = '-'
                santa_row, santa_col = next_row, next_col
                matrix[santa_row][next_col] = 'S'
                current_present -= 1
                nice_kids_counter -= 1
                if current_present <= 0:
                    break

            elif matrix[next_row][next_col] == 'X':
                matrix[santa_row][santa_col] = '-'
                santa_row, santa_col = next_row, next_col
                matrix[santa_row][next_col] = 'S'

            elif matrix[next_row][next_col] == 'C':
                matrix[santa_row][santa_col] = '-'
                santa_row, santa_col = next_row, next_col
                matrix[santa_row][next_col] = 'S'
                matrix, nice_kids_counter, current_present = direction(matrix, next_row, next_col, nice_kids_counter, current_present)
                if current_present == 0:
                    break
            else:
                matrix[santa_row][santa_col] = '-'
                santa_row, santa_col = next_row, next_col
                matrix[santa_row][next_col] = 'S'
        else:
            break


if 0 == current_present and nice_kids_counter > 0:
    print('Santa ran out of presents!')

for el in matrix:
    print(f'{" ".join(el)}')

if nice_kids_counter == 0:
    print(f'Good job, Santa! {total_presents} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids_counter} nice kid/s.')

