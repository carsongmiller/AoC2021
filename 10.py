from timeit import default_timer as timer

lines = str()
with open('10_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def part1(lines):
	score = 0
	validLines = []
	
	for line in lines:
		invalid = False
		targetList = []
		for char in line:

			if char == '(' or char == '[' or char == '{' or char == '<':
				targetList.append(char)
				continue

			elif char == ')':
				if targetList[-1] == '(': targetList.pop()
				else: invalid = True

			elif char == ']':
				if targetList[-1] == '[': targetList.pop()
				else: invalid = True

			elif char == '}':
				if targetList[-1] == '{': targetList.pop()
				else: invalid = True

			elif char == '>':
				if targetList[-1] == '<': targetList.pop()
				else: invalid = True
			
			if invalid:
				if char == ')': score += 3
				elif char == ']': score += 57
				elif char == '}': score += 1197
				elif char == '>': score += 25137
				break

		if not invalid: validLines.append(line)
	return score, validLines

def part2(lines):
	#we know all lines we're given are valid now
	scores = []
	for line in lines:
		targetList = []
		for char in line:

			if char == '(' or char == '[' or char == '{' or char == '<':
				targetList.append(char)
				continue	

			else: targetList.pop()
		
		thisScore = 0
		for i in reversed(range(len(targetList))):
			thisScore *= 5
			if targetList[i] == '(': thisScore += 1
			elif targetList[i] == '[': thisScore += 2
			elif targetList[i] == '{': thisScore += 3
			elif targetList[i] == '<': thisScore += 4
		scores.append(thisScore)
	
	scores.sort()		
	return scores[int(len(scores)/2)]


start = timer()
p1 = part1(lines)
end = timer()
print("Part 1:", p1[0])
print("Time (msec):", (end - start) * 1000)
print()

start = timer()
p2 = part2(p1[1])
end = timer()
print("Part 2:", p2)
print("Time (msec):", (end - start) * 1000)
print()