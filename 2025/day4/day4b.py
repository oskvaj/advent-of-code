import time


start_time = time.time()
with open("2025/day4/day_4_input.txt", "r") as file:
    raw_data = file.readlines()

data = [item.strip() for item in raw_data]
for index, item in enumerate(data):
    data[index] = "." + item + "."
buffer = ""
for char in range(len(data[0])):
    buffer += "."
data.insert(0, buffer)
data.append(buffer)


def check_paper_roll(row: int, column: int, map: list) -> int:
    nearby_stacks = 0
    for offset in range(-1, 2):
        if data[row - 1][column + offset] == "@":
            nearby_stacks += 1
        if offset % 2 == 1 and data[row][column + offset] == "@":
            nearby_stacks += 1
        if data[row + 1][column + offset] == "@":
            nearby_stacks += 1
    if nearby_stacks < 4:
        return 1
    else:
        return 0


paper_stacks = 0
change = 1
while change > 0:
    change = 0
    moved_rolls = []
    for row_index, row in enumerate(data[1 : len(data) - 1], start=1):
        for column_index, column in enumerate(row[1 : len(row) - 1], start=1):
            if data[row_index][column_index] == "@":
                temp = check_paper_roll(row_index, column_index, data)
                paper_stacks += temp
                change += temp
                if temp:
                    moved_rolls.append((row_index, column_index))
    for row, column in moved_rolls:
        data[row] = data[row][0:column] + "x" + data[row][column + 1 : len(data[row])]

print(paper_stacks)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 1sec and 563.16ms
