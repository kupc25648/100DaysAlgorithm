'''
It took me almost two months to find a courage to implement quicksort. And here we are. This algorithm is a nightmare. It’s pretty easy to grasp the concept, but it’s extremely difficult to implement.
I have already implemented another algorithm based on the same idea on day 35, but I cowardly duplicated partitions.
Quicksort is a very efficient algorithm running in expected O(n.log n) time, with very low multiplicative constant, around 2 — if implemented correctly.
The problem is, standard version of the algorithm is linearithmic only on unique data. If elements occur many times, the performance degrades. Lifesaver is 3-way quicksort that splits the data into three partitions, lower, higher and same as pivot.
Another catch is uniform randomization of pivot. It is a vital part of proof that the algorithm is expected to run in linearithmic time. Deterministic selections of pivot do not have this property.

'''
import numpy as np

# Algorithm
def swap(data, i,j):
    data[i], data[j] = data[j], data[i]

def qsort3(data, left, right):
    # sorted
    if left >= right:
        return

    # select pivot
    i = np.random.randint(left, right+1)
    swap(data, left, i)
    pivot = data[left]

    # i : points behind left partition
    # j : points ahead of right partition
    # k : current element
    i,j,k = left,right, left +1

    # split to [left] + [pivot] + [right]
    while k <= j:
        if data[k] < pivot:
            swap(data, i,k)
            i+=1
        elif data[k] > pivot:
            swap(data, j,k)
            j -= 1
            k -= 1

        k+= 1

    # recursion
    qsort3(data, left, i-1)
    qsort3(data, j+1, right)

def qsort(data):
    qsort3(data, min(data), len(data)-1)

# Run
data = np.random.randint(-2,10,100)
print(data)

qsort(data)

print(data)

