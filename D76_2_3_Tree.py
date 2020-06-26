'''
2–3 tree is a perfectly balanced binary search tree. Which means that every path from root to leaf has the same length and the data structure guarantees worst case O(log n) time complexity for search and insert operations.
What is the difference to regular BST I have talked about on day 45?
2–3 tree extends node capacity.
2-node contains a single value and has two children [unless it is leaf]
3-node contains two values and has three children [unless it is leaf]
To insert a value into 2–3 tree, find proper leaf as in regular BST and insert the value in-place. If the leaf now contains 3 values, it is called temporary 4-node. Split the node into three 2-nodes, and insert the middle value into parent.

source: wikipedia
While this all sounds good, 2–3 trees are very difficult and tricky to implement. But there is a way to implement them in a very nice and efficient way — using a left-leaning variant of red-black trees.
Let me tell you, back at the university I had to know how to implement and prove all the stuff around red-black trees. Yet, I never really understood the intuition behind, until I saw the left-leaning variant which is very simple to understand.
We can implement 2-node as regular node, but mark the node and its children black. 3-nodes are implemented such that the lower value is child of higher value and is marked red.
When a value is inserted into leaf, it is red by default. Then traverse back up to the root and check the following invariants.
only left child can be red — if left child is black and right child is red, rotate the node to left
red parent can’t have red child — if so, rotate the node to right
parent can’t have two red children — if so, mark them black and make the parent red
It requires some drawing on the paper, but the operations are very intuitive and one-to-one reflect operations in 2–3 tree
'''
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import push_notebook
from time import sleep

# Algorithm
class Node:
    def __init__(self,value,left=None, right=None, red=False):
        self.value = value
        self.left = left
        self.right = right
        self.red = red

    @staticmethod
    def red(node):
        return node and node.red

    def rotate_left(self):
        if not Node.red(self.left) and Node.red(self.right):
            child = self.right
            self.right, child.left = child.left, self
            self.red, child.red = True, self.red
            return child
        else:
            return self

    def rotate_right(self):
        if Node.red(self.left) and Node.red(self.left.left):
            child = self.left
            self.left, child.right = child.right, self
            self.red, child.red = True, self.red
            return child
        else:
            return self

    def flip_colors(self):
        if Node.red(self.left) and Node.red(self.right):
            self.red, self.left.red, self.right.red = True, False, False

def insert(node, value, root=True):
    if not node:
        return Node(value, red=not root)

    # insert value
    if value == node.value:
        pass
    elif value < node.value:
        node.left = insert(node.left, value, root= False)
    else:
        node.right = insert(node.right, value, root=False)

    # update tree w.r.t invariants
    node = node.rotate_left()
    node = node.rotate_right()
    node.flip_colors()

    # keep root black
    if root:
        node.red = False

    return node

def draw(node, red, black, xlo=0, xhi =1, x=.5, y=0):
    if node:
        x_, y_ = (xlo + xhi) / 2, y-1
        (red if node.red else black).append([x,y,x_,y_])
        draw(node.left, red,black,xlo,x_,x_,y_)
        draw(node.right, red,black,x_,xhi,x_,y_)

# Run
# insert few value
root = None
for i in range(5):
    root = insert(root,i)

output_notebook()

output_notebook()

# get plot data
red, black = [], []
draw(root, red, black)

# plot
plot = figure(plot_height=400, plot_width=800)
plot.axis.visible = False
plot.grid.visible = False

red_segment = plot.segment(*zip(*red), color='#ff0000')
black_segment = plot.segment(*zip(*black), color='#000000')

handle = show(plot, notebook_handle=True)

for _ in range(100):
    for i in np.random.randint(0, 1000, 5):
        root = insert(root, i)

    red, black = [], []
    draw(root, red, black)

    x0, y0, x1, y1 = red and zip(*red) or [tuple()] * 4
    red_segment.data_source.data.update({
        'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1
    })
    x0, y0, x1, y1 = black and zip(*black) or [tuple()] * 4
    black_segment.data_source.data.update({
        'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1
    })

    push_notebook()
    sleep(.1)
