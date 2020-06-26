'''
Spiral matrix is an old toy algorithm. A funny way to implement the spiral would be to fill the top row in and rotate the matrix to unfold the sequence.

Fortunately, rotations and symmetries are in close relationship and any rotation can be expressed using point and line symmetry or using two line symmetries, which is our case. All we need is to flip the matrix horizontally and transpose.
'''

def spiral(n):
    matrix = [range(i * n + n)[-n:] for i in range(n)]
    X, C, R = {}, count(1), matrix
    while R:
        X.update(zip(R[0], C))
        R = list(zip(*[i[::-1] for i in R[1:]]))
    return [[X[j] for j in i] for i in matrix]

for i in spiral(5):
    print('\t'.join(map(str, i)))



