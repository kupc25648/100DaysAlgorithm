'''
Tonight I heard a strange noise coming out of my bathroom. After a quick check I found there’s a small unplanned fountain in my wall.

It was 3:30AM and as I was waiting for emergency service to arrive, I thought it would be a good idea to implement Ford-Fulkerson today.
It is an algorithm that finds a maximum flow between source and sink node in directed graph. There are two conditions.
each edge in the graph has a fixed capacity and a flow through the edge must not exceed the capacity
total incoming flow into any node must be equal to total outgoing flow from the node
Ford-Fulkerson greedily searches for a path between source and sink, such that each edge along the path still has a capacity reserve. If such path exists, the flow along the path gets increased.
However, the path is allowed to go through an edge in inverse direction. If there is any flow on such edge, it gets decreased, instead. This step effectively redirects flow from the edge and increases its capacity reserve, while total flow in graph increases.
note to Python version
If you use Python 3.6 the algorithm behaves deterministically due to a new dictionary implementation. Python 3.5 should return different results on different runs. In which case you can witness a selection of inverted edges and increases of capacity reserves, such as path ADFCGH below.

'''
import numpy as np
from scipy.fftpack import fft2, ifft2
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import push_notebook
from time import sleep

# Algorithm
def ford_fulkerson(graph, source, sink, debug=None):
    flow, path = 0, True

    while path:
        # search for path with flow reserve
        path, reserve = depth_first_search(graph, source, sink)
        flow += reserve
        # increase flow along the path
        for v, u in zip(path, path[1:]):
            if graph.has_edge(v, u):
                graph[v][u]['flow'] += reserve
            else:
                graph[u][v]['flow'] -= reserve

        # show intermediate results
        if callable(debug):
            debug(graph, path, reserve, flow)
def depth_first_search(graph, source, sink):
    undirected = graph.to_undirected()
    explored = {source}
    stack = [(source, 0, undirected[source])]

    while stack:
        v, _, neighbours = stack[-1]
        if v == sink:
            break

        # search the next neighbour
        while neighbours:
            u, e = neighbours.popitem()
            if u not in explored:
                break
        else:
            stack.pop()
            continue

        # current flow and capacity
        in_direction = graph.has_edge(v, u)
        capacity = e['capacity']
        flow = e['flow']
        # increase or redirect flow at the edge
        if in_direction and flow < capacity:
            stack.append((u, capacity - flow, undirected[u]))
            explored.add(u)
        elif not in_direction and flow:
            stack.append((u, flow, undirected[u]))
            explored.add(u)
    # (source, sink) path and its flow reserve
    reserve = min((f for _, f, _ in stack[1:]), default=0)
    path = [v for v, _, _ in stack]

    return path, reserve
# Graph
graph = nx.DiGraph()
graph.add_nodes_from('ABCDEFGH')
graph.add_edges_from([
    ('A', 'B', {'capacity': 4, 'flow': 0}),
    ('A', 'C', {'capacity': 5, 'flow': 0}),
    ('A', 'D', {'capacity': 7, 'flow': 0}),
    ('B', 'E', {'capacity': 7, 'flow': 0}),
    ('C', 'E', {'capacity': 6, 'flow': 0}),
    ('C', 'F', {'capacity': 4, 'flow': 0}),
    ('C', 'G', {'capacity': 1, 'flow': 0}),
    ('D', 'F', {'capacity': 8, 'flow': 0}),
    ('D', 'G', {'capacity': 1, 'flow': 0}),
    ('E', 'H', {'capacity': 7, 'flow': 0}),
    ('F', 'H', {'capacity': 6, 'flow': 0}),
    ('G', 'H', {'capacity': 4, 'flow': 0}),
])
layout = {
    'A': [0, 1], 'B': [1, 2], 'C': [1, 1], 'D': [1, 0],
    'E': [2, 2], 'F': [2, 1], 'G': [2, 0], 'H': [3, 1],
}

def draw_graph():
    plt.figure(figsize=(12, 4))
    plt.axis('off')

    nx.draw_networkx_nodes(graph, layout, node_color='steelblue', node_size=600)
    nx.draw_networkx_edges(graph, layout, edge_color='gray')
    nx.draw_networkx_labels(graph, layout, font_color='white')

    for u, v, e in graph.edges(data=True):
        label = '{}/{}'.format(e['flow'], e['capacity'])
        color = 'green' if e['flow'] < e['capacity'] else 'red'
        x = layout[u][0] * .6 + layout[v][0] * .4
        y = layout[u][1] * .6 + layout[v][1] * .4
        t = plt.text(x, y, label, size=16, color=color,
                     horizontalalignment='center', verticalalignment='center')

    plt.show()
draw_graph()

# Run
def flow_debug(graph, path, reserve, flow):
    print('flow increased by', reserve,
          'at path', path,
          '; current flow', flow)
    draw_graph()
ford_fulkerson(graph, 'A', 'H', flow_debug)
