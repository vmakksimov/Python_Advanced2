name = input()
products = {}
for letter in name:
    if letter == ' ':
        continue
    if letter in products:
        products[letter] += 1
        continue
    products[letter] = letter.count(letter)


for key, value in products.items():
    print(f'{key} -> {value}')
