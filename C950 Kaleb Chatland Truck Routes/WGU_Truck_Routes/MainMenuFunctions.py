#this file contains all of the functions used by the main file which are all
# used to display information to the user
from TruckLoading import getHashTable

#function is used to display the main menu for the user
#they are prompted to enter a number and based on that selection
# they will be taken to further options
#Space-time complexity O(1)
def displayMenu():
    print('Enter a number 0 to 4 for the following selections: ')
    print('0: Exit the program')
    print('1: Display all package data')
    print('2: Display all packages at specified times')
    print('3: Enter package ID for specific package info')
    print('4: Enter package ID with time for delivery times')
    selection = int(input())
    return selection
#displays all data run through the program including notes
#Space-time complexity O(N)
def displayRoutes():
    print('All packages including notes')
    for i in range(1, 41):
        print(getHashTable().search(str(i)))
#displays all data based on a time provided by the user
#Space-time complexity O(N)
def displayRoutesByTime(t):
    for i in range(1, 41):
        startTime = getHashTable().search(str(i))[8]
        deliveryTime = getHashTable().search(str(i))[10]
        s = checkInput(startTime)
        d = checkInput(deliveryTime)
        if s >= t:
            getHashTable().search(str(i))[11] = 'Currently at WGU hub'
            getHashTable().search(str(i))[5] = 'Departs for delivery at: ' + startTime
            printPackage(i)
        else:
            if t < d :
                getHashTable().search(str(i))[11] = 'Out for delivery'
                getHashTable().search(str(i))[5] = 'Departed hub at: ' + startTime
                printPackage(i)
            else:
                getHashTable().search(str(i))[11] = 'Delivered at: ' + deliveryTime
                getHashTable().search(str(i))[5] = 'Departed hub at: ' + startTime
                printPackage(i)
#similar to the function above, it takes a user package ID and a time
#and displays that particuar package's info
#Space-time complexity O(1)
def displayPackageByTime(i, t):
    startTime = getHashTable().search(str(i))[8]
    deliveryTime = getHashTable().search(str(i))[10]
    s = checkInput(startTime)
    d = checkInput(deliveryTime)
    if s >= t:
        getHashTable().search(str(i))[11] = 'Currently at WGU hub'
        getHashTable().search(str(i))[5] = 'Departs for delivery at: ' + startTime
        printPackage(i)
    else:
        if t < d:
            getHashTable().search(str(i))[11] = 'Out for delivery'
            getHashTable().search(str(i))[5] = 'Departed hub at: ' + startTime
            printPackage(i)
        else:
            getHashTable().search(str(i))[11] = 'Delivered at: ' + deliveryTime
            getHashTable().search(str(i))[5] = 'Departed hub at: ' + startTime
            printPackage(i)
#This function is called repetitively and displays basic data for each package
#Space-time complexity O(1)
def printPackage(i):
    print('Package ID:', getHashTable().search(str(i))[0],
          ' Address:', getHashTable().search(str(i))[1], getHashTable().search(str(i))[2],
                        getHashTable().search(str(i))[3], getHashTable().search(str(i))[4],
          ' Due by ', getHashTable().search(str(i))[5],
          ' Weight in Kilograms:', getHashTable().search(str(i))[6],
          ' Time of delivery: ', getHashTable().search(str(i))[10],
          ' Package status:', getHashTable().search(str(i))[11])
#checks the input provided by a user and converts
#it to an integer, this allows for times to be simply compared
#Space-time complexity O(N)
def checkInput(string):
    chars = [':', ';', '!', "*", ' ', 'A', 'M', 'P']
    for i in chars:
        string = string.replace(i, '')
    try:
        t = int(string)
        return t
    except ValueError:
        print('Error, value not an integer')










