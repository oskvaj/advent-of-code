import re

with open('C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/python/Day2Input.txt', 'r') as file:
    origionalData = file.readlines()

patternBlue = r'(\d+)\s*(blue)'
patternGreen = r'(\d+)\s*(green)'
patternRed = r'(\d+)\s*(red)'

data = []
for item in origionalData:
    data.append(re.split(';|:', item))

sum = 0
for dataPoint in data:
    blueMatches = []
    redMatches = []
    greenMatches = []
    dataPoint[0] = (re.sub(r'[^0-9]', '', dataPoint[0]))
    for item in dataPoint[1:]:
        matches = re.findall(patternBlue, item)
        for match in matches:
            number, word = match
            blueMatches.append(number)
        matches = re.findall(patternGreen, item)
        for match in matches:
            number, word = match
            greenMatches.append(number)
        matches = re.findall(patternRed, item)
        for match in matches:
            number, word = match
            redMatches.append(number)
    blueMatches = sorted(blueMatches, key=int)
    redMatches = sorted(redMatches, key=int)
    greenMatches = sorted(greenMatches, key=int)
    sum += int(blueMatches[-1])*int(redMatches[-1])*int(greenMatches[-1])

print(sum)