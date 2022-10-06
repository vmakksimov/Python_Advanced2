

def calculate(nums, nums_left, first_c, second_c):
    if len(nums_left) > 0:
        if first_c == 'add' and second_c == 'beginning':
            nums_left = sorted(nums_left, reverse=True)
        for el in nums_left:

            if first_c == 'add':
                if second_c == 'beginning':
                    nums.insert(0, el)

                elif second_c == 'end':
                    nums.append(el)

            elif first_c == 'remove':
                for removal in range(el):
                    if second_c == 'beginning':
                        nums.pop(0)

                    if second_c == 'end':
                        nums.pop()
    else:
        if second_c == 'beginning':
            nums.pop(0)
        elif second_c == 'end':
            nums.pop()

    return nums

def list_manipulator(*args):
    numbers = args[0]
    first_command = args[1]
    second_command = args[2]
    numbers_left = args[3:]
    numbers = calculate(numbers, numbers_left, first_command, second_command)

    return numbers



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))





