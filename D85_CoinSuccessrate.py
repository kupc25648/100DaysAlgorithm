'''
What is the probability to see a success run of 10 heads if we toss a fair coin thousand times?
You might be tempted to answer 1/2¹⁰, but this problem is really non-trivial. Such an intuitive [mis]understanding of probability is often source of gambler’s fallacy.
Derivation and proof of the correct answer is way beyond this series. In this case I will only show a general solution and provide its implementation.
I would also like to express my gratitude to professor Santosh S. Venkatesh. His excellent lectures and book helped me to understand probability and statistics.
Let’s denote
r — length of success run
p — probability of tossing heads
u[n] — a success run (first or subsequent) of length r occurs at trial n
f[n] — the first success run of length r occurs at trial n
s[n] — at least one success run of length r occurs at or before trial n

To get an answer for the question I laid, we set r=10, p=.5 and find s[1000]. List of probabilities below gives the answer. Probability to see a success run of 10 heads within thousand tosses is 39%.

https://medium.com/100-days-of-algorithms/day-85-coin-success-runs-ea3958b27bc8
'''

import numpy as np

# Algorithm
def probability(n, k, p, all_probs=False):
    F = np.zeros(n + 1)
    U = np.zeros(n + 1)
    R = p ** np.arange(k + 1)

    for i in range(k, n + 1):
        U[i] = R[k] - R[1:k] @ U[i-k+1:i][::-1]
        F[i] = U[i] - F[1:i] @ U[1:i][::-1]

    S = F.cumsum()

    return S if all_probs else S[-1]

# Run
def print_chance(n):
    print(n, 'tosses; probability to see at least ...')

    for k in range(1, n+1):
        p = probability(n,k,.5)
        print('%dx HEADS in row = %.4f' % (k, p))
        if p < 1e-4:
            break

print_chance(50)
