import time


start_time = time.time()
with open('2024/day9/day_9_input.txt', 'r') as file:
    raw_data = file.read()

data = [int(item) for item in raw_data]

is_file = True
decompacted_data = []
tracker = 0
total_full_stops = 0
for char in data:
    if is_file:
        for j in range(char):
            decompacted_data.append(tracker)
        tracker += 1
    else:
        for j in range(char):
            decompacted_data.append(".")
            total_full_stops+=1
    is_file = not is_file

end_of_decompacted_data = len(decompacted_data)-1
for i in range(len(decompacted_data) - total_full_stops):
    if(decompacted_data[i] == "."):
        for j, char in enumerate(decompacted_data[::-1]):
            if char != ".":
                temp = decompacted_data[end_of_decompacted_data-j]
                decompacted_data[end_of_decompacted_data-j] = decompacted_data[i]
                decompacted_data[i] = temp
                break
    print(f'{round((i*100/(len(decompacted_data) - total_full_stops)),2)}% done')

filesystem_checksum = 0

for i, item in enumerate(decompacted_data):
    if item != ".":
        filesystem_checksum += i*item

print(filesystem_checksum)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

#60.124 sek