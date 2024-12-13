import re

with open("2024/day3/day_3_input.txt", "r") as file:
    rawData = file.readlines()

data = []
for i in rawData:
    temp = []
    temp.append(i.split())
    for line in temp:
        for item in line:
            for instance in re.findall(r"mul\((\d+,\d+)\)", item):
                data.append(instance.split(","))

sum = 0
for item in data:
    sum += int(item[0]) * int(item[1])

print(sum)
