import time

start_time = time.perf_counter()
with open("2024/day5/day_5_input.txt", "r") as file:
    dataRaw = file.read()
dataRaw = dataRaw.split("\n\n")

restrictions = [item.split("|") for item in dataRaw[0].split("\n")]
sequences = [[int(item) for item in row.split(",")] for row in dataRaw[1].split()]

sum = 0
for row in sequences:
    # Check all requecies to the left
    shouldBeIncluded = False
    for index, _ in enumerate(row):
        for i in range(len(row) - 1):
            if i < index:
                for data in restrictions:
                    if data[0] == row[index] and data[1] == row[i]:
                        shouldBeIncluded = True
                        temp = row[i]
                        row[i] = row[index]
                        row[index] = temp
                        i = 0
    if shouldBeIncluded:
        sum += int(row[int((len(row) - 1) / 2)])
print(sum)
end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 2249.44 ms
