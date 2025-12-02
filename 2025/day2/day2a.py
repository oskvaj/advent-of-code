import time


start_time = time.time()
with open("2025/day2/day_2_input.txt", "r") as file:
    raw_data = file.read().split(",")

data = [[int(x) for x in item.split("-")] for item in raw_data]

id_sum = 0

for start, finish in data:
    for id in range(start, finish + 1):
        str_Id = str(id)
        if str_Id[0 : (len(str_Id) // 2)] == str_Id[(len(str_Id) // 2) : len(str_Id)]:
            id_sum += id

print(id_sum)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 1sec and 154.71ms
