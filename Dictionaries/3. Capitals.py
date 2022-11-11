countries = input().split(', ')
capitals = input().split(', ')
difference = {}
zip_object = zip(countries, capitals)
for countries, capitals in zip_object:
    difference[countries] = capitals
for key, value in difference.items():
    print(f'{key} -> {value}')
