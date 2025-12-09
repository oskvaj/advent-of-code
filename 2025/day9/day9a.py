import time


start_time = time.perf_counter()
with open("2025/day9/day_9_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [tuple(int(item) for item in row.split(",")) for row in raw_data]

larges_rect = -1
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        dx = abs(data[i][0] - data[j][0]) + 1
        dy = abs(data[i][1] - data[j][1]) + 1
        if dx * dy > larges_rect:
            larges_rect = dx * dy

print(larges_rect)

end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 55.72ms
