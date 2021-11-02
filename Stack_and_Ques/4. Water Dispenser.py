from collections import deque

quiantity_of_water = int(input())

name = input()
queue = deque()
while not name == 'Start':
    queue.append(name)
    name = input()

command = input()

while not command == 'End':
    if 'refill' in command:
        quiantity_of_water += int(command.split()[1])
    else:
        liters_needed = int(command)
        name = queue.popleft()
        if quiantity_of_water >= liters_needed:
            print(f'{name} got water')
            quiantity_of_water -= liters_needed
        else:
            print(f'{name} must wait')
    command = input()

print(f'{quiantity_of_water} liters left')