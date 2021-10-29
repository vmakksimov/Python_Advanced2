from collections import deque

materials = [int(i) for i in input().split()]
magic_level = deque([int(i) for i in input().split()])

matrix = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400,
}
crafted_gifts = {}
while materials and magic_level:
    current_material = materials[-1]
    current_magic = magic_level[0]
    result = current_magic * current_material
    if result < 0:
        result = current_magic + current_material
        magic_level.popleft()
        materials.pop()
        materials.append(result)
    elif result > 0:
        if result in matrix.values():
            for key, value in matrix.items():
                if value == result:
                    if key in crafted_gifts:
                        crafted_gifts[key] += 1
                    else:
                        crafted_gifts[key] = 1
            materials.pop()
            magic_level.popleft()
        else:
            magic_level.popleft()
            materials[-1] += 15
    elif current_material == 0 or current_magic == 0:
        if current_material == 0:
            materials.pop()
        if current_magic == 0:
            magic_level.popleft()

if 'Doll' in crafted_gifts and 'Wooden train' in crafted_gifts or 'Teddy bear' in crafted_gifts and 'Bicycle' in crafted_gifts:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials or magic_level:
    if materials:
        materials = [str(i) for i in materials]
        print(f'Materials left: {", ".join(reversed(materials))}')
    if magic_level:
        magic_level = [str(i) for i in magic_level]
        print(f'Magic left: {", ".join(magic_level)}')

crafted_gifts = dict(sorted(crafted_gifts.items(), key=lambda x: x[0]))
for name, counts in crafted_gifts.items():
    print(f'{name}: {counts}')