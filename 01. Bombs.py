from collections import deque


def calculate(bomb_lo, bombs_fill, bombs_eff, bombs_cas):
    if not bomb_lo == 40 and not bomb_lo == 60 and not bomb_lo == 120:
        bombs_cas[-1] -= 5
    else:
        if bomb_lo == 40:
            bombs_fill['Datura Bombs'] += 1

        elif bomb_lo == 60:
            bombs_fill['Cherry Bombs'] += 1

        elif bomb_lo == 120:
            bombs_fill['Smoke Decoy Bombs'] += 1

        bombs_eff.popleft()
        bombs_cas.pop()

    return bombs_fill, bombs_eff, bombs_cas


bombs_effect = deque([int(el) for el in input().split(', ')])
bombs_casing = [int(el) for el in input().split(', ')]
bombs_filled = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
is_bomber = False

while True:
    if len(bombs_effect) == 0:
        break

    if len(bombs_casing) == 0:
        break

    current_bomb = bombs_effect[0]
    current_casting = bombs_casing[-1]
    bomb_loading = current_bomb + current_casting

    bombs_filled, bombs_effect, bombs_casing = calculate(bomb_loading, bombs_filled, bombs_effect, bombs_casing)

    if bombs_filled['Datura Bombs'] >= 3 and bombs_filled['Cherry Bombs'] >= 3 and bombs_filled['Smoke Decoy Bombs'] >=3:
        is_bomber = True
        break

if is_bomber:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')

if len(bombs_effect) <= 0:
    print('Bomb Effects: empty')
else:
    print(f'Bomb Effects: {", ".join(map(str, bombs_effect))}')

if len(bombs_casing) <= 0:
    print('Bomb Casings: empty')
else:
    print(f'Bomb Casings: {", ".join(map(str, bombs_casing))}')

alpha = dict(sorted(bombs_filled.items(), key=lambda x: x[0]))
for key, value in alpha.items():
    print(f'{key}: {value}')


