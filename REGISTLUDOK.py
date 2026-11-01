import json , random, os

class Ludok:
    def __init__(self,name,balance,id,kod,bonuss):
        self.name = name
        self.__balance = balance
        self.id = id
        self.kod = kod
        self.bonuss = bonuss

    def giv_bal(self):
        kodd = input("Uzrakstiet savu kodu!:")
        if kodd == self.kod:
            return self.__balance

    def Give_Inf (self):
        return(f"Name:{self.name} Bank:{self.__balance} Player Id: {self.id}")
    
    def to_dict(self):
        return {"Name": self.name, "Bank": self.__balance, "Player Id": self.id, "Self kod": self.kod, "Vai bonuss ir izmantots?": self.bonuss }
    
    def predlok(self):
        atb = input("Vai vēlaties iemaksāt naudu? Y = ja N = ne:")
        if atb == "Y":
            dep = input("Deposit:")
            self.deposit(dep)
        elif atb =="N":
            print(f"Jūsu __balance:{self.__balance}")
        else: 
            print("ERROR")

    def deposit(self,dep):
        dep = int (dep)
        self.__balance += dep
        print(f"Balance: {self.__balance}")
    
sp2 = Ludok(
    name = input("Uzrakstiet vards:"),
    balance = 0,
    id = random.randint(1, 99999),
    kod = input("Uzrakstiet kodu:"),
    bonuss = False
)
sp2.predlok()
print (sp2.Give_Inf())

file_path = "LUDOKLIST.json"
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump([], file)

with open("LUDOKLIST.json", "r", encoding="utf-8") as file:
        data= json.load(file)

data.append(sp2.to_dict())

with open ("LUDOKLIST.json","w",encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
