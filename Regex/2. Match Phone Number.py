import re
text = input()
pattern = r'(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'
regex = re.finditer(pattern, text)
final_result = [p.group(0) for p in regex]
print(", ".join(final_result))
