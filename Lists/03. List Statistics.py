num = int(input())
positive = []
negative = []

for i in range(1, num + 1):
    current_number = int(input())
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}')