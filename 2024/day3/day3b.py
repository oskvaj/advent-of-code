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
            for instance in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", item):
                instance = re.sub(r"do\(\)", "1", instance)
                instance = re.sub(r"don't\(\)", "0", instance)
                instance = re.sub(r"mul\(", "", instance)
                instance = re.sub(r"\)", "", instance)
                data.append(instance)

sum = 0
go = 1
for item in data:
    if item == "1":
        go = 1
    elif item == "0":
        go = 0
    elif go == 1:
        temp = []
        temp = item.split(",")
        sum += int(temp[0]) * int(temp[1])

print(sum)
end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 2.09 ms
