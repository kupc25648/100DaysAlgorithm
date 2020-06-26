'''
I’ve already spent days 10 and 20 on multiplication algorithms, but I couldn’t resist this one. The first reason was that I actually never implemented Strassen algorithm and the second that the algorithm is intriguing.

When you look closely at the expressions Strassen discovered, it’s so hard to comprehend. I spend a lot of time on math and regardless of topic difficulty, there’s always intuition and formal expression behind any idea. Strassen’s expressions, however, completely lack any intuition and I can’t imagine how could he possibly make the discovery?

Unfortunately, the algorithm was unlucky. After its discovery it was rarely used due to concerns about loss of precision and it took many years to prove the concerns were false. Today it has become completely obsolete due to work of Mr. Kazushige Goto and his extraordinary skill to develop highly optimized code on superscalar CPUs.

https://en.wikipedia.org/wiki/Strassen_algorithm
'''
import numpy as np

def strassen(A,B):
    k = A.shape[0] // 2
    if k == 0:
        return A * B
    A11, A12 = A[:k, :k], A[:k, k:]
    A21, A22 = A[k:, :k], A[k:, k:]
    B11, B12 = B[:k, :k], B[:k, k:]
    B21, B22 = B[k:, :k], B[k:, k:]

    T1 = strassen(A11 + A22, B11 + B22)
    T2 = strassen(A21 + A22, B11)
    T3 = strassen(A11, B12 - B22)
    T4 = strassen(A22, B21 - B11)
    T5 = strassen(A11 + A12, B22)
    T6 = strassen(A21 - A11, B11 + B12)
    T7 = strassen(A12 - A22, B21 + B22)

    C = np.zeros(A.shape, dtype=A.dtype)
    C[:k, :k] = T1 + T4 - T5 + T7
    C[:k, k:] = T3 + T5
    C[k:, :k] = T2 + T4
    C[k:, k:] = T1 - T2 + T3 + T6

    return C

X = np.random.randint(0, 10, (8, 8))
Y = np.random.randint(0, 10, (8, 8))
print(strassen(X, Y))
