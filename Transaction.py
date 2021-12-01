# handles all transaction information
from datetime import date


class Transaction:
    # fields with type annotations
    amount: int
    direction: str
    date: str
    category: str

    def __init__(self, inAmount: int, inCategory: str):
        self.amount = inAmount
        # determine if credit or debit
        if inAmount >= 0:
            self.direction = "debit"
        else:
            self.direction = "credit"
        self.date = str(date.today())

        self.category = inCategory

    def displayTransaction(self):
        print("Transaction: " + str(self.amount))
        print("Type: " + self.direction)
        print("Date: " + self.date)
        print("Category: " + self.category)