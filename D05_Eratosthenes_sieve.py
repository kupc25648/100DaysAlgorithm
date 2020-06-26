'''
Find prime number in n number

The sieve of Eratosthenes is a beautiful piece. It’s also surprisingly powerful and fast when segmented implementation is applied, on i7 CPU (single-threaded) you can generate prime numbers up to 10⁹ within 1 second.
In my implementation I used basic version (not segmented), only omitting even numbers in the array.

ps
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.

ps 2
Ever since Python 1.4, the slicing syntax has supported an optional third ``step'' or ``stride'' argument. For example, these are all legal Python syntax: L[1:10:2], L[:-1:1], L[::-1]. This was added to Python at the request of the developers of Numerical Python, which uses the third argument extensively. However, Python's built-in list, tuple, and string sequence types have never supported this feature, raising a TypeError if you tried it. Michael Hudson contributed a patch to fix this shortcoming.

For example, you can now easily extract the elements of a list that have even indexes:

>>> L = range(10)
>>> L[::2]
[0, 2, 4, 6, 8]

'''
import numpy as np

def eratosthenes(n):
    n = (n+1) >> 1
    i,j, p = 1,3, np.ones(n, dtype=np.int8)

    while i < n:
        if p[i]:
            p[j*j>>1::j] = 0
        i,j = i+1,j+2

    return p.sum()

print(eratosthenes(1000000))





