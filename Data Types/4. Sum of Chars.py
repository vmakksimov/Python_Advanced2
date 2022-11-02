n = int(input())
total = 0
for number in range(1, n + 1):
    letter = input()
    code_word = ord(letter)
    total += code_word
print(f'The sum equals: {total}')