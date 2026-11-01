import json
import random


class Ludok:
    def __init__(self, name, balance, id, kod, bonuss, freespins):
        self.name = name
        self.balance = balance
        self.id = id
        self.kod = kod
        self.bonuss = bonuss
        self.freespins = freespins

    def to_dict(self):
        return {"Name": self.name, "Bank": self.balance, "Player Id": self.id,
                "Self kod": self.kod, "Vai bonuss ir izmantots?": self.bonuss,
                "Free Spins": self.freespins}


def read_file():
    try:
        with open("LUDOKLIST.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save(player):
    data = read_file()
    new = []
    for d in data:
        if d["Player Id"] != player.id:
            new.append(d)
    new.append(player.to_dict())
    with open("LUDOKLIST.json", "w", encoding="utf-8") as f:
        json.dump(new, f, ensure_ascii=False, indent=4)


def register():
    print("\n" + "=" * 40)
    print("          REGISTRATION")
    print("=" * 40)
    name = input("Your name: ")
    kod = str(random.randint(1000000, 9999999))
    for d in read_file():
        while str(d["Self kod"]) == kod:
            kod = str(random.randint(1000000, 9999999))
    id = random.randint(1, 99999)
    player = Ludok(name, 0, id, kod, True, 100)
    save(player)
    print("\n" + "*" * 40)
    print("  YOUR ACCESS CODE:", kod)
    print("  (write it down!)")
    print("  Bonus: 100 FREE SPINS added!")
    print("*" * 40)
    return player


def login():
    while True:
        print("\n" + "-" * 40)
        print("  [code] login   [r] register   [q] quit")
        print("-" * 40)
        kod = input("Access code: ")
        if kod == "q":
            return None
        if kod == "r":
            return register()
        for d in read_file():
            if str(d["Self kod"]) == kod:
                # .get nuzen, potomu chto igroki iz REGISTLUDOK.py ne imejut Free Spins
                player = Ludok(d["Name"], int(d.get("Bank", 0)), d["Player Id"], str(d["Self kod"]),
                               d.get("Vai bonuss ir izmantots?", False), d.get("Free Spins", 0))
                if player.bonuss == False:
                    # bonus eshe ne vzjat -> daem 100 fri spinov
                    player.bonuss = True
                    player.freespins += 100
                    print("\n*** BONUS! You got 100 FREE SPINS! ***")
                    save(player)
                return player
        print("\n  X Wrong code!")


def get_bet(player):
    while True:
        bet = input("\nYour bet (0 = back): ")
        if not bet.isdigit():
            print("  X Enter a number!")
        elif int(bet) > player.balance:
            print("  X Not enough money!")
        else:
            return int(bet)


def slots(player):
    symbols = ["A", "B", "C", "D", "7"]
    pay = {"7": 10, "A": 5, "B": 4, "D": 3, "C": 2}
    max_free_bet = 100  # maksimalnaja stavka na fri spin
    print("\n" + "=" * 40)
    print("                SLOTS")
    print("=" * 40)
    print(" 7 = 10x | A = 5x | B = 4x | D = 3x | C = 2x")
    print(" any pair = bet back")
    while True:
        print("\n" + "-" * 40)
        print(" Balance:", player.balance, "| Free spins:", player.freespins)
        print("-" * 40)
        print(" [s] spin   [f] free spins   [q] back")
        c = input("> ")
        if c == "q":
            return

        if c == "f":
            if player.freespins == 0:
                print("  X No free spins!")
                continue
            bet = input("\nStake per free spin (1-" + str(max_free_bet) + ", enter = 10): ")
            if bet == "":
                bet = 10
            elif bet.isdigit() and 1 <= int(bet) <= max_free_bet:
                bet = int(bet)
            else:
                print("  X Wrong stake")
                continue
            count = input("How many spins? (1-" + str(player.freespins) + " or all): ")
            if count == "all":
                count = player.freespins
            elif count.isdigit() and 1 <= int(count) <= player.freespins:
                count = int(count)
            else:
                print("  X Wrong number")
                continue
            free = True
        elif c == "s":
            bet = get_bet(player)
            if bet == 0:
                return
            count = input("How many spins? (enter = 1): ")
            if count == "":
                count = 1
            elif count.isdigit() and int(count) >= 1:
                count = int(count)
            else:
                print("  X Wrong number")
                continue
            free = False
        else:
            continue

        done = 0
        total_win = 0
        total_bet = 0
        print()
        for i in range(count):
            if free:
                player.freespins -= 1
            else:
                if player.balance < bet:
                    print("  X Not enough money, stopped.")
                    break
                player.balance -= bet
                total_bet += bet
            done += 1
            a = random.choice(symbols)
            b = random.choice(symbols)
            d = random.choice(symbols)
            prize = 0
            if a == b == d:
                prize = bet * pay[a]
            elif a == b or b == d or a == d:
                if free == False:
                    prize = bet
            player.balance += prize
            total_win += prize
            # pokazyvaem vse spini esli ih malo, a esli mnogo - tolko vigrishi
            if count <= 10 or prize > bet:
                print("  [", a, "|", b, "|", d, "]   +" + str(prize))
        print("\n" + "-" * 40)
        print(" Spins:", done, "| Total win:", total_win, end="")
        if free == False:
            print(" | Profit:", total_win - total_bet)
        else:
            print()
        print("-" * 40)
        save(player)


def roulette(player):
    print("\n" + "=" * 40)
    print("               ROULETTE")
    print("=" * 40)
    print(" red/black = 2x | green(0) or number = 36x")
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    while True:
        print("\n" + "-" * 40)
        print(" Balance:", player.balance)
        print("-" * 40)
        bet = get_bet(player)
        if bet == 0:
            return
        mode = input("Bet on [c] color or [n] number? ")
        if mode == "c":
            choice = input("[b] black  [r] red  [g] green: ")
        elif mode == "n":
            choice = input("Number (0-36): ")
        else:
            continue
        player.balance -= bet
        number = random.randint(0, 36)
        if number == 0:
            color = "g"
        elif number in red:
            color = "r"
        else:
            color = "b"
        print("\n  Ball: ( " + str(number) + " )", color)
        if mode == "c" and choice == color:
            if color == "g":
                player.balance += bet * 36
            else:
                player.balance += bet * 2
            print("  >>> YOU WIN! <<<")
        elif mode == "n" and choice == str(number):
            player.balance += bet * 36
            print("  >>> YOU WIN! <<<")
        else:
            print("  --- You lose ---")
        save(player)


def score(hand):
    s = sum(hand)
    aces = hand.count(11)
    while s > 21 and aces > 0:
        s -= 10
        aces -= 1
    return s


def blackjack(player):
    print("\n" + "=" * 40)
    print("               BLACKJACK")
    print("=" * 40)
    while True:
        print("\n" + "-" * 40)
        print(" Balance:", player.balance)
        print("-" * 40)
        bet = get_bet(player)
        if bet == 0:
            return
        player.balance -= bet
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 11] * 4 + [10] * 16
        random.shuffle(deck)
        me = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]
        print("\n Your cards:  ", me, "=", score(me))
        print(" Dealer card: ", dealer[0], "+ [?]")
        while score(me) < 21:
            c = input("\n[h] hit   [s] stand: ")
            if c == "h":
                me.append(deck.pop())
                print("\n Your cards:  ", me, "=", score(me))
            elif c == "s":
                break
        if score(me) > 21:
            print("\n  --- BUST! You lose ---")
        else:
            while score(dealer) < 17:
                dealer.append(deck.pop())
            print("\n Your cards:  ", me, "=", score(me))
            print(" Dealer cards:", dealer, "=", score(dealer))
            print()
            if score(dealer) > 21 or score(me) > score(dealer):
                print("  >>> YOU WIN! <<<")
                player.balance += bet * 2
            elif score(me) == score(dealer):
                print("  === Draw, bet back ===")
                player.balance += bet
            else:
                print("  --- Dealer wins ---")
        save(player)


def menu(player):
    while True:
        print("\n" + "=" * 40)
        print("          OLYMPUS CASINO")
        print("=" * 40)
        print(" Player:", player.name)
        print(" Balance:", player.balance, "| Free spins:", player.freespins)
        print("-" * 40)
        print(" 1) Blackjack")
        print(" 2) Slots")
        print(" 3) Roulette")
        print(" 4) Profile")
        print(" 5) Deposit")
        print(" 0) Log out")
        print("-" * 40)
        c = input("> ")
        if c == "1":
            blackjack(player)
        elif c == "2":
            slots(player)
        elif c == "3":
            roulette(player)
        elif c == "4":
            print("\n" + "=" * 40)
            print("               PROFILE")
            print("=" * 40)
            print(" Name:       ", player.name)
            print(" Player Id:  ", player.id)
            print(" Balance:    ", player.balance)
            print(" Free spins: ", player.freespins)
            print(" Bonus used: ", player.bonuss)
            print("=" * 40)
            input("\n(press Enter to go back)")
        elif c == "5":
            summa = input("\nDeposit amount: ")
            if summa.isdigit():
                player.balance += int(summa)
                save(player)
                print("\n  + Deposited", summa, "| New balance:", player.balance)
            else:
                print("  X Wrong amount")
        elif c == "0":
            save(player)
            return


print("=" * 40)
print("    WELCOME TO GAMBLING OLYMPUS")
print("=" * 40)
while True:
    player = login()
    if player == None:
        break
    menu(player)
