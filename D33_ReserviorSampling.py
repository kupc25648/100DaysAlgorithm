'''
Reservoir sampling is super useful when there is an endless stream of data and your goal is to grab a small sample with uniform probability.
The math behind is straightforward. Given a sample of size K with N items processed so far, the chance for any item to be selected is K/N. When the next item comes in, current sample has a chance to survive K/N*N/(N+1)=K/(N+1) while the new item has chance K/(N+1) to be selected.
https://github.com/coells/100days

'''
import numpy as np

# Algorithm
# size = amount of sample
def reservior_sampling(size):
    i, sample = 0, []

    while True:
        item = yield i, sample
        i += 1
        k = np.random.randint(0,i)

        if len(sample) < size:
            sample.append(item)
        elif k < size:
            sample[k] = item

# Sampling
reservior = reservior_sampling(5)
next(reservior)

for i in range(1000):
    k, sample = reservior.send(i)
    if k % 100 == 0:
        print(k, sample)
