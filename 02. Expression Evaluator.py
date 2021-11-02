from collections import deque

matrix = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b,
    '/' : lambda a, b: a // b,
}
expression = deque(input().split())
numbers = deque()
operators = []
result = 0

for el in expression:
    if el in matrix:
        result = numbers.popleft()
        while numbers:
            number = numbers.popleft()
            result = matrix[el](result, number)
        numbers.append(result)

    else:
        numbers.append(int(el))


print(result)