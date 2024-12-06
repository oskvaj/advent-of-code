import re

with open(
    "C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/python/Day4Input.txt", "r"
) as file:
    originalData = file.read().split("\n")

data = []
for item in originalData:
    item = item.split(":")
    data.append(item[1].split("|"))

tempCounter = 1
sum = 0
duplicatesOfFutureScratchcards = []
for item in data:
    winningNumbers = []
    numbersYouHave = []
    i = 0
    timesThisCardShouldBeCounted= 1
    for number in item:
        numbersOnThisHalfOfTheRow = re.findall(r"\d+", number,)
        if i == 0:
            winningNumbers = list(map(int, numbersOnThisHalfOfTheRow))
        elif i == 1:
            numbersYouHave = list(map(int, numbersOnThisHalfOfTheRow))
        i += 1
    i = 0
    if len(duplicatesOfFutureScratchcards) > 0:
        timesThisCardShouldBeCounted += duplicatesOfFutureScratchcards.pop(0)
    for item in winningNumbers:
        if item in numbersYouHave:
            i +=1
    for j in range(i):
        if j < len(duplicatesOfFutureScratchcards):
            duplicatesOfFutureScratchcards[j] += timesThisCardShouldBeCounted
        else:
            duplicatesOfFutureScratchcards.append(timesThisCardShouldBeCounted)
    sum += timesThisCardShouldBeCounted
    tempCounter +=1
print(sum)
