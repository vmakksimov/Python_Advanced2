people = int(input())
days = int(input())
total_coins = 0
companion_coin = 0
for i in range(1, days +1):
    total_coins += 50
    if i % 10 == 0:
        people -= 2
    if i % 15 == 0:
        people += 5
    total_coins -= 2 * people
    if i % 3 == 0:
        total_coins -= 3 * people
    if i % 5 == 0:
        total_coins += 20 * people
        if i % 15 == 0:
            total_coins -= 2 * people
    companions_counter = total_coins / people
print(f'{people} companions received {int(companion_coin)} coins each.')