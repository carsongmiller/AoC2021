from timeit import default_timer as timer

lines = str()
with open('6_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def stepDay(fishDict):
	newFishDict = {}
	for key in fishDict:
		if key == 0:
			newFishDict[8] = fishDict[key]
			if 6 not in newFishDict:
				newFishDict[6] = fishDict[key]
			else:
				newFishDict[6] += fishDict[key]
		else:
			if key-1 not in newFishDict:
				newFishDict[key-1] = fishDict[key]
			else:
				newFishDict[key-1] += fishDict[key]
	return newFishDict

def part1(lines):
	fishes = [int(fish) for fish in lines[0].split(',')]

	fishDict = {}
	for fish in fishes:
		if fish not in fishDict:
			fishDict[fish] = 1
		else:
			fishDict[fish] += 1
	
	for i in range(80):
		fishDict = stepDay(fishDict)
		
		# print(fishDict)
		# sum = 0
		# for key in fishDict:
		# 	sum += fishDict[key]
		# print(sum)
	
	sum = 0
	for key in fishDict:
		sum += fishDict[key]
	return sum

def part2(lines):
	fishes = [int(fish) for fish in lines[0].split(',')]
	fishDict = {}
	for fish in fishes:
		if fish not in fishDict:
			fishDict[fish] = 1
		else:
			fishDict[fish] += 1
	for i in range(256):
		fishDict = stepDay(fishDict)
	sum = 0
	for key in fishDict:
		sum += fishDict[key]
	return sum


start = timer()
p1 = part1(lines)
end = timer()
print("Part 1:", p1)
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(lines)
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()