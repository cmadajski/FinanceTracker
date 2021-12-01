from Transaction import *
from Display import *


# program execution starts here
def main():
    mainLoop = True
    # list holds Transaction objects
    transactionList = []
    while(mainLoop):
        userInput = input(">> ")
        # separate string commands
        splitString = userInput.split()
        if splitString[0] == "help":
            helpMenu()
        elif splitString[0] == "add":
            transactionList.append(Transaction(int(splitString[1]), splitString[2]))
        elif splitString[0] == "show":
            transactionList[0].displayTransaction()
        elif splitString[0] == "exit":
            mainLoop = False
        else:
            inputError()


if __name__ == '__main__':
    main()