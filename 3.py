lines = str()
with open('3_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def part1(lines):
	gamma = ''
	epsilon = ''
	for index in range(len(lines[0])):
		countZero = 0
		countOne = 0
		

		for line in lines:
			if line[index] == '0': countZero += 1
			else: countOne += 1
		if countZero > countOne:
			gamma = gamma + '0'
			epsilon = epsilon + '1'
		else:
			gamma = gamma + '1'
			epsilon = epsilon + '0'

	return int(gamma, 2) * int(epsilon, 2)


def oxygenRating(lines, index):
	if len(lines) == 1: return int(lines[0], 2)

	countZero = 0
	countOne = 0
	newLines = []

	for line in lines:
		if line[index] == '0': countZero += 1
		else: countOne += 1
	if countZero > countOne:
		for line in lines:
			if line[index] == '0': newLines.append(line)
	elif countZero <= countOne:
		for line in lines:
			if line[index] == '1': newLines.append(line)

	return oxygenRating(newLines, index + 1)

def C02Rating(lines, index):
	if len(lines) == 1: return int(lines[0], 2)

	countZero = 0
	countOne = 0
	newLines = []

	for line in lines:
		if line[index] == '0': countZero += 1
		else: countOne += 1
	if countZero <= countOne:
		for line in lines:
			if line[index] == '0': newLines.append(line)
	elif countZero > countOne:
		for line in lines:
			if line[index] == '1': newLines.append(line)

	return C02Rating(newLines, index + 1)


def part2(lines):
	return oxygenRating(lines, 0) * C02Rating(lines, 0)


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))