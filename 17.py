from timeit import default_timer as timer
import re
from PIL import Image

lines = str()
with open('17_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def pathToImage(path, xTarget, yTarget, hit):
	xMin = xTarget[0]
	xMax = xTarget[1]
	yMin = yTarget[0]
	yMax = yTarget[1]

	for p in path:
		xMin = min(p[0], xMin)
		xMax = max(p[0], xMax)
		yMin = min(p[1], yMin)
		yMax = max(p[1], yMax)

	shiftX = -1 * xMin
	shiftY = yMax

	img = Image.new('RGB', (xMax + shiftX + 1, ((yMin - shiftY) * -1) + 1), "white") # Create a new white image
	pixels = img.load() # Create the pixel map

	for x in range(xTarget[0], xTarget[1] + 1):
		for y in range(yTarget[0], yTarget[1] + 1):
			imgPointX = x + shiftX
			imgPointY = (y - shiftY) * -1
			if hit:
				pixels[imgPointX, imgPointY] = (0, 255, 0)
			else:
				pixels[imgPointX, imgPointY] = (0, 0, 0)

	for p in path:
		imgPointX = p[0] + shiftX
		imgPointY = (p[1] - shiftY) * -1
		pixels[imgPointX, imgPointY] = (255, 0, 0)
	img.show()
	


def part1(lines):
	area = re.split('(target area: x=)|(\.\.)|(, y=)', lines[0])
	xBounds = (int(area[4]), int(area[8]))
	yBounds = (int(area[12]), int(area[16]))
	pos = (0,0)
	
	hit = False
	path = []
	# if you start with upwards Vy, you will, at some point, always come back to y = 0
	# so maximum Vy will be (-1 * the bottom of your target)
	# becaues then one step after you come back to y = 0 you are just barely hitting the furthest edge of your target
	# So start with Vy there.
	# Then start with Vx = 0, and increase Vx until you hit the target or overshoot
	# If you overshoot without hitting it with that Vy, that means it's just impossible, and you need to decrease Vy and try again
	# It's possible for it to miss entirely for a given Vy because our steps are discrete.
	# If we were running in continuous time, it would always be able to hit for a given Vy
	# So decrease Vy by 1 and try again

	Vy = yBounds[0] * -1
	path.append(pos)

	peak = -1
	while not hit:
		overshot = False
		for Vx in range(xBounds[1]):
			vel = (Vx,Vy)
			path = []
			# Increase Vy until we no longer hit the target
			pos = (0,0)
			path.append(pos)
			hit = False
			while True:
				if xBounds[0] <= pos[0] <= xBounds[1] and yBounds[0] <= pos[1] <= yBounds[1]: # hit
					hit = True
					break
				if pos[0] > xBounds[1]: # missed
					overshot = True
					break
				if pos[1] < yBounds[0]: # missed
					break
				
				pos = (pos[0] + vel[0], pos[1] + vel[1])
				path.append(pos)
				if vel[0] > 0:
					vel = (vel[0] - 1, vel[1] - 1)
				elif vel[0] < 0:
					vel = (vel[0] + 1, vel[1] - 1)
				else:
					vel = (vel[0], vel[1] - 1)
			if hit:
				# pathToImage(path, xBounds, yBounds, hit)
				peak = max([p[1] for p in path])
				break
			elif overshot: break
		if peak == -1:
			Vy -= 1
	return (xBounds, yBounds), Vy, peak


def part2(targetArea, VyMax):
	#Get the target area adn VyMax from part 1
	xBounds = targetArea[0]
	yBounds = targetArea[1]
	VyMin = yBounds[0]
	VxMin = 1
	VxMax = xBounds[1]
	hitCount = 0
	hitVels = []
	for Vx in range(VxMin, VxMax + 1):
		for Vy in range(VyMin, VyMax + 1):
			#Try every combo of initial Vx and Vy to see if they hit the target
			vel = (Vx,Vy)
			path = []
			pos = (0,0)
			path.append(pos)
			hit = False
			while True:
				if xBounds[0] <= pos[0] <= xBounds[1] and yBounds[0] <= pos[1] <= yBounds[1]: # hit
					hit = True
					break
				if pos[0] > xBounds[1] or pos[1] < yBounds[0]: # missed
					break
				
				pos = (pos[0] + vel[0], pos[1] + vel[1])
				path.append(pos)
				if vel[0] > 0:
					vel = (vel[0] - 1, vel[1] - 1)
				elif vel[0] < 0:
					vel = (vel[0] + 1, vel[1] - 1)
				else:
					vel = (vel[0], vel[1] - 1)
			if hit:
				# pathToImage(path, xBounds, yBounds, hit)
				hitCount += 1
				hitVels.append((Vx, Vy))
	print
	return hitCount


start = timer()
targetArea, VyMax, Peak = part1(lines)
end = timer()
print("Part 1:", Peak)
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(targetArea, VyMax)
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()