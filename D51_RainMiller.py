'''
A friend of mine asked me to implement RSA. Let’s implement RSA from scratch, then. And since RSA encryption requires more than one algorithm, I will spread it into several days.
In this article I will dig deep but still not deep enough. I’m sorry if the explanation is not crystal clear or sufficient. I need to assume you are comfortable with basics of algebra. If you are not, just say loudly, “bad, bad math”, and read only the first and the last paragraphs.
disclaimer: do not consider my code to be secure; do not consider any cryptography coming from non-experts to be secure; you should never implement any kind of cryptography on your own nor should you interfere with your security in any way; this series is just for fun and as such should be taken
First of all, I will need large prime numbers. To find some, I will implement Rabin-Miller which is what is called a strong pseudoprime test.
That’s a probabilistic test that always identifies a prime number, but sometimes incorrectly denotes a composite as prime. Fortunately, the chance to make a mistake can be decreased by repeating the test.
How does is work? Remember the famous Fermat’s little theorem.

https://miro.medium.com/max/524/1*9AB7D5jJAXvYN8EYchFOng.png

For a prime p the congruence forms a finite field and holds for any a < p. This has a consequence for a square roots of unity.

https://miro.medium.com/max/808/1*6MgPldV7Erjxv4V39UuNDQ.png

If x² is congruent to 1, then x+1 or x-1 has to be divisible by p which implies that x must either be 1 or -1. Hence for prime p there exists no non-trivial (other than 1 or -1) square root of unity.
Rabin-Miller searches for such roots. It starts by a^(p-1) and repetitively takes the square roots. If any non-trivial root is found, p is composite.
The recipe as described would be difficult to implement. But it can be implemented in a probabilistic way. First, we decompose p.

https://miro.medium.com/max/602/1*9GQrzQwfJfpJUyiLTOJnOw.png

Next we choose a random a and check the following conditions.

https://miro.medium.com/max/970/1*3zCl17oRfwxBzXsryQXsVA.png

For any prime p either the first condition holds or there exists s to comply the second condition. If the conditions can’t be satisfied, p is composite.
But if p is in fact a composite, there is 1/4 chance it will pass the test. Therefore we select another a and repeat the test. After testing k independent values for a, the chance for a mistake gets down to 4^-k.
Notice the idea behind Rabin-Miller. The test initially assumes p to be a prime. Then it searches for evidence it is not. If the evidence is not found, p is a prime with high probability, also called pseudoprime.

'''
from random import randrange

# Algorithm
def rabin_miller(prime, tests):
    if prime < 5:
        return print in [2,3]

    # set: prime = q*2**r+1
    q,r = prime-1,0
    while not q & 1:
        q >>=1
        r += 1

    # test repeatedly
    for _ in range(tests):
        a = randrange(2, prime-1)

        # pass if: a**q ==1
        x = pow(a,q,prime)
        if x in [1, prime-1]:
            continue

        # pass if: a**(q*2**s) == -1,s<r
        for _ in range(r-1):
            x = pow(x,2,prime)
            if x ==prime-1:
                break

        else:
            return False

    return True

def prime(bits, tests):
    while True:
        # random number in [2**bits... 2**(bits+1)-1]
        prime = (1<< bits) | randrange(1<<bits) | 1

        # primality test
        if rabin_miller(prime, tests):
            return prime


# Run
print(prime(256,32))
