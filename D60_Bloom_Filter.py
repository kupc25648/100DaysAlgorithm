'''
Bloom filter is a probabilistic data structure based on hashing. It’s very similar to hash table, but differs in several important aspects.
only add() and contains() operations are supported (I’ll skip union)
contains() may return false positives
uses fixed memory size (can’t enlarge), but scales well for big data
Bloom filter is relatively simple. It is using fixed bit array that is zeroed at the beginning and a fixed collection of k hash functions.
add(item) sets all the k bits of array to 1, array[hash[i](item)] = 1.
contains(item) conversely checks if all the k bits are set,
all(array[hash[i](item)] == 1).
It is obvious that any item that has been added will be correctly reported as present. However, it may happen that items which have not been added will be reported as present, too. That’s a false positive.
I will skip the math of a chance to get false positive and try the bloom filter directly in code. Let’s use a textbook example. Users are coming to a website. Based on user IP address, find out if the user is returning.
There are two groups of about million users, A — returning users, and B — new users. Using a standard hash table, we would need about 6*10**6 bytes of memory.
Bloom filter with 10**6 bytes of memory and 3 hash functions has about 4% of false positive rate. Bloom filter with 4*10**6 bytes of memory and 6 hash functions is below 0.1%.
Check the run section at the end of article.
'''
import numpy as np
from collections import deque
from bitarray import bitarray
# Algorithm

# SKip cannot impot bit array
