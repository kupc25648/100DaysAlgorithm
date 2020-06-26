'''
BST is another very interesting data structure. It allows for fast lookup, insertion and removal in expected O(log n) time. What’s even more important, BST keeps the data sorted and supports interval retrieval in time O(k+log n) for k items. That makes binary trees a key tool in RDBMS.

There are many improvements to a basic binary tree, most profound would be 2–3 tree, Red-Black tree, B-tree, B+tree, B*tree. But don’t get confused when learning them for the first [or second, or third] time.

They all are just basic BSTs with additional constraints, tweaks and optimizations. When you think of them in terms of basic binary trees, the life is often much easier.

2–3 tree is a perfectly balanced BST [almost, there’s a hidden constant]

LLRB-tree is BST implementation of 2–3 tree with path coloring constraint

RB-tree is BST implementation of 2–3–4 tree with path coloring constraint

B-tree is a perfectly balanced BST with subtree block alignment

Besides the usual implementation, today I’d like to focus on an interesting property: When adding uniformly distributed data into unbalanced BST, the height of the tree is O(log n).

I’ve implemented unbalanced BST and used a simulation. 1000 trees are built and sampled at certain sizes. With a little bit of statistics we may check if the height is truly logarithmic. In such case we should be able to fit a linear model on a log-scaled data.

See for yourselves. The plot has log-scaled x-axis and contains min, max and average height.

The full source code is available on github. And trust me, it’s less work and it’s much easier than it sounds.
'''
import numpy as np
from sklearn.linear_model import LinearRegression
from bokeh.plotting import figure, show, output_notebook
# Algorithm
def search(node, value):
    if node:
        x,left,right = node
        this = value == x
        lserarch = value < x and search(left,value)
        rserarch = value > x and search(right,value)
        return this or lserarch or rserarch

def add(node, value):
    if node:
        x,left,right = node
        this = value == x and node
        ladd = value < x and (x,add(left,value), right)
        radd = value > x and (x,left, add(right,value))
        return this or ladd or radd
    return value, None, None

def depth(node):
    return node and max(depth(node[1]), depth(node[2])) + 1 or 0

def iterate(node):
    if node:
        x, left, right  = node
        yield from iterate(left)
        yield x
        yield from iterate(right)
# Run
data = [2, 16, 4, 2, 2, 11, 9, 0, 14, 11, 11, 9, 12, 7, 2, 12, 3, 9, 6, 12]

root = None
for value in data:
    root = add(root, value)

print('depth', depth(root))
print(list(iterate(root)))
print(10, search(root, 10))
print(16, search(root, 16))

# Simulation
tree_vs_depth = {
    10: [], 20: [], 50: [],
    100: [], 200: [], 500: [],
    1000: [], 2000: []
}

for _ in range(1000):
    root = None
    for i, value in enumerate(np.random.randint(100000, size=2500)):
        root = add(root, value)
        if i + 1 in tree_vs_depth:
            tree_vs_depth[i + 1].append(depth(root))

# Statistics
x, y = [], []

for i, d in tree_vs_depth.items():
    x.append([np.log(i)])
    y.append([np.mean(d), np.min(d), np.max(d), np.std(d)])
    print('{:4} items: depth[mean,min,max,std]={}'.format(i, np.round(y[-1], 1)))

x, y = np.array(x), np.array(y)

model_mean = LinearRegression().fit(x, y[:, 0])
print('mean', model_mean.coef_[0], model_mean.intercept_)

model_min = LinearRegression().fit(x, y[:, 1])
print('min', model_min.coef_[0], model_min.intercept_)

model_max = LinearRegression().fit(x, y[:, 2])
print('max', model_max.coef_[0], model_max.intercept_)


