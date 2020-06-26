'''
I used to play this game as a kid and never won as far as I can remember. Writing a program to guess the secret and to make computer play against itself is the least satisfaction.
If you ever come to conclusion there’s only a little to study on this problem, read The Art of Computer Programming. In Knuth’s hands can even the smallest problem turn into surprisingly difficult consequences.
'''
from random import choice, sample
from itertools import permutations

# Algorithm
def score(x,y):
    bulls = sum(i==j for i,j in zip(x,y))
    cows = len(set(x) & set(y)) - bulls
    return bulls, cows
def player1(player2):
    secret = sample(range(10),4)

    tip = next(player2)
    while True:
        b,c = score(secret, tip)
        if b <4:
            print(b, 'bulls',c, 'cows')
            tip = player2.send((b,c))
        else:
            print('you won')
            break

def player2():
    tips = list(permutations(range(10),4))

    while True:
        tip = choice(tips)
        print(tip,'?')
        bc = yield tip
        tips = [i for i in tips if score(i,tip) == bc]

player1(player2())

# Run

