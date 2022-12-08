n = int(input())
word = input()
new_word = []
match_word = []
for words in range(n):
    current_words = input()
    new_word.append(current_words)
    if word in current_words:
        match_word.append(current_words)
print(new_word)
print(match_word)

