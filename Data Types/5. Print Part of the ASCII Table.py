start = int(input())
finish = int(input())
total = ''
for i in range(start, finish + 1):
    i_as = chr(i)
    total += i_as + ' '
print(total)