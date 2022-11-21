course = input()
final_course = {}
while not course == 'end':
    module, name = course.split(' : ')
    if not module in final_course:
        final_course[module] = [name]
    else:
        final_course[module].append(name)

    course = input()

sorted_by_name = dict(sorted(final_course.items(), key=lambda x: len(x[1]), reverse=True))
for key, value in sorted_by_name.items():
    print(f'{key}: {len(value)}')
    value = sorted(value)
    for name in value:
        print(f'-- {name}')