n = int(input())

even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []
for i in range(n):
    numbers = int(input())
    if numbers % 2 == 0:
        even_numbers.append(numbers)
    if not numbers % 2 == 0:
        odd_numbers.append(numbers)
    if numbers < 0:
        negative_numbers.append(numbers)
    if numbers >= 0:
        positive_numbers.append(numbers)
command = input()
if command == 'even':
    print(even_numbers)
elif command == 'odd':
    print(odd_numbers)
elif command == 'negative':
    print(negative_numbers)
elif command == 'positive':
    print(positive_numbers)