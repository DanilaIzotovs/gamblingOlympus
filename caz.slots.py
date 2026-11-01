import random
import time

symbols = ['A', 'B', 'C', 'D', '7']

payouts = {'7' : 10,
           'A' : 5,
           'B' : 4,
           'D' : 3,
           'C' : 2,
           }

def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

def print_reels(reels):
    print('\n ['+' | '.join(reels) +'] \n')

def calculate_payout(reels, bet):
    if reels[0] == reels[1] == reels[2]:
        symbol = reels[0]
        multiplier = payouts[symbol]
        return bet * multiplier, f'Triple {symbol}!!! u won {multiplier}x ur bet!!!'
    elif reels[0] == reels[2] or reels[1] == reels[0] or reels[1] == reels[2]:
        return bet, 'Two of a kind! u got ur bet back.'
    else:
        return 0, 'no match, better luck next time!'

def main():
    balance = 100
    print('=' * 35)
    print('WELCOME TO PYTHON SLOT MACHINE!')
    print('=' * 35)
    print('starting balance: ${balance}')
    print('symbols & triple payouts:')
    for symbol, mult in payouts.items():
        print(f' 3x {symbol} -> {mult}x bet')
    print('any 2x -> 1x bet (money back) ')
    print('=' * 35)

    while balance > 0:
        print(f'\n current balance: ${balance}')
        bet_input = input('enter ur bet amount (or q to quit):').strip().lower()

        if bet_input == 'q':
            print('thanks for playing, final balance:', balance)
            break

        if not bet_input.isdigit():
            print('pls enter a valid number.')
            continue

        bet = int(bet_input)  
        
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
        if bet > balance:
            print("You don't have enough balance for that bet.")
            continue

        balance -= bet
        print('\n spinning the reels...')
        time.sleep(1)

        reels = spin_reels()
        print_reels(reels)

        winnings, message = calculate_payout(reels, bet)
        balance += winnings

        print(message)

        if balance == 0:
            print("\nYou ran out of money! Game Over.")

if __name__ == '__main__':
    main()