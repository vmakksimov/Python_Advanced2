number_of_invitations = int(input())

invitations = set()

for x in range(number_of_invitations):
    guests = input()
    invitations.add(guests)

command = input()

while not command == 'END':
    if command in invitations:
        invitations.discard(command)
    command = input()
print(len(invitations))
for el in sorted(invitations):
        if el[0].isdigit():
            print(el)
for k in sorted(invitations):
    if k[0].isalpha():
        print(k)

