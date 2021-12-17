from timeit import default_timer as timer

lines = str()
with open('5_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def part1(lines):
	pointPairs = [([int(x) for x in pair[0].split(',')], [int(x) for x in pair[1].split(',')]) for pair in [line.split(' -> ') for line in lines]]

	#use only vert or hori pairs for this part
	#orthoPairs = []
	map = {}
	for pointPair in pointPairs:
		if pointPair[0][0] == pointPair[1][0]:
			x = pointPair[0][0]
			for y in range(min(pointPair[0][1], pointPair[1][1]), max(pointPair[0][1], pointPair[1][1]) + 1):
				if (x, y) not in map:
					map[(x, y)] = 1
				else:
					map[(x, y)] += 1
		elif pointPair[0][1] == pointPair[1][1]:
			y = pointPair[0][1]
			for x in range(min(pointPair[0][0], pointPair[1][0]), max(pointPair[0][0], pointPair[1][0]) + 1):
				if (x, y) not in map:
					map[(x, y)] = 1
				else:
					map[(x, y)] += 1
	
	#now count map entries that are >= 2
	sum = 0
	for key in map:
		if map[key] >= 2:
			sum += 1
	return sum

def part2(lines):
	pointPairs = [([int(x) for x in pair[0].split(',')], [int(x) for x in pair[1].split(',')]) for pair in [line.split(' -> ') for line in lines]]

	#use only vert or hori pairs for this part
	#orthoPairs = []
	map = {}
	for pointPair in pointPairs:
		if pointPair[0][0] == pointPair[1][0]: #vertical
			x = pointPair[0][0]
			for y in range(min(pointPair[0][1], pointPair[1][1]), max(pointPair[0][1], pointPair[1][1]) + 1):
				if (x, y) not in map:
					map[(x, y)] = 1
				else:
					map[(x, y)] += 1
		elif pointPair[0][1] == pointPair[1][1]: #horizontal
			y = pointPair[0][1]
			for x in range(min(pointPair[0][0], pointPair[1][0]), max(pointPair[0][0], pointPair[1][0]) + 1):
				if (x, y) not in map:
					map[(x, y)] = 1
				else:
					map[(x, y)] += 1
		else: #45 degrees
			xStart = pointPair[0][0]
			xEnd = pointPair[1][0]

			yStart = pointPair[0][1]
			yEnd = pointPair[1][1]

			for i in range(abs(xEnd - xStart) + 1):
				if xStart < xEnd: x = xStart + i
				else: x = xStart - i

				if yStart < yEnd: y = yStart + i
				else: y = yStart - i

				if (x, y) not in map:
					map[(x, y)] = 1
				else:
					map[(x, y)] += 1
		
	#now count map entries that are >= 2
	sum = 0
	for key in map:
		if map[key] >= 2:
			sum += 1
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