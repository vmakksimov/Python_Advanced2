from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')
#time = time + timedelta(seconds=1)
robots = []
products = deque()
available_robots = deque([])
for n in range(len(data)):
    robot_data = data[n].split('-')
    robot = {}
    robot['name'] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot['available_at'] = time
    robots.append(robot)
    available_robots.append(robot)

product = input()
while not product == 'End':
    products.append(product)
    product = input()
time = time + timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f'{robot["name"]} - {current_product} {time.strftime("[%H:%M:%S]")}')
    else:
        for r in robots:
            if time >= r['available_at']:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            print(f'{robot["name"]} - {current_product} {time.strftime("[%H:%M:%S]")}')
    time = time + timedelta(seconds=1)
