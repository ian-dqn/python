import numpy as np

def print_grid(grid): 
#function to print the grid
    for i in range(9): 
        for j in range(9): 
            print grid[i][j], 
        print ('') 

def is_possible(grid, y, x, n):
#fct who determines if the n number can fit into the case in y, x coordinates
	for i in range(0, 9):
		if grid[y][i] == n:
			return False
	for j in range(0, 9):
		if grid[j][x] == n:
			return False
	x0 = (x/3)*3
	y0 = (y/3)*3
	for i in range(0, 3):
		for j in range(0, 3):
			if grid[y0+i][x0+j] == n:
				return False
	return True

def solver(grid):
#recursive function
	for y in range(0, 9):
		for x in range(0, 9):
			if grid[y][x] == 0:
				for n in range (1, 10):
					if is_possible(grid, y, x, n):
						grid[y][x] = n
						solver(grid)
						#if we came here, none of n is possible
						grid[y][x] = 0
				return
	print_grid(grid)

if __name__ == "__main__":
	grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]] 
	solver(grid)
