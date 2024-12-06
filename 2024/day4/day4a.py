def Left(data, i, j):
    if data[i][j - 1] == "M" and data[i][j - 2] == "A" and data[i][j - 3] == "S":
        return True
    return False


def UpLeft(data, i, j):
    if (
        data[i - 1][j - 1] == "M"
        and data[i - 2][j - 2] == "A"
        and data[i - 3][j - 3] == "S"
    ):
        return True
    return False


def Up(data, i, j):
    if data[i - 1][j] == "M" and data[i - 2][j] == "A" and data[i - 3][j] == "S":
        return True
    return False


def UpRight(data, i, j):
    if (
        data[i - 1][j + 1] == "M"
        and data[i - 2][j + 2] == "A"
        and data[i - 3][j + 3] == "S"
    ):
        return True
    return False


def Right(data, i, j):
    if data[i][j + 1] == "M" and data[i][j + 2] == "A" and data[i][j + 3] == "S":
        return True
    return False


def DownRight(data, i, j):
    if (
        data[i + 1][j + 1] == "M"
        and data[i + 2][j + 2] == "A"
        and data[i + 3][j + 3] == "S"
    ):
        return True
    return False


def Down(data, i, j):
    if data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
        return True
    return False


def DownLeft(data, i, j):
    if (
        data[i + 1][j - 1] == "M"
        and data[i + 2][j - 2] == "A"
        and data[i + 3][j - 3] == "S"
    ):
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
    xAxisUppOk = i >= 3
    xAxisDownOk = i <= len(row) - 4
    for j, _ in enumerate(row):
        notCheckedYet = True
        yAxisLeftOk = j >= 3
        yAxisRightOk = j <= len(row) - 4
        if data[i][j] == "X":
            # parameters; 1: xAxisUppOk, 2: xAxisDownOk, 3: yAxisLeftOk, 4: yAxisRightOk, notCheckedYet first if required
            # Center: T T T T, check: up, up-right, right, down-right, down, down-left, left, up-left
            if xAxisUppOk and xAxisDownOk and yAxisLeftOk and yAxisRightOk:
                if Up(data, i, j):
                    sum += 1
                if UpRight(data, i, j):
                    sum += 1
                if Right(data, i, j):
                    sum += 1
                if DownRight(data, i, j):
                    sum += 1
                if Down(data, i, j):
                    sum += 1
                if DownLeft(data, i, j):
                    sum += 1
                if Left(data, i, j):
                    sum += 1
                if UpLeft(data, i, j):
                    sum += 1
                notCheckedYet = False
            # Case Top Edge: F T T T, check: right, down-right, down, down-left, left
            if (
                notCheckedYet
                and not xAxisUppOk
                and xAxisDownOk
                and yAxisLeftOk
                and yAxisRightOk
            ):
                if Right(data, i, j):
                    sum += 1
                if DownRight(data, i, j):
                    sum += 1
                if Down(data, i, j):
                    sum += 1
                if DownLeft(data, i, j):
                    sum += 1
                if Left(data, i, j):
                    sum += 1
                notCheckedYet = False
            # Case Bottom edge: T F T T, check: right, up-right, up, up-left, left
            if (
                notCheckedYet
                and xAxisUppOk
                and not xAxisDownOk
                and yAxisLeftOk
                and yAxisRightOk
            ):
                if Right(data, i, j):
                    sum += 1
                if UpRight(data, i, j):
                    sum += 1
                if Up(data, i, j):
                    sum += 1
                if UpLeft(data, i, j):
                    sum += 1
                if Left(data, i, j):
                    sum += 1
                notCheckedYet = False
            # Case left edge: T T F T, check: up, up-right, right, down-right, down
            if (
                notCheckedYet
                and xAxisUppOk
                and xAxisDownOk
                and not yAxisLeftOk
                and yAxisRightOk
            ):
                if Up(data, i, j):
                    sum += 1
                if UpRight(data, i, j):
                    sum += 1
                if Right(data, i, j):
                    sum += 1
                if DownRight(data, i, j):
                    sum += 1
                if Down(data, i, j):
                    sum += 1
                notCheckedYet = False
            # Case Right Edge: T T T F, check: up, up-left, left, down-left, down
            if (
                notCheckedYet
                and xAxisUppOk
                and xAxisDownOk
                and yAxisLeftOk
                and not yAxisRightOk
            ):
                if Up(data, i, j):
                    sum += 1
                if UpLeft(data, i, j):
                    sum += 1
                if Left(data, i, j):
                    sum += 1
                if DownLeft(data, i, j):
                    sum += 1
                if Down(data, i, j):
                    sum += 1
            # Case Top Left Corner: F T F T, check: right, down-right, down
            if (
                notCheckedYet
                and not xAxisUppOk
                and xAxisDownOk
                and not yAxisLeftOk
                and yAxisRightOk
            ):
                if Right(data, i, j):
                    sum += 1
                if DownRight(data, i, j):
                    sum += 1
                if Down(data, i, j):
                    sum += 1
                notCheckedYet = False
            # Case Top Right Corner: F T T F, check: left, down-left, down
            if (
                notCheckedYet
                and not xAxisUppOk
                and xAxisDownOk
                and yAxisLeftOk
                and not yAxisRightOk
            ):
                if Left(data, i, j):
                    sum += 1
                if DownLeft(data, i, j):
                    sum += 1
                if Down(data, i, j):
                    sum += 1
                notCheckedYet = False
            # Case Bottom Left Corner: T F F T, check: up, up-right, right
            if (
                notCheckedYet
                and xAxisUppOk
                and not xAxisDownOk
                and not yAxisLeftOk
                and yAxisRightOk
            ):
                if Up(data, i, j):
                    sum += 1
                if UpRight(data, i, j):
                    sum += 1
                if Right(data, i, j):
                    sum += 1
                notCheckedYet = False
            # Case Bottom Right Corner: T F T F, check: up, up-left, left
            if (
                notCheckedYet
                and xAxisUppOk
                and not xAxisDownOk
                and yAxisLeftOk
                and not yAxisRightOk
            ):
                if Up(data, i, j):
                    sum += 1
                if UpLeft(data, i, j):
                    sum += 1
                if Left(data, i, j):
                    sum += 1
                notCheckedYet = False


print(sum)
