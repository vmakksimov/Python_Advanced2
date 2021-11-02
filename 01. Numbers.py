first_seq_set = set([int(el) for el in input().split()])
second_seq = set([int(el) for el in input().split()])


n = int(input())
for commands in range(n):
    command = input().split()
    act = command.pop(0)
    number = command.pop(0)
    if act == 'Add':
        if number == 'First':
            [first_seq_set.add(int(el)) for el in command]
        elif number == 'Second':
            [second_seq.add(int(el)) for el in command]
    elif act == 'Remove':
        if number == 'First':
            if len(first_seq_set) > 0:
                [first_seq_set.remove(int(el)) for el in command if int(el) in first_seq_set]
        elif number == 'Second':
            if len(second_seq) > 0:
                [second_seq.remove(int(el)) for el in command if int(el) in second_seq]
    elif act == 'Check':
        if first_seq_set.issubset(second_seq) or second_seq.issubset(first_seq_set):
            print('True')
        else:
            print('False')

if len(first_seq_set) > 0:
    modified_first = sorted([int(el) for el in first_seq_set])
    print(*modified_first, sep=', ')
if len(second_seq) > 0:
    modified_second = sorted([int(el) for el in second_seq])
    print(*modified_second, sep=', ')



