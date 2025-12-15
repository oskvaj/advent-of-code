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

sum = 0

for i in leftSide:
    similar = 0
    for j in rightSide:
        if i == j:
            similar += 1
    temp = int(i)
    sum += temp * similar

print(sum)
end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 56.16 ms
