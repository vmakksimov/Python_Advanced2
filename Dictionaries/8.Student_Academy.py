students_number = int(input())
students = {}
average_grade = {}

for student in range(1, students_number + 1):
    name = input()
    grade = float(input())
    if not name in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for name, value in students.items():
    average_grade[name] = sum(value) / len(value)
    if average_grade[name] < 4.50:
        average_grade.pop(name)
descending = dict(sorted(average_grade.items(), key=lambda x: x[1], reverse=True))
for key, value in descending.items():
    print(f'{key} -> {value:.2f}')

