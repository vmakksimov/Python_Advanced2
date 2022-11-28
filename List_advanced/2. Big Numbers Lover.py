numbers = input().split()
numbers_as_string = ''.join(sorted(numbers, reverse=True))
print(numbers_as_string)
