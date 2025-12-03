import time


start_time = time.time()
with open("2025/day3/day_3_input.txt", "r") as file:
    raw_data = file.readlines()

data = [item.strip() for item in raw_data]

sum = 0
for item in data:
    max_numbers = []
    for _ in range(12):
        max_numbers.append((-1, 0))
    for index, number in enumerate(item[: len(item) - 11 :]):
        if int(number) > max_numbers[0][0]:
            max_numbers[0] = (int(number), index)
    for i in range(1, 12):
        for index, number in enumerate(
            item[max_numbers[i - 1][1] + 1 : len(item) - (11 - i) :],
            start=max_numbers[i - 1][1] + 1,
        ):
            if int(number) > max_numbers[i][0]:
                max_numbers[i] = (int(number), index)
    row_max = 0
    for index, number in enumerate(max_numbers):
        row_max += number[0] * (10 ** (11 - index))
    sum += row_max

print(sum)
end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 37.96ms
