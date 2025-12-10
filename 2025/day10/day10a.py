import time

start_time = time.perf_counter()
with open("2025/day10/day_10_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [tuple(x for x in item.split()) for item in raw_data]
goals = [[0 if char == "." else 1 for char in item[0][1:-1]] for item in data]
button_list = [
    [list(map(int, button[1:-1].split(","))) for button in item[1:-1]] for item in data
]


def find_shortest_combo(
    start: list[int], buttons: list[list[int]], depth: int
) -> list[list[int]]:
    if depth > 1:
        returned_results = find_shortest_combo(start, buttons, depth - 1)
        results = []
        for result in returned_results:
            for button in buttons:
                temp = result.copy()
                for digit in button:
                    temp[digit] = (temp[digit] + 1) % 2
                results.append(temp)
        return results
    else:
        results = []
        for button in buttons:
            temp = start.copy()
            for digit in button:
                temp[digit] = (temp[digit] + 1) % 2
            results.append(temp)
        return results


smallest_combination_sum = 0
for goal, buttons in zip(goals, button_list):
    i = 1
    while True:
        results = find_shortest_combo([0 for _ in goal], buttons, i)
        if goal in results:
            smallest_combination_sum += i
            break
        else:
            i += 1


print(smallest_combination_sum)

end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 20sec and 231.85ms
