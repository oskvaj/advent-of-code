import re

with open(
    "C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/python/Day4Input.txt", "r"
) as file:
    originalData = file.read().split("\n")

data = []
for item in originalData:
    item = item.split(":")
    data.append(item[1].split("|"))

sum = 0
for item in data:
    winningNumbers = []
    numbersYouHave = []
    i = 0
    for number in item:
        numbersOnThisHalfOfTheRow = re.findall(r"\d+", number,)
        if i == 0:
            winningNumbers = list(map(int, numbersOnThisHalfOfTheRow))
        elif i == 1:
            numbersYouHave = list(map(int, numbersOnThisHalfOfTheRow))
        i += 1
    i = 0
    for item in winningNumbers:
        if item in numbersYouHave:
            i *= 2
            if i == 0:
                i = 1
    sum += i
print("sum is: " + str(sum))
