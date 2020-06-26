'''
Gram-Schmidt orthogonalization is a method used in linear algebra to produce an orthogonal [or orthonormal] base that generates the same vector space as a linear span of a given set of vectors.
The algorithm is easy to understand if you are familiar with linear algebra. If you are not, here’s an intuitive explanation.
It’s right noon and Sun is at the highest point on the sky. There is a column in front of you throwing a shadow on the floor. The shadow indicates that the column is not perpendicular to the floor. Therefore you slightly push the column until shadow disappears.
In terms of linear algebra:
floor ~ vector space
shadow ~ projection
perpendicular ~ orthogonal
pushing until shadow disappears ~ Gram-Schmidt process
Gram-Schmidt also gives us QR decomposition for free. It is a process of decomposing matrix X into a product of two matrices, X = QR, where Q is an orthogonal matrix and R is upper triangular matrix.

https://medium.com/100-days-of-algorithms/day-66-gram-schmidt-ed282b9b4ef2
'''

import numpy as np

# Algorithm

def gram_schmidt(X):
    O = np.zeros(X.shape)

    for i in range(X.shape[1]):
        # orthogonalization
        vector = X[:,i]
        space = O[:,:i]
        projection = vector @ space
        vector = vector - np.sum(projection * space, axis=1)

        # normalization
        norm = np.sqrt(vector@vector)
        vector /= abs(norm) < 1e-8 and 1 or norm

        O[:,i] =vector

    return O

# Run
# 6 column vectors in 4D, only 3 are independent
vectors = np.array([
    [1, 1, 2, 0, 1, 1],
    [0, 0, 0, 1, 2, 1],
    [1, 2, 3, 1, 3, 2],
    [1, 0, 1, 0, 1, 1]
], dtype=float)

orthonormal = gram_schmidt(vectors)
#print(orthonormal)
#print(orthonormal.T @ orthonormal)

# QR decomposition
matrix = np.array([
    [1, 1, -1],
    [1, 2, 1],
    [1, 3, 0]
], dtype=float)
Q = gram_schmidt(matrix)
print(Q)

R = Q.T @ matrix
print('______________________________________________')
print(R)
print('______________________________________________')
print(Q@R)
