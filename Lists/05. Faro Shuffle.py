import copy

cards = input().split()
shuffles = int(input())
top_card = cards[0]
bottom_card = cards[-1]
a = 5
half_deck = len(cards) / 2

shuffle_cards = []
for shuffle_card in range(shuffles):
    left_half = []
    right_half = []
    for index in range(1, int(half_deck)):
        left_half.append(cards[index])
    for index in range(int(half_deck), len(cards) - 1):
        right_half.append(cards[index])

    for index in range(len(left_half)):
        shuffle_cards.append(right_half[index])
        shuffle_cards.append(left_half[index])

    cards = shuffle_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffle_cards = []
print(cards)

