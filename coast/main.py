import fileinput

# maybe should have done this one as a class.. so much "global" stuff...
def visit_node(i, j):
	global h, w, edges, grid, visited_nodes, unvisited_nodes

	# check if out of grid
	if i < 0 or j < 0 or i >= h or j >= w:
		return

	# check if on land, we came from the sea so this must be an edge
	if grid[i][j] == 1:
		edges += 1
		return

	# if the node was unvisited, continue to next nodes
	node_s = "%d,%d" % (i,j)
	if node_s not in visited_nodes: # walk to next nodes
		visited_nodes.add(node_s)
		unvisited_nodes.append("%d,%d" % (i-1, j)) # up
		unvisited_nodes.append("%d,%d" % (i+1, j)) # down
		unvisited_nodes.append("%d,%d" % (i, j-1)) # left
		unvisited_nodes.append("%d,%d" % (i, j+1)) # right


def main():
	# generate grid
	for row in fileinput.input():
		grid.append(map(int, list(row.rstrip())))

	# add all edge nodes to unvisited_nodes
	for i in range(h):
		unvisited_nodes.append("%d,%d" % (i,0))
		unvisited_nodes.append("%d,%d" % (i, w-1))
	for j in range(w):
		unvisited_nodes.append("%d,%d" % (0, j))
		unvisited_nodes.append("%d,%d" % (h-1, j))

	# start exploring
	while len(unvisited_nodes):
		i,j = map(int, unvisited_nodes.pop().split(','))
		visit_node(i,j)

	# answer
	print(edges)


h, w = map(int, raw_input().split(' '))
edges = 0
grid = list()
visited_nodes = set()
unvisited_nodes = list()

if __name__ == "__main__":
	main()
