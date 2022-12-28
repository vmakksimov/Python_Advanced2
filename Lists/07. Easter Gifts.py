gifts = input().split()
command = input().split(', ')

while command != 'No Money':
    for com in command:
        command, gift, index = com.split()
        if command == 'OutOfStock':
            for index, item in enumerate(gifts):
                if item == 'Eggs':
                    gifts[index] = 'None'
        elif command == 'Required':
                index = gift[index]
    command = input()