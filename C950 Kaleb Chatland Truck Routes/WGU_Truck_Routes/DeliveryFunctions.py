#this file contains all of the main functions needed to compute the
#most optimal route. These are also the functions discussed in the paper
import csv
import datetime
from TruckLoading import getHashTable
#opens the distance data and saves it to distances variable
with open("Distances.csv", encoding="utf-8-sig") as csvfile:
    distances = list(csv.reader(csvfile, delimiter=','))
    # Testing purposes to inspect csv data
    #for i in distanceData:
    #    print(i)
    def getDistanceData():
        return distances
#opens address data which is used for locations, this is needed to match
#the distances and addresses, without it, there is no way to correlate the distances
with open("AddressIDs.csv", encoding="utf-8-sig") as csvfile:
    addresses = list(csv.reader(csvfile, delimiter=','))
    #Testing purposes to inspect csv data
    #for i in addressData:
    #    print(i)
    def getAddressData():
        return addresses

distanceData = getDistanceData()
addressData = getAddressData()
#This function assigns address numbers pulled in from the address data.
# This is important because it is how the distances are calculated between points
#the function searches through both the list given and compares it to the
# address data, when there is a match it assigns that location to the 9th index
#Space-time complexity O(N^2)
def assignLocations(route):
    try:
        i = 0
        for j in route:
            for k in addressData:
                if j[1] == k[1]:
                    route[i][9] = k[0]
            i += 1
    except IndexError:
        pass
    return route
#this function recieves a two numbers which are the row and column in the
#distance data. If it is blank, it flips and reads the other way. This allows
# for any order combination of two locations to be readily found
##Space-time complexity O(1)
def getDistance(row, col):
    distance = distanceData[row][col]
    if distance is '':
        distance = distanceData[col][row]
    return float(distance)
"""
The mother queen bread and butter function of the program
It has two parameters, an unordered list and an integer representing
a location. This function works by utilizing a greedy algorithm. The greedy part is the first for loop as it
picks the shortest distance and saves it. Once that loop finishes, it then does another for loop
that again finds the shortest distance. When it is found, it creates an optimized list and saves the location. 
This process represents a point or address on the map. The original list is cut short with .pop which
represents a point visited. The function then is called again recursively and the hunt for
the next shortest point begins. The optimized list grows while the original list gets shorter and shorter. 
This is important as it will eventually get to zero or empty which satisfies the base case. Once the last
point has been 'visited', the list is now empty and the function can stop its recursive calls. 
The optimized list has now been created and is returned when the base case executes.

The space time complexity is O(N^2) due to the two for loops
"""
optimizedRoute = []
def getOptimalRoute(routeList, location):
    if len(routeList) == 0:
        return optimizedRoute
    else:
        try:
            shortest = 20.0
            newLocation = 0
            for i in routeList:
                d = getDistance(location, int(i[9]))
                if d < shortest:
                    shortest = d
                    newLocation = int(i[9])
            for i in routeList:
                d = getDistance(location, int(i[9]))
                if d == shortest:
                    optimizedRoute.append(i)
                    routeList.pop(routeList.index(i))
                    location = newLocation
                    return getOptimalRoute(routeList, location)
        except IndexError:
            pass
#Start times of each truck respectively
#this function converts a distance into minutes which is then accumulated as a timestamp
#Space-time complexity O(N)
startTime1 = ['8:00']
startTime2 = ['9:15']
startTime3 = ['11:00']
def getTimeStamp(distance, truckNumber):
    ts = ''
    startTime = []
    minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(distance /18 * 60, 60))
    if truckNumber == 1:
        startTime = startTime1
    if truckNumber == 2:
        startTime = startTime2
    if truckNumber == 3:
        startTime = startTime3
    startTime.append(minutes)
    stamp = datetime.timedelta()
    for i in startTime:
        (h, m) = i.split(':')
        s = datetime.timedelta(hours=int(h), minutes=int(m))
        stamp += s
        ts = str(stamp)
    if len(ts) == 8:
        timeStamp = ts[:5]
    else:
        timeStamp = ts[:4]
    return timeStamp

#this function takes an optimzed list and delivers the packages
#Since the 18 mph is constant, no time is required in the deliver
#and the timestamp takes emmediate effect
#Space-time complexity O(N)
def deliverPackages(route, truckNumber):
    totalDistance = float(0)
    for i in range(len(route)):
        try:
            if i != 0:
                distance = getDistance(int(route[i-1][9]), int(route[i][9]))
            else:
                distance = getDistance(0, int(route[i][9]))
            timeStamp = getTimeStamp(distance, truckNumber)
            route[i][10] = timeStamp
            route[i][11] = 'Delivered'
            totalDistance += distance
            getHashTable().update(int(route[i][0]), route)
            i += 1
        except IndexError:
            pass
    return totalDistance

#this function is here to combine functions so a truck list can be sent
#from the main menu and a total distance returned. This allows for
#one truck list to be sent and processed. This also makes trouble-shooting easier.
#Space-time complexity O(1)
def sendTruckOut(newRoute, truckNumber):
    optimizedRoute.clear()
    assignedRoute = assignLocations(newRoute)
    optzdRoute = getOptimalRoute(assignedRoute, 0)
    absTotalDistance = deliverPackages(optzdRoute, truckNumber)

    return absTotalDistance

