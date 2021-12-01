# handles all transaction information
from datetime import date


class Transaction:
    # fields with type annotations
    amount: float
    direction: str
    date: str
    category: str

    def __init__(self, inAmount: int, inCategory: str):
        if inAmount >= 0:
            self.direction = "Credit(+)"
        else:
            self.direction = "Debit(-)"
        self.amount = abs(inAmount)
        currDate = date.today()
        # format date
        self.date = currDate.strftime("%m/%d/%Y")
        self.category = inCategory

    def displayTransaction(self):
        print("--------------------")
        print(str(self.direction) + ": $" + str(self.amount))
        print("Purchased: " + self.date)
        print("Category: "+ self.category)