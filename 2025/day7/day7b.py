import time


start_time = time.time()
with open("2025/day7/day_7_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

grid = [list(row) for row in raw_data]
beam_start_position = -1
for index, item in enumerate(grid[0]):
    if item == "S":
        beam_start_position = index


def splitter(
    row_index: int,
    pos: int,
    grid: list[list[str]],
    dynamic_time: dict[tuple[int, int], int],
) -> int:
    if row_index == len(grid):
        return 1

    if grid[row_index][pos] == "^":
        if (row_index, pos) in dynamic_time:
            return dynamic_time.get((row_index, pos))
        else:
            temp = splitter(row_index + 1, pos - 1, grid, dynamic_time) + splitter(
                row_index + 1, pos + 1, grid, dynamic_time
            )
            dynamic_time[(row_index, pos)] = temp
            return temp
    else:
        if (row_index, pos) in dynamic_time:
            return dynamic_time[(row_index, pos)]
        else:
            temp = splitter(row_index + 1, pos, grid, dynamic_time)
            dynamic_time[(row_index, pos)] = temp
            return temp


dynamic_time: dict[tuple[int, int], int] = {}
print(splitter(1, beam_start_position, grid, dynamic_time))

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 4.09ms
