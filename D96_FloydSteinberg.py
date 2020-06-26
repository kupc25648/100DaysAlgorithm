'''
Floyd-Steinberg dithering is a truly magical technique. It is supposed to fool your eye and brain to make you think that you see more than there really is to be seen.

In general, dither is method to reduce color space of an image by adding an artificial noise. The key idea is that the amount of light in an area should remain about the same.

Floyd-Steinberg uses non-uniform distribution of quantization error to surrounding pixels. It means that the center pixel is rounded to 0 or 1. The residual error is then added to surrounding pixels.

All the three pictures you can find in this article were grayscaled and dithered. They all consist of only two-color noise. The rest is handled by your brain.
And if you want to see real masterpieces, try to google C64 artwork. The images usually have 4, 8 or 16 colors, but we percept much wider color scale just because of the dithering applied.
'''
import numpy as np
from PIL import Image
from requests import get
from bokeh.plotting import figure, show, output_notebook
from bokeh.layouts import layout
from bokeh.palettes import gray

# Algorithm
def image_dither(path, black='#000000', white = '#ffffff'):
    image_rgb  = read_image(path)
    image_gray = grayscale(image_rgb)
    image_bw = floyd_steinberg(image_gray)

    show(layout([[
        plot(image_gray, palette = gray(256)),
        plot(image_bw, palette=[black,white])
        ]]))

def floyd_steinberg(image):
    image = imgae.copy()
    distribution = np.array([7,3,5,1], dtype=float) / 16
    u = np.array([0,1,1,1])
    v = np.array([1,-1,0,1])

    for y in range(image.shape[0]-1):
        for x in range(image.shap[1]-1):
            value = np.round(image[y,x])
            error = image[y,x] - value
            image[y,x] = value
            image[y+u, x+v] += error*distribution

    image[:, -1] = 1
    image[-1, :] = 1

    return image

def grayscale(image):
    height, width, _ = image.shape

    image = np.array(image, dtype=np.float32) / 255
    image = image[:,:,0]*0.21 + image[:,:,1]*0.72 + image[:,:,2] *0.07

    return image.reshape(height, width)

def read_image(path, size = 400):
    if path.startswith('http://'):
        image = Image.open(get(path, sream=True).raw)
    else:
        image = Image.open(path)

    width, height = image.size
    width, height = size, int(size*height / width)
    image = image.resize((width, height), Image.ANTIALIAS)

    data = image.getdata()
    assert data.bands in [3,4], 'RGB or RGBA image is required'

    raw = np.array(data, dtype = np.unit8)

    return raw.reshape(height, width, data.bands)

def plot(image, palette):
    y,x = image.shape

    plot = figure(x_range=(0,x), y_range=(0,y), plot_width = x, plot_heigth = y)
    plot.axis.visible = False
    plot.toolbar_loacation = None
    plot.min_border = 0
    plot.image([np.flipud(image)], x =0, y=0, dw=x, dh=y, palette=palette)

    return plot

# RUN
URL = lambda name: 'https://raw.githubusercontent.com/coells/100days/master/resource/day 96 - %s.jpg' % (name,)
# URL = lambda name: './resource/day 96 - %s.jpg' % (name,)


