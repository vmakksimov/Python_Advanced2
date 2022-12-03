def shoot(nums, i, v):
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums
def radius(nums, i,r):
    if 0 <= i < len(nums):
        pops = []
        if 0 <= i + r < len(nums) and 0 <= i - r < len(nums):
            pops.append(nums[i])
            pops.append(nums[i + 1])
            pops.append(nums[i - 1])
            for poping in pops:
                if poping in nums:
                    nums.remove(poping)
        else:
            print('Strike missed!')
    else:
        print('Strike missed!')
    return nums
def add(nums, i, v):
    if 0 <= i < len(nums):
        nums.insert(i, v)
    else:
        print('Invalid placement!')
    return nums

targets = [int(el) for el in input().split()]

command = input()
while not command == 'End':
    comm, index, value = command.split()
    if comm == 'Shoot':
        index = int(index)
        value = int(value)
        targets = shoot(targets, index, value)
    elif comm == 'Strike':
        index = int(index)
        value = int(value)
        targets = radius(targets, index, value)
    elif comm == 'Add':
        index = int(index)
        value = int(value)
        targets = add(targets, index, value)
    command = input()
print(*targets, sep='|')