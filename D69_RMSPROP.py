'''
What about some machine learning related topic, today? Rmsprop is a gradient-based optimization technique proposed by Geoffrey Hinton at his Neural Networks Coursera course.

https://medium.com/100-days-of-algorithms/day-69-rmsprop-7a88d475003b
'''
import numpy as np
from bokeh.plotting import figure, show, output_notebook

# Algorithm
def gradient_descent(F, dF, x, steps =100, lr=0.001):
    loss = []
    for _ in range(steps):
        dx = dF(x)
        x -= lr *dx
        loss.append(F(x))

    return x, loss

def rmsprop(F, dF, x, steps=100, lr=0.001, decay=.9, eps = 1e-8):
    loss = []
    dx_mean_sqr = np.zeros(x.shape, dtype = float)

    for _ in range(steps):
        dx = dF(x)
        dx_mean_sqr = decay*dx_mean_sqr+(1 - decay) * dx **2
        x -= lr*dx/(np.sqrt(dx_mean_sqr)+eps)
        loss.append(F(x))

    return x, loss

def rmsprop_momentum(F, dF, x, steps=100, lr=0.001, decay=.9, eps = 1e-8, mu=.9):
    loss =[]
    dx_mean_sqr = np.zeros(x.shape, dtype=float)
    momentum = np.zeros(x.shape, dtype=float)

    for _ in range(steps):
        dx = dF(x)
        dx_mean_sqr = decay*dx_mean_sqr+(1 - decay)*dx**2
        momentum = mu*momentum + lr * dx / (np.sqrt(dx_mean_sqr)+eps)

        x -= momentum
        loss.append(F(x))

    return x, loss

# Function
def F(x):
    residual = A @ x - np.eye(len(A), dtype=float)
    return np.sum(residual ** 2)
def dF(x):
    return 2 * A.T @ (A @ x - np.eye(len(A), dtype=float))
A = np.array([
    [2, 5, 1, 4, 6],
    [3, 5, 0, 0, 0],
    [1, 1, 0, 3, 8],
    [6, 6, 2, 2, 1],
    [8, 3, 5, 1, 4],
], dtype=float)

# Optimization
X, loss1 = gradient_descent(F, dF, A * 0, steps=300)
(A @ X).round(2), loss1[-1]
X, loss2 = rmsprop(F, dF, A * 0, steps=300)
(A @ X).round(2), loss2[-1]
X, loss3 = rmsprop_momentum(F, dF, A * 0, steps=300)
(A @ X).round(2), loss3[-1]

output_notebook()

plot = figure()
plot.line(x=range(len(loss1)), y=loss1, color='steelblue', legend='gd')
plot.line(x=range(len(loss2)), y=loss2, color='green', legend='rmsprop')
plot.line(x=range(len(loss3)), y=loss3, color='red', legend='rmsprop+momentum')

show(plot)
