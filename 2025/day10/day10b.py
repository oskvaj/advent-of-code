import time
import numpy as np

start_time = time.perf_counter()
with open("2025/day10/day_10_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [tuple(x for x in item.split()) for item in raw_data]
goals = []
button_list_raw = []
joltages = []

for item in data:
    goals.append(len(item[0][1:-1]))
    button_list_raw.append(
        [list(map(int, button[1:-1].split(","))) for button in item[1:-1]]
    )
    joltages.append(list(map(int, item[-1][1:-1].split(","))))

button_vectors = []
for goal, button_list in zip(goals, button_list_raw):
    inner_vectors = []
    for button in button_list:
        this_vector = []
        for i in range(goal):
            if i in button:
                this_vector.append(1)
            else:
                this_vector.append(0)
        inner_vectors.append(this_vector)
    button_vectors.append(inner_vectors)


def find_min_coefficients(goal, vectors):
    A = np.array(vectors).T
    goal = np.array(goal)

    coeffs, *_ = np.linalg.lstsq(A, goal, rcond=None)

    return np.rint(coeffs).astype(int)


presses_total = 0
for j, bv in zip(joltages, button_vectors):
    presses_total += np.sum(find_min_coefficients(j, bv))

print(presses_total)

end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 7.89ms
