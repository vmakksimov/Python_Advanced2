queries = int(input())
stack = []
for x in range(queries):
    command = input().split()
    act = int(command[0])
    if act == 1:
        stack.append(int(command[1]))
    elif act == 2:
        if len(stack) > 0:
            stack.pop()
    elif act == 3:
        if len(stack) > 0:
            print(max(stack))
    elif act == 4:
        if len(stack) > 0:
            print(min(stack))
result = []
while stack:
    result.append(stack.pop())
print(*result, sep=', ')
