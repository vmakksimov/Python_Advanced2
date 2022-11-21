text = input()
letter = ''
digit = ''
char = ''

for words in text:
    if words.isalpha():
        letter += words
    elif words.isdigit():
        digit += words
    else:
        char += words
print(digit)
print(letter)
print(char)