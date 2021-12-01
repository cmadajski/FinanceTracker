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