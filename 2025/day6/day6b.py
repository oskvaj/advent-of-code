import time
from math import prod


start_time = time.time()
with open("2025/day6/day_6_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [list(row) for row in raw_data]
raw_operands = data.pop(-1)
operands = [item.strip() for item in raw_operands if item.strip() != ""]
raw_columns = [list(col) for col in zip(*data)]
for i, row in enumerate(raw_columns):
    raw_columns[i] = "".join(raw_columns[i])

columns = []
inner_col = []
for num in raw_columns:
    stripped = num.strip()
    if stripped != "":
        inner_col.append(stripped)
    else:
        columns.append(inner_col)
        inner_col = []
if inner_col:
    columns.append(inner_col)

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
# Time took: 0sec and 4.34ms
