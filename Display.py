# contains all the CLI display formatting

# shows basic commands
def helpMenu():
    print("BASIC INPUTS")
    print("add - add a new transaction")
    print("EXAMPLE: add [amount] [purchase_category]")
    # print("del - get rid of a transaction")
    # print("EXAMPLE: del list")


def inputError():
    print("Input not recognized, try again.")


def addHelpMenu():
    print("SYNTAX: add [amount] [category]")
    print("EXAMPLE: add 1000 work")