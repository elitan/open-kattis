import sys

def legal_move_count(i, j, grid):
	grid_size = len(grid[0])
	if grid[i][j] != '.':
		return 0

	ret = 0 # return value
	# check top
	if j > 1 and grid[i][j-1] == 'o' and grid[i][j-2] == 'o':
		ret += 1
	# check bot
	if j < grid_size - 2 and grid[i][j+1] == 'o' and grid[i][j+2] == 'o':
		ret += 1
	# check right 
	if i < grid_size - 2 and grid[i+1][j] == 'o' and grid[i+2][j] == 'o':
		ret += 1
	# check left
	if i > 1 and grid[i-1][j] == 'o' and grid[i-2][j] == 'o':
		ret += 1
	return ret

grid = list()
for row in xrange(7):
	grid.append(list(raw_input()))

c = 0
for i, x in enumerate(grid):
	for j, y in enumerate(x):
		c += legal_move_count(i, j, grid)
print(c)
