lines = str()
with open('7_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def triangleNum(n):
	if n == 0:
		return n
	i = n
	while True:
		if i == 1:
			return n
		i -= 1
		n += i

def part1(lines):
	crabs = [int(x) for x in lines[0].split(',')]
	bestDist = max(crabs) * len(crabs)
	bestLoc = 0
	for i in range(min(crabs), max(crabs) + 1):
		travelDist = 0
		for crab in crabs:
			travelDist += abs(crab - i)
		if travelDist < bestDist:
			bestDist = travelDist
			bestLoc = i
	print(bestLoc)
	return bestDist

def part2(lines):
	crabs = [int(x) for x in lines[0].split(',')]

	#precompute all the triangle numbers we may need, store in dict
	triangles = {}
	for i in range(max(crabs) + 1):
		triangles[i] = triangleNum(i)

	bestDist = triangles[max(crabs)] * len(crabs)
	bestLoc = 0

	for i in range(min(crabs), max(crabs) + 1):
		travelDist = 0
		for crab in crabs:
			travelDist += triangles[abs(crab - i)]
		if travelDist < bestDist:
			bestDist = travelDist
			bestLoc = i

	print(bestLoc)
	return bestDist


print("Part 1:", part1(lines)) #turns out this is just the median
print("Part 2:", part2(lines)) #turns out this is just the mean (rounded down)