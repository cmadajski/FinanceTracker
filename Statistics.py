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

    def readStats(self, inBalance: float, inFlowIn: float, inFlowOut: float):
        self.balance = inBalance
        self.flowIn = inFlowIn
        self.flowOut = inFlowOut

    def addBalance(self, amount: float):
        self.balance += amount
        if amount >= 0:
            self.flowIn += amount
        else:
            self.flowOut += abs(amount)

    def delBalance(self, amount: float):
        self.balance -= amount
        if amount >= 0:
            self.flowIn -= amount
        else:
            self.flowOut -= abs(amount)

    def editBalance(self, prevAmount: float, currAmount: float):
        tempBalance = self.balance - prevAmount
        if prevAmount >= 0:
            self.flowIn -= prevAmount
        else:
            self.flowOut -= abs(prevAmount)
        self.balance = tempBalance + currAmount
        if currAmount >= 0:
            self.flowIn += currAmount
        else:
            self.flowOut += abs(currAmount)


    def showStats(self):
        print("Total Balance: $%.2f" % self.balance)
        print("Money In: $%.2f" % self.flowIn)
        print("Money Out: $%.2f (%.2f%%)" % (abs(self.flowOut), (abs(self.flowOut) / self.flowIn) * 100))