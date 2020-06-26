'''
Today I’d like to implement an algorithm and keep a track of the process. It may seem to be out of scope of the series, but implementation of algorithm is an incremental process, and often a long one.
A good showcase is somewhat typical task you may receive at a job interview.
In a sequence find the longest unique consecutive subsequence, i.e. sequence consisting of unique items. Make the algorithm run in O(n) time in worst case.
The text often offers a hints in form of restrictions that tell you what to do.
O(1) time — there’s a pattern; take pen a pencil and find it; solution can be found in a constant number of steps; no cycles needed
O(log n) time — there’s a recursive pattern; you can eliminate half of input at each step; use single cycle
O(n) time — you have to cycle through; constants number of cycles can be used, but no nested cycles are allowed (not entirely true, there are exceptions, but rare)
O(n.log n) time — efficient solution requires sorting or sorted auxiliary structure
O(n²) time — an auxiliary table has to be built
O(1) memory — no structures, use as many variables as you wish, but any complex structure must be limited by constant
O(log n) memory — there is a pattern in bit representation of input that can be captured and applied
O(n) memory — auxiliary array is needed, maybe table; if it is a table all but one dimension must be constant
O(n²) memory — auxiliary table is required; time can never be below O(n²) in this case (and you rarely see this one on an interview)
version #1
Somewhat obvious solution is to cycle through the sequence and iteratively shrink and expand sliding window over unique sequences. I will keep track of the items using set to comply O(n) time.

'''
from functools import reduce

text = 'Premature optimization is the root of all evil -- DonaldKnuth'
# Algorithm
def longest_unique_sequence(sequence):
    i,j,k = 0,0, set()
    bi,bj = 0,0

    while j<len(sequence):
        if sequence[j] in k:
            k.remove(sequence[i])
            i+=1
        else:
            k.add(sequence[j])
            j +=1
        if j -i > bj-bi:
            bi, bj = i,j

    return bi,bj
# Run
i, j = longest_unique_sequence(text)
print(i, j, '"%s"' % text[i:j])
