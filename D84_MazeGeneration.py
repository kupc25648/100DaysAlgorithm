'''
Every good story needs a labyrinth. Ariadne and Theseus, The Shining, Harry Potter, … I have used Kruskal’s algorithm for minimum spanning tree to generate a maze in a simple and efficient way.

First, we generate an undirected graph represented by 2-dimensional matrix.
white square is a cell — and represents graph node
green square is a wall
black square can be either one — and represents graph link

Kruskals’ algorithm splits the graph nodes into separate components and repeatedly unifies them using graph links. However, there is a condition that after the link has been added, number of components must have decreased.
Graph components and their unions… it should have been familiar since I have already implemented union-find structure on day 41.
All we need is to pick an edge on random, check if the neighbouring cells belong to a different components and unify them by turning black position into white cell. Otherwise make there wall.

https://medium.com/100-days-of-algorithms/day-84-maze-generation-634aaca67e34
'''

import numpy as np
from bokeh.plotting import figure, show, output_notebook

# Algorithm
def generate_maze(n,m):
    # maze skeleton
    maze = np.tile([[1,2],[2,0]], (n//2+1,m//2+1))
    maze = maze[:-1,:-1]

    cells = {(i,j):(i,j) for i,j in np.argwhere(maze ==1)}
    walls = np.argwhere(maze ==2)

    # union-find
    def find(p,q):
        if p != cells[p] or q != cells[q]:
            cells[p], cells[q] = find(cells[p], cells[q])
        return cells[p], cells[q]

    # find spanning tree
    np.random.shuffle(walls)
    for wi, wj in walls:
        if wi % 2:
            p,q = find((wi-1,wj),(wi+1,wj))
        else:
            p,q = find((wi,wj-1),(wi,wj+1))
        maze[wi,wj] = p != q
        if p != q:
            cells[p] = q

    return maze

# Run
maze = generate_maze(40,80)

#output_notebook()
plot = figure(x_range = (0,1), y_range=(0,1), plot_height=410, plot_width = 810)
plot.axis.visible = False
plot.outline_line_color = '#ffffff'
plot.image([maze], x=0,y=0,dw=1,dh=1,palette =['#228B22','#ffffff'])
show(plot)
