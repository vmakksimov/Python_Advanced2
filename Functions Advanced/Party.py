class Party:
    def __init__(self):
        self.people = []
        command = input()
        while not command == 'End':
            self.people.append(command)

            command = input()


names = Party()
print(f'Going: {", ".join(names.people)}')
print(f'Total: {len(names.people)}')