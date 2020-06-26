'''
Union-Find is a data structure that is capable of tracking and merging of disjoint sets. As a structure it is very important inside other algorithms like Prolog unification or percolation problem.

There are two signification improvements that can be made to speed the algorithm up, weighting and path compression. I’ve implemented path compression, only, the code is short and performance is pretty good.
'''

# Algorithm
def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]

def union(data,i,j):
    pi,pj = find(data,i),find(data,j)
    if pi != pj:
        data[pi] = pj

def connected(data,i,j):
    return find(data, i) == find(data,j)
# Run
n = 10
data = [i for i in range(n)]
connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]

# union
for i,j in connections:
    union(data,i,j)

# find
for i in range(n):
    print('item', i, '-> component', find(data, i))
