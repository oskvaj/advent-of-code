import time
import functools


start_time = time.time()
with open("2024/day11/day_11_input.txt", "r") as file:
    raw_data = file.read().split()

data = [int(item) for item in raw_data]


@functools.lru_cache(maxsize=None)
def blinking(current_number: int, times_blinked: int) -> int:
    len_of_current_number = len(str(current_number))
    if times_blinked == 75:
        return 1
    else:
        if current_number == 0:
            return blinking(1, times_blinked + 1)
        elif len_of_current_number % 2 == 0:
            return blinking(
                int(current_number % (10 ** (len_of_current_number / 2))),
                times_blinked + 1,
            ) + blinking(
                int(current_number / (10 ** (len_of_current_number / 2))),
                times_blinked + 1,
            )
        else:
            return blinking(current_number * 2024, times_blinked + 1)


total_stones = 0
for item in data:
    total_stones += blinking(item, 0)

print(total_stones)

end_time = time.time()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)

# 133ms
# hade tagit 56 år och 6 månader med lösning från part a med 75 istället för 25