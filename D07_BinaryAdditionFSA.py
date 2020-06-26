'''
Adding two binary numbers can be done the same way you were taught at school, just remember that 1+1=10 and follow the manual.
There’s a lot to say about this seemingly simple arithmetics, for example you can take a look at parallel adder implementation where things get a bit more interesting.
I’ve decided to use serial implementation via finite state automaton. There are 4 states based on combination of output 0/1 and carry 0/1 and set of transitions based on input bits.
The thing is … do we need 4 states? It is actually possible to use only 3 states, can you find out how?

about FSA https://en.wikipedia.org/wiki/Finite-state_machine



'''

import itertools


#   states
p0c0 = 0 , {}
p1c0 = 1 , {}
p0c1 = 0 , {}
p1c1 = 1 , {}

#   transitions between states
p0c0[1].update({(0, 0): p0c0, (1, 0): p1c0,
                (0, 1): p1c0, (1, 1): p0c1})

p1c0[1].update({(0, 0): p0c0, (1, 0): p1c0,
                (0, 1): p1c0, (1, 1): p0c1})

p0c1[1].update({(0, 0): p1c0, (1, 0): p0c1,
                (0, 1): p0c1, (1, 1): p1c1})

p1c1[1].update({(0, 0): p1c0, (1, 0): p0c1,
                (0, 1): p0c1, (1, 1): p1c1})

def add(x,y):
    x = map(int, reversed(x))
    y = map(int, reversed(y))
    z =[]

    # simulate automaton
    value, transition = p0c0
    for r,s in itertools.zip_longest(x,y, fillvalue = 0):
        value, transition = transition[r,s]
        z.append(value)

    # handle carry
    z.append(transition[0,0][0])

    return ''.join(map(str, reversed(z)))

# Test
print(add('1100100100100', '100100011000'))





