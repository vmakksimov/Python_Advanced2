numbers = tuple([float(el) for el in input().split()])
results = []
for el in numbers:
    if el not in results:
        print(f'{el:.1f} - {numbers.count(el)} times')
        results.append(el)




