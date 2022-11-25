food = input().split()
products = {}
for el in range(0, len(food), 2):
    key = food[el]
    value = int(food[el +1])
    products[key] = value

print(products)
