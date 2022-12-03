shell_to_fill = int(input())
electron = []

for index in range(0, shell_to_fill +1):
    filled = 2 * (index + 1) ** 2
    if filled > shell_to_fill:
        electron.append(shell_to_fill)
        shell_to_fill -= shell_to_fill
    else:
        electron.append(filled)
        shell_to_fill -= filled
    if shell_to_fill == 0:
        break
print(electron)