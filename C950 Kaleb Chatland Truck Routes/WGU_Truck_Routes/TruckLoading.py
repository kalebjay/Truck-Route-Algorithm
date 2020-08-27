#This file contains the code needed to load the trucks
import csv
from HashTable import ChainingHashTable
#opens the csv data and saves it to packageData variable
with open("PackageData.csv", encoding="utf-8-sig") as csvfile:
    packageData = csv.reader(csvfile, delimiter=',')
    #Testing purposes, this is to inspect the csv data
    #for row in packageData:
    #    print(row)
    #declaration of variables
    x = 0
    hashTable = ChainingHashTable()
    firstTruck = []
    secondTruck = []
    firstTruck_roundTwo = []
    # this for loop takes each column of the package data and saves it as variables with
    #their proper indexes
    #Space-time complexity O(N) due to for loop
    for col in packageData:
        packageID = col[0]
        address = col[1]
        city = col[2]
        state = col[3]
        zip = col[4]
        deliveryTime = col[5]
        sizeKG = col[6]
        note = col[7]
        start = col[8]
        location = ''  #[9]
        timeStamp = '' #[10]
        status = 'Currently at WGU Hub' #11 used for notes later in the user interface
        value = [packageID,address,city,state,zip,deliveryTime,sizeKG,note,start,location,timeStamp,status]
        #here the values are all saved to the 'value' variable

        #the trucks are loaded manually and the wrong address is corrected
        #commented out code is placed below that could be used to auto load the trucks
        if value[8] == '1':
            value[8] = '8:00'
            firstTruck.append(value)
        if value[8] == '2':
            value[8] = '9:15'
            secondTruck.append(value)
        if 'Wrong address listed' in value[7]:
            value[1] = '410 S State St'
            value[4] = '84111'
            value[8] = '11:00'
            firstTruck_roundTwo.append(value)
        if value[8] == '3':
            value[8] = '11:00'
            firstTruck_roundTwo.append(value)

        hashTable.insert(packageID, value)  # packageID is the key to the hashtable

"""This is here for testing purposes to inspect how each truck has been loaded
print('First Truck has ',len(firstTruck),' packages')
for i in firstTruck:
    print(i)
print()
print('Second Truck has ',len(secondTruck),' packages')
for i in secondTruck:
    print(i)
print('Third Truck has ',len(firstTruck_roundTwo),' packages')
for i in firstTruck_roundTwo:
    print(i)
"""
# series of getters to access the truck data in other files
# all of these have complexity of O(1)
def getHashTable():
    return hashTable

def getFirstTruckLoad():
    return firstTruck

def getSecondTruckLoad():
    return secondTruck

def getFirstTruck_SecondLoad():
    return firstTruck_roundTwo


"""
As mentioned above, this is code that could be used to auto load the trucks. 
It was used and tested mutliple times but I decided to manually load the trucks 
due to optimizing the order of the loads.
        #Checks for time critical packages and others that must be loaded together
        if value[5] != 'EOD' or 'Must be delivered with' in value[7] :
            if 'Delayed on flight' in value[7]:
                value[8] = '9:15'
                value[9] = 'Added at 1'
                secondTruck.append(value)
            else:
                if len(firstTruck) < 16:
                    value[8] = '8:00'
                    value[9] = 'Added at 1'
                    firstTruck.append(value) # first truck loaded
        #Checks for packages that must be on truck two            
        if 'only be on truck 2' in value[7] or 'Delayed on flight' in value[7]:
            if value not in secondTruck:
                value[8] = '9:15'
                value[9] = 'Added at 2'
                secondTruck.append(value) # second truck loaded
        #catches the wrong address, additional code would be needed for 
        #future errors and additional methods to correct them
        if 'Wrong address listed' in value[7]:
            value[1] = '410 S State St'
            value[4] = '84111'
            value[8] = '11:00'
            value[9] = 'Wrong Address was caught'
            firstTruck_roundTwo.append(value)
        #loop that checks for addresses already in the first truck, 
        #if so, they are loaded, this combines packages which greatly 
        #reduces the distances 
        for i in firstTruck:
            if value[1] == i[1] and value[0] != i[0]:
                if len(firstTruck) < 16 and 'only be on truck 2' not in value[7]:
                    if value not in firstTruck and value not in secondTruck:
                        value[8] = '8:00'
                        value[9] = 'Added at for1'
                        firstTruck.append(value)
                else:
                    if value not in secondTruck:
                        value[8] = '9:15'
                        value[9] = 'Added at for1'
                        secondTruck.append(value)
        #same as above only for second truck
        for i in secondTruck:
            if value[1] == i[1] and value[0] != i[0]:
                if value not in firstTruck and value not in secondTruck:
                    value[8] = '9:15'
                    value[9] = 'Added at for2'
                    secondTruck.append(value)
        #any leftover packages are loaded here in the final truck load
        if value not in firstTruck and value not in secondTruck:
            if 'Wrong address listed' not in value[7]: #prevents fistTruck_roundTwo from being overwritten or added twice
                if len(firstTruck_roundTwo) < len(secondTruck) :
                        value[8] = '11:00'
                        firstTruck_roundTwo.append(value)
                else:
                    value[8] = '9:15'
                    value[9] = 'Added at 3'
                    secondTruck.append(value)

        hashTable.insert(packageID, value)  # packageID is the key to the hashtable
"""
