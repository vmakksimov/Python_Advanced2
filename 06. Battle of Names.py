n = int(input())
even_n = set()
odd_n = set()

for el in range(1, n +1):
    calculator = 0
    name = input()
    for letter in name:
        calculator += ord(letter)
    result = calculator // el
    if result % 2 == 0:
        even_n.add(result)
    else:
        odd_n.add(result)

if sum(even_n) == sum(odd_n):
    modified = [str(el) for el in (even_n.union(odd_n))]
    print(f"{', '.join(modified)}")
elif sum(odd_n) > sum(even_n):
    modified = [str(el) for el in odd_n.difference(even_n)]
    print(f"{', '.join(modified)}")
elif sum(even_n) > sum(odd_n):
    modified = [str(el) for el in even_n.symmetric_difference(odd_n)]
    print(f"{', '.join(modified)}")