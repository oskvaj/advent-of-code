import re

def replaceTextWithNumbers(text):
    text = text.replace("one", "on1e")
    text = text.replace("two", "tw2o")
    text = text.replace("three", "thr3ee")
    text = text.replace("four", "fo4ur")
    text = text.replace("five", "fi5ve")
    text = text.replace("six", "si6x")
    text = text.replace("seven", "sev7en")
    text = text.replace("eight", "ei8ght")
    text =  text.replace("nine", "ni9ne")
    return text

with open('C:/Users/oskar/OneDrive/Documents/Prog/AdventOfCode2023/Day1Input.txt', 'r') as file:
    data = file.readlines()
    newdata = []
    for item in data:
        item = replaceTextWithNumbers(item)
        item = (re.sub(r'[^0-9]', '', item))
        print(item)
        if(len(item) == 1):
            newdata.append(int(item)*10 + int(item))
        else:
            lastItem = int(item)%10
            temp = int(str(item)[0])*10 + lastItem
            newdata.append(temp)

sum = 0
for item in newdata:
    print(item)
    sum += item

print(sum)

