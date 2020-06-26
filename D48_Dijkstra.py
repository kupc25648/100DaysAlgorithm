'''
If I remember correctly, Dijkstra’s algorithm was the very first graph algorithm they taught us in Discrete mathematics lectures.

And I think there are many reasons to why it is a good starting point.
finite graph traversal is a key technique
there’s a beautiful proof of correctness using mathematical induction
it works for unweighted and weighted graphs
it works for undirected and directed graphs
its deep understanding helps to implement other algorithms with ease
If you would like to practice on your own, here are few hints to think about.
what happens if an edge weight is negative?
what conditions can be added to avoid redundant cycles in outer loop?
how would you extend the single-source implementation to a multi-source? (multi-source means we start searching at multiple points)
what happens if the condition for the next node to be searched changes? how to alter the algorithm to deal with it?
The last point is a key to successful implementation of A* algorithm.

'''
from heapq import heappush, heappop
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Algorithm
def dijkstra(graph,source):
    distance = {}
    queue = [(0,source)]

    while queue:
        # shortest unexplored path
        p, v = heappop(queue)
        if v in distance:
            continue

        # shortest path (sourrce,...,v)
        print('({},...,{}) = {}'.format(source,v,p))
        distance[v] = p

        # extend path to (sourrce,...,v,u)
        for _, u, e in graph.edges(v, data = True):
            heappush(queue, (p+e['weight'],u))

    return distance
# Graph
n = 20
graph = nx.Graph()
graph.add_nodes_from(range(n))
for u, v in np.random.randint(0, n, (n, 2)):
    graph.add_edge(u, v, weight=abs(u - v))

print(graph)

# Run
dijkstra(graph, 0)
