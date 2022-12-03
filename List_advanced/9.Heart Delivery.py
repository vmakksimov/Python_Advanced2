
def jump(nums, value, counter):
    if 0 < counter <= len(nums):
        if nums[counter] == 0:
            print(f'Place {counter} already had Valentine\'s day.')
        else:
            nums[counter] -= 2
            if nums[counter] == 0:
                print(f'Place {counter} has Valentine\'s day.')
    elif counter == 0:
        if nums[counter] == 0:
            print(f'Place {counter} already had Valentine\'s day.')
        elif nums[counter] > 0:
            nums[counter] -= 2
            if nums[counter] == 0:
                print(f'Place {counter} has Valentine\'s day.')
    return nums

numbers = [int(el) for el in input().split('@')]
data = input()

counter = 0

counter_houses = 0
while not data == 'Love!':
    command, value = data.split()
    if command == 'Jump':
        value = int(value)
        counter += value
        if counter > len(numbers) - 1:
            counter = 0
        numbers = jump(numbers, value, counter)

    data = input()
print(f'Cupid\'s last position was {counter}.')
for house in numbers:
    if house > 0:
        counter_houses += 1
if counter_houses > 0:
    print(f'Cupid has failed {counter_houses} places.')
else:
    print(f'Mission was successful.')

