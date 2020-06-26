'''
Some time ago a friend of mine asked me to help him with this problem.
Playing Monopoly, what is the probability that you step at position #24 during the first round?
Law of total probability says that the chance to step on certain position is sum of disjoint events of how we could get there. In this case, we get at #24 if we tossed 1 while standing at #23, or we tossed 2 while standing at #22, … or we tossed 6 while standing at #18. This leads to a recursive formula.

https://miro.medium.com/max/976/1*mtkLOY6Ek-_jRwl-RIk5lQ.png

It looks quite familiar, doesn’t it? Right, Fibonacci numbers. Strategy to choose? Dynamic programming.

'''
import matplotlib.pyplot as plt
# n =  position in monopoly game board
def probability(n):
    # initial probabilities
    p = [ 0, 0 ,0 ,0 ,0 ,1]

    # next field is conditioned on previous six fileds
    for _ in range(n):
        p.append(sum(p[-6:])/6)

    return p[6:]


print(probability(24))

plt.plot(probability(24))

plt.show()


