'''
In machine learning we often need to shuffle data. For example, if we are about to make a train/test split and the data were sorted by category beforehand, we might end up training on just half of the classes. That would be bad.

Uniform shuffle guarantees that every item has the same chance to occur at any position. Seems like an easy task, but it requires a bit of thinking.

Hasty solution would be to cycle through all N positions, each time generate random value in range [0, N) and swap the current position with a random one. Is that uniform?

We select out of N^N shuffles, but there are only N! permutations. Obviously, we can’t get uniform distribution in this way and some items will have its preferences.

What we need, instead, is to get a random permutation. To find one, we cycle through, at position i generate a random value in range [i, N) and swap the two positions. Is that uniform?

Each item has the chance 1/N to get at position 0. Each item also has the chance (N-1)/N not to get there. Hence the chance for position 1 is the same, again, 1/N. This condition holds for all the array.
'''
import numpy as np
# Algorithm
def shuffle(data):
    n = len(data)
    for i in range(n):
        k = np.random.randint(i,n)
        data[i], data[k] = data[k], data[i]

    return data
# Run
data = list(range(10))
print(shuffle(data))
print(shuffle(data))
