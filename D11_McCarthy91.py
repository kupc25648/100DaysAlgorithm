'''
Our today’s guest is very special. No doubt it is one of the most useless functions ever, yet, the most profound for causing nightmares of computer science students.
What does is do? When you plug a natural number N in, McCarthy91 flushes N-10 out, if N is larger than 100. Otherwise it always returns 91.
Why should anybody have nightmares? Well, this function is being used as a study case for formal verification. In other words, you don’t have to implement it, you have to prove it is correct and finite, instead.

'''
def mccarthy91(n):
    k =1
    while k:
        if n > 100:
            n -= 10
            k -= 1

        else:
            n += 11
            k += 1

    return n

def mccarthy91_rec(n):
    if n >100:
        return n - 10

    else:
        return mccarthy91_rec(mccarthy91_rec(n+11))




print(mccarthy91(80))
