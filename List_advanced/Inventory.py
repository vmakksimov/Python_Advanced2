items = input().split(', ')
inventory = items.copy()
command = input()
while not command == 'Craft!':
    comm, item = command.split(' - ')
    if comm == 'Collect':
        if item not in inventory:
            inventory.append(item)
    elif comm == 'Drop':
        if item in inventory:
            inventory.remove(item)
    elif comm == 'Combine Items':
        old, new = item.split(':')
        if old in inventory:
            index_old_item = inventory.index(old)
            inventory.insert(index_old_item + 1, new)
    elif comm == 'Renew':
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input()
print(*inventory, sep=', ')