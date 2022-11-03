number = int(input())

for i in range(0, number):
    for K in range(0, number):
        for M in range(0, number):
            print(f'{chr(97 + i)}{chr(97 + K)}{chr(97 + M)}')