import re
data = input().lower()
searched_word = input().lower()
result_no = f'\\b{searched_word}\\b'
regex = re.findall(result_no, data)
result = regex.count(searched_word)
print(result)


