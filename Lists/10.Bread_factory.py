event = input().split('|')
initial_energy = 100
coins = 100
energy = 100
bankrupt = False
for el in event:
    data = el.split('-')
    value = int(data[1])
    if data[0] == 'rest':
        spent_energy = 0
        if energy + value > initial_energy:
            diff = initial_energy - energy
            energy = initial_energy

        else:
            energy += value
            spent_energy = value
        print(f'You gained {spent_energy} energy.')
        print(f'Current energy: {energy}.')

    elif data[0] == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        coins -= value
        if not coins <= 0:
            print(f'You bought {data[0]}.')
        else:
            print(f'Closed! Cannot afford {data[0]}.')
            bankrupt = True
            break
if not bankrupt:
    print(f'Day completed!\n'
          f'Coins: {coins}\n'
          f'Energy: {energy}')
