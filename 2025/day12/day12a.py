import time


start_time = time.perf_counter()
with open("2025/day12/day_12_input.txt", "r") as file:
    raw_data = file.read().strip().split("\n\n")

data = [item for item in raw_data]
present_sizes = []
for i in range(6):
    lines = data[i].split("\n")[1:]
    size = sum(line.count("#") for line in lines)
    present_sizes.append(size)
trees = []
for tree in data[6].split("\n"):
    grid, present_counts = tree.split(":")
    width, height = grid.split("x")
    counts = [int(p) for p in present_counts.split()]
    trees.append((int(width), int(height), counts))

ok_trees = 0
for width, height, counts in trees:
    if (
        sum(count * size for count, size in zip(counts, present_sizes))
        <= width * height
    ):
        ok_trees += 1

print(ok_trees)

end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 3.42ms
