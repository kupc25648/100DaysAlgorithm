'''
Logistic regression is a regression model used for data classification. The model is very simple since, in fact, it is a linear classifier.
However, when you start to explore your data, the simplest model is a good spot to start at.
It is easy to program, fast to train and the model is explanatory which means that the model tells you what influence each feature has on the dependent variable.

In advance, input data can be manually extended by polynomial features and logistic regression can become quite useful non-linear classifier that requires almost no assumptions about the data.
'''

import numpy as np
from bokeh.plotting import figure, show, output_notebook

# Algorithm
def logistic_regression(X, Y, W, lr =0.001, steps=1000):
    m = len(Y)
    sigmoid = lambda z:1 / (1+np.exp(-z))

    for _ in range(steps):
        # prediction
        hypothesis = sigmoid(X @ W)
        # fix overflow & underflow
        hypothesis = np.clip(hypothesis, 1e-5, 1-1e-5)
        # loss function, gradient, training
        loss = -1/m * (Y@np.log(hypothesis) + (1-Y)@np.log(1-hypothesis))
        gradient = 1/m * (X.T@(hypothesis-Y))
        W -= lr *gradient

    # current loss and prediction
    return loss, sigmoid(X @ W)

# Data
n = 10000
# random value
x_ , y_ = np.random.rand(2,n)
# polynomial coefficient
X = np.c_[np.ones(n), x_, y_, x_**2, y_**2]
# Y: target values
Y = (x_ - .5 <= (y_ - .5)**2)*1
# weights
W = np.zeros(5)

# Training classification model
for _ in range(10):
    loss, H = logistic_regression(X,Y,W,lr=5., steps=1000)
    print(loss)

print('accuracy', np.mean(Y == H.round()))
print('weights', W)

# plot

output_notebook()

palette = ['steelblue', 'red', 'lightgreen']
color = [palette[i] for i in (Y + H.round()).astype(int)]

plot = figure()
plot.circle(x_, y_, line_color='#c0c0c0', fill_color=color, alpha=.6, size=8)

show(plot)
