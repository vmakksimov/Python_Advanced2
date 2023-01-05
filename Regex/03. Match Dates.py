import re

data = input()
pattern = r'(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'
regex = re.finditer(pattern, data)
for y in regex:
    t = y.groupdict()
    print(f'Day: {t["day"]}, Month: {t["month"]}, Year: {t["year"]}')

