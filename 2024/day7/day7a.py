import time

start_time = time.perf_counter()
with open("2024/day7/day_7_input.txt", "r") as file:
    dataRaw = file.readlines()

data = [item.strip().split(":") for item in dataRaw]
for item in data:
    item[1] = item[1].split()
    item[1] = [int(x) for x in item[1]]
    item[0] = int(item[0])


def AllVariations(
    numberVariations: list[int],
    allowedOperators: list[str],
    currentNumber: int,
    howFarBack: int,
) -> list[int]:
    copyOfnumberVariations = numberVariations.copy()
    if len(numberVariations) == 0:
        numberVariations.append(currentNumber)
    elif len(numberVariations) == 1:
        for item in allowedOperators:
            if item == "+":
                numberVariations.append(
                    copyOfnumberVariations[len(copyOfnumberVariations) - 1]
                    + currentNumber
                )
            elif item == "*":
                numberVariations.append(
                    copyOfnumberVariations[len(copyOfnumberVariations) - 1]
                    * currentNumber
                )
    else:
        for item in allowedOperators:
            if item == "+":
                for i in range(howFarBack):
                    numberVariations.append(
                        copyOfnumberVariations[len(copyOfnumberVariations) - 1 - i]
                        + currentNumber
                    )
            elif item == "*":
                for i in range(howFarBack):
                    numberVariations.append(
                        copyOfnumberVariations[len(copyOfnumberVariations) - 1 - i]
                        * currentNumber
                    )
    return numberVariations


allowedOperators = ["+", "*"]

sum = 0
for answer, nums in data:
    numberVariations = []
    for i, num in enumerate(nums):
        AllVariations(numberVariations, allowedOperators, num, 2 ** (i - 1))
    if answer in numberVariations[-(2 ** (len(nums) - 1)) :]:
        sum += answer

print(sum)
end_time = time.perf_counter()
print(
    f"Time took: {round(end_time - start_time)}sec and {round((round((end_time - start_time) * 1000, 2))%1000.0, 2)}ms"
)
# 82.43 ms
