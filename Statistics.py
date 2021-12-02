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

    def updateBalance(self, amount: float, action: str, inDirection: str):
        # when a new transaction is added
        if action == "add":
            self.balance += amount
            if inDirection == "Credit(+)":
                self.flowIn += amount
            else:
                self.flowOut += amount
        # when a transaction is removed
        elif action == "del":
            self.balance -= amount
            if inDirection == "Credit(+)":
                self.flowIn -= amount
            else:
                self.flowOut -= amount

    def showStats(self):
        print("Total Balance: " + str(self.balance))
        print("Money In: " + str(self.flowIn))
        print("Money Out: " + str(self.flowOut))