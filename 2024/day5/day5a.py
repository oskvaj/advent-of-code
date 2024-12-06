with open("2024/day5/day_5_input.txt", "r") as file:
    dataRaw = file.read()
dataRaw = dataRaw.split("\n\n")
temp = dataRaw[0].split("\n")
restrictions = []
for item in temp:
    restrictions.append(item.split("|"))
temp = dataRaw[1].split()
sequences = []
for item in temp:
    sequences.append(item.split(","))

sum = 0
for row in sequences:
    # Check all requecies to the left
    shouldBeIncluded = True
    for index, _ in enumerate(row):
        for i in range(len(row) - 1):
            if i < index:
                for data in restrictions:
                    if data[0] == row[index] and data[1] == row[i]:
                        shouldBeIncluded = False
    if shouldBeIncluded:
        sum += int(row[int((len(row) - 1) / 2)])
print(sum)
