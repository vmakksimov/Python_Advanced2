text = input()
final = {}
for occ in text:
    letter = occ
    result = text.count(letter)
    if letter not in final:
        final[letter] = result

sorted_items = dict(sorted(final.items(), key=lambda x: x[0]))
for key, value in sorted_items.items():
    print(f'{key}: {value} time/s')
