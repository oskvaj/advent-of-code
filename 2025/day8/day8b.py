import time
from queue import PriorityQueue


def dist(point1: tuple[int, int, int], point2: tuple[int, int, int]) -> int:
    return (
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2
        + (point1[2] - point2[2]) ** 2
    )


start_time = time.time()
with open("2025/day8/day_8_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [tuple(int(x) for x in row.split(",")) for row in raw_data]
q = PriorityQueue()
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        q.put((dist(data[i], data[j]), data[i], data[j]))

networks: dict[int, list[tuple[int, int, int]]] = {}
poles_to_networks: dict[tuple[int, int, int], int] = {}
network_identifiers: int = 1
while not q.empty():
    d, point1, point2 = q.get()
    if point1 not in poles_to_networks and point2 not in poles_to_networks:
        # none of them are in a network
        networks[network_identifiers] = [point1, point2]
        poles_to_networks[point1] = network_identifiers
        poles_to_networks[point2] = network_identifiers
        network_identifiers += 1
    elif point1 in poles_to_networks and point2 not in poles_to_networks:
        # point 1 in a network, but 2 isn't
        networks[poles_to_networks[point1]].append(point2)
        poles_to_networks[point2] = poles_to_networks[point1]
        if len(networks[poles_to_networks[point1]]) == len(data):
            print(point1[0] * point2[0])
            break
    elif point1 not in poles_to_networks and point2 in poles_to_networks:
        # point 1 not in a network, but 2 is
        networks[poles_to_networks[point2]].append(point1)
        poles_to_networks[point1] = poles_to_networks[point2]
        if len(networks[poles_to_networks[point1]]) == len(data):
            print(point1[0] * point2[0])
            break
    else:
        # both are in separate networks
        p1id = poles_to_networks[point1]
        p2id = poles_to_networks[point2]
        if p1id == p2id:
            continue
        affected_poles = networks[p2id]
        networks[p1id].extend(affected_poles)
        if len(networks[poles_to_networks[point1]]) == len(data):
            print(point1[0] * point2[0])
            break
        networks.pop(p2id)
        for pole in affected_poles:
            poles_to_networks[pole] = p1id

network_sizes = []
for value in networks.values():
    network_sizes.append(len(value))

network_sizes.sort(reverse=True)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 1sec and 852.37ms
