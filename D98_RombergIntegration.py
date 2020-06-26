'''
Romberg’s method to find a definite integral combines two formulas, extended trapezoidal rule and Richardson extrapolation, to get a good approximation in relatively low number of steps.
Let’s explain how it all works without causing a serious headache.
The simplest way to find a definite integral of function f on interval (a, b) is to use a trapezoidal rule.

trapezoidal rule
It’s the left-most chart and you can see that the formula is merely an area of trapezoid.

definite integral estimates
You can also notice that there’s a certain error which can be improved using extended trapezoidal rule. Split interval (a, b) into two halves, apply trapezoidal rule onto each half and sum them up.

extended trapezoidal rule
It’s the chart in the middle. The formula is merely an area of two trapezoids.
The third plot contains another halving and even better estimate. We can go on and on until we are satisfied with the estimate error.
The problem is, the convergence in this way would be very slow. And here comes Richardson extrapolation to the rescue.
In Richardson extrapolation we take two bad estimates and combine them into a good one. The best explanation I’ve ever seen is definitely described in this Dilbert strip, check it out.
Dilbert Comic Strip on 2008-05-07 | Dilbert by Scott Adams
The Boss says, "Use the CRS database to size the market." Dilbert says, "That data is wrong." The Boss says, "Then use…
dilbert.com
However, unlike Dilbert we are lucky since we know error bound of each estimate.
In other words, if we are sure that one estimate is better that the other [e.g. due to smaller interval in extended trapezoidal rule], we also know in which direction should we expect the exact solution.

Richardson extrapolation
Finally, Romberg’s method builds a table of estimates with surprisingly accurate results.

Romberg integration
The first column contains results of extended trapezoidal rule, each row using twice as many splits as the row before. All the other values are results of Richardson extrapolation.
The diagonal contains the final estimates and each diagonal element gives about two more digits of precision. Hence the element at 5th row and 5th column gives an estimate of about 10 digits of accuracy.

https://medium.com/100-days-of-algorithms/day-98-romberg-integration-16d8626a1340
'''
import numpy as np
import sys

np.set_printoptions(precision=14, linewidth=120)

# Algorithm
def integrate( fn, a,b, steps=5, debug=False, exact = None):
    table = np.zeros((steps,steps), dtype = np.float64)
    pow_4 = 4 **np.arange(steps, dtype= np.float64)- 1

    # trapezodial rule
    h = (b-a)
    table[0,0] = h* (fn(a)+ fn(b)) /2

    for j in range(1, steps):
        h /= 2

        # extended trapzodial rule
        table[j,0] = table[j-1,0]/2
        table[j,0] += h*np.sum(fn(a+i*h) for i in range(1,2**j+1,2))

        # richardson extrapolation
        for k in range(1, j+1):
            table[j,k] = table[j,k-1]+ (table[j,k-1] - table[j-1,k-1]) / pow_4[k]

    # debug
    if debug:
        print(table, file= sys.stderr)
        if exact is not None:
            errors = ['%.2e' % i for i in np.abs(table.diagonal() - exact)]
            print('abs. error:', errors, file=sys.stderr)

    return table[-1,-1]

#integral[0, 1] of e^(-x^2)
integrate(lambda x: np.exp(-x * x), 0, 1, debug=True, exact=0.746824132812427)
