'''
LCS is an algorithm built in tools you probably use every day. One example for all, Git wouldn’t be able to work the way it works without LCS.
A few facts:
it is a textbook case of dynamic programming technique
time complexity to find LCS is O(n²) and space required is O(n²) for 2 input sequences
time complexity to find only length of LCS is still O(n²) but space required is O(n) for 2 input sequences
While the algorithm is polynomial with respect to a sequence length, it is exponential with respect to the number of sequences. Time complexity to find LCS of k sequences is O(n^k). And that’s pretty hard to solve.
Long time ago I was very curious about an optimal solution for DNA-like input set with many sequences. I wrote a highly optimized C++ code to give me one. After 20+ hours it truly reached the optimum. It was the same solution that genetic algorithm returned after 1.5 seconds.

'''
from collections import defaultdict

# Algorithm
def lcs(x,y):
    # memoize longest subsequences
    table = defaultdict(lambda: 0)

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                table[i,j] = table[i-1,j-1]+1
            else:
                table[i,j] = max(table[i-1,j], table[i,j-1])

    # reconstruction
    sequence = ''
    i,j = len(x)-1, len(y)-1

    while i >= 0 and j >=0:
        if x[i] == y[j]:
            sequence = x[i] +sequence
            i -=1
            j -=1
        elif table[i-1,j] < table[i,j-1]:
            j -= 1
        else:
            i -=1

    # result
    return table[len(x)-1, len(y)-1], sequence

# Run

print(lcs('longest common sub/sequence', 'shortest unique sub-sequence'))

