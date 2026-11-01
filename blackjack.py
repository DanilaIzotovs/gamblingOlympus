
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


def calculate_score(hand):
    score = sum(hand)

    aces = hand.count(11)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


game = 1

while game == 1:

    player_hand = []
    dealer_hand = []

    for i in range(2):
        player_hand.append(deck.pop(random.randrange(len(deck))))
        dealer_hand.append(deck.pop(random.randrange(len(deck))))

    print("\n=== BLACKJACK ===")

    print(f"Your cards: {player_hand}")
    print(f"Your score: {calculate_score(player_hand)}")

    print(f"Dealer's visible card: {dealer_hand[0]}")

    while calculate_score(player_hand) < 21:

        choice = input("\nHit or Stand? (h/s): ").lower()

        if choice == "h":
            card = deck.pop(random.randrange(len(deck)))
            player_hand.append(card)

            print(f"You got: {card}")
            print(f"Your cards: {player_hand}")
            print(f"Your score: {calculate_score(player_hand)}")

        elif choice == "s":
            break

        else:
            print("Invalid choice!")

    player_score = calculate_score(player_hand)

    if player_score > 21:
        print("\nYou busted! Dealer wins.")

    else:
        print("\nDealer's turn!")

        while calculate_score(dealer_hand) < 17:
            card = deck.pop(random.randrange(len(deck)))
            dealer_hand.append(card)
            print(f"Dealer takes a card: {card}")

        dealer_score = calculate_score(dealer_hand)

        print(f"\nYour cards: {player_hand} = {player_score}")
        print(f"Dealer's cards: {dealer_hand} = {dealer_score}")

        if dealer_score > 21:
            print("Dealer busted! You win!")

        elif player_score > dealer_score:
            print("You win!")

        elif player_score < dealer_score:
            print("Dealer wins!")

        else:
            print("It's a draw!")

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        game = 0

print("\nThanks for playing!")
