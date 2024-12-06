def BackslashRegular(data, i, j):
    if data[i - 1][j - 1] == "M" and data[i + 1][j + 1] == "S":
        return True
    return False


def BackslashReverse(data, i, j):
    if data[i - 1][j - 1] == "S" and data[i + 1][j + 1] == "M":
        return True
    return False


def SlashRegular(data, i, j):
    if data[i - 1][j + 1] == "M" and data[i + 1][j - 1] == "S":
        return True
    return False


def SlashReverse(data, i, j):
    if data[i - 1][j + 1] == "S" and data[i + 1][j - 1] == "M":
        return True
    return False


with open("2024/day4/day_4_input.txt", "r") as file:
    rawdata = file.readlines()

data = []
for item in rawdata:
    temp = []
    for char in item:
        if char != "\n":
            temp.append(char)
    data.append(temp)

# hitta möster i en karta number two electric bogalo :^ ) the classic from last year returns

sum = 0
for i, row in enumerate(data):
    xAxisUppOk = i >= 1
    xAxisDownOk = i <= len(row) - 2
    for j, _ in enumerate(row):
        notCheckedYet = True
        yAxisLeftOk = j >= 1
        yAxisRightOk = j <= len(row) - 2
        if data[i][j] == "A":
            if xAxisUppOk and xAxisDownOk and yAxisLeftOk and yAxisRightOk:
                backSlash = BackslashRegular(data, i, j) or BackslashReverse(data, i, j)
                slash = SlashRegular(data, i, j) or SlashReverse(data, i, j)
                if backSlash and slash:
                    sum += 1
print(sum)
