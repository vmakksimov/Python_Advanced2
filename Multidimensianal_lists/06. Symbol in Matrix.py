num = int(input())

matrix = []

for i in range(num):
    matrix.append(list(input()))

special_symbol = input()
is_found = False
position = None
for cols in range(num):
    for rows in range(num):
        if matrix[cols][rows] == special_symbol:
            is_found = True
            position = (cols, rows)
            break
    if is_found:
        break

if not is_found:
    print(f'{special_symbol} does not occur in the matrix')
else:
    print(position)


