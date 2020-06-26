'''
Perceptron is a beautiful statistical learning device for classification.
Perceptron is very simple to implement, it is an online algorithm, but what’s most important, it is a combination of mathematical function, learning algorithm and a proof of the algorithm correctness when applied on linearly separable sets.

ps try chaning data and runtime!!
'''
import numpy as np

#---------------------------------
#DATA
#---------------------------------
X = np.array([
    [0, 2, 1], [1, 0, 1], [1, 1, 1], [-1, 1, 1], [1, -1, 1]
])
Y = np.array([1, 1, 1, 0, 0])
W = np.zeros(3)

#---------------------------------
#ALGORITHM
#---------------------------------
def perceptron(x,w):
    return(x @ w >= 0).astype(int)

def train(x,y,w):
    for i in range(len(x)):
        # evaluate perceptron
        h = perceptron(x[i,:], w)
        # missclassification
        if h != y[i]:
            # positive sample
            if y[i] == 1:
                w += x[i,:]
            # negative sample
            else:
                w -= x[i,:]
    # evalate
    return perceptron(x,w)

for _ in range(10):
    h = train(X, Y, W)
    print('w=', W, 'acc=', np.mean(h == Y))

