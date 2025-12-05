import time


start_time = time.time()
with open("2025/day5/day_5_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [tuple(int(x) for x in row.split("-")) for row in raw_data if "-" in row]
ingredients = [int(item) for item in raw_data if "-" not in item and item != ""]

sum = 0
for ingredient in ingredients:
    for low, high in data:
        if ingredient <= high and ingredient >= low:
            sum += 1
            break

print(sum)
end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 15.99ms
