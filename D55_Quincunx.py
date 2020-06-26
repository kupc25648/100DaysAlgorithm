'''
https://medium.com/100-days-of-algorithms/day-55-quincunx-35265a2b7b35

'''
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import push_notebook
from time import sleep

# Algorithm
def update_quincunx(n, balls, buckets):
    x0, x1, y = balls.T

    #update buckets
    buckets[x1[y ==1] +n] +=1

    # update y
    y[:] -= 1
    y[y<=0] = n

    # update x
    x1[y==n] = 0
    x0[:] = x1
    x1[:] += np.random.choice([-1,1],len(x1))

def animate_quincunx(time, balls):
    x0,x1,y = balls.T

    # animate position
    x = x0 *(1-time) + x1 *time
    y = y *(1-time) + (y-1)*time

    return x,y

#  Initialization
N = 30 # quincunx size
# row ~ ball, column ~ (current_x, next_x, current_y)
balls = np.zeros((N - 1, 3), dtype=int)
balls[:, 2] = np.arange(N - 1, dtype=int) + N + 1
# bottom buckets
buckets = np.zeros(2 * N + 1, dtype=float)
buckets_x = np.arange(-N, N + 1)

# Plot
output_notebook()

# figure
plot = figure(plot_width=640, plot_height=420, tools='',
              x_range=(-N, N), y_range=(0, N))
plot.grid.visible = False
plot.yaxis.visible = False

# initial plot
x, y = animate_quincunx(1, balls)

vbar = plot.vbar(x=buckets_x, width=.8, bottom=0, top=buckets,
                 fill_alpha=.4, fill_color='red', line_color='red')
scatter = plot.scatter(x, y)

# show
handle = show(plot, notebook_handle=True)

for i in range(N * 5 * 30):
    time = round(i / 5 % 1, 1)

    # update bars
    if time == 0:
        update_quincunx(N, balls, buckets)
        vbar.data_source.data['top'] = buckets * .2

    # update scatter
    x, y = animate_quincunx(time, balls)
    scatter.data_source.data['x'] = x
    scatter.data_source.data['y'] = y

    push_notebook()
    sleep(.05)
