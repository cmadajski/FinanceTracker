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
            # when numTransactions is less than 5
            if numTransactions <= 5:
                for i in transactionList:
                    i.displayTransaction()
            # when numTransactions exceeds 5
            else:
                j = numTransactions
                while j > numTransactions - 5:
                    transactionList[j - 1].displayTransaction()
                    j -= 1
        # to quit the program
        elif splitString[0] == "del":
            # removes most recent transaction
            if len(splitString) == 1:
                transactionList.pop()
            elif splitString[1].isdigit():
                transactionList.pop(int(splitString[1]))
            # elif splitString[1].isalpha():
                # transactionList.remove(transactionList[1])
            else:
                print("Error deleting transaction")
        elif splitString[0] == "exit":
            mainLoop = False
        # if the input is not recognized, alert the user of an error
        else:
            inputError()


if __name__ == '__main__':
    main()