first, second, third = current_version = input().split('.')
first = int(first)
second = int(second)
third = int(third)
if third >= 9:
    third = 0
    if second >= 9:
        second = 0
        if first < 9:
            first += 1
    else:
        second += 1
else:
    third += 1
new_version = ''
new_version += str(first)
new_version += str(second)
new_version += str(third)
version = '.'.join(new_version)
print(version)
