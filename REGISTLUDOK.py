import json , random

class Ludok:
    def __init__(self,name,bank,id):
        self.name = name
        self.bank = bank
        self.id = id
    def Give_Inf (self):
        return f"Name:{self.name} Bank:{self.bank} Player Id: {self.id}"
    def to_dict(self):
        return {"Name": self.name, "Bank": self.bank, "Player Id": self.id}
    
sp2 = Ludok(
    name = input("write name:"),
    bank = str(input("deposit:")),
    id = random.randint(1, 99999)
)

print (sp2.Give_Inf)

data = sp2.to_dict()
with open ("LUDOKLIST.json","w",encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

## norm zaebok
