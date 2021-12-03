# handles all transaction information
from datetime import date


class Transaction:
    # fields with type annotations
    amount: float
    # need to distinguish between signed and unsigned for display purposes
    amountSigned: float
    sign: str
    date: str
    category: str

    def __init__(self, inAmount: float, inCategory: str, inDate: str):
        if inAmount >= 0:
            self.direction = "+"
        else:
              self.direction = "-"
        self.amountSigned = inAmount
        self.amount = abs(self.amountSigned)
        self.date = inDate
        self.category = inCategory

    def displayTransaction(self):
        print("--------------------")
        print(str(self.direction) + " $" + str(self.amount))
        print("Date: " + self.date)
        print("Category: "+ self.category)