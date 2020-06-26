'''
Let’s say we want to find roots of the polynomial, e.g. x⁵+x⁴+x³+x²+x+1.
While there’s no analytical solution for higher order polynomials, numerical solution is just an application of linear algebra. All we need is to construct a matrix whose characteristic polynomial is the one we are solving.

0  0  0  0  -1
1  0  0  0  -1
0  1  0  0  -1
0  0  1  0  -1
0  0  0  1  -1

To get the roots we then find eigenvalues of the matrix.

FINDING ROOTS OF POLYNOMIAL WITH EIGEN
http://web.mit.edu/18.06/www/Spring17/Eigenvalue-Polynomials.pdf
'''

import numpy as np

'''
*coeffs of
x⁵+x⁴+x³+x²+x+1
is
1, 1, 1, 1, 1, 1
'''


def roots(*coeffs):
    matrix = np.eye(len(coeffs) - 1, k=-1)
    matrix[:,-1] = np.array(coeffs[:0:-1]) / -coeffs[0]
    return np.linalg.eigvals(matrix)


for i in range(len(roots(1, 1, 1, 1, 1, 1))):
    print(roots(1, 1, 1, 1, 1, 1)[i])
