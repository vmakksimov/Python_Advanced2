
products = {}
command = input()
while not command == 'stop':
    quantity = input()
    key = command
    value = int(quantity)
    if key in products:
        products[key] += value
    else:
        products[key] = value
    command = input()
for key, value in products.items():
    print(f'{key} -> {value}')
