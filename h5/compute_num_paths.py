# Find the number of different paths from source (0,0) to sink (n,m) in an n by
# m rectangular grid. A valid path can only go down or right (no diagonal
# moves).  This script solves the problem using a dynamic programming algorithm.
#
# Twist: allow diagonal moves (down and right)
#   this requires taking into consideration all three grid entries prior to the
#   current (i,j) entry, rather than just the (i-1,j) and (i,j-1) entries
#
# CISC471
# Sean Nesdoly
# 2017-10-25

def initialize(n,m):

    # create n by m grid
    grid = [0] * n
    for i in range(n):
        grid[i] = [0] * m

    # fill first column with ones
    for row in range(n):
        grid[row][0] = 1

    # fill first row with ones
    for col in range(m):
        grid[0][col] = 1

    return grid


# fill in grid, NOT allowing diagonal moves
def fill_grid(n,m):
    grid = initialize(n,m)

    for i in range(1,n):
        for j in range(1,m):
            grid[i][j] = grid[i-1][j] + grid[i][j-1] # recurrence relation

    return grid[n-1][m-1] # solution


# fill in grid, allowing diagonal moves
def fill_grid_diagonals(n,m):
    grid = initialize(n,m)

    for i in range(1,n):
        for j in range(1,m):
            grid[i][j] = grid[i-1][j] + grid[i][j-1] + 1 # recurrence relation

            # Rappaport's recurrence relation (possibly wrong.....)
            #grid[i][j] = grid[i-1][j] + grid[i][j-1] + grid[i-1][j-1]


    return grid[n-1][m-1] # solution


# test runs
print fill_grid(3,3) # 6
print fill_grid_diagonals(3,3) # 11 (13 by Rappaport's recurrence relation)
