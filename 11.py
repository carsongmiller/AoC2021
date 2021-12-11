from timeit import default_timer as timer

def cascade(G, r, c, flashed):
	h = len(G)
	w = len(G[0])
	DR = [-1, -1, 0, 1, 1, 1, 0, -1]
	DC = [0, 1, 1, 1, 0, -1, -1, -1]

	if G[r][c] > 9 and (r, c) not in flashed:
		flashed.append((r, c))
		for i in range(8): #increase all octopi in 8 directions
			if 0 <= r+DR[i] < h and 0 <= c+DC[i] < w:
				G[r+DR[i]][c+DC[i]] += 1
				cascade(G, r+DR[i], c+DC[i], flashed)

def printMap(G):
	s = ''
	for r in range(len(G)):
		for c in range(len(G[r])):
			s += str(G[r][c])
		s += '\n'
	print(s)

def part1(lines):
	G = []
	flashes = 0
	for line in lines: G.append([int(x) for x in line])
	
	for step in range(100):
		flashed = []

		G = [[z+1 for z in y] for y in G] #increase all by 1

		for r in range(len(G)):
			for c in range(len(G[r])):
				cascade(G, r, c, flashed)
			
		flashes += len(flashed)

		G = [[0 if z > 9 else z for z in y] for y in G] #reset any that are >= 9 to zero
		
	return flashes



def part2(lines):
	G = []
	for line in lines: G.append([int(x) for x in line])
	synced = False
	max = len(G) * len(G[0])
	step = 0
	while True:
		flashed = []

		G = [[z+1 for z in y] for y in G] #increase all by 1
		step += 1

		for r in range(len(G)):
			for c in range(len(G[r])):
				cascade(G, r, c, flashed)
			
		if len(flashed) == max:
			return step
		
		G = [[0 if z > 9 else z for z in y] for y in G] #reset any that are >= 9 to zero
		

lines = str()
with open('11_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

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