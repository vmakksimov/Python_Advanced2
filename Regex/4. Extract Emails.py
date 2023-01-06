import re

text = input()
regex = r'(?<![\-._])\b[a-zA-Z0-9]+[\-._]?[a-zA-Z0-9]+@[a-z]+(\.)?(\-)?[a-z]+[\.][a-z]+[\.a-z]+\b'
pattern = re.finditer(regex, text)
for y in pattern:
    print(y.group())
