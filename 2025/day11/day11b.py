import time
from functools import lru_cache

start_time = time.perf_counter()
with open("2025/day11/day_11_input.txt", "r") as file:
    raw_data = file.read().strip().splitlines()

data = [list(x for x in item.split(":")) for item in raw_data]
connections = [list(x for x in item[1].split()) for item in data]
servers = [item[0] for item in data]
server_to_connections: dict[str, list[str]] = {}
for s, cs in zip(servers, connections):
    server_to_connections[s] = cs


@lru_cache(maxsize=None)
def count_paths(start: str, dac: bool, fft: bool) -> int:
    paths = 0
    for connection in server_to_connections[start]:
        if connection == "out":
            if dac and fft:
                paths += 1
        else:
            if connection == "dac":
                dac = True
            elif connection == "fft":
                fft = True
            paths += count_paths(connection, dac, fft)
    return paths


total_paths = 0
for start in server_to_connections["svr"]:
    total_paths += count_paths(start, False, False)

print(total_paths)

end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# Time took: 0sec and 2.04ms
