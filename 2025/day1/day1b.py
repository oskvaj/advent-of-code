import time


start_time = time.time()
with open("2025/day1/day_1_input.txt", "r") as file:
    rawData = file.readlines()

data = [[item.strip()[0], item.strip()[1:]] for item in rawData]
curr_val = 50
code = 0

for dir, val in data:
    if dir == "R":
        new_val = curr_val + int(val)
        crossings = (new_val) // 100
    elif dir == "L":
        new_val = curr_val - int(val)
        crossings = (curr_val - 1) // 100 - (new_val - 1) // 100

    code += crossings
    curr_val = new_val % 100

print(code)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 4 ms
