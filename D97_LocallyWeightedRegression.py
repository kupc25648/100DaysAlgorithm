'''
Locally weighted regression is a very powerful non-parametric model used in statistical learning.

To explain how it works, we can begin with a linear regression model and ordinary least squares.

Given a dataset X, y, we attempt to find a linear model h(x) that minimizes residual sum of squared errors. The solution is given by Normal equations.
Linear model can only fit a straight line, however, it can be empowered by polynomial features to get more powerful models. Still, we have to decide and fix the number and types of features ahead.
Alternate approach is given by locally weighted regression.

Given a dataset X, y, we attempt to find a model h(x) that minimizes residual sum of weighted squared errors. The weights are given by a kernel function which can be chosen arbitrarily and in my case I chose a Gaussian kernel. The solution is very similar to Normal equations, we only need to insert diagonal weight matrix W.
What is interesting about this particular setup? By adjusting meta-parameter τ you can get a non-linear model that is as strong as polynomial regression of any degree.
And if you are interested, you can find an excellent explanation of what kernel really does in Andrew Ng’s Machine learning course.
This time the notebook contains interactive plot. You can adjust meta-parameter τ and watch in realtime its influence on the model. Have fun!

https://medium.com/100-days-of-algorithms/day-97-locally-weighted-regression-c9cfaff087fb
'''
import numpy as np
from ipywidgets import interact
from bokeh.plotting import figure, show, output_notebook
from bokeh.layouts import gridplot
from bokeh.io import push_notebook

# Algorithm
def local_regression(x0, X, Y, tau):
    # add bias term
    x0 = np.r_[1,x0]
    X = np.c_[np.ones(len(X)),X]

    # fit model: normal equations with kernel
    xw = X.T *  radial_kernel(x0, X, tau)
    beta = np.linalg.pinv(xw @ X) @ xw @ Y

    # predict value
    return x0 @ beta

def radial_kernel(x0, X, tau):
    return np.exp(np.sum((X-x0)**2, axis =1) / (-2* tau*tau))

# Data
n = 1000

# generate dataset
X = np.linspace(-3, 3 , num=n)
Y = np.log(np.abs(X**2-1) +0.5 )

# jitter X
X += np.random.normal(scale = 0.1, size =n)

# fit & plot model

def plot_lwr(tau):
    # prediction
    domain = np.linspace(-3,3, num= 300)
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]

    plot = figure(plot_width = 400, plot_height =400)
    plot.title.text = 'tau=%g' % tau
    plot.scatter(X,Y, alpha =0.3)
    plot.line(domain, prediction, line_width = 2, color= 'red')

    return plot

show(gridplot([
    [plot_lwr(10.), plot_lwr(1.)],
    [plot_lwr(0.1),plot_lwr(0.01)]
    ]))


def interactive_update(tau):
    model.data_source.data['y'] = [local_regression(x0, X, Y, tau) for x0 in domain]
    push_notebook()

    domain = np.linspace(-3, 3, num=100)
    prediction = [local_regression(x0, X, Y, 1.) for x0 in domain]

    plot = figure()
    plot.scatter(X, Y, alpha=.3)
    model = plot.line(domain, prediction, line_width=2, color='red')
    show(plot, notebook_handle=True)

#interact(interactive_update, tau=(0.01, 3., 0.01))
'''
Locally weighted regression is a very powerful non-parametric model used in statistical learning.

To explain how it works, we can begin with a linear regression model and ordinary least squares.

Given a dataset X, y, we attempt to find a linear model h(x) that minimizes residual sum of squared errors. The solution is given by Normal equations.
Linear model can only fit a straight line, however, it can be empowered by polynomial features to get more powerful models. Still, we have to decide and fix the number and types of features ahead.
Alternate approach is given by locally weighted regression.

Given a dataset X, y, we attempt to find a model h(x) that minimizes residual sum of weighted squared errors. The weights are given by a kernel function which can be chosen arbitrarily and in my case I chose a Gaussian kernel. The solution is very similar to Normal equations, we only need to insert diagonal weight matrix W.
What is interesting about this particular setup? By adjusting meta-parameter τ you can get a non-linear model that is as strong as polynomial regression of any degree.
And if you are interested, you can find an excellent explanation of what kernel really does in Andrew Ng’s Machine learning course.
This time the notebook contains interactive plot. You can adjust meta-parameter τ and watch in realtime its influence on the model. Have fun!

https://medium.com/100-days-of-algorithms/day-97-locally-weighted-regression-c9cfaff087fb
'''
import numpy as np
from ipywidgets import interact
from bokeh.plotting import figure, show, output_notebook
from bokeh.layouts import gridplot
from bokeh.io import push_notebook

# Algorithm
def local_regression(x0, X, Y, tau):
    # add bias term
    x0 = np.r_[1,x0]
    X = np.c_[np.ones(len(X)),X]

    # fit model: normal equations with kernel
    xw = X.T *  radial_kernel(x0, X, tau)
    beta = np.linalg.pinv(xw @ X) @ xw @ Y

    # predict value
    return x0 @ beta

def radial_kernel(x0, X, tau):
    return np.exp(np.sum((X-x0)**2, axis =1) / (-2* tau*tau))

# Data
n = 1000

# generate dataset
X = np.linspace(-3, 3 , num=n)
Y = np.log(np.abs(X**2-1) +0.5 )

# jitter X
X += np.random.normal(scale = 0.1, size =n)

# fit & plot model

def plot_lwr(tau):
    # prediction
    domain = np.linspace(-3,3, num= 300)
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]

    plot = figure(plot_width = 400, plot_height =400)
    plot.title.text = 'tau=%g' % tau
    plot.scatter(X,Y, alpha =0.3)
    plot.line(domain, prediction, line_width = 2, color= 'red')

    return plot

show(gridplot([
    [plot_lwr(10.), plot_lwr(1.)],
    [plot_lwr(0.1),plot_lwr(0.01)]
    ]))


def interactive_update(tau):
    model.data_source.data['y'] = [local_regression(x0, X, Y, tau) for x0 in domain]
    push_notebook()

    domain = np.linspace(-3, 3, num=100)
    prediction = [local_regression(x0, X, Y, 1.) for x0 in domain]

    plot = figure()
    plot.scatter(X, Y, alpha=.3)
    model = plot.line(domain, prediction, line_width=2, color='red')
    show(plot, notebook_handle=True)

#interact(interactive_update, tau=(0.01, 3., 0.01))
