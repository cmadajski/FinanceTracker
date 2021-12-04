# handles all transaction information
from datetime import *


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
            self.sign = "+"
        else:
              self.sign = "-"
        self.amountSigned = inAmount
        self.amount = abs(self.amountSigned)
        self.date = inDate
        self.category = inCategory

    def displayTransaction(self):
        print("--------------------")
        print(str(self.sign) + " $" + str(self.amount))
        print("Date: " + str(self.date))
        print("Category: "+ self.category)

    def editTransaction(self, editType: str, inputVal):
        if editType == "amount":
            inputAmount = float(inputVal)
            if inputAmount >= 0:
                self.sign = '+'
            else:
                self.sign = '-'
            self.amountSigned = float(inputAmount)
            self.amount = abs(self.amountSigned)
        elif editType == "category":
            self.category = str(inputVal)
        elif editType == "date":
            self.date = str(inputVal)
        else:
            print('Unrecognized input, edit failed.')