'''
Median is just a special case of searching for k-th element. For today, let’s just focus on arrays with distinct elements, hence each value needs to be unique.

While straightforward solution would be to sort the array in O(n.log(n)) and pick k-th position in O(1), we can do better and implement the lookup in O(n).

The idea is to use splitting by pivot in a way that quicksort does. However, unlike quicksort we are only interested in one partition and carry on search in there.

It can be shown that the expected time of this algorithm is O(n). And it also looks like the worst case running time is O(n²). But the reason I chose median lookup today was to show a little intuition of why that’s not true.

Let’s see what may happen. Obviously the best case is to hit pivot very close to median and carry on search on half of array. But we may also hit pivot very far from median and carry on almost the same array as in previous step.

Fortunately, there’s a proof that a good pivot is any element from the middle half of array (in statistics it’s called IQR). When the pivot is randomly selected from a set of distinct elements, we have 50% chance to get a good one.

We only need about the same number of good and bad pivots, in which case we can say we reach 2*O(n) running time instead of O(n) and hide the constant inside Big-O notation.

We also have 50% chance to get a bad pivot and here comes the crucial part. If we randomize on pivot from a set of distinct elements, we effectively eliminate pathological situations. For O(n²) running time we would need to hit bad pivots often, but the chance of choosing a series of bad ones falls down exponentially.

Intuitively, the worst case estimate doesn’t work in practice because the chances required to touch O(n²) are quickly decreasing with the problem size.

https://github.com/coells/100days
'''

import numpy as np

# Algorithm
def kth(items, k, depth=1):
    if len(items) == 1:
        return items[0], depth

    #randomize on pivot
    pivot = np.random.choice(items)
    split = np.sum(items <= pivot)

    #search partition
    if k < split:
        return kth(items[items<=pivot], k, depth+1)
    else:
        return kth(items[items > pivot], k-split, depth+1)

# Run
items = np.arange(1000000)
np.random.shuffle(items)

print(kth(items, len(items)//2))

print(kth(items, 0))

print(kth(items, len(items)-1))
