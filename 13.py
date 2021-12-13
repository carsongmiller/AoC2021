from timeit import default_timer as timer
from PIL import Image

lines = str()
with open('13_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]


def dotImage(points):
	xMax = 0
	yMax = 0
	for p in points:
		xMax = max(p[0], xMax)
		yMax = max(p[1], yMax)

	img = Image.new('RGB', (xMax + 1, yMax + 1), "white") # Create a new white image
	pixels = img.load() # Create the pixel map

	for p in points:
		pixels[p[0], p[1]] = (0, 0, 0)
	img.show()

def part1(lines):
	points = []
	coords = []
	folds = []
	for line in lines:
		if len(line) > 0:
			if line[0] == 'f':
				if line[11] == 'x':
					folds.append(('x', int(line[13:])))
				elif line[11] == 'y':
					folds.append(('y', int(line[13:])))
				
				
			else: coords.append(line)
	for coord in coords:
		s = coord.split(',')
		a = 0
		points.append((int(s[0]), int(s[1])))
	
	# fold now
	fold = folds[0]
	for i in range(len(points)):
		p = points[i]
		if fold[0] == 'x':
			if fold[1] < p[0]:
				points[i] = (fold[1] * 2 - p[0], p[1])
		else:
			if fold[1] < p[1]:
				points[i] = (p[0], fold[1] * 2 - p[1])
	
	unique = []
	for p in points:
		if p not in unique: unique.append(p)
	
	return len(unique)


def part2(lines):
	points = []
	coords = []
	folds = []
	for line in lines:
		if len(line) > 0:
			if line[0] == 'f':
				if line[11] == 'x':
					folds.append(('x', int(line[13:])))
				elif line[11] == 'y':
					folds.append(('y', int(line[13:])))
				
				
			else: coords.append(line)
	for coord in coords:
		s = coord.split(',')
		a = 0
		points.append((int(s[0]), int(s[1])))
	
	# fold now
	for fold in folds:
		for i in range(len(points)):
			p = points[i]
			if fold[0] == 'x':
				if fold[1] < p[0]:
					points[i] = (fold[1] * 2 - p[0], p[1])
			else:
				if fold[1] < p[1]:
					points[i] = (p[0], fold[1] * 2 - p[1])
	
		unique = []
		for p in points:
			if p not in unique: unique.append(p)
	
	dotImage(unique)



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