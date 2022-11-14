
command = input()
final_product = {}
final_price = {}
product_price = {}
while not command == 'buy':
    data = command.split()
    product = data[0]
    currnet_price = float(data[1])
    quantity = int(data[2])
    if not product in final_product:
        final_product[product] = quantity
        final_price[product] = quantity * currnet_price
        product_price[product] = currnet_price
    else:
        for key, old_value in product_price.items():
            if key == product:
                final_product[product] += quantity
                if currnet_price != old_value:
                    final_price[product] = final_product[product] * currnet_price
                else:
                    final_price[product] = final_product[product] * currnet_price
    command = input()
for key, value in final_price.items():
    print(f'{key} -> {value:.2f}')