'''
In 2-sum, 3-sum or 4-sum problems we are searching for a tuples, triplets or quadruplets that sum to zero. Or any other value.
There are several strategies to approach 4-sum problem. The one I chose builds a hash map to search for pairs of tuples that satisfy (2sum, -2sum).
We can also set similarity = I{sum(tuple1) == -sum(tuple2)} to redefine the problem into concept of similarity. That brings us quickly into Locality-Sensitive Hashing and big data mining where the same algorithm can be successfully deployed and tweaked for memory/speed trade-off.

'''
import numpy as np
from itertools import combinations, product
from collections import defaultdict

# Algorithm
def sum4(data):
    # store 2-sums
    sum_of_2 = defaultdict(list)
    for i, j in combinations(range(len(data)),2):
        k = data[i] + data[j]
        sum_of_2[k].append((i,j))

    # match pairs of 2-sums
    sum_of_4 = set()
    for k in sum_of_2:
        if k >= 0 and -k in sum_of_2:
            for i,j in product(sum_of_2[k],sum_of_2[-k]):
                index = tuple(sorted(set(i+j)))
                if len(index) == 4:
                    sum_of_4.add(index)

    return sum_of_4
# Run
n = 10
data = np.random.randint(-n,n,n)
print(data)

for index in sorted(sum4(data)):
    print(index, data[list(index)])

