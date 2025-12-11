import re

with open(
    "C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/python/Day3Input.txt", "r"
) as file:
    originalData = file.read().split("\n")

sum = 0
i = 0

for dataRow in originalData:
    j = 0
    shouldBeSummized = False
    for item in dataRow:
        numbersNextToTheGears = []
        #Hitta alla *
        if dataRow[j] == '*':
            if dataRow[j] == '*':
                if originalData[i-1][j-1].isdigit():
                    numbersNextToTheGears.append([i-1, j-1])
                if originalData[i-1][j].isdigit():
                    numbersNextToTheGears.append([i-1, j])
                if originalData[i-1][j+1].isdigit():
                    numbersNextToTheGears.append([i-1, j+1])
                if originalData[i][j-1].isdigit():
                    numbersNextToTheGears.append([i, j-1])
                if originalData[i][j+1].isdigit():
                    numbersNextToTheGears.append([i, j+1])
                if originalData[i+1][j-1].isdigit():
                    numbersNextToTheGears.append([i+1, j-1])
                if originalData[i+1][j].isdigit():
                    numbersNextToTheGears.append([i+1, j])
                if originalData[i+1][j+1].isdigit():
                    numbersNextToTheGears.append([i+1, j+1])
            removeThisList = []
            k = 0
            for item in numbersNextToTheGears:
                for thing in numbersNextToTheGears:
                    if (
                        thing == item
                        or thing in removeThisList
                    ): 
                        pass
                    elif thing[0] == item[0]:
                        if (
                            thing[1] == item[1] +1
                            or thing[1] == item[1] -1
                        ):  
                            removeThisList.append(item)
            for item in removeThisList:
                numbersNextToTheGears.remove(item)
            k = 0
            l = 0
            if len(numbersNextToTheGears) == 2:
                print(numbersNextToTheGears)
                for item in numbersNextToTheGears:
                    tempValue = 1
                    numbers = []
                    newValues = []
                    for thing in originalData[numbersNextToTheGears[l][0]]:
                        if thing.isdigit():
                            numbers.append([thing, k])
                        k += 1
                    l += 1
                    k = 0
                    for num,index in numbers:
                        if len(newValues) == 0:
                            newValues.append([num, [index]])
                        elif newValues[-1][1][-1] == index-1:
                            newValues[-1][0] += num
                            newValues[-1][1].append(index)
                        else:
                            newValues.append([num, [index]])
                    print(newValues)
                    for item in newValues:
                        if numbersNextToTheGears[0][k] in newValues[k][1]:
                            print(newValues[k][0])
                            tempValue *= newValues[k][0]
                        k+=1
                    if tempValue != 1:
                        sum += int(tempValue)
                    print(sum)
                l = 0
        j += 1
    i += 1