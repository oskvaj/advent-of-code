import time


start_time = time.perf_counter()
with open("2024/day1/day_1_input.txt", "r") as file:
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

end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 2.27 ms
