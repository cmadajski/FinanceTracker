from datetime import *
from Display import *
from Statistics import *
from Transaction import *


# program execution starts here
def main():

    mainLoop = True

    # list holds Transaction objects
    transactionList = []

    # start tracking important metrics
    stats = Statistics()

    # determines today's date
    today = date.today()
    currDate = today.strftime("%d/%m/%Y")

    # read Transaction data from data.txt
    readFile = open("data.txt", "r")
    linesRead = 0
    currLine = readFile.readline()
    while currLine:
        splitLine = currLine.split()
        if splitLine[0] == "stats":
            stats.readStats(float(splitLine[1]), float(splitLine[2]), float(splitLine[3]))
        else:
            transactionList.append(Transaction(float(splitLine[0]), splitLine[1], splitLine[2]))
            linesRead += 1
        currLine = readFile.readline()
    readFile.close()
    print("Transactions loaded from memory: " + str(linesRead))

    # MAIN LOOP
    while(mainLoop):
        # get user input
        userInput = input(">> ")
        # separate string commands by whitespace
        splitString = userInput.split()
        if len(splitString) == 0:
            noCommand()
        # shows command examples
        elif splitString[0] == "help":
            helpMenu()
        # adds a new transaction to the Transactions list
        elif splitString[0] == "add":
            if len(splitString) == 1:
                print("Function not implemented yet :'(")
            elif splitString[1] == "help":
                addHelpMenu()
            else:
                transactionList.append(Transaction(float(splitString[1]), splitString[2], currDate))
                stats.addBalance(float(splitString[1]))
        # shows most recent transaction
        elif splitString[0] == 'edit':
            # default case, edit the most recent transaction
            if len(splitString) == 1:
                print('Select [amount] as float, [date] as MM/DD/YYYY, or [category] as str:')
                editInput = input('>> ')
                editlist = editInput.split()
                mostRecent = len(transactionList) - 1
                if editlist[0] == "amount":
                    stats.editBalance(transactionList[mostRecent].amountSigned, float(editlist[1]))
                transactionList[mostRecent].editTransaction(editlist[0], editlist[1])

            # elif splitString[1].isdigit():
                # currTransaction = transactionList[splitString[1]]
            else:
                print("LOLWUT M8, GET REKT")
        elif splitString[0] == "ls":
            numTransactions = len(transactionList)
            # when numTransactions is less than 5, show all transactions
            if numTransactions <= 5:
                i = numTransactions - 1
                while(i > -1):
                    transactionList[i].displayTransaction()
                    i -= 1
            # when numTransactions exceeds 5, show most recent 5 transactions
            else:
                j = numTransactions
                while j > numTransactions - 5:
                    transactionList[j - 1].displayTransaction()
                    j -= 1
        elif splitString[0] == "del":
            # removes most recent transaction
            if len(splitString) == 1:
                temp = transactionList.pop()
                stats.updateBalance(temp.amountSigned, "del")
            elif splitString[1].isdigit():
                temp = transactionList.pop(int(splitString[1]))
                stats.updateBalance(temp.amountSigned, "del")
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

        # if the input is not recognized, alert the user of an error
        else:
            inputError()

    print("Total transaction count: " + str(len(transactionList)))
    # save data from the program by writing to data.txt before termination
    writeFile = open("data.txt", "w")
    # writes one transaction per line
    for a in transactionList:
        writeFile.write(str(a.amountSigned) + " " + a.category + " " + a.date + "\n")
    # writes one line with all the statistics
    writeFile.write("stats " + str(stats.balance) + " " + str(stats.flowIn) + " " + str(stats.flowOut))
    writeFile.close()


if __name__ == '__main__':
    main()