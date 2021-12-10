from timeit import default_timer as timer

lines = str()
with open('4_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]



def vertWin(board):
	for i in range(len(board[0])):
		col = set([item[i] for item in board])
		if len(col) == 1 and '' in col: return True
	return False

def horiWin(board):
	for i in range(len(board)):
		col = set(board[i])
		if len(col) == 1 and '' in col: return True
	return False

def part1(lines):

	calls = lines[0].split(',')

	boards = []

	lines = lines[1:]
	lines.remove('')

	boards.append([])
	for i in range(len(lines)):
		if i % 6 == 5:
			boards.append([])
			continue
		boards[-1].append(lines[i].split())
	callsRequired = []

	for b in range(len(boards)):
		board = boards[b]
		winFound = False
		for c in range(len(calls)):
			call = calls[c]
			for row in range(len(board)):
				for cell in range(len(board[row])):
					if board[row][cell] == call:
						board[row][cell] = ''
						if vertWin(board) or horiWin(board):
							callsRequired.append(c + 1)
							winFound = True
					if winFound: break
				if winFound: break
			if winFound: break
		
	winner = callsRequired.index(min(callsRequired))
	sum = 0
	for row in boards[winner]:
		for cell in row:
			if cell != '': sum += int(cell)

	return (sum * int(calls[min(callsRequired) - 1]))

def part2(lines):

	calls = lines[0].split(',')
	boards = []

	lines = lines[1:]
	lines.remove('')

	boards.append([])
	for i in range(len(lines)):
		if i % 6 == 5:
			boards.append([])
			continue
		boards[-1].append(lines[i].split())

	callsRequired = []

	for b in range(len(boards)):
		board = boards[b]
		winFound = False
		for c in range(len(calls)):
			call = calls[c]
			for row in range(len(board)):
				for cell in range(len(board[row])):
					if board[row][cell] == call:
						board[row][cell] = ''
						if vertWin(board) or horiWin(board):
							callsRequired.append(c + 1)
							winFound = True
							break
					if winFound: break
				if winFound: break
			if winFound: break
		
	loser = callsRequired.index(max(callsRequired))
	sum = 0
	for row in boards[loser]:
		for cell in row:
			if cell != '': sum += int(cell)
	return sum * int(calls[max(callsRequired) - 1])


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