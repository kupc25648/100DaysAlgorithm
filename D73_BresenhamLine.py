'''
https://medium.com/100-days-of-algorithms/day-73-bresenhams-line-4d6a28e9dfef
'''
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.palettes import Set3_12


# Algorithm
def bresenham(x0, y0, x1, y1, color, canvas):
    # swap major and minor axis
    if abs(y0 - y1) > abs(x0 - x1):
        x0, y0, x1, y1 = y0, x0, y1, x1
        canvas = canvas.T

    # swap x-axis direction
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0

    # initialize
    dx, dy = abs(x0 - x1), abs(y0 - y1)
    dz = 1 if y0 <= y1 else -1
    p = 2*dy - dy

    # draw
    while x0 <= x1:
        canvas[y0, x0] = color

        if p > 0:
            p -= 2*dx
            y0 += dz

        p += 2*dy
        x0 += 1

# Plot
def plot(canvas):
    w, h = canvas.shape

    plot = figure(x_range = (0, w-1), y_range=(0, h-1))
    plot.grid.visible = False
    plot.axis.visible = False
    image = plot.image([canvas], x=0, y=0, dw=w-1, dh=h-1, palette=['#000000']+ Set3_12)

    show(plot)

# Run1
'''
n =50
canvas = np.zeros((n,n), dtype = int)
m = n // 2
bresenham(m, m, n-1, m+10, 1, canvas)
bresenham(m, m, n-1, m-10, 2, canvas)
bresenham(m, m, m+10, n-1, 3, canvas)
bresenham(m, m, m+10, 0, 4, canvas)
bresenham(0, m+10, m, m, 5, canvas)
bresenham(0, m-10, m, m, 6, canvas)
bresenham(m-10, n-1, m, m, 7, canvas)
bresenham(m-10, 0, m, m, 8, canvas)
bresenham(m, m, m, m, 0, canvas)
plot(canvas)
'''
# Run2
'''
n = 100
canvas = np.zeros((n, n), dtype=int)

for i in range(10):
    x = np.random.randint(0, n, 4)
    bresenham(*x, i + 1, canvas)
plot(canvas)
'''
# Run3
n = 200
canvas = np.zeros((n, n), dtype=int)

for i in range(n):
    bresenham(0, 0, i, n - 1, i % 10 + 1, canvas)
    bresenham(0, 0, n - 1, i, i % 10 + 1, canvas)
plot(canvas)
