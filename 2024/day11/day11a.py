import time
from multiprocessing.dummy import Pool as ThreadPool


start_time = time.time()
with open("2024/day11/day_11_input.txt", "r") as file:
    raw_data = file.read().split()

data = [int(item) for item in raw_data]


def how_many_numbers_from_this_number(current_number: int) -> int:
    data = [current_number]
    for _ in range(25):
        copy_of_data = data.copy()
        splits_during_this_blink = 0
        for i, item in enumerate(copy_of_data):
            if item == 0:
                data.pop(i + splits_during_this_blink)
                data.insert(i + splits_during_this_blink, 1)
            elif len(str(item)) % 2 == 0:
                data.pop(i + splits_during_this_blink)
                data.insert(
                    i + splits_during_this_blink,
                    int((item % (10 ** (len(str(item)) / 2)))),
                )
                data.insert(
                    i + splits_during_this_blink,
                    int((item / (10 ** (len(str(item)) / 2)))),
                )
                splits_during_this_blink += 1
            else:
                data[i + splits_during_this_blink] = (
                    data[i + splits_during_this_blink] * 2024
                )
    return len(data)


pool = ThreadPool(6)

total_numbers = pool.map(how_many_numbers_from_this_number, data)

print(sum(total_numbers))

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)

# 1 sec 467ms
