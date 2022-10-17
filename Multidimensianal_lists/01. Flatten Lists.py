numbers = input()

matrix = []
current_string = None
index_number = None
for el in range(len(numbers)-1, -1, -1):
    if numbers[el] == '|' or el == 0:
        if current_string:
            current_string = numbers[el:index_number]

        else:
            current_string = numbers[el:]
        index_number = el
        new = current_string.replace('|', '')
        final = new.split()
        for nums in final:
            matrix.append(int(nums))

print(*matrix)