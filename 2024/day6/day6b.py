import time


def increseDirIndex(index):
    if index != 3:
        index += 1
    else:
        index = 0
    return index


start_time = time.perf_counter()
with open("2024/day6/day_6_input.txt", "r") as file:
    rawData = file.read().split()
data = [[char for char in row] for row in rawData]


def isItALoop(data):
    directions = [0, 1, 2, 3]
    dirIndex = 0
    # find guards starting position
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
    startingPos = guardPos.copy()
    startingDir = dirIndex

    isFirstTime = True
    guardIsOnScreen = True
    itr = 0
    while guardIsOnScreen:
        # guard is going up
        if directions[dirIndex] == 0:
            if guardPos[0] - 1 >= 0 and data[guardPos[0] - 1][guardPos[1]] == "#":
                dirIndex = increseDirIndex(dirIndex)
                if isFirstTime:
                    startingDir = dirIndex
                    startingPos = guardPos.copy()
            elif guardPos[0] - 1 >= 0:
                guardPos[0] = guardPos[0] - 1
            else:
                return False
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
                return False
        # guard is going down
        elif directions[dirIndex] == 2:
            if (
                guardPos[0] + 1 < len(data)
                and data[guardPos[0] + 1][guardPos[1]] == "#"
            ):
                dirIndex = increseDirIndex(dirIndex)
            elif guardPos[0] + 1 < len(data):
                guardPos[0] = guardPos[0] + 1
            else:
                return False
        # guard is going left
        elif directions[dirIndex] == 3:
            if guardPos[1] - 1 >= 0 and data[guardPos[0]][guardPos[1] - 1] == "#":
                dirIndex = increseDirIndex(dirIndex)
            elif guardPos[1] - 1 >= 0:
                guardPos[1] = guardPos[1] - 1
            else:
                return False
        # check if we are on same square and same direction as when we started
        if (
            startingPos[0] == guardPos[0]
            and startingPos[1] == guardPos[1]
            and startingDir == dirIndex
            and not isFirstTime
        ):
            return True
        if (
            startingPos[0] == guardPos[0]
            and startingPos[1] == guardPos[1]
            and startingDir == dirIndex
        ):
            isFirstTime = False
        itr += 1
        if itr == 10000:
            return True


sum = 0
for i, row in enumerate(data):
    for j, char in enumerate(row):
        temp = [item.copy() for item in data]
        if temp[i][j] != "^" and temp[i][j] != "#":
            temp[i][j] = "#"
            if isItALoop(temp):
                sum += 1

print(sum)
end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# >10s (unmeasured)
