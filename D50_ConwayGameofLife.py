'''
I guess Conway’s game of life is so well-known that it hardly needs any introduction. Let’s just quickly repeat the rules:
if a cell is alive and has 2 or 3 neighbours, it stays alive
if a cell is dead and has 3 neighbours, it is reborn
otherwise it dies on underpopulation or overpopulation

On day 20 I briefly mentioned that Fourier transform can be used to apply 2D kernel on image. It’s still regular multiplication, just in 2D. And that’s how you can implement game’s update rule in 2 lines of code.
Today, the series is right in the middle. It has been 50 wonderful days and I’m looking forward to another 50. Thank you all for your support!

'''
import numpy as np
from scipy.fftpack import fft2, ifft2
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import push_notebook,export_png
from time import sleep

# Algorithm
def conway(size, prob = .5):
    # initialize game
    board = (np.random.rand(size,size) < prob).astype(int)

    #kernel
    kernel = np.zeros(board.shape)
    kernel[sorted([0,1,-1]*3), [-1,0,1]*3] =1
    kernel[0,0] = 10
    kernel = fft2(kernel)

    # update step
    def _conway():
        cell = ifft2(fft2(board)*kernel).real.round()
        board[:] = (cell==3) |(cell==12)|(cell==13)
        return board

    return _conway

# Plotting
count = 0
def animate(game, frames =30):

    frame = game()

    #output_notebook()
    plot = figure(x_range=(0, 1), y_range=(0, 1),
                  plot_width=frame.shape[1] * 5,
                  plot_height=frame.shape[0] * 5)
    plot.axis.visible = False
    image = plot.image([frame], x=0,y=0,dw=1,dh=1)

    handle = show(plot, notebook_handle=True)

    for i in range(frames):
        image.data_source.data['image'] = [game()]
        push_notebook()
        sleep(.05)

    export_png(plot, filename='plot'+count+'.png')
    count+=1


# Run
game = conway(50)
board = game()

# pulsar
index = [4, 5, 6, 10, 11, 12]
board[2, index] = 1
board[7, index] = 1
board[9, index] = 1
board[14, index] = 1
board[index, 2] = 1
board[index, 7] = 1
board[index, 9] = 1
board[index, 14] = 1

# glider
board[[30, 30, 30, 31, 32], [30, 31, 32, 30, 31]] = 1

# animate
animate(game, frames=200)
