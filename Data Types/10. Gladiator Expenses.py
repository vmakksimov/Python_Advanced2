lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_counter = 0
sword_counter = 0
shield_counter = 0
total = 0

for game in range(1, lost_fights +1):
    if game % 2 == 0:
        total += helmet_price
    if game % 3 == 0:
        total += sword_price
    if game % 6 == 0:
        total += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            total += armor_price
print(f'Gladiator expenses: {total:.2f} aureus')