'''
Given a stream of zeroes and ones, the goal today is to count number of ones in an arbitrarily large window.

That is surprisingly difficult problem. If there are 10⁹ elements in a day and you are queried for the past 6 months, you can’t just keep all the stream in memory, and still, you have to keep the track somehow.

What we can do is to estimate the number. Instead of representing a single large window, we only keep buckets representing consecutive windows containing exactly 2^k ones together with timestamps of the last occurrence. To limit resources, buckets of the same size can be grouped together into twice as large bucket as data are streamed.

When querying number of ones, we take the buckets that fit into the requested window and half of the last bucket that doesn’t fit. The estimate will than make 50% error at worst.

The algorithm requires O(log²n) memory and a single query takes O(log n) time. What’s the best, we can store zero in O(1) time and we can store one in O(1) amortized time.
https://github.com/coells/100days

'''
import numpy as np
from itertools import count
from collections import defaultdict

# Algorithm
def stream_counter():
    bucket = defaultdict(list)
    timestamp = count(1)
    estimate = None

    while True:
        code = yield estimate
        estimate = None

        # update buckets
        if code is True:
            bucket[1].append(next(timestamp))

            i = 1
            while len(bucket[i]) ==3:
                bucket[2*i].append(bucket[i][1])
                del bucket[i][:2]
                i *= 2

        elif code is False:
            next(timestamp)

        # estimate count
        elif isinstance(code, int):
            counts = [
                i for i in bucket
                for t in bucket[i] if code < t] or [0]
            estimate = sum(counts) - counts[-1]//2

        # debug
        elif code == 'debug':
            for i in bucket:
                print(i,bucket[i])
# Run
n = 10**6
ctr = stream_counter()
next(ctr)
for i in range(n):
    ctr.send(np.random.rand()>=.5)

for i in np.linspace(.99,0,5):
    k = int(i*n)
    print(f'last {n - k} bits: {ctr.send(k)}')

