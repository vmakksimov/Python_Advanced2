result = [int(x) for x in input().split()]
capacity = int(input())

current_value = 0
counter_racks = 0
current_capacity = capacity
while result:
    removed = result.pop()
    if removed <= current_capacity:
        current_capacity -= removed
    else:
        counter_racks += 1
        current_capacity = capacity
        current_capacity -= removed

#if current_value > 0:
    #counter_racks += 1
print(counter_racks)





