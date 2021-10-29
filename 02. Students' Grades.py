number = int(input())

average_grades = {}

for x in range(number):
    command = input().split()
    name = command[0]
    grade = float(command[1])
    if name not in average_grades:
        average_grades[name] = [grade]
    else:
        average_grades[name].append(grade)

for key, value in average_grades.items():
    print(f'{key} -> {" ".join(map(lambda grade: f"{grade:.2f}", value))} (avg: {sum(value)/len(value):.2f})')