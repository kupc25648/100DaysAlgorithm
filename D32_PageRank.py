'''
PageRank is an algorithm to determine what is called centrality in egonets. There are other ways to measure centrality, e.g. betweenness, closeness or hubs and authorities.
However, PageRank is quite useful for huge graphs due to its relation to Markov Chains. Specifically, if the graph adjacency matrix M is stochastic, irreducible and aperiodic, there exists a single point of convergence that is solution to equation M*r=r.
The solution is leading eigenvector and Power iteration is an iterative method that can be used to find it. Power iteration has fast convergence rate and its computation can be easily distributed.
https://github.com/coells/100days

@ = numpy.matmul

'''
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Function
def pagerank(graph, alpha=0.9):
    n = len(graph)

    # remove links to self
    graph[range(n), range(n)] = 0

    # ensure stochasticity
    graph[:, graph.sum(0) == 0] = 1
    graph /= graph.sum(0)

    # add random teleports
    graph = alpha * graph + (1-alpha)/ n*np.ones((n,n))

    # power iteration
    prev = np.zeros(n)
    rank = prev + 1/n
    while (rank-prev)@ (rank-prev) > 1e-8:
        prev = rank
        rank = graph@rank

    return rank

# Generate graph
n =10

graph = nx.DiGraph()
graph.add_nodes_from(range(n))
graph.add_edges_from(np.random.randint(0,n,(3*n,2)))

# Run
ranks = pagerank(
    np.array(nx.adjacency_matrix(graph).todense(),dtype=np.float32)).round(2)


nx.draw_networkx(graph, node_color='lightgreen', node_size=ranks * 5000)

plt.show()
