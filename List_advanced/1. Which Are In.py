values = input().split(', ')

new_line = input().split(", ")

unique = [word for word in values for el in new_line if word in el]

print(sorted(set(unique), key=unique.index))
