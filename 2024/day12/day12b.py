import time


start_time = time.time()
with open("2024/day12/day_12_input.txt", "r") as file:
    raw_data = file.read().split()

data = [[item for item in row] for row in raw_data]

edge_row = []
for i in range(len(data[0]) + 2):
    edge_row.append(".")

for item in data:
    item.append(".")
    item.insert(0, ".")
data.append(edge_row)
data.insert(0, edge_row)


def find_plant_region(
    plant: str, farm_map: list[list[str]], i: int, j: int, visited: set
) -> set:
    visited.add(((i, j)))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        new_i = i + dx
        new_j = j + dy
        if (new_i, new_j) not in visited:
            if farm_map[new_i][new_j] == plant:
                visited.update(
                    find_plant_region(plant, farm_map, new_i, new_j, visited)
                )
    return visited


def find_edge_amount(all_plots: set) -> int:
    edges = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for x, y in all_plots:
        for i, (dx, dy) in enumerate(directions):
            if (x + dx, y + dy) not in all_plots:
                edge = set()
                edge.add((4000 + dx, 4000 + dy))
                edge.add((x, y))
                j = 1
                dir_1_ok = True
                dir_2_ok = True
                while True:
                    x_mod_l = 0
                    x_mod_r = 0
                    y_mod_l = 0
                    y_mod_r = 0
                    if directions[i - 1][0] == 0:
                        y_mod_l = directions[(i + 1) % 4][1] * j
                        y_mod_r = directions[(i - 1) % 4][1] * j
                    else:
                        x_mod_l = directions[(i + 1) % 4][0] * j
                        x_mod_r = directions[(i - 1) % 4][0] * j
                    if dir_1_ok:
                        if (
                            x + x_mod_l,
                            y + y_mod_l,
                        ) not in all_plots:
                            dir_1_ok = False
                        else:
                            if (
                                x + x_mod_l + dx,
                                y + y_mod_l + dy,
                            ) in all_plots:
                                dir_1_ok = False
                            else:
                                edge.add(
                                    (
                                        x + x_mod_l,
                                        y + y_mod_l,
                                    )
                                )
                    if dir_2_ok:
                        if (x + x_mod_r, y + y_mod_r) not in all_plots:
                            dir_2_ok = False
                        else:
                            if (
                                x + x_mod_r + dx,
                                y + y_mod_r + dy,
                            ) in all_plots:
                                dir_2_ok = False
                            else:
                                edge.add(
                                    (
                                        x + x_mod_r,
                                        y + y_mod_r,
                                    )
                                )
                    if not dir_1_ok and not dir_2_ok:
                        break
                    j += 1
                if edge not in edges:
                    edges.append(edge)
    return len(edges)


all_regions = []
found_plots = set()
for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char != ".":
            current_position = (i, j)
            if current_position not in found_plots:
                plots_in_region = find_plant_region(char, data, i, j, set())
                all_regions.append([char, plots_in_region])
                found_plots.update(plots_in_region)

cost = 0
for crop, plots in all_regions:
    cost += len(plots) * find_edge_amount(plots)

print(cost)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)

# 37 ms
