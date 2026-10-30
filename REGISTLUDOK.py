import json , random

class Ludok:
    def __init__(self,name,id,kod):
        self.name = name
        self.__balance = 0
        self.id = id
        self.kod = kod
        self.bonuss = False
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
    kod = input("Uzrakstiet kodu:"),
    id = random.randint(1, 99999)
)
sp2.predlok()
print (sp2.Give_Inf())




with open("LUDOKLIST.json", "r", encoding="utf-8") as file:
        data= json.load(file)

data.append(sp2.to_dict())

with open ("LUDOKLIST.json","w",encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
