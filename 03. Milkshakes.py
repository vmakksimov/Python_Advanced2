
from collections import deque
chocolates = [int(el) for el in input().split(', ')]
milk_shakes = deque([int(el) for el in input().split(', ')])
counter = 0
is_done = False
while len(chocolates) > 0 and len(milk_shakes) > 0:
    last_chocolate_portion = chocolates[-1]
    first_milk_portion = milk_shakes[0]

    if last_chocolate_portion <= 0 or first_milk_portion <= 0:
        if last_chocolate_portion <= 0:
            chocolates.pop()
        if first_milk_portion <= 0:
            milk_shakes.popleft()
        continue

    if last_chocolate_portion == first_milk_portion:
        chocolates.pop()
        milk_shakes.popleft()
        counter += 1
    else:
        removed = milk_shakes.popleft()
        milk_shakes.append(removed)
        chocolates[-1] -= 5

    if counter == 5:
        is_done = True
        break

if is_done:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print('Chocolate: empty')

if milk_shakes:
    print(f"Milk: {', '.join(map(str, milk_shakes))}")
else:
    print('Milk: empty')
