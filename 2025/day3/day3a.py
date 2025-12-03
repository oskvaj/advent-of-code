import time


start_time = time.time()
with open("2025/day3/day_3_input.txt", "r") as file:
    raw_data = file.readlines()

data = [item.strip() for item in raw_data]

sum = 0
for item in data:
    max_start = (-1,)
    for index, number in enumerate(item[: len(item) - 1 :]):
        if int(number) > max_start[0]:
            max_start = (int(number), index)
    max_second = -1
    for number in item[max_start[1] + 1 : :]:
        if int(number) > max_second:
            max_second = int(number)
    sum += max_start[0] * 10 + max_second

print(sum)
end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 7.66ms
