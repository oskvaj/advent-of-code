import re
import sys

def nextValue(conversionNumbers, seed):
    for item in conversionNumbers:
        if seed >= item[0][0] and seed <= item[0][1]:
            return seed - item[1][2]
    return seed

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

print(sublist)

'''for item in data[0]:
    for i in range(item[0], item[1]):
        data[0] += i'''

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

endValue = 0
closestLocation = sys.maxsize
for seed in data[0]:
    endValue = nextValue(seedToSoil, seed)
    endValue = nextValue(soilToFertilizer, endValue)
    endValue = nextValue(fertilizerToWater, endValue)
    endValue = nextValue(waterToLight, endValue)
    endValue = nextValue(lightToTemperature, endValue)
    endValue = nextValue(temperatureToHumidity, endValue)
    endValue = nextValue(humidityToLocation, endValue)
    if endValue < closestLocation:
        closestLocation = endValue

print(closestLocation)