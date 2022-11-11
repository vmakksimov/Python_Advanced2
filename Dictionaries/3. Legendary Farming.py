
target = 250
products = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
while True:
    materials = input().lower().split()
    is_found = False
    for index in range(0, len(materials), 2):
        key = materials[index + 1]
        value = int(materials[index])
        if key in products:
            products[key] += value
        else:
            if key in junk:
                junk[key] += value
            else:
                junk[key] = value
        for key, value in products.items():
            if value >= target:
                diff = value - target
                products[key] = diff
                if key == 'fragments':
                    key = 'Valanyr'
                elif key == 'shards':
                    key = 'Shadowmourne'
                elif key == 'motes':
                    key = 'Dragonwrath'
                print(f'{key} obtained!')
                is_found = True
                break
        if is_found:
            break
    if is_found:
        break
sorted_by_name = dict(sorted(products.items(), key=lambda x: (-x[1], x[0])))
alpha = dict(sorted(junk.items(), key=lambda x: x[0]))
for key, value in sorted_by_name.items():
    print(f'{key}: {value}')
for key, value in alpha.items():
    print(f'{key}: {value}')



