from Transaction import *
from Display import *


# program execution starts here
def main():
    mainLoop = True
    while(mainLoop):
        userInput = input(">> ")
        if userInput == "help":
            helpMenu()
        elif userInput == "exit":
            mainLoop = False
        else:
            inputError()


if __name__ == '__main__':
    main()