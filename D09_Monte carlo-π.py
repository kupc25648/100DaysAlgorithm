'''
I guess I’ll introduce more the one randomised algorithm in this series, and that’s not only because I love probabilistic approach. Randomised simulation is often the best/only way to solve otherwise intractable problems.

if you are mathematician, excuse my sloppy wording; randomised simulation should be understood as a random sampling from space of simulations under given distribution

How can we estimate π if the only tool we have at disposal is a good random number generator? When we choose a random coordinate (x, y) in range (-1, 1) and each point has equal chance to be chosen, the probability to hit a circle with unit radius is

x,y = U(-1,1)
p((x**2)+(y**2)<=1) = pi/4

Having sufficiently large set of points [and a good generator] we can get as close as we want according to Chebyshev’s inequality.

------------------------------------------
https://en.wikipedia.org/wiki/Chebyshev%27s_inequality

------------------------------------------
numpy.random.rand(d0, d1, ..., dn)
Random values in a given shape.

Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).

Parameters:
d0, d1, …, dn : int, optional
The dimensions of the returned array, should all be positive. If no argument is given a single Python float is returned.
------------------------------------------
numpy.sum(arr, axis, dtype, out) : This function returns the sum of array elements over the specified axis.

Parameters :
arr : input array.
axis : axis along which we want to calculate the sum value. Otherwise, it will consider arr to be flattened(works on all the axis). axis = 0 means along the column and axis = 1 means working along the row.
out : Different array in which we want to place the result. The array must have same dimensions as expected output. Default is None.
initial : [scalar, optional] Starting value of the sum.

Return : Sum of the array elements (a scalar value if axis is none) or array with sum values along the specified axis.
------------------------------------------



'''
import numpy as np

def pi(n, batch = 10):
    t =0
    for i in range(n//batch):
        p = np.random.rand(batch,2)
        p = (p*p).sum(axis =1)
        t += (p<=1).sum()
    return 4*t/n

print(pi(10**8))




