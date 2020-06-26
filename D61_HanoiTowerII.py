'''
Let’s solve Hanoi tower once again. Unlike day 1, the problem is slightly different today.
In an optimal game (with the least number of moves), find how many moves have been played given towers’ configuration. And conversely, given towers’ configuration find how many moves have been played.
The key observation here is the number of moves in optimal game. For 1 disk, it’s 1 move. For n disks, it’s 2^n — 1 moves. This can be proved by induction.
Solving n-disk game, transfer n-1 disks to auxiliary rod, move the largest disk and transfer n-1 disks from auxiliary to target rod. Following the induction.

The proof also gives a direct solution to the problem. In n-disk game, the largest disk is transferred exactly on move 2^(n-1)! After a single check on moves >= 2 ** (n-1) we immediately know where the largest disk is. And we can proceed recursively on a n-1-disk game.
Regarding to this problem, I’d like to talk a bit about algorithmization. Similar to mathematics, algorithms are not lonely islands, but I’ve seen teachers, books and articles that pretend they are.
A good programmer is not a living library of algorithms. Not at all. A good programmer is aware of the interconnections and should be able to use them to improve and adapt the implementation for the current situation.
On day 54 I said, “Do not make the best solution. Do the solution you need.” There is no best solution. The law of conservation of energy applies to algorithms, too.
You can make trade-offs — memory for speed, speed for effort, effort for readability… And there is no single number to be measured. In every single problem you solve, you have to state your own measure and write the solution that is the best one at the moment.
This algorithm proves that the state of optimal game can be uniquely encoded as a sequence of integers. While somewhat obvious observation, there’s a strong relation to Huffman code and Hamming code.
As a consequence, state of n-disk game can be represented using n bits of memory, and conversely, n bits is the least amount we need for representation. This relates to day 47 and information representation.
If you would like to send a secret message to your friend, you might use Hanoi tower! Just encode your message into the game configuration. It’s called steganography and until age of modern cryptography it was widely used mechanism.
It is worth of mentioning that my friend solved this problem in school. He observed that disk position follows certain congruences and came up with a completely different solution. That makes another relation.
The next time you are asked to write a solution for Hanoi tower problem, here is one you should understand now. And I think it’s a good one.
'''

# Algorithm
def get_rods(move, towers, left, middle, right):
    if towers:
        if (move<<1) & (1<<towers):
            right.append(towers)
            get_rods(move,towers-1,middle,left,right)
        else:
            left.append(towers)
            get_rods(move,towers-1,left,right,middle)

def get_move(towers, left, middle, right):
    if not towers:
        return 0
    if not left or right and left[0] < right[0]:
        move = 1 <<(towers-1)
        return move+get_move(towers-1, middle,left, right[1:])
    else:
        return get_move(towers-1, left[1:], right, middle)

def hanoi(towers):
    for i in range(2**towers):
        rods = [],[],[]
        get_rods(i,towers,*rods)
        move = get_move(towers, *rods)
        print('{:2} moves == {} {} {}'.format(move,*rods))

# RUN

hanoi(15)
