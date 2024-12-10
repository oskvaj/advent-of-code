import time
from multiset import *


start_time = time.time()
with open('2024/day10/day_10_input.txt', 'r') as file:
    raw_data = file.read().split()

data = [[int(item) for item in row] for row in raw_data]
edge_row = []
for i in range(len(data[0])+2):
    edge_row.append(".")
for item in data:
    item.append(".")
    item.insert(0, ".")
data.append(edge_row)
data.insert(0, edge_row)

def find_number_of_paths(data: list, i: int, j: int, current_number: int) -> Multiset:
    positions_reachable = Multiset()

    if(current_number == 8):
        if data[i][j+1] == 9:
            positions_reachable.add(str(i) + "," + str(j+1))
        if data[i][j-1] == 9:
            positions_reachable.add(str(i) + "," + str(j-1))
        if data[i-1][j] == 9:
            positions_reachable.add(str(i-1) + "," + str(j))
        if data[i+1][j] == 9:
            positions_reachable.add(str(i+1) + "," + str(j))
    else:
        if data[i+1][j] == current_number+1:
            positions_reachable.update(find_number_of_paths(data,i+1,j,current_number+1))
        if data[i-1][j] == current_number+1:
            positions_reachable.update(find_number_of_paths(data,i-1,j,current_number+1))
        if data[i][j+1] == current_number+1:
            positions_reachable.update(find_number_of_paths(data,i,j+1,current_number+1))
        if data[i][j-1] == current_number+1:
            positions_reachable.update(find_number_of_paths(data,i,j-1,current_number+1))

    return(positions_reachable)

total_paths = 0
for i, row in enumerate(data):
    for j, number in enumerate(row):
        if number == 0:
            total_paths += len(find_number_of_paths(data,i,j,0))

print(total_paths)

end_time = time.time()
print(f'Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms')

#9 ms