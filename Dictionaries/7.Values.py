characters = input().split(', ')
products = {}
for el in range(0, len(characters)):
    key = characters[el]
    value = ord(characters[el])
    products[key] = value

print(products)