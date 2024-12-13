import time
import re
import numpy as np


start_time = time.time()
with open("2024/day13/day_13_input.txt", "r") as file:
    raw_data = file.readlines()

data = [item.strip() for item in raw_data if item != "\n"]
button_list = []

for i in range(len(data) + 1):
    if i != 0 and i % 3 == 0:
        machine = []
        for j in range(i - 3, i):
            current_item = list(
                map(
                    lambda inputs: (int(inputs[0]), int(inputs[1])),
                    re.findall(r"X[^a-z]{1}(\d+), Y[^a-z]{1}(\d+)", data[j]),
                )
            )
            if i == j + 1:
                machine.append(
                    (
                        current_item[0][0] + 10000000000000,
                        current_item[0][1] + 10000000000000,
                    )
                )
            else:
                machine.append(current_item[0])
        button_list.append(machine)


def find_combinations(
    button_a: tuple[int, int], button_b: tuple[int, int], destination: tuple[int, int]
) -> int:
    matrix1 = np.linalg.inv(np.array([[button_a[0], button_b[0]], [button_a[1], button_b[1]]]))
    matrix2 = np.array([[destination[0]], [destination[1]]])
    result = np.matmul(matrix1, matrix2)

    for item in result:
        if abs(item[0] - round(item[0])) > 0.001:
            return -1

    return round(result[0][0]) * 3 + round(result[1][0])


total_tokes = 0
prizes_won = 0
for button_a, button_b, destination in button_list:
    found_cost = find_combinations(button_a, button_b, destination)
    if found_cost != -1:
        prizes_won += 1
        total_tokes += found_cost


print(prizes_won, ",", total_tokes)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)

# 4.5 ms
