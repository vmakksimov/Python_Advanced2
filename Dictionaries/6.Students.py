students = []

final = {}
while True:
    data = input()
    token = data.split(':')
    if len(token) < 2:
        for index in range(len(token)):
            final= token[0]
            break
        break
    students.append([token[0], token[1], token[2]])

for el in students:
    if el[2][0] in final[0]:
        print(f'{el[0]} - {el[1]}')







