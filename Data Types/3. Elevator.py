number_of_people = int(input())
capacity = int(input())
courses_counter = 0
courses_counter += number_of_people // capacity
if number_of_people % capacity != 0:
    courses_counter += 1
print(courses_counter)