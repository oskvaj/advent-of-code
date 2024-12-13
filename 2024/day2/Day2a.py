with open("2024/day2/Day2Input.txt", "r") as file:
    rawData = file.readlines()

data = []
for item in rawData:
    data.append(item.split())

sum = 0
for line in data:
    safe = True
    ascDesc = ""
    if int(line[0]) - int(line[1]) > 0:
        ascDesc = "desc"
    if int(line[1]) - int(line[0]) > 0:
        ascDesc = "asc"
    for i, item in enumerate(line):
        if (i != len(line) - 1) and safe:
            if int(line[i]) - int(line[i + 1]) == 0:
                safe = False
            if ascDesc == "asc":
                if (int(line[i + 1]) - int(line[i])) > 3 or (
                    int(line[i + 1]) - int(line[i])
                ) < 1:
                    safe = False
            elif ascDesc == "desc":
                if (int(line[i]) - int(line[i + 1])) > 3 or (
                    int(line[i]) - int(line[i + 1])
                ) < 1:
                    safe = False
    if safe:
        sum += 1

print(sum)
