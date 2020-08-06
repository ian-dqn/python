def print_grid(grid, x1, x2, y1, y2):
	size_v = len(grid)
	size_h = len(grid[0])
	for y in range(0, size_v):
		for x in range(0, size_h):
			if x >= x1 and x <= x2 and y >= y1 and y <= y2:
				print('x'),
			else:
				print(grid[y][x]),
		print('')
def main(grid, size_h, size_v):
	sum_grid = [[0 for k in range(size_h+1)] for l in range(size_v+1)]
	maxi = 0
	for y in range(size_v):
		for x in range(size_h):
			if grid[y][x] == 'o':
				sum_grid[y][x] = 0
			elif grid[y][x] == '.':
				sum_grid[y+1][x+1] = (1+min(sum_grid[y][x+1], sum_grid[y+1][x], sum_grid[y][x]))
				if sum_grid[y+1][x+1] > maxi:
					maxi = sum_grid[y+1][x+1]
					pos = [y, x]
			else:
				print('error')
				return -1, -1, -1
	return maxi, pos[0], pos[1]
		
if __name__ == '__main__':
	grid = ['oo...o', '.....o', '.o...o', 'o..o.o', 'o..o.o']
	size_v = len(grid)
	size_h = len(grid[0])
	square_size, y, x = main(grid, size_h, size_v)
	if y == -1:
		print('format error')
	print_grid(grid, x-square_size+1, x, y-square_size+1, y)
	
