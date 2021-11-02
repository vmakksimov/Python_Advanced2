parantheses = input()

mirror = {'{': '}', '[': ']', '(': ')'}
stack = []
last_perant = ''
is_valid = True
for el in parantheses:
    if el not in mirror.values():
        stack.append(el)
    else:
        if not stack:
            is_valid = False
            break
        last_perant = stack.pop()
        if not el == mirror[last_perant]:
            is_valid = False
            break
if is_valid:
    print('YES')
else:
    print('NO')
