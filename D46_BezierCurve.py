'''
Bézier curve is a simple and smooth curve in between two points.

Degree-n Bézier is using parameter t in range [0, 1] and n+1 fixed control points to evaluate the curve. And there’s a beautiful recursive definition that brings intuition of how it works.

For example, for Cubic Bézier we define 4 initial control points and ask for point at the curve at time t. The 4 points form 3 lines and using parameter t we find a new point at each line.

P**3 = {P0,P1,P2,P3}
P**2 = {P0=P0,1(t),P1=P1,2(t),P2=P2,3(t)}
P**1 = {P0=P0,1(t),P1=P1,2(t)}
P**0 = P0,1(t)

We get 3 brand new control points. But, hey! Quadratic Bézier is defined by 3 points. To step further, these 3 points form 2 lines and we get 2 new control points.
Cool, Linear Bézier is defined by 2 control points. And the point we get at this final step lies at the original cubic at time t.
If you think about this process, you may notice a disadvantage. The curve is easy to be controlled at the endpoints (t close to 0 or 1), but it is somewhat more difficult in the middle.
Its derivative is not constant, hence it tends to “speed up” and “slow down” which may not always be desirable.

'''
import numpy as np
import scipy.special
from bokeh.plotting import figure, show, output_notebook

# Algorithm
def bezier(points, steps=100):
    n = len(points)
    b = [scipy.special.binom(n-1,i) for i in range(n)]
    r = np.arange(n)

    for t in np.linspace(0,1,steps):
        u = np.power(t,r) * np.power(1-t,n-r-1)*b
        yield t,u@points
# Plot
point = np.array([[0, 0], [0, 1], [1, 1], [1, 0]] * 4)
plot = figure()
for i in range(3, 14):
    curve = np.array([p for _, p in bezier(point[:i])])
    color = tuple(np.random.randint(0, 256, 3))
    plot.line(curve[:, 0], curve[:, 1], color=color)
show(plot)
