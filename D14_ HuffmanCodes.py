'''
For many years the Huffman coding was state of the art in statistical data compression. Even though it should be noted that the main reason probably was that arithmetic coding was patented.
The idea is very similar to one of Samuel Morse, to create a sparse representation of the data.
Unlike Morse code, Huffman codes have unique prefixes which removes the need for separator and resulting stream has only one way of decoding. Disadvantage is that any error in a single bit can easily break the remaining part of the message.


ps In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression.

https://en.wikipedia.org/wiki/Huffman_coding
'''

import collections


def find_min(freq):
    item = min(freq, key=lambda i:i[0])
    freq.remove(item)
    return item

def print_codes(tree, prefix=''):
    if isinstance(tree, tuple):
        print_codes(tree[0], prefix+'0')
        print_codes(tree[1], prefix+'1')
    else:
        print(tree, prefix)

def huffman_codes(text):
    freq = [(i,x) for x,i in collections.Counter(text).items()]

    while len(freq) > 1:
        li, lx =find_min(freq)
        ri, rx =find_min(freq)
        freq.append((li+ri,(lx,rx)))

    print_codes(freq.pop()[1])



huffman_codes('Hello')
