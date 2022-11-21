number_of_registration = int(input())
registered_users = {}
for person in range(0, number_of_registration):
    persons = input().split()
    command = persons[0]
    if command == 'register':
        username = persons[1]
        license_plate = persons[2]
        if username not in registered_users and license_plate not in registered_users:
            registered_users[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
        elif username in registered_users and license_plate not in registered_users:
            print(f'ERROR: already registered with plate number {license_plate}')
    elif command == 'unregister':
        username = persons[1]
        if username in registered_users:
            print(f'{username} unregistered successfully')
            registered_users.pop(username)
        else:
            print(f'ERROR: user {username} not found')
for key, value in registered_users.items():
    print(f'{key} => {value}')

