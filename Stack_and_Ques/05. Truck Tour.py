from collections import deque
number_of_stations = int(input())
stations = deque()

for _ in range(number_of_stations):
    stations.append([int(el) for el in input().split()])

for big_cirle_iterations in range(number_of_stations):
    is_valid = True
    tank_petrol = 0
    for small_circle_iterations in range(number_of_stations):
        current_station = stations[small_circle_iterations]
        petrol = current_station[0]
        distance_to_next_station = current_station[1]
        tank_petrol += petrol - distance_to_next_station
        if tank_petrol < 0:
            is_valid = False
            stations.append(stations.popleft())
            break
    if is_valid:
        print(big_cirle_iterations)
        break



