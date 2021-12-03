# calculates important Transaction data

class Statistics:

    # fields
    balance: float
    flowIn: float
    flowOut: float
    # dictionary: keys are categories, values are
    byCategory = {}

    def __init__(self):
        self.balance = 0
        self.flowIn = 0
        self.flowOut = 0

    def updateBalance(self, amount: float, action: str):
        # when a new transaction is added
        if action == "add":
            self.balance += amount
            if amount >= 0:
                self.flowIn += amount
            else:
                self.flowOut += amount
        # when a transaction is removed
        elif action == "del":
            self.balance -= amount
            if amount >= 0:
                self.flowIn -= amount
            else:
                self.flowOut -= amount

    def showStats(self):
        print("Total Balance: $%.2f" % self.balance)
        print("Money In: $%.2f" % self.flowIn)
        print("Money Out: $%.2f (%.2f%%)" % (abs(self.flowOut), (abs(self.flowOut) / self.flowIn) * 100))