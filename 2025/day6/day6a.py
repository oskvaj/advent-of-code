import time
from math import prod


start_time = time.time()
with open("2025/day6/day_6_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [item.split() for item in raw_data]
operands = data.pop(-1)
columns = [list(col) for col in zip(*data)]

answer = 0
for op, column in zip(operands, columns):
    problem_sum = 0
    if op == "+":
        problem_sum = sum(int(x) for x in column)
    elif op == "*":
        problem_sum = prod(int(x) for x in column)
    answer += problem_sum

print(answer)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 1.92ms
