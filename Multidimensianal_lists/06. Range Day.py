def check(r, c):
    if 0 <= r < 5 and 0 <= c < 5:
        return True
    return False


def check_positions(shoot_row, shoot_col, directions):
    if directions == 'down':
        return shoot_row + 1, shoot_col

    elif directions == 'up':
        return shoot_row - 1, shoot_col

    elif directions == 'left':
        return shoot_row, shoot_col - 1

    elif directions == 'right':
        return shoot_row, shoot_col + 1


def check_commands(moved_row, moved_cow, m_index, directionn):
    if directionn == 'down':
        return moved_row + m_index, moved_cow
    elif directionn == 'up':
        return moved_row - m_index, moved_cow
    elif directionn == 'left':
        return moved_row, moved_cow - m_index
    elif directionn == 'right':
        return moved_row, m_index + moved_cow


matrix = []
target_counter = 0
for _ in range(5):
    matrix.append(input().split())

shooter_row, shooter_col = 0, 0

for row in range(5):
    for col in range(5):
        if matrix[row][col] == 'A':
            shooter_row, shooter_col = row, col
        elif matrix[row][col] == 'x':
            target_counter += 1

num_of_commands = int(input())
position = []
valid = None
all_target_number = target_counter
for el in range(num_of_commands):
    if target_counter == 0:
        break

    commands = input().split()
    act = commands[0]
    direction = commands[1]
    next_row, next_col = shooter_row, shooter_col
    if act == 'move':
        move_index = int(commands[2])
        next_row, next_col = check_commands(next_row, next_col, move_index, direction)
        check_is_valid = check(next_row, next_col)
        if check_is_valid:
            if matrix[next_row][next_col] == '.':
                matrix[next_row][next_col] = 'A'
                shooter_row, shooter_col = next_row, next_col

    elif act == 'shoot':

        while 0 <= next_row < 5 and 0 <= next_col < 5:
            next_row, next_col = check_positions(next_row, next_col, direction)
            valid = check(next_row, next_col)

            if valid:
                current_symbol = matrix[next_row][next_col]
                if current_symbol == 'x':
                    target_counter -= 1
                    matrix[next_row][next_col] = '.'
                    position.append([next_row, next_col])
                    break


if target_counter > 0:
    print(f"Training not completed! {target_counter} targets left.")

elif target_counter == 0:
    print(f"Training completed! All {all_target_number} targets hit.")

[print(x) for x in position]
