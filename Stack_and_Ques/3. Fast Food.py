from collections import deque
quantity = int(input())
orders = deque(input().split())
result = [int(el) for el in orders]
print(max(result))

for order in range(len(orders)):
    if quantity >= result[order]:
        removed = orders.popleft()
        quantity -= int(removed)
    else:
        print(f'Orders left: {" ".join(orders)}')
        break
if not orders:
    print('Orders complete')



