#Kaleb Chatland Student ID: 000984351
#main file
from DeliveryFunctions import sendTruckOut
from TruckLoading import getFirstTruckLoad
from TruckLoading import getSecondTruckLoad
from TruckLoading import getFirstTruck_SecondLoad
from MainMenuFunctions import displayMenu
from MainMenuFunctions import displayRoutes
from MainMenuFunctions import displayRoutesByTime
from MainMenuFunctions import displayPackageByTime
from MainMenuFunctions import checkInput
from MainMenuFunctions import printPackage

#this brings in each truck list
firstRoute = getFirstTruckLoad()
secondRoute = getSecondTruckLoad()
thirdRoute = getFirstTruck_SecondLoad()
#the trucks are sent sequentially and the total distance combined
r1 = sendTruckOut(firstRoute, 1)
r2 = sendTruckOut(secondRoute, 2)
r3 = sendTruckOut(thirdRoute, 3)
totalDistance = r1 + r2 + r3

class TruckRoute:

    print('Welcome to the WGU truck route algorithm')
    print('All routes completed in', "{0:.1f}".format(totalDistance, 1), 'miles.')
    #Main flow of logic for the user interface
    #Each selection is based on the user input
    running = True
    while running is True:
        s = displayMenu()
        if s == 0:
            print('0 selected, Program will now exit')
            running = False # if 0 is selected, running becomes false and the while loop ends terminating the program
        elif s == 1:
            print('1 selected, all package data will now be shown.')
            displayRoutes()
        elif s == 2:
            userInput = input('2 selected, please enter a time in HH:MM (ex 8:00) format')
            time = checkInput(userInput)
            if type(time) is int:
                displayRoutesByTime(time)
            else:
                print('Incorrect time format entered, please try again.')
        elif s == 3:
            userInput = input('3 selected, please enter a package ID.')
            printPackage(userInput)
        elif s == 4:
            id = input('4 selected, please enter a package ID.')
            time = input('please enter a time in HH:MM (ex 8:00) format')
            i = checkInput(id)
            t = checkInput(time)
            displayPackageByTime(i, t)
        else:# this attempts to catch numbers outside of 0 to 4, letters crash the program
            print('Incorrect input, Please enter a number 0 to 4')
            print()




