'''
Clique in an undirected graph is a subgraph that is complete. Particularly, if there is a subset of k vertices that are connected to each other, we say that graph contains a k-clique.

complete graph
We can find all the 2-cliques by simply enumerating all the edges.
To find k+1-cliques, we can use the previous results. Compare all the pairs of k-cliques. If the two subgraphs have k-1 vertices in common and graph contains the missing edge, we can form a k+1-clique.
It should be noted that while finding a k-clique is a polynomial problem running in O(n^k) time, a clique decision problem (does the graph contain clique of size k?) is NP-complete.

https://en.wikipedia.org/wiki/Clique_(graph_theory)
'''
from itertools import combinations
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Algorithm
def k_cliques(graph):
    # 2-cliques
    cliques = [{i,j} for i,j in graph.edges() if i != j]
    k =2

    while cliques:
        #result
        yield k ,cliques

        # merge k-cliques into (k+1)-cliques
        cliques_1 = set()
        for u,v in combinations(cliques,2):
            w = u ^ v
            if len(w) == 2 and graph.has_edge(*w):
                cliques_1.add(tuple(u|w))

        # remove duplicate
        cliques = list(map(set, cliques_1))
        k+=1

def print_cliques(graph):
    for k, cliques in k_cliques(graph):
        info = k,len(cliques), cliques[:3]
        print('%d-cliques: #%d , %s ...' %info)

# Complete Graph
nodes = 6
graph = nx.Graph()
graph.add_nodes_from(range(nodes))
graph.add_edges_from(combinations(range(nodes),2))

# K-Cliques
print_cliques(graph)

