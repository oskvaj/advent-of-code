import re
import sys

def nextValueSingle(conversionNumbers, seed):
    returnList = []
    breakpoints = []
    outsideOfRange = []
    conversionNumbers.sort()
    for item in conversionNumbers:
        #handles if the input wraps the allowed range
        #Handles if the lower part is part of the range
        if seed[0] >= item[0][0] and seed[0] < item[0][1]:
            if seed[1] < item[0][1]:
                temp = [item[1][0] - (item[0][0] - seed[0]), item[1][1] - (item[0][1] - seed[1] - 1)]
                if temp and temp[0] not in returnList:
                    returnList.append(temp)
                seed[0] = 0
                seed[1] = 0
            else:
                temp = [item[1][0] - (item[0][0] - seed[0]), item[1][1] - (item[0][1] - seed[1]) - (seed[1]-item[0][1]-1)]
                if temp and temp[0] not in returnList:
                    returnList.append(temp)
                breakpoints.append([seed[1] - (seed[1]-item[0][1]-1), seed[1]])
                seed[0]=item[0][1]+1
        #Handles if in range but starts outside
        elif seed[1] >= item[0][0] and seed[1] < item[0][1]:
            temp = [item[1][0], item[1][1] - (item[0][1] - seed[1] - 1)]
            if temp and temp[0] not in returnList:
                returnList.append(temp)
            outsideOfRange.append([seed[0], item[0][0]])
            seed[1] = item[0][0]
        #Handles if it is enterly outside the range
        elif {
            (seed[0] < item[0][0] and seed[1] < item[0][1])
            or (seed[0] >= item[0][1] and seed[1] >= item[0][1])
            }:
            temp = [seed[0], seed[1]]
            if temp not in outsideOfRange and temp != [0,0]:
                outsideOfRange.append(temp)
    if len(breakpoints) == 0:
        returnList += outsideOfRange
        return returnList
    else:
        for item in breakpoints:
            temp = nextValueSingle(conversionNumbers, item)
            if temp and temp[0] not in returnList: 
                returnList += temp
        returnList += outsideOfRange
        return returnList

def nextValue(conversionNumbers, seed):
    returnList = []
    if isinstance(seed[0], int):
        temp = (nextValueSingle(conversionNumbers, seed))
        if temp and temp[0] not in returnList:
            returnList += temp
    else:
        for item in seed:
            temp = nextValueSingle(conversionNumbers, item)
            if temp and temp[0] not in returnList:
                returnList += temp
    return returnList

def getConversionNumbers (data, index):
    returnThisList = []
    for row in data[index][1:]:
        returnThisList.append([[row[1], row[1] + row[2]-1, row[1]-row[0]], [row[0], row[0] + row[2]-1, row[1]-row[0]]])
    return returnThisList

with open(
    "C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/python/Day5Input.txt", "r"
) as file:
    originalData = file.read().split("\n")


data = []
templist = []
for item in originalData:
    if item == '':
        if templist:
            data.append(templist)
        templist = []
    else:
        templist.append(item)
if templist:
    data.append(templist)

data[0] = re.sub(r'[^0-9]', ' ', data[0][0])
data[0] = list(map(int, re.findall(r"\d+", data[0])))

i = 0
sublist = []
templist = []
for item in data[0]:
    if i == 1:
        templist.append(templist[0] + item - 1)
        sublist.append(templist)
        templist = []
        i = 0
    else:
        templist.append(item)
        i +=1
data[0] = sublist

currentRow = 1
currentColumn = 1
for row in data[1:]:
    for item in row[1:]:
        data[currentRow][currentColumn] = list(map(int, re.findall(r"\d+", item)))
        currentColumn += 1
    currentRow += 1
    currentColumn = 1

seedToSoil = getConversionNumbers(data, 1)
soilToFertilizer = getConversionNumbers(data, 2)
fertilizerToWater = getConversionNumbers(data, 3)
waterToLight = getConversionNumbers(data, 4)
lightToTemperature = getConversionNumbers(data, 5)
temperatureToHumidity = getConversionNumbers(data, 6)
humidityToLocation = getConversionNumbers(data, 7)

endValue = []
closestLocation = sys.maxsize

for seed in data[0]:
    endValue = nextValue(seedToSoil, seed)
    endValue = nextValue(soilToFertilizer, endValue)
    endValue = nextValue(fertilizerToWater, endValue)
    endValue = nextValue(lightToTemperature, endValue)
    endValue = nextValue(temperatureToHumidity, endValue)
    endValue = nextValue(humidityToLocation, endValue)
    endValue.sort()
    print(endValue[0][0])
    if endValue[0][0] < closestLocation:
        closestLocation = endValue[0][0]
print(closestLocation)