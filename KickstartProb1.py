# Kickstart Code Jam
# Code by Michael Sherif Naguib
# @ The University of Tulsa
# September 21, 2018
# Google Kickstart Event By Rodrigo Chandia & Evan Forbes



#Get and Parse Case By case the input data returns: (citiesList,bussQuantity,busRouteData,endIndex)
def parseCaseData(rawData,startingIndex):
    # number of busses
    bussQuantity = int(rawData[startingIndex]) #the input file gives how many numbers

    # get A_n  and B_n  for all the items and make a list
    rawBusRouteData = rawData[startingIndex+1]
    rawBusRouteData = rawBusRouteData.split(" ")
    busRouteData = list(map(lambda x: int(x), rawBusRouteData))# convert to integers

    # the P number of cities interested in not number of cities total
    PCities = int(rawData[startingIndex+2])

    # the city locations along the line and convert to int
    citiesList = []
    for i in range(1, PCities + 1):
        citiesList.append(int(rawData[startingIndex +2 + i]))


    endIndex = +startingIndex+ 3 +PCities
    return citiesList,bussQuantity,busRouteData,endIndex

#Make shure that the output is always consistant and unified
def formatCaseOut(case,arrayOfArgs):
    myStr = "Case #"+str(case)+":"
    for i in range(0,len(arrayOfArgs)):
        myStr += " "+ str(arrayOfArgs[i])
    print(myStr)

#Divide up by Bus data     [a1,b1,a2,b2]  => [ [a1,b1],  [a2,b2]]
def divideUpBusData(busStopsList):
    #setup data storage
    busByStopsList = []

    for i in range(0,len(busStopsList),2):#JUMP BY the number of items per bus which is 2
        busByStopsList.append([busStopsList[i],busStopsList[i+1]])

    return busByStopsList

#determine if a bus is withine a stop
def cityInBusStopRange(city,busStopsOrdered):
    t = ((busStopsOrdered[0] <= city) and (city <= busStopsOrdered[1]))
    return t

# "if you use python divide your computational ops per sec by 10"
if __name__ == "__main__":

    #==================== Parse the Input Data =================================
    inputFile=  open("small_data.txt","r")#
    rawData = inputFile.read()
    rawData = rawData.split("\n")#Split on the newlines

    #the number of entire sets of data
    NTestCases = int(rawData[0])

    #============================== Main Algorithim ===========================
    previousIndex = 1# becaus first num 0 was NTestCases
    for i in range(1,NTestCases+1):
        citiesList, bussQuantity, routeData, endIndex = parseCaseData(rawData,previousIndex)
        busByStop = divideUpBusData(routeData)  # parses the data so as to each sub list is a 'bus' whcih is a list of its stops
        busByStopOrdered =list(map(sorted, busByStop))  # orders each of those sub lists
        citiesBusCount = []
        for i in range(0, len(citiesList)):#for each city
            cityTally = 0

            for j in range(0, len(busByStopOrdered)): #iterate through each bus range
                if (cityInBusStopRange(citiesList[i], busByStopOrdered[j])):
                    cityTally += 1

            # append
            citiesBusCount.append(cityTally)  # initilize
        formatCaseOut(i,citiesBusCount)
        previousIndex = endIndex + 1 #Continue with next iteration and add one because there is newline between the cases