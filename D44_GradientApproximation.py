'''
 == differential of function(x)
If you had to vote, what would you consider as the most important debugging tool ever? Without hesitation, gradient approximation would be my first choice.

Either was it neural network training or any other multivariate function optimization, it was very difficult due to bugs in derivatives. And there always were some bugs.
In my experience, it took 30 minutes to implement the task, and it took 6–12 more hours to make it work. Approximate gradient was super useful to identify the spots to be fixed.
It’s hard to describe how easy the life is with TensorFlow or Theano.
'''
import numpy as np
# Algorithm
def gradient(fun,x,delta=1e-4):
    x = np.asfarray(x)
    grad = np.zeros(x.shape, dtype = x.dtype)

    for i,t in np.ndenumerate(x):
        x[i] = t+delta
        grad[i] = fun(x)
        x[i] = t- delta
        grad[i] -= fun(x)
        x[i] = t

    return grad/(2*delta)
# Run
def function(x):
    return 3 * x**2 + 2 * x + 1

print(gradient(function, [1]))
