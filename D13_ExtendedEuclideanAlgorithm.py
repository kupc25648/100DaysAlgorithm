'''
One of the most fundamentals algorithms in number theory is extended euclidean algorithm. It’s purpose is to solve Diophantine equation


ax + by = GCD(a, b)
Seriously, every programmer must know this one, I don’t even know what else to say.

ps1. extended euclidean algorithm find  'greatest common divisor' and integers to multiply x,y

https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm

ps2. Diophantine problems have fewer equations than unknown variables and involve finding integers that work correctly for all equations.

https://en.wikipedia.org/wiki/Diophantine_equation
'''

def gcd(x,y):
    u0, v0 = 1,0
    u1, v1 = 0,1
    while y:
        q = x//y
        u0, u1 = u1, u0-q*u1
        v0, v1 = v1, v0-q*v1
        x, y   = y , x%y
    return x ,u0 ,v0

print(gcd(2*3*7*9*11, 6*12*13))
