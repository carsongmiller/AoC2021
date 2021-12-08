from collections import Counter

lines = str()
with open('8_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def part1(lines):
	outputList = []
	sum = 0
	for line in lines:
		for output in line.split(' | ')[1].split():
			if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7: sum += 1
	return sum

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

# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l

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
		0: set(['a','b', 'c', 'e', 'f', 'g']),
		1: set(['c', 'f']),
		2: set(['a', 'c', 'd', 'e', 'g']),
		3: set(['a', 'c', 'd', 'f', 'g']),
		4: set(['b', 'c', 'd', 'f']),
		5: set(['a', 'b', 'd', 'f', 'g']),
		6: set(['a', 'b', 'd', 'e', 'f', 'g']),
		7: set(['a', 'c', 'f']),
		8: set(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
		9: set(['a', 'b', 'c', 'd', 'f', 'g'])
	}
	segmentsMapped = [map[x] for x in segments]
	segmentSet = set(segmentsMapped)
	for key in digits:
		if digits[key] == segmentSet: return key
	return ''


def part2(lines):
	entries = [[y[0].split(), y[1].split()] for y in [x.split(' | ') for x in lines]]
	allPerms = permutation([chr(x) for x in range(ord('a'), ord('g') + 1)])
	validMappings = []
	for perm in allPerms:
		newMap = {}
		for i in range(len(perm)):
			newMap[chr(97 + i)] = perm[i]
		validMappings.append(newMap)

	outputSum = 0
	checked = 0

	for entry in entries:
		correctMap = {}

		for map in validMappings:
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


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))