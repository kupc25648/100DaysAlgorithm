'''
When you write down a positive integer as binary number, how many 1s do you get? For example,

99 = 0b1100011

An obvious solution would be to take a single-bit mask, walk over the number X & (1 << k) and count non-zero results up. But this solution counts both 0s and 1s.
Can you do better by only counting 1s and completely ignoring 0s? There’s a ton of beautiful and surprising bit-tricks you can do. Too bad we don’t need them any more.

ps x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
'''

def count_of_1bits(bitvalue):
    n = 0
    while bitvalue:
        bitvalue &= bitvalue-1
        n+=1
    return n

print(count_of_1bits(0b11001100))






