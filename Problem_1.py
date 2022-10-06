from collections import deque

def prepaid(palm, willow, croseete):
    if palm >= 3 and willow >= 3 and croseete >= 3:
        return True
    return False

def check(f_effects, e_power,results, palm, willow, crossete):
    if results % 3 == 0 and not results % 5 == 0:
        palm += 1

    elif results % 5 == 0 and not results % 3 == 0:
        willow += 1

    elif results % 5 == 0 and results % 3 == 0:
        crossete += 1
    else:
        f_effects[0] -= 1
        moved = f_effects.popleft()
        f_effects.append(moved)
        return f_effects, e_power, palm, willow, crossete

    f_effects.popleft()
    e_power.pop()
    return f_effects, e_power, palm, willow, crossete


firework_effects = deque([int(el) for el in input().split(', ')])
explosive_power = [int(el) for el in input().split(', ')]


palm_firework = 0
willow_firework = 0
crossete_firework = 0
is_valid = False
while True:
    if len(firework_effects) == 0:
        break

    if len(explosive_power) == 0:
        break

    current_firework = firework_effects[0]
    current_explosive = explosive_power[-1]

    if 0 >= current_firework:
        firework_effects.popleft()
        continue

    if 0 >= current_explosive:
        explosive_power.pop()
        continue

    result = current_explosive + current_firework
    firework_effects, explosive_power, palm_firework, willow_firework, crossete_firework = check(firework_effects, explosive_power, result, palm_firework, willow_firework, crossete_firework)
    is_valid = prepaid(palm_firework, willow_firework, crossete_firework)
    if is_valid:
        break

if is_valid:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if len(firework_effects) > 0:
    print(f'Firework Effects left: {", ".join(map(str, firework_effects))}')
if len(explosive_power) > 0:
    print(f'Explosive Power left: {", ".join(map(str, explosive_power))}')

print(f'Palm Fireworks: {palm_firework}')
print(f'Willow Fireworks: {willow_firework}')
print(f'Crossette Fireworks: {crossete_firework}')