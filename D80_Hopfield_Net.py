'''
Hopfield net is a kind of neural network with binary threshold units and recurrent connections. The connections are symmetric and the model has a global energy function which results in a surprisingly simple training algorithm.
I’m not going to dive deep into Hopfield nets. Instead, let me show a little intuition using a small example.
This model was pre-trained to store a memory 011. We set its units to values 110 and will track the energy function.

E = -(-1*1*1 + -1*1*0 + 1*1*0) = 1
If two units are active, the weight of their connection is subtracted from the global energy.

E = -(-1*1*0 + -1*0*0 + 1*1*0) = 0
After flipping the top unit, global energy decreased which is a good thing.

E = -(-1*1*0 + -1*1*0 + 1*1*1) = -1
After another flipping of the bottom right unit, energy decreased, again. The system is at its global energy minimum. This minimum represents a previously stored memory 011.
Hopfield net is able to reconstruct a full information from a portion of it. If you look at the examples below, three memories are stored into Hopfield net. These vectors are later fully reconstructed from just a few bits.

https://medium.com/100-days-of-algorithms/day-80-hopfield-net-5f18d3dbf6e6
'''

import numpy as np

# Algorithm
def hopfield_net(n):
    weights = np.zeros((n,n), dtype= int)

    def _store(data):
        nonlocal weights

        vector = np.array(data, dtype=int)*2 -1
        weights += np.outer(vector, vector) - np.eye(len(data), dtype = int)

    def _reconstruct(data):
        visible = np.array(data, dtype= int)

        while True:
            for i, v in np.ndenumerate(visible):
                visible[i] = weights[i] @ visible >= 0

            hidden = weights @ visible >= 0
            if np.all(hidden ==  visible):
                return visible


    return _store, _reconstruct


# Run
store, reconstruct = hopfield_net(25)

# Memories
store([
    1,0,0,0,1,
    0,1,0,1,0,
    0,0,1,0,0,
    0,1,0,1,0,
    1,0,0,0,1,
])
store([
    1,1,1,1,1,
    1,0,0,0,1,
    1,0,0,0,1,
    1,0,0,0,1,
    1,1,1,1,1,
])
store([
    0,0,1,0,0,
    0,0,1,0,0,
    1,1,1,1,1,
    0,0,1,0,0,
    0,0,1,0,0,
])
# reconstruct
reconstruct([
    1,1,1,1,1,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
]).reshape(5, 5)
np.array([[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]])
reconstruct([
    1,0,0,0,0,
    0,1,0,0,0,
    0,0,1,0,0,
    0,0,0,1,0,
    0,0,0,0,1,
]).reshape(5, 5)
np.array([[1, 0, 0, 0, 1],
       [0, 1, 0, 1, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 0, 0, 1]])
