from timeit import default_timer as timer
import copy

lines = str()
with open('9_input.txt') as f:	
	lines = [n.strip() for n in f.readlines()]


def printBasinMap(map):
	s = ''
	for r in range(len(map)):
		for c in range(len(map[r])):
			if map[r][c] == 9: s += 'X'
			elif map[r][c] == -1: s += 'O'
			else: s += '.'
		s += '\n'
	for i in range(len(map[0]) + 5): s += '='
	s += '\n\n'
	print(s)


def part1(lines):
	map = []
	totalRisk = 0
	for line in lines:
		map.append([int(x) for x in line])
	for r in range(len(map)):
		for c in range(len(map[r])):
			a = len(map[r])
			lowPoint = True
			thisPoint = map[r][c]
			try:
				if r-1 >= 0 and map[r-1][c] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			try:
				if r+1 < len(map) and map[r+1][c] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			try:
				if c-1 >= 0 and map[r][c-1] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			try:
				if c+1 < len(map[r]) and map[r][c+1] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			if lowPoint: totalRisk += thisPoint + 1
	return totalRisk
	

def part2(lines):
	map = []
	lowPoints = []
	for line in lines:
		map.append([int(x) for x in line])
	
	h = len(map)
	w = len(map[0]) #all rows are uniform length

	for r in range(len(map)):
		for c in range(len(map[r])):
			a = len(map[r])
			lowPoint = True
			thisPoint = map[r][c]
			try:
				if r-1 >= 0 and map[r-1][c] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			try:
				if r+1 < len(map) and map[r+1][c] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			try:
				if c-1 >= 0 and map[r][c-1] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			try:
				if c+1 < len(map[r]) and map[r][c+1] <= thisPoint:
					lowPoint = False
					continue
			except:
				pass
			if lowPoint:
				lowPoints.append((r, c))
	
	largeBasins = [0, 0, 0]

	# now that we've got the low points, do a flood-fill for each one until we hit 9's
	for lowPoint in lowPoints:
		# create a copy of the map
		#map = copy.deepcopy(map)
		map[lowPoint[0]][lowPoint[1]] = -1
		# start at the point, and spread out to the 4 cardinal directions if possible
		# if a square is not -1 and also not 9, set it to -1
		# do this util we don't infect any more points on a single cycle

		fullyFilled = False
		infected = [(lowPoint[0], lowPoint[1])]

		basinSize = 1

		while not fullyFilled:
			fullyFilled = True
			newInfected = []
			for inf in infected:
				r = inf[0]
				c = inf[1]
				if r-1 >= 0 and map[r-1][c] >= 0 and map[r-1][c] < 9: #point is able to be infected
					fullyFilled = False
					map[r-1][c] = -1
					newInfected.append((r-1, c))
					basinSize += 1
				if r+1 < h and map[r+1][c] >= 0 and map[r+1][c] < 9: #point is able to be infected
					fullyFilled = False
					map[r+1][c] = -1
					newInfected.append((r+1, c))
					basinSize += 1
				if c-1 >= 0 and map[r][c-1] >= 0 and map[r][c-1] < 9: #point is able to be infected
					fullyFilled = False
					map[r][c-1] = -1
					newInfected.append((r, c-1))
					basinSize += 1
				if c+1 < h and map[r][c+1] >= 0 and map[r][c+1] < 9: #point is able to be infected
					fullyFilled = False
					map[r][c+1] = -1
					newInfected.append((r, c+1))
					basinSize += 1
			infected = newInfected #next loop we'll only look at the points we just now infected
			#if not fullyFilled: printBasinMap(map)
		
		if basinSize > largeBasins[0]:
			largeBasins[2] = largeBasins[1]
			largeBasins[1] = largeBasins[0]
			largeBasins[0] = basinSize
		elif basinSize > largeBasins[1]:
			largeBasins[2] = largeBasins[1]
			largeBasins[1] = basinSize
		elif basinSize > largeBasins[2]:
			largeBasins[2] = basinSize

	return largeBasins[0] * largeBasins[1] * largeBasins[2]


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