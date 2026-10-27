import random, math, json, time

class Ludok:
    def __init__(self,name,bank,id):
        self.name = name
        self.bank = bank
        self.id = id
    def Give_Inf (self):
        return f"Name:{self.name} Bank:{self.bank} Player Id: {self.id}"
    def to_dict(self):
        return {"Name": self.name, "Bank": self.bank, "Player Id": self.id}


ld1 = Ludok("Kirill",20,8281)

data = ld1.to_dict()

with open ("LUDOKLIST.json","w",encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)