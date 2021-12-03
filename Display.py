# contains all the CLI display formatting

# shows basic commands
def helpMenu():
    print("BASIC INPUTS")
    print("ADD - add a new transaction")
    print("EXAMPLE: add [amount] [category]")
    print("DEL - remove transaction from the list; defaults to most recently added transaction")
    print("EXAMPLE: del")
    print("to remove transaction at a specific index")
    print("EXAMPLE: del [index]")
    print("SHOW - lists 5 most recent transactions")
    print("EXAMPLE: show")
    print("EXIT - exit the program (saves transaction data to file)")
    print("EXAMPLE: exit")



def inputError():
    print("Input not recognized, try again.")


def showCommands():
    print("COMMANDS")
    print("ADD  ||  SHOW  || DEL  ||  HELP  ||  EXIT")


def addHelpMenu():
    print("SYNTAX: add [amount] [category]")
    print("EXAMPLE: add 1000 work")