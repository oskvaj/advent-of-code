import time
import re


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
            machine.append(current_item[0])
        button_list.append(machine)


def find_combinations(
    button_a: tuple[int, int], button_b: tuple[int, int], destination: tuple[int, int]
) -> int:
    possible_combinations = []
    for i in range(101):
        current_x = button_a[0] * i
        current_y = button_a[1] * i
        for j in range(101):
            inner_x = current_x + button_b[0] * j
            inner_y = current_y + button_b[1] * j
            if (inner_x, inner_y) == destination:
                possible_combinations.append(i * 3 + j)
                break
            if (inner_x > destination[0]) or (inner_y > destination[1]):
                break
        if (current_x > destination[0]) or (current_y > destination[1]):
            break
    if len(possible_combinations) == 0:
        return -1
    else:
        return min(possible_combinations)


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

# 175 ms
