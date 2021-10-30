def numbers_searching(*numbers):
    numbers = list(numbers)
    result = []
    missing = []
    max_n = max(numbers)
    min_n = min(numbers)
    for el in range(min_n, max_n +1):
        if el not in  numbers:
            missing.append(el)
        else:
            if numbers.count(el) > 1:
                result.append(el)
    missing.append(result)

    return missing


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))