import time

start_time = time.perf_counter()
with open("2025/day9/day_9_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [tuple(int(item) for item in row.split(",")) for row in raw_data]

boundaries = {}

for i in range(len(data)):
    # Bygg gränse
    x1, y1 = data[i]
    x2, y2 = data[(i + 1) % len(data)]

    # vertical
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if y not in boundaries:
                boundaries[y] = [x1, x1]
            else:
                boundaries[y][0] = min(boundaries[y][0], x1)
                boundaries[y][1] = max(boundaries[y][1], x1)
    # horizontal
    else:
        if y1 not in boundaries:
            boundaries[y1] = [min(x1, x2), max(x1, x2)]
        else:
            boundaries[y1][0] = min(boundaries[y1][0], x1, x2)
            boundaries[y1][1] = max(boundaries[y1][1], x1, x2)


def is_valid(
    p1: tuple[int, int], p2: tuple[int, int], boundaries: dict[int, tuple[int, int]]
) -> bool:
    max_x = max(p1[0], p2[0])
    min_x = min(p1[0], p2[0])
    max_y = max(p1[1], p2[1])
    min_y = min(p1[1], p2[1])

    for y in range(min_y, max_y + 1):
        if y not in boundaries:
            return False
        bound_min_x, bound_max_x = boundaries[y]
        if min_x < bound_min_x or max_x > bound_max_x:
            return False

    return True


larges_rect = -1
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        dx = abs(data[i][0] - data[j][0]) + 1
        dy = abs(data[i][1] - data[j][1]) + 1
        area = dx * dy
        if area > larges_rect and is_valid(data[i], data[j], boundaries):
            larges_rect = area

print(larges_rect)

end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 50sec and 996.44ms
