n = int(input())
tank = 255
total = 0
for i in range(1, n + 1):
    capacity = int(input())
    if capacity > tank:
        print('Insufficient capacity!')
    else:
        total += capacity
        tank -= capacity
print(total)
