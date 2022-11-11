data = [w.lower() for w in input().split()]

products = {}
final_product = {}
for name in data:
    products[name] = data.count(name)

for key, value in products.items():
    if value % 2 != 0:
        final_product[key] = value
for key in final_product:
    print(f'{key}', end=' ')