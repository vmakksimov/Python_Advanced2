
A_team = 11
B_team = 11
cards = input().split(' ')
removed_cards = []
for card in cards:
    if card in removed_cards:
        continue
    removed_cards.append(card)
    team, card = card.split('-')
    card = int(card)
    if team == 'A' and 1 <= card <= 11:
        A_team -= 1
    elif team == 'B' and 1 <= card <= 11:
        B_team -= 1
    if A_team < 7 or B_team < 7:
        print(f'Team A - {A_team}; Team B - {B_team}')
        print('Game was terminated')
        break
if A_team >= 7 and B_team >= 7:
    print(f'Team A - {A_team}; Team B - {B_team}')

