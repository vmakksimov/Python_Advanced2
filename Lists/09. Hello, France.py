type = input().split('|')
budget = float(input())
items = []
new_price_items = []
profit = []
diff = 0
for buy in type:
    type_clothes, value = buy.split('->')
    value = float(value)
    if type_clothes == 'Clothes' and value > 50:
        continue
    elif type_clothes == 'Shoes' and value > 35:
        continue
    elif type_clothes == 'Accessories' and value > 20.50:
        continue

    if budget >= value:
        items.append(value)
        budget -= value
        profit.append(value * 0.40)
        new_price_items.append((value * 0.40) + value)
    else:
        continue
for new_items in new_price_items:
    print(f'{new_items:.2f} ', end='')
print()
print(f'Profit: {sum(profit):.2f}')

if sum(new_price_items) + budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
