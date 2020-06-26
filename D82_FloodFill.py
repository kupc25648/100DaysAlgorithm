'''
I remember when I was programming flood fill algorithm on my beloved Commodore 64 in BASIC, and later on 386 in Pascal. The program was so slow that you got flood fill with animation for free.
There are several versions of the algorithm and I have implemented one with scan-line.
Algorithm contains two loops, inner and outer. Outer loop repeatedly takes a position from stack and calls the inner loop.
Inner loop is called scan-line. It fills all the consecutive horizontal pixels from left to right. At each step the row directly above and the row directly below is checked on a change in color. If there is a change, scan-line stores this position onto stack for the outer loop.

The algorithm is very simple, yet smart, as it is able to fill areas “behind corner”.
When you need to implement your own version, you should consider horizontal and vertical scan-line. In case of very tall or very wide areas one version may be faster than the other.

https://medium.com/100-days-of-algorithms/day-82-flood-fill-ae03faa491c3
'''

import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.palettes import RdYlGn

# Algorithm
def flood_fill(x,y, canvas, color, bg=None):
    h,w = canvas.shape
    bg = canvas[y,x] if bg is None else bg
    stack = [(y,x)]

    while stack:
        i,j = stack.pop()
        if canvas[i,j] != bg:
            continue

        # find left boundary
        while j > 0 and canvas[i,j-1] == bg:
            j-= 1

        # scan right
        up, down = True, True
        while j < w and canvas[i,j] == bg:
            canvas[i,j] = color

            # detect color change above
            if i + 1 <h:
                if up and canvas[i+1,j] == bg:
                    stack.append((i+1,j))
                up = canvas[i+1,j] != bg

            # detect color change below
            if i > 0:
                if down and canvas[i-1, j ] == bg:
                    stack.append((i-1,j))
                down = canvas[i-1,j] != bg

            j +=1

# Run
n = 300
canvas = np.zeros((n,n), dtype = np.int8)

# draw random line
for i in range(10):
    x,y = np.random.randint(0,n,2)
    canvas[i & 1 and range(0,y) or range(y,n), x] = 1
    x,y = np.random.randint(0,n,2)
    canvas[y,i & 1 and range(0,x) or range(x,n)] = 1

plot = figure(x_range=(0,1), y_range=(0,1))
plot.image([canvas], x=0,y=0,dw=1,dh=1)
show(plot)

palette = RdYlGn[11]

# flood fill
for i in range(100):
    x, y = np.random.randint(0, n, 2)
    flood_fill(x, y, canvas, color=(i % len(palette)) + 2, bg=0)

plot = figure(x_range=(0, 1), y_range=(0, 1))
plot.image([canvas], x=0, y=0, dw=1, dh=1, palette=['#000000', '#ffffff'] + palette)
show(plot)
