from collections import deque
customers = deque([int(el) for el in input().split(', ')])
taxi = [int(el) for el in input().split(', ')]

total_time = 0
while True:
    if len(customers) <= 0:
        break

    if len(taxi) <= 0:
        break

    current_customer = customers[0]
    current_taxi = taxi[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft()
        taxi.pop()
    else:
        taxi.pop()

if len(customers) <= 0:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')

if len(customers) > 0 and len(taxi) <= 0:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(map(str, customers))}')

