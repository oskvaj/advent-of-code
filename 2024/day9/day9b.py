import time


start_time = time.time()
with open('2024/day9/day_9_input.txt', 'r') as file:
    raw_data = file.read()

data = [int(item) for item in raw_data]

is_file = True
decompacted_data = []
tracker = 0
total_full_stops_items = 0
for char in data:
    data_row = []
    if is_file:
        data_row.append(tracker)
        data_row.append(char)
        tracker += 1
    else:
        data_row.append(".")
        data_row.append(char)
        total_full_stops_items += 1
    is_file = not is_file
    if char != 0:
        decompacted_data.append(data_row)

reset_loop = False
i = 0
currentLen = len(decompacted_data)-1
while i <= currentLen:
    if(reset_loop):
        i = 0
        reset_loop = False
    if decompacted_data[currentLen-i][0] != ".":
        for j, inner_item in enumerate(decompacted_data):
            if (currentLen-i) == j:
                break
            elif inner_item[0] == "." and decompacted_data[currentLen-i][1] <= inner_item[1]:
                temp_item = decompacted_data.pop(-1-i)
                temp_dots = decompacted_data.pop(j)
                decompacted_data.insert(currentLen-1-i,[".", temp_item[1]])
                decompacted_data.insert(j, [".", (temp_dots[1]-temp_item[1])])
                decompacted_data.insert(j,temp_item)
                reset_loop = True
                currentLen = len(decompacted_data)-1
                break
    i+=1

reconstructed_data = []
for item, amount in decompacted_data:
    for i in range(amount):
        reconstructed_data.append(item)

filesystem_checksum = 0

for i, item in enumerate(reconstructed_data):
    if item != ".":
        filesystem_checksum += i*item

print(filesystem_checksum)

end_time = time.time()
print(f'Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms')

#232.869 sek