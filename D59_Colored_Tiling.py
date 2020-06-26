'''
We have a stock of tiles with colored edges at our disposal and there’s a wall we need to tile up. However, there are two catches. The stock is limited and if two tiles touch each other, their edges must match on color.

The solution to the problem is backtracking. And even though I have already used backtracking on day 23, the tiling problem is worth the attention.
It is provably difficult problem that belongs to NP-complete class. There are not many NP-complete problems and I think it’s important to try to solve few of them to get a grasp of how difficult they really are.
The problem instance in my case is the following:
wall 7x7 with predefined colors at the edges
stock of 30 tiles
2 colors represented as 0 and 1
tile represented as a tuple(w, x, y, z)
tiles must match by the schema on the picture

That’s a small wall, but if there’s no solution I need to check a large portion of the incorrect ones, which is up to
30!/5! = 2210440498434925488635904000000
'''
import numpy as np
from collections import deque
# Algorithm
def add(wall, row, col, tile):
    assert np.all(wall[row, col, :] == -1)

    # check neighbours if the tile fits
    for i, j, m, n in [[-1, 0, 3, 0], [1, 0, 0, 3],
                       [0, -1, 1, 2], [0, 1, 2, 1]]:
        t = wall[row + i, col + j, m]
        if t != -1 and t != tile[n]:
            return False
    # add the tile
    wall[row, col, :] = tile
    return True
def remove(wall, row, col):
    wall[row, col, :] = -1
def solve(wall, tiles, row=1, col=1):
    # carry on the next row
    if col == wall.shape[1] - 1:
        row += 1
        col = 1
    # solution found
    if row == wall.shape[0] - 1:
        return True
    # try each tile
    for i in range(len(tiles)):
        tile = tiles.popleft()
        if add(wall, row, col, tile):
            # backtrack
            if solve(wall, tiles, row, col + 1):
                return True
            remove(wall, row, col)
        tiles.append(tile)

# Wall
def make_wall(rows, cols):
    # create wall
    wall = np.zeros((rows, cols, 4), dtype=int) - 1
    # randomize wall edges
    wall[-1, :, 0] = np.random.randint(0, 2, cols)
    wall[:, 0, 1] = np.random.randint(0, 2, rows)
    wall[:, -1, 2] = np.random.randint(0, 2, rows)
    wall[0, :, 3] = np.random.randint(0, 2, cols)
    return wall
def print_wall(wall):
    chars = np.array(list('01 '))
    tile = lambda i, j: ''.join(chars[wall[i, j, :]])
    # print rows
    for i in range(wall.shape[0]):
        row = [tile(i, j)[:2] for j in range(wall.shape[1])]
        print(' '.join(row))
        row = [tile(i, j)[2:] for j in range(wall.shape[1])]
        print(' '.join(row))

# Run
wall = make_wall(6,6)
tiles = deque(np.random.randint(0,2,(30,4)))

solve(wall, tiles)
print_wall(wall)
