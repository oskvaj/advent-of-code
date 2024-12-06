with open('C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2024/Day1Input.txt', 'r') as file:
    data = file.readlines()
    leftSide = []
    rightSide = []
    for item in data:
        leftSide.append(item.split()[0])
        rightSide.append(item.split()[1])
    leftSide.sort()
    rightSide.sort()

sum = 0

for i in leftSide:
    similar = 0
    for j in rightSide:
        if(i == j):
            similar += 1
    temp = int(i)
    sum += temp*similar

print(sum)