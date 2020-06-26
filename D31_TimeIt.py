'''
There are two areas in computer science I consider to be a rocket science, multithreading and benchmarking. And regarding to latter, Python offering a surgical tool instead of useful one is not much helpful.

Today’s algorithm focuses on timeit implementation that addresses two caveats the built-in timeit does not:

    -   measure defined as number of calls per second, not elapsed time per call
    -   empirical estimation of time complexity

Note that a good benchmark is defined in terms of methodology, not in numbers. To conclude, here’s what happens once you benchmark your code:
    -   everyone gets different results on local machine
    -   faster implementation is slower under a different measure
    -   perfcounters on production differ from your local results (that’s because environment has changed; GC, CPU, memory, order/number of calls, etc.)
    -   team spends a week on optimization to find there was a bug in the test/benchmark
'''
import numpy as np
from time import perf_counter

def timeit(fn, fargs, n_range, seconds =5):
    print(f'[timeit] {seconds} seconds per N')

    # timeit for N
    bench = []
    for n in n_range:
        args = fargs(n)
        calls = 0

        # benchmark
        timer = perf_counter()
        while perf_counter() - timer < seconds:
            fn(args)
            calls += 1
        timer = perf_counter() - timer

        # results
        bench.append([np.e,n,timer/calls])
        print(f'[N={n}] {calls/timer:.2f} calls/sec')

    # estimate complexity
    bench = np.log(bench)
    (alpha, beta), *_ = np.linalg.lstsq(bench[:,:2], bench[:,-1])
    print(f'estimated 0({np.exp(alpha):.3}*N^{beta:.3f})')

n_range = [100, 1000, 10000, 100000, 1000000]

def get_array(n):
    return np.random.randint(0, n, n)


timeit(sorted, get_array, n_range)
