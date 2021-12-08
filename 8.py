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
		if segmentSet.union(validDigit) == segmentSet:
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

def part2(lines):
	entries = [[y[0].split(), y[1].split()] for y in [x.split(' | ') for x in lines]]
	allPerms = permutation([chr(x) for x in range(ord('a'), ord('g') + 1)])
	validMappings = []
	for perm in allPerms:
		newMap = {}
		for i in range(len(perm)):
			newMap[chr(97 + i)] = perm[i]
		validMappings.append(newMap)


	for entry in entries:
		# possible = {}
		# for c in range(ord('a'), ord('g') + 1):
		# 	possible[chr(c)] = [chr(x) for x in range(ord('a'), ord('g') + 1)]
		
		# reducePossible(possible, entry[0])

		currentValid = validMappings.copy()

		for digit in entry[0]:
			currentCopy = currentValid.copy()
			for map in currentCopy:
				#create list of the segments that would be on for this digit with this map
				testDigit = []
				for segment in digit:
					testDigit.append(map[segment])
				if not isValidDigit(testDigit): currentValid.remove(map)
		print(len(currentValid))

			
		
		

		


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))