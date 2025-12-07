import time


start_time = time.time()
with open("2025/day7/day_7_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

grid = [list(row) for row in raw_data]
beam_positions = []
for index, item in enumerate(grid[0]):
    if item == "S":
        beam_positions.append(index)

splits = 0
for row in grid[1 : len(grid) - 1]:
    new_positions = set()
    for beam in beam_positions:
        if row[beam] == "^":
            splits += 1
            new_positions.add(beam - 1)
            new_positions.add(beam + 1)
        else:
            new_positions.add(beam)
    beam_positions = new_positions

print(splits)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 14.54ms
