import random,json,os

class Ludok:
    def __init__(self,name,balance,id,kod,bonuss):
        self.name = name
        self.__balance = balance
        self.id = id
        self.kod = kod
        self.bonuss = bonuss
    def get_colb(self):
        while True:
            choice = input("Choose black, red or green (b/r/g): ")
            if choice in ['b', 'r', 'g']:
                return choice
            print(" Invalid choice.")
    def get_numb(self):
        while True:
            number = int(input("Choose a number between 0 and 36: "))
            if number in range(0, 37):
                return number
            print("Invalid number. Please choose a number between 0 and 36.")
    def play_again(self):
        while True:
            choice = input("Do you want to play again? (y/n): ")
            if choice in ['y', 'n']:
                return choice
            print("Invalid choice. Please enter 'y' or 'n'.")
    def play_rulet(self):
        red = list(range(1, 19))
        black = list(range(19, 37))
        green = 0
        print("Welcome to the rulet KAZIK!")
        while True:
                balance = self.__balance
                print(f"Your balance is: {balance}")
                number = random.randint(0, 36)
                bet = int(input("Enter your bet amount: "))
                if bet > balance:
                    print("You don't have enough balance for that bet.")
                    continue
                choice_reshim = input("Do you want to bet on a color or a number? (c/n): ")
                if choice_reshim == 'c':
                     choice = self.get_colb()
                     balance -= bet
                     if choice == 'b' and number in black:
                        print(f"The ball landed on {number} (black). You win!")
                        balance += bet * 2
                     elif choice == 'r' and number in red:
                        print(f"The ball landed on {number} (red). You win!")
                        balance += bet * 2
                     elif choice == 'g' and number == green:
                        print(f"The ball landed on {number} (green). You win!")
                        balance += bet * 35
                     else:
                        if number in black:
                             ballcolor = "black"
                        if number in red:
                             ballcolor = "red"
                        if number == green:
                             ballcolor = "green"
                        print(f"The ball landed on {number} ({ballcolor}). You lose.")
                if choice_reshim == 'n':
                     choice = self.get_numb()
                     balance -= bet
                     if choice == number:
                        print(f"The ball landed on {number}. You win!")
                        balance += bet * 35
                     else:
                        print(f"The ball landed on {number}. You lose.")
                self.__balance = balance
                play_again = self.play_again()
                if play_again == 'n':
                    print(f"Your final balance is: {balance}")
                    break
        
with open("LUDOKLIST.json", "r", encoding="utf-8") as file:
        data= json.load(file)

def find_user():
    user_name = input("Uzrakstiet savu Vardu:")
    user_kod = input("Uzrakstiet savu kodu:")
    user = next((user for user in data if user["Name"] == user_name and user["Self kod"] == user_kod), None)
    if user: 
        player = Ludok(user["Name"], user["Bank"], user["Player Id"], user["Self kod"], user["Vai bonuss ir izmantots?"])
        return player

def save_balance(player):
    for user in data:
        if user["Name"] == player.name and user["Self kod"] == player.kod:
            user["Bank"] = player._Ludok__balance
            break
    with open("LUDOKLIST.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

player = find_user()
player.play_rulet()
save_balance(player)