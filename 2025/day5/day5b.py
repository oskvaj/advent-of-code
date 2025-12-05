import time


start_time = time.time()
with open("2025/day5/day_5_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [tuple(int(x) for x in row.split("-")) for row in raw_data if "-" in row]

change_occured = True
while change_occured:
    change_occured = False
    i = 0
    while i < len(data):
        merged = False
        j = i + 1
        while j < len(data):
            low1, high1 = data[i]
            low2, high2 = data[j]
            if not (high1 < low2 or high2 < low1):
                data[i] = (min(low1, low2), max(high1, high2))
                data.pop(j)
                change_occured = True
                merged = True
            else:
                j += 1
        if not merged:
            i += 1


sum = 0
for low, high in data:
    sum += high - (low - 1)
print(sum)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 5.91ms
