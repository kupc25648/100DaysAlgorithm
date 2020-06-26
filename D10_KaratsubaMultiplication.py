'''
When you multiply two numbers on the paper, you probably follow the good old [and naive] way. Using Master theorem it is pretty straightforward to show that this algorithm requires O(n²) multiplications. But there’s actually very clever way to speed the things up.

                        A    B
                    x   C    D
                ---------------
                       AD   BD
                   AC  BC
                ---------------
                AC   AD+BC  BD
                ===============

The middle part of table contains expression AD+BC which requires two O(n²/4) multiplications and one O(n) addition. And here is Karatsuba’s idea:

                (A+B)(C+D)-AC-BD = AD + BC

Since we already have AC and BD anyways, we can use only one O(n²/4) multiplication and four O(n) additions/subtractions to reach overall complexity O(n^log2(3)).

Why don’t we use Karatsuba as replacement of the naive way? Well, for us a subtraction seems to be more difficult, non-intuitive and error-prone than addition. However, for computer there’s no difference.

I wish we could spend way more time on this topic. At least I’ll provide some pointers to general theory and advanced algorithms: polynomial rings, number theoretic transform, Toom-Cook, Schonhage-Strassen.


'''
from itertools import zip_longest as zip_longest

def add(x, y):
    z, carry = [], 0
    for r, s in zip_longest(x, y, fillvalue=0):
        t = r + s + carry
        carry = t // 10
        z.append(t % 10)
    if carry:
        z.append(carry)
    return z
def sub(x, y):
    z, carry = [], 0
    for r, s in zip_longest(x, y, fillvalue=0):
        t = r - s + carry
        carry = t // 10
        z.append(t % 10)
    return z
def karatsuba(x, y):
    # ensure same length
    while len(x) < len(y):
        x.append(0)
    while len(x) > len(y):
        y.append(0)
    # length and split
    n = len(x)
    n_2 = (n + 1) >> 1
    # trivial case
    if n == 1:
        return add([x[0] * y[0]], [])
    # split
    x0, x1 = x[:n_2], x[n_2:]
    y0, y1 = y[:n_2], y[n_2:]
    # karatsuba algorithm
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1, y1)
    z2 = karatsuba(add(x0, x1), add(y0, y1))
    z2 = sub(sub(z2, z0), z1)
    z = add(z0, [0] * (n_2 << 1) + z1)
    z = add(z, [0] * n_2 + z2)
    return z

x, y = '3', '5'
x = list(map(int, reversed(x)))
y = list(map(int, reversed(y)))
z = karatsuba(x, y)
''.join(map(str, reversed(z)))




print(z)
