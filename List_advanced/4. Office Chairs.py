number_of_rooms = int(input())
free_chairs_left = 0
all_free_chairs = 0
people = 0
for rooms in range(1, number_of_rooms +1):
    chairs, taken = input().split()
    taken = int(taken)
    all_free_chairs += len(chairs)
    people += taken
    if len(chairs) < taken:
        print(f'{taken - len(chairs)} more chairs needed in room {rooms}')
    else:
        free_chairs_left += len(chairs) - taken
if all_free_chairs >= people:
    print(f'Game On, {free_chairs_left} free chairs left')