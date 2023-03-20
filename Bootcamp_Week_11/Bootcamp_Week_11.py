class ValueOutOfRange(Exception):
    pass

def RunMenu(menuOptions):

    isValid = False

    while isValid == False:

        print(menuOptions[0] + "\n")

        for x in range(1, len(menuOptions)):
            print(str(x) + ": " + menuOptions[x])

        try:

            menuChoice = int(input("\nPlease make a selection from the list provided:\n"))

            if menuChoice < 1 or menuChoice > len(menuChoice - 1):
                
                raise ValueOutOfRange

        except ValueOutOfRange:

            input("Sorry, you can only select from the list provided...\n[Enter to Try Again]\n\n")

        except ValueError:

            input("Sorry, you can only enter whole numbers...\n[Enter to Try Again]\n\n")

        except:

            input("Error! Please Try again...\n[Enter to Try Again]\n\n")

        else:

            isValid = True

    return menuChoice

def Main():

    menuChoice = 0;

    while menuChoice != 4:

        menuOptions = ["------Menu------", "Start", "Save", "Load", "Exit"]
        menuChoice = RunMenu(menuOptions)

        if menuChoice == 1:

            print("You have selected to Start!")
            input("[Press Enter to Run the Menu Again]")

        elif menuChoice == 2:

            print("You have selected to Save!")
            input("[Press Enter to Run the Menu Again]")

        elif menuChoice == 3:

            print("You have selected to Load!")
            input("[Press Enter to Run the Menu Again]")

        else:

            print("Bye, Bye!")


#Code Will start running from this point--------------------------------------------------------------------------------
Main()
