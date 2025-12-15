import time


def isLineSafe(line):
    isSafe = True
    ascDesc = ""
    if (int(line[0]) - int(line[1])) > 0:
        ascDesc = "desc"
    elif (int(line[0]) - int(line[1])) < 0:
        ascDesc = "asc"
    else:
        isSafe = False
    for i in range(0, len(line) - 1):
        if (i != len(line) - 1) and isSafe:
            if int(line[i]) - int(line[i + 1]) == 0:
                isSafe = False
            if ascDesc == "asc":
                if (int(line[i + 1]) - int(line[i])) > 3 or (
                    int(line[i + 1]) - int(line[i])
                ) < 1:
                    isSafe = False
            elif ascDesc == "desc":
                if (int(line[i]) - int(line[i + 1])) > 3 or (
                    int(line[i]) - int(line[i + 1])
                ) < 1:
                    isSafe = False
    return isSafe


start_time = time.perf_counter()
with open("2024/day2/day_2_input.txt", "r") as file:
    rawData = file.readlines()

data = [item.split() for item in rawData]

sum = 0
for line in data:
    safe = True
    length = len(line)
    for i in range(0, length):
        temp = line.copy()
        temp.pop(i)
        safe = isLineSafe(temp)
        if safe:
            break
    if safe:
        sum += 1

print(sum)
end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 8.41 ms
