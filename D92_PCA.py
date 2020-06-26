'''
Principal Component Analysis [PCA] is incredibly useful when you need [among others] to visualise high-dimensional data. It’s also very simple to implement, but requires plenty of work beforehand.
A friend of mine, Pavel, has complained that I often don’t dive deep into the topic. And I hope that PCA will satisfy even such an eager mind.
Let’s say we have a bunch of multi-dimensional data stored in a matrix X. Each row represents a sample, and each column represents a variable.
We say that two variables are correlated if there is a linear relationship in between them. Their scatterplot may look similarly to this one.

strongly correlated data
On the other hand, the variables on the next scatterplot are uncorrelated.

uncorrelated data
While the first plot seems to be more useful, PCA takes the advantage of the second one.

To study these dependencies between variables, we use a covariance matrix. When data has no correlated variables, all off-diagonal elements of the Σ matrix must be zero.
And as a side note, for any covariance matrix Σ there exists matrix V called eigenvector matrix and diagonal matrix Λ called eigenvalue matrix, such that the expressions above hold. Both matrices are unique except for the order of columns.
How does PCA work?

PCA normalizes the data matrix X to zero mean and then multiples by some matrix P. The multiplication is actually linear transformation of data. That means if we choose P very carefully, we can either rotate, scale or project the data into vector subspace.

Say we have applied PCA to data matrix X and received another matrix Z. What do we know about Σ matrix of Z?

There is a [quadratic] relationship between both covariance matrices of X and Z! And what happens if we choose P to be eigenvector matrix V defined above?

This means that the projected matrix Z is uncorrelated and its variables have no longer any kind of linear dependency [because Λ is diagonal matrix].
Wait! What just happened?
Let me show you an example and another point of view.

first and second principal components
PCA finds the data mean and principal components. In case of 2D data the principal components are axes x and y rotated to the point that the data became uncorrelated.
There is also another term that is often used. We say that the first principal component is a rotation of x-axis to maximize the variance of the data projected onto it.

PCA: data with maximum variance
Is PCA just a rotation of coordinate systems? Why on earth should this have any use?
If you look at the code below, I generate a set of binary vectors, and each vector has 30 dimensions. Is there any linear relationship in the data?
X = np.random.rand(90, 30)
X[:30, :] = X[:30, :] < ([.4] * 10 + [.1] * 10 + [.1] * 10)
X[30:60, :] = X[30:60, :] < ([.1] * 10 + [.4] * 10 + [.1] * 10)
X[60:, :] = X[60:, :] < ([.1] * 10 + [.1] * 10 + [.4] * 10)
Well, there is, because I generated the data to have one [while it may not be immediately obvious]. But in practice we do not know and would like to find out.
In advance, each vector I generated sits in a corner of 30D unit cube and human brain can’t sort information of this kind.
When we apply PCA to this data, all the variables become uncorrelated and the dimensions now hold as much information as possible independently of one another and in descending order.
Also projection from 30D to 2D is now trivial — simply remove 28 trailing variables [because variables are independent] and plot the graph.

PCA: 2D visualization of 30D data
As you can see, the data projected from 30D onto 2D still contain the key information that I generated vectors of the same color to be close to each other. And each set of 30 vectors forms a nice cluster [but I need to say the reason behind is because I generated the data carefully to make such clusters].
I wish a had more time. The last sample, corners of 30D unit cube, moves us to the most interesting topic, latent factor analysis, which offers another view on PCA and more advanced techniques.
Anyways, how to implement PCA?

normalize X to zero mean
calculate covariance matrix Σ
find [orthonormal] eigenvectors of Σ
After a ton of paperwork, the algorithm is only on few lines of code. And you know, sometimes typing the code itself is the easiest part of all the work.


https://medium.com/100-days-of-algorithms/day-92-pca-bdb66840a8fb
'''
import numpy as np
from bokeh.plotting import figure, show, output_notebook

# Algorithm
def PCA(X, n_component):
    # normalize to zero mean
    mu = X.mean(axis = 0)
    X = X- mu

    # eigenvectors of covariance matrix
    sigma = X.T @ X
    eigvals, eigvecs = np.linalg.eig(sigma)

    # pricipal component
    order = np.argsort(eigvals)[::-1]
    components = eigvecs[:, order[:n_component]]

    # projection
    Z = X @ components

    # result
    return Z, components

# 2D data and principal component
# generate points
x = np.linspace(0,13,num =10)
y = x +np.sin(x) - np.cos(x)

# 2D data
X = np.c_[x,y]

# PCA
projection, components = PCA(X, n_component=2)

# Principal component
print(components)

# Convariance matrix of projected data
print((projection.T @ projection).round(3))

# prepare plot data
mean = np.mean(X, axis=0)
extent = projection.min(), projection.max()
angle = np.arctan(components[1]/components[0]) + np.pi *(components[0] < 0)

# plot original data & principal component

# plot original data & principal components
'''
plot = figure()

plot.scatter(x, y)
plot.ray(*mean, length=0, angle=angle[0], line_width=2, line_color='red')
plot.ray(*mean, length=0, angle=angle[1], line_width=2, line_color='green')

show(plot)

# plot projected data
plot = figure(x_range=extent, y_range=extent)
plot.scatter(projection[:, 0], projection[:, 1])
show(plot)

'''
# generate binary vectors
X = np.random.rand(90, 30)
X[:30, :] = X[:30, :] < ([.4] * 10 + [.1] * 10 + [.1] * 10)
X[30:60, :] = X[30:60, :] < ([.1] * 10 + [.4] * 10 + [.1] * 10)
X[60:, :] = X[60:, :] < ([.1] * 10 + [.1] * 10 + [.4] * 10)

# define 3 classes
Y = ['red'] * 30 + ['green'] * 30 + ['blue'] * 30
# PCA
projection, _ = PCA(X, n_component=2)
# plot projected data: 30D -> 2D
plot = figure()
plot.scatter(projection[:, 0], projection[:, 1], color=Y)
show(plot)
