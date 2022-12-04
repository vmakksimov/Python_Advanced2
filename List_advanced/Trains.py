wagons = int(input())


wagon = [0 for _ in range(wagons)]


command = input()
while command != 'End':
    data = command.split()

    if data[0] == 'add':
        number_of_people = int(data[1])
        wagon[-1] += number_of_people
    elif data[0] == 'insert':
        index = int(data[1])
        number_of_people = int(data[2])
        wagon[index] += number_of_people
    elif data[0] == 'leave':
        index = int(data[1])
        number_of_people = int(data[2])
        wagon[index] -= number_of_people

    command = input()

print(wagon)