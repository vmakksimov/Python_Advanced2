
secret_massage = input().split()
new_word = []

for words in secret_massage:
    digits_to_convert = ''
    strings = []
    for word in words:
        if word.isdigit():
           digits_to_convert += word
        elif word.isalpha():
            strings.append(word)
    digits_to_convert = chr(int(digits_to_convert))
    strings[0], strings[-1] = strings[-1], strings[0]
    for wordy in strings:
        digits_to_convert += wordy
    new_word.append(digits_to_convert)
print(*new_word, sep=' ')









