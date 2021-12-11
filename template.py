from timeit import default_timer as timer

def part1(lines):
	pass

def part2(lines):
	pass


lines = str()
with open('X_input.txt') as f:
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