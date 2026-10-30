import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

deck = []

for card in cards:
    if card == 10:
        deck.extend([10] * 16)
    elif card == 11:
        deck.extend([11] * 4)
    else:
        deck.extend([card] * 4)

game = 1

while game == 1:

    card1 = random.choice(deck)
    card2 = random.choice(deck)

    if card1 + card2 < 17:
        card3 = random.choice(deck)
        cards = card1 + card2 + card3
        print(cards)
    elif card1 + card2 + card3 < 17:
        card4 = random.choice(deck)
        cards = card1 + card2 + card3 + card4
        print(cards)
    else:
        cards = card1 + card2
        print(cards)
    

    print(f"Dealer takes a card! Its")
    print(f"Dealer takes another card and its flipped!")
    game = game - 1