
def check_sell(items, box):
    for el in items:
        if el.isnumeric():
            el = int(el)
            for index in range(el):
                box.pop(0)
        else:
            if el in box:
                while el in box:
                    box.remove(el)
    return box


def check_delivery(items, box):
    for el in items:
        box.append(el)
    return box


def stock_availability(*args):
    box_list = list(map(str, args[0]))
    action = args[1]
    new_items = list(map(str, args[2:]))

    if action == 'delivery':
        box_list = check_delivery(new_items, box_list)

    elif action == 'sell':
        if len(new_items) > 0:
            box_list = check_sell(new_items, box_list)
        else:
            box_list.pop(0)

    return box_list



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


