from Transaction import *
from Display import *


# program execution starts here
def main():

    # VARIABLES
    mainLoop = True
    # list holds Transaction objects
    transactionList = []

    # MAIN LOOP
    while(mainLoop):
        # get user input
        userInput = input(">> ")
        # separate string commands by whitespace
        splitString = userInput.split()
        # shows command examples
        if splitString[0] == "help":
            helpMenu()
        # adds a new transaction
        elif splitString[0] == "add":
            transactionList.append(Transaction(int(splitString[1]), splitString[2]))
        # shows most recent transaction
        elif splitString[0] == "show":
            numTransactions = len(transactionList)
            if numTransactions < 5:
                for i in transactionList:
                    i.displayTransaction()
            else:
                for j in range(numTransactions - 1, numTransactions - 5, 1):
                    transactionList[j].displayTransaction()
        # to quit the program
        elif splitString[0] == "exit":
            mainLoop = False
        # if the input is not recognized, alert the user of an error
        else:
            inputError()


if __name__ == '__main__':
    main()