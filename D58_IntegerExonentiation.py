'''
Fast integer exponentiation is very important in cryptography. I have used Python built-in function pow() for RSA implementation, but it’s good to know what’s hidden inside.
When computing x^y, base x is repetitively squared to get powers x¹, x², x⁴, x⁸, … Since exponent y is an integer, it can be expressed as binary number which tells us what powers have to be multiplied.
For example, x⁹⁹ = x¹x²x³²x⁶⁴.
We are usually limited to modular arithmetic or fixed point arithmetic, so we are allowed to say that the algorithm runs in O(log y) time.
'''
import numpy as np
# Algorithm
def _power(x,y, identity=None, op=None):
    p = identity

    while y:
        p = op(p,x) if y & 1 else p
        x = op(x,x)
        y >>= 1

    return p

def power(x,y):
    return _power(x,y, identity= type(x)(1), op=type(x).__mul__)

def mod_power(x,y,n):
    return _power(x,y, identity=1, op = lambda a,b: (a*b)%n)

def matrix_power(x,y):
    return _power(x,y, identity= np.eye(x.shape[0], dtype=x.dtype), op=np.ndarray.__matmul__)

# Run

print(power(2.,100))
