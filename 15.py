from timeit import default_timer as timer
from PIL import Image
import heapq

lines = str()
with open('15_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return not self.elements
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def manhattan(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getNeighbors(p, rMax, cMax):
	n = [
		(p[0]-1, p[1]),
		(p[0]+1, p[1]),
		(p[0], p[1]-1),
		(p[0], p[1]+1)
	]
	return [x for x in n if 0 <= x[0] < rMax and 0 <= x[1] < cMax]

def printPath(closed, valueDict):
	finished = False
	current = closed[-1]
	
	while not finished:
		currentVals = valueDict[current]
		print(current, currentVals.weight)
		if current == (0,0): finished = True
		else: current = currentVals.parent
	print()

def pathFromParentDict(parent, start, end):
	finished = False
	current = end
	path = []
	while not finished:
		path.insert(0, current)
		if current == start: finished = True
		else: current = parent[current]
	return path

def pathToImage(path):
	xMax = 0
	yMax = 0
	for p in path:
		xMax = max(p[0], xMax)
		yMax = max(p[1], yMax)

	img = Image.new('RGB', (xMax + 1, yMax + 1), "white") # Create a new white image
	pixels = img.load() # Create the pixel map

	for p in path:
		pixels[p[1], p[0]] = (0, 0, 0)
	img.show()

def AStarDistance(map, start, end):
	open = PriorityQueue() #priority queue.  contains only coordinates
	open.put(start, 0)
	nodeCosts = {}
	parents = {}
	nodeCosts[(0,0)] = 0

	finished = False
	while not finished:
		currentPos = open.get() # gets node with lowest F value, and removes it from queue

		if currentPos == end:
			finished = True
		else:
			neighbors = getNeighbors(currentPos, len(map), len(map[0]))
			
			for n in neighbors:
				newG = nodeCosts[currentPos] + map[n[0]][n[1]]
				if n not in nodeCosts or newG < nodeCosts[n]:
					nodeCosts[n] = newG
					parents[n] = currentPos
					open.put(n, nodeCosts[n] + manhattan(n, end))

	return nodeCosts, parents

def part1(lines):
	map = [[int(c) for c in line] for line in lines]
	target = (len(map) - 1, len(map[0]) - 1)
	nodeCosts, parents = AStarDistance(map, (0,0), target)
	# pathToImage(pathFromParentDict(parents, (0,0), target))
	return nodeCosts[target]

def part2(lines):
	baseMap = [[int(c) for c in line] for line in lines]

	tileR = 5
	tileC = 5
	tiledMap = []
	for r in range(tileR):
		for innerR in range(len(baseMap)):
			tiledMap.append([])
			for c in range(tileC):
				tiledMap[r*len(baseMap) + innerR].extend([(((x + c + r)-1) % 9) + 1 for x in baseMap[innerR]])

	target = (len(tiledMap) - 1, len(tiledMap[0]) - 1)
	nodeCosts, parents = AStarDistance(tiledMap, (0,0), target)
	# pathToImage(pathFromParentDict(parents, (0,0), target))
	return nodeCosts[target]


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