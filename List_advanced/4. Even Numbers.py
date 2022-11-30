

numbers = input().split(', ')
# result = [index for index, digit in enumerate(numbers) if int(digit) % 2 == 0]

result = list(map(int, numbers))
print(result)