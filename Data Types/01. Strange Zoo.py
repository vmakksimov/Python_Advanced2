name = [1, 12.5, True, 'Hello', 2]
only_int = []
for el in name:
    if isinstance(el, int) and not isinstance(el, bool):
        only_int.append(el)
print(only_int)