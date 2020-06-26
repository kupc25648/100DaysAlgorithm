'''
It has been 35 years since Ken Perlin has discovered a technique today called Perlin noise to generate a fixed gradient noise to achieve a better looking textures in the famous movie Tron.

perlin noise: different frequencies
How Perlin noise works?
Look at the top left square at the picture. There are four corners, and each has defined a fixed 2D vector representing gradient, G¹, G², G³, G⁴. For any pixel P inside we define four vectors representing the difference between the P and each corner, V¹, V², V³, V⁴. Finally, we project gradients G onto vectors V and use bilinear interpolation to transform four numbers into one.
Each square on the picture contains 4-times more changes in gradient when compared to the previous square. As the number of changes increases, the output is more and more noisy.
When these 8 images with different frequencies are combined together using [for example] a weighted average, we get quite nice procedural textures.

perlin noise: weighted average & blue-white palette
Non-linear smoothing function and other tricks can be used to get more realistically looking textures. Fire, skies, fluids, landscapes, islands, mountains … Perlin noise and its successors like Simplex noise represent the very basic building block of procedurally generated textures.

https://medium.com/100-days-of-algorithms/day-88-perlin-noise-96d23158a44c
'''

import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.palettes import gray
from bokeh.layouts import layout

# Algorithm
def generate_gradient(seed = None):
    global gradient

    seed and np.random.seed(seed)
    gradient = np.random.rand(512,512,2)*2 - 1

def perlin_noise(size_x, size_y, frequency):
    global gradient

    # linear space by frequency
    x = np.tile(np.linspace(0, frequency, size_x, endpoint=False), size_y)
    y = np.repeat(np.linspace(0,frequency, size_y, endpoint = False), size_x)

    # gradient coordinates
    x0 = x.astype(int)
    y0 = y.astype(int)

    # local coordinate
    x -= x0
    y -= y0

    # gradient projections
    g00 = gradient[x0,y0]
    g10 = gradient[x0+1,y0]
    g01 = gradient[x0,y0+1]
    g11 = gradient[x0+1,y0+1]

    # fade
    t = (3 -2*x)*x*x

    # linear interpolation
    r = g00[:,0]*x + g00[:,1]*y
    s = g10[:,0]*(x-1)+g10[:,1]*y
    g0 = r+t*(s-r)

    # linear interpolation
    r = g01[:,0] * x + g01[:,1]*(y-1)
    s = g11[:,0] *(x-1) + g11[:,1] * (y-1)
    g1 = r+t*(s-r)

    # fade
    t = (3-2*y)*y*y

    # (bi)linear interpolation
    g = g0 + t * (g1-g0)

    # reshape
    return g.reshape(size_y, size_x)

def banded_perlin_noise(size_x, size_y, frequencies, amplitudes):
    image = np.zeros((size_y,size_x))

    for f, a in zip(frequencies, amplitudes):
        image += perlin_noise(size_x,size_y,f)*a

    image -= image.min()
    image /= image.max()

    return image

#perlin noise1
'''
generate_gradient()
plots = []

for frequency in [1, 2, 4, 8, 16, 32, 64, 128]:
    image = perlin_noise(200, 200, frequency)

    plot = figure(x_range=(0, 1), y_range=(0, 1), plot_width=200, plot_height=200)
    plot.axis.visible = False
    plot.toolbar_location = None
    plot.min_border = 0
    plot.image([image], x=0, y=0, dw=1, dh=1, palette=gray(256))

    plots.append(plot)

show(layout([plots[:4], plots[4:]]))
'''
#perlin noise2
generate_gradient(39320)

image = banded_perlin_noise(512, 512, [2, 4, 8, 16, 32, 64], [32, 16, 8, 4, 2, 1])

start = np.array([0x42, 0x92, 0xc6])
end = np.array([0xf7, 0xfb, 0xff])
palette = [
    "#%02x%02x%02x" % tuple(((1 - i) * start + i * end).astype(int))
    for i in np.linspace(0, 1, num=256)
]

plot = figure(x_range=(0, 1), y_range=(0, 1), plot_width=512, plot_height=512)

plot.axis.visible = False
plot.toolbar_location = None
plot.min_border = 0
plot.image([image], x=0, y=0, dw=1, dh=1, palette=palette)

show(plot)
