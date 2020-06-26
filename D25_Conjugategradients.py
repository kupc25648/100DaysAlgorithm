'''
When you need to solve a system of linear equations, conjugate gradients present a fast way.

The idea is quite clever. Take a function F=L2(X’, X⁰)², that is a squared L2 norm of [not necessarily correct] solution X’ and the real solution X⁰. The function has parabolic shape and under the best scenario its minimum is located at origin (which would also be the solution). In such case, we may travel from X’ perpendicularly to each axis, one by one, to arrive into X⁰.
While this is not usually the case, real scenarios are not that much different. In contrast to the best scenario, conjugate gradients travel perpendicularly to eigenvectors which results in the same effect as described above.
Just remember that your matrix has to be positive semidefinite. If that’s not the case, use transformation (A’A)x=(A’b). That will handle overdetermined and underdetermined systems, too.

'''
import numpy as np

def conjugate_gradients(A,b):
    x = np.zeros(A.shape[1])
    residuals = b-A@x
    direction = residuals
    error = residuals.T@residuals

    # step along conjugate directions
    while error > 1e-8:
        x += direction * error / (direction.T@A@direction)
        residuals = b-A@x
        error1 = error
        error = residuals.T@residuals
        direction = residuals + error/error1*direction

    return x

A = np.random.rand(3, 3)
b = np.random.rand(3)
print('A')
print(A)
print('b')
print(b)
print('x')
# make system positive semidefinite
print(conjugate_gradients(A.T @ A, A.T @ b))
