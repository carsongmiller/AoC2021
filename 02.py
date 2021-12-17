from timeit import default_timer as timer

lines = str()
with open('2_input.txt') as f:
    lines = [n for n in f.readlines()]


def part1(lines):

    vertDist = 0
    horDist = 0

    for line in lines:
        line = line.strip().split()
        if line[0] == 'up':
            vertDist -= int(line[1])
        elif line[0] == 'down':
            vertDist += int(line[1])
        elif line[0] == 'forward':
            horDist += int(line[1])

    return vertDist * horDist

def part2(lines):

    vertDist = 0
    horDist = 0
    aim = 0

    for line in lines:
        line = line.strip().split()
        if line[0] == 'up':
            aim -= int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        elif line[0] == 'forward':
            horDist += int(line[1])
            vertDist += aim * int(line[1])

    return vertDist * horDist

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