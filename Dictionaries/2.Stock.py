products = input().split()
searched_products = input().split()
searched = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index +1])
    searched[key] = value

for x in searched_products:
    if x in searched:
        print(f'We have {searched[x]} of {x} left')
    else:
        print(f'Sorry, we don\'t have {x}')
