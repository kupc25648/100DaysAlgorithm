'''
Aho-Corasick is a string searching algorithm running in linear time and my heart would be broken if I missed this one in the series.
I already spent a day on string searching, so what’s the difference to day 29? Aho-Corasick uses a finite state automaton to search for a whole set of patterns at once while holding linearity condition regardless of the set size.
There are two parts you have to implement, FSA construction and searching. I definitely recommend to study the FSA construction through. Years ago I attended a competition and adaptation of Aho-Corasick with carefully designed FSA proved to be many times faster than any other solution and helped me to win.
https://github.com/coells/100days

'''
from collections import deque, defaultdict
from itertools import count

# Algorithm
def aho_corasick():
    G = defaultdict(count(1).__next__)  # transition
    W = defaultdict(set)                # alphabet
    F = defaultdict(lambda: 0)          # fallbacks
    O = defaultdict(set)                # output

    # automation
    return G, W, F, O

def add_word(word, G, W, F, O):
    state = 0

    # add transition between states
    for w in word:
        W[state].add(w)
        state = G[state,w]

    # add output
    O[state].add(word)

def build_fsa(G, W, F, O):
    # initial states
    queue = deque(G[0,w] for w in W[0])

    while queue:
        state = queue.popleft()

        # for each letter in alphabet
        for w in W[state]:
            # find fallback state
            t = F[state]
            while t and (t,w) not in G:
                t =F[t]

            # for next state define its fallback and output
            s = G[state, w]
            F[s] = G[t,w] if (t,w) in G else 0
            O[s] |= O[F[s]]

            queue.append(s)

def search(text, G, W, F, O):
    state = 0

    for i,t in enumerate(text):
        # fallback
        while state and (state, t) not in G:
            state = F[state]

        # transition
        state = G[state,t] if (state, t) in G else 0

        # output
        if O[state]:
            print('@', i ,O[state])

# Run
AC = aho_corasick()
add_word('bar', *AC)
add_word('ara', *AC)
add_word('bara', *AC)
add_word('barbara', *AC)
build_fsa(*AC)

search('barbarian barbara said: barabum', *AC)
