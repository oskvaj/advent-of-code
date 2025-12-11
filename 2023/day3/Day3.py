import re

with open(
    "C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/python/Day3Input.txt", "r"
) as file:
    originalData = file.read().split("\n")

sum = 0
counter = 0

for dataRow in originalData:
    counter2 = 0
    amountOfGoodNumbersInThisRow = 0
    shouldBeSummized = False
    for item in dataRow:
        if dataRow[counter2].isdigit():
            acceptableInput = [True, True, True, True]
            if counter - 1 < 0:
                acceptableInput[0] = False
            if counter + 1 >= len(originalData):
                acceptableInput[1] = False
            if counter2 - 1 < 0:
                acceptableInput[2] = False
            if counter2 + 1 >= len(dataRow):
                acceptableInput[3] = False
            # Handles corners
            if not acceptableInput[0] and not acceptableInput[2]:
                pass
            elif not acceptableInput[1] and not acceptableInput[2]:
                pass
            elif not acceptableInput[0] and not acceptableInput[3]:
                if (
                    originalData[counter + 1][counter2] != "."
                    or originalData[counter + 1][counter2 - 1] != "."
                ):
                    shouldBeSummized = True
            elif not acceptableInput[1] and not acceptableInput[3]:
                if (
                    originalData[counter - 1][counter2] != "."
                    or originalData[counter - 1][counter2] != "."
                ):
                    shouldBeSummized = True
            # handles edges
            elif not acceptableInput[0]:
                if (
                    originalData[counter][counter2 - 1].isdigit()
                    and not originalData[counter][counter2 + 1].isdigit()
                ):
                    if (
                        originalData[counter][counter2 + 1] != "."
                        or originalData[counter + 1][counter2 - 1] != "."
                        or originalData[counter + 1][counter2] != "."
                        or originalData[counter + 1][counter2 + 1] != "."
                    ):
                        shouldBeSummized = True
                elif (
                    originalData[counter][counter2 + 1].isdigit()
                    and not originalData[counter][counter2 - 1].isdigit()
                ):
                    if (
                        originalData[counter][counter2 - 1] != "."
                        or originalData[counter + 1][counter2 - 1] != "."
                        or originalData[counter + 1][counter2] != "."
                        or originalData[counter + 1][counter2 + 1] != "."
                    ):
                        shouldBeSummized = True
                elif (
                    not originalData[counter][counter2 + 1] != "."
                    or not originalData[counter][counter - 1] != "."
                ):
                    if (
                        originalData[counter + 1][counter2 - 1] != "."
                        or originalData[counter + 1][counter2] != "."
                        or originalData[counter + 1][counter2 + 1] != "."
                        or originalData[counter][counter + 1] != "."
                        or originalData[counter][counter - 1] != "."
                    ):
                        shouldBeSummized = True
            elif not acceptableInput[1]:
                if (
                    originalData[counter][counter2 - 1].isdigit()
                    and not originalData[counter][counter2 + 1].isdigit()
                ):
                    if (
                        originalData[counter][counter2 - 1] != "."
                        or originalData[counter - 1][counter2 - 1] != "."
                        or originalData[counter - 1][counter2] != "."
                        or originalData[counter - 1][counter2 + 1] != "."
                    ):
                        shouldBeSummized = True
                elif (
                    originalData[counter][counter2 + 1].isdigit()
                    and not originalData[counter][counter2 - 1].isdigit()
                ):
                    if (
                        originalData[counter][counter2 - 1] != "."
                        or originalData[counter - 1][counter2 - 1] != "."
                        or originalData[counter - 1][counter2] != "."
                        or originalData[counter - 1][counter2 + 1] != "."
                    ):
                        shouldBeSummized = True
                elif (
                    not originalData[counter][counter2 - 1].isdigit()
                    and not originalData[counter][counter2 + 1].isdigit()
                ):
                    if (
                        originalData[counter - 1][counter2 - 1] != "."
                        or originalData[counter - 1][counter2] != "."
                        or originalData[counter - 1][counter2 + 1] != "."
                        or originalData[counter][counter + 1] != "."
                        or originalData[counter][counter - 1] != "."
                    ):
                        shouldBeSummized = True
            elif not acceptableInput[2]:
                if originalData[counter][counter2 + 1].isdigit():
                    pass
                else:
                    if (
                        originalData[counter - 1][counter2] != "."
                        or originalData[counter - 1][counter2 + 1] != "."
                        or originalData[counter + 1][counter2] != "."
                        or originalData[counter + 1][counter2 + 1] != "."
                    ):
                        shouldBeSummized = True
            elif not acceptableInput[3]:
                if originalData[counter][counter2 - 1].isdigit():
                    pass
                else:
                    if (
                        originalData[counter - 1][counter2] != "."
                        or originalData[counter - 1][counter2 - 1] != "."
                        or originalData[counter + 1][counter2] != "."
                        or originalData[counter + 1][counter2 - 1] != "."
                    ):
                        shouldBeSummized = True
            # handles middle of board
            elif (
                not originalData[counter][counter2 - 1].isdigit()
                and not originalData[counter][counter2 + 1].isdigit()
            ):
                if (
                    originalData[counter][counter2 + 1] != "."
                    or originalData[counter][counter2 - 1] != "."
                    or originalData[counter + 1][counter2 - 1] != "."
                    or originalData[counter + 1][counter2] != "."
                    or originalData[counter + 1][counter2 + 1] != "."
                    or originalData[counter - 1][counter2 - 1] != "."
                    or originalData[counter - 1][counter2] != "."
                    or originalData[counter - 1][counter2 + 1] != "."
                ):
                    shouldBeSummized = True
            else:
                if (
                    originalData[counter][counter2 + 1].isdigit()
                    and originalData[counter][counter2 - 1].isdigit()
                ):
                    pass
                elif (
                    originalData[counter][counter2 + 1].isdigit()
                    and not originalData[counter][counter2 - 1].isdigit()
                ):
                    if (
                        originalData[counter][counter2 - 1] != "."
                        or originalData[counter + 1][counter2 - 1] != "."
                        or originalData[counter + 1][counter2] != "."
                        or originalData[counter + 1][counter2 + 1] != "."
                        or originalData[counter - 1][counter2 - 1] != "."
                        or originalData[counter - 1][counter2] != "."
                        or originalData[counter - 1][counter2 + 1] != "."
                    ):
                        shouldBeSummized = True
                elif (
                    not originalData[counter][counter2 + 1].isdigit()
                    and originalData[counter][counter2 - 1].isdigit()
                ):
                    if (
                        originalData[counter][counter2 + 1] != "."
                        or originalData[counter + 1][counter2 - 1] != "."
                        or originalData[counter + 1][counter2] != "."
                        or originalData[counter + 1][counter2 + 1] != "."
                        or originalData[counter - 1][counter2 - 1] != "."
                        or originalData[counter - 1][counter2] != "."
                        or originalData[counter - 1][counter2 + 1] != "."
                    ):
                        shouldBeSummized = True
            # Summarization
            shouldKeepInMind = False
            if shouldBeSummized:
                if acceptableInput[3] and originalData[counter][counter2 + 1].isdigit():
                    shouldKeepInMind = True
                if shouldKeepInMind is False:
                    number = re.findall(r"\d+", dataRow)
                    sum += int(number[amountOfGoodNumbersInThisRow])
            if shouldKeepInMind is False:
                shouldBeSummized = False

            if acceptableInput[3] and not originalData[counter][counter2 + 1].isdigit():
                amountOfGoodNumbersInThisRow += 1
        counter2 += 1
    amountOfGoodNumbersInThisRow = 0
    counter += 1
print(sum)
