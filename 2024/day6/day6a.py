def increseDirIndex(index):
    if index != 3:
        index += 1
    else:
        index = 0
    return index


with open("2024/day6/day_6_input.txt", "r") as file:
    rawData = file.read().split()
data = [[char for char in row] for row in rawData]

directions = [0, 1, 2, 3]
dirIndex = 0

# find guard
guardPos = []
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char == "^":
            dirIndex = 0
            guardPos.append(i)
            guardPos.append(j)
        elif char == ">":
            dirIndex = 1
            guardPos.append(i)
            guardPos.append(j)
        elif char == "v":
            dirIndex = 2
            guardPos.append(i)
            guardPos.append(j)
        elif char == "<":
            dirIndex = 3
            guardPos.append(i)
            guardPos.append(j)
# guard is at data[guardPos[0]][guardPos[1]]
data[guardPos[0]][guardPos[1]] = "X"

sum = 1
guardIsOnScreen = True
while guardIsOnScreen:
    # change the square the first time the guard walks on it
    if data[guardPos[0]][guardPos[1]] == ".":
        data[guardPos[0]][guardPos[1]] = "X"
        sum += 1
    # guard is going up
    if directions[dirIndex] == 0:
        if guardPos[0] - 1 >= 0 and data[guardPos[0] - 1][guardPos[1]] == "#":
            dirIndex = increseDirIndex(dirIndex)
        elif guardPos[0] - 1 >= 0:
            guardPos[0] = guardPos[0] - 1
        else:
            guardIsOnScreen = False
    # guard is going right
    elif directions[dirIndex] == 1:
        if (
            guardPos[1] + 1 < len(data[guardPos[0]])
            and data[guardPos[0]][guardPos[1] + 1] == "#"
        ):
            dirIndex = increseDirIndex(dirIndex)
        elif guardPos[1] - 1 < len(data[guardPos[0]]):
            guardPos[1] = guardPos[1] + 1
        else:
            guardIsOnScreen = False
    # guard is going down
    elif directions[dirIndex] == 2:
        if guardPos[0] + 1 < len(data) and data[guardPos[0] + 1][guardPos[1]] == "#":
            dirIndex = increseDirIndex(dirIndex)
        elif guardPos[0] + 1 < len(data):
            guardPos[0] = guardPos[0] + 1
        else:
            guardIsOnScreen = False
    # guard is going left
    elif directions[dirIndex] == 3:
        if guardPos[1] - 1 >= 0 and data[guardPos[0]][guardPos[1] - 1] == "#":
            dirIndex = increseDirIndex(dirIndex)
        elif guardPos[1] - 1 >= 0:
            guardPos[1] = guardPos[1] - 1
        else:
            guardIsOnScreen = False

for item in data:
    print(item)

print("\n\n", sum)
