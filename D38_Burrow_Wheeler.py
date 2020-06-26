'''
Burrows-Wheeler transform is a text transformation used to improve compression in bzip2 to outperform other state-of-the-art techniques [at the time].
The idea is to use advantage of frequently occurring bigrams. he, the, there, her, where are all frequent words containing bigram he. BWT permutes the text so that h is grouped together.
Let’s transform text he her hers.

BWT first creates all permutations given by translations. Than the set is sorted alphabetically and the last column represents the final permutation.
To reverse the process we start by an empty set. The original column is prepended to the current set and the set is sorted alphabetically. Repeating column by column, IBWT reconstructs the original table.
There are two obvious problems, speed and memory. BWT doesn’t need to keep all the permutations in memory, points will do. And authors also claimed they were able to sort in almost linear time. However, to achieve significant results, blocks of 1MB size have to be processed. While today 1MB is worth of nothing, at the time bzip2 came it was a lot.

'''

# Algorithm
def bwt(source):
    aux = [source[i:] + source[:i] for i in range(len(source))]
    aux.sort()
    idx = aux.index(source)
    return ''.join(i[-1] for i in aux), idx

def ibwt(source, idx):
    n = len(source)
    aux = ['']*n
    for _ in range(n):
        aux = sorted([i+j for i,j in zip(source, aux)])
    return aux[idx]
# Run
target, i = bwt('the theta, there and there, was her')

print(target, i)

source = ibwt(target, i)

print(source)


