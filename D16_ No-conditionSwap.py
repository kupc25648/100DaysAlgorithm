'''
Another piece from a bit-trick family. How to swap two integers if you can’t use any condition?
It is not an algorithm for daily use. The idea is rather proof of concept that it is indeed possible. Similar tricks are used by compiler during code optimizations to spare few more ticks of CPU time.
'''

def swap(x,y):
    # s as boolian : True in boolian == 1
    s = x < y

    return x*s + y * (1-s), y * s + x*(1-s)



print(swap(3, 15), swap(15, 3))
