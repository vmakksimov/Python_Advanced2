import re
data = input()
regex = r'(?<=\b_)[a-zA-Z0-9]+\b'
pattern = re.findall(regex, data)
result = [y for y in pattern]
print(*result, sep=',')