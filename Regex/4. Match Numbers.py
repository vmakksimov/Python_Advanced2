import re

regex = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
data = input()

pattern = re.finditer(regex, data)

result = [y.group(0) for y in pattern]
print(*result)