products = input()
final_product = {}
while not products == 'statistics':
    product, value = products.split(': ')
    value = int(value)
    if product in final_product:
        final_product[product] += value
    else:
        final_product[product] = value
    products = input()


print('Products in stock:')
for key, value in final_product.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(final_product)}')
print(f'Total Quantity: {sum(final_product.values())}')