'''
Topological sort of a directed acyclic graph [DAG] is partial ordering of its nodes such that U < V implies there must not exist a path from V to U.
Kahn’s algorithm I implemented, instead produces a linear ordering such that […, U, …, V, …] means there may be a path from U to V, but not vice versa.

topological sort: all edges are directed from left to right
Partial ordering is very useful in many situations. One of them arises in parallel computing where a program can be represented as DAG.
E = (A + B) * (C - D)
Each node represents an operation and directed links in between are their dependencies.

topological sort of DAG representing the expression
There are 8 operations [including fetch and store] in this expression, but modern super-scalar CPUs are able to execute some operations in parallel to reduce the execution time up to 4 steps.

https://medium.com/100-days-of-algorithms/day-81-topological-sort-7a317e0c1dde
'''

import networkx as nx
from collections import deque
from bokeh.plotting import figure, show, output_notebook

# Algorithm
def topological_sort(graph):
    topology =[]
    degree = {n: graph.in_degree(n) for n in graph.nodes()}

    # nodes without incoming edges
    queue = deque( n for n, d in degree.items() if not d)

    while queue:
        n= queue.popleft()
        topology.append(n)

        # remove node's edges
        for m in list(graph[n]):
            degree[m] -= 1

            # enqueue nodes with no incoming edges
            if not degree[m]:
                queue.append(m)

    if len(topology) < len(graph):
        raise ValueError('graph contains cycle')
    return topology

# Run
graph = nx.DiGraph([
    ('A', 'B'),
    ('A', 'D'),
    ('B', 'C'),
    ('B', 'E'),
    ('C', 'D'),
    ('C', 'E'),
    ('D', 'E'),
    ('F', 'G'),
])

topology = topological_sort(graph)
print(topology)

# Plot
n = len(topology)
x = range(n)
q = []

for u, v in graph.edges():
    x0 = topology.index(u)
    x1 = topology.index(v)
    yc = 0 if abs(x0 - x1) == 1 else -.7 if x0 & 1 else .7
    q.append([x0, 0, x1, 0, (x0 + x1) / 2, yc])

output_notebook()

plot = figure(x_range = (-1, n), y_range = (-1, 1), plot_width=600, plot_height=300)
plot.grid.visible = False
plot.axis.visible = False

plot.quadratic(*zip(*q), color='red')
plot.circle(x, 0, size=30)
plot.text(x, 0, text=topology, text_color='yellow', text_align='center', text_baseline='middle')

show(plot)
