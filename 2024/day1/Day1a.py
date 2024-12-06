with open('C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2024/Day1Input.txt', 'r') as file:
    data = file.readlines()
    leftSide = []
    rightSide = []
    for item in data:
        leftSide.append(item.split()[0])
        rightSide.append(item.split()[1])
    leftSide.sort()
    rightSide.sort()

dataButFun = []

for i, item in enumerate(leftSide):
    temp = []
    temp.append(leftSide[i])
    temp.append(rightSide[i])
    dataButFun.append(temp)

sum = 0

for item in dataButFun:
    int0 = int(item[0])
    int1 = int(item[1])
    sum += abs(int0 - int1)

print(sum)