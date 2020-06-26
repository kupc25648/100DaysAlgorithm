'''
I have prepared something cool today. Let’s implement a program with [a simple] artificial intelligence.
The task that the program has to learn is a game called simple Nim. There are two players who alternately take 1, 2 or 3 objects from a heap and the player who takes the last object wins.
Remember game theory? For any finite deterministic game of two players and without draws there exists a winning strategy for one of the players. Can you find the strategy on your own?
There are many definitions of what intelligence is or what artificial intelligence should be [and nobody actually knows]. Intuitively, we would expect the program to learn from an experience and gradually improve its performance.
However, rather counter-intuitive is a fact that to simulate human behaviour and/or human skills we only need very little of statistics. People often refuse to accept that humans would be so simple. And humans are not simple, but their behaviour very often is.
To implement AI player, let’s set the following rules.
For each size of the heap keep the total number of wins per objects taken. For example, when heap size is 20, remember that player won 100x when took 1 object, won 200x when took 2 objects, and won 1x when took 3 objects.
In the next game randomize each move. In the example above, player should take 1 object with probability 100/(100+200+1), take 2 objects with probability 200/301, and take 3 objects with probability 1/301.
When the player wins the game, increase number of wins at each move played.
When the player looses the game, increase number of wins for the two alternative moves.
The code below does exactly what I have just described. When class Player is called to play, it takes the current distribution for the heap size and randomizes move. After the game has finished, method learn updates distributions based on the learning rules (3) and (4).
The rule (3) is crystal clear, player won. The rule (4) allows the player to learn even from the loss. There is also a dirty trick [called normalization] I use to speed the learning up, but it’s the least important part of the code.
What happens if we let the AI player learn through 100.000 games against different opponents?
expert opponent
The opponent knows and plays the winning strategy. If there is none, she randomizes move. [While this might look as the best strategy, it’s not — can you find a better strategy based on the examples I provided?]
10000 games, W/L ratio 0.0081
20000 games, W/L ratio 0.0138
30000 games, W/L ratio 0.012
40000 games, W/L ratio 0.0344
50000 games, W/L ratio 0.0386
60000 games, W/L ratio 0.1356
70000 games, W/L ratio 0.4653
80000 games, W/L ratio 0.4978
90000 games, W/L ratio 0.4988
100000 games, W/L ratio 0.4995
You can see via win/loose ratio the AI gradually improves its performance. In the last 10.000 games AI won almost exactly half of the games.

Check what AI thinks about the game. X-axis contains heap size and y-axis contains probability distribution. E.g. when the heap size is 5, AI will almost always take 1 object. For the heaps where it can’t win the distribution is almost uniform [and it’s not just because of a dirty trick I do to speed the learning up], hence AI has no preference.
random opponent
The opponent simply takes random number of objects without thinking.
10000 games, W/L ratio 0.8735
20000 games, W/L ratio 0.9495
30000 games, W/L ratio 0.959
40000 games, W/L ratio 0.9597
50000 games, W/L ratio 0.96
60000 games, W/L ratio 0.9678
70000 games, W/L ratio 0.962
80000 games, W/L ratio 0.9656
90000 games, W/L ratio 0.9654
100000 games, W/L ratio 0.9639
AI crushed the opponent, even though there’s a non-negligible chance to win the game even if you simply guess.

What AI thinks about the game know? It’s not surprising to see much wider distributions. That’s because AI learns from wins and the larger the heap is, the higher was the chance to win regardless of what was played.
take-3 opponent
What about the opponent that always takes 3 objects?
10000 games, W/L ratio 0.9743
20000 games, W/L ratio 0.9979
30000 games, W/L ratio 0.9991
40000 games, W/L ratio 0.999
50000 games, W/L ratio 0.9996
60000 games, W/L ratio 1.0
70000 games, W/L ratio 0.9999
80000 games, W/L ratio 1.0
90000 games, W/L ratio 1.0
100000 games, W/L ratio 1.0
A decisive victory! This is clearly very bad strategy without any chance on random win.

Look at the chart when the heap size is 6, AI takes 1 or 2 objects with an equal chance. Both moves lead to a quick win so it doesn’t really matter. But the move is not deterministic which complicates identification of AI’s strategy.
That seems to be very close to how humans think. The program doesn’t think, but it is still able to simulate human-like behaviour.
The AI player knows nothing about the game. It only deploys statistics to adapt to a strategy of its opponent. While it’s probably not what you might imagine under term artificial intelligence, it’s exactly how it works.
And here’s what you can do. Download the notebook, examine my code and write your own opponent. Then let the AI to discover weak points of your strategy.

https://medium.com/100-days-of-algorithms/day-90-simple-nim-ai-864b2fdf9e8a
'''
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_notebook

# Player AI
class Player:
    def __init__(self, heap):
        self.history = {}
        self.distribution = np.ones((heap + 1,3), dtype=int)
        self.cutoff =1000

    def __call__(self,heap):
        # randomize move based on previous game
        dist = self.distribution[heap].cumsum()
        rnd = np.random.randint(dist[2])
        move = 1 if rnd < dist[0] else 2 if rnd < dist[1] else 3

        # store move in history
        self.history[heap] = min(heap, move)

        return self.history[heap]

    def learn(self, winner):
        # update move distribution
        for heap, move in self.history.items():
            if winner is self:
                self.distribution[heap][move-1] += 1
            else:
                self.distribution[heap][move-1] -= 1
                self.distribution[heap] += 1

        # normalize distribution to speed learning up
        normalize = np.argwhere(self.distribution.sum(axis=1) > self.cutoff)
        for heap in normalize:
            self.distribution[heap] -= self.distribution[heap].min()-1

        # reset game history
        self.history = {}

    def strategy(self):
        distribution = self.distribution[1:]
        return distribution.T/distribution.sum(axis=1)

# Opponent
def expert_opponent(heap):
    return heap%4 or min(heap, np.random.randint(1,4))
def random_opponent(heap):
    return min(heap, np.random.randint(1,4))
def take_n_opponent(heap):
    return lambda heap: min(heap, take)

# Trainning
def play(heap, player, opponent):
    players = player, opponent
    wins = 0

    for game in range(100001):
        # update plot periodically
        if game % 10000 == 0:
            print(game, 'games, W/L ratio', wins / 10000)
            wins = 0

        # a single game
        h = heap
        while h:
            h -= players[0](h)
            players = players[1], players[0]

        winner = players[1]
        wins += winner is player

        # let player learn
        player.learn(winner)

    # plot distribution
    plot_strategy(heap, player)

def plot_strategy(heap, player):
    # data
    take_1, take_2, take_3 = player.strategy()
    take_2 += take_1
    take_3 += take_2
    kwargs = {'x': range(1, heap+1),'width': .8}

    # plot
    plot = figure(plot_width = 600, plot_height = 400)
    plot.vbar(**kwargs, bottom=0, top=take_1, legend='take 1', color='#a44444')
    plot.vbar(**kwargs, bottom=take_1, top=take_2, legend='take 2', color='#88a888')
    plot.vbar(**kwargs, bottom=take_2, top=take_3, legend='take 3', color='#ccccac')
    show(plot)

# Learning
HEAP =21
play(HEAP, Player(HEAP), expert_opponent)
#play(HEAP, Player(HEAP), take_n_opponent(1))
#play(HEAP, Player(HEAP), take_n_opponent(3))
