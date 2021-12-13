from timeit import default_timer as timer
import networkx as nx
import copy

lines = str()
with open('12_input.txt') as f:
	lines = [n.strip() for n in f.readlines()]

def findPaths_1(G, curNode, curPath, allPaths):
	if curNode == 'end':
		allPaths.append(copy.deepcopy(curPath))
		return

	curPath = nx.DiGraph(curPath)
	for nextNode in G.adj[curNode]:
		if (curNode, nextNode) not in curPath.edges and (nextNode.isupper() or nextNode not in curPath.nodes):
			curPath.add_edge(curNode, nextNode)
			findPaths_1(G, nextNode, curPath, allPaths)
			curPath.remove_edge(curNode, nextNode)
			#if that was the only edge connecting nextNode, remove the node as well
			if len(curPath.adj[nextNode]) == 0: curPath.remove_node(nextNode)

def findPaths_2(G, curNode, curPath, allPaths, smallVisitedTwice):
	if curNode == 'end':
		allPaths.append(copy.deepcopy(curPath))
		return

	curPath = nx.DiGraph(curPath)
	for nextNode in G.adj[curNode]:
		if nextNode.isupper() or nextNode not in curPath.nodes or (not smallVisitedTwice and nextNode !='start' and nextNode != 'end'):
			if not nextNode.isupper() and nextNode in curPath.nodes:
				curPath.add_edge(curNode, nextNode)
				findPaths_2(G, nextNode, curPath, allPaths, True)
			else:
				curPath.add_edge(curNode, nextNode)
				findPaths_2(G, nextNode, curPath, allPaths, smallVisitedTwice)

			curPath.remove_edge(curNode, nextNode)
			#if that was the only edge connecting nextNode, remove the node as well
			if len(curPath.adj[nextNode]) == 0: curPath.remove_node(nextNode)


def part1(lines):
	G = nx.Graph()
	for line in lines:
		[a, b] = line.split('-')
		G.add_edge(a, b)
	
	pathList = []
	findPaths_1(G, 'start', nx.DiGraph(), pathList)

	return len(pathList)




def part2(lines):
	G = nx.Graph()
	for line in lines:
		[a, b] = line.split('-')
		G.add_edge(a, b)
	
	pathList = []
	findPaths_2(G, 'start', nx.DiGraph(), pathList, False)

	return len(pathList)


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