command = input()
employees = {}
while not command == 'End':
    name, id = command.split(' -> ')
    if not id in employees and not name in employees:
        employees[name] = [id]
    elif name in employees and not id in employees[name]:
        employees[name].append(id)
    command = input()

ascending = dict(sorted(employees.items(), key=lambda x: x[0]))
for key, value in ascending.items():
    print(f'{key}')
    for v in value:
        print(f'-- {"".join(v)}')
