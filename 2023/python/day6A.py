import re

with open(
    "C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/python/Day6Input.txt", "r"
) as file:
   originalData = file.read().split("\n")

for i, item in enumerate(originalData):
   item = re.sub(r'[^0-9]', ' ', item)
   originalData[i] = list(map(int, re.findall(r"\d+", item)))

data = []
for i in range(0, len(originalData[0])):
   data.append([originalData[0][i], originalData[1][i]])

totalWays = 1
waysForThisRace = 0
for item in data:
   for i in range(0, item[0]+ 1):
        distance = (item[0] - i) * i
        if distance > item[1]:
            waysForThisRace += 1
   totalWays *= waysForThisRace
   waysForThisRace = 0

print(totalWays)