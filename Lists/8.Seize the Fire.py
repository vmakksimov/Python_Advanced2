# readin and splitting the data
high_fire = range(81, 126)
medium_fire = range(51, 81)
low_fire = range(1, 51)
type_of_fire = input().split('#')
water_amount = int(input())
effort = 0
fire_off = []
for fire in type_of_fire:
    fire_value, value = fire.split(' = ')
    value = int(value)
    if fire_value == 'High' and value not in high_fire:
        continue
    elif fire_value == 'Low' and value not in low_fire:
        continue
    elif fire_value == 'Medium' and value not in medium_fire:
        continue
    if water_amount >= value:
        water_amount -= value
        fire_off.append(value)
        effort += value * 0.25
print('Cells:')
for fire in fire_off:
    print(f'- {fire}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(fire_off)}')