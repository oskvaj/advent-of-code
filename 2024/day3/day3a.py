import re
import time


start_time = time.perf_counter()
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
end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 16.11 ms
