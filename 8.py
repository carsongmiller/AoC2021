from timeit import default_timer as timer

lines = str()
with open('8_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]



def removeAllBut(list, removeVals):
	listCopy = list.copy()
	for item in list:
		if item not in removeVals: listCopy.remove(item)
	return listCopy

def isValidDigit(segments):
	valid = [
		set(['a','b', 'c', 'e', 'f', 'g']),
		set(['c', 'f']),
		set(['a', 'c', 'd', 'e', 'g']),
		set(['a', 'c', 'd', 'f', 'g']),
		set(['b', 'c', 'd', 'f']),
		set(['a', 'b', 'd', 'f', 'g']),
		set(['a', 'b', 'd', 'e', 'f', 'g']),
		set(['a', 'c', 'f']),
		set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
		set(['a', 'b', 'c', 'd', 'f', 'g'])
	]
	segmentSet = set(segments)
	found = False
	for validDigit in valid:
		if segmentSet == validDigit:
			return True
	return False


def printDigit(segments, map = {'a': 'a','b': 'b','c': 'c','d': 'd','e': 'e','f': 'f','g': 'g'}):
	segmentsMapped = [map[x] for x in segments]
	s = ' '
	s += '---' if 'a' in segmentsMapped else ' '
	s += ' \n'
	s += '|' if 'b' in segmentsMapped else ' '
	s += '   '
	s += '|' if 'c' in segmentsMapped else ' '
	s += '\n '
	s += '---' if 'd' in segmentsMapped else ' '
	s += ' \n'
	s += '|' if 'e' in segmentsMapped else ' '
	s += '   '
	s += '|' if 'f' in segmentsMapped else ' '
	s += '\n '
	s += '---' if 'g' in segmentsMapped else ' '
	s += ' '
	print(s)

def segmentsToInt(segments, map = {'a': 'a','b': 'b','c': 'c','d': 'd','e': 'e','f': 'f','g': 'g'}):
	digits = {
		frozenset(['a','b', 'c', 'e', 'f', 'g']): 0,
		frozenset(['c', 'f']): 1,
		frozenset(['a', 'c', 'd', 'e', 'g']): 2,
		frozenset(['a', 'c', 'd', 'f', 'g']): 3,
		frozenset(['b', 'c', 'd', 'f']): 4,
		frozenset(['a', 'b', 'd', 'f', 'g']): 5,
		frozenset(['a', 'b', 'd', 'e', 'f', 'g']): 6,
		frozenset(['a', 'c', 'f']): 7,
		frozenset(['a', 'b', 'c', 'd', 'e', 'f', 'g']): 8,
		frozenset(['a', 'b', 'c', 'd', 'f', 'g']): 9
	}
	segmentsMapped = [map[x] for x in segments]
	segmentSet = frozenset(segmentsMapped)
	return digits[segmentSet]


#takes list of digits and modifies dictionary of possible valid mappings for each segment accordingly
def reducePossible(possible, digits):
	for digit in digits:
		antiDigit = []
		allChars = [chr(x) for x in range(ord('a'), ord('g') + 1)]
		for c in allChars:
			if c not in digit: antiDigit.append(c)

		if len(digit) == 2:
			possible['a'] = removeAllBut(possible['a'], [c for c in antiDigit])
			possible['b'] = removeAllBut(possible['b'], [c for c in antiDigit])
			possible['c'] = removeAllBut(possible['c'], [c for c in digit])
			possible['d'] = removeAllBut(possible['d'], [c for c in antiDigit])
			possible['e'] = removeAllBut(possible['e'], [c for c in antiDigit])
			possible['f'] = removeAllBut(possible['f'], [c for c in digit])
			possible['g'] = removeAllBut(possible['g'], [c for c in antiDigit])
		if len(digit) == 3:
			possible['a'] = removeAllBut(possible['a'], [c for c in digit])
			possible['b'] = removeAllBut(possible['b'], [c for c in antiDigit])
			possible['c'] = removeAllBut(possible['c'], [c for c in digit])
			possible['d'] = removeAllBut(possible['d'], [c for c in antiDigit])
			possible['e'] = removeAllBut(possible['e'], [c for c in antiDigit])
			possible['f'] = removeAllBut(possible['f'], [c for c in digit])
			possible['g'] = removeAllBut(possible['g'], [c for c in antiDigit])
		if len(digit) == 4:
			possible['a'] = removeAllBut(possible['a'], [c for c in antiDigit])
			possible['b'] = removeAllBut(possible['b'], [c for c in digit])
			possible['c'] = removeAllBut(possible['c'], [c for c in digit])
			possible['d'] = removeAllBut(possible['d'], [c for c in digit])
			possible['e'] = removeAllBut(possible['e'], [c for c in antiDigit])
			possible['f'] = removeAllBut(possible['f'], [c for c in digit])
			possible['g'] = removeAllBut(possible['g'], [c for c in antiDigit])
	return possible


def part1(lines):
	sum = 0
	for line in lines:
		for output in line.split(' | ')[1].split():
			if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7: sum += 1
	return sum


def part2(lines):
	entries = [[y[0].split(), y[1].split()] for y in [x.split(' | ') for x in lines]]

	outputSum = 0
	checked = 0

	for entry in entries:

		possible = {}
		for c in range(ord('a'), ord('g') + 1):
			possible[chr(c)] = [chr(x) for x in range(ord('a'), ord('g') + 1)]

		reducePossible(possible, entry[0])


		valid = []
		#There will always be 8 valid permutations left after this
		for i in range(8):
			newValid = {}
			newValid['a'] = possible['a'][0]
			newValid['b'] = possible['b'][0] if i % 2 == 0 else possible['b'][1]
			newValid['c'] = possible['c'][0] if (i>>1) % 2 == 0 else possible['c'][1]
			newValid['d'] = possible['d'][0] if i % 2 == 1 else possible['b'][1]
			newValid['e'] = possible['e'][0] if (i>>2) % 2 == 0 else possible['e'][1]
			newValid['f'] = possible['f'][0] if (i>>1) % 2 == 1 else possible['f'][1]
			newValid['g'] = possible['g'][0] if (i>>2) % 2 == 1 else possible['g'][1]
			newReverse = {} #now flip this map around because that what I wrote the code below to take ...
			for x in newValid:
				newReverse[newValid[x]] = x
			
			valid.append(newReverse)
		correctMap = {}

		#go through each permutation of mappings until we find one that works
		for map in valid:
			for digit in entry[0]:
				allValid = True
				#create list of the segments that would be on for this digit with this map
				testDigit = [map[segment] for segment in digit]
				
				checked += 1
				if not isValidDigit(testDigit):
					allValid = False
					break
			if allValid:
				correctMap = map
				break
		outputStr = ''
		for digit in entry[1]: outputStr += str(segmentsToInt([segment for segment in digit], correctMap))
		outputSum += int(outputStr)

	return outputSum

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