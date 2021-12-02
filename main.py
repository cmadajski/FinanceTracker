from Transaction import *
from Display import *
from Statistics import *


# program execution starts here
def main():

    mainLoop = True

    # list holds Transaction objects
    transactionList = []

    # start tracking important metrics
    stats = Statistics()

    # read Transaction data from data.txt
    readFile = open("data.txt", "r")
    # NON FUNCTIONAL, WIP

    # MAIN LOOP
    while(mainLoop):
        # get user input
        userInput = input(">> ")
        # separate string commands by whitespace
        splitString = userInput.split()
        # shows command examples
        if splitString[0] == "help":
            helpMenu()
        # adds a new transaction to the Transactions list
        elif splitString[0] == "add":
            if splitString[1] == "help":
                addHelpMenu()
            else:
                transactionList.append(Transaction(float(splitString[1]), splitString[2]))
                stats.updateBalance(float(splitString[1]), "add", transactionList[len(transactionList) - 1].direction)
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
        # shows available commands in a simple format, less detailed than "help"
        elif splitString[0] == "cmds":
            showCommands()
        # show current statistics
        elif splitString[0] == "stats":
            stats.showStats()
        # to quit the program
        elif splitString[0] == "exit" or splitString[0] == "quit":
            # end the main loop
            mainLoop = False
            # save data from the program by writing to data.txt before termination
            writeFile = open("data.txt", "w")
            for a in transactionList:
                writeFile.write(str(a.amount) + " " + a.direction + " " + a.date + " " + a.category + "\n")
            writeFile.close()
        # if the input is not recognized, alert the user of an error
        else:
            inputError()


if __name__ == '__main__':
    main()