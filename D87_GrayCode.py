'''
Gray code is a binary encoding such that two successive codes must differ only by a single bit.

There are many ways to generate the encoding. Knuth, for example, describes seven types: standard, balanced, complementary, long-run, nonlocal, monotonic and trend-free.

standard 10-bit Gray code
My implementation provides a standard code which has very nice visualization that might help to understand the construction. The image above contains the full 10-bit standard encoding, each code represented as a single column.

https://medium.com/100-days-of-algorithms/day-87-gray-code-cb1ccea5ced1
'''

import numpy as np
from bokeh.plotting import figure, show, output_notebook

# Algorithm
def gray_code(n):
    code = [0]*n
    i, parity = 0,0

    while i < n:
        yield code[::-1]

        i = parity
        parity ^= 1
        while i and not code[i-1]:
            i += 1

        if i < n:
            code[i] ^= 1

# Run

for code in gray_code(4):
    print(code)

# Plot
def plot_code(n):
    code = np.array(list(gray_code(n))).T

    plot = figure(x_range=(0, 1), y_range=(0, 1), plot_width=800, plot_height=200)
    plot.axis.visible = False
    plot.image([code], x=0, y=0, dw=1, dh=1, palette=['#ffffff', '#000000'])

    show(plot)

plot_code(10)
