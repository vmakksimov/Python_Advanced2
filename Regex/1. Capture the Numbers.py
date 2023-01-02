import re

data = input()

while data:
    regex = r'\d+'
    pattern = re.findall(regex, data)
    for x in pattern:
        print(x, end=' ')
    data = input()

