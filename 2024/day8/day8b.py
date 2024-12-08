import time
start = time.time()

with open('2024/day8/day_8_input.txt', 'r') as file:
	dataRaw = file.read().split("\n")

data=[[item.split() for item in row] for row in dataRaw]
possibleAntena = set()

for row in data:
	for item in row:
		if item != ['.']:
			possibleAntena.update(item)


antenaLocations = []
for char in possibleAntena:
	dataRow = [char]
	locations = []
	yLength = len(data)-1
	for i, row in enumerate(data):
		xLength = len(row)-1
		for j, item in enumerate(row):
			if data[i][j] == [char]:
				locations.append([i,j])
	dataRow.append(locations)
	antenaLocations.append(dataRow)

intersections = set()

for i, row in enumerate(data):
	for j, _ in enumerate(row):
		for symbol, locations in antenaLocations:
			for xcord1, ycord1 in locations:
				for xcord2, ycord2 in locations:
					for k in range(100):
						if(k*(j-xcord1) == (k-1)*(j-xcord2) and k*(i-ycord1) == (k-1)*(i-ycord2)):
							if([xcord1,ycord1] != [xcord2,ycord2]):
								intersections.add(str(j)+","+str(i))



print(len(intersections))

end = time.time()
print(end-start)