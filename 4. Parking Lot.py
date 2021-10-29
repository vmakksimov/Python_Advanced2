number = int(input())

left_cars = set()

for car in range(number):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        left_cars.add(car_number)
    elif direction == 'OUT':
        left_cars.discard(car_number)

if left_cars:
    [print(el) for el in left_cars]
else:
    print('Parking Lot is Empty')
