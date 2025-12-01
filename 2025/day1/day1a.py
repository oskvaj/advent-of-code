import time


start_time = time.time()
with open("2025/day1/day_1_input.txt", "r") as file:
    rawData = file.readlines()

data = [[item.strip()[0], item.strip()[1:]] for item in rawData]
curr_val = 50
code = 0

for dir, val in data:
    if dir == "L":
        curr_val -= int(val)
    elif dir == "R":
        curr_val += int(val)
    if curr_val > 99 or curr_val < 0:
        curr_val = curr_val % 100
    if curr_val == 0:
        code += 1

print(code)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 4.68 ms
