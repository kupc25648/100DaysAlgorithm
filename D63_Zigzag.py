'''
Zig-zag scan of a matrix is useful when you transform your 2D data between domains and the transformation tends to accumulate information into top left corner.

https://medium.com/100-days-of-algorithms/day-63-zig-zag-51a41127f31
'''
import numpy as np

# Algorithm
def zig_zag_index(k,n):
    # upper side interval
    if k >= n*(n+1)//2:
        i,j = zig_zag_index(n*n-1-k,n)
        return n-1-i, n-1-j
    # lower side of interval
    i = int((np.sqrt(1+8*k)-1)/2)
    j = k-i*(i+1)//2
    return (j,i-j) if i&1 else(i-j,j)

def zig_zag_value(i,j,n):
    # upper side of interval
    if i+j >=n:
        return n*n-1-zig_zag_value(n-1-i,n-1-j,n)
    # lower side of interval
    k = (i+j)*(i+j+1)//2
    return k+i if (i+j)&1 else k+j
# Index to Value
n =10
M = np.zeros((n,n), dtype = int)
for i in range(n):
    for j in range(n):
        M[i,j] = zig_zag_value(i,j,n)

print(M)
# Value to Index
n =10
M = np.zeros((n,n), dtype = int)
for k in range(n*n):
    M[zig_zag_index(k,n)] = k

print(M)
