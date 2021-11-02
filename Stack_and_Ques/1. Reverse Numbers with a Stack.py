numbers = input().split()
stack = []

while numbers:
    stack.append(numbers.pop())
result = [int(el) for el in stack]
print(*result)